## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester`

```diff

-1917.0.1.0.0
-  __TEXT.__text: 0xdf9bc
-  __TEXT.__auth_stubs: 0xf20
+1919.0.0.0.0
+  __TEXT.__text: 0xdfd58
+  __TEXT.__auth_stubs: 0xf50
   __TEXT.__objc_methlist: 0x91fc
   __TEXT.__const: 0x708
-  __TEXT.__gcc_except_tab: 0x2d4c
-  __TEXT.__cstring: 0x9f4b
-  __TEXT.__oslogstring: 0xab77
+  __TEXT.__gcc_except_tab: 0x2d34
+  __TEXT.__cstring: 0xa0c3
+  __TEXT.__oslogstring: 0xab83
   __TEXT.__dlopen_cstrs: 0x17a6
   __TEXT.__ustring: 0x33e
   __TEXT.__unwind_info: 0x2888
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x10a4
-  __TEXT.__objc_methname: 0x1f676
-  __TEXT.__objc_methtype: 0x2655
+  __TEXT.__objc_classname: 0x10a7
+  __TEXT.__objc_methname: 0x1f6b9
+  __TEXT.__objc_methtype: 0x268d
   __TEXT.__objc_stubs: 0x11c60
   __DATA_CONST.__got: 0x8a0
-  __DATA_CONST.__const: 0x30d8
+  __DATA_CONST.__const: 0x3128
   __DATA_CONST.__objc_classlist: 0x4a8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x5f98
   __DATA_CONST.__objc_superrefs: 0x378
-  __DATA_CONST.__objc_arraydata: 0xb60
-  __AUTH_CONST.__auth_got: 0x7a0
+  __DATA_CONST.__objc_arraydata: 0xb48
+  __AUTH_CONST.__auth_got: 0x7b8
   __AUTH_CONST.__const: 0x1740
-  __AUTH_CONST.__cfstring: 0x9dc0
-  __AUTH_CONST.__objc_const: 0x124b8
+  __AUTH_CONST.__cfstring: 0x9d80
+  __AUTH_CONST.__objc_const: 0x12518
   __AUTH_CONST.__objc_intobj: 0xf60
-  __AUTH_CONST.__objc_arrayobj: 0x780
+  __AUTH_CONST.__objc_arrayobj: 0x768
   __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH.__objc_data: 0x730
-  __DATA.__objc_ivar: 0xcc0
+  __DATA.__objc_ivar: 0xccc
   __DATA.__data: 0x3c8
   __DATA.__bss: 0x528
   __DATA_DIRTY.__objc_data: 0x2760

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ECB9C7AC-FF55-315A-805A-B1256E798BDA
-  Functions: 4313
-  Symbols:   15087
-  CStrings:  8440
+  UUID: 82F2F92C-4848-3D94-AEC0-03FF32BED13E
+  Functions: 4316
+  Symbols:   15101
+  CStrings:  8442
 
Symbols:
+ -[_PSContactHandleFeatureProvider _interactionFeaturesForHandle:].cold.2
+ _OBJC_IVAR_$__PSSuggesterCache._hasQueuedRefetch
+ _OBJC_IVAR_$__PSSuggesterCache._queuedRefetchGroup
+ _OBJC_IVAR_$__PSSuggesterCache._refetchLock
+ ___106-[_PSContactSuggesterForPeopleWidget contactSuggestionsWithMaxSuggestions:excludeContactsWithIdentifiers:]_block_invoke.51
+ ___48+[_PSContactResolver handlesForContactFavorites]_block_invoke
+ ___48+[_PSContactResolver handlesForContactFavorites]_block_invoke.cold.1
+ ___48+[_PSContactResolver handlesForContactFavorites]_block_invoke.cold.2
+ ___55-[_PSContactSuggesterForPeopleWidget favoritedContacts]_block_invoke.47
+ ___55-[_PSContactSuggesterForPeopleWidget favoritedContacts]_block_invoke.cold.1
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.542
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.550
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.565
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.571
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.578
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke_2.575
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSArray"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSArray"8ls32l8s40l8
+ ___block_literal_global.53
+ ___block_literal_global.545
+ ___block_literal_global.552
+ ___block_literal_global.568
+ ___block_literal_global.580
+ _dispatch_group_wait
+ _objc_msgSend$accessFavoriteContactEntriesWithBlock:
+ _os_unfair_lock_assert_not_owner
+ _os_unfair_lock_trylock
- +[_PSContactResolver handlesForContactFavorites].cold.1
- +[_PSContactResolver handlesForContactFavorites].cold.2
- -[_PSContactSuggesterForPeopleWidget favoritedContacts].cold.1
- ___106-[_PSContactSuggesterForPeopleWidget contactSuggestionsWithMaxSuggestions:excludeContactsWithIdentifiers:]_block_invoke.49
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.539
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.544
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.562
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.568
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.575
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke_2.572
- ___block_literal_global.51
- ___block_literal_global.542
- ___block_literal_global.546
- ___block_literal_global.565
- ___block_literal_global.571
- _objc_msgSend$favoriteContactEntries
CStrings:
+ "<_PSSuggesterCache %p> (trylock failed in -[_PSSuggesterCache description])"
+ "<_PSSuggesterCache %p> cachedSuggestions: %@, cachedSessionID: %@, cachedContext: %@"
+ "@\"NSObject<OS_dispatch_group>\""
+ "SELECT    intentClass,    bundleId,    groupIdentifier,    COALESCE(%d - MAX(CASE WHEN interactionDirection = 2 THEN absoluteTimestamp END), -1) AS %@,    COALESCE(%d - MAX(CASE WHEN interactionDirection = 3 THEN absoluteTimestamp END), -1) AS %@,    COUNT(CASE WHEN interactionDirection = 2 THEN 1 END) AS %@,    COUNT(CASE WHEN interactionDirection = 3 THEN 1 END) AS %@ FROM    \"App.Intent\" WHERE\n    (intentClass = 'INSendMessageIntent'    AND groupIdentifier = 'iMessage;-;%@') OR (intentClass = 'INSendMessageIntent'    AND groupIdentifier = 'SMS;-;%@') OR (intentClass = 'INSendMessageIntent'    AND groupIdentifier = 'RCS;-;%@') OR (intentClass = 'INSendMessageIntent'    AND groupIdentifier = 'any;-;%@') OR (intentClass = 'INStartCallIntent'    AND groupIdentifier = '%@') GROUP BY    groupIdentifier;"
+ "_hasQueuedRefetch"
+ "_queuedRefetchGroup"
+ "_refetchLock"
+ "accessFavoriteContactEntriesWithBlock:"
+ "favoritedContacts count: %tu"
+ "query = %@"
+ "{atomic_flag=\"_Value\"AB}"
- "RCS"
- "SELECT\n    intentClass,\n    bundleId,\n    groupIdentifier,\n    COALESCE(%d - MAX(CASE WHEN interactionDirection = 2 THEN absoluteTimestamp END), -1) AS %@,    COALESCE(%d - MAX(CASE WHEN interactionDirection = 3 THEN absoluteTimestamp END), -1) AS %@,    COUNT(CASE WHEN interactionDirection = 2 THEN 1 END) AS %@,\n    COUNT(CASE WHEN interactionDirection = 3 THEN 1 END) AS %@\nFROM\n    \"App.Intent\"\nWHERE\n    intentClass = 'INSendMessageIntent'\n    AND groupIdentifier = 'protocol;-;%@'\nGROUP BY\n    groupIdentifier;"
- "SMS"
- "cachedSuggestions: %@, cachedSessionID: %@, cachedContext: %@"
- "favoriteContactEntries"
- "favoritedContacts count: %@"
- "protocol"

```
