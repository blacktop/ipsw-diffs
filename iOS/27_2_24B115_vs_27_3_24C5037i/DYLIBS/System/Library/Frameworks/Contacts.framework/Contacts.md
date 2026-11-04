## Contacts

> `/System/Library/Frameworks/Contacts.framework/Contacts`

```diff

-3846.200.91.2.1
-  __TEXT.__text: 0x212d7c
-  __TEXT.__objc_methlist: 0x1be98
+3846.300.21.0.0
+  __TEXT.__text: 0x214c68
+  __TEXT.__objc_methlist: 0x1bfd8
   __TEXT.__const: 0x4c60
-  __TEXT.__gcc_except_tab: 0x3c3c
-  __TEXT.__cstring: 0xcc39
-  __TEXT.__dlopen_cstrs: 0x97e
-  __TEXT.__oslogstring: 0xf83a
+  __TEXT.__gcc_except_tab: 0x3ca0
+  __TEXT.__cstring: 0xcce9
+  __TEXT.__dlopen_cstrs: 0xa28
+  __TEXT.__oslogstring: 0xf9ba
   __TEXT.__ustring: 0x12
   __TEXT.__constg_swiftt: 0x16d4
   __TEXT.__swift5_typeref: 0x1b0f

   __TEXT.__swift_as_entry: 0xb8
   __TEXT.__swift_as_ret: 0xe0
   __TEXT.__swift_as_cont: 0x158
-  __TEXT.__unwind_info: 0xbab8
+  __TEXT.__unwind_info: 0xbb38
   __TEXT.__eh_frame: 0x4000
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6728
-  __DATA_CONST.__objc_classlist: 0x11b0
+  __DATA_CONST.__const: 0x6780
+  __DATA_CONST.__objc_classlist: 0x11c0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9d88
+  __DATA_CONST.__objc_selrefs: 0x9e48
   __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0xa20
+  __DATA_CONST.__objc_superrefs: 0xa28
   __DATA_CONST.__objc_arraydata: 0x268
-  __DATA_CONST.__got: 0x1db8
-  __AUTH_CONST.__const: 0x9258
-  __AUTH_CONST.__cfstring: 0xdfc0
-  __AUTH_CONST.__objc_const: 0x2dbe0
+  __DATA_CONST.__got: 0x1dc0
+  __AUTH_CONST.__const: 0x92b8
+  __AUTH_CONST.__cfstring: 0xe040
+  __AUTH_CONST.__objc_const: 0x2de88
   __AUTH_CONST.__objc_intobj: 0x5e8
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x1de8
-  __AUTH.__objc_data: 0x5e00
+  __AUTH.__objc_data: 0x5ea0
   __AUTH.__data: 0x860
-  __DATA.__objc_ivar: 0x1330
+  __DATA.__objc_ivar: 0x1350
   __DATA.__data: 0x3ab8
   __DATA.__common: 0xa0
   __DATA_DIRTY.__objc_data: 0x6368
   __DATA_DIRTY.__data: 0x58
-  __DATA_DIRTY.__bss: 0x1128
+  __DATA_DIRTY.__bss: 0x1158
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ClassKit.framework/ClassKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14239
-  Symbols:   20175
-  CStrings:  3456
+  Functions: 14275
+  Symbols:   20232
+  CStrings:  3464
 
Symbols:
+ +[CNFakeSensitiveNicknameProvider makeIfEnabled]
+ +[CNiOSContactFetcher contactsForFetchRequest:matchInfos:inAddressBook:environment:managedConfiguration:authorizationContext:error:]
+ +[CNiOSContactFetcher os_log]
+ +[CNiOSFetchExecution contactsMatchingPredicates:sortOrdering:matchInfos:options:addressBook:authorizationContext:environment:error:]
+ +[CNiOSFetchExecution contactsMatchingPredicates:sortOrdering:options:addressBook:authorizationContext:progressiveResults:completion:environment:]
+ +[CNiOSPersonFetchRequest(CNConversion) fetchRequestFromCNFetchRequest:managedConfiguration:authorizationContext:error:]
+ +[_CNABPredicateObservable observableWithPredicates:sortOrdering:options:addressBook:authorizationContext:environment:]
+ -[CNFakeSensitiveIMNicknameProvider .cxx_destruct]
+ -[CNFakeSensitiveIMNicknameProvider allNicknamesForContact:]
+ -[CNFakeSensitiveIMNicknameProvider cn_anyHandleForContact:]
+ -[CNFakeSensitiveIMNicknameProvider contactsByRecordID]
+ -[CNFakeSensitiveIMNicknameProvider forwardingTargetForSelector:]
+ -[CNFakeSensitiveIMNicknameProvider identifiers]
+ -[CNFakeSensitiveIMNicknameProvider realProvider]
+ -[CNFakeSensitiveIMNicknameProvider setContactsByRecordID:]
+ -[CNFakeSensitiveIMNicknameProvider setIdentifiers:]
+ -[CNFakeSensitiveIMNicknameProvider setRealProvider:]
+ -[CNFakeSensitiveNicknameProvider .cxx_destruct]
+ -[CNFakeSensitiveNicknameProvider cn_makeSensitivityAnalysis]
+ -[CNFakeSensitiveNicknameProvider cn_stablePosterArchiveDataForContact:]
+ -[CNFakeSensitiveNicknameProvider fakeIMProvider]
+ -[CNFakeSensitiveNicknameProvider initWithIdentifiers:]
+ -[CNFakeSensitiveNicknameProvider realProvider]
+ -[CNFakeSensitiveNicknameProvider setFakeIMProvider:]
+ -[CNFakeSensitiveNicknameProvider setRealProvider:]
+ -[CNFakeSensitiveNicknameProvider sharedWallpaperForNickname:]
+ -[CNFakeSensitiveNicknameProvider sharedWatchWallpaperImageDataForNickname:]
+ -[CNSharedProfileStateOracle cn_isFakeSensitiveDebugContact]
+ -[CNiOSABFullTextSearchContactPredicate _predicatesWithAddressBook:fetchRequest:environment:]
+ -[CNiOSABFullTextSearchContactPredicate cn_handlesLimitedAccessAtSQLLevel]
+ -[CNiOSABPredicateRunner searchPeopleWithPredicate:sortOrder:ranked:authorizationContext:inAddressBook:withDelegate:]
+ -[CNiOSContactFetcher _filterPeopleForLimitedAccess:]
+ -[CNiOSContactFetcher initWithFetchRequest:addressBook:environment:managedConfiguration:authorizationContext:]
+ -[CNiOSPersonFetchRequest authorizationContext]
+ -[CNiOSPersonFetchRequest initWithPredicate:keysToFetch:shouldSort:sortOrder:unifiedFetch:batchSize:managedConfiguration:options:authorizationContext:]
+ -[_CNABPredicateObservable initWithPredicate:sortOrdering:options:addressBook:authorizationContext:environment:]
+ GCC_except_table46
+ _OBJC_CLASS_$_ABPredicateSearchOptions
+ _OBJC_CLASS_$_CNFakeSensitiveIMNicknameProvider
+ _OBJC_CLASS_$_CNFakeSensitiveNicknameProvider
+ _OBJC_IVAR_$_CNFakeSensitiveIMNicknameProvider._contactsByRecordID
+ _OBJC_IVAR_$_CNFakeSensitiveIMNicknameProvider._identifiers
+ _OBJC_IVAR_$_CNFakeSensitiveIMNicknameProvider._realProvider
+ _OBJC_IVAR_$_CNFakeSensitiveNicknameProvider._fakeIMProvider
+ _OBJC_IVAR_$_CNFakeSensitiveNicknameProvider._realProvider
+ _OBJC_IVAR_$_CNiOSContactFetcher._authorizationContext
+ _OBJC_IVAR_$_CNiOSPersonFetchRequest._authorizationContext
+ _OBJC_IVAR_$__CNABPredicateObservable._authorizationContext
+ _OBJC_METACLASS_$_CNFakeSensitiveIMNicknameProvider
+ _OBJC_METACLASS_$_CNFakeSensitiveNicknameProvider
+ __OBJC_$_CLASS_METHODS_CNFakeSensitiveNicknameProvider
+ __OBJC_$_INSTANCE_METHODS_CNFakeSensitiveIMNicknameProvider
+ __OBJC_$_INSTANCE_METHODS_CNFakeSensitiveNicknameProvider
+ __OBJC_$_INSTANCE_VARIABLES_CNFakeSensitiveIMNicknameProvider
+ __OBJC_$_INSTANCE_VARIABLES_CNFakeSensitiveNicknameProvider
+ __OBJC_$_PROP_LIST_CNFakeSensitiveIMNicknameProvider
+ __OBJC_$_PROP_LIST_CNFakeSensitiveNicknameProvider
+ __OBJC_CLASS_RO_$_CNFakeSensitiveIMNicknameProvider
+ __OBJC_CLASS_RO_$_CNFakeSensitiveNicknameProvider
+ __OBJC_METACLASS_RO_$_CNFakeSensitiveIMNicknameProvider
+ __OBJC_METACLASS_RO_$_CNFakeSensitiveNicknameProvider
+ ___119+[_CNABPredicateObservable observableWithPredicates:sortOrdering:options:addressBook:authorizationContext:environment:]_block_invoke
+ ___133+[CNiOSFetchExecution contactsMatchingPredicates:sortOrdering:matchInfos:options:addressBook:authorizationContext:environment:error:]_block_invoke
+ ___133+[CNiOSFetchExecution contactsMatchingPredicates:sortOrdering:matchInfos:options:addressBook:authorizationContext:environment:error:]_block_invoke_2
+ ___146+[CNiOSFetchExecution contactsMatchingPredicates:sortOrdering:options:addressBook:authorizationContext:progressiveResults:completion:environment:]_block_invoke
+ ___146+[CNiOSFetchExecution contactsMatchingPredicates:sortOrdering:options:addressBook:authorizationContext:progressiveResults:completion:environment:]_block_invoke_2
+ ___146+[CNiOSFetchExecution contactsMatchingPredicates:sortOrdering:options:addressBook:authorizationContext:progressiveResults:completion:environment:]_block_invoke_3
+ ___29+[CNiOSContactFetcher os_log]_block_invoke
+ ___53-[CNiOSContactFetcher _filterPeopleForLimitedAccess:]_block_invoke
+ ___93-[CNiOSABFullTextSearchContactPredicate _predicatesWithAddressBook:fetchRequest:environment:]_block_invoke
+ ___93-[CNiOSABFullTextSearchContactPredicate _predicatesWithAddressBook:fetchRequest:environment:]_block_invoke_2
+ ___93-[CNiOSABFullTextSearchContactPredicate _predicatesWithAddressBook:fetchRequest:environment:]_block_invoke_3
+ ___CNiOSContactFetcherShouldLogUnoptimizedLimitedAccessPredicate_block_invoke
+ ___CNiOSContactFetcherShouldLogUnoptimizedLimitedAccessPredicate_block_invoke_2
+ ___CNiOSContactFetcherShouldLogUnoptimizedLimitedAccessPredicate_block_invoke_3
+ ___block_descriptor_48_e8_32s_e15_"NSNumber"8?0lu40l8s32l8
+ ___block_descriptor_69_e8_32s40s48s_e21_v16?0"ABPredicate"8ls32l8s40l8s48l8
+ ___block_descriptor_76_e8_32s40s_e47_"_CNABPredicateObservable"16?0"NSPredicate"8ls32l8s40l8
+ __shouldFetchAvatarDataGivenRequestedKeys:.cn_once_object_8
+ __shouldFetchAvatarDataGivenRequestedKeys:.cn_once_token_8
+ __shouldFetchPosterDataGivenRequestedKeys:.cn_once_object_7
+ __shouldFetchPosterDataGivenRequestedKeys:.cn_once_token_7
+ _descriptionForActionType:.cn_once_object_78
+ _descriptionForActionType:.cn_once_token_78
+ _descriptionForUpdateState:.cn_once_object_79
+ _descriptionForUpdateState:.cn_once_token_79
+ _linkedPeopleComparator.cn_once_object_3
+ _linkedPeopleComparator.cn_once_token_3
- +[CNiOSContactFetcher contactsForFetchRequest:matchInfos:inAddressBook:environment:managedConfiguration:error:]
- +[CNiOSFetchExecution contactsMatchingPredicates:sortOrdering:matchInfos:options:addressBook:environment:error:]
- +[CNiOSFetchExecution contactsMatchingPredicates:sortOrdering:options:addressBook:progressiveResults:completion:environment:]
- +[CNiOSPersonFetchRequest(CNConversion) fetchRequestFromCNFetchRequest:managedConfiguration:error:]
- +[_CNABPredicateObservable observableWithPredicates:sortOrdering:options:addressBook:environment:]
- -[CNiOSABFullTextSearchContactPredicate _predicatesWithAddressBook:environment:]
- -[CNiOSABPredicateRunner searchPeopleWithPredicate:sortOrder:ranked:inAddressBook:withDelegate:]
- -[CNiOSContactFetcher initWithFetchRequest:addressBook:environment:managedConfiguration:]
- -[CNiOSPersonFetchRequest initWithPredicate:keysToFetch:shouldSort:sortOrder:unifiedFetch:batchSize:managedConfiguration:options:]
- -[_CNABPredicateObservable initWithPredicate:sortOrdering:options:addressBook:environment:]
- ___112+[CNiOSFetchExecution contactsMatchingPredicates:sortOrdering:matchInfos:options:addressBook:environment:error:]_block_invoke
- ___112+[CNiOSFetchExecution contactsMatchingPredicates:sortOrdering:matchInfos:options:addressBook:environment:error:]_block_invoke_2
- ___125+[CNiOSFetchExecution contactsMatchingPredicates:sortOrdering:options:addressBook:progressiveResults:completion:environment:]_block_invoke
- ___125+[CNiOSFetchExecution contactsMatchingPredicates:sortOrdering:options:addressBook:progressiveResults:completion:environment:]_block_invoke_2
- ___125+[CNiOSFetchExecution contactsMatchingPredicates:sortOrdering:options:addressBook:progressiveResults:completion:environment:]_block_invoke_3
- ___80-[CNiOSABFullTextSearchContactPredicate _predicatesWithAddressBook:environment:]_block_invoke
- ___80-[CNiOSABFullTextSearchContactPredicate _predicatesWithAddressBook:environment:]_block_invoke_2
- ___80-[CNiOSABFullTextSearchContactPredicate _predicatesWithAddressBook:environment:]_block_invoke_3
- ___98+[_CNABPredicateObservable observableWithPredicates:sortOrdering:options:addressBook:environment:]_block_invoke
- ___block_descriptor_61_e8_32s40s_e21_v16?0"ABPredicate"8ls32l8s40l8
- ___block_descriptor_68_e8_32s_e47_"_CNABPredicateObservable"16?0"NSPredicate"8ls32l8
- __shouldFetchAvatarDataGivenRequestedKeys:.cn_once_object_4
- __shouldFetchAvatarDataGivenRequestedKeys:.cn_once_token_4
- __shouldFetchPosterDataGivenRequestedKeys:.cn_once_object_3
- __shouldFetchPosterDataGivenRequestedKeys:.cn_once_token_3
- _descriptionForActionType:.cn_once_object_76
- _descriptionForActionType:.cn_once_token_76
- _descriptionForUpdateState:.cn_once_object_77
- _descriptionForUpdateState:.cn_once_token_77
- _linkedPeopleComparator.cn_once_object_0
- _linkedPeopleComparator.cn_once_token_0
CStrings:
+ "CNFakeSensitiveNicknameProviderContentType"
+ "CNFakeSensitiveNicknameProviderEnabled"
+ "CNFakeSensitiveNicknameProviderIdentifiers"
+ "CNFakeSensitivePosterArchive."
+ "CNiOSContactFetcher"
+ "FakeSensitive debug: ignoring shared-profile action %@ (with nicknames) for %{public}@ to preserve the faked poster"
+ "FakeSensitive debug: ignoring shared-profile action %@ for %{public}@ to preserve the faked poster"
+ "This process is using a %@ predicate, which has not been optimized for Limited Access. Please file a radar against Contacts | New Bugs if you see performance issues."
```
