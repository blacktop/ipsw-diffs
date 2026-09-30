## StocksCore

> `/System/Library/PrivateFrameworks/StocksCore.framework/Versions/A/StocksCore`

```diff

-2022.0.0.0.0
-  __TEXT.__text: 0x25e134
-  __TEXT.__objc_methlist: 0x6c04
+2028.0.0.0.0
+  __TEXT.__text: 0x25f608
+  __TEXT.__objc_methlist: 0x6c2c
   __TEXT.__const: 0x1d5b0
-  __TEXT.__cstring: 0xff10
-  __TEXT.__gcc_except_tab: 0x2b8
-  __TEXT.__oslogstring: 0x3405
+  __TEXT.__cstring: 0xff60
+  __TEXT.__gcc_except_tab: 0x334
+  __TEXT.__oslogstring: 0x3665
   __TEXT.__ustring: 0x28
   __TEXT.__swift5_typeref: 0x5667
   __TEXT.__swift5_capture: 0x2344

   __TEXT.__swift_as_entry: 0x294
   __TEXT.__swift_as_ret: 0x2b4
   __TEXT.__swift_as_cont: 0x490
-  __TEXT.__unwind_info: 0x9488
+  __TEXT.__unwind_info: 0x94f8
   __TEXT.__eh_frame: 0xd07c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x3d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3720
+  __DATA_CONST.__objc_selrefs: 0x3738
   __DATA_CONST.__objc_protorefs: 0x1c8
   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0xf58
-  __DATA_CONST.__got: 0x12b8
-  __AUTH_CONST.__const: 0x18ad8
-  __AUTH_CONST.__cfstring: 0x1520
-  __AUTH_CONST.__objc_const: 0x14260
+  __DATA_CONST.__got: 0x12d0
+  __AUTH_CONST.__const: 0x18aa8
+  __AUTH_CONST.__cfstring: 0x1560
+  __AUTH_CONST.__objc_const: 0x14278
   __AUTH_CONST.__objc_arrayobj: 0x618
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x22a8
+  __AUTH_CONST.__auth_got: 0x22b0
   __AUTH.__objc_data: 0x240
   __AUTH.__data: 0x120
   __DATA.__objc_ivar: 0x320
-  __DATA.__data: 0x4380
+  __DATA.__data: 0x43b0
   __DATA.__objc_stublist: 0x60
   __DATA.__bss: 0x18cc0
+  __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x2358
-  __DATA_DIRTY.__data: 0xb5f0
+  __DATA_DIRTY.__data: 0xb5c0
   __DATA_DIRTY.__bss: 0x17ab0
-  __DATA_DIRTY.__common: 0x208
+  __DATA_DIRTY.__common: 0x1f0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /System/Library/Frameworks/EventKit.framework/Versions/A/EventKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
+  - /System/Library/PrivateFrameworks/AppPrivateData.framework/Versions/A/AppPrivateData
   - /System/Library/PrivateFrameworks/NewsCore.framework/Versions/A/NewsCore
   - /System/Library/PrivateFrameworks/NewsTransport.framework/Versions/A/NewsTransport
   - /System/Library/PrivateFrameworks/OAuth.framework/Versions/A/OAuth

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13788
-  Symbols:   6350
-  CStrings:  1875
+  Functions: 13819
+  Symbols:   6370
+  CStrings:  1886
 
Symbols:
+ +[NSError(SCWAdditions) scw_databaseDecodeErrorWithUnderlyingError:]
+ +[NSError(SCWAdditions) scw_databaseReadErrorWithUnderlyingError:]
+ -[NSError(SCWAdditions) scw_isFileNotFoundError]
+ -[SCWDatabaseJSONStore _loadFromFileURL:error:]
+ -[SCWDatabaseJSONStore _reloadIfNeededFromFileURL:didReload:error:]
+ -[SCWDatabaseJSONStore readWithError:accessor:]
+ -[SCWDatabaseJSONStore readZone:error:accessor:]
+ -[SCWDatabaseJSONStore reloadWithError:accessor:]
+ -[SCWDatabaseJSONStore writeWithError:accessor:]
+ -[SCWDatabaseJSONStore writeZone:error:accessor:]
+ -[SCWFauxDatabaseStoreCoordinator readWithError:accessor:]
+ -[SCWFauxDatabaseStoreCoordinator readZone:error:accessor:]
+ -[SCWFauxDatabaseStoreCoordinator reloadWithError:accessor:]
+ -[SCWFauxDatabaseStoreCoordinator writeWithError:accessor:]
+ -[SCWFauxDatabaseStoreCoordinator writeZone:error:accessor:]
+ GCC_except_table112
+ GCC_except_table120
+ GCC_except_table129
+ GCC_except_table148
+ GCC_except_table154
+ GCC_except_table161
+ GCC_except_table18
+ GCC_except_table21
+ GCC_except_table46
+ GCC_except_table54
+ _NSCocoaErrorDomain
+ _NSLocalizedDescriptionKey
+ _NSPOSIXErrorDomain
+ __46-[SCWWatchlistManager _enqueueStartupSequence]_block_invoke_3
+ __47-[SCWDatabaseJSONStore readWithError:accessor:]_block_invoke
+ __51-[SCWDatabase _enqueueStartupSequenceWithFeatures:]_block_invoke_6
+ __54-[SCWDatabase _recoverFromIdentityLossWithCompletion:]_block_invoke
+ __54-[SCWDatabase _recoverFromIdentityLossWithCompletion:]_block_invoke_2
+ __OBJC_$_CLASS_METHODS_NSError(SCWAdditions|SCWAdditions)
+ __OBJC_$_INSTANCE_METHODS_NSError(SCWAdditions|SCWAdditions)
+ ___47-[SCWDatabaseJSONStore readWithError:accessor:]_block_invoke
+ ___47-[SCWDatabaseJSONStore readWithError:accessor:]_block_invoke_2
+ ___48-[SCWDatabaseJSONStore readZone:error:accessor:]_block_invoke
+ ___48-[SCWDatabaseJSONStore writeWithError:accessor:]_block_invoke
+ ___48-[SCWDatabaseJSONStore writeWithError:accessor:]_block_invoke_2
+ ___49-[SCWDatabaseJSONStore reloadWithError:accessor:]_block_invoke
+ ___49-[SCWDatabaseJSONStore reloadWithError:accessor:]_block_invoke_2
+ ___49-[SCWDatabaseJSONStore writeZone:error:accessor:]_block_invoke
+ ___51-[SCWDatabase _enqueueStartupSequenceWithFeatures:]_block_invoke_7
+ ___58-[SCWFauxDatabaseStoreCoordinator readWithError:accessor:]_block_invoke
+ ___59-[SCWFauxDatabaseStoreCoordinator readZone:error:accessor:]_block_invoke
+ ___59-[SCWFauxDatabaseStoreCoordinator writeWithError:accessor:]_block_invoke
+ ___60-[SCWFauxDatabaseStoreCoordinator reloadWithError:accessor:]_block_invoke
+ ___60-[SCWFauxDatabaseStoreCoordinator writeZone:error:accessor:]_block_invoke
+ ___block_descriptor_56_e8_32bs40r48r_e5_v8?0l
+ ___block_descriptor_56_e8_32s40bs48r_e15_v16?0"NSURL"8l
+ ___block_descriptor_56_e8_32s40s48r_e24_v16?0"<SCWZoneStore>"8l
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e17_v16?0"NSError"8l
+ ___block_descriptor_80_e8_32s40s48s56bs64r72r_e5_v8?0l
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e74_v44?0"CKRecordZoneID"8"CKServerChangeToken"16"NSData"24B32"NSError"36l
+ ___copy_helper_block_e8_32b40r48r
+ ___copy_helper_block_e8_32s40s48s56b64r72r
+ ___copy_helper_block_e8_32s40s48s56s64s72b80r
+ ___destroy_helper_block_e8_32s40r48r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80r
+ _objc_autorelease
+ _objc_msgSend$_loadFromFileURL:error:
+ _objc_msgSend$_reloadIfNeededFromFileURL:didReload:error:
+ _objc_msgSend$readWithError:accessor:
+ _objc_msgSend$readZone:error:accessor:
+ _objc_msgSend$reloadWithError:accessor:
+ _objc_msgSend$scw_databaseDecodeErrorWithUnderlyingError:
+ _objc_msgSend$scw_databaseReadErrorWithUnderlyingError:
+ _objc_msgSend$scw_isFileNotFoundError
+ _objc_msgSend$writeWithError:accessor:
+ _objc_msgSend$writeZone:error:accessor:
- -[SCWDatabaseJSONStore _loadFromFileURL:]
- -[SCWDatabaseJSONStore _reloadIfNeededFromFileURL:]
- -[SCWDatabaseJSONStore readWithAccessor:]
- -[SCWDatabaseJSONStore readZone:withAccessor:]
- -[SCWDatabaseJSONStore reloadWithAccessor:]
- -[SCWDatabaseJSONStore writeWithAccessor:]
- -[SCWDatabaseJSONStore writeZone:withAccessor:]
- -[SCWFauxDatabaseStoreCoordinator readWithAccessor:]
- -[SCWFauxDatabaseStoreCoordinator readZone:withAccessor:]
- -[SCWFauxDatabaseStoreCoordinator reloadWithAccessor:]
- -[SCWFauxDatabaseStoreCoordinator writeWithAccessor:]
- -[SCWFauxDatabaseStoreCoordinator writeZone:withAccessor:]
- GCC_except_table108
- GCC_except_table115
- GCC_except_table141
- GCC_except_table147
- GCC_except_table155
- GCC_except_table44
- GCC_except_table51
- __41-[SCWDatabaseJSONStore readWithAccessor:]_block_invoke
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSError_$_SCWAdditions
- ___41-[SCWDatabaseJSONStore readWithAccessor:]_block_invoke
- ___41-[SCWDatabaseJSONStore readWithAccessor:]_block_invoke_2
- ___42-[SCWDatabaseJSONStore writeWithAccessor:]_block_invoke
- ___42-[SCWDatabaseJSONStore writeWithAccessor:]_block_invoke_2
- ___43-[SCWDatabaseJSONStore reloadWithAccessor:]_block_invoke
- ___43-[SCWDatabaseJSONStore reloadWithAccessor:]_block_invoke_2
- ___46-[SCWDatabaseJSONStore readZone:withAccessor:]_block_invoke
- ___47-[SCWDatabaseJSONStore writeZone:withAccessor:]_block_invoke
- ___52-[SCWFauxDatabaseStoreCoordinator readWithAccessor:]_block_invoke
- ___53-[SCWFauxDatabaseStoreCoordinator writeWithAccessor:]_block_invoke
- ___54-[SCWDatabase _recoverFromIdentityLossWithCompletion:]_block_invoke_4
- ___54-[SCWFauxDatabaseStoreCoordinator reloadWithAccessor:]_block_invoke
- ___57-[SCWFauxDatabaseStoreCoordinator readZone:withAccessor:]_block_invoke
- ___58-[SCWFauxDatabaseStoreCoordinator writeZone:withAccessor:]_block_invoke
- ___block_descriptor_48_e8_32bs40r_e5_v8?0l
- ___block_descriptor_48_e8_32s40bs_e15_v16?0"NSURL"8l
- ___block_descriptor_56_e8_32s40s48bs_e28_v16?0"<SCWDatabaseStore>"8l
- ___block_descriptor_64_e8_32s40s48bs56r_e24_v16?0"<SCWZoneStore>"8l
- ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8l
- ___block_descriptor_72_e8_32s40s48s56bs64r_e5_v8?0l
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e74_v44?0"CKRecordZoneID"8"CKServerChangeToken"16"NSData"24B32"NSError"36l
- ___copy_helper_block_e8_32s40s48s56b
- __swift_closure_destructor.20Tm
- _objc_msgSend$_loadFromFileURL:
- _objc_msgSend$_reloadIfNeededFromFileURL:
- _objc_msgSend$readWithAccessor:
- _objc_msgSend$readZone:withAccessor:
- _objc_msgSend$reloadWithAccessor:
- _objc_msgSend$writeWithAccessor:
- _objc_msgSend$writeZone:withAccessor:
CStrings:
+ "%p JSON store failed to decode JSON from disk with error: %{public}@"
+ "%p JSON store failed to load from disk with error: %{public}@"
+ "%p JSON store failed to read with error: %{public}@"
+ "%p JSON store failed to reload with error: %{public}@"
+ "%p JSON store failed to write with error: %{public}@"
+ "The on-disk database store could not be decoded."
+ "The on-disk database store could not be read."
+ "failed to load zones from disk at startup with error: %{public}@"
+ "ignoring empty watchlist zone due to error: %{public}@"
+ "skipping database changes fetch because the store could not be read: %{public}@"
+ "skipping identity-loss recovery because the store could not be written: %{public}@"
+ "skipping modification of zone %{public}@ because the store could not be written: %{public}@"
- "%p failed to decode database JSON with error: %{public}@"
```
