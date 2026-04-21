## NewsCore

> `/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore`

```diff

-5880.0.0.0.0
-  __TEXT.__text: 0x431994
+5882.0.0.0.0
+  __TEXT.__text: 0x43282c
   __TEXT.__auth_stubs: 0x3c60
-  __TEXT.__objc_methlist: 0x34d34
+  __TEXT.__objc_methlist: 0x34d9c
   __TEXT.__const: 0xdaf8
   __TEXT.__swift5_typeref: 0x40ec
   __TEXT.__constg_swiftt: 0x3174

   __TEXT.__swift5_proto: 0x994
   __TEXT.__swift5_types: 0x40c
   __TEXT.__swift5_capture: 0xe00
-  __TEXT.__oslogstring: 0x18039
+  __TEXT.__oslogstring: 0x180b3
   __TEXT.__swift5_protos: 0x68
   __TEXT.__swift_as_entry: 0x310
   __TEXT.__swift_as_ret: 0x398
-  __TEXT.__cstring: 0x55214
+  __TEXT.__cstring: 0x55319
   __TEXT.__swift5_builtin: 0x168
   __TEXT.__swift5_assocty: 0x3d0
   __TEXT.__swift5_mpenum: 0x54
-  __TEXT.__gcc_except_tab: 0x50a4
+  __TEXT.__gcc_except_tab: 0x5128
   __TEXT.__dlopen_cstrs: 0x11c
   __TEXT.__ustring: 0x280
-  __TEXT.__unwind_info: 0xfff8
+  __TEXT.__unwind_info: 0x10018
   __TEXT.__eh_frame: 0xa058
   __TEXT.__objc_classname: 0x8064
-  __TEXT.__objc_methname: 0x89888
-  __TEXT.__objc_methtype: 0xce4d
-  __TEXT.__objc_stubs: 0x35e00
+  __TEXT.__objc_methname: 0x89a08
+  __TEXT.__objc_methtype: 0xce90
+  __TEXT.__objc_stubs: 0x35f60
   __DATA_CONST.__got: 0x2bb8
-  __DATA_CONST.__const: 0x118d8
+  __DATA_CONST.__const: 0x11908
   __DATA_CONST.__objc_classlist: 0x1cc8
   __DATA_CONST.__objc_catlist: 0x298
   __DATA_CONST.__objc_protolist: 0x908
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x149d0
+  __DATA_CONST.__objc_selrefs: 0x14a20
   __DATA_CONST.__objc_protorefs: 0x258
   __DATA_CONST.__objc_superrefs: 0x15c0
   __DATA_CONST.__objc_arraydata: 0x2a88
   __AUTH_CONST.__auth_got: 0x1e48
   __AUTH_CONST.__const: 0xc2b0
-  __AUTH_CONST.__cfstring: 0x31c60
-  __AUTH_CONST.__objc_const: 0x795f0
+  __AUTH_CONST.__cfstring: 0x31cc0
+  __AUTH_CONST.__objc_const: 0x79658
   __AUTH_CONST.__objc_arrayobj: 0x6c0
-  __AUTH_CONST.__objc_intobj: 0x13c8
+  __AUTH_CONST.__objc_intobj: 0x13e0
   __AUTH_CONST.__objc_dictobj: 0xc30
   __AUTH_CONST.__objc_doubleobj: 0x120
   __AUTH.__objc_data: 0x41f0
   __AUTH.__data: 0x650
-  __DATA.__objc_ivar: 0x458c
+  __DATA.__objc_ivar: 0x4590
   __DATA.__data: 0x6798
   __DATA.__bss: 0xd3f0
   __DATA.__common: 0x90
-  __DATA_DIRTY.__objc_ivar: 0xfa0
+  __DATA_DIRTY.__objc_ivar: 0xfa4
   __DATA_DIRTY.__objc_data: 0xdf70
   __DATA_DIRTY.__data: 0x2c10
   __DATA_DIRTY.__common: 0x480

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 15ECC176-5B16-3F77-9664-89A1F61B492A
-  Functions: 24612
-  Symbols:   65914
-  CStrings:  37767
+  UUID: 2D63C71D-0F55-38E8-A420-9564EEB424EB
+  Functions: 24623
+  Symbols:   65951
+  CStrings:  37792
 
Symbols:
+ +[FCFeedTransformationSort transformationWithSortMethod:configurationSet:personalizer:feedTagID:]
+ -[FCAssertPreparedFeedPersonalizer sortItems:options:configurationSet:feedTagID:]
+ -[FCFeedTransformationPersonalizedSort feedTagID]
+ -[FCFeedTransformationPersonalizedSort setFeedTagID:]
+ -[FCKeyValueStore saveASAPWithCompletionHandler:]
+ -[FCRecordChainFetchOperation fetchedRecordHandler]
+ -[FCRecordChainFetchOperation setFetchedRecordHandler:]
+ -[FCTodayFeedConfigOperation _validateResultRecords:fetchedCKArticleRecords:]
+ -[NSDate(FCAdditions) fc_isLaterThanOrEqualTo:withPrecision:]
+ _FCCKRecipeIsSponsoredKey
+ _OBJC_IVAR_$_FCFeedTransformationPersonalizedSort._feedTagID
+ ___42-[FCTodayFeedConfigOperation _fetchFromCK]_block_invoke.30
+ ___42-[FCTodayFeedConfigOperation _fetchFromCK]_block_invoke_2.31
+ ___42-[FCTodayFeedConfigOperation _fetchFromCK]_block_invoke_4
+ ___48-[FCTodayFeedConfigOperation _fetchFromNewsEdge]_block_invoke.83
+ ___48-[FCTodayFeedConfigOperation _fetchFromNewsEdge]_block_invoke.84
+ ___48-[FCTodayFeedConfigOperation _fetchFromNewsEdge]_block_invoke.87
+ ___48-[FCTodayFeedConfigOperation _fetchFromNewsEdge]_block_invoke_2.88
+ ___49-[FCKeyValueStore saveASAPWithCompletionHandler:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48bs56bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s48l8s40l8s56l8
+ ___block_literal_global.79
+ _objc_msgSend$_validateResultRecords:fetchedCKArticleRecords:
+ _objc_msgSend$dateFormatterWithFormat:timezone:forReuse:
+ _objc_msgSend$fc_isLaterThanOrEqualTo:withPrecision:
+ _objc_msgSend$feedTagID
+ _objc_msgSend$fetchedRecordHandler
+ _objc_msgSend$saveASAPWithCompletionHandler:
+ _objc_msgSend$setFeedTagID:
+ _objc_msgSend$setFetchedRecordHandler:
+ _objc_msgSend$sortItems:options:configurationSet:feedTagID:
+ _objc_msgSend$systemTimeZone
+ _objc_msgSend$transformationWithSortMethod:configurationSet:personalizer:feedTagID:
- ___42-[FCTodayFeedConfigOperation _fetchFromCK]_block_invoke.28
- ___42-[FCTodayFeedConfigOperation _fetchFromCK]_block_invoke_2.29
- ___48-[FCTodayFeedConfigOperation _fetchFromNewsEdge]_block_invoke.81
- ___48-[FCTodayFeedConfigOperation _fetchFromNewsEdge]_block_invoke.82
- ___48-[FCTodayFeedConfigOperation _fetchFromNewsEdge]_block_invoke.85
- ___48-[FCTodayFeedConfigOperation _fetchFromNewsEdge]_block_invoke_2.86
CStrings:
+ "\nid=%@, modifiedAt=%@, fetchedAt=%@, isPaid=%@"
+ "%{public}@ config references articles:%{public}@"
+ "%{public}@ is missing article record referenced by config, id=%{public}@"
+ "-[FCTodayFeedConfigOperation _validateResultRecords:fetchedCKArticleRecords:]"
+ "@\"FCFeedPersonalizedItems\"48@0:8@\"NSArray\"16q24q32@\"NSString\"40"
+ "@48@0:8q16q24@32@40"
+ "T@\"NSString\",C,N,V_feedTagID"
+ "T@?,C,N,V_fetchedRecordHandler"
+ "_feedTagID"
+ "_fetchedRecordHandler"
+ "_validateResultRecords:fetchedCKArticleRecords:"
+ "article record returned by CK was not adopted into cache but should have been"
+ "article record was not refreshed when fetching the config"
+ "fc_isLaterThanOrEqualTo:withPrecision:"
+ "feedTagID"
+ "fetchedRecordHandler"
+ "saveASAPWithCompletionHandler:"
+ "setFeedTagID:"
+ "setFetchedRecordHandler:"
+ "sortItems:options:configurationSet:feedTagID:"
+ "systemTimeZone"
+ "transformationWithSortMethod:configurationSet:personalizer:feedTagID:"

```
