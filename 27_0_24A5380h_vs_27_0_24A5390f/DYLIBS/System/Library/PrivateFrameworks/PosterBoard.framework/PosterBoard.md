## PosterBoard

> `/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-347.102.0.0.0
-  __TEXT.__text: 0x272a9c
-  __TEXT.__objc_methlist: 0xee5c
-  __TEXT.__const: 0x73d4
-  __TEXT.__gcc_except_tab: 0x4604
-  __TEXT.__cstring: 0x143c5
-  __TEXT.__oslogstring: 0x1db6a
+350.1.100.0.0
+  __TEXT.__text: 0x2742a4
+  __TEXT.__objc_methlist: 0xeee4
+  __TEXT.__const: 0x73e4
+  __TEXT.__gcc_except_tab: 0x4624
+  __TEXT.__cstring: 0x144e5
+  __TEXT.__oslogstring: 0x1e04a
   __TEXT.__dlopen_cstrs: 0x2c6
   __TEXT.__ustring: 0xe
   __TEXT.__swift5_typeref: 0x89b6

   __TEXT.__swift_as_ret: 0x34
   __TEXT.__swift_as_cont: 0xe0
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x6c00
+  __TEXT.__unwind_info: 0x6c18
   __TEXT.__eh_frame: 0x1a38
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x6c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9bc8
+  __DATA_CONST.__objc_selrefs: 0x9c30
   __DATA_CONST.__objc_protorefs: 0x2c8
   __DATA_CONST.__objc_superrefs: 0x3e0
   __DATA_CONST.__objc_arraydata: 0x140
-  __DATA_CONST.__got: 0x1da8
-  __AUTH_CONST.__const: 0x9230
-  __AUTH_CONST.__cfstring: 0xc180
-  __AUTH_CONST.__objc_const: 0x3d940
+  __DATA_CONST.__got: 0x1db0
+  __AUTH_CONST.__const: 0x9250
+  __AUTH_CONST.__cfstring: 0xc300
+  __AUTH_CONST.__objc_const: 0x3daa0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__auth_got: 0x2450
+  __AUTH_CONST.__auth_got: 0x2458
   __AUTH.__objc_data: 0x3b38
   __AUTH.__data: 0xfc0
-  __DATA.__objc_ivar: 0x105c
+  __DATA.__objc_ivar: 0x1084
   __DATA.__data: 0x62a0
-  __DATA.__bss: 0x2f38
+  __DATA.__bss: 0x2f48
   __DATA.__common: 0x130
   __DATA_DIRTY.__objc_data: 0x6e98
   __DATA_DIRTY.__data: 0x1548

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10824
-  Symbols:   15084
-  CStrings:  3942
+  Functions: 10841
+  Symbols:   15123
+  CStrings:  3968
 
Symbols:
+ -[PBFLockScreenColorConfigurationCache _stateCaptureDescription]
+ -[PBFLockScreenColorConfigurationCache dealloc]
+ -[PBFLockScreenRoleCoordinator transactionDidCommitWithCollection:]
+ -[PBFLockScreenRoleCoordinator transactionDidFailWithError:]
+ -[PBFPosterSnapshotManager _lock_scheduleStartupRetryRekickWithDelay:]
+ -[PBFPosterSnapshotManager _test_installProviderTracker:pbfTracker:forRequest:enqueueAndKickoff:]
+ -[PBFPosterSnapshotManager initWithRuntimeAssertionProvider:modelCoordinatorProvider:extensionProvider:applicationStateMonitor:]
+ -[PBFPosterSnapshotPUIRequestTracker consumeStartupRetryIfAvailable]
+ -[PBFPosterSnapshotPUIRequestTracker startupRetriesRemaining]
+ -[PBFPosterSnapshotProviderTracker _lock_reclaimSnapshotterState:]
+ -[PBFPosterSnapshotProviderTracker availableInstanceCount]
+ -[PBFPosterSnapshotProviderTracker dequeueSnapshotterForPath:error:]
+ -[PBFPosterSnapshotProviderTracker initWithProvider:extension:extensionInstanceProvider:]
+ -[PBFPosterSnapshotProviderTracker liveInstanceCount]
+ -[PBFPosterSnapshotProviderTracker numberOfLiveSnapshotters]
+ -[PBFPosterSnapshotProviderTracker releaseSnapshotter:shouldTerminate:]
+ -[PBFPosterSnapshotProviderTracker snapshotterDidInvalidateScene:]
+ -[PBFPosterSnapshotProviderTracker terminateAndReclaimSnapshotterImmediately:]
+ _OBJC_CLASS_$_PFPosterExtensionInstanceProvider
+ _OBJC_IVAR_$_PBFLockScreenColorConfigurationCache._lock_generation
+ _OBJC_IVAR_$_PBFLockScreenColorConfigurationCache._lock_lastWrittenConfigurations
+ _OBJC_IVAR_$_PBFLockScreenColorConfigurationCache._stateCaptureHandle
+ _OBJC_IVAR_$_PBFPosterSnapshotManager._extensionInstanceProvider
+ _OBJC_IVAR_$_PBFPosterSnapshotManager._lock_puiRequestToSnapshotter
+ _OBJC_IVAR_$_PBFPosterSnapshotManager._lock_startupRetryRekickScheduled
+ _OBJC_IVAR_$_PBFPosterSnapshotPUIRequestTracker._lock_startupRetriesRemaining
+ _OBJC_IVAR_$_PBFPosterSnapshotProviderTracker._extension
+ _OBJC_IVAR_$_PBFPosterSnapshotProviderTracker._extensionInstanceProvider
+ _OBJC_IVAR_$_PBFPosterSnapshotProviderTracker._lock_liveSnapshotters
+ _OBJC_IVAR_$_PBFPosterSnapshotProviderTracker._lock_pendingTerminateVerdict
+ _OBJC_IVAR_$_PBFPosterSnapshotProviderTracker._lock_snapshotterInstances
+ _PBFErrorIsBenignNonCrash
+ _PBFLogSnapshotProviderTracker
+ _PBFLogSnapshotProviderTracker.__logObj
+ _PBFLogSnapshotProviderTracker.onceToken
+ _PFDispatchTimeAfterSeconds
+ ___58-[PBFLockScreenColorConfigurationCache initWithCachePath:]_block_invoke
+ ___58-[PBFLockScreenColorConfigurationCache initWithCachePath:]_block_invoke_2
+ ___70-[PBFPosterSnapshotManager _lock_scheduleStartupRetryRekickWithDelay:]_block_invoke
+ ___PBFLogSnapshotProviderTracker_block_invoke
+ _objc_msgSend$_lock_reclaimSnapshotterState:
+ _objc_msgSend$_lock_scheduleStartupRetryRekickWithDelay:
+ _objc_msgSend$_stateCaptureDescription
+ _objc_msgSend$briefStateCaptureLine
+ _objc_msgSend$consumeStartupRetryIfAvailable
+ _objc_msgSend$dequeueSnapshotterForPath:error:
+ _objc_msgSend$fileModificationDate
+ _objc_msgSend$fileSize
+ _objc_msgSend$initWithDefaultInstanceIdentifier:maxNumberOfInstancesPerExtension:
+ _objc_msgSend$initWithProvider:extension:extensionInstanceProvider:
+ _objc_msgSend$initWithRuntimeAssertionProvider:modelCoordinatorProvider:extensionProvider:applicationStateMonitor:
+ _objc_msgSend$instanceForExtension:reason:
+ _objc_msgSend$invalidateCache
+ _objc_msgSend$releaseSnapshotter:shouldTerminate:
+ _objc_msgSend$snapshotterDidInvalidateScene:
+ _objc_msgSend$startupRetriesRemaining
+ _objc_msgSend$terminateAndReclaimSnapshotterImmediately:
+ _objc_msgSend$transactionDidCommitWithCollection:
+ _objc_msgSend$transactionDidFailWithError:
- -[PBFLockScreenRoleCoordinator _updateColorConfigurationCacheWithCollection:]
- -[PBFPosterSnapshotManager initWithRuntimeAssertionProvider:modelCoordinatorProvider:applicationStateMonitor:]
- -[PBFPosterSnapshotProviderTracker alignmentKeys]
- -[PBFPosterSnapshotProviderTracker createSnapshotterForPath:error:]
- -[PBFPosterSnapshotProviderTracker initWithProvider:extensionProvider:]
- -[PBFPosterSnapshotProviderTracker releaseSnapshotter:]
- -[PBFPosterSnapshotProviderTracker removeSnapshotterForAlignmentKey:]
- -[PBFPosterSnapshotProviderTracker snapshotterDidInvalidateScene:shouldTerminate:]
- -[PBFPosterSnapshotProviderTracker snapshotterForAlignmentKey:]
- _OBJC_IVAR_$_PBFPosterSnapshotProviderTracker._extensionProvider
- _OBJC_IVAR_$_PBFPosterSnapshotProviderTracker._lock_snapshottersByAlignmentKey
- _PBFAlignmentKeyForPath
- _objc_msgSend$_updateColorConfigurationCacheWithCollection:
- _objc_msgSend$createSnapshotterForPath:error:
- _objc_msgSend$initWithProvider:extensionProvider:
- _objc_msgSend$initWithRuntimeAssertionProvider:modelCoordinatorProvider:applicationStateMonitor:
- _objc_msgSend$releaseSnapshotter:
- _objc_msgSend$removeSnapshotterForAlignmentKey:
- _objc_msgSend$snapshotterDidInvalidateScene:shouldTerminate:
- _objc_msgSend$snapshotterForAlignmentKey:
CStrings:
+ "  %@\n"
+ "(pooled, no reason)"
+ "N"
+ "PBFLockScreenColorConfigurationCache"
+ "PBFLockScreenColorConfigurationCache.m"
+ "PBFLockScreenColorConfigurationCache: failed to create cache directory: %{public}@"
+ "PBFPosterSnapshotManager"
+ "PUI request %{public}@ failed (%{public}@); terminating process and retrying (%lu attempts left)"
+ "SnapshotProviderTracker"
+ "Y"
+ "[%{public}@] canAcceptMoreSnapshotters:%lu -> liveInstances=%lu availableForReuse=%lu (snapshotters total=%lu pending=%lu) canAccept=%d"
+ "[%{public}@] dequeueSnapshotterForPath: %{public}@ %{public}@ instance (reason=%{public}@) -> liveInstances=%lu availableForReuse=%lu (snapshotters total=%lu pending=%lu)"
+ "[%{public}@] dequeueSnapshotterForPath: %{public}@ failed to acquire instance (reason=%{public}@): %{public}@"
+ "[%{public}@] releaseSnapshotter: snapshotter=%{public}@ shouldTerminate=%d marked pending-invalidation -> total=%lu pending=%lu (active=%lu)"
+ "[%{public}@] snapshotterDidInvalidateScene: EARLY-RETURN — snapshotter=%{public}@ not found in _lock_snapshottersPendingInvalidation (already invalidated, or never released?)"
+ "[%{public}@] snapshotterDidInvalidateScene: snapshotter=%{public}@ shouldTerminate=%d -> total=%lu pending=%lu (real teardown confirmed)"
+ "[%{public}@] terminateAndReclaimSnapshotterImmediately: snapshotter=%{public}@ -> total=%lu pending=%lu (no scene to wait for)"
+ "[%{public}@] terminateAndReclaimSnapshotterImmediately: snapshotter=%{public}@ already reclaimed — no-op"
+ "booted NEW"
+ "cancelRequests: invalidating orphaned snapshotter %{public}@ and reclaiming its instance"
+ "cancelRequests: releasing orphaned snapshotter %{public}@ for reuse"
+ "configs=%lu\n"
+ "createDir failed"
+ "epoch=%llu lastWrittenBytes=%lu pending=%lu valid=%@\n"
+ "kickoff: no instance for %{public}@ (%{public}@); retrying (%lu attempts left)"
+ "kickoff: no instance for %{public}@ after retries: %{public}@ — failing request"
+ "path=%@ exists=%@ size=%llu mtime=%@\n"
+ "raced invalidate (post-IO)"
+ "raced invalidate (pre-IO)"
+ "reused POOLED"
+ "\x91"
- "cancelRequests: No more active work for alignment key %{public}@, invalidating orphaned snapshotter"
- "cancelRequests: No more active work for alignment key %{public}@, releasing orphaned snapshotter for reuse"
- "cancelRequests: alignment key %{public}@ still in use by another active request, keeping snapshotter"
- "kickoff: Created snapshotter for alignment key %{public}@"
- "kickoff: Failed to create snapshotter for %{public}@: %{public}@"
```
