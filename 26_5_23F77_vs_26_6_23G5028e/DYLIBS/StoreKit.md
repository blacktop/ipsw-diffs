## StoreKit

> `/System/Library/Frameworks/StoreKit.framework/StoreKit`

```diff

-815.5.6.0.0
-  __TEXT.__text: 0x1cceb0
-  __TEXT.__auth_stubs: 0x31e0
-  __TEXT.__objc_methlist: 0x5c44
+815.6.2.0.0
+  __TEXT.__text: 0x1ce750
+  __TEXT.__auth_stubs: 0x31f0
+  __TEXT.__objc_methlist: 0x5db4
   __TEXT.__gcc_except_tab: 0x1038
-  __TEXT.__const: 0x16be4
-  __TEXT.__cstring: 0x7cb1
+  __TEXT.__const: 0x16bc4
+  __TEXT.__cstring: 0x7ce1
   __TEXT.__oslogstring: 0x3140
   __TEXT.__dlopen_cstrs: 0x498
   __TEXT.__constg_swiftt: 0x42a8
   __TEXT.__swift5_typeref: 0x583c
   __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_reflstr: 0x37a4
+  __TEXT.__swift5_reflstr: 0x3784
   __TEXT.__swift5_fieldmd: 0x5234
   __TEXT.__swift5_assocty: 0xad8
   __TEXT.__swift5_proto: 0x1424

   __TEXT.__swift_as_ret: 0x66c
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x2c
-  __TEXT.__unwind_info: 0x8b18
+  __TEXT.__unwind_info: 0x8b68
   __TEXT.__eh_frame: 0xfa3c
-  __TEXT.__objc_classname: 0x1aa7
-  __TEXT.__objc_methname: 0xd587
-  __TEXT.__objc_methtype: 0x33e4
-  __TEXT.__objc_stubs: 0x9420
+  __TEXT.__objc_classname: 0x1ab7
+  __TEXT.__objc_methname: 0xd797
+  __TEXT.__objc_methtype: 0x33f4
+  __TEXT.__objc_stubs: 0x9620
   __DATA_CONST.__got: 0xb90
-  __DATA_CONST.__const: 0x18b0
-  __DATA_CONST.__objc_classlist: 0x3f8
+  __DATA_CONST.__const: 0x18c8
+  __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x380
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3158
+  __DATA_CONST.__objc_selrefs: 0x31d0
   __DATA_CONST.__objc_protorefs: 0x1c0
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x1900
+  __AUTH_CONST.__auth_got: 0x1908
   __AUTH_CONST.__const: 0x11b68
-  __AUTH_CONST.__cfstring: 0x3780
-  __AUTH_CONST.__objc_const: 0x16440
+  __AUTH_CONST.__cfstring: 0x3800
+  __AUTH_CONST.__objc_const: 0x167e8
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x2728
+  __AUTH.__objc_data: 0x2778
   __AUTH.__data: 0x3068
-  __DATA.__objc_ivar: 0x5a0
-  __DATA.__data: 0x6dc0
+  __DATA.__objc_ivar: 0x5d0
+  __DATA.__data: 0x6dd0
   __DATA.__bss: 0x25a30
   __DATA.__common: 0xc0
   __DATA_DIRTY.__objc_data: 0x370

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 036B745B-5D9C-3CA0-BAFA-CE4A9851CF77
-  Functions: 14442
-  Symbols:   19122
-  CStrings:  4500
+  UUID: 2897C2E9-57A9-369A-B98E-E295B2248AF9
+  Functions: 14477
+  Symbols:   19229
+  CStrings:  4538
 
Symbols:
+ -[SKPaymentQueue _logPurchaseResult:primaryError:mappedError:inAppPurchaseID:]
+ -[SKPaymentQueue _logPurchaseStartForProduct:]
+ -[SKPurchaseEvent .cxx_destruct]
+ -[SKPurchaseEvent canCreatePayload]
+ -[SKPurchaseEvent context]
+ -[SKPurchaseEvent createPayload]
+ -[SKPurchaseEvent environment]
+ -[SKPurchaseEvent eventName]
+ -[SKPurchaseEvent inAppPurchaseID]
+ -[SKPurchaseEvent mappedErrorDescription]
+ -[SKPurchaseEvent mappedErrorType]
+ -[SKPurchaseEvent mappedError]
+ -[SKPurchaseEvent phase]
+ -[SKPurchaseEvent primaryError]
+ -[SKPurchaseEvent purchaseResult]
+ -[SKPurchaseEvent serverCorrelationID]
+ -[SKPurchaseEvent setContext:]
+ -[SKPurchaseEvent setEnvironment:]
+ -[SKPurchaseEvent setInAppPurchaseID:]
+ -[SKPurchaseEvent setMappedError:]
+ -[SKPurchaseEvent setMappedErrorDescription:]
+ -[SKPurchaseEvent setMappedErrorType:]
+ -[SKPurchaseEvent setPhase:]
+ -[SKPurchaseEvent setPrimaryError:]
+ -[SKPurchaseEvent setPurchaseResult:]
+ -[SKPurchaseEvent setServerCorrelationID:]
+ -[SKPurchaseEvent setStoreKitAPI:]
+ -[SKPurchaseEvent setStorefront:]
+ -[SKPurchaseEvent storeKitAPI]
+ -[SKPurchaseEvent storefront]
+ GCC_except_table95
+ _OBJC_CLASS_$_SKPurchaseEvent
+ _OBJC_IVAR_$_SKPurchaseEvent._context
+ _OBJC_IVAR_$_SKPurchaseEvent._environment
+ _OBJC_IVAR_$_SKPurchaseEvent._inAppPurchaseID
+ _OBJC_IVAR_$_SKPurchaseEvent._mappedError
+ _OBJC_IVAR_$_SKPurchaseEvent._mappedErrorDescription
+ _OBJC_IVAR_$_SKPurchaseEvent._mappedErrorType
+ _OBJC_IVAR_$_SKPurchaseEvent._phase
+ _OBJC_IVAR_$_SKPurchaseEvent._primaryError
+ _OBJC_IVAR_$_SKPurchaseEvent._purchaseResult
+ _OBJC_IVAR_$_SKPurchaseEvent._serverCorrelationID
+ _OBJC_IVAR_$_SKPurchaseEvent._storeKitAPI
+ _OBJC_IVAR_$_SKPurchaseEvent._storefront
+ _OBJC_METACLASS_$_SKPurchaseEvent
+ __OBJC_$_INSTANCE_METHODS_SKPurchaseEvent
+ __OBJC_$_INSTANCE_VARIABLES_SKPurchaseEvent
+ __OBJC_$_PROP_LIST_SKPurchaseEvent
+ __OBJC_CLASS_PROTOCOLS_$_SKPurchaseEvent
+ __OBJC_CLASS_RO_$_SKPurchaseEvent
+ __OBJC_METACLASS_RO_$_SKPurchaseEvent
+ ___50-[SKPaymentQueue(Package) checkServerQueueForced:]_block_invoke.166
+ _kCoreAnalyticsKeyPhase
+ _kCoreAnalyticsKeyPurchaseResult
+ _kCoreAnalyticsKeyStoreKitAPI
+ _objc_msgSend$_logPurchaseResult:primaryError:mappedError:inAppPurchaseID:
+ _objc_msgSend$_logPurchaseStartForProduct:
+ _objc_msgSend$context
+ _objc_msgSend$environment
+ _objc_msgSend$mappedErrorDescription
+ _objc_msgSend$mappedErrorType
+ _objc_msgSend$phase
+ _objc_msgSend$purchaseResult
+ _objc_msgSend$serverCorrelationID
+ _objc_msgSend$setContext:
+ _objc_msgSend$setMappedErrorDescription:
+ _objc_msgSend$setMappedErrorType:
+ _objc_msgSend$setPhase:
+ _objc_msgSend$setPurchaseResult:
+ _objc_msgSend$setStoreKitAPI:
+ _objc_msgSend$storeKitAPI
+ _objc_retain_x9
- GCC_except_table91
- ___50-[SKPaymentQueue(Package) checkServerQueueForced:]_block_invoke.162
CStrings:
+ "03:43:57"
+ "H"
+ "May 15 2026"
+ "SKPurchaseEvent"
+ "T@\"NSString\",&,N,V_mappedErrorDescription"
+ "T@\"NSString\",&,N,V_mappedErrorType"
+ "T@\"NSString\",&,N,V_storefront"
+ "Tq,N,V_context"
+ "Tq,N,V_phase"
+ "Tq,N,V_purchaseResult"
+ "Tq,N,V_storeKitAPI"
+ "_context"
+ "_logPurchaseResult:primaryError:mappedError:inAppPurchaseID:"
+ "_logPurchaseStartForProduct:"
+ "_mappedErrorDescription"
+ "_mappedErrorType"
+ "_phase"
+ "_purchaseResult"
+ "_storeKitAPI"
+ "com.apple.storekit.purchase"
+ "mappedErrorDescription"
+ "phase"
+ "purchaseResult"
+ "setContext:"
+ "setMappedErrorDescription:"
+ "setMappedErrorType:"
+ "setPhase:"
+ "setPurchaseResult:"
+ "setStoreKitAPI:"
+ "setStorefront:"
+ "storeKitAPI"
+ "v48@0:8q16@24@32@40"
- "21:43:34"
- "Apr 18 2026"

```
