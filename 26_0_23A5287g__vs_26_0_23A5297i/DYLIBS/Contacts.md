## Contacts

> `/System/Library/Frameworks/Contacts.framework/Contacts`

```diff

-3799.100.2.0.0
-  __TEXT.__text: 0x1b5620
+3801.100.3.1.1
+  __TEXT.__text: 0x1b65f4
   __TEXT.__auth_stubs: 0x3280
-  __TEXT.__objc_methlist: 0x1acc0
+  __TEXT.__objc_methlist: 0x1ad20
   __TEXT.__const: 0x2058
-  __TEXT.__gcc_except_tab: 0x3b08
-  __TEXT.__cstring: 0xc992
+  __TEXT.__gcc_except_tab: 0x3b2c
+  __TEXT.__cstring: 0xc982
   __TEXT.__dlopen_cstrs: 0x8de
-  __TEXT.__oslogstring: 0xb99a
+  __TEXT.__oslogstring: 0xba8a
   __TEXT.__ustring: 0x12
   __TEXT.__constg_swiftt: 0xdc4
   __TEXT.__swift5_typeref: 0xe9f

   __TEXT.__swift5_capture: 0x5d4
   __TEXT.__swift_as_entry: 0x68
   __TEXT.__swift_as_ret: 0x5c
-  __TEXT.__unwind_info: 0x7e40
+  __TEXT.__unwind_info: 0x7e70
   __TEXT.__eh_frame: 0x25b8
   __TEXT.__objc_classname: 0x43df
-  __TEXT.__objc_methname: 0x2b116
+  __TEXT.__objc_methname: 0x2b208
   __TEXT.__objc_methtype: 0x53e4
-  __TEXT.__objc_stubs: 0x1e4e0
+  __TEXT.__objc_stubs: 0x1e560
   __DATA_CONST.__got: 0x1b50
-  __DATA_CONST.__const: 0x6200
+  __DATA_CONST.__const: 0x61c0
   __DATA_CONST.__objc_classlist: 0x10e0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x95e0
+  __DATA_CONST.__objc_selrefs: 0x9600
   __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0x9a8
+  __DATA_CONST.__objc_superrefs: 0x9b0
   __DATA_CONST.__objc_arraydata: 0x268
   __AUTH_CONST.__auth_got: 0x1950
-  __AUTH_CONST.__const: 0x6888
-  __AUTH_CONST.__cfstring: 0xd9a0
-  __AUTH_CONST.__objc_const: 0x2ba08
+  __AUTH_CONST.__const: 0x6848
+  __AUTH_CONST.__cfstring: 0xd9c0
+  __AUTH_CONST.__objc_const: 0x2ba78
   __AUTH_CONST.__objc_intobj: 0x5d0
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x56b0
   __AUTH.__data: 0x660
-  __DATA.__objc_ivar: 0x124c
+  __DATA.__objc_ivar: 0x1254
   __DATA.__data: 0x2d20
   __DATA.__bss: 0x24a0
   __DATA.__common: 0x80
   __DATA_DIRTY.__objc_data: 0x5d48
   __DATA_DIRTY.__data: 0x38
-  __DATA_DIRTY.__bss: 0xfd8
+  __DATA_DIRTY.__bss: 0xfe8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ClassKit.framework/ClassKit
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 93AA36E3-C4D6-398F-8958-7B096D50B15B
-  Functions: 12407
-  Symbols:   36370
-  CStrings:  12742
+  UUID: D7640C89-E1EB-36D3-B623-A7D40E53B888
+  Functions: 12422
+  Symbols:   36420
+  CStrings:  12756
 
Symbols:
+ +[CNContactPosterUpdateRequest requestToUpdateWatchWallpaper:forContactIdentifier:]
+ +[CNGeminiChannel os_log]
+ +[CNGeminiChannel os_log].cold.1
+ +[CNUserActivityRestoration exactMatchForNameAndAtLeastOneHandleFromPayload:containerIdentifiers:contactStore:]
+ +[CNUserActivityRestoration exactMatchForNameAndAtLeastOneHandleFromPayload:containerIdentifiers:contactStore:].cold.1
+ +[CNUserActivityRestoration exactMatchForNameAndAtLeastOneHandleFromPayload:containerIdentifiers:contactStore:].cold.2
+ +[CNUserActivityRestoration exactMatchForNameAndAtLeastOneHandleFromPayload:containerIdentifiers:contactStore:].cold.3
+ +[CNUserActivityRestoration exactMatchForNameAndAtLeastOneHandleFromPayload:containerIdentifiers:contactStore:].cold.4
+ +[CNUserActivityRestoration exactNameMatchFoundForPayload:withContact:]
+ -[CNChangesNotifier fakePostDidSavePosters]
+ -[CNChangesNotifierProxy receiveExternalNotificationName:].cold.1
+ -[CNChangesNotifierProxy receiveNotificationNames:fromSender:saveIdentifier:userInfo:calledFromNotifierQueue:isFromExternalProcess:]
+ -[CNContactPosterUpdateRequest .cxx_destruct]
+ -[CNContactPosterUpdateRequest contactIdentifier]
+ -[CNContactPosterUpdateRequest initWithWatchWallpaperImages:contactIdentifier:]
+ -[CNContactPosterUpdateRequest watchWallpaperImages]
+ -[CNWatchWallpaperImageDataDescription(PosterData) posterDataChangeRequestsForValue:contactIdentifier:]
+ GCC_except_table128
+ GCC_except_table134
+ GCC_except_table53
+ GCC_except_table88
+ _CNLabelUnknown
+ _OBJC_IVAR_$_CNContactPosterUpdateRequest._contactIdentifier
+ _OBJC_IVAR_$_CNContactPosterUpdateRequest._watchWallpaperImages
+ __OBJC_$_INSTANCE_METHODS_CNWatchWallpaperImageDataDescription(iOSBuffers|PosterData|iOSAB)
+ __OBJC_$_INSTANCE_VARIABLES_CNContactPosterUpdateRequest
+ __OBJC_$_PROP_LIST_CNContactPosterUpdateRequest
+ ___132-[CNChangesNotifierProxy receiveNotificationNames:fromSender:saveIdentifier:userInfo:calledFromNotifierQueue:isFromExternalProcess:]_block_invoke
+ ___132-[CNChangesNotifierProxy receiveNotificationNames:fromSender:saveIdentifier:userInfo:calledFromNotifierQueue:isFromExternalProcess:]_block_invoke_2
+ ___132-[CNChangesNotifierProxy receiveNotificationNames:fromSender:saveIdentifier:userInfo:calledFromNotifierQueue:isFromExternalProcess:]_block_invoke_3
+ ___25+[CNGeminiChannel os_log]_block_invoke
+ ___72-[CNContactDiff(PosterData) posterDataRequestsForContactWithIdentifier:]_block_invoke_2
+ ___72-[CNGeminiManager remoteBestSenderIdentityForHandle:contactStore:error:]_block_invoke.178
+ ___72-[CNGeminiManager remoteBestSenderIdentityForHandle:contactStore:error:]_block_invoke.cold.1
+ ___83-[CNGeminiManager remoteGeminiResultForContact:substituteDefaultForDangling:error:]_block_invoke.174
+ ___83-[CNGeminiManager remoteGeminiResultForContact:substituteDefaultForDangling:error:]_block_invoke.cold.1
+ ___block_descriptor_48_e8_32r40r_e42_B16?0"CNContactPosterDataChangeRequest"8lr32l8r40l8
+ ___block_descriptor_56_e8_32s40r48r_e47_"NSArray"16?0"<CNContactUpdate_PosterData>"8ls32l8r40l8r48l8
+ ___block_literal_global.182
+ ___block_literal_global.195
+ ___block_literal_global.365
+ _descriptorForRequiredKeys.cn_once_object_5
+ _descriptorForRequiredKeys.cn_once_token_5
+ _objc_msgSend$_cn_objectOrDefaultToEmptyArrayForKey:
+ _objc_msgSend$exactNameMatchFoundForPayload:withContact:
+ _objc_msgSend$initWithWatchWallpaperImages:contactIdentifier:
+ _objc_msgSend$posters
+ _objc_msgSend$predicateForContactsMatchingName:
+ _objc_msgSend$predicateForContactsWithOrganizationName:
+ _objc_msgSend$requestToUpdateWatchWallpaper:forContactIdentifier:
+ _objc_msgSend$watchWallpaperImages
- -[CNHandleStringsContactPredicate(CoreRecents) emailsMatchingSearchClassification:forContact:]
- -[CNHandleStringsContactPredicate(CoreRecents) phoneNumbersMatchingSearchClassification:forContact:]
- GCC_except_table126
- GCC_except_table25
- GCC_except_table46
- GCC_except_table51
- GCC_except_table65
- GCC_except_table86
- __OBJC_$_INSTANCE_METHODS_CNWatchWallpaperImageDataDescription(iOSBuffers|iOSAB)
- ___100-[CNHandleStringsContactPredicate(CoreRecents) phoneNumbersMatchingSearchClassification:forContact:]_block_invoke
- ___100-[CNHandleStringsContactPredicate(CoreRecents) phoneNumbersMatchingSearchClassification:forContact:]_block_invoke_2
- ___100-[CNHandleStringsContactPredicate(CoreRecents) phoneNumbersMatchingSearchClassification:forContact:]_block_invoke_3
- ___100-[CNHandleStringsContactPredicate(CoreRecents) phoneNumbersMatchingSearchClassification:forContact:]_block_invoke_4
- ___100-[CNHandleStringsContactPredicate(CoreRecents) phoneNumbersMatchingSearchClassification:forContact:]_block_invoke_5
- ___131-[CNChangesNotifierProxy receiveNotificationName:fromSender:saveIdentifier:userInfo:calledFromNotifierQueue:isFromExternalProcess:]_block_invoke_2
- ___131-[CNChangesNotifierProxy receiveNotificationName:fromSender:saveIdentifier:userInfo:calledFromNotifierQueue:isFromExternalProcess:]_block_invoke_3
- ___72-[CNGeminiManager remoteBestSenderIdentityForHandle:contactStore:error:]_block_invoke_2
- ___75-[CNHandleStringsContactPredicate(CoreRecents) contactsFromRecentsLibrary:]_block_invoke
- ___83-[CNGeminiManager remoteGeminiResultForContact:substituteDefaultForDangling:error:]_block_invoke.172
- ___94-[CNHandleStringsContactPredicate(CoreRecents) emailsMatchingSearchClassification:forContact:]_block_invoke
- ___94-[CNHandleStringsContactPredicate(CoreRecents) emailsMatchingSearchClassification:forContact:]_block_invoke_2
- ___block_descriptor_32_e23_16?0"CNPhoneNumber"8l
- ___block_descriptor_40_e8_32s_e23_B16?0"CNPhoneNumber"8ls32l8
- ___block_descriptor_40_e8_32s_e27_"CNPair"16?0"CNContact"8ls32l8
- ___block_descriptor_40_e8_32s_e47_"NSArray"16?0"<CNContactUpdate_PosterData>"8ls32l8
- ___block_literal_global.168
- ___block_literal_global.176
- ___block_literal_global.192
- ___block_literal_global.363
- _descriptorForRequiredKeys.cn_once_object_3
- _descriptorForRequiredKeys.cn_once_token_3
- _objc_msgSend$componentsFromString:options:
- _objc_msgSend$emailsMatchingSearchClassification:forContact:
- _objc_msgSend$phoneNumbersMatchingSearchClassification:forContact:
- _objc_msgSend$setNickname:
CStrings:
+ "B16@?0@\"CNContactPosterDataChangeRequest\"8"
+ "Error fetching contacts by handle: %@"
+ "Error fetching contacts by name: %@"
+ "Received a dictionary with no handles or names, giving up"
+ "Supports Gemini: %i"
+ "T@\"NSArray\",R,C,N,V_watchWallpaperImages"
+ "We can't match an empty dictionary"
+ "_$!<Unknown>!$_"
+ "_cn_objectOrDefaultToEmptyArrayForKey:"
+ "_watchWallpaperImages"
+ "exactMatchForNameAndAtLeastOneHandleFromPayload:containerIdentifiers:contactStore:"
+ "exactNameMatchFoundForPayload:withContact:"
+ "fakePostDidSavePosters"
+ "gemini"
+ "initWithWatchWallpaperImages:contactIdentifier:"
+ "requestToUpdateWatchWallpaper:forContactIdentifier:"
+ "watchWallpaperImages"
- "@16@?0@\"CNPhoneNumber\"8"
- "B16@?0@\"CNPhoneNumber\"8"
- "componentsFromString:options:"
- "emailsMatchingSearchClassification:forContact:"
- "phoneNumbersMatchingSearchClassification:forContact:"

```
