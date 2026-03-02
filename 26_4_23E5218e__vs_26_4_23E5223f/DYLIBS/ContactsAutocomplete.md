## ContactsAutocomplete

> `/System/Library/PrivateFrameworks/ContactsAutocomplete.framework/ContactsAutocomplete`

```diff

-1356.500.32.0.0
-  __TEXT.__text: 0x59ae4
+1356.500.41.0.0
+  __TEXT.__text: 0x59ad4
   __TEXT.__auth_stubs: 0x1130
   __TEXT.__objc_methlist: 0x4544
   __TEXT.__const: 0x3620
-  __TEXT.__oslogstring: 0x36ac
+  __TEXT.__oslogstring: 0x369c
   __TEXT.__cstring: 0x2485
   __TEXT.__gcc_except_tab: 0x6fc
   __TEXT.__constg_swiftt: 0xc84

   __TEXT.__unwind_info: 0x1db8
   __TEXT.__eh_frame: 0xba8
   __TEXT.__objc_classname: 0x168e
-  __TEXT.__objc_methname: 0xa3fa
+  __TEXT.__objc_methname: 0xa40a
   __TEXT.__objc_methtype: 0x1217
-  __TEXT.__objc_stubs: 0x88e0
+  __TEXT.__objc_stubs: 0x8900
   __DATA_CONST.__got: 0x890
   __DATA_CONST.__const: 0x1790
   __DATA_CONST.__objc_classlist: 0x3c0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2650
+  __DATA_CONST.__objc_selrefs: 0x2658
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C017DFA3-E072-3AB7-856C-FA29F8982F32
+  UUID: EE3DB465-1667-3DEE-9ACC-96AE57015105
   Functions: 2792
-  Symbols:   6722
-  CStrings:  2925
+  Symbols:   6723
+  CStrings:  2926
 
Symbols:
+ _objc_msgSend$addEntriesFromDictionary:
Functions:
~ -[CNAutocompleteDelegateWrapper _autocompleteFetch:distributeReceivedResults:] : 468 -> 528
~ -[CNAutocompleteQueryResponsePreparer resultsNotPreviouslyReturned:] : 160 -> 192
~ -[CNAutocompleteResult isEqual:] : 336 -> 192
~ -[CNAutocompleteResult updateUsingInformationFromRelatedResult:] : 1724 -> 1760
CStrings:
+ "About to tell our delegate about %@ results deduped from %@ total"
+ "Merged userInfo for two identical results: %@"
+ "Using sorting algorithm provided by client"
+ "addEntriesFromDictionary:"
- "About to tell our delegate about %@ results"
- "Serious bug: I don't expect dupes with userInfos, dropping %@, keeping only %@"
- "Using sorting algoritm provided by client"

```
