## ContactsAutocomplete

> `/System/Library/PrivateFrameworks/ContactsAutocomplete.framework/Versions/A/ContactsAutocomplete`

```diff

-1224.0.0.0.0
-  __TEXT.__text: 0x4f41c
-  __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_methlist: 0x387c
-  __TEXT.__const: 0x1520
+1226.0.0.0.0
+  __TEXT.__text: 0x4f948
+  __TEXT.__auth_stubs: 0xf70
+  __TEXT.__objc_methlist: 0x386c
+  __TEXT.__const: 0x1510
   __TEXT.__oslogstring: 0x2e87
-  __TEXT.__cstring: 0x279f
+  __TEXT.__cstring: 0x265f
   __TEXT.__gcc_except_tab: 0x670
-  __TEXT.__constg_swiftt: 0x5b8
-  __TEXT.__swift5_typeref: 0x94a
-  __TEXT.__swift5_fieldmd: 0x574
+  __TEXT.__constg_swiftt: 0x5c0
+  __TEXT.__swift5_typeref: 0x96d
+  __TEXT.__swift5_fieldmd: 0x568
   __TEXT.__swift5_types: 0x70
   __TEXT.__swift5_reflstr: 0x3f2
   __TEXT.__swift5_assocty: 0x1d8

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x16a0
+  __TEXT.__unwind_info: 0x16d8
   __TEXT.__eh_frame: 0x610
   __TEXT.__objc_classname: 0xfb5
-  __TEXT.__objc_methname: 0x96b9
-  __TEXT.__objc_methtype: 0x10ff
-  __TEXT.__objc_stubs: 0x7cc0
+  __TEXT.__objc_methname: 0x96be
+  __TEXT.__objc_methtype: 0x1115
+  __TEXT.__objc_stubs: 0x7ce0
   __DATA_CONST.__got: 0x868
-  __DATA_CONST.__const: 0x6b8
+  __DATA_CONST.__const: 0x6d8
   __DATA_CONST.__objc_classlist: 0x358
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22a8
+  __DATA_CONST.__objc_selrefs: 0x22b0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x7b0
-  __AUTH_CONST.__auth_ptr: 0x4c0
-  __AUTH_CONST.__const: 0x2700
+  __AUTH_CONST.__auth_got: 0x7c8
+  __AUTH_CONST.__auth_ptr: 0x4d0
+  __AUTH_CONST.__const: 0x2720
   __AUTH_CONST.__cfstring: 0x1c60
-  __AUTH_CONST.__objc_const: 0x95f0
+  __AUTH_CONST.__objc_const: 0x95e0
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x7a8
-  __AUTH.__data: 0x8e0
+  __AUTH.__data: 0x8f0
   __DATA.__objc_ivar: 0x3d8
-  __DATA.__data: 0xec8
-  __DATA.__bss: 0x2600
+  __DATA.__data: 0xee8
+  __DATA.__bss: 0x2610
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x1770
   __DATA_DIRTY.__data: 0x68

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2162
-  Symbols:   4552
-  CStrings:  400
+  Functions: 2169
+  Symbols:   4566
+  CStrings:  395
 
Symbols:
+ -[CNAutocompleteCalendarServerSearch initWithEventStoreProvider:operationFactory:]
+ GCC_except_table12
+ OBJC_IVAR_$_CNAutocompleteCalendarServerSearch._eventStoreProvider
+ _EKEphemeralCacheEventStoreProviderFunction
+ __97-[CNAutocompleteCalendarServerSearch executeRequest:source:resultsFactory:withCompletionHandler:]_block_invoke.18
+ __97-[CNAutocompleteCalendarServerSearch executeRequest:source:resultsFactory:withCompletionHandler:]_block_invoke.20
+ __97-[CNAutocompleteCalendarServerSearch executeRequest:source:resultsFactory:withCompletionHandler:]_block_invoke.24
+ ___42-[CNAutocompleteCalendarServerSearch init]_block_invoke
+ ___block_descriptor_32_e19_"EKEventStore"8?0l
+ __block_literal_global.109
+ _classEKEphemeralCacheEventStoreProvider
+ _getEKEphemeralCacheEventStoreProviderClass
+ _initEKEphemeralCacheEventStoreProvider
+ _objc_msgSend$initWithCreationBlock:
+ _objc_msgSend$initWithEventStoreProvider:operationFactory:
+ _swift_dynamicCastClass
+ _swift_unknownObjectRetain_n
+ _symbolic Say_____G 20ContactsAutocomplete16ComposeRecipientV6HandleV
+ _symbolic _____Sg 20ContactsAutocomplete16ComposeRecipientV6HandleV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10AppIntents12IntentPersonV6HandleV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 20ContactsAutocomplete16ComposeRecipientV6HandleV
- -[CNAutocompleteCalendarServerSearch eventStore]
- -[CNAutocompleteCalendarServerSearch initWithEventStore:operationFactory:]
- OBJC_IVAR_$_CNAutocompleteCalendarServerSearch._eventStore
- __97-[CNAutocompleteCalendarServerSearch executeRequest:source:resultsFactory:withCompletionHandler:]_block_invoke.17
- __97-[CNAutocompleteCalendarServerSearch executeRequest:source:resultsFactory:withCompletionHandler:]_block_invoke.19
- __97-[CNAutocompleteCalendarServerSearch executeRequest:source:resultsFactory:withCompletionHandler:]_block_invoke.23
- _objc_msgSend$initWithEventStore:operationFactory:
- _symbolic Say_____G 20ContactsAutocomplete16ComposeRecipientV
CStrings:
+ "@\"EKEventStore\"8@?0"
+ "Compose Recipient"
+ "EKEphemeralCacheEventStoreProvider"
+ "The names to search for"
+ "The services to check for availability"
+ "Title for Complete (verb) Name Intent"
- "AUTOCOMPLETE_QUERY_INTENT_DESCRIPTION"
- "AUTOCOMPLETE_QUERY_INTENT_NAME"
- "AUTOCOMPLETE_QUERY_INTENT_PARAMETER_NAMES_DESCRIPTION"
- "AUTOCOMPLETE_QUERY_INTENT_PARAMETER_NAMES_LABEL"
- "AUTOCOMPLETE_QUERY_INTENT_PARAMETER_SERVICES_DESCRIPTION"
- "AUTOCOMPLETE_QUERY_INTENT_PARAMETER_SERVICES_LABEL"
- "COMPOSE_RECIPIENT_ENTITY_NAME"
- "COMPOSE_RECIPIENT_ENTITY_PROPERTY_CHILDREN_NAME"
- "COMPOSE_RECIPIENT_ENTITY_PROPERTY_PERSON_NAME"
- "COMPOSE_RECIPIENT_ENTITY_PROPERTY_STATUS_NAME"
- "Title for Complete Name Intent"

```
