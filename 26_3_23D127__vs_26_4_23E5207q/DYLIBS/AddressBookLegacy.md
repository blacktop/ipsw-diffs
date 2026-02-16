## AddressBookLegacy

> `/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`

```diff

-12851.400.21.2.2
-  __TEXT.__text: 0x756e8
-  __TEXT.__auth_stubs: 0x2210
-  __TEXT.__objc_methlist: 0x2fc4
-  __TEXT.__const: 0x339
-  __TEXT.__cstring: 0x268f7
-  __TEXT.__oslogstring: 0x24b2
-  __TEXT.__gcc_except_tab: 0x62c
+12851.500.111.0.0
+  __TEXT.__text: 0x75e64
+  __TEXT.__auth_stubs: 0x2200
+  __TEXT.__objc_methlist: 0x3054
+  __TEXT.__const: 0x341
+  __TEXT.__cstring: 0x26ada
+  __TEXT.__oslogstring: 0x270f
+  __TEXT.__gcc_except_tab: 0x638
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x24c
-  __TEXT.__unwind_info: 0x1978
-  __TEXT.__objc_classname: 0x501
-  __TEXT.__objc_methname: 0x922e
-  __TEXT.__objc_methtype: 0x1454
-  __TEXT.__objc_stubs: 0x7c00
-  __DATA_CONST.__got: 0x5c8
+  __TEXT.__unwind_info: 0x1a30
+  __TEXT.__objc_classname: 0x51d
+  __TEXT.__objc_methname: 0x937c
+  __TEXT.__objc_methtype: 0x14e7
+  __TEXT.__objc_stubs: 0x7cc0
+  __DATA_CONST.__got: 0x5d8
   __DATA_CONST.__const: 0x27f8
-  __DATA_CONST.__objc_classlist: 0x190
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24e8
-  __DATA_CONST.__objc_superrefs: 0xf8
+  __DATA_CONST.__objc_selrefs: 0x2520
+  __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x1118
+  __AUTH_CONST.__auth_got: 0x1110
   __AUTH_CONST.__const: 0xe80
-  __AUTH_CONST.__cfstring: 0xd9e0
-  __AUTH_CONST.__objc_const: 0x4b80
+  __AUTH_CONST.__cfstring: 0xdaa0
+  __AUTH_CONST.__objc_const: 0x4cb0
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0xaa0
-  __DATA.__objc_ivar: 0x3f4
+  __AUTH.__objc_data: 0xaf0
+  __DATA.__objc_ivar: 0x400
   __DATA.__data: 0x2c8
   __DATA.__common: 0x4
   __DATA.__bss: 0x358

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 586D4CDA-3C38-32E5-BE05-B98C3838AEA4
-  Functions: 2523
-  Symbols:   7149
-  CStrings:  6064
+  UUID: 7FB57813-144C-3401-8388-06746207A29B
+  Functions: 2582
+  Symbols:   7317
+  CStrings:  6107
 
Symbols:
+ -[ABChangeHistorySummarizer .cxx_destruct]
+ -[ABChangeHistorySummarizer addressBook]
+ -[ABChangeHistorySummarizer dealloc]
+ -[ABChangeHistorySummarizer fetchAllSourcesForClientWithIdentifier:]
+ -[ABChangeHistorySummarizer fetchAllSourcesForClientWithIdentifier:].cold.1
+ -[ABChangeHistorySummarizer fetchAllSourcesForClientWithIdentifier:].cold.2
+ -[ABChangeHistorySummarizer initWithAddressBook:]
+ -[ABChangeHistorySummarizer logDiscoveredSummaryOfChangesForAccountWithIdentifier:]
+ -[ABChangeHistorySummarizer log]
+ -[ABChangeHistorySummarizer summarizeChangesForClientWithIdentifier:]
+ -[ABChangeHistorySummarizer summarizeChangesForClientWithIdentifier:].cold.1
+ -[ABChangeHistorySummarizer summarizeChangesForClientWithIdentifier:].cold.2
+ -[ABChangeHistorySummarizer summarizeChangesInAllSourcesForClientWithIdentifier:]
+ -[ABChangeHistorySummarizer summarizeChangesInAllSourcesForClientWithIdentifier:].cold.1
+ -[ABChangeHistorySummarizer summarizeChangesInSource:forClientIdentifier:]
+ -[ABChangeHistorySummarizer summarizeChangesInSource:forClientIdentifier:].cold.1
+ -[ABChangeHistorySummarizer summarizeChangesInSource:forClientIdentifier:].cold.2
+ -[ABChangeHistorySummarizer summary]
+ GCC_except_table53
+ _ABChangeHistoryCopyAllSourcesTrackedByClient
+ _ABChangeHistoryGetSummaryOfPendingChangesForClient
+ _ABPersonGetShowContactPhotos
+ _ABPersonSetShowContactPhotos
+ _OBJC_CLASS_$_ABChangeHistorySummarizer
+ _OBJC_IVAR_$_ABChangeHistorySummarizer._addressBook
+ _OBJC_IVAR_$_ABChangeHistorySummarizer._log
+ _OBJC_IVAR_$_ABChangeHistorySummarizer._summary
+ _OBJC_METACLASS_$_ABChangeHistorySummarizer
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ __OBJC_$_INSTANCE_METHODS_ABChangeHistorySummarizer
+ __OBJC_$_INSTANCE_VARIABLES_ABChangeHistorySummarizer
+ __OBJC_$_PROP_LIST_ABChangeHistorySummarizer
+ __OBJC_CLASS_RO_$_ABChangeHistorySummarizer
+ __OBJC_METACLASS_RO_$_ABChangeHistorySummarizer
+ ___block_literal_global.123
+ ___block_literal_global.364
+ ___block_literal_global.407
+ ___block_literal_global.409
+ ___block_literal_global.411
+ _kCFBooleanFalse
+ _objc_copyStruct
+ _objc_msgSend$fetchAllSourcesForClientWithIdentifier:
+ _objc_msgSend$init
+ _objc_msgSend$logDiscoveredSummaryOfChangesForAccountWithIdentifier:
+ _objc_msgSend$summarizeChangesForClientWithIdentifier:
+ _objc_msgSend$summarizeChangesInAllSourcesForClientWithIdentifier:
+ _objc_msgSend$summarizeChangesInSource:forClientIdentifier:
+ _objc_retain_x28
- GCC_except_table51
- ___block_literal_global.117
- ___block_literal_global.361
- ___block_literal_global.404
- ___block_literal_global.406
- ___block_literal_global.408
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x23
- _objc_retain_x26
CStrings:
+ "@\"NSObject<OS_os_log>\""
+ "ABChangeHistorySummarizer"
+ "CFArrayRef ABChangeHistoryCopyAllSourcesTrackedByClient(ABAddressBookRef, CFStringRef)"
+ "Changes were truncated for client %{public}@, cannot provide accurate count"
+ "Failed to retrieve change history for client %{public}@"
+ "Failed to retrieve event types array for client %{public}@"
+ "Found %lu sources tracked by client %{public}@"
+ "Getting pending changes count for client: %{public}@"
+ "No sources tracked by client %{public}@"
+ "Pending changes for client %{public}@: added=%d, updated=%d, deleted=%d"
+ "SELECT COUNT(*) FROM %@;"
+ "SELECT DISTINCT store_id FROM ClientCursor WHERE client_identifier = ?;"
+ "T@\"NSObject<OS_os_log>\",R,V_log"
+ "T^v,R,V_addressBook"
+ "T{?=iii},R,V_summary"
+ "Unknown event type %d encountered while counting changes"
+ "_log"
+ "_summary"
+ "change-history-summarization"
+ "clientIdentifier = %@\n>> sources = %@"
+ "com.apple.contacts.addressbook"
+ "fetchAllSourcesForClientWithIdentifier:"
+ "log"
+ "logDiscoveredSummaryOfChangesForAccountWithIdentifier:"
+ "showContactPhotos"
+ "summarizeChangesForClientWithIdentifier:"
+ "summarizeChangesForClientWithIdentifier: called with null addressBook"
+ "summarizeChangesForClientWithIdentifier: called with null clientIdentifier"
+ "summarizeChangesInAllSourcesForClientWithIdentifier:"
+ "summarizeChangesInSource:forClientIdentifier:"
+ "summary"
+ "v32@0:8^v16@24"
+ "vCard image: Cannot compress image to fit within 224KB limit, omitting photo"
+ "vCard image: PNG at quality %.1f still exceeds limit (%lu bytes), reducing quality"
+ "vCard image: PNG exceeds 224KB limit, commpressing the PNG instead"
+ "{?=\"countOfAddedContacts\"i\"countOfUpdatedContacts\"i\"countOfDeletedContacts\"i}"
+ "{?=iii}16@0:8"
+ "{?=iii}24@0:8@16"
- "SELECT COUNT(*) FROM (SELECT NULL FROM %@);"

```
