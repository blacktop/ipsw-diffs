## CascadeSets

> `/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets`

```diff

-198.0.0.0.0
-  __TEXT.__text: 0x5523c
+200.0.0.0.0
+  __TEXT.__text: 0x557e0
   __TEXT.__auth_stubs: 0xd30
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x4824
+  __TEXT.__objc_methlist: 0x486c
   __TEXT.__const: 0x394
-  __TEXT.__gcc_except_tab: 0x124c
-  __TEXT.__cstring: 0x3ee2
+  __TEXT.__gcc_except_tab: 0x1278
+  __TEXT.__cstring: 0x3f82
   __TEXT.__oslogstring: 0x4ba4
   __TEXT.__dlopen_cstrs: 0x278
   __TEXT.__swift5_typeref: 0x168

   __TEXT.__swift_as_ret: 0x20
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x15f0
+  __TEXT.__unwind_info: 0x1608
   __TEXT.__eh_frame: 0x2f8
-  __TEXT.__objc_classname: 0xb22
-  __TEXT.__objc_methname: 0xa330
-  __TEXT.__objc_methtype: 0x2053
+  __TEXT.__objc_classname: 0xb20
+  __TEXT.__objc_methname: 0xa3c5
+  __TEXT.__objc_methtype: 0x20b5
   __TEXT.__objc_stubs: 0x6dc0
-  __DATA_CONST.__got: 0x4c8
-  __DATA_CONST.__const: 0x1340
+  __DATA_CONST.__got: 0x4c0
+  __DATA_CONST.__const: 0x13c8
   __DATA_CONST.__objc_classlist: 0x340
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x128

   __DATA_CONST.__objc_superrefs: 0x2b0
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x6b0
-  __AUTH_CONST.__const: 0x4b0
+  __AUTH_CONST.__const: 0x560
   __AUTH_CONST.__cfstring: 0x3480
-  __AUTH_CONST.__objc_const: 0xabe8
+  __AUTH_CONST.__objc_const: 0xac08
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH.__objc_data: 0x3e8
+  __AUTH.__objc_data: 0x7d0
   __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0x4c0
-  __DATA.__data: 0xd6c
+  __DATA.__objc_ivar: 0x4bc
+  __DATA.__data: 0xd70
   __DATA.__bss: 0x48
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x1e00
+  __DATA_DIRTY.__objc_data: 0x1a18
   __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation
   - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
-  - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 7F1C4CF4-DDE5-3FD4-8F42-3F7A0BC7C79E
-  Functions: 2016
-  Symbols:   6638
-  CStrings:  3389
+  UUID: 2314C6B6-4FE0-3318-AD64-57B71AC6C82D
+  Functions: 2030
+  Symbols:   6657
+  CStrings:  3392
 
Symbols:
+ +[CCDataResource enumerateDataResources:setIdentifier:descriptors:container:includingTombstoned:startAfterSet:sorted:usingBlock:]
+ -[CCDataResourceReadAccess _requestAccessToResource:error:]
+ -[CCDataResourceReadAccess _requestAccessToSetsDirectoryWithOptions:error:]
+ -[CCDataResourceReadAccess _requestAccessToSetsDirectoryWithOptions:error:].cold.1
+ -[CCDataResourceReadAccess _sortedSetsFromProcessEntitlements:filteredBySortedIdentifiers:]
+ -[CCDataResourceReadAccess enumerateReadableSets:resourceOptions:setIdentifiers:descriptors:startAfterSet:sorted:usingBlock:]
+ -[CCDataResourceReadAccess enumerateReadableSets:resourceOptions:setIdentifiers:descriptors:startAfterSet:sorted:usingBlock:].cold.1
+ -[CCDataResourceReadAccess initWithAssertionOverride:useCase:]
+ -[CCDataResourceWriteAccess initWithAssertionOverride:]
+ -[CCDataResourceWriteAccess requestAccessToResource:withMode:useCase:error:]
+ -[CCDatabaseSetEnumerator allSetsWithOptions:itemType:descriptors:error:]
+ -[CCDatabaseSetEnumerator enumerateAllSets:withOptions:itemType:descriptors:usingBlock:]
+ -[CCDatabaseSetEnumerator enumerateAllSets:withOptions:setIdentifiers:descriptors:startAfterSet:usingBlock:]
+ -[CCDatabaseSetEnumerator enumerateAllSets:withOptions:setIdentifiers:descriptors:startAfterSet:usingBlock:].cold.1
+ -[CCSerializedSetEnumerator allSetsWithOptions:itemType:descriptors:error:]
+ -[CCSerializedSetEnumerator enumerateAllSets:withOptions:itemType:descriptors:usingBlock:]
+ GCC_except_table44
+ GCC_except_table46
+ _OBJC_IVAR_$_CCDataResourceReadAccess._assertionOverride
+ _OBJC_IVAR_$_CCDataResourceWriteAccess._assertionOverride
+ ___108-[CCDatabaseSetEnumerator enumerateAllSets:withOptions:setIdentifiers:descriptors:startAfterSet:usingBlock:]_block_invoke
+ ___125-[CCDataResourceReadAccess enumerateReadableSets:resourceOptions:setIdentifiers:descriptors:startAfterSet:sorted:usingBlock:]_block_invoke
+ ___125-[CCDataResourceReadAccess enumerateReadableSets:resourceOptions:setIdentifiers:descriptors:startAfterSet:sorted:usingBlock:]_block_invoke.21
+ ___129+[CCDataResource enumerateDataResources:setIdentifier:descriptors:container:includingTombstoned:startAfterSet:sorted:usingBlock:]_block_invoke
+ ___129+[CCDataResource enumerateDataResources:setIdentifier:descriptors:container:includingTombstoned:startAfterSet:sorted:usingBlock:]_block_invoke_2
+ ___129+[CCDataResource enumerateDataResources:setIdentifier:descriptors:container:includingTombstoned:startAfterSet:sorted:usingBlock:]_block_invoke_3
+ ___129+[CCDataResource enumerateDataResources:setIdentifier:descriptors:container:includingTombstoned:startAfterSet:sorted:usingBlock:]_block_invoke_4
+ ___73-[CCDatabaseSetEnumerator allSetsWithOptions:itemType:descriptors:error:]_block_invoke
+ ___75-[CCSerializedSetEnumerator allSetsWithOptions:itemType:descriptors:error:]_block_invoke
+ ___88-[CCDatabaseSetEnumerator enumerateAllSets:withOptions:itemType:descriptors:usingBlock:]_block_invoke
+ ___90-[CCSerializedSetEnumerator enumerateAllSets:withOptions:itemType:descriptors:usingBlock:]_block_invoke
+ ___block_descriptor_32_e43_q24?0"CCDataResource"8"CCDataResource"16l
+ ___block_descriptor_32_e45_q24?0"CCSerializedSet"8"CCSerializedSet"16l
+ ___block_descriptor_40_e8_32bs_e19_v24?0"CCSet"8^B16ls32l8
+ ___block_descriptor_40_e8_32s_e24_B16?0"CCDataResource"8ls32l8
+ ___block_descriptor_49_e8_32bs40bs_e24_B16?0"CCDataResource"8ls32l8s40l8
+ ___swift_memcpy0_1
+ ___swift_noop_void_return
+ _objc_msgSend$_requestAccessToResource:error:
+ _objc_msgSend$_requestAccessToSetsDirectoryWithOptions:error:
+ _objc_msgSend$_sortedSetsFromProcessEntitlements:filteredBySortedIdentifiers:
+ _objc_msgSend$allSetsWithOptions:itemType:descriptors:error:
+ _objc_msgSend$dataResourcePathComponentFromResource:
+ _objc_msgSend$enumerateAllSets:withOptions:itemType:descriptors:usingBlock:
+ _objc_msgSend$enumerateAllSets:withOptions:setIdentifiers:descriptors:startAfterSet:usingBlock:
+ _objc_msgSend$enumerateDataResources:setIdentifier:descriptors:container:includingTombstoned:startAfterSet:sorted:usingBlock:
+ _objc_msgSend$enumerateReadableSets:resourceOptions:setIdentifiers:descriptors:startAfterSet:sorted:usingBlock:
+ _objc_msgSend$initWithAssertionOverride:
+ _objc_msgSend$initWithAssertionOverride:useCase:
+ _objc_msgSend$sortUsingComparator:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$sortedArrayUsingDescriptors:
- +[CCDataResource enumerateDataResources:setIdentifier:descriptors:container:includingTombstoned:usingBlock:]
- +[CCSetDescriptor accountIdentifierFromAccount:error:]
- -[CCDataResourceReadAccess _requestAccessToResource:outAccessAssertion:error:]
- -[CCDataResourceReadAccess _requestAccessToSetsDirectoryWithOptions:outAccessAssertion:error:]
- -[CCDataResourceReadAccess _requestAccessToSetsDirectoryWithOptions:outAccessAssertion:error:].cold.1
- -[CCDataResourceReadAccess enumerateReadableSets:resourceOptions:setIdentifiers:usingBlock:]
- -[CCDataResourceReadAccess enumerateReadableSets:resourceOptions:setIdentifiers:usingBlock:].cold.1
- -[CCDataResourceReadAccess initWithContainerOverride:useCase:]
- -[CCDataResourceWriteAccess initWithContainerOverride:]
- -[CCDataResourceWriteAccess requestAccess:forResource:withMode:useCase:error:]
- -[CCDatabaseSetEnumerator enumerateAllSets:withOptions:setIdentifiers:usingBlock:]
- -[CCDatabaseSetEnumerator enumerateAllSets:withOptions:setIdentifiers:usingBlock:].cold.1
- -[CCSet account]
- GCC_except_table24
- GCC_except_table38
- GCC_except_table45
- _CCAddAcountInfoToDescriptors
- _CCSetDescriptorKeyAccountIdentifier
- _OBJC_CLASS_$_BMAccount
- _OBJC_IVAR_$_CCDataResourceReadAccess._containerOverride
- _OBJC_IVAR_$_CCDataResourceWriteAccess._containerOverride
- _OBJC_IVAR_$_CCSet._account
- ___108+[CCDataResource enumerateDataResources:setIdentifier:descriptors:container:includingTombstoned:usingBlock:]_block_invoke
- ___61-[CCDatabaseSetEnumerator allSetsWithOptions:itemType:error:]_block_invoke
- ___63-[CCSerializedSetEnumerator allSetsWithOptions:itemType:error:]_block_invoke
- ___82-[CCDatabaseSetEnumerator enumerateAllSets:withOptions:setIdentifiers:usingBlock:]_block_invoke
- ___92-[CCDataResourceReadAccess enumerateReadableSets:resourceOptions:setIdentifiers:usingBlock:]_block_invoke
- ___92-[CCDataResourceReadAccess enumerateReadableSets:resourceOptions:setIdentifiers:usingBlock:]_block_invoke.22
- ___92-[CCDataResourceReadAccess enumerateReadableSets:resourceOptions:setIdentifiers:usingBlock:]_block_invoke.25
- ___block_descriptor_40_e8_32s_e22_B24?0"NSString"8^B16ls32l8
- _objc_msgSend$_requestAccessToResource:outAccessAssertion:error:
- _objc_msgSend$_requestAccessToSetsDirectoryWithOptions:outAccessAssertion:error:
- _objc_msgSend$accountIdentifier
- _objc_msgSend$accountIdentifierFromAccount:error:
- _objc_msgSend$allSetsWithOptions:itemType:error:
- _objc_msgSend$arrayByAddingObject:
- _objc_msgSend$enumerateAllSets:withOptions:setIdentifiers:usingBlock:
- _objc_msgSend$enumerateDataResources:setIdentifier:descriptors:container:includingTombstoned:usingBlock:
- _objc_msgSend$enumerateReadableSets:resourceOptions:setIdentifiers:usingBlock:
- _objc_msgSend$initWithAccountIdentifier:
- _objc_msgSend$initWithContainerOverride:
- _objc_msgSend$initWithContainerOverride:useCase:
- _objc_msgSend$objectsPassingTest:
- _objc_msgSend$setWithArray:
CStrings:
+ "@\"NSArray\"40@0:8S16S20@\"NSArray\"24^@32"
+ "@40@0:8S16S20@24^@32"
+ "@48@0:8@16Q24@32^@40"
+ "B16@?0@\"CCDataResource\"8"
+ "B48@0:8^@16S24S28@\"NSArray\"32@?<v@?@\"CCSet\">40"
+ "B48@0:8^@16S24S28@32@?40"
+ "B60@0:8^@16S24@28@36@44@?52"
+ "B64@0:8^@16C24@28@36@44B52@?56"
+ "B72@0:8^@16@24@32@40B48@52B60@?64"
+ "FullSort"
+ "Skipping access request with assertion override: %@"
+ "Skipping read only access request with assertion override: %@"
+ "_assertionOverride"
+ "_requestAccessToResource:error:"
+ "_requestAccessToSetsDirectoryWithOptions:error:"
+ "_sortedSetsFromProcessEntitlements:filteredBySortedIdentifiers:"
+ "allSetsWithOptions:itemType:descriptors:error:"
+ "dataResourcePathComponentFromResource:"
+ "enumerateAllSets:withOptions:itemType:descriptors:usingBlock:"
+ "enumerateAllSets:withOptions:setIdentifiers:descriptors:startAfterSet:usingBlock:"
+ "enumerateDataResources:setIdentifier:descriptors:container:includingTombstoned:startAfterSet:sorted:usingBlock:"
+ "enumerateReadableSets:resourceOptions:setIdentifiers:descriptors:startAfterSet:sorted:usingBlock:"
+ "initWithAssertionOverride:"
+ "initWithAssertionOverride:useCase:"
+ "q24@?0@\"CCDataResource\"8@\"CCDataResource\"16"
+ "q24@?0@\"CCSerializedSet\"8@\"CCSerializedSet\"16"
+ "requestAccessToResource:withMode:useCase:error:"
+ "sortUsingComparator:"
+ "sortedArrayUsingComparator:"
+ "sortedArrayUsingDescriptors:"
- "@\"BMAccount\""
- "@36@0:8C16^@20^@28"
- "@40@0:8@16^@24^@32"
- "@56@0:8^@16@24Q32@40^@48"
- "B24@?0@\"NSString\"8^B16"
- "B44@0:8^@16C24@28@?36"
- "B44@0:8^@16S24@28@?36"
- "B60@0:8^@16@24@32@40B48@?52"
- "Skipping access request with container override: %@"
- "Skipping read only access request with container override: %@"
- "T@\"BMAccount\",R,N,V_account"
- "_account"
- "_containerOverride"
- "_requestAccessToResource:outAccessAssertion:error:"
- "_requestAccessToSetsDirectoryWithOptions:outAccessAssertion:error:"
- "account"
- "accountIdentifier"
- "accountIdentifierFromAccount:error:"
- "arrayByAddingObject:"
- "enumerateAllSets:withOptions:setIdentifiers:usingBlock:"
- "enumerateDataResources:setIdentifier:descriptors:container:includingTombstoned:usingBlock:"
- "enumerateReadableSets:resourceOptions:setIdentifiers:usingBlock:"
- "initWithAccountIdentifier:"
- "initWithContainerOverride:"
- "initWithContainerOverride:useCase:"
- "objectsPassingTest:"
- "requestAccess:forResource:withMode:useCase:error:"
- "setWithArray:"

```
