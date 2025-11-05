## jsc

> `/System/iOSSupport/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc`

```diff

-620.2.4.11.6
-  __TEXT.__text: 0x35138
-  __TEXT.__auth_stubs: 0x1720
-  __TEXT.__const: 0x210
-  __TEXT.__cstring: 0x574c
-  __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__auth_got: 0xb90
+621.1.15.11.10
+  __TEXT.__text: 0x36be4
+  __TEXT.__auth_stubs: 0x1770
+  __TEXT.__const: 0x218
+  __TEXT.__cstring: 0x5c61
+  __DATA_CONST.__auth_got: 0xbb8
   __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x17c8
+  __DATA_CONST.__const: 0x17e8
   __DATA_CONST.__jsc_ops: 0x0
   __DATA.__data: 0x8
-  __DATA.__bss: 0xa8
+  __DATA.__bss: 0xb0
   - /System/iOSSupport/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/JavaScriptCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libedit.3.dylib
-  UUID: 6141A241-0137-3131-909F-8EDA977214B8
-  Functions: 327
-  Symbols:   421
-  CStrings:  799
+  UUID: DF889C27-BBEC-3315-996E-950E594D74BE
+  Functions: 324
+  Symbols:   426
+  CStrings:  825
 
Symbols:
+ __ZN3JSC17DeferredWorkTimer14addPendingWorkENS0_8WorkTypeERNS_2VMEPNS_8JSObjectEON3WTF6VectorIPNS_6JSCellELm0ENS6_15CrashOnOverflowELm16ENS6_10FastMallocEEE
+ __ZN3JSC19HeapSnapshotBuilderC1ERNS_12HeapProfilerENS0_12SnapshotTypeEN3WTF14OverflowPolicyE
+ __ZN3JSC19JSWebAssemblyMemory6createERNS_2VMEPNS_9StructureE
+ __ZN3JSC27retrieveTypeImportAttributeEPNS_14JSGlobalObjectERKN3WTF7HashMapINS2_6RefPtrINS2_17UniquedStringImplENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEENS2_6StringENS2_11DefaultHashISA_EENS2_10HashTraitsISA_EENSE_ISB_EENS2_15HashTableTraitsELNS2_17ShouldValidateKeyE0EEE
+ __ZN3JSC28WebAssemblyMemoryConstructor26createMemoryFromDescriptorEPNS_14JSGlobalObjectEPNS_9StructureEPNS_8JSObjectENSt3__18optionalINS_10MemoryModeEEE
+ __ZN3WTF14forceEnablePGMEt
+ __ZN3WTF6Thread20initializeCurrentTLSEv
+ __ZN7bmalloc3api23tzoneAllocateNonCompactEPv
+ __ZN7bmalloc3api27tzoneAllocateNonCompactSlowEmRKNS0_18TZoneSpecificationE
+ __ZN7bmalloc3api9tzoneFreeEPv
+ __ZNK3JSC12CachePayload4spanEv
+ __ZNK3WTF17StringPrintStream8toStringEv
+ __ZNK3WTF17StringPrintStream9toCStringEv
- __ZN3JSC17DeferredWorkTimer14addPendingWorkENS0_8WorkTypeERNS_2VMEPNS_8JSObjectEON3WTF6VectorINS_4WeakINS_6JSCellEEELm0ENS6_15CrashOnOverflowELm16ENS6_10FastMallocEEE
- __ZN3JSC19HeapSnapshotBuilderC1ERNS_12HeapProfilerENS0_12SnapshotTypeE
- __ZN3JSC19JSWebAssemblyMemory9tryCreateEPNS_14JSGlobalObjectERNS_2VMEPNS_9StructureE
- __ZN3JSC27retrieveTypeImportAttributeEPNS_14JSGlobalObjectERKN3WTF7HashMapINS2_6RefPtrINS2_17UniquedStringImplENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEENS2_6StringENS2_11DefaultHashISA_EENS2_10HashTraitsISA_EENSE_ISB_EENS2_15HashTableTraitsEEE
- __ZN3WTF14forceEnablePGMEv
- __ZN3WTF17StringPrintStream8toStringEv
- __ZN3WTF17StringPrintStream9toCStringEv
- __ZNK3JSC12CachePayload4sizeEv
CStrings:
+ "\"use strict\";\n"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/System/iOSSupport/usr/local/include/wtf/MemoryPressureHandler.h"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/System/iOSSupport/usr/local/include/wtf/RefCounted.h"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/System/iOSSupport/usr/local/include/wtf/ThreadSpecific.h"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/System/iOSSupport/usr/local/include/wtf/text/StringConcatenate.h"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/JavaScriptCore_iosmac/Source/JavaScriptCore/heap/AbstractSlotVisitorInlines.h"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/JavaScriptCore_iosmac/Source/JavaScriptCore/jsc.cpp"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/JavaScriptCore_iosmac/Source/JavaScriptCore/runtime/DisallowVMEntry.h"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/JavaScriptCore_iosmac/Source/JavaScriptCore/runtime/ExceptionScope.h"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/JavaScriptCore_iosmac/Source/JavaScriptCore/runtime/IndexingHeader.h"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/JavaScriptCore_iosmac/Source/JavaScriptCore/runtime/JSObject.h"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/JavaScriptCore_iosmac/Source/JavaScriptCore/runtime/JSObjectInlines.h"
+ "BoundsChecking"
+ "Could not open file: "
+ "Error when parsing file name: %s\n"
+ "Expected 'binary' or 'caller relative' as second argument."
+ "Signaling"
+ "WTF::RefCountedBase::~RefCountedBase()"
+ "WTF::StringTypeAdapter<std::span<const unsigned char>>::StringTypeAdapter(std::span<CharacterType, Extent>)"
+ "allocationProfilingMode"
+ "createWebAssemblyMemoryWithMode"
+ "createWebAssemblyMemoryWithMode expects either 'BoundsChecking' or 'Signaling' as the second argument."
+ "createWebAssemblyMemoryWithMode expects the first argument to be an object"
+ "createWebAssemblyMemoryWithMode should only be called if the useWebAssembly option is set"
+ "dumpHeapOnLowMemory"
+ "enableStrongRefTracker"
+ "freeRetiredWasmCode"
+ "heapGrowthFunctionThresholdInMB"
+ "heapGrowthMaxIncrease"
+ "heapGrowthSteepnessFactor"
+ "libpasForcePGMWithRate"
+ "markedBlockDumpInfoCount"
+ "maxLoopUnrollingBodyNodeSize"
+ "maxLoopUnrollingCount"
+ "maxLoopUnrollingIterationCount"
+ "maxRegExpStackSize"
+ "maximumOMGCandidateCost"
+ "printEachUnrolledLoop"
+ "traceWasmLLIntExecution"
+ "useAtomicsPause"
+ "useErrorIsError"
+ "useImportDefer"
+ "useIteratorChunking"
+ "useIteratorSequencing"
+ "useJSONSourceTextAccess"
+ "useLoopUnrolling"
+ "useMapGetOrInsert"
+ "useMathSumPreciseMethod"
+ "useMoreCurrencyDisplayChoices"
+ "useOMGInlining"
+ "validateVMEntryCalleeSaves"
+ "verboseLoopUnrolling"
+ "zeroExecutableMemoryOnFree"
- "--"
- "-d"
- "-e"
- "-f"
- "-h"
- "-i"
- "-m"
- "-p"
- "-s"
- "-x"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/System/iOSSupport/usr/local/include/wtf/MemoryPressureHandler.h"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/System/iOSSupport/usr/local/include/wtf/ThreadSpecific.h"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/System/iOSSupport/usr/local/include/wtf/text/StringConcatenate.h"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/JavaScriptCore_iosmac/Source/JavaScriptCore/heap/AbstractSlotVisitorInlines.h"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/JavaScriptCore_iosmac/Source/JavaScriptCore/jsc.cpp"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/JavaScriptCore_iosmac/Source/JavaScriptCore/runtime/DisallowVMEntry.h"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/JavaScriptCore_iosmac/Source/JavaScriptCore/runtime/ExceptionScope.h"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/JavaScriptCore_iosmac/Source/JavaScriptCore/runtime/IndexingHeader.h"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/JavaScriptCore_iosmac/Source/JavaScriptCore/runtime/JSObject.h"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/JavaScriptCore_iosmac/Source/JavaScriptCore/runtime/JSObjectInlines.h"
- "Expected 'binary' as second argument."
- "unsigned int WTF::stringLength(size_t)"
- "useWasmGC"
- "useWasmJITLessJSEntrypoint"
- "wasmIPIntTiersUpToBBQ"
- "wasmIPIntTiersUpToOMG"
- "wasmLLIntTiersUpToBBQ"

```
