## StoreKit

> `/System/Library/Frameworks/StoreKit.framework/StoreKit`

```diff

-  __TEXT.__text: 0x1ce750
-  __TEXT.__auth_stubs: 0x31f0
-  __TEXT.__objc_methlist: 0x5db4
+  __TEXT.__text: 0x1cfafc
+  __TEXT.__auth_stubs: 0x31e0
+  __TEXT.__objc_methlist: 0x5e24
   __TEXT.__gcc_except_tab: 0x1038
-  __TEXT.__const: 0x16bc4
-  __TEXT.__cstring: 0x7ce1
+  __TEXT.__const: 0x16cd4
+  __TEXT.__cstring: 0x7d21
   __TEXT.__oslogstring: 0x3140
   __TEXT.__dlopen_cstrs: 0x498
-  __TEXT.__constg_swiftt: 0x42a8
-  __TEXT.__swift5_typeref: 0x583c
-  __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_reflstr: 0x3784
-  __TEXT.__swift5_fieldmd: 0x5234
-  __TEXT.__swift5_assocty: 0xad8
-  __TEXT.__swift5_proto: 0x1424
-  __TEXT.__swift5_types: 0x67c
+  __TEXT.__constg_swiftt: 0x4304
+  __TEXT.__swift5_typeref: 0x584e
+  __TEXT.__swift5_builtin: 0x190
+  __TEXT.__swift5_reflstr: 0x37f4
+  __TEXT.__swift5_fieldmd: 0x528c
+  __TEXT.__swift5_assocty: 0xaf0
+  __TEXT.__swift5_proto: 0x142c
+  __TEXT.__swift5_types: 0x688
   __TEXT.__swift5_capture: 0x1b54
   __TEXT.__swift_as_entry: 0x5d0
   __TEXT.__swift_as_ret: 0x66c
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x2c
-  __TEXT.__unwind_info: 0x8b68
-  __TEXT.__eh_frame: 0xfa3c
-  __TEXT.__objc_classname: 0x1ab7
-  __TEXT.__objc_methname: 0xd797
-  __TEXT.__objc_methtype: 0x33f4
-  __TEXT.__objc_stubs: 0x9620
-  __DATA_CONST.__got: 0xb90
+  __TEXT.__unwind_info: 0x8b90
+  __TEXT.__eh_frame: 0xf9d4
+  __TEXT.__objc_classname: 0x1ad7
+  __TEXT.__objc_methname: 0xd867
+  __TEXT.__objc_methtype: 0x3414
+  __TEXT.__objc_stubs: 0x96e0
+  __DATA_CONST.__got: 0xb98
   __DATA_CONST.__const: 0x18c8
-  __DATA_CONST.__objc_classlist: 0x400
+  __DATA_CONST.__objc_classlist: 0x408
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x380
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x31d0
+  __DATA_CONST.__objc_selrefs: 0x31e8
   __DATA_CONST.__objc_protorefs: 0x1c0
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x1908
-  __AUTH_CONST.__const: 0x11b68
+  __AUTH_CONST.__auth_got: 0x1900
+  __AUTH_CONST.__const: 0x11c38
   __AUTH_CONST.__cfstring: 0x3800
-  __AUTH_CONST.__objc_const: 0x167e8
+  __AUTH_CONST.__objc_const: 0x168d0
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x2778
-  __AUTH.__data: 0x3068
+  __AUTH.__objc_data: 0x27e8
+  __AUTH.__data: 0x3088
   __DATA.__objc_ivar: 0x5d0
-  __DATA.__data: 0x6dd0
-  __DATA.__bss: 0x25a30
+  __DATA.__data: 0x6de0
+  __DATA.__bss: 0x25b30
   __DATA.__common: 0xc0
   __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__data: 0x598

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14477
-  Symbols:   19229
-  CStrings:  4538
+  Functions: 14513
+  Symbols:   19250
+  CStrings:  4546
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[SKPaymentQueue _logPurchaseResult:primaryError:mappedError:inAppPurchaseID:analyticsMetadata:]
+ _OBJC_CLASS_$_SKPurchaseAnalyticsMetadata
+ _OBJC_METACLASS_$_SKPurchaseAnalyticsMetadata
+ __CLASS_METHODS_SKPurchaseAnalyticsMetadata
+ __DATA_SKPurchaseAnalyticsMetadata
+ __INSTANCE_METHODS_SKPurchaseAnalyticsMetadata
+ __IVARS_SKPurchaseAnalyticsMetadata
+ __METACLASS_DATA_SKPurchaseAnalyticsMetadata
+ __PROPERTIES_SKPurchaseAnalyticsMetadata
+ ___48-[SKPaymentQueue _updatedTransactions:restored:]_block_invoke.97
+ ___50-[SKPaymentQueue(Package) checkServerQueueForced:]_block_invoke.167
+ ___swift_memcpy73_8
+ _objc_msgSend$_logPurchaseResult:primaryError:mappedError:inAppPurchaseID:analyticsMetadata:
+ _objc_msgSend$initWithStorefront:environment:serverCorrelationID:
+ _objc_msgSend$metadataFromError:
+ _objc_msgSend$metadataFromTransactionDictionary:
+ _objc_msgSend$setEnvironment:
+ _objc_msgSend$setServerCorrelationID:
+ _objc_msgSend$setStorefront:
+ _symbolic _____ 8StoreKit22SKPurchaseEventContextV
+ _symbolic _____ So13SKStoreKitAPIV
+ _symbolic _____ So26SKAnalyticsEnvironmentTypeV
+ _type_layout_string 8StoreKit22SKPurchaseEventContextV
- -[SKPaymentQueue _logPurchaseResult:primaryError:mappedError:inAppPurchaseID:]
- ___48-[SKPaymentQueue _updatedTransactions:restored:]_block_invoke.96
- ___50-[SKPaymentQueue(Package) checkServerQueueForced:]_block_invoke.166
- _objc_msgSend$_logPurchaseResult:primaryError:mappedError:inAppPurchaseID:
- _objc_retain_x9
CStrings:
+ "07:10:53"
+ "@40@0:8@16q24@32"
+ "Jun 17 2026"
+ "SKPurchaseAnalyticsMetadata"
+ "StoreKit_Internal.SKPurchaseAnalyticsMetadata"
+ "Tq,N,R,Venvironment"
+ "Tq,N,V_environment"
+ "_logPurchaseResult:primaryError:mappedError:inAppPurchaseID:analyticsMetadata:"
+ "initWithStorefront:environment:serverCorrelationID:"
+ "metadataFromError:"
+ "metadataFromTransactionDictionary:"
+ "v56@0:8q16@24@32@40@48"
- "23:12:22"
- "H"
- "Jun  2 2026"
- "_logPurchaseResult:primaryError:mappedError:inAppPurchaseID:"
- "v48@0:8q16@24@32@40"

```
