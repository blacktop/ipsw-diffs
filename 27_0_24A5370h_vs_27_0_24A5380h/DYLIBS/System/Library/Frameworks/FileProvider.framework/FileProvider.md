## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/FileProvider`

```diff

-  __TEXT.__text: 0x12bafc
-  __TEXT.__objc_methlist: 0xe8a4
+  __TEXT.__text: 0x12d0ac
+  __TEXT.__objc_methlist: 0xe97c
   __TEXT.__const: 0x88a
-  __TEXT.__cstring: 0x14d8f
-  __TEXT.__gcc_except_tab: 0x8a54
-  __TEXT.__oslogstring: 0xe2b3
+  __TEXT.__cstring: 0x14e47
+  __TEXT.__gcc_except_tab: 0x8af8
+  __TEXT.__oslogstring: 0xe335
   __TEXT.__dlopen_cstrs: 0x793
   __TEXT.__ustring: 0x21e
   __TEXT.__swift5_typeref: 0xb4

   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x58c0
+  __TEXT.__unwind_info: 0x5910
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6188
-  __DATA_CONST.__objc_classlist: 0x690
+  __DATA_CONST.__const: 0x61f8
+  __DATA_CONST.__objc_classlist: 0x698
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7028
+  __DATA_CONST.__objc_selrefs: 0x70a8
   __DATA_CONST.__objc_protorefs: 0x158
-  __DATA_CONST.__objc_superrefs: 0x548
+  __DATA_CONST.__objc_superrefs: 0x550
   __DATA_CONST.__objc_arraydata: 0xab0
-  __DATA_CONST.__got: 0xad0
+  __DATA_CONST.__got: 0xb18
   __AUTH_CONST.__const: 0x1da8
-  __AUTH_CONST.__cfstring: 0x114e0
-  __AUTH_CONST.__objc_const: 0x24e58
+  __AUTH_CONST.__cfstring: 0x115a0
+  __AUTH_CONST.__objc_const: 0x25008
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__auth_got: 0xeb0
-  __AUTH.__objc_data: 0x4b0
+  __AUTH.__objc_data: 0x25f8
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x10c0
+  __DATA.__objc_ivar: 0x10d4
   __DATA.__data: 0x23f0
-  __DATA.__bss: 0xc20
+  __DATA.__bss: 0xc30
   __DATA.__common: 0x39
-  __DATA_DIRTY.__objc_data: 0x3cf0
+  __DATA_DIRTY.__objc_data: 0x1bf8
   __DATA_DIRTY.__data: 0x1
   __DATA_DIRTY.__bss: 0x2e8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  Functions: 7422
-  Symbols:   23942
-  CStrings:  6243
+  Functions: 7453
+  Symbols:   24035
+  CStrings:  6260
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Symbols:
+ +[FPFINodeSession sharedSession]
+ +[NSFileManager(FPAdditionsTesting) _test_flushFINodeSession]
+ +[NSFileManager(FPAdditionsTesting) _test_setFINodeSessionIdleTimeout:]
+ -[FPFINodeSession .cxx_destruct]
+ -[FPFINodeSession enter]
+ -[FPFINodeSession flushForTesting]
+ -[FPFINodeSession init]
+ -[FPFINodeSession leave]
+ -[FPFINodeSession setIdleTimeoutForTesting:]
+ -[FPItemManager _fetchSearchableItemIdentifiersForURL:synchronously:skipURLValidation:completionHandler:]
+ -[FPItemManager fetchSearchableItemIdentifiersForURL:completionHandler:]
+ -[FPItemManager searchableItemIdentifiersForURL:error:]
+ GCC_except_table121
+ GCC_except_table136
+ GCC_except_table77
+ _FPFileLockedByFlock
+ _FPURLIsKnownCiaoLocalStorage
+ _OBJC_CLASS_$_FPFINodeSession
+ _OBJC_IVAR_$_FPFINodeSession._generation
+ _OBJC_IVAR_$_FPFINodeSession._idleTimeout
+ _OBJC_IVAR_$_FPFINodeSession._outstanding
+ _OBJC_IVAR_$_FPFINodeSession._pendingGeneration
+ _OBJC_IVAR_$_FPFINodeSession._queue
+ _OBJC_METACLASS_$_FPFINodeSession
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSFileManager_$_FPAdditionsTesting
+ __OBJC_$_CATEGORY_NSFileManager_$_FPAdditionsTesting
+ __OBJC_$_CLASS_METHODS_FPFINodeSession
+ __OBJC_$_INSTANCE_METHODS_FPFINodeSession
+ __OBJC_$_INSTANCE_METHODS_NSFileManager(FPAdditionsTesting|FPAdditions)
+ __OBJC_$_INSTANCE_VARIABLES_FPFINodeSession
+ __OBJC_CLASS_RO_$_FPFINodeSession
+ __OBJC_METACLASS_RO_$_FPFINodeSession
+ ___105-[FPItemManager _fetchSearchableItemIdentifiersForURL:synchronously:skipURLValidation:completionHandler:]_block_invoke
+ ___24-[FPFINodeSession enter]_block_invoke
+ ___24-[FPFINodeSession leave]_block_invoke
+ ___24-[FPFINodeSession leave]_block_invoke_2
+ ___32+[FPFINodeSession sharedSession]_block_invoke
+ ___34-[FPFINodeSession flushForTesting]_block_invoke
+ ___44-[FPFINodeSession setIdleTimeoutForTesting:]_block_invoke
+ ___55-[FPItemManager searchableItemIdentifiersForURL:error:]_block_invoke
+ ___block_descriptor_40_e8_32s_e60_"FIOperationReply"24?0"FIOperation"8"FIOperationError"16ls32l8
+ ___block_descriptor_48_e8_32s40r_e60_"FIOperationReply"24?0"FIOperation"8"FIOperationError"16lr40l8s32l8
+ ___block_descriptor_48_e8_i12?0i8l
+ ___block_descriptor_56_e8_32s40r48r_e33_v24?0"FIOperation"8"NSArray"16lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___fpfs_get_purgeable_info_at_block_invoke
+ ___fpfs_unset_purgeable_at_block_invoke
+ _fpfs_get_purgeable_info_at
+ _fpfs_query_purgeable_bytes
+ _fpfs_unset_purgeable_at
+ _objc_msgSend$_fetchSearchableItemIdentifiersForURL:synchronously:skipURLValidation:completionHandler:
+ _objc_msgSend$cancelled
+ _objc_msgSend$end
+ _objc_msgSend$enter
+ _objc_msgSend$flushForTesting
+ _objc_msgSend$initWithResolution:error:
+ _objc_msgSend$leave
+ _objc_msgSend$listOfMonitoredApps
+ _objc_msgSend$searchableItemIdentifiersForURL:completionHandler:
+ _objc_msgSend$setIdleTimeoutForTesting:
+ _objc_msgSend$setWarningHandler:
+ _objc_msgSend$sharedRegistryIfAvailable
+ _objc_msgSend$sharedSession
+ _sharedSession.once
+ _sharedSession.sharedSession
- GCC_except_table131
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSFileManager_$_FPAdditions
- __OBJC_$_CATEGORY_NSFileManager_$_FPAdditions
- ___71-[NSFileManager(FPAdditions) fp_trashItemAtURL:resultingItemURL:error:]_block_invoke_2
- ___block_descriptor_40_e8_32r_e60_"FIOperationReply"24?0"FIOperation"8"FIOperationError"16lr32l8
- ___block_descriptor_48_e8_32s40r_e33_v24?0"FIOperation"8"NSArray"16lr40l8s32l8
- ___fpfs_t_unset_evictable_at_block_invoke
- _fpfs_t_unset_evictable_at
- _objc_msgSend$executedAsFPAction
CStrings:
+ "/private/var/mobile/Containers/"
+ "/var/mobile/Containers/"
+ "4838.0.70"
+ "FIOperationReply"
+ "FileLockedByFlock"
+ "NSFileManager+FPAdditions.m"
+ "[DEBUG] Item got trashed at %@ (%@)"
+ "[DEBUG] Trashing %@ failed with %@"
+ "[DEBUG] Trashing %@ got a warning: %@"
+ "[ERROR] Couldn't get a FIMoveToTrashOperation for trashing"
+ "[ERROR] Couldn't get a FINode for trashing"
+ "com.apple.FileProvider.FINodeSession"
+ "pending close with outstanding=%d"
- "4838.0.29.502.2"
- "[WARNING] Trashing going through FP instead of DS - probably not the expectation"

```
