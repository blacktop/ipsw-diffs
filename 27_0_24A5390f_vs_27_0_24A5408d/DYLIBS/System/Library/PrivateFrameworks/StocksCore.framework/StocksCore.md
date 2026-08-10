## StocksCore

> `/System/Library/PrivateFrameworks/StocksCore.framework/StocksCore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
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
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__objc_stublist`
- `__DATA_DIRTY.__objc_data`

```diff

-2022.0.0.0.0
-  __TEXT.__text: 0x256844
-  __TEXT.__objc_methlist: 0x6c04
+2028.1.0.0.0
+  __TEXT.__text: 0x257afc
+  __TEXT.__objc_methlist: 0x6c2c
   __TEXT.__const: 0x1d5c0
-  __TEXT.__cstring: 0xffc0
-  __TEXT.__gcc_except_tab: 0x2b8
-  __TEXT.__oslogstring: 0x3405
+  __TEXT.__cstring: 0x10010
+  __TEXT.__gcc_except_tab: 0x334
+  __TEXT.__oslogstring: 0x3665
   __TEXT.__ustring: 0x28
   __TEXT.__swift5_typeref: 0x5667
   __TEXT.__swift5_capture: 0x2344

   __TEXT.__swift_as_entry: 0x294
   __TEXT.__swift_as_ret: 0x2b4
   __TEXT.__swift_as_cont: 0x490
-  __TEXT.__unwind_info: 0x95f8
+  __TEXT.__unwind_info: 0x9630
   __TEXT.__eh_frame: 0xd094
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x3d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3738
+  __DATA_CONST.__objc_selrefs: 0x3750
   __DATA_CONST.__objc_protorefs: 0x1c8
   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0xf58
-  __DATA_CONST.__got: 0x12c0
+  __DATA_CONST.__got: 0x12d8
   __AUTH_CONST.__const: 0x17c58
-  __AUTH_CONST.__cfstring: 0x1580
-  __AUTH_CONST.__objc_const: 0x14260
+  __AUTH_CONST.__cfstring: 0x15c0
+  __AUTH_CONST.__objc_const: 0x14278
   __AUTH_CONST.__objc_arrayobj: 0x618
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH_CONST.__auth_got: 0x2470
+  __AUTH_CONST.__auth_got: 0x2478
   __AUTH.__objc_data: 0x240
   __AUTH.__data: 0x120
   __DATA.__objc_ivar: 0x320
-  __DATA.__data: 0x43d0
+  __DATA.__data: 0x4410
   __DATA.__objc_stublist: 0x60
   __DATA.__bss: 0x18d40
+  __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x2358
-  __DATA_DIRTY.__data: 0xb5e0
+  __DATA_DIRTY.__data: 0xb5c0
   __DATA_DIRTY.__bss: 0x17a40
-  __DATA_DIRTY.__common: 0x208
+  __DATA_DIRTY.__common: 0x1f0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/Frameworks/EventKit.framework/EventKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
+  - /System/Library/PrivateFrameworks/AppPrivateData.framework/AppPrivateData
   - /System/Library/PrivateFrameworks/NewsCore.framework/NewsCore
   - /System/Library/PrivateFrameworks/NewsTransport.framework/NewsTransport
   - /System/Library/PrivateFrameworks/OAuth.framework/OAuth

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13741
-  Symbols:   6336
-  CStrings:  1884
+  Functions: 13770
+  Symbols:   6346
+  CStrings:  1895
 
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
+ GCC_except_table100
+ GCC_except_table113
+ GCC_except_table117
+ GCC_except_table123
+ GCC_except_table14
+ GCC_except_table17
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table91
+ GCC_except_table97
+ _NSCocoaErrorDomain
+ _NSLocalizedDescriptionKey
+ _NSPOSIXErrorDomain
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
+ ___58-[SCWFauxDatabaseStoreCoordinator readWithError:accessor:]_block_invoke
+ ___59-[SCWFauxDatabaseStoreCoordinator readZone:error:accessor:]_block_invoke
+ ___59-[SCWFauxDatabaseStoreCoordinator writeWithError:accessor:]_block_invoke
+ ___60-[SCWFauxDatabaseStoreCoordinator reloadWithError:accessor:]_block_invoke
+ ___60-[SCWFauxDatabaseStoreCoordinator writeZone:error:accessor:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e28_v16?0"<SCWDatabaseStore>"8ls40l8s32l8
+ ___block_descriptor_56_e8_32bs40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40bs48r_e15_v16?0"NSURL"8ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e24_v16?0"<SCWZoneStore>"8lr48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e17_v16?0"NSError"8lr64l8s32l8s40l8s56l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56bs64r72r_e5_v8?0ls32l8s40l8r64l8r72l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e74_v44?0"CKRecordZoneID"8"CKServerChangeToken"16"NSData"24B32"NSError"36ls32l8s40l8s48l8s56l8s64l8r80l8s72l8
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
- GCC_except_table110
- GCC_except_table114
- GCC_except_table120
- GCC_except_table35
- GCC_except_table90
- GCC_except_table95
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSError_$_SCWAdditions
- ___41-[SCWDatabaseJSONStore readWithAccessor:]_block_invoke
- ___41-[SCWDatabaseJSONStore readWithAccessor:]_block_invoke_2
- ___41-[SCWDatabaseJSONStore readWithAccessor:]_block_invoke_3
- ___42-[SCWDatabaseJSONStore writeWithAccessor:]_block_invoke
- ___42-[SCWDatabaseJSONStore writeWithAccessor:]_block_invoke_2
- ___43-[SCWDatabaseJSONStore reloadWithAccessor:]_block_invoke
- ___43-[SCWDatabaseJSONStore reloadWithAccessor:]_block_invoke_2
- ___46-[SCWDatabaseJSONStore readZone:withAccessor:]_block_invoke
- ___47-[SCWDatabaseJSONStore writeZone:withAccessor:]_block_invoke
- ___48-[SCWDatabase modifyContentsOfZone:withCommand:]_block_invoke_4
- ___48-[SCWDatabase modifyContentsOfZone:withCommand:]_block_invoke_5
- ___52-[SCWFauxDatabaseStoreCoordinator readWithAccessor:]_block_invoke
- ___53-[SCWFauxDatabaseStoreCoordinator writeWithAccessor:]_block_invoke
- ___54-[SCWDatabase _recoverFromIdentityLossWithCompletion:]_block_invoke_4
- ___54-[SCWFauxDatabaseStoreCoordinator reloadWithAccessor:]_block_invoke
- ___57-[SCWFauxDatabaseStoreCoordinator readZone:withAccessor:]_block_invoke
- ___58-[SCWFauxDatabaseStoreCoordinator writeZone:withAccessor:]_block_invoke
- ___block_descriptor_48_e8_32bs40r_e5_v8?0ls32l8r40l8
- ___block_descriptor_48_e8_32s40bs_e15_v16?0"NSURL"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e28_v16?0"<SCWDatabaseStore>"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e28_v16?0"<SCWDatabaseStore>"8ls48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48bs56r_e24_v16?0"<SCWZoneStore>"8lr56l8s32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s40l8s56l8s48l8
- ___block_descriptor_72_e8_32s40s48s56bs64r_e5_v8?0ls32l8s40l8r64l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e74_v44?0"CKRecordZoneID"8"CKServerChangeToken"16"NSData"24B32"NSError"36ls32l8s40l8s48l8s56l8s64l8s72l8
- ___swift_closure_destructor.20Tm
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
