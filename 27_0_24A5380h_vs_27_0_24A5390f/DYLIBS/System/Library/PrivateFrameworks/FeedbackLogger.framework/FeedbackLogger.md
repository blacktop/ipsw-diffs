## FeedbackLogger

> `/System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_assocty`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-3600.56.16.0.0
-  __TEXT.__text: 0x1c200
-  __TEXT.__objc_methlist: 0x117c
-  __TEXT.__const: 0x1490
+3600.56.21.0.0
+  __TEXT.__text: 0x1d25c
+  __TEXT.__objc_methlist: 0x11fc
+  __TEXT.__const: 0x14a0
   __TEXT.__swift5_typeref: 0x4e7
   __TEXT.__swift5_fieldmd: 0x3f4
   __TEXT.__constg_swiftt: 0x288
-  __TEXT.__cstring: 0x2026
+  __TEXT.__cstring: 0x2081
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x10c
   __TEXT.__swift5_types: 0x38
   __TEXT.__swift5_reflstr: 0x2fd
   __TEXT.__swift5_capture: 0xec
-  __TEXT.__oslogstring: 0x1b54
+  __TEXT.__oslogstring: 0x1cfe
   __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__gcc_except_tab: 0x1e4
-  __TEXT.__unwind_info: 0x9e0
+  __TEXT.__gcc_except_tab: 0x260
+  __TEXT.__unwind_info: 0xa30
   __TEXT.__eh_frame: 0x538
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x360
+  __DATA_CONST.__const: 0x428
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc30
+  __DATA_CONST.__objc_selrefs: 0xc88
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__objc_arraydata: 0x18
+  __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__got: 0x2a0
   __AUTH_CONST.__const: 0x778
   __AUTH_CONST.__cfstring: 0x920
-  __AUTH_CONST.__objc_const: 0x19d0
-  __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__objc_const: 0x1a60
+  __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x878
+  __AUTH_CONST.__auth_got: 0x880
   __AUTH.__objc_data: 0x168
   __AUTH.__data: 0x3d0
-  __DATA.__objc_ivar: 0x120
+  __DATA.__objc_ivar: 0x12c
   __DATA.__data: 0x558
   __DATA.__common: 0xf8
   __DATA.__bss: 0x2080

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 909
-  Symbols:   1285
-  CStrings:  332
+  Functions: 926
+  Symbols:   1322
+  CStrings:  340
 
Symbols:
+ -[FLLogger _dispatchCleanupWithWatchdog]
+ -[FLLogger _dispatchPersistWithWatchdogForStoreID:category:payloadSize:writeTransaction:persistor:completion:]
+ -[FLLogger _persistentStoreKeyForStoreId:category:]
+ -[FLLogger cleanupWatchdogTimeout]
+ -[FLLogger persistWatchdogTimeout]
+ -[FLLogger reportCACleanupTimeout]
+ -[FLLogger reportCAPersistTimeoutFromBundleID:category:size:]
+ -[FLLogger setCleanupWatchdogTimeout:]
+ -[FLLogger setPersistWatchdogTimeout:]
+ -[FLLogger setWatchdogQueue:]
+ -[FLLogger watchdogQueue]
+ GCC_except_table102
+ GCC_except_table119
+ GCC_except_table180
+ GCC_except_table249
+ GCC_except_table274
+ GCC_except_table348
+ GCC_except_table47
+ GCC_except_table66
+ GCC_except_table68
+ GCC_except_table70
+ GCC_except_table72
+ GCC_except_table78
+ GCC_except_table83
+ GCC_except_table85
+ GCC_except_table89
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_IVAR_$_FLLogger._cleanupWatchdogTimeout
+ _OBJC_IVAR_$_FLLogger._persistWatchdogTimeout
+ _OBJC_IVAR_$_FLLogger._watchdogQueue
+ ___110-[FLLogger _dispatchPersistWithWatchdogForStoreID:category:payloadSize:writeTransaction:persistor:completion:]_block_invoke
+ ___40-[FLLogger _dispatchCleanupWithWatchdog]_block_invoke
+ ___52-[FLLogger write:category:toStoreWithID:completion:]_block_invoke_2
+ ___75-[FLLogger reportDataPlatformBatchedEvent:forBundleID:ofSchema:completion:]_block_invoke_2
+ ___block_descriptor_104_e8_32s40s48s56s64s72bs80bs88r96r_e5_v8?0lr88l8s32l8s40l8s48l8s56l8r96l8s72l8s64l8s80l8
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
+ ___block_descriptor_48_e8_32bs40r_e17_v16?0"NSError"8lr40l8s32l8
+ ___block_descriptor_48_e8_32r40w_e5_v8?0lw40l8r32l8
+ ___block_descriptor_48_e8_32s40s_e38_"NSError"16?0"FLSQLitePersistence"8ls32l8s40l8
+ ___block_descriptor_80_e8_32s40s48bs56r64w_e5_v8?0lr56l8w64l8s32l8s40l8s48l8
+ _objc_msgSend$_dispatchCleanupWithWatchdog
+ _objc_msgSend$_dispatchPersistWithWatchdogForStoreID:category:payloadSize:writeTransaction:persistor:completion:
+ _objc_msgSend$_persistentStoreKeyForStoreId:category:
+ _objc_msgSend$cleanupWatchdogTimeout
+ _objc_msgSend$dbConnection
+ _objc_msgSend$persistWatchdogTimeout
+ _objc_msgSend$reportCACleanupTimeout
+ _objc_msgSend$reportCAPersistTimeoutFromBundleID:category:size:
+ _sqlite3_interrupt
- GCC_except_table163
- GCC_except_table232
- GCC_except_table257
- GCC_except_table331
- GCC_except_table41
- GCC_except_table59
- GCC_except_table63
- GCC_except_table65
- GCC_except_table71
- GCC_except_table88
- GCC_except_table90
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s72l8s64l8
CStrings:
+ "@\"NSError\"16@?0@\"FLSQLitePersistence\"8"
+ "Cleanup completed via watchdog interrupt path"
+ "Cleanup watchdog fired — interrupting cached SQLite connections to break TTL-cleanup deadlock"
+ "Persist for store (%{public}@, %{public}@) skipped — watchdog fired before FBF block could run"
+ "Persist for store (%{public}@, %{public}@) was interrupted by watchdog; inner err=%@"
+ "Persist watchdog fired for store (%{public}@, %{public}@) — interrupting in-flight SQLite operation"
+ "com.apple.feedbacklogger.watchdog"
+ "v16@?0@\"NSError\"8"
```
