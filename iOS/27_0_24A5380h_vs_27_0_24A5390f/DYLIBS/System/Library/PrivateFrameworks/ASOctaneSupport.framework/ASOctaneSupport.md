## ASOctaneSupport

> `/System/Library/PrivateFrameworks/ASOctaneSupport.framework/ASOctaneSupport`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-816.0.38.0.0
-  __TEXT.__text: 0x2e24
-  __TEXT.__objc_methlist: 0x46c
-  __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x2a4
-  __TEXT.__cstring: 0x138
-  __TEXT.__unwind_info: 0x270
+816.0.41.0.0
+  __TEXT.__text: 0xb20
+  __TEXT.__objc_methlist: 0x1dc
+  __TEXT.__const: 0x10
+  __TEXT.__gcc_except_tab: 0x74
+  __TEXT.__cstring: 0xd8
+  __TEXT.__unwind_info: 0xd0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1d8
+  __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f8
+  __DATA_CONST.__objc_selrefs: 0x140
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__got: 0x48
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0xa0
-  __AUTH_CONST.__objc_const: 0x2b8
+  __DATA_CONST.__got: 0x20
+  __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__cfstring: 0x80
+  __AUTH_CONST.__objc_const: 0x1e0
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0xc0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 78
-  Symbols:   231
-  CStrings:  12
+  Functions: 22
+  Symbols:   109
+  CStrings:  8
 
