## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

```diff

-64567.3.3.0.0
-  __TEXT.__text: 0xa79bc
-  __TEXT.__auth_stubs: 0x1fc0
-  __TEXT.__objc_methlist: 0x5d4c
+64570.56.1.0.0
+  __TEXT.__text: 0xaaeac
+  __TEXT.__auth_stubs: 0x2190
+  __TEXT.__objc_methlist: 0x6408
   __TEXT.__const: 0x1c0
-  __TEXT.__cstring: 0xf136
-  __TEXT.__gcc_except_tab: 0x4c5c
-  __TEXT.__oslogstring: 0x160a
+  __TEXT.__cstring: 0xfa20
+  __TEXT.__gcc_except_tab: 0x4f28
+  __TEXT.__oslogstring: 0x1614
   __TEXT.__ustring: 0x24
-  __TEXT.__unwind_info: 0x26e0
-  __TEXT.__objc_classname: 0x7df
-  __TEXT.__objc_methname: 0xe8f5
-  __TEXT.__objc_methtype: 0x82f9
-  __TEXT.__objc_stubs: 0x9500
-  __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x3398
-  __DATA_CONST.__objc_classlist: 0x2a8
+  __TEXT.__unwind_info: 0x2800
+  __TEXT.__objc_classname: 0x81d
+  __TEXT.__objc_methname: 0xf160
+  __TEXT.__objc_methtype: 0x85e5
+  __TEXT.__objc_stubs: 0x9720
+  __DATA_CONST.__got: 0x430
+  __DATA_CONST.__const: 0x3638
+  __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x32f0
-  __DATA_CONST.__objc_superrefs: 0x1e8
-  __DATA_CONST.__objc_arraydata: 0x718
-  __AUTH_CONST.__auth_got: 0xff8
-  __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0xaa8
-  __AUTH_CONST.__cfstring: 0xc6a0
-  __AUTH_CONST.__objc_const: 0xbf38
-  __AUTH_CONST.__objc_arrayobj: 0x108
+  __DATA_CONST.__objc_selrefs: 0x3478
+  __DATA_CONST.__objc_superrefs: 0x1f8
+  __DATA_CONST.__objc_arraydata: 0x870
+  __AUTH_CONST.__auth_got: 0x10e0
+  __AUTH_CONST.__auth_ptr: 0x28
+  __AUTH_CONST.__const: 0xb88
+  __AUTH_CONST.__cfstring: 0xd3e0
+  __AUTH_CONST.__objc_const: 0xb9e0
+  __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x230
+  __AUTH.__objc_data: 0x2d0
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0xc24
+  __DATA.__objc_ivar: 0xc58
   __DATA.__data: 0xce8
-  __DATA.__bss: 0x530
-  __DATA.__common: 0x9
+  __DATA.__bss: 0x550
+  __DATA.__common: 0xf1
   __DATA_DIRTY.__objc_data: 0x1860
   __DATA_DIRTY.__crash_info: 0x40
-  __DATA_DIRTY.__bss: 0xd0
+  __DATA_DIRTY.__bss: 0xd8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
+  - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication
   - /System/Library/PrivateFrameworks/MallocStackLogging.framework/MallocStackLogging
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2869
-  Symbols:   3745
-  CStrings:  5748
+  Functions: 2982
+  Symbols:   3953
+  CStrings:  5933
 
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
+ __xpc_error_connection_invalid
+ __xpc_type_connection
+ _csops_audittoken
+ _dispatch_activate
+ _dispatch_data_create
+ _dispatch_group_create
+ _dispatch_mach_create
+ _dispatch_mach_msg_create
+ _mapped_memory_pointer_to_local_mapping_updated_with_extra_bits
+ _nw_array_create
+ _nw_frame_create
+ _objc_allocateProtocol
+ _objc_opt_self
+ _objc_retain_x11
+ _objc_retain_x13
+ _os_transaction_create
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
- _OBJC_CLASS_$_NSValue
- _access
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
+ " for ACTIVE TRANSACTION with"
+ "%s gave { .name = \"%s\", .Offset = %u, .Kind = %s, .TR = { .Typeref = %p (type %s) } }\n"
+ "%s%s\n"
+ "%u block%s  %s bytes"
+ "*** Symbolication:  malloc zone address %#llx is invalid\n"
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
- "Request/Reply message for active transaction with "
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
- "{NSSliceFields}"

```
