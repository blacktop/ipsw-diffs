## Categories

> `/System/Library/PrivateFrameworks/Categories.framework/Versions/A/Categories`

```diff

-56.0.0.0.0
-  __TEXT.__text: 0xc3e8
-  __TEXT.__objc_methlist: 0x7c4
+58.0.1.0.0
+  __TEXT.__text: 0xc85c
+  __TEXT.__objc_methlist: 0x82c
   __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x424
-  __TEXT.__cstring: 0x2d0c
+  __TEXT.__gcc_except_tab: 0x428
+  __TEXT.__cstring: 0x2dbc
   __TEXT.__oslogstring: 0x656
-  __TEXT.__unwind_info: 0x3d0
+  __TEXT.__unwind_info: 0x3e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x130
+  __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6c8
+  __DATA_CONST.__objc_selrefs: 0x720
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__objc_arraydata: 0xaa0
+  __DATA_CONST.__objc_arraydata: 0xab8
   __DATA_CONST.__got: 0xf0
-  __AUTH_CONST.__const: 0x7a0
-  __AUTH_CONST.__cfstring: 0x3620
-  __AUTH_CONST.__objc_const: 0xc70
+  __AUTH_CONST.__const: 0x830
+  __AUTH_CONST.__cfstring: 0x36c0
+  __AUTH_CONST.__objc_const: 0xca0
   __AUTH_CONST.__objc_arrayobj: 0x990
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x4c
+  __DATA.__objc_ivar: 0x50
   __DATA.__data: 0x1e8
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x230

   - /System/Library/PrivateFrameworks/ContextKit.framework/Versions/A/ContextKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 240
-  Symbols:   674
-  CStrings:  496
+  Functions: 250
+  Symbols:   698
+  CStrings:  501
 
Symbols:
+ +[CTCategories _cacheKeyForBundleID:targetUserIsU13:]
+ +[CTCategory _bundleCategoriesLookupResultsForBundleIdentifiers:platform:withCompletionHandler:]
+ +[CTCategory categoryForBundleID:platform:targetUserIsU13:withCompletionHandler:]
+ +[CTCategory categoryForBundleIdentifiers:platform:targetUserIsU13:withCompletionHandler:]
+ +[CTCategory categoryForBundleIdentifiers:platform:version:targetUserIsU13:withCompletionHandler:]
+ +[CTCategoryResolver resolvedIdentifierForVersion:appStoreCategories:ckIdentifier:systemOverride:targetUserIsU13:]
+ -[CTAppStoreCategories contentDescriptors]
+ -[CTAppStoreCategories initWithPrimary:secondary:contentDescriptors:]
+ -[CTCategories categoriesForBundleIDs:platform:targetUserIsU13:completionHandler:]
+ -[CTCategories categoryForBundleID:platform:targetUserIsU13:completionHandler:]
+ GCC_except_table100
+ GCC_except_table117
+ GCC_except_table29
+ GCC_except_table35
+ GCC_except_table40
+ GCC_except_table44
+ GCC_except_table46
+ GCC_except_table48
+ GCC_except_table49
+ GCC_except_table50
+ GCC_except_table67
+ GCC_except_table68
+ GCC_except_table85
+ OBJC_IVAR_$_CTAppStoreCategories._contentDescriptors
+ __82-[CTCategories categoriesForBundleIDs:platform:targetUserIsU13:completionHandler:]_block_invoke
+ __96+[CTCategory _bundleCategoriesLookupResultsForBundleIdentifiers:platform:withCompletionHandler:]_block_invoke
+ __98+[CTCategory categoryForBundleIdentifiers:platform:version:targetUserIsU13:withCompletionHandler:]_block_invoke
+ ___79-[CTCategories categoryForBundleID:platform:targetUserIsU13:completionHandler:]_block_invoke
+ ___81+[CTCategory categoryForBundleID:platform:targetUserIsU13:withCompletionHandler:]_block_invoke
+ ___82-[CTCategories categoriesForBundleIDs:platform:targetUserIsU13:completionHandler:]_block_invoke
+ ___82-[CTCategories categoriesForBundleIDs:platform:targetUserIsU13:completionHandler:]_block_invoke_2
+ ___96+[CTCategory _bundleCategoriesLookupResultsForBundleIdentifiers:platform:withCompletionHandler:]_block_invoke
+ ___98+[CTCategory categoryForBundleIdentifiers:platform:version:targetUserIsU13:withCompletionHandler:]_block_invoke
+ ___98+[CTCategory categoryForBundleIdentifiers:platform:version:targetUserIsU13:withCompletionHandler:]_block_invoke_2
+ ___block_descriptor_41_e8_32s_e37_v32?0"NSString"8"CTCategory"16^B24l
+ ___block_descriptor_49_e8_32s40s_e25_v32?0"NSString"8Q16^B24l
+ ___block_descriptor_57_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_65_e8_32s40r_e57_v32?0"NSString"8"CTBundleCategoriesLookupResult"16^B24l
+ ___block_descriptor_65_e8_32s40s48bs56r_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_73_e8_32s40bs48r_e34_v24?0"NSDictionary"8"NSError"16l
+ _objc_msgSend$_bundleCategoriesLookupResultsForBundleIdentifiers:platform:withCompletionHandler:
+ _objc_msgSend$_cacheKeyForBundleID:targetUserIsU13:
+ _objc_msgSend$categoriesForBundleIDs:platform:targetUserIsU13:completionHandler:
+ _objc_msgSend$categoryForBundleID:platform:targetUserIsU13:completionHandler:
+ _objc_msgSend$categoryForBundleIdentifiers:platform:targetUserIsU13:withCompletionHandler:
+ _objc_msgSend$categoryForBundleIdentifiers:platform:version:targetUserIsU13:withCompletionHandler:
+ _objc_msgSend$contentDescriptors
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$initWithPrimary:secondary:contentDescriptors:
+ _objc_msgSend$resolvedIdentifierForVersion:appStoreCategories:ckIdentifier:systemOverride:targetUserIsU13:
- +[CTCategoryResolver resolvedIdentifierForVersion:appStoreCategories:ckIdentifier:systemOverride:]
- GCC_except_table112
- GCC_except_table23
- GCC_except_table28
- GCC_except_table30
- GCC_except_table37
- GCC_except_table38
- GCC_except_table39
- GCC_except_table43
- GCC_except_table47
- GCC_except_table57
- GCC_except_table63
- GCC_except_table80
- GCC_except_table95
- _CTErrorKeyHTTPResponse
- _CTErrorKeyHTTPResponseData
- __66-[CTCategories categoriesForBundleIDs:platform:completionHandler:]_block_invoke
- __82+[CTCategory categoryForBundleIdentifiers:platform:version:withCompletionHandler:]_block_invoke
- ___63-[CTCategories categoryForBundleID:platform:completionHandler:]_block_invoke
- ___66-[CTCategories categoriesForBundleIDs:platform:completionHandler:]_block_invoke
- ___66-[CTCategories categoriesForBundleIDs:platform:completionHandler:]_block_invoke_2
- ___82+[CTCategory categoryForBundleIdentifiers:platform:version:withCompletionHandler:]_block_invoke
- ___82+[CTCategory categoryForBundleIdentifiers:platform:version:withCompletionHandler:]_block_invoke_2
- ___block_descriptor_56_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16l
- ___block_descriptor_64_e8_32s40r_e57_v32?0"NSString"8"CTBundleCategoriesLookupResult"16^B24l
- ___block_descriptor_72_e8_32s40bs48r_e34_v24?0"NSDictionary"8"NSError"16l
- _objc_msgSend$resolvedIdentifierForVersion:appStoreCategories:ckIdentifier:systemOverride:
CStrings:
+ "%@|u13=%d"
+ "com.apple.CompanionSetup"
+ "com.apple.LocalAuthenticationUIService"
+ "contentDescriptors"
+ "ios://com.apple.musicrecognition"
+ "macos://com.apple.musicrecognition.mac"
+ "watchos://com.apple.nanomusicrecognition"
- "HTTPResponse"
- "HTTPResponseData"
```
