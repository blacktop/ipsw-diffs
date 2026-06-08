## ASOctaneSupport

> `/System/Library/PrivateFrameworks/ASOctaneSupport.framework/ASOctaneSupport`

```diff

-815.5.6.0.0
-  __TEXT.__text: 0x335c
-  __TEXT.__auth_stubs: 0x1a0
+816.0.30.2.1
+  __TEXT.__text: 0x2e24
   __TEXT.__objc_methlist: 0x46c
   __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x2b4
-  __TEXT.__cstring: 0x136
+  __TEXT.__gcc_except_tab: 0x2a4
+  __TEXT.__cstring: 0x138
   __TEXT.__unwind_info: 0x270
-  __TEXT.__objc_classname: 0x3c
-  __TEXT.__objc_methname: 0xd9f
-  __TEXT.__objc_methtype: 0x67c
-  __TEXT.__objc_stubs: 0x540
-  __DATA_CONST.__got: 0x48
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1d8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_selrefs: 0x2f8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xe0
+  __DATA_CONST.__got: 0x48
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x2b8
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 26D1CC59-D196-303E-A3C9-87A92C02FD6B
+  UUID: 1712AE70-8289-32DF-87DE-C8D2EFB5CEB1
   Functions: 78
-  Symbols:   303
-  CStrings:  188
+  Symbols:   311
+  CStrings:  17
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x23
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
Functions:
~ +[ASOctaneServer shared] : 84 -> 68
~ -[ASOctaneServer init] : 448 -> 436
~ -[ASOctaneServer activePort] : 212 -> 208
~ -[ASOctaneServer appRemovedWithBundleID:] : 112 -> 108
~ -[ASOctaneServer buyProductWithID:bundleID:] : 360 -> 348
~ ___44-[ASOctaneServer buyProductWithID:bundleID:]_block_invoke : 72 -> 16
~ -[ASOctaneServer cancelTransactionWithIdentifier:forBundleID:] : 352 -> 336
~ ___62-[ASOctaneServer cancelTransactionWithIdentifier:forBundleID:]_block_invoke : 72 -> 16
~ -[ASOctaneServer changeAutoRenewStatus:transactionID:bundleID:] : 360 -> 352
~ ___63-[ASOctaneServer changeAutoRenewStatus:transactionID:bundleID:]_block_invoke : 72 -> 16
~ -[ASOctaneServer clearOverridesForBundleID:] : 336 -> 328
~ ___44-[ASOctaneServer clearOverridesForBundleID:]_block_invoke : 72 -> 16
~ -[ASOctaneServer completeAskToBuyRequestWithResponse:transactionID:forBundleID:] : 360 -> 352
~ ___80-[ASOctaneServer completeAskToBuyRequestWithResponse:transactionID:forBundleID:]_block_invoke : 72 -> 16
~ -[ASOctaneServer deleteAllTransactionsForBundleID:] : 336 -> 328
~ ___51-[ASOctaneServer deleteAllTransactionsForBundleID:]_block_invoke : 72 -> 16
~ -[ASOctaneServer deleteTransactionWithIdentifier:forBundleID:] : 352 -> 336
~ ___62-[ASOctaneServer deleteTransactionWithIdentifier:forBundleID:]_block_invoke : 72 -> 16
~ -[ASOctaneServer expireOrRenewSubscriptionWithIdentifier:expire:forBundleID:] : 368 -> 364
~ ___77-[ASOctaneServer expireOrRenewSubscriptionWithIdentifier:expire:forBundleID:]_block_invoke : 72 -> 16
~ ___43-[ASOctaneServer getStorefrontForBundleID:]_block_invoke : 72 -> 16
~ ___48-[ASOctaneServer getTransactionDataForBundleID:]_block_invoke : 72 -> 16
~ -[ASOctaneServer getEncodedTransactionsForBundleID:withReply:] : 284 -> 288
~ -[ASOctaneServer refundTransactionWithIdentifier:forBundleID:] : 352 -> 336
~ ___62-[ASOctaneServer refundTransactionWithIdentifier:forBundleID:]_block_invoke : 72 -> 16
~ -[ASOctaneServer resolveIssueForTransactionWithIdentifier:forBundleID:] : 352 -> 336
~ ___71-[ASOctaneServer resolveIssueForTransactionWithIdentifier:forBundleID:]_block_invoke : 72 -> 16
~ -[ASOctaneServer setStorefront:forBundleID:] : 360 -> 348
~ ___44-[ASOctaneServer setStorefront:forBundleID:]_block_invoke : 72 -> 16
~ -[ASOctaneServer useConfigurationDirectory:forBundleID:] : 216 -> 224
~ ___56-[ASOctaneServer registerForEventOfType:withFilterData:]_block_invoke : 72 -> 16
~ -[ASOctaneServer unregisterForEventWithIdentifier:] : 104 -> 100
~ ___37-[ASOctaneServer messageForBundleID:]_block_invoke : 72 -> 16
~ -[ASOctaneServer messageOfTypeForBundleID:messageReason:] : 324 -> 328
~ ___57-[ASOctaneServer messageOfTypeForBundleID:messageReason:]_block_invoke : 72 -> 16
~ ___75-[ASOctaneServer startPriceIncreaseForTransactionID:bundleID:needsConsent:]_block_invoke : 72 -> 16
~ ___92-[ASOctaneServer completePriceConsentRequestWithResponse:transactionIdentifier:forBundleID:]_block_invoke : 72 -> 16
~ -[ASOctaneServer validateSKAdNetworkSignature:withPublicKey:source:andParameters:forBundleID:] : 396 -> 412
~ -[ASOctaneServer storeKitErrorForCategory:bundleID:] : 252 -> 248
~ -[ASOctaneServer setStoreKitError:forCategory:bundleID:] : 136 -> 132
~ -[ASOctaneServer getIntegerValueForIdentifier:forBundleID:] : 256 -> 252
~ -[ASOctaneServer getIntegerValueForIdentifier:forBundleID:completion:] : 292 -> 296
~ -[ASOctaneServer setIntegerValue:forIdentifier:forBundleID:] : 360 -> 352
~ ___60-[ASOctaneServer setIntegerValue:forIdentifier:forBundleID:]_block_invoke : 72 -> 16
~ ___58-[ASOctaneServer getStringValueForIdentifier:forBundleID:]_block_invoke : 72 -> 16
~ -[ASOctaneServer setStringValue:forIdentifier:forBundleID:] : 368 -> 364
~ ___59-[ASOctaneServer setStringValue:forIdentifier:forBundleID:]_block_invoke : 72 -> 16
~ -[ASOctaneServer _synchronousRemoteObjectProxy:] : 284 -> 280
~ -[ASOctaneServer _remoteObjectProxyWithErrorHandler:] : 184 -> 180
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8^@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8Q16@24"
- "@32@0:8q16@24"
- "@36@0:8@16B24@28"
- "@36@0:8B16Q20@28"
- "@36@0:8Q16@24B32"
- "@40@0:8:16@24@32"
- "@40@0:8@16Q24@32"
- "@40@0:8q16Q24@32"
- "@56@0:8@16@24q32@40@48"
- "ASOctaneServer"
- "ASOctaneSupportXPCServiceProtocol"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_connectionToService"
- "_remoteObjectProxyWithErrorHandler:"
- "_synchronousRemoteObjectProxy:"
- "activePort"
- "appRemovedWithBundleID:"
- "appRemovedWithBundleID:withReply:"
- "autorelease"
- "buyProductWithConfiguration:withReply:"
- "buyProductWithID:bundleID:"
- "buyProductWithID:bundleID:withReply:"
- "cancelTransactionWithIdentifier:forBundleID:"
- "cancelTransactionWithIdentifier:forBundleID:withReply:"
- "changeAutoRenewStatus:transactionID:bundleID:"
- "changeAutoRenewStatus:transactionID:bundleID:withReply:"
- "class"
- "clearOverridesForBundleID:"
- "clearOverridesForBundleID:withReply:"
- "completeAskToBuyRequestWithResponse:transactionID:forBundleID:"
- "completeAskToBuyRequestWithResponse:transactionIdentifier:forBundleID:withReply:"
- "completePriceConsentRequestWithResponse:transactionIdentifier:forBundleID:"
- "completePriceConsentRequestWithResponse:transactionIdentifier:forBundleID:withReply:"
- "conformsToProtocol:"
- "debugDescription"
- "deleteAllTransactionsForBundleID:"
- "deleteAllTransactionsForBundleID:withRelpy:"
- "deleteTransactionWithIdentifier:forBundleID:"
- "deleteTransactionWithIdentifier:forBundleID:withReply:"
- "description"
- "expireOrRenewSubscriptionWithIdentifier:expire:forBundleID:"
- "expireOrRenewSubscriptionWithIdentifier:expire:forBundleID:withReply:"
- "generateSKANPostbackSignature:"
- "generateSKANPostbackSignature:withReply:"
- "getEncodedTransactionsForBundleID:withReply:"
- "getIntegerValueForIdentifier:forBundleID:"
- "getIntegerValueForIdentifier:forBundleID:completion:"
- "getIntegerValueForIdentifier:forBundleID:withReply:"
- "getPortWithReply:"
- "getStorefrontForBundleID:"
- "getStorefrontForBundleID:withReply:"
- "getStringValueForIdentifier:forBundleID:"
- "getStringValueForIdentifier:forBundleID:withReply:"
- "getTransactionDataForBundleID:"
- "getTransactionDataForBundleID:withReply:"
- "hash"
- "init"
- "initWithServiceName:"
- "interfaceWithProtocol:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "messageForBundleID:"
- "messageForBundleID:withReply:"
- "messageOfTypeForBundleID:messageReason:"
- "messageOfTypeForBundleID:messageReason:withReply:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "q16@0:8"
- "q32@0:8Q16@24"
- "q32@0:8q16@24"
- "refundTransactionWithIdentifier:forBundleID:"
- "refundTransactionWithIdentifier:forBundleID:withReply:"
- "registerForEventOfType:filterData:withReply:"
- "registerForEventOfType:withFilterData:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "resolveIssueForTransactionWithIdentifier:forBundleID:"
- "resolveIssueForTransactionWithIdentifier:forBundleID:withReply:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setIntegerValue:forIdentifier:forBundleID:"
- "setIntegerValue:forIdentifier:forBundleID:withReply:"
- "setRemoteObjectInterface:"
- "setStoreKitError:forCategory:bundleID:"
- "setStoreKitError:forCategory:bundleID:withReply:"
- "setStorefront:forBundleID:"
- "setStorefront:forBundleID:withReply:"
- "setStringValue:forIdentifier:forBundleID:"
- "setStringValue:forIdentifier:forBundleID:withReply:"
- "setWithObjects:"
- "shared"
- "startPriceIncreaseForTransactionID:bundleID:needsConsent:"
- "startPriceIncreaseForTransactionID:bundleID:needsConsent:withReply:"
- "startServingConfiguration:forBundleID:withReply:"
- "storeKitErrorForCategory:bundleID:"
- "storeKitErrorForCategory:bundleID:withReply:"
- "superclass"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "unregisterForEventWithIdentifier:"
- "useConfigurationDirectory:forBundleID:"
- "v16@0:8"
- "v24@0:8@\"NSUUID\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?q>16"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSError\"@\"NSString\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSString\">24"
- "v32@0:8@\"NSString\"16@?<v@?>24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSData\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@\"NSString\"16@\"NSNumber\"24@?<v@?@\"NSDictionary\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8Q16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8Q16@\"NSString\"24@?<v@?@\"NSString\">32"
- "v40@0:8Q16@\"NSString\"24@?<v@?q>32"
- "v40@0:8Q16@24@?32"
- "v40@0:8q16@\"NSData\"24@?<v@?@\"NSUUID\">32"
- "v40@0:8q16@\"NSString\"24@?<v@?q>32"
- "v40@0:8q16@24@?32"
- "v40@0:8q16q24@32"
- "v44@0:8@\"NSString\"16B24@\"NSString\"28@?<v@?@\"NSError\">36"
- "v44@0:8@16B24@28@?36"
- "v44@0:8B16Q20@\"NSString\"28@?<v@?@\"NSError\">36"
- "v44@0:8B16Q20@28@?36"
- "v44@0:8Q16@\"NSString\"24B32@?<v@?@\"NSError\">36"
- "v44@0:8Q16@24B32@?36"
- "v48@0:8@\"NSString\"16Q24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v48@0:8@16Q24@32@?40"
- "v48@0:8q16Q24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v48@0:8q16Q24@32@?40"
- "v48@0:8q16q24@\"NSString\"32@?<v@?>40"
- "v48@0:8q16q24@32@?40"
- "v64@0:8@\"NSString\"16@\"NSString\"24q32@\"NSDictionary\"40@\"NSString\"48@?<v@?@\"NSError\">56"
- "v64@0:8@16@24q32@40@48@?56"
- "validateSKAdNetworkSignature:withPublicKey:source:andParameters:forBundleID:"
- "validateSKAdNetworkSignature:withPublicKey:source:andParameters:forBundleID:withReply:"
- "zone"

```
