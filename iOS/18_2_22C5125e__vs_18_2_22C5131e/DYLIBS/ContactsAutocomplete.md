## ContactsAutocomplete

> `/System/Library/PrivateFrameworks/ContactsAutocomplete.framework/ContactsAutocomplete`

```diff

-1337.0.0.0.0
-  __TEXT.__text: 0x586f8
-  __TEXT.__auth_stubs: 0x11b0
-  __TEXT.__objc_methlist: 0x3d2c
-  __TEXT.__const: 0x307a
-  __TEXT.__oslogstring: 0x3621
-  __TEXT.__cstring: 0x2e33
+1339.0.0.0.0
+  __TEXT.__text: 0x58950
+  __TEXT.__auth_stubs: 0x1200
+  __TEXT.__objc_methlist: 0x3d74
+  __TEXT.__const: 0x306a
+  __TEXT.__oslogstring: 0x362c
+  __TEXT.__cstring: 0x2eb3
   __TEXT.__gcc_except_tab: 0x718
-  __TEXT.__constg_swiftt: 0xca4
-  __TEXT.__swift5_typeref: 0xd38
-  __TEXT.__swift5_fieldmd: 0x958
-  __TEXT.__swift5_types: 0xbc
-  __TEXT.__swift5_reflstr: 0x626
+  __TEXT.__constg_swiftt: 0xc7c
+  __TEXT.__swift5_typeref: 0xd3e
+  __TEXT.__swift5_fieldmd: 0x924
+  __TEXT.__swift5_types: 0xb8
+  __TEXT.__swift5_reflstr: 0x61e
   __TEXT.__swift5_assocty: 0x1f8
   __TEXT.__swift5_proto: 0x2dc
-  __TEXT.__swift5_capture: 0x68
+  __TEXT.__swift5_capture: 0x38
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1d98
-  __TEXT.__eh_frame: 0x9d8
+  __TEXT.__unwind_info: 0x1da0
+  __TEXT.__eh_frame: 0xa10
   __TEXT.__objc_classname: 0x10eb
-  __TEXT.__objc_methname: 0x9fb8
+  __TEXT.__objc_methname: 0xa0fd
   __TEXT.__objc_methtype: 0x11e8
-  __TEXT.__objc_stubs: 0x8680
-  __DATA_CONST.__got: 0x878
+  __TEXT.__objc_stubs: 0x8740
+  __DATA_CONST.__got: 0x868
   __DATA_CONST.__const: 0x1758
-  __DATA_CONST.__objc_classlist: 0x3c0
+  __DATA_CONST.__objc_classlist: 0x3b8
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2560
+  __DATA_CONST.__objc_selrefs: 0x2590
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x8e8
+  __AUTH_CONST.__auth_got: 0x910
   __AUTH_CONST.__auth_ptr: 0x4f0
-  __AUTH_CONST.__const: 0x1eb8
-  __AUTH_CONST.__cfstring: 0x1e60
-  __AUTH_CONST.__objc_const: 0xac58
+  __AUTH_CONST.__const: 0x1e68
+  __AUTH_CONST.__cfstring: 0x1e80
+  __AUTH_CONST.__objc_const: 0xabe8
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x2d0
-  __AUTH.__data: 0x9e8
-  __DATA.__objc_ivar: 0x444
-  __DATA.__data: 0x1508
-  __DATA.__bss: 0x57c0
+  __AUTH.__objc_data: 0x2d8
+  __AUTH.__data: 0x938
+  __DATA.__objc_ivar: 0x44c
+  __DATA.__data: 0x1518
+  __DATA.__bss: 0x5800
   __DATA.__common: 0xd8
   __DATA_DIRTY.__objc_data: 0x2120
   __DATA_DIRTY.__data: 0x308
-  __DATA_DIRTY.__bss: 0x1f8
+  __DATA_DIRTY.__bss: 0x1d8
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/ClassKit.framework/ClassKit
+  - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2840
-  Symbols:   2218
-  CStrings:  2695
+  Functions: 2843
+  Symbols:   2226
+  CStrings:  2707
 
Symbols:
+ __swift_stdlib_reportUnimplementedInitializer
CStrings:
+ "\x02\x121"
+ "\a\x12"
+ "-[CNAutocompleteDelegateWrapper autocompleteFetchHitMaximumResultsCount:results:]"
+ "CNAutocompleteDelegateWrapper.m"
+ "ContactsAutocomplete.StoreSpy"
+ "Query is complete (%!s(MISSING)) with: %!l(MISSING)d items"
+ "T@\"CNContactStore\",R"
+ "T@\"NSArray\",&,V_completeResults"
+ "T@\"NSLocale\",R"
+ "T@\"NSOrderedSet\",R"
+ "TQ,V_maximumResultsCount"
+ "[%!{(MISSING)public}@] Reached maximumResultsCount (%!l(MISSING)u) completeResults: (%!l(MISSING)u), cancelling."
+ "[%!{(MISSING)public}@] Search operation complete."
+ "_autocompleteFetch:distributeReceivedResults:"
+ "_cancelationToken.isCanceled"
+ "_completeResults"
+ "_maximumResultsCount"
+ "autocompleteFetchHitMaximumResultsCount:results:"
+ "completeResults"
+ "init()"
+ "maximumResultsCount"
+ "setCompleteResults:"
+ "setMaximumResultsCount:"
+ "streamContinuation"
- "\x02\x12!"
- "\a\x11"
- "Error fetching autocomplete results: %!@(MISSING)"
- "Finishing continuation"
- "Query is complete (%!s(MISSING))"
- "Received %!{(MISSING)private}s"
- "Received results"
- "_TtC20ContactsAutocompleteP33_EBE34D4C21093596BE6E4DA9F1A7E5D210QueryScope"
- "onError"
- "onFinish"
- "onResults"

```