Symbols:
+ GCC_except_table10
+ GCC_except_table12
+ GCC_except_table14
+ GCC_except_table16
- -[ASOctaneServer activePort]
- -[ASOctaneServer appRemovedWithBundleID:]
- -[ASOctaneServer buyProductWithConfiguration:withReply:]
- -[ASOctaneServer buyProductWithID:bundleID:]
- -[ASOctaneServer cancelTransactionWithIdentifier:forBundleID:]
- -[ASOctaneServer changeAutoRenewStatus:transactionID:bundleID:]
- -[ASOctaneServer clearOverridesForBundleID:]
- -[ASOctaneServer completeAskToBuyRequestWithResponse:transactionID:forBundleID:]
- -[ASOctaneServer completePriceConsentRequestWithResponse:transactionIdentifier:forBundleID:]
- -[ASOctaneServer deleteTransactionWithIdentifier:forBundleID:]
- -[ASOctaneServer expireOrRenewSubscriptionWithIdentifier:expire:forBundleID:]
- -[ASOctaneServer getIntegerValueForIdentifier:forBundleID:]
- -[ASOctaneServer getIntegerValueForIdentifier:forBundleID:completion:]
- -[ASOctaneServer getStorefrontForBundleID:]
- -[ASOctaneServer getTransactionDataForBundleID:]
- -[ASOctaneServer messageForBundleID:]
- -[ASOctaneServer messageOfTypeForBundleID:messageReason:]
- -[ASOctaneServer refundTransactionWithIdentifier:forBundleID:]
- -[ASOctaneServer registerForEventOfType:withFilterData:]
- -[ASOctaneServer resolveIssueForTransactionWithIdentifier:forBundleID:]
- -[ASOctaneServer setIntegerValue:forIdentifier:forBundleID:]
- -[ASOctaneServer setStoreKitError:forCategory:bundleID:]
- -[ASOctaneServer setStorefront:forBundleID:]
- -[ASOctaneServer setStringValue:forIdentifier:forBundleID:]
- -[ASOctaneServer startPriceIncreaseForTransactionID:bundleID:needsConsent:]
- -[ASOctaneServer storeKitErrorForCategory:bundleID:]
- -[ASOctaneServer unregisterForEventWithIdentifier:]
- -[ASOctaneServer useConfigurationDirectory:forBundleID:]
- GCC_except_table13
- GCC_except_table15
- GCC_except_table17
- GCC_except_table19
- GCC_except_table21
- GCC_except_table23
- GCC_except_table25
- GCC_except_table27
- GCC_except_table29
- GCC_except_table34
- GCC_except_table36
- GCC_except_table38
- GCC_except_table42
- GCC_except_table45
- GCC_except_table47
- GCC_except_table49
- GCC_except_table51
- GCC_except_table53
- GCC_except_table55
- GCC_except_table57
- GCC_except_table61
- GCC_except_table66
- GCC_except_table68
- GCC_except_table70
- GCC_except_table72
- GCC_except_table9
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSNumber
- _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_NSString
- _OBJC_CLASS_$_NSURL
- ___28-[ASOctaneServer activePort]_block_invoke
- ___37-[ASOctaneServer messageForBundleID:]_block_invoke
- ___41-[ASOctaneServer appRemovedWithBundleID:]_block_invoke
- ___43-[ASOctaneServer getStorefrontForBundleID:]_block_invoke
- ___44-[ASOctaneServer buyProductWithID:bundleID:]_block_invoke
- ___44-[ASOctaneServer clearOverridesForBundleID:]_block_invoke
- ___44-[ASOctaneServer setStorefront:forBundleID:]_block_invoke
- ___48-[ASOctaneServer getTransactionDataForBundleID:]_block_invoke
- ___52-[ASOctaneServer storeKitErrorForCategory:bundleID:]_block_invoke
- ___56-[ASOctaneServer buyProductWithConfiguration:withReply:]_block_invoke
- ___56-[ASOctaneServer registerForEventOfType:withFilterData:]_block_invoke
- ___56-[ASOctaneServer setStoreKitError:forCategory:bundleID:]_block_invoke
- ___56-[ASOctaneServer useConfigurationDirectory:forBundleID:]_block_invoke
- ___57-[ASOctaneServer messageOfTypeForBundleID:messageReason:]_block_invoke
- ___59-[ASOctaneServer getIntegerValueForIdentifier:forBundleID:]_block_invoke
- ___59-[ASOctaneServer setStringValue:forIdentifier:forBundleID:]_block_invoke
- ___60-[ASOctaneServer setIntegerValue:forIdentifier:forBundleID:]_block_invoke
- ___62-[ASOctaneServer cancelTransactionWithIdentifier:forBundleID:]_block_invoke
- ___62-[ASOctaneServer deleteTransactionWithIdentifier:forBundleID:]_block_invoke
- ___62-[ASOctaneServer refundTransactionWithIdentifier:forBundleID:]_block_invoke
- ___63-[ASOctaneServer changeAutoRenewStatus:transactionID:bundleID:]_block_invoke
- ___70-[ASOctaneServer getIntegerValueForIdentifier:forBundleID:completion:]_block_invoke
- ___70-[ASOctaneServer getIntegerValueForIdentifier:forBundleID:completion:]_block_invoke_2
- ___71-[ASOctaneServer resolveIssueForTransactionWithIdentifier:forBundleID:]_block_invoke
- ___75-[ASOctaneServer startPriceIncreaseForTransactionID:bundleID:needsConsent:]_block_invoke
- ___77-[ASOctaneServer expireOrRenewSubscriptionWithIdentifier:expire:forBundleID:]_block_invoke
- ___80-[ASOctaneServer completeAskToBuyRequestWithResponse:transactionID:forBundleID:]_block_invoke
- ___92-[ASOctaneServer completePriceConsentRequestWithResponse:transactionIdentifier:forBundleID:]_block_invoke
- ___block_descriptor_40_e8_32bs_e8_v16?0q8ls32l8
- ___block_descriptor_40_e8_32r_e16_v16?0"NSData"8lr32l8
- ___block_descriptor_40_e8_32r_e16_v16?0"NSUUID"8lr32l8
- ___block_descriptor_40_e8_32r_e22_v16?0"NSDictionary"8lr32l8
- ___block_descriptor_40_e8_32r_e8_v16?0q8lr32l8
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
- _objc_msgSend$appRemovedWithBundleID:withReply:
- _objc_msgSend$buyProductWithConfiguration:withReply:
- _objc_msgSend$buyProductWithID:bundleID:withReply:
- _objc_msgSend$cancelTransactionWithIdentifier:forBundleID:withReply:
- _objc_msgSend$changeAutoRenewStatus:transactionID:bundleID:withReply:
- _objc_msgSend$clearOverridesForBundleID:withReply:
- _objc_msgSend$completeAskToBuyRequestWithResponse:transactionIdentifier:forBundleID:withReply:
- _objc_msgSend$completePriceConsentRequestWithResponse:transactionIdentifier:forBundleID:withReply:
- _objc_msgSend$deleteTransactionWithIdentifier:forBundleID:withReply:
- _objc_msgSend$expireOrRenewSubscriptionWithIdentifier:expire:forBundleID:withReply:
- _objc_msgSend$getIntegerValueForIdentifier:forBundleID:withReply:
- _objc_msgSend$getPortWithReply:
- _objc_msgSend$getStorefrontForBundleID:withReply:
- _objc_msgSend$getTransactionDataForBundleID:withReply:
- _objc_msgSend$messageForBundleID:withReply:
- _objc_msgSend$messageOfTypeForBundleID:messageReason:withReply:
- _objc_msgSend$refundTransactionWithIdentifier:forBundleID:withReply:
- _objc_msgSend$registerForEventOfType:filterData:withReply:
- _objc_msgSend$resolveIssueForTransactionWithIdentifier:forBundleID:withReply:
- _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
- _objc_msgSend$setIntegerValue:forIdentifier:forBundleID:withReply:
- _objc_msgSend$setStoreKitError:forCategory:bundleID:withReply:
- _objc_msgSend$setStorefront:forBundleID:withReply:
- _objc_msgSend$setStringValue:forIdentifier:forBundleID:withReply:
- _objc_msgSend$setWithObjects:
- _objc_msgSend$startPriceIncreaseForTransactionID:bundleID:needsConsent:withReply:
- _objc_msgSend$startServingConfiguration:forBundleID:withReply:
- _objc_msgSend$storeKitErrorForCategory:bundleID:withReply:
- _objc_msgSend$unregisterForEventWithIdentifier:
- _objc_opt_class
- _objc_release_x22
- _objc_retain_x22
- _objc_retain_x4
CStrings:
- "Error setting configuration file %@ for %@: %@"
- "v16@?0@\"NSDictionary\"8"
- "v16@?0@\"NSUUID\"8"
- "v16@?0q8"
```
