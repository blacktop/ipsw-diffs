## Espresso

> `/System/Library/PrivateFrameworks/Espresso.framework/Espresso`

```diff

-  __TEXT.__text: 0xd19bd0
+  __TEXT.__text: 0xd1bacc
   __TEXT.__objc_methlist: 0x322c
   __TEXT.__const: 0x5e8e2
-  __TEXT.__cstring: 0x54021
-  __TEXT.__gcc_except_tab: 0xce2f8
-  __TEXT.__oslogstring: 0x7b2a
-  __TEXT.__unwind_info: 0x2c4f8
+  __TEXT.__cstring: 0x53eb1
+  __TEXT.__gcc_except_tab: 0xce758
+  __TEXT.__oslogstring: 0x8a69
+  __TEXT.__unwind_info: 0x2c5b8
   __TEXT.__eh_frame: 0x4b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0x24e8
   __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0x298
-  __DATA_CONST.__got: 0xa80
+  __DATA_CONST.__got: 0xa98
   __AUTH_CONST.__const: 0x9f1f0
   __AUTH_CONST.__cfstring: 0xa100
   __AUTH_CONST.__objc_const: 0x8b90

   __AUTH.__thread_bss: 0x400
   __DATA.__objc_ivar: 0x5b8
   __DATA.__data: 0x4c8
-  __DATA.__bss: 0x6790
+  __DATA.__bss: 0x6770
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x90
-  __DATA_DIRTY.__bss: 0x2b8
+  __DATA_DIRTY.__bss: 0x2d8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 34654
-  Symbols:   87639
-  CStrings:  11685
+  Functions: 34701
+  Symbols:   87645
+  CStrings:  11741
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __AUTH.__thread_vars : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ __ZN4E5RT14E5CompilerImpl27PurgeE5BundlesForInputModelINSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvRKT_
+ __ZN4E5RT14E5CompilerImpl7CompileINSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEENS2_10unique_ptrINS_14ProgramLibraryENS2_14default_deleteISA_EEEERKT_RKNS_17E5CompilerOptionsE
+ __ZNK4E5RT14E5CompilerImpl12GetModelLockERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZNSt3__15tupleIJbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN4E5RT14ProgramLibraryENS_14default_deleteIS9_EEEEEED1Ev
- __ZNSt3__15tupleIJbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN4E5RT14ProgramLibraryENS_14default_deleteIS9_EEEEEED2Ev
CStrings:
+ "3600.52.2"
+ "Closed ANEDevice = 0x%lx\n"
+ "Created E5BundleCache at %s\n"
+ "Customized E5 bundle location \n"
+ "Detected ANE Inference overflow during async execution."
+ "Detected ANE Inference overflow."
+ "Detected call to mapIOSurfacesWithModel on VM run. Ignore return result as this API is not supported on VM."
+ "Detected rank mistmatch between E5 and EIR. Input = %s, E5 rank = %s, EIR rank = %s. Skipped checking shape mistmatch."
+ "Detected shape mistmatch between E5 and EIR. Input = %s, dim = %s, E5 = %s, EIR = %s. EIR will be reshaped to match E5 shape."
+ "E5BundleCache IsNewCompileRequired: input=%s forceRecompile=True\n"
+ "E5BundleCache Lookup: input=%s output=%s exists=%d\n"
+ "E5BundleCache exists at %s\n"
+ "E5BundleCacheManager: GlobalCacheDirectory %s\n"
+ "E5BundleCacheManager: is root user\n"
+ "E5BundleCacheManager::MarkAsMobileOwned: path = %s\n"
+ "E5BundleCacheManager::MarkAsMobileOwned: path = %s. Unable to query grp for mobile.\n"
+ "E5BundleCacheManager::MarkAsMobileOwned: path = %s. Unable to query pwd for mobile.\n"
+ "E5BundleCacheManager::MarkAsMobileOwnedRecursive: path = %s failed with errno = %i \n"
+ "E5CompilerImpl:: processInfo is nil.\n"
+ "E5CompilerImpl::Compile acquiring global lock input=%s\n"
+ "E5CompilerImpl::Compile acquiring per-model lock input=%s\n"
+ "E5CompilerImpl::Compile fast-path cache hit input=%s\n"
+ "E5CompilerImpl::Compile(MIL, !CreateProtectedAssets) acquiring global lock input=%s\n"
+ "E5CompilerImpl::Compile(MIL, !CreateProtectedAssets) acquiring per-model lock input=%s\n"
+ "E5CompilerImpl::Compile(MIL, !CreateProtectedAssets) fast-path cache hit input=%s\n"
+ "E5CompilerImpl::Compile(MIL, CreateProtectedAssets) acquiring global lock input=%s\n"
+ "E5CompilerImpl::Compile(MIL, CreateProtectedAssets) acquiring per-model lock input=%s\n"
+ "E5CompilerImpl::Compile(MIL, CreateProtectedAssets) fast-path cache hit input=%s\n"
+ "E5CompilerImpl::CompileInternal::performCompilation input=%s output=%s tmp-output=%s\n"
+ "E5CompilerImpl::CompileInternal::performCompilation renamed %s to %s\n"
+ "E5CompilerImpl::GetModelLock key=%s stripe=%zu\n"
+ "E5CompilerImpl::IsNewCompileRequired acquiring per-model lock input=%s\n"
+ "E5CompilerImpl::PurgeE5BundlesForInputModel acquiring per-model lock input=%s\n"
+ "E5CompilerImpl::PurgeE5BundlesForInputModel(MIL) acquiring per-model locks milFastHash=%s milHash=%s\n"
+ "E5MLExecutionStreamSyncTelemetry"
+ "Espresso.e5ml.trace: serializing IO ports to tmp dir: %s"
+ "Loaded ANE Model at path = %s with programHandle = 0x%llx\n"
+ "Loaded ANE Model with cacheURLIdentifier = %s with programHandle = 0x%llx\n"
+ "Loading E5 compiled for platform = 0x%llx on platform = 0x%llx."
+ "Loading a shared resource. URI = %s \n"
+ "MPSGraph op: E5 Input shape is unknown for input/inOut = %s. Skipping input validation and reshape as part of PrepareOpForEncode()."
+ "MPSGraph op: Skipping output tensor validation for output = %s"
+ "Mapped pre-wire allocations for ANEDevice = 0x%lx programHandle = 0x%llx # buffers = %d\n"
+ "Opened ANEDevice = 0x%lx for programHandle = 0x%llx, aneId = %d \n"
+ "Process holds E5 bundle sharing entitlement.\n"
+ "Profiling Callback invoked. Reported Duration = %f ms\n"
+ "Purging tmp bundle at %s"
+ "RequestID=%{signpost.description:attribute}sGPUResourceCommitDuration=%{signpost.description:attribute}f"
+ "ResetStream() : No ops in stream."
+ "Unable to set compute_unit_mask"
+ "Unloaded ANE JIT Model at path = %s \n"
+ "Unloaded ANE Model at path = %s with programHandle = 0x%llx\n"
+ "Unmapped pre-wire allocations for ANEDevice 0x%lx programHandle 0x%llx # buffers = %d\n"
+ "Warning: Failed to create E5SegmentIO directory: %s"
+ "e5rt"
+ "remove_all() of path = %s failed with error code = %d\n"
- "3600.52.1"

```
