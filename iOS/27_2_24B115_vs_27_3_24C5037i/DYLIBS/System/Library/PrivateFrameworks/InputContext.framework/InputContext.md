## InputContext

> `/System/Library/PrivateFrameworks/InputContext.framework/InputContext`

```diff

-137.0.0.0.0
-  __TEXT.__text: 0x13c3c
-  __TEXT.__objc_methlist: 0x1574
+138.0.0.0.0
+  __TEXT.__text: 0x13a50
+  __TEXT.__objc_methlist: 0x167c
   __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0xa70
-  __TEXT.__gcc_except_tab: 0x99c
+  __TEXT.__cstring: 0xa3e
+  __TEXT.__gcc_except_tab: 0x8f8
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__oslogstring: 0x130f
+  __TEXT.__oslogstring: 0x1264
   __TEXT.__ustring: 0x12
-  __TEXT.__unwind_info: 0x880
+  __TEXT.__unwind_info: 0x860
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5c0
-  __DATA_CONST.__objc_classlist: 0xa8
+  __DATA_CONST.__const: 0x548
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd68
-  __DATA_CONST.__objc_superrefs: 0x88
+  __DATA_CONST.__objc_selrefs: 0xdd8
+  __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x78
-  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__got: 0x2e0
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0xda0
-  __AUTH_CONST.__objc_const: 0x23d0
+  __AUTH_CONST.__cfstring: 0xd60
+  __AUTH_CONST.__objc_const: 0x25a0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x1b8
-  __DATA.__data: 0x42a
-  __DATA_DIRTY.__objc_data: 0x640
-  __DATA_DIRTY.__bss: 0xa0
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x1c8
+  __DATA.__data: 0x48a
+  __DATA_DIRTY.__objc_data: 0x5f0
+  __DATA_DIRTY.__bss: 0x90
+  - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/LanguageModeling.framework/LanguageModeling
   - /System/Library/PrivateFrameworks/Lexicon.framework/Lexicon
+  - /System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester
   - /System/Library/PrivateFrameworks/PersonalizationPortrait.framework/PersonalizationPortrait
   - /System/Library/PrivateFrameworks/ProactiveInputPredictions.framework/ProactiveInputPredictions
   - /System/Library/PrivateFrameworks/ResponseKit.framework/ResponseKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 569
-  Symbols:   1062
-  CStrings:  244
+  Functions: 563
+  Symbols:   1087
+  CStrings:  238
 
Symbols:
+ +[_ICContactScorer scoreForContactIdentifier:rankMap:]
+ -[_ICContactScorer .cxx_destruct]
+ -[_ICContactScorer fetchRankMap]
+ -[_ICContactScorer init]
+ -[_ICContactsLexiconSource .cxx_destruct]
+ -[_ICContactsLexiconSource _beginPass:manager:]
+ -[_ICContactsLexiconSource _contactFromCNContact:]
+ -[_ICContactsLexiconSource _contactStoreDidChange:]
+ -[_ICContactsLexiconSource _deletedContactPlaceholder]
+ -[_ICContactsLexiconSource _endPassWithManager:isInitialLoad:]
+ -[_ICContactsLexiconSource _handleContact:changeType:]
+ -[_ICContactsLexiconSource _processChangeHistory]
+ -[_ICContactsLexiconSource _rankMapForPass]
+ -[_ICContactsLexiconSource dealloc]
+ -[_ICContactsLexiconSource hibernate]
+ -[_ICContactsLexiconSource init]
+ -[_ICContactsLexiconSource startLoadingWithManager:]
+ -[_ICContactsLexiconSource visitAddContactEvent:]
+ -[_ICContactsLexiconSource visitDeleteContactEvent:]
+ -[_ICContactsLexiconSource visitDropEverythingEvent:]
+ -[_ICContactsLexiconSource visitUpdateContactEvent:]
+ -[_ICContactsLexiconSource warmUp]
+ _CNContactFamilyNameKey
+ _CNContactGivenNameKey
+ _CNContactIdentifierKey
+ _CNContactJobTitleKey
+ _CNContactMiddleNameKey
+ _CNContactNicknameKey
+ _CNContactOrganizationNameKey
+ _CNContactPhoneticFamilyNameKey
+ _CNContactPhoneticGivenNameKey
+ _CNContactPhoneticMiddleNameKey
+ _CNContactPostalAddressesKey
+ _CNContactRelationsKey
+ _CNContactStoreDidChangeNotification
+ _OBJC_CLASS_$_CNChangeHistoryFetchRequest
+ _OBJC_CLASS_$_CNContactStore
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$__ICContactScorer
+ _OBJC_CLASS_$__ICContactsLexiconSource
+ _OBJC_CLASS_$__PSPredictionContext
+ _OBJC_CLASS_$__PSSuggester
+ _OBJC_IVAR_$__ICContactScorer._suggester
+ _OBJC_IVAR_$__ICContactsLexiconSource._historyToken
+ _OBJC_IVAR_$__ICContactsLexiconSource._manager
+ _OBJC_IVAR_$__ICContactsLexiconSource._observingStoreChanges
+ _OBJC_IVAR_$__ICContactsLexiconSource._pass
+ _OBJC_IVAR_$__ICContactsLexiconSource._queue
+ _OBJC_IVAR_$__ICContactsLexiconSource._rankMap
+ _OBJC_IVAR_$__ICContactsLexiconSource._scorer
+ _OBJC_IVAR_$__ICContactsLexiconSource._store
+ _OBJC_METACLASS_$__ICContactScorer
+ _OBJC_METACLASS_$__ICContactsLexiconSource
+ __ICContactKeyDescriptors.keys
+ __ICContactKeyDescriptors.onceToken
+ __OBJC_$_CLASS_METHODS__ICContactScorer
+ __OBJC_$_INSTANCE_METHODS__ICContactScorer
+ __OBJC_$_INSTANCE_METHODS__ICContactsLexiconSource
+ __OBJC_$_INSTANCE_VARIABLES__ICContactScorer
+ __OBJC_$_INSTANCE_VARIABLES__ICContactsLexiconSource
+ __OBJC_$_PROP_LIST__ICContactsLexiconSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CNChangeHistoryEventVisitor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CNChangeHistoryEventVisitor
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CNChangeHistoryEventVisitor
+ __OBJC_$_PROTOCOL_REFS_CNChangeHistoryEventVisitor
+ __OBJC_CLASS_PROTOCOLS_$__ICContactsLexiconSource
+ __OBJC_CLASS_RO_$__ICContactScorer
+ __OBJC_CLASS_RO_$__ICContactsLexiconSource
+ __OBJC_LABEL_PROTOCOL_$_CNChangeHistoryEventVisitor
+ __OBJC_METACLASS_RO_$__ICContactScorer
+ __OBJC_METACLASS_RO_$__ICContactsLexiconSource
+ __OBJC_PROTOCOL_$_CNChangeHistoryEventVisitor
+ ___51-[_ICContactsLexiconSource _contactStoreDidChange:]_block_invoke
+ ___52-[_ICContactsLexiconSource startLoadingWithManager:]_block_invoke
+ ____ICContactKeyDescriptors_block_invoke
- +[_ICPortraitUtilities contactChangeTypeForPortraitChangeType:]
- +[_ICPortraitUtilities contactFromPortraitContact:]
- +[_ICPortraitUtilities contactRecordFromPortraitContactRecord:]
- +[_ICPortraitUtilities contactSourceTypeForPortraitSourceType:]
- +[_ICPortraitUtilities excludedAlgorithms]
- -[_ICPortraitLexiconSource .cxx_destruct]
- -[_ICPortraitLexiconSource _makeContactDelegate]
- -[_ICPortraitLexiconSource _makeNamedEntityDelegate]
- -[_ICPortraitLexiconSource _makePPNamedEntityStore]
- -[_ICPortraitLexiconSource hibernate]
- -[_ICPortraitLexiconSource init]
- -[_ICPortraitLexiconSource provideFeedbackForString:type:style:]
- -[_ICPortraitLexiconSource startLoadingWithManager:]
- -[_ICPortraitLexiconSource warmUp]
- _OBJC_CLASS_$_PPContactNameRecordLoadingDelegate
- _OBJC_CLASS_$_PPContactStore
- _OBJC_CLASS_$_PPNamedEntityQuery
- _OBJC_CLASS_$_PPNamedEntityRecordLoadingDelegate
- _OBJC_CLASS_$_PPNamedEntityStore
- _OBJC_CLASS_$__ICPortraitLexiconSource
- _OBJC_IVAR_$__ICPortraitLexiconSource._contactDelegate
- _OBJC_IVAR_$__ICPortraitLexiconSource._contactStore
- _OBJC_IVAR_$__ICPortraitLexiconSource._manager
- _OBJC_IVAR_$__ICPortraitLexiconSource._namedEntityDelegate
- _OBJC_IVAR_$__ICPortraitLexiconSource._namedEntityStore
- _OBJC_METACLASS_$__ICPortraitLexiconSource
- __OBJC_$_INSTANCE_METHODS__ICPortraitLexiconSource
- __OBJC_$_INSTANCE_VARIABLES__ICPortraitLexiconSource
- __OBJC_CLASS_PROTOCOLS_$__ICPortraitLexiconSource
- __OBJC_CLASS_RO_$__ICPortraitLexiconSource
- __OBJC_METACLASS_RO_$__ICPortraitLexiconSource
- ___48-[_ICPortraitLexiconSource _makeContactDelegate]_block_invoke
- ___48-[_ICPortraitLexiconSource _makeContactDelegate]_block_invoke_2
- ___48-[_ICPortraitLexiconSource _makeContactDelegate]_block_invoke_3
- ___48-[_ICPortraitLexiconSource _makeContactDelegate]_block_invoke_4
- ___48-[_ICPortraitLexiconSource _makeContactDelegate]_block_invoke_5
- ___48-[_ICPortraitLexiconSource _makeContactDelegate]_block_invoke_6
- ___51-[_ICPortraitLexiconSource _makePPNamedEntityStore]_block_invoke
- ___52-[_ICPortraitLexiconSource _makeNamedEntityDelegate]_block_invoke
- ___52-[_ICPortraitLexiconSource _makeNamedEntityDelegate]_block_invoke_2
- ___52-[_ICPortraitLexiconSource _makeNamedEntityDelegate]_block_invoke_3
- ___52-[_ICPortraitLexiconSource _makeNamedEntityDelegate]_block_invoke_4
- ___52-[_ICPortraitLexiconSource _makeNamedEntityDelegate]_block_invoke_5
- ___52-[_ICPortraitLexiconSource _makeNamedEntityDelegate]_block_invoke_6
- ___52-[_ICPortraitLexiconSource _makeNamedEntityDelegate]_block_invoke_7
- ___block_descriptor_40_e8_32w_e29_C16?0"PPContactNameRecord"8lw32l8
- ___block_descriptor_40_e8_32w_e29_C16?0"PPNamedEntityRecord"8lw32l8
- ___block_descriptor_40_e8_32w_e5_C8?0lw32l8
- __makePPNamedEntityStore.onceToken
- __makePPNamedEntityStore.store
CStrings:
+ "Failed to read contact change history: %@"
+ "PeopleSuggester ranked %lu of %lu suggested contacts"
+ "_ICContactsLexiconSource loading contacts"
+ "com.apple.inputcontext.contactslexiconsource"
- "C16@?0@\"PPContactNameRecord\"8"
- "C16@?0@\"PPNamedEntityRecord\"8"
- "C8@?0"
- "Error: feedback received by _ICPortraitLexiconSource with unknown type or style: %d / %d"
- "Feedback received by _ICPortraitLexiconSource with type = %d, style = %d"
- "ICLex"
- "ICPortraitLexiconSource"
- "_ICPortraitLexiconSource loading data"
- "failed to load contact name records from Portrait: %@"
- "failed to load named entity records from Portrait: %@"
```
