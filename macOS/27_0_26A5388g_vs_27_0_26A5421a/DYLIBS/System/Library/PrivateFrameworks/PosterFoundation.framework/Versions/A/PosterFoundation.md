## PosterFoundation

> `/System/Library/PrivateFrameworks/PosterFoundation.framework/Versions/A/PosterFoundation`

```diff

-350.1.0.0.0
-  __TEXT.__text: 0x495f4
-  __TEXT.__objc_methlist: 0x3528
+355.0.0.0.0
+  __TEXT.__text: 0x4a5e8
+  __TEXT.__objc_methlist: 0x3550
   __TEXT.__const: 0x1e6
-  __TEXT.__cstring: 0x4381
-  __TEXT.__oslogstring: 0x3ba5
-  __TEXT.__gcc_except_tab: 0xe38
-  __TEXT.__unwind_info: 0x1390
+  __TEXT.__cstring: 0x449e
+  __TEXT.__oslogstring: 0x3ff6
+  __TEXT.__gcc_except_tab: 0xe68
+  __TEXT.__unwind_info: 0x13c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6c0
+  __DATA_CONST.__const: 0x6d0
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f48
+  __DATA_CONST.__objc_selrefs: 0x1f88
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x250
   __DATA_CONST.__got: 0x530
-  __AUTH_CONST.__const: 0x18e0
-  __AUTH_CONST.__cfstring: 0x4420
-  __AUTH_CONST.__objc_const: 0x8660
+  __AUTH_CONST.__const: 0x1900
+  __AUTH_CONST.__cfstring: 0x4580
+  __AUTH_CONST.__objc_const: 0x86b0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x310
+  __DATA.__objc_ivar: 0x318
   __DATA.__data: 0x850
-  __DATA.__bss: 0xd0
+  __DATA.__bss: 0xe8
   __DATA_DIRTY.__objc_data: 0xdc0
   __DATA_DIRTY.__bss: 0x200
   __DATA_DIRTY.__common: 0xc

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1825
-  Symbols:   3652
-  CStrings:  928
+  Functions: 1839
+  Symbols:   3681
+  CStrings:  951
 
Symbols:
+ +[PFPosterPath reapStaleProcessScopedTemporaryDirectoriesWithPolicy:]
+ -[PFPosterExtensionInstanceProvider initWithDefaultInstanceIdentifier:maxNumberOfInstancesPerExtension:]
+ -[PFPosterExtensionInstanceProvider maxNumberOfInstancesPerExtension]
+ GCC_except_table101
+ GCC_except_table48
+ GCC_except_table78
+ OBJC_IVAR_$_PFPosterExtensionInstanceProvider._lock_releasedInstances
+ OBJC_IVAR_$_PFPosterExtensionInstanceProvider._maxNumberOfInstancesPerExtension
+ _OUTLINED_FUNCTION_49
+ _PFCurrentBootSessionUUID
+ _PFCurrentBootSessionUUID.bootSessionUUID
+ _PFCurrentBootSessionUUID.onceToken
+ _PFPosterPathStaleTempReapBootSessionDefaultsKey
+ _PFPosterPathStaleTempReapLastCleanupDateDefaultsKey
+ _PFReapStaleProcessScopedTemporaryDirectories
+ _PFSweepStaleProcessScopedTemporaryDirectories
+ __PFCurrentBootSessionUUID
+ __PFReapGuardLock
+ __PFReapStaleProcessScopedTemporaryDirectories
+ __PFSweepStaleProcessScopedTemporaryDirectories
+ ___104-[PFPosterExtensionInstanceProvider initWithDefaultInstanceIdentifier:maxNumberOfInstancesPerExtension:]_block_invoke
+ ___PFReapStaleProcessScopedTemporaryDirectories_block_invoke
+ ____PFCurrentBootSessionUUID_block_invoke
+ ____PFReapStaleProcessScopedTemporaryDirectories_block_invoke
+ _getpid
+ _objc_msgSend$acquireWithError:
+ _objc_msgSend$contentsOfDirectoryAtPath:error:
+ _objc_msgSend$initWithDefaultInstanceIdentifier:maxNumberOfInstancesPerExtension:
+ _objc_msgSend$pf_extendRenderSessionWithReason:
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$synchronize
+ _objc_msgSend$timeIntervalSinceNow
- GCC_except_table46
- GCC_except_table77
- ___71-[PFPosterExtensionInstanceProvider initWithDefaultInstanceIdentifier:]_block_invoke
CStrings:
+ "(%p) BACKSTOP HIT: extension '%{public}@' already has %lu live instances (max %lu); refusing to create another for reason '%{public}@' — an upstream gate over-admitted (accounting bug). rdar://181536204"
+ "(%p) relinquish of UNKNOWN instance '%{public}@'/%{public}@ for reason '%{public}@' — never vended by this provider"
+ "(%p) relinquish of already-released instance '%{public}@'/%{public}@ for reason '%{public}@' — no-op"
+ "+[NSURL pf_directoryURLWithContainerPath:basenamePrefix:error:]: failed to create container %{public}@: %{public}@"
+ "Duvet"
+ "PFPosterPath reap stale temp"
+ "PFPosterPathStaleTempReapBootSession"
+ "PFPosterPathStaleTempReapLastCleanupDate"
+ "_temporaryDirectoryURLWithBasenamePrefix: process-local fallback also failed for prefix=%{public}@: %{public}@"
+ "_temporaryDirectoryURLWithBasenamePrefix: recovered via process-local fallback container=%{public}@ prefix=%{public}@ (override %{public}@ was unreachable)"
+ "cannot ensure reachability of a nil contentsURL"
+ "exceeds max number of instances for extension"
+ "maxNumberOfInstancesPerExtension"
+ "never"
+ "nobootuuid"
+ "proc-"
+ "proc-%@-"
+ "proc-%@-%d"
+ "reap: attempting cleanup for boot=%{public}@ ; %.0fs since last attempt (%{public}@)"
+ "reap: failed to list %{public}@: %{public}@"
+ "reap: failed to remove stale temp %{public}@: %{public}@"
+ "reap: no boot session UUID (kern.bootsessionuuid unavailable?); skipping"
+ "reap: removed stale process-scoped temp %{public}@"
+ "reap: sweep raised %{public}@ — abandoning (attempt already recorded, won't retry this boot)"
- "(%p) attempted to relinquish unknown or mismatched instance '%{public}@'/%{public}@ for reason '%{public}@'"
```
