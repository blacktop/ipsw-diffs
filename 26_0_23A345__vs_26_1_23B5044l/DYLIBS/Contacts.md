## Contacts

> `/System/Library/Frameworks/Contacts.framework/Contacts`

```diff

-3804.100.1.2.4
-  __TEXT.__text: 0x1b6d80
+3804.200.33.0.0
+  __TEXT.__text: 0x1b7ecc
   __TEXT.__auth_stubs: 0x3280
-  __TEXT.__objc_methlist: 0x1ad68
-  __TEXT.__const: 0x20c8
-  __TEXT.__gcc_except_tab: 0x3b2c
-  __TEXT.__cstring: 0xc982
+  __TEXT.__objc_methlist: 0x1ae58
+  __TEXT.__const: 0x20b8
+  __TEXT.__gcc_except_tab: 0x3b3c
+  __TEXT.__cstring: 0xca22
   __TEXT.__dlopen_cstrs: 0x8de
-  __TEXT.__oslogstring: 0xbaea
+  __TEXT.__oslogstring: 0xbd6a
   __TEXT.__ustring: 0x12
   __TEXT.__constg_swiftt: 0xdc4
   __TEXT.__swift5_typeref: 0xea1

   __TEXT.__swift5_capture: 0x5d4
   __TEXT.__swift_as_entry: 0x68
   __TEXT.__swift_as_ret: 0x5c
-  __TEXT.__unwind_info: 0x7e98
+  __TEXT.__unwind_info: 0x7ee8
   __TEXT.__eh_frame: 0x25c0
-  __TEXT.__objc_classname: 0x43df
-  __TEXT.__objc_methname: 0x2b32e
+  __TEXT.__objc_classname: 0x442e
+  __TEXT.__objc_methname: 0x2b3d9
   __TEXT.__objc_methtype: 0x53c2
-  __TEXT.__objc_stubs: 0x1e5a0
+  __TEXT.__objc_stubs: 0x1e600
   __DATA_CONST.__got: 0x1b50
-  __DATA_CONST.__const: 0x61c0
-  __DATA_CONST.__objc_classlist: 0x10e0
+  __DATA_CONST.__const: 0x61b8
+  __DATA_CONST.__objc_classlist: 0x10f0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9638
+  __DATA_CONST.__objc_selrefs: 0x9650
   __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0x9b0
+  __DATA_CONST.__objc_superrefs: 0x9b8
   __DATA_CONST.__objc_arraydata: 0x268
   __AUTH_CONST.__auth_got: 0x1950
-  __AUTH_CONST.__const: 0x6a38
-  __AUTH_CONST.__cfstring: 0xd9c0
-  __AUTH_CONST.__objc_const: 0x2bb38
+  __AUTH_CONST.__const: 0x6a78
+  __AUTH_CONST.__cfstring: 0xda60
+  __AUTH_CONST.__objc_const: 0x2bcf8
   __AUTH_CONST.__objc_intobj: 0x5d0
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x5638
+  __AUTH.__objc_data: 0x56d8
   __AUTH.__data: 0x660
-  __DATA.__objc_ivar: 0x1264
+  __DATA.__objc_ivar: 0x1268
   __DATA.__data: 0x2d20
   __DATA.__bss: 0x2920
   __DATA.__common: 0x80
   __DATA_DIRTY.__objc_data: 0x5dc0
   __DATA_DIRTY.__data: 0x38
-  __DATA_DIRTY.__bss: 0xb88
+  __DATA_DIRTY.__bss: 0xb98
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ClassKit.framework/ClassKit
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3102B528-C4D3-30C6-A202-9928344D087C
-  Functions: 12441
-  Symbols:   36437
-  CStrings:  12765
+  UUID: 2F173F6D-C9DE-30EE-8DFC-39801B46FBD9
+  Functions: 12465
+  Symbols:   36508
+  CStrings:  12800
 
Symbols:
+ +[CNAggregateContactStore log]
+ +[CNAggregateContactStore log].cold.1
+ +[CNContact(Predicates_Private) predicateForContactsWithExternalIdentifiers:]
+ +[CNExternalIdentifierContactPredicate supportsSecureCoding]
+ -[CNContactPoster initWithIdentifier:posterData:posterMetadata:watchPosterData:lastUsedDate:]
+ -[CNExternalIdentifierContactPredicate .cxx_destruct]
+ -[CNExternalIdentifierContactPredicate description]
+ -[CNExternalIdentifierContactPredicate encodeWithCoder:]
+ -[CNExternalIdentifierContactPredicate externalIdentifiers]
+ -[CNExternalIdentifierContactPredicate hash]
+ -[CNExternalIdentifierContactPredicate initWithCoder:]
+ -[CNExternalIdentifierContactPredicate initWithExternalIdentifiers:]
+ -[CNExternalIdentifierContactPredicate isEqual:]
+ -[CNiOSABExternalIdentifierContactPredicate _inputsAreValid]
+ -[CNiOSABExternalIdentifierContactPredicate cn_ABQSLPredicateForAddressBook:fetchRequest:error:]
+ -[CNiOSABExternalIdentifierContactPredicate cn_copyPeopleInAddressBook:fetchRequest:matchInfos:environment:error:]
+ -[CNiOSABExternalIdentifierContactPredicate cn_supportsEncodedFetching]
+ -[CNiOSABExternalIdentifierContactPredicate cn_supportsNativeBatchFetch]
+ -[CNiOSABExternalIdentifierContactPredicate cn_supportsNativeSorting]
+ GCC_except_table99
+ _OBJC_CLASS_$_CNExternalIdentifierContactPredicate
+ _OBJC_CLASS_$_CNiOSABExternalIdentifierContactPredicate
+ _OBJC_IVAR_$_CNExternalIdentifierContactPredicate._externalIdentifiers
+ _OBJC_METACLASS_$_CNExternalIdentifierContactPredicate
+ _OBJC_METACLASS_$_CNiOSABExternalIdentifierContactPredicate
+ __OBJC_$_CLASS_METHODS_CNAggregateContactStore
+ __OBJC_$_CLASS_METHODS_CNExternalIdentifierContactPredicate
+ __OBJC_$_INSTANCE_METHODS_CNExternalIdentifierContactPredicate
+ __OBJC_$_INSTANCE_METHODS_CNiOSABExternalIdentifierContactPredicate
+ __OBJC_$_INSTANCE_VARIABLES_CNExternalIdentifierContactPredicate
+ __OBJC_$_PROP_LIST_CNExternalIdentifierContactPredicate
+ __OBJC_$_PROP_LIST_CNiOSABExternalIdentifierContactPredicate
+ __OBJC_CLASS_PROTOCOLS_$_CNiOSABExternalIdentifierContactPredicate
+ __OBJC_CLASS_RO_$_CNExternalIdentifierContactPredicate
+ __OBJC_CLASS_RO_$_CNiOSABExternalIdentifierContactPredicate
+ __OBJC_METACLASS_RO_$_CNExternalIdentifierContactPredicate
+ __OBJC_METACLASS_RO_$_CNiOSABExternalIdentifierContactPredicate
+ ___30+[CNAggregateContactStore log]_block_invoke
+ ___44-[CNExternalIdentifierContactPredicate hash]_block_invoke
+ ___48-[CNExternalIdentifierContactPredicate isEqual:]_block_invoke
+ ___48-[CNExternalIdentifierContactPredicate isEqual:]_block_invoke_2
+ ___48-[CNExternalIdentifierContactPredicate isEqual:]_block_invoke_3
+ ___60-[CNiOSABExternalIdentifierContactPredicate _inputsAreValid]_block_invoke
+ ___66-[CNAggregateContactStore enumeratorForContactFetchRequest:error:]_block_invoke.71
+ ___77-[CNAggregateContactStore executeFetchRequest:progressiveResults:completion:]_block_invoke.65
+ ___78-[CNAggregateContactStore unifiedContactsMatchingPredicate:keysToFetch:error:]_block_invoke.32
+ ___88-[CNAggregateContactStore enumerateNonUnifiedContactsWithFetchRequest:error:usingBlock:]_block_invoke.61
+ ___90-[CNAggregateContactStore enumerateContactsAndMatchInfoWithFetchRequest:error:usingBlock:]_block_invoke.46
+ ___90-[CNAggregateContactStore enumerateContactsAndMatchInfoWithFetchRequest:error:usingBlock:]_block_invoke.53
+ ___block_literal_global.63
+ _objc_msgSend$externalIdentifiers
+ _objc_msgSend$initWithExternalIdentifiers:
+ _objc_msgSend$initWithIdentifier:posterData:posterMetadata:watchPosterData:lastUsedDate:
+ _objc_msgSend$predicateForContactsWithExternalIdentifiers:
- -[CNContactPoster initWithIdentifier:posterData:posterMetadata:lastUsedDate:]
- GCC_except_table72
- GCC_except_table97
- ___66-[CNAggregateContactStore enumeratorForContactFetchRequest:error:]_block_invoke.68
- ___77-[CNAggregateContactStore executeFetchRequest:progressiveResults:completion:]_block_invoke.62
- ___78-[CNAggregateContactStore unifiedContactsMatchingPredicate:keysToFetch:error:]_block_invoke.28
- ___88-[CNAggregateContactStore enumerateNonUnifiedContactsWithFetchRequest:error:usingBlock:]_block_invoke.58
- ___90-[CNAggregateContactStore enumerateContactsAndMatchInfoWithFetchRequest:error:usingBlock:]_block_invoke.42
- ___90-[CNAggregateContactStore enumerateContactsAndMatchInfoWithFetchRequest:error:usingBlock:]_block_invoke.50
- ___block_literal_global.41
- ___block_literal_global.65
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_Contacts
- _objc_msgSend$initWithIdentifier:posterData:posterMetadata:lastUsedDate:
CStrings:
+ "-[CNContact predicateForContactsWithExternalIdentifiers:]"
+ "Adding shared photo decorator (includeSharedPhotoContacts=YES)"
+ "CNExternalIdentifierContactPredicate"
+ "CNiOSABExternalIdentifierContactPredicate"
+ "Calling imNicknameProvider.allNicknamesForContact:contact"
+ "Calling nicknameForContact for %@"
+ "Contact %@ not in auto-update state"
+ "Contains wallpaper key: %d"
+ "Current nickname: %@"
+ "FavoritesServerRetryDisabled"
+ "Final keysToFetchVector: %@"
+ "Got %lu nicknames: %@"
+ "IMNicknameProvider returned %lu nicknames"
+ "Original required keys: %@"
+ "Processing %lu contacts for shared photo decoration"
+ "Skipping shared photo decorator (includeSharedPhotoContacts=NO)"
+ "Skipping: enableSharedPhoto=NO"
+ "Skipping: required keys missing"
+ "T@\"NSArray\",R,C,N,V_externalIdentifiers"
+ "Validating keys for %lu descriptors"
+ "_externalIdentifiers"
+ "aggregate-store"
+ "allNicknamesForContact called for %@"
+ "decoratedContacts called with %lu contacts"
+ "externalIdentifiers"
+ "found"
+ "initWithExternalIdentifiers:"
+ "initWithIdentifier:posterData:posterMetadata:watchPosterData:lastUsedDate:"
+ "nicknameForContact called for %@"
+ "predicateForContactsWithExternalIdentifiers:"
- "Fetching all nicknames %@ for %{private}@"
- "initWithIdentifier:posterData:posterMetadata:lastUsedDate:"

```
