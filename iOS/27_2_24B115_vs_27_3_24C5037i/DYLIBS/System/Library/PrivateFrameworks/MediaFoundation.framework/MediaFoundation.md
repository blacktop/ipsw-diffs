## MediaFoundation

> `/System/Library/PrivateFrameworks/MediaFoundation.framework/MediaFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__oslogstring`

```diff

-4026.200.17.0.0
-  __TEXT.__text: 0x29ab0
-  __TEXT.__const: 0x4e18
-  __TEXT.__cstring: 0x6aa
-  __TEXT.__swift5_typeref: 0x10f9
-  __TEXT.__swift5_capture: 0x4d8
-  __TEXT.__swift5_reflstr: 0xf31
+4026.300.12.0.0
+  __TEXT.__text: 0x2afc0
+  __TEXT.__const: 0x4de8
+  __TEXT.__cstring: 0x81b
+  __TEXT.__swift5_typeref: 0x10b9
+  __TEXT.__swift5_capture: 0x2e8
+  __TEXT.__swift5_reflstr: 0xf3d
   __TEXT.__swift5_assocty: 0x218
-  __TEXT.__swift5_fieldmd: 0x1490
-  __TEXT.__constg_swiftt: 0x114c
+  __TEXT.__swift5_fieldmd: 0x1474
+  __TEXT.__constg_swiftt: 0x10f4
   __TEXT.__swift5_builtin: 0x1cc
   __TEXT.__swift5_mpenum: 0x54
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_proto: 0x1f8
-  __TEXT.__swift5_types: 0x12c
+  __TEXT.__swift5_types: 0x128
   __TEXT.__swift5_types2: 0x38
   __TEXT.__oslogstring: 0x26a
-  __TEXT.__unwind_info: 0x1560
-  __TEXT.__eh_frame: 0x1a48
+  __TEXT.__unwind_info: 0x1590
+  __TEXT.__eh_frame: 0x1af0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xe0
-  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x550
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x36c8
-  __AUTH_CONST.__objc_const: 0x248
-  __AUTH_CONST.__auth_got: 0x918
-  __DATA.__data: 0x4c8
+  __AUTH_CONST.__const: 0x2fd8
+  __AUTH_CONST.__objc_const: 0x2d8
+  __AUTH_CONST.__auth_got: 0x9a8
+  __AUTH.__data: 0xa8
+  __DATA.__data: 0x4e8
   __DATA.__common: 0x18
-  __DATA_DIRTY.__data: 0xa00
+  __DATA_DIRTY.__data: 0x9f0
   __DATA_DIRTY.__common: 0x8
   __DATA_DIRTY.__bss: 0x280
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1929
-  Symbols:   774
-  CStrings:  66
+  Functions: 1927
+  Symbols:   773
+  CStrings:  76
 
Symbols:
+ __DATA__TtCV15MediaFoundation11SQLDatabase13StatementPool
+ __METACLASS_DATA__TtCV15MediaFoundation11SQLDatabase13StatementPool
+ __os_signpost_emit_with_name_impl
+ _objc_release_x27
+ _objc_release_x28
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _sqlite3_backup_finish
+ _sqlite3_backup_init
+ _sqlite3_backup_step
+ _sqlite3_db_readonly
+ _symbolic SiSg
+ _symbolic _____ 2os12OSSignposterV
+ _symbolic _____y_____y_____GG 15Synchronization5MutexVAARi_zrlE s11UniqueArrayVsRi_zrlE 15MediaFoundation11SQLDatabaseV17PreparedStatementV
- ___swift_memcpy73_8
- _objc_release_x24
- _objc_release_x26
- _swift_arrayInitWithTakeBackToFront
- _swift_arrayInitWithTakeFrontToBack
- _swift_getFixedArrayTypeMetadata
- _symbolic SSIego_
- _symbolic SbIegd_
- _symbolic Sry_____G 15MediaFoundation11SQLDatabaseV17PreparedStatementV
- _symbolic _____ 15MediaFoundation11SQLDatabaseV13StatementPoolC4Slot33_85DA4BD8E26B0D36C7853F6976DE6552LLV
- _symbolic _____ s15ContinuousClockV7InstantV
- _symbolic _____Iegd_ s5Int32V
- _symbolic _____Iegr_ s5Int32V
- _symbolic _____y_$31_G 15MediaFoundation11SQLDatabaseV13StatementPoolC
- _symbolic _____yx_____y_x_GG s11InlineArrayVsRi__rlE 15MediaFoundation11SQLDatabaseV13StatementPoolC4Slot33_85DA4BD8E26B0D36C7853F6976DE6552LLV
CStrings:
+ "PRAGMA page_size"
+ "PRAGMA page_size = "
+ "PRAGMA query_only"
+ "PRAGMA query_only = "
+ "SQLDatabase.Connection"
+ "[Error] Interval already ended"
+ "cache hit statement pool"
+ "cache miss statement pool"
+ "execute statement"
+ "failed to execute statement"
+ "prepared statement"
+ "successfully executed statement"
- "?mode=memory&cache=shared"
- "index used "
```
