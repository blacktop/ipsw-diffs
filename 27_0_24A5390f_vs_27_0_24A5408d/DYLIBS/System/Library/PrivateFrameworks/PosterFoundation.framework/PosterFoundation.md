## PosterFoundation

> `/System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-350.1.100.0.0
-  __TEXT.__text: 0x5e500
-  __TEXT.__objc_methlist: 0x3ab8
+355.0.5.0.0
+  __TEXT.__text: 0x5f134
+  __TEXT.__objc_methlist: 0x3ac8
   __TEXT.__const: 0x568
-  __TEXT.__cstring: 0x49b9
-  __TEXT.__oslogstring: 0x4911
-  __TEXT.__gcc_except_tab: 0xe28
+  __TEXT.__cstring: 0x4a89
+  __TEXT.__oslogstring: 0x4c21
+  __TEXT.__gcc_except_tab: 0xe58
   __TEXT.__swift5_typeref: 0x44d
   __TEXT.__swift5_capture: 0x2b8
   __TEXT.__constg_swiftt: 0x164

   __TEXT.__swift_as_cont: 0x44
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x18e0
+  __TEXT.__unwind_info: 0x1910
   __TEXT.__eh_frame: 0x838
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x13f8
+  __DATA_CONST.__const: 0x1408
   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2280
+  __DATA_CONST.__objc_selrefs: 0x22b0
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x250
   __DATA_CONST.__got: 0x608
-  __AUTH_CONST.__const: 0x14c0
-  __AUTH_CONST.__cfstring: 0x44c0
+  __AUTH_CONST.__const: 0x14e0
+  __AUTH_CONST.__cfstring: 0x45e0
   __AUTH_CONST.__objc_const: 0x93e0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0xd70
+  __AUTH_CONST.__auth_got: 0xd78
   __AUTH.__objc_data: 0x628
   __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0x318
   __DATA.__data: 0xd60
-  __DATA.__bss: 0xd0
+  __DATA.__bss: 0xe8
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0xd70
   __DATA_DIRTY.__data: 0xa8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2178
-  Symbols:   3916
-  CStrings:  1018
+  Functions: 2187
+  Symbols:   3935
+  CStrings:  1037
 
Symbols:
+ +[PFPosterPath reapStaleProcessScopedTemporaryDirectoriesWithPolicy:]
+ GCC_except_table34
+ GCC_except_table43
+ GCC_except_table97
+ _PFPosterPathStaleTempReapBootSessionDefaultsKey
+ _PFPosterPathStaleTempReapLastCleanupDateDefaultsKey
+ __PFCurrentBootSessionUUID
+ __PFCurrentBootSessionUUID.bootSessionUUID
+ __PFCurrentBootSessionUUID.onceToken
+ __PFReapGuardLock
+ __PFReapStaleProcessScopedTemporaryDirectories
+ __PFSweepStaleProcessScopedTemporaryDirectories
+ ____PFCurrentBootSessionUUID_block_invoke
+ ____PFReapStaleProcessScopedTemporaryDirectories_block_invoke
+ _getpid
+ _objc_msgSend$acquireWithError:
+ _objc_msgSend$contentsOfDirectoryAtPath:error:
+ _objc_msgSend$pf_extendRenderSessionWithReason:
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$synchronize
+ _objc_msgSend$timeIntervalSinceNow
- _OUTLINED_FUNCTION_45
- _OUTLINED_FUNCTION_46
CStrings:
+ "+[NSURL pf_directoryURLWithContainerPath:basenamePrefix:error:]: failed to create container %{public}@: %{public}@"
+ "Duvet"
+ "PFPosterPath reap stale temp"
+ "PFPosterPathStaleTempReapBootSession"
+ "PFPosterPathStaleTempReapLastCleanupDate"
+ "_temporaryDirectoryURLWithBasenamePrefix: process-local fallback also failed for prefix=%{public}@: %{public}@"
+ "_temporaryDirectoryURLWithBasenamePrefix: recovered via process-local fallback container=%{public}@ prefix=%{public}@ (override %{public}@ was unreachable)"
+ "cannot ensure reachability of a nil contentsURL"
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
```
