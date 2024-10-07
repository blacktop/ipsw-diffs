## PosterBoard

> `/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard`

```diff

-228.1.4.1.0
-  __TEXT.__text: 0x19ecf4
+228.1.7.0.0
+  __TEXT.__text: 0x19f520
   __TEXT.__auth_stubs: 0x2a80
-  __TEXT.__objc_methlist: 0xa034
+  __TEXT.__objc_methlist: 0xa07c
   __TEXT.__const: 0x2374
-  __TEXT.__gcc_except_tab: 0x45c4
-  __TEXT.__cstring: 0x14bab
-  __TEXT.__oslogstring: 0x14492
+  __TEXT.__gcc_except_tab: 0x45a4
+  __TEXT.__cstring: 0x14b9b
+  __TEXT.__oslogstring: 0x145c2
   __TEXT.__dlopen_cstrs: 0x26e
   __TEXT.__ustring: 0xe
   __TEXT.__swift5_typeref: 0x1ec4

   __TEXT.__swift5_types: 0x110
   __TEXT.__swift5_capture: 0x1194
   __TEXT.__swift5_protos: 0x40
-  __TEXT.__unwind_info: 0x4d18
+  __TEXT.__unwind_info: 0x4d28
   __TEXT.__eh_frame: 0x8e0
   __TEXT.__objc_classname: 0x228b
-  __TEXT.__objc_methname: 0x28794
-  __TEXT.__objc_methtype: 0x87cd
-  __TEXT.__objc_stubs: 0x171c0
+  __TEXT.__objc_methname: 0x2886d
+  __TEXT.__objc_methtype: 0x87db
+  __TEXT.__objc_stubs: 0x17240
   __DATA_CONST.__got: 0x1410
-  __DATA_CONST.__const: 0x4670
+  __DATA_CONST.__const: 0x46c0
   __DATA_CONST.__objc_classlist: 0x630
   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x558
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7748
+  __DATA_CONST.__objc_selrefs: 0x7760
   __DATA_CONST.__objc_protorefs: 0x208
   __DATA_CONST.__objc_superrefs: 0x398
   __DATA_CONST.__objc_arraydata: 0xd0
   __AUTH_CONST.__auth_got: 0x1550
-  __AUTH_CONST.__auth_ptr: 0x778
-  __AUTH_CONST.__const: 0x5428
-  __AUTH_CONST.__cfstring: 0xa6e0
-  __AUTH_CONST.__objc_const: 0x326f8
+  __AUTH_CONST.__auth_ptr: 0x768
+  __AUTH_CONST.__const: 0x5468
+  __AUTH_CONST.__cfstring: 0xa720
+  __AUTH_CONST.__objc_const: 0x32898
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x2320
   __AUTH.__data: 0x4b8
-  __DATA.__objc_ivar: 0xe80
+  __DATA.__objc_ivar: 0xe8c
   __DATA.__data: 0x3a68
   __DATA.__bss: 0xc00
   __DATA.__common: 0x90

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7138
-  Symbols:   6599
-  CStrings:  10044
+  Functions: 7146
+  Symbols:   6608
+  CStrings:  10059
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
CStrings:
+ "\x01!\x15F"
+ "\x02!5\x12\x13\x18"
+ "\x0f\x05\x11&\x1a"
+ "!*!\x11\x12"
+ "(%!{(MISSING)public}@) Aborting capture, snapshotter is reporting that it is done."
+ "(%!{(MISSING)public}@) prewarm runtime assertion was invalidated: %!{(MISSING)public}@"
+ "(null reason)"
+ "-[PBFPosterSnapshotManager _evaluateInUseAssertionsByRemovingAssertion:orAddingAssertion:]"
+ "@16@?0@\"BSSimpleAssertion\"8"
+ "PBFPosterExtensionReloadConfigurationOperation refreshPosterConfiguration"
+ "PBFPosterSnapshotter is running for %!@(MISSING); keep PosterBoard alive until complete"
+ "Prewarm Assertion *WAS* cleaned up."
+ "Prewarm Assertion was *FORCIBLY* cleaned up: reason '%!{(MISSING)public}@'"
+ "Prewarm Assertion was *NOT* cleaned up: no prewarm assertion currently acquired."
+ "Prewarm Assertion was *NOT* cleaned up: outstanding requests remain."
+ "_evaluateInUseAssertionsByRemovingAssertion:orAddingAssertion:"
+ "_extensionsCurrentlyUpdatingFlag"
+ "_keepPosterBoardAliveUntilSnapshottingIsComplete"
+ "_lock_posterBoardPrewarmAssertion"
+ "_lock_teardownPrewarmAssertion state; outstanding snapshot handlers %!l(MISSING)d;  invalidated: %!{(MISSING)BOOL}u"
+ "_lock_teardownPrewarmAssertionShouldForce:reason:"
+ "_operationQueueLock"
+ "_operationQueueLock_isOperationQueueSuspended"
+ "_operationQueueLock_updateOperationQueueSuspended:"
+ "_teardownPrewarmAssertionShouldForce:reason:"
+ "_updateOperationQueueSuspended:"
+ "activeSnapshotterInUseAssertionCount"
+ "activeSnapshotterInUseAssertionReasons"
+ "bs_array"
+ "reloadDescriptors for "
+ "snapshotter operation queue activated"
+ "snapshotter operation queue activating..."
+ "snapshotter operation queue already activated; no work to do"
+ "snapshotter operation queue suspended"
+ "snapshotter operation queue suspending..."
+ "v28@0:8B16@20"
- "\x01!\x14F"
- "\x02!5\x12\x12\x18"
- "\x0f\x05\x11%!\(MISSING)x1a"
- "\x11'\x13\"\x12"
- "(%!{(MISSING)public}@) prewarm runtime assertion was invalidated; probably ran out of time?"
- "-[PBFPosterSnapshotManager _assertionLock_evaluateInUseAssertions]"
- "-[PBFPosterSnapshotManager _enumerateAssertionObservers:respondingToSelector:]"
- "PBFPosterSnapshotter cleanup is running for %!@(MISSING)/%!@(MISSING); keep PosterBoard alive until invalidation complete"
- "Prewarm Assertion was cleaned up for reason: %!{(MISSING)public}@; operation queue is suspended %!{(MISSING)BOOL}u; number of _lock_requestToCompletion handlers %!l(MISSING)d; number of operations %!l(MISSING)d; invalidated: %!{(MISSING)BOOL}u"
- "_assertionLock_evaluateInUseAssertions"
- "_assertionLock_isOperationQueueSuspended"
- "_assertionLock_updateOperationQueueSuspended:"
- "_lock_teardownPrewarmAssertionIfAppropriate:"
- "_posterBoardPrewarmAssertion"
- "_stateLock_enqueueRefreshPosterConfigurationMatchingUUID refreshPosterConfiguration"
- "_stateLock_updatingExtensions"
- "_teardownPrewarmAssertionIfAppropriate:"
- "posterConfigurations"
- "snapshotter operation queue activating"
- "snapshotter operation queue already activated"
- "snapshotter operation queue suspending"

```
