## Contacts

> `/System/Library/Frameworks/Contacts.framework/Versions/A/Contacts`

```diff

-3650.0.0.0.0
-  __TEXT.__text: 0x18a6d4
-  __TEXT.__auth_stubs: 0x1ee0
-  __TEXT.__objc_methlist: 0x156f0
+3652.0.0.0.0
+  __TEXT.__text: 0x18dfb0
+  __TEXT.__auth_stubs: 0x1f70
+  __TEXT.__objc_methlist: 0x15740
   __TEXT.__const: 0x1268
-  __TEXT.__cstring: 0xba32
-  __TEXT.__oslogstring: 0x7e6a
-  __TEXT.__gcc_except_tab: 0x2254
+  __TEXT.__cstring: 0xbb52
+  __TEXT.__oslogstring: 0x804a
+  __TEXT.__gcc_except_tab: 0x2268
   __TEXT.__dlopen_cstrs: 0x482
   __TEXT.__ustring: 0xe
   __TEXT.__constg_swiftt: 0xc24

   __TEXT.__swift5_proto: 0x90
   __TEXT.__swift5_types: 0x8c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_capture: 0x308
-  __TEXT.__unwind_info: 0x6928
-  __TEXT.__eh_frame: 0x1b38
+  __TEXT.__swift5_capture: 0x364
+  __TEXT.__unwind_info: 0x69e0
+  __TEXT.__eh_frame: 0x1dc8
   __TEXT.__objc_classname: 0x38b9
-  __TEXT.__objc_methname: 0x25abd
+  __TEXT.__objc_methname: 0x25bda
   __TEXT.__objc_methtype: 0x4261
-  __TEXT.__objc_stubs: 0x1b6a0
-  __DATA_CONST.__got: 0x17d0
-  __DATA_CONST.__const: 0x2840
+  __TEXT.__objc_stubs: 0x1b7c0
+  __DATA_CONST.__got: 0x17d8
+  __DATA_CONST.__const: 0x2870
   __DATA_CONST.__objc_classlist: 0xe80
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x280
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8868
+  __DATA_CONST.__objc_selrefs: 0x88c0
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x7f8
   __DATA_CONST.__objc_arraydata: 0x330
-  __AUTH_CONST.__auth_got: 0xf80
+  __AUTH_CONST.__auth_got: 0xfc8
   __AUTH_CONST.__auth_ptr: 0x3f8
-  __AUTH_CONST.__const: 0x96b0
-  __AUTH_CONST.__cfstring: 0xca40
-  __AUTH_CONST.__objc_const: 0x27fb8
+  __AUTH_CONST.__const: 0x9808
+  __AUTH_CONST.__cfstring: 0xca60
+  __AUTH_CONST.__objc_const: 0x27fc0
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_dictobj: 0x208
-  __AUTH.__objc_data: 0x2b28
+  __AUTH.__objc_data: 0x2b40
   __AUTH.__data: 0x500
   __DATA.__objc_ivar: 0xef8
-  __DATA.__data: 0x2640
+  __DATA.__data: 0x2660
   __DATA.__bss: 0x2a40
   __DATA.__common: 0x88
   __DATA_DIRTY.__objc_data: 0x7030

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 10421
-  Symbols:   21232
-  CStrings:  2197
+  Functions: 10466
+  Symbols:   21270
+  CStrings:  2206
 
Symbols:
+ +[CNContactProviderSupportDomainCommand invalidateDomain:]
+ +[CNContactProviderSupportDomainCommand invalidateDomain:].cold.1
+ -[CNCDContactFetcher faultContactIdsInFetchedContacts]
+ -[CNCDContactFetcher fetchContactsWithPredicate:]
+ -[CNCDContactFetcher mergeContactImpls:]
+ -[CNContactProviderSupport invalidateDomainWithCompletionHandler:]
+ -[CNContactProviderSupportManager invalidateDomain:bundleIdentifier:error:]
+ GCC_except_table31
+ _ABCDRecordToUniqueIdTransform
+ _CFUserNotificationDisplayAlert
+ _CNProviderDomainCommandTypeInvalidateDomain
+ ___40-[CNCDContactFetcher mergeContactImpls:]_block_invoke
+ ___40-[CNCDContactFetcher mergeContactImpls:]_block_invoke_2
+ ___54-[CNCDContactFetcher faultContactIdsInFetchedContacts]_block_invoke
+ ___54-[CNCDContactFetcher faultContactIdsInFetchedContacts]_block_invoke_2
+ ___block_descriptor_32_e26_"NSArray"16?0"NSArray"8l
+ ___block_descriptor_32_e27_"NSNumber"16?0"NSArray"8l
+ ___block_descriptor_40_e8_32s_e21_B16?0"CNCDContact"8l
+ ___block_descriptor_40_e8_32s_e21_v16?0"CNCDContact"8l
+ ___block_descriptor_40_e8_32s_e26_"NSArray"16?0"NSArray"8l
+ ___block_descriptor_48_e8_32s40r_e35_v24?0"CNPropertyDescription"8^B16l
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_Contacts
+ _objc_msgSend$faultContactIdsInFetchedContacts
+ _objc_msgSend$fetchContactsWithPredicate:
+ _objc_msgSend$hasFaultForRelationshipNamed:
+ _objc_msgSend$invalidateDomain:
+ _objc_msgSend$invalidateDomain:bundleIdentifier:error:
+ _objc_msgSend$invalidateExtensionFor:bundleIdentifier:completionHandler:
+ _objc_msgSend$isFault
+ _objc_msgSend$map:
+ _objc_msgSend$mergeContactImpls:
+ areNotesInaccessible.cn_once_object_3
+ areNotesInaccessible.cn_once_token_3
+ block_copy_helper.62
+ block_copy_helper.70
+ block_copy_helper.76
+ block_copy_helper.82
+ block_descriptor.64
+ block_descriptor.72
+ block_descriptor.78
+ block_descriptor.84
+ block_destroy_helper.63
+ block_destroy_helper.71
+ block_destroy_helper.77
+ block_destroy_helper.83
+ isAddressingGrammarInaccessible.cn_once_object_8
+ isAddressingGrammarInaccessible.cn_once_token_8
+ keyVectorByRemovingInaccessibleKeysFromVector:.cn_once_object_2
+ keyVectorByRemovingInaccessibleKeysFromVector:.cn_once_token_2
+ objectdestroy.57Tm
+ objectdestroy.60Tm
- ___block_descriptor_32_e27_"CNResult"16?0"NSArray"8l
- ___block_descriptor_40_e8_32s_e27_"CNResult"16?0"NSArray"8l
- __block_literal_global.25
- areNotesInaccessible.cn_once_object_2
- areNotesInaccessible.cn_once_token_2
- block_copy_helper.49
- block_copy_helper.55
- block_descriptor.51
- block_descriptor.57
- block_destroy_helper.50
- block_destroy_helper.56
- isAddressingGrammarInaccessible.cn_once_object_7
- isAddressingGrammarInaccessible.cn_once_token_7
- keyVectorByRemovingInaccessibleKeysFromVector:.cn_once_object_1
- keyVectorByRemovingInaccessibleKeysFromVector:.cn_once_token_1
CStrings:
+ "@\"NSNumber\"16@?0@\"NSArray\"8"
+ "B16@?0@\"CNCDContact\"8"
+ "ENABLE_ALERT_BUTTON_ALLOW"
+ "ENABLE_ALERT_BUTTON_DENY"
+ "ENABLE_ALERT_MESSAGE "
+ "ENABLE_ALERT_TITLE "
+ "InvalidateDomain"
+ "invalidateExtension(for:bundleIdentifier:)"
+ "v16@?0@\"CNCDContact\"8"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "@\"CNResult\"16@?0@\"NSArray\"8"

```
