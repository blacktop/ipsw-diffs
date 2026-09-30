## ContactsAutocompleteUI

> `/System/Library/PrivateFrameworks/ContactsAutocompleteUI.framework/ContactsAutocompleteUI`

```diff

-819.500.71.0.0
-  __TEXT.__text: 0x4a384
+819.500.72.0.0
+  __TEXT.__text: 0x4aaac
   __TEXT.__auth_stubs: 0xad0
-  __TEXT.__objc_methlist: 0x7094
-  __TEXT.__const: 0x424
-  __TEXT.__cstring: 0x16ad
-  __TEXT.__gcc_except_tab: 0x49c
-  __TEXT.__oslogstring: 0xbc5
+  __TEXT.__objc_methlist: 0x70dc
+  __TEXT.__const: 0x434
+  __TEXT.__cstring: 0x16dd
+  __TEXT.__gcc_except_tab: 0x4b4
+  __TEXT.__oslogstring: 0xe98
   __TEXT.__ustring: 0x14
   __TEXT.__dlopen_cstrs: 0x4a
   __TEXT.__swift5_typeref: 0x26

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__unwind_info: 0x1628
+  __TEXT.__unwind_info: 0x1638
   __TEXT.__objc_classname: 0xd7e
-  __TEXT.__objc_methname: 0x14dec
+  __TEXT.__objc_methname: 0x14e0b
   __TEXT.__objc_methtype: 0x52c7
-  __TEXT.__objc_stubs: 0xda80
-  __DATA_CONST.__got: 0x900
+  __TEXT.__objc_stubs: 0xdac0
+  __DATA_CONST.__got: 0x908
   __DATA_CONST.__const: 0x1360
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4e60
-  __DATA_CONST.__objc_superrefs: 0x180
+  __DATA_CONST.__objc_selrefs: 0x4e78
+  __DATA_CONST.__objc_superrefs: 0x188
   __AUTH_CONST.__auth_got: 0x578
-  __AUTH_CONST.__const: 0x600
+  __AUTH_CONST.__const: 0x640
   __AUTH_CONST.__cfstring: 0x1180
   __AUTH_CONST.__objc_const: 0xa0a8
   __AUTH_CONST.__objc_intobj: 0x18

   __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0x5c0
   __DATA.__data: 0xdf0
-  __DATA.__bss: 0x2e0
+  __DATA.__bss: 0x300
   __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0xa00
   __DATA_DIRTY.__bss: 0x48

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B1179CE7-FFF1-324D-8F96-50AB322D30F5
-  Functions: 1975
-  Symbols:   7480
-  CStrings:  4254
+  UUID: 95EC2801-E1AB-38F6-8BAE-F0E4E19565CF
+  Functions: 1983
+  Symbols:   7507
+  CStrings:  4273
 
Symbols:
+ +[CNAutocompleteResultsTableView log]
+ +[CNAutocompleteResultsTableView log].cold.1
+ +[CNAutocompleteSearchController log]
+ +[CNAutocompleteSearchController log].cold.1
+ -[CNAutocompleteResultsTableView didMoveToSuperview]
+ -[CNAutocompleteResultsTableView setHidden:]
+ GCC_except_table27
+ GCC_except_table44
+ GCC_except_table56
+ _NSCocoaErrorDomain
+ _OUTLINED_FUNCTION_7
+ __OBJC_$_CLASS_METHODS_CNAutocompleteResultsTableView
+ __OBJC_$_CLASS_METHODS_CNAutocompleteSearchController
+ ___37+[CNAutocompleteResultsTableView log]_block_invoke
+ ___37+[CNAutocompleteSearchController log]_block_invoke
+ ___45-[CNContactsAutocompleteSearchOperation main]_block_invoke_3
+ ___45-[CNContactsAutocompleteSearchOperation main]_block_invoke_4
+ ___block_literal_global.54
+ ___block_literal_global.71
+ ___block_literal_global.92
+ _log.cn_once_object_790
+ _log.cn_once_token_790
+ _objc_msgSend$code
+ _objc_msgSend$domain
+ _os_log.cn_once_object_794
+ _os_log.cn_once_token_794
+ _shouldUseScreenRelativeFooterViewPositioning.cn_once_object_2
+ _shouldUseScreenRelativeFooterViewPositioning.cn_once_token_2
- +[CNComposeRecipientNamer displayStringForRecipient:].cold.4
- GCC_except_table25
- GCC_except_table40
- GCC_except_table52
- ___45-[CNContactsAutocompleteSearchOperation main]_block_invoke.88
- ___45-[CNContactsAutocompleteSearchOperation main]_block_invoke_2.89
- ___block_literal_global.82
- _os_log.cn_once_object_793
- _os_log.cn_once_token_793
- _shouldUseScreenRelativeFooterViewPositioning.cn_once_object_1
- _shouldUseScreenRelativeFooterViewPositioning.cn_once_token_1
CStrings:
+ "Deferring tableview update"
+ "Hiding results"
+ "Input text changed, length %lu"
+ "Recipients updated, will layoutIfNeeded (count=%lu, inDisambiguationMode=%i)"
+ "Scheduling UI consumption of unified recipients (count:%lu)"
+ "Showing results"
+ "Updating tableview (%lu searchResults, %lu suggestedSearchResults, %lu serverSearchResults)"
+ "[CNAUI-%{public}@] BEGIN CNContactsAutocompleteSearchOperation for \"%{private}@\", length %lu"
+ "[CNAUI-%{public}@] FINISH CNContactsAutocompleteSearchOperation cancelled"
+ "[CNAUI-%{public}@] FINISH CNContactsAutocompleteSearchOperation complete"
+ "[CNAUI-%{public}@] FINISH CNContactsAutocompleteSearchOperation error %{public}@"
+ "[CNAUI-%{public}@] FINISHING"
+ "[CNAUI-%{public}@] Found %ld autocomplete results"
+ "[CNAUI-%{public}@] cancelling"
+ "[CNAUI-%{public}@] consumeAutocompleteSearchResults"
+ "[CNAUI-%{public}@] consumeCorecipientSearchResults"
+ "[CNAUI-%{public}@] consumeResults"
+ "code"
+ "compose-recipient-textview"
+ "didMoveToSuperview"
+ "didReceiveResults (count:%lu, isCancelled:%i)"
+ "domain"
+ "search-controller"
+ "search-manager"
+ "tableView didMoveToSuperview: %{public}@, hidden: %i"
+ "tableView hidden changing: %i -> %i, superview: %{public}@"
+ "tableview"
- "Beginning CNContactsAutocompleteSearchOperation for \"%{private}@\" (task %{public}@)"
- "CNAutocompleteFetch Error for task %{public}@: %@"
- "Group’s display name: '%{private}@'"
- "canceling CNAutocompleteFetch for task %{public}@"
- "contactssearchmanager"
- "task %{public}@ cancelled"
- "task %{public}@ finished"
- "task %{public}@ found %ld autocomplete results"

```
