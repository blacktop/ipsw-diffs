## CommerceKit

> `/System/Library/PrivateFrameworks/CommerceKit.framework/Versions/A/CommerceKit`

```diff

-715.2.3.0.0
-  __TEXT.__text: 0x3e53c
+715.4.5.0.0
+  __TEXT.__text: 0x3be60
   __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_methlist: 0x38c0
-  __TEXT.__cstring: 0x4cb0
+  __TEXT.__objc_methlist: 0x3fc0
+  __TEXT.__cstring: 0x4d2d
   __TEXT.__const: 0x2960
-  __TEXT.__gcc_except_tab: 0x1110
+  __TEXT.__gcc_except_tab: 0xfe0
   __TEXT.__oslogstring: 0x87b
-  __TEXT.__unwind_info: 0x1148
+  __TEXT.__unwind_info: 0x1018
   __TEXT.__objc_classname: 0x770
-  __TEXT.__objc_methname: 0xa1e1
+  __TEXT.__objc_methname: 0x9fbc
   __TEXT.__objc_methtype: 0x17e6
-  __TEXT.__objc_stubs: 0x7620
-  __DATA_CONST.__got: 0x548
+  __TEXT.__objc_stubs: 0x73c0
+  __DATA_CONST.__got: 0x530
   __DATA_CONST.__const: 0x740
   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2950
+  __DATA_CONST.__objc_selrefs: 0x2a00
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1a0
+  __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0xb0
   __AUTH_CONST.__auth_got: 0x290
-  __AUTH_CONST.__const: 0x1950
-  __AUTH_CONST.__cfstring: 0x65c0
-  __AUTH_CONST.__objc_const: 0xa958
+  __AUTH_CONST.__const: 0x1700
+  __AUTH_CONST.__cfstring: 0x6560
+  __AUTH_CONST.__objc_const: 0x9cd8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x118
   __DATA.__objc_ivar: 0x42c
   __DATA.__data: 0xa50
-  __DATA.__bss: 0x140
+  __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0x14a0
   __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /System/Library/PrivateFrameworks/StoreFoundation.framework/Versions/A/StoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 09FBD13D-73E6-3069-969C-407FA5F2BDF0
-  Functions: 1438
-  Symbols:   4125
-  CStrings:  3884
+  UUID: 1DAB49A0-E8BF-3A49-8101-EC85B9CB19A8
+  Functions: 1411
+  Symbols:   4059
+  CStrings:  3862
 
Symbols:
+ +[CKAnalytics sharedInstance].cold.1
+ +[CKAppStoreLauncher sharedInstance].cold.1
+ +[CKAssetDownloadQueue downloadQueueWithIdentifier:].cold.1
+ +[CKBookLibrary hasSampleWithItemIdentifier:returningMetadata:].cold.1
+ +[CKDialogController sharedDialogController].cold.1
+ +[CKDownloadQueue sharedDownloadQueue].cold.1
+ +[CKMachineAuthorization sharedMachineAuthorization].cold.1
+ +[CKPurchaseController sharedPurchaseController].cold.1
+ +[CKPurchaseQueue purchaseQueueForIdentifier:].cold.1
+ +[CKStoreClient _serviceProxy].cold.1
+ +[CKStoreClient configureClientAsType:].cold.1
+ +[CKStoreDAAPLibrary daapLibraryWithStoreClient:].cold.1
+ +[CKStoreRequest _macOSBuildString].cold.1
+ +[CKStoreRequest _macOSVersionString].cold.1
+ +[CKStoreRequest _webKitVersionString].cold.1
+ +[CKUpdateController sharedUpdateController].cold.1
+ +[ServiceProxy _commerceConnection].cold.2
+ +[ServiceProxy commerceClient].cold.1
+ -[SSURLRequestProperties encodeWithCoder:].cold.1
+ -[SSURLRequestProperties initWithCoder:].cold.1
+ CKLogObject.cold.1
+ _touchIDClients.cold.1
- GCC_except_table16
- GCC_except_table34
- GCC_except_table37
- GCC_except_table43
- GCC_except_table59
- GCC_except_table62
- _OBJC_CLASS_$_NSCache
- _OBJC_CLASS_$_NSImage
- __43-[CKSoftwareMap addProductsObserver:queue:]_block_invoke.64
- ___110-[CKSoftwareMap updateRequestBodyData:includeInstalledApps:includeBundledApps:conditionally:hadUnadoptedApps:]_block_invoke
- ___110-[CKSoftwareMap updateRequestBodyData:includeInstalledApps:includeBundledApps:conditionally:hadUnadoptedApps:]_block_invoke_2
- ___23-[CKSoftwareMap adopt:]_block_invoke
- ___23-[CKSoftwareMap adopt:]_block_invoke_2
- ___28-[CKSoftwareMap allProducts]_block_invoke
- ___28-[CKSoftwareMap allProducts]_block_invoke_2
- ___32-[CKSoftwareMap productForPath:]_block_invoke
- ___32-[CKSoftwareMap productForPath:]_block_invoke_2
- ___34+[CKSoftwareMap sharedSoftwareMap]_block_invoke
- ___41-[CKSoftwareMap connectionWasInterrupted]_block_invoke
- ___41-[CKSoftwareMap connectionWasInterrupted]_block_invoke_2
- ___41-[CKSoftwareMap connectionWasInterrupted]_block_invoke_3
- ___41-[CKSoftwareMap receiptFromBundleAtPath:]_block_invoke
- ___41-[CKSoftwareMap receiptFromBundleAtPath:]_block_invoke_2
- ___42-[CKSoftwareMap productForItemIdentifier:]_block_invoke
- ___42-[CKSoftwareMap productForItemIdentifier:]_block_invoke_2
- ___43-[CKSoftwareMap addProductsObserver:queue:]_block_invoke
- ___43-[CKSoftwareMap addProductsObserver:queue:]_block_invoke_2
- ___43-[CKSoftwareMap adoptableBundleIdentifiers]_block_invoke
- ___43-[CKSoftwareMap adoptableBundleIdentifiers]_block_invoke_2
- ___44-[CKSoftwareMap bundleInfoFromBundleAtPath:]_block_invoke
- ___44-[CKSoftwareMap bundleInfoFromBundleAtPath:]_block_invoke_2
- ___44-[CKSoftwareMap productForBundleIdentifier:]_block_invoke
- ___44-[CKSoftwareMap productForBundleIdentifier:]_block_invoke_2
- ___47-[CKSoftwareMap iconForApplicationWithBundeID:]_block_invoke
- ___47-[CKSoftwareMap iconForApplicationWithBundeID:]_block_invoke_2
- ___47-[CKSoftwareMap iconForApplicationWithBundeID:]_block_invoke_3
- ___50-[CKSoftwareMap isTrialVersionOfBundleIdentifier:]_block_invoke
- ___50-[CKSoftwareMap isTrialVersionOfBundleIdentifier:]_block_invoke_2
- ___67-[CKSoftwareMap adoptionCompletedForBundleID:adoptingDSID:appleID:]_block_invoke
- ___67-[CKSoftwareMap adoptionCompletedForBundleID:adoptingDSID:appleID:]_block_invoke_2
- ___block_descriptor_40_e8_32s_e18_v16?0"NSString"8l
- ___block_descriptor_40_e8_32s_e62_v24?0"<ISAssetService>"8"NSObject<OS_dispatch_semaphore>"16l
- ___block_descriptor_40_e8_32w_e30_v24?0"CKSoftwareProduct"8q16l
- ___block_descriptor_48_e8_32s40r_e16_v16?0"NSData"8l
- ___block_descriptor_48_e8_32s40r_e27_v16?0"CKSoftwareProduct"8l
- ___block_descriptor_48_e8_32s40r_e27_v16?0"ISPurchaseReceipt"8l
- ___block_descriptor_48_e8_32s40r_e37_v28?0B8"NSDictionary"12"NSError"20l
- ___block_descriptor_48_e8_32s40r_e62_v24?0"<ISAssetService>"8"NSObject<OS_dispatch_semaphore>"16l
- ___block_descriptor_56_e8_32s40s48r_e62_v24?0"<ISAssetService>"8"NSObject<OS_dispatch_semaphore>"16l
- ___block_descriptor_59_e8_32r40r48r_e62_v24?0"<ISAssetService>"8"NSObject<OS_dispatch_semaphore>"16l
- ___block_descriptor_64_e8_32s40r48r56r_e22_v24?0"NSData"8B16B20l
- ___copy_helper_block_e8_32r40r48r
- ___copy_helper_block_e8_32s40r48r56r
- ___destroy_helper_block_e8_32r40r48r
- ___destroy_helper_block_e8_32s40r48r56r
- __block_literal_global.86
- _objc_msgSend$addSoftwareMapObserver:reply:
- _objc_msgSend$adoptBundleIDsWithInfo:replyBlock:
- _objc_msgSend$adoptableBundleIdentifiersWithReplyBlock:
- _objc_msgSend$adoptionCompletedForBundleIDWithInfo:replyBlock:
- _objc_msgSend$allProductsWithReplyBlock:
- _objc_msgSend$bundleInfoFromBundleAtPath:replyBlock:
- _objc_msgSend$createSoftwareProductForAppAtPath:replyBlock:
- _objc_msgSend$httpPostBodyWithInstalledApps:bundledApps:conditionally:replyBlock:
- _objc_msgSend$iconForApplicationWithBundeID:replyBlock:
- _objc_msgSend$initWithData:
- _objc_msgSend$isTrialVersionOfBundleIdentifier:replyBlock:
- _objc_msgSend$productForBundleIdentifier:replyBlock:
- _objc_msgSend$productForItemIdentifier:replyBlock:
- _objc_msgSend$productsObservers
- _objc_msgSend$receiptFromBundleAtPath:replyBlock:
- _objc_msgSend$setBlock:
- _objc_msgSend$setQueue:
- _objc_msgSend$softwareProduct:updatedState:
- _objc_msgSend$startAdoptionEligibilityCheckWithReplyBlock:
- iconForApplicationWithBundeID:.imageCache
- iconForApplicationWithBundeID:.onceToken
- sharedSoftwareMap.onceToken
- sharedSoftwareMap.sMap
CStrings:
+ "%@: CKSoftwareMap no longer functional"
+ "+[CKSoftwareMap sharedSoftwareMap]"
+ "-[CKSoftwareMap initWithStoreClient:]"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/CKPurchaseController.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/CKUpdateController.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/_CKDAAPParser.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/Store Services Framework/CKClientDispatch.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/iTunes Store Framework/CKSoftwareMap.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/CKPurchaseController.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/CKUpdateController.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/_CKDAAPParser.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/CommerceKit/iTunes Protocol/Store Services Framework/CKClientDispatch.m"
- "addSoftwareMapObserver:reply:"
- "adoptBundleIDsWithInfo:replyBlock:"
- "adoptableBundleIdentifiersWithReplyBlock:"
- "adoptionCompleted"
- "adoptionCompletedForBundleIDWithInfo:replyBlock:"
- "allProductsWithReplyBlock:"
- "bundleIDs"
- "bundleInfoFromBundleAtPath:replyBlock:"
- "com.apple."
- "createSoftwareProductForAppAtPath:replyBlock:"
- "dsid"
- "httpPostBodyWithInstalledApps:bundledApps:conditionally:replyBlock:"
- "iconForApplicationWithBundeID:replyBlock:"
- "initWithData:"
- "isTrialVersionOfBundleIdentifier:replyBlock:"
- "productForBundleIdentifier:replyBlock:"
- "productForItemIdentifier:replyBlock:"
- "receiptFromBundleAtPath:replyBlock:"
- "v16@?0@\"CKSoftwareProduct\"8"
- "v16@?0@\"ISPurchaseReceipt\"8"
- "v16@?0@\"NSData\"8"
- "v24@?0@\"CKSoftwareProduct\"8q16"
- "v24@?0@\"NSData\"8B16B20"

```
