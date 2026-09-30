## PosterBoard

> `/System/iOSSupport/System/Library/PrivateFrameworks/PosterBoard.framework/Versions/A/PosterBoard`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-347.100.0.0.0
-  __TEXT.__text: 0x1c0720
-  __TEXT.__objc_methlist: 0xc64c
+350.1.0.0.0
+  __TEXT.__text: 0x1c1ff4
+  __TEXT.__objc_methlist: 0xc6fc
   __TEXT.__const: 0x55b4
-  __TEXT.__gcc_except_tab: 0x3f14
-  __TEXT.__cstring: 0x1152e
-  __TEXT.__oslogstring: 0x18ba2
+  __TEXT.__gcc_except_tab: 0x3f28
+  __TEXT.__cstring: 0x115ee
+  __TEXT.__oslogstring: 0x18e82
   __TEXT.__dlopen_cstrs: 0x150
   __TEXT.__ustring: 0xe
   __TEXT.__swift5_typeref: 0x5bbc

   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x3c
-  __TEXT.__unwind_info: 0x5258
+  __TEXT.__unwind_info: 0x52a0
   __TEXT.__eh_frame: 0xa10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x508
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8000
+  __DATA_CONST.__objc_selrefs: 0x8078
   __DATA_CONST.__objc_protorefs: 0x208
   __DATA_CONST.__objc_superrefs: 0x390
   __DATA_CONST.__objc_arraydata: 0x120
   __DATA_CONST.__got: 0x18e8
   __AUTH_CONST.__const: 0x54b8
-  __AUTH_CONST.__cfstring: 0xb200
-  __AUTH_CONST.__objc_const: 0x2ec10
+  __AUTH_CONST.__cfstring: 0xb320
+  __AUTH_CONST.__objc_const: 0x2ec80
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1f20
+  __AUTH_CONST.__auth_got: 0x1f28
   __AUTH.__objc_data: 0x29d0
   __AUTH.__data: 0xa70
-  __DATA.__objc_ivar: 0xe60
+  __DATA.__objc_ivar: 0xe6c
   __DATA.__data: 0x4980
   __DATA.__bss: 0x2728
   __DATA.__common: 0xa0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8152
-  Symbols:   13005
-  CStrings:  3351
+  Functions: 8173
+  Symbols:   13035
+  CStrings:  3369
 
Symbols:
+ +[PBFGenericDisplayContext displayContextsCollapsedToOnePerPhysicalDisplay:]
+ -[PBFApplicationStateForegroundAssertion initWithMonitor:reason:pinnedDisplayContexts:]
+ -[PBFApplicationStateMonitor acquireForegroundAssertionWithReason:pinnedDisplayContexts:]
+ -[PBFLockScreenColorConfigurationCache _stateCaptureDescription]
+ -[PBFLockScreenColorConfigurationCache dealloc]
+ -[PBFLockScreenRoleCoordinator transactionDidCommitWithCollection:]
+ -[PBFLockScreenRoleCoordinator transactionDidFailWithError:]
+ -[PBFPosterExtensionDataStoreXPCServiceGlue refreshPinnedDisplays]
+ -[PBFPosterSnapshotManager _lock_beginFinishingActivePUIRequest:]
+ -[PBFPosterSnapshotManager _lock_releaseSnapshotterForOrphanedPUIRequest:]
+ -[PBFPosterSnapshotManager _test_cancelActiveOrphan:]
+ -[PBFPosterSnapshotManager _test_makePUIRequestActive:providerTracker:]
+ -[PBFPosterSnapshotManager _test_simulateSnapshotterCompletionForPUIRequest:]
+ OBJC_IVAR_$_PBFLockScreenColorConfigurationCache._lock_generation
+ OBJC_IVAR_$_PBFLockScreenColorConfigurationCache._lock_lastWrittenConfigurations
+ OBJC_IVAR_$_PBFLockScreenColorConfigurationCache._stateCaptureHandle
+ _PBFAlignmentKeyForPath
+ _PBFDisplayContextUnresolvedFieldCount
+ _PFDispatchTimeAfterSeconds
+ ___58-[PBFLockScreenColorConfigurationCache initWithCachePath:]_block_invoke
+ ___58-[PBFLockScreenColorConfigurationCache initWithCachePath:]_block_invoke_2
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80w_e48_v24?0"PUIPosterSnapshotterResult"8"NSError"16lw80l8s32l8s40l8s48l8s56l8s64l8s72l8
+ _objc_msgSend$_lock_beginFinishingActivePUIRequest:
+ _objc_msgSend$_lock_releaseSnapshotterForOrphanedPUIRequest:
+ _objc_msgSend$_stateCaptureDescription
+ _objc_msgSend$acquireForegroundAssertionWithReason:pinnedDisplayContexts:
+ _objc_msgSend$briefStateCaptureLine
+ _objc_msgSend$displayContextWithUpdatedAccessibilityContrast:
+ _objc_msgSend$displayContextsCollapsedToOnePerPhysicalDisplay:
+ _objc_msgSend$fileModificationDate
+ _objc_msgSend$fileSize
+ _objc_msgSend$initWithMonitor:reason:pinnedDisplayContexts:
+ _objc_msgSend$invalidateCache
+ _objc_msgSend$rootIdentity
+ _objc_msgSend$transactionDidCommitWithCollection:
+ _objc_msgSend$transactionDidFailWithError:
- -[PBFLockScreenRoleCoordinator _updateColorConfigurationCacheWithCollection:]
- GCC_except_table53
- ___block_descriptor_80_e8_32s40s48s56s64s72w_e48_v24?0"PUIPosterSnapshotterResult"8"NSError"16lw72l8s32l8s40l8s48l8s56l8s64l8
- _objc_msgSend$_updateColorConfigurationCacheWithCollection:
- _objc_msgSend$initWithMonitor:reason:
- _objc_msgSend$setPinnedDisplayContexts:
CStrings:
+ "  %@\n"
+ "Attempted to decrement running snapshotters below 0 while releasing orphaned PUI request"
+ "N"
+ "PBFLockScreenColorConfigurationCache"
+ "PBFLockScreenColorConfigurationCache.m"
+ "PBFLockScreenColorConfigurationCache: failed to create cache directory: %{public}@"
+ "Y"
+ "b[%@]-f[%@]-s[%f]-o[%lu]-ui[%lu]-ax[%lu]-dt[%@]-dc[%lu]-ao[%lu]"
+ "cancelRequests: No more active work for alignment key %{public}@, invalidating orphaned snapshotter"
+ "cancelRequests: No more active work for alignment key %{public}@, releasing orphaned snapshotter for reuse"
+ "cancelRequests: alignment key %{public}@ still in use by another active request, keeping snapshotter"
+ "configs=%lu\n"
+ "createDir failed"
+ "epoch=%llu lastWrittenBytes=%lu pending=%lu valid=%@\n"
+ "geo:%@:%g"
+ "kickoff: Provider %{public}@ entered crash cooldown (>=3 snapshot failures within %.0fs) — pausing its non-visible posters"
+ "path=%@ exists=%@ size=%llu mtime=%@\n"
+ "raced invalidate (post-IO)"
+ "raced invalidate (pre-IO)"
+ "updatePinnedDisplays: rebuilt pinned-context set was empty (embedded context unavailable); retaining prior pinned component"
- "No more work for alignment key %{public}@, releasing snapshotter"
- "b[%@]-f[%@]-s[%f]-o[%lu]-ui[%lu]-ax[%lu]-dt[%@]-dc[%lu]-ao[%lu]-sa[%@]"
```
