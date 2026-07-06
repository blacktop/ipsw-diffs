## CascadeEngine

> `/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine`

```diff

-  __TEXT.__text: 0x61a38
-  __TEXT.__objc_methlist: 0x1ddc
-  __TEXT.__const: 0x1228
-  __TEXT.__gcc_except_tab: 0x61c
-  __TEXT.__cstring: 0x2894
-  __TEXT.__oslogstring: 0x6539
+  __TEXT.__text: 0x639f4
+  __TEXT.__objc_methlist: 0x1e8c
+  __TEXT.__const: 0x1248
+  __TEXT.__gcc_except_tab: 0x6bc
+  __TEXT.__cstring: 0x2a84
+  __TEXT.__oslogstring: 0x6a29
   __TEXT.__ustring: 0x7c
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__swift5_typeref: 0xdbe
-  __TEXT.__swift5_reflstr: 0x317
+  __TEXT.__swift5_typeref: 0xdc6
+  __TEXT.__swift5_reflstr: 0x31e
   __TEXT.__swift5_assocty: 0xf0
-  __TEXT.__constg_swiftt: 0x5b8
-  __TEXT.__swift5_fieldmd: 0x368
+  __TEXT.__constg_swiftt: 0x5c0
+  __TEXT.__swift5_fieldmd: 0x374
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_capture: 0xd9c
+  __TEXT.__swift5_capture: 0xdd8
   __TEXT.__swift5_proto: 0x78
   __TEXT.__swift5_types: 0x58
-  __TEXT.__swift_as_entry: 0x8c
-  __TEXT.__swift_as_ret: 0x88
-  __TEXT.__swift_as_cont: 0xc8
-  __TEXT.__unwind_info: 0x14e0
+  __TEXT.__swift_as_entry: 0x94
+  __TEXT.__swift_as_ret: 0x90
+  __TEXT.__swift_as_cont: 0xd0
+  __TEXT.__unwind_info: 0x1558
   __TEXT.__eh_frame: 0x1748
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xde8
+  __DATA_CONST.__const: 0xf00
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x118
+  __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1958
+  __DATA_CONST.__objc_selrefs: 0x19f0
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x50
-  __DATA_CONST.__got: 0x638
-  __AUTH_CONST.__const: 0x26a0
-  __AUTH_CONST.__cfstring: 0x1960
-  __AUTH_CONST.__objc_const: 0x4cf0
+  __DATA_CONST.__got: 0x670
+  __AUTH_CONST.__const: 0x2718
+  __AUTH_CONST.__cfstring: 0x1980
+  __AUTH_CONST.__objc_const: 0x50d8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0xed0
-  __AUTH.__objc_data: 0x918
-  __AUTH.__data: 0x1c8
-  __DATA.__objc_ivar: 0x2ac
-  __DATA.__data: 0xe38
-  __DATA.__bss: 0xb50
-  __DATA_DIRTY.__objc_data: 0x820
-  __DATA_DIRTY.__data: 0x2c8
-  __DATA_DIRTY.__bss: 0x410
+  __AUTH_CONST.__auth_got: 0xed8
+  __AUTH.__objc_data: 0x648
+  __AUTH.__data: 0x50
+  __DATA.__objc_ivar: 0x2b8
+  __DATA.__data: 0xdf8
+  __DATA.__bss: 0xb40
+  __DATA_DIRTY.__objc_data: 0xb00
+  __DATA_DIRTY.__data: 0x508
+  __DATA_DIRTY.__bss: 0x420
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2235
-  Symbols:   5011
-  CStrings:  1003
+  Functions: 2263
+  Symbols:   5099
+  CStrings:  1026
 
Sections:
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
Symbols:
+ -[CCDifferentialSetUpdater _updateCacheContentForPredicate:cacheContentData:isEvict:outIsDuplicate:outDidEvictRow:error:]
+ -[CCDifferentialSetUpdater cacheEvictionResult]
+ -[CCDifferentialSetUpdater evictBatchOfKeyPrefixedIdentifiers:outRowsEvicted:error:]
+ -[CCDifferentialSetUpdater finalizeEvictionInPlaceWithError:]
+ -[CCDifferentialSetUpdater reclaimableFreelistBytes:]
+ -[CCDifferentialSetUpdater runEvictionSessionWithPercentage:candidateBatchProvider:error:]
+ -[CCDonationServiceConnection evictCacheContentWithStorageReductionPercentageTarget:reply:]
+ -[CCDonationServiceConnection(CacheEviction) _evictCacheContentWithStorageReductionPercentageTarget:candidateBatchProvider:reply:]
+ -[CCSetStoreUpdateServiceExported evictCacheContentWithStorageReductionPercentageTarget:reply:]
+ GCC_except_table24
+ GCC_except_table35
+ _OBJC_CLASS_$_CCSetDonationCacheEvictionResult
+ _OBJC_CLASS_$_CCSetDonationResult
+ _OBJC_IVAR_$_CCDifferentialSetUpdater._cacheEvictionResult
+ _OBJC_IVAR_$_CCDifferentialSetUpdater._evictionInitialFootprintBytes
+ _OBJC_IVAR_$_CCDifferentialSetUpdater._evictionSessionActive
+ _OUTLINED_FUNCTION_179
+ __OBJC_$_INSTANCE_METHODS_CCDonationServiceConnection(CacheEviction)
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CCCacheEvictionCandidateProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CCDonationService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCCacheEvictionCandidateProvider
+ __OBJC_$_PROTOCOL_REFS_CCCacheEvictionCandidateProvider
+ __OBJC_LABEL_PROTOCOL_$_CCCacheEvictionCandidateProvider
+ __OBJC_PROTOCOL_$_CCCacheEvictionCandidateProvider
+ ___130-[CCDonationServiceConnection(CacheEviction) _evictCacheContentWithStorageReductionPercentageTarget:candidateBatchProvider:reply:]_block_invoke
+ ___55-[CCSetStoreAdminConnection _shouldDeferActivityBlock:]_block_invoke_3
+ ___55-[CCSetStoreAdminConnection _shouldDeferActivityBlock:]_block_invoke_4
+ ___77-[CCDonationServiceConnection endSetDonationWithOptions:revisionToken:reply:]_block_invoke_2
+ ___91-[CCDonationServiceConnection evictCacheContentWithStorageReductionPercentageTarget:reply:]_block_invoke
+ ___91-[CCDonationServiceConnection evictCacheContentWithStorageReductionPercentageTarget:reply:]_block_invoke_2
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSArray"8lr32l8
+ ___block_descriptor_48_e8_32bs40r_e20_v20?0C8"NSError"12ls32l8r40l8
+ ___block_descriptor_48_e8_32bs_e38_B24?0"CCDifferentialSetUpdater"8^16ls32l8
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e18_"NSArray"16?0^8ls32l8r40l8
+ ___block_descriptor_50_e8_32s40r_e38_B24?0"CCDifferentialSetUpdater"8^16ls32l8r40l8
+ ___block_descriptor_64_e8_32r40r48r56r_e5_v8?0lr32l8r40l8r48l8r56l8
+ ___block_descriptor_80_e8_32r40r48r56r64r72r_e5_v8?0lr32l8r40l8r48l8r56l8r64l8r72l8
+ ___block_descriptor_88_e8_32s40s48s56r64r72r_e5_B8?0ls32l8r56l8r64l8r72l8s40l8s48l8
+ ___swift_closure_destructor.369Tm
+ _objc_msgSend$_evictCacheContentWithStorageReductionPercentageTarget:candidateBatchProvider:reply:
+ _objc_msgSend$_updateCacheContentForPredicate:cacheContentData:isEvict:outIsDuplicate:outDidEvictRow:error:
+ _objc_msgSend$accessAssertion
+ _objc_msgSend$cacheEvictionResult
+ _objc_msgSend$evictBatchOfKeyPrefixedIdentifiers:outRowsEvicted:error:
+ _objc_msgSend$evictCacheContentWithStorageReductionPercentageTarget:reply:
+ _objc_msgSend$finalizeEvictionInPlaceWithError:
+ _objc_msgSend$initWithInitialStorageFootprintBytes:finalStorageFootprintBytes:
+ _objc_msgSend$nonEmptyContentRowCount:
+ _objc_msgSend$predicateWithKeyPrefixedIdentifier:error:
+ _objc_msgSend$provideEvictionCandidateBatch:
+ _objc_msgSend$reclaimableFreelistBytes:
+ _objc_msgSend$remoteObjectInterface
+ _objc_msgSend$runEvictionSessionWithPercentage:candidateBatchProvider:error:
+ _objc_msgSend$sourceItemIdentifierHash
+ _objc_msgSend$storageFootprintForSet:accessAssertion:error:
+ _objc_msgSend$vacuumAndTruncateWAL:
+ _symbolic _____Sg 13CascadeEngine014CCCloudKitSyncB0C
+ _symbolic ytSg
+ _symbolic ytSgIeAgHr_
- GCC_except_table11
- GCC_except_table25
- __OBJC_$_INSTANCE_METHODS_CCDonationServiceConnection
- ___block_descriptor_42_e8_32s_e38_B24?0"CCDifferentialSetUpdater"8^16ls32l8
- ___block_descriptor_56_e8_32s40s_e5_B8?0ls32l8s40l8
- _get_type_metadata 15Synchronization5MutexVy13CascadeEngine12WALTruncatorC13BudgetTrackerVG noncopyable
- _get_type_metadata 15Synchronization5MutexVy13CascadeEngine12WALTruncatorC16TerminationStateVG noncopyable
- _get_type_metadata 15Synchronization5MutexVySDySSSiGG noncopyable
- _swift_runtimeSupportsNoncopyableTypes
CStrings:
+ "%@: evictCacheContent percentage=%.3f"
+ "%@: eviction batch reverse-XPC error: %@"
+ "%@: eviction session bailing after %lu iterations without reaching target (target=%llu)"
+ "%@: eviction session done after %lu iteration(s); evictedRows=%llu of targetRows=%llu (avgRowFootprint=%llu, adjustedTarget=%llu, rawTarget=%llu, existingFreelist=%llu, initialFootprint=%llu)"
+ "%@: eviction session not starting: failed to sample existing freelist: %@"
+ "%@: eviction session not starting: failed to sample initial storage footprint: %@"
+ "%@: eviction session not starting: failed to sample live cache row count: %@"
+ "%@: eviction session starting: initialFootprint=%llu, percentage=%.3f, rawTarget=%llu, existingFreelist=%llu, adjustedTarget=%llu, liveRows=%llu, avgRowFootprint=%llu, targetRows=%llu"
+ "%@: eviction session stopping: batch eviction failed (iteration=%lu, evictedRows=%llu of targetRows=%llu)"
+ "%@: eviction session stopping: target already covered before eviction (rawTarget=%llu, existingFreelist=%llu, liveRows=%llu) — finish-time VACUUM will reclaim"
+ "%@: eviction session stopping: target met (evictedRows=%llu of targetRows=%llu) after %lu iteration(s)"
+ "%@: failed to sample final footprint (reporting 0): %@"
+ "%@: vacuumAndTruncateWAL skipped (proceeding with un-compacted final): %@"
+ "-[CCDifferentialSetUpdater evictBatchOfKeyPrefixedIdentifiers:outRowsEvicted:error:]"
+ "-[CCDifferentialSetUpdater finalizeEvictionInPlaceWithError:]"
+ "-[CCDifferentialSetUpdater runEvictionSessionWithPercentage:candidateBatchProvider:error:]"
+ "-[CCDonationServiceConnection(CacheEviction) _evictCacheContentWithStorageReductionPercentageTarget:candidateBatchProvider:reply:]"
+ "@\"NSArray\"16@?0^@8"
+ "Cancelling in-flight CKSyncEngine operations"
+ "Eviction batch provider unavailable"
+ "Reverse-XPC eviction batch call returned nil"
+ "com.apple.cascade.shouldDefer.state"
+ "v16@?0@\"NSArray\"8"
+ "v20@?0C8@\"NSError\"12"
- "%@: Item is already evicted for sourceItemIdentifier: %@"
- "%@: invalid sourceItemIdentifer: %@"

```
