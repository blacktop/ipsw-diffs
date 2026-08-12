## FinHealthCore

> `/System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore`

```diff

-1.9.1.28.0
-  __TEXT.__text: 0xf8218
+1.9.1.29.0
+  __TEXT.__text: 0xf4424
   __TEXT.__objc_methlist: 0x35e4
-  __TEXT.__const: 0x3cf8
-  __TEXT.__cstring: 0xa2ea
-  __TEXT.__oslogstring: 0x3f6e
+  __TEXT.__const: 0x3b78
+  __TEXT.__cstring: 0xa26a
+  __TEXT.__oslogstring: 0x3f9e
   __TEXT.__gcc_except_tab: 0xbe8
-  __TEXT.__swift5_typeref: 0x1a52
-  __TEXT.__constg_swiftt: 0xfa0
+  __TEXT.__swift5_typeref: 0x19b2
+  __TEXT.__constg_swiftt: 0xf8c
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__swift5_reflstr: 0xc53
-  __TEXT.__swift5_fieldmd: 0xeec
-  __TEXT.__swift5_assocty: 0x180
-  __TEXT.__swift5_proto: 0x1dc
-  __TEXT.__swift5_types: 0x114
+  __TEXT.__swift5_reflstr: 0xc33
+  __TEXT.__swift5_fieldmd: 0xed0
+  __TEXT.__swift5_assocty: 0x150
+  __TEXT.__swift5_proto: 0x1cc
+  __TEXT.__swift5_types: 0x110
   __TEXT.__swift5_capture: 0x448
-  __TEXT.__swift_as_entry: 0x198
+  __TEXT.__swift_as_entry: 0x1a8
   __TEXT.__swift_as_ret: 0x1f8
-  __TEXT.__swift_as_cont: 0x394
+  __TEXT.__swift_as_cont: 0x378
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x2a68
-  __TEXT.__eh_frame: 0x5720
+  __TEXT.__unwind_info: 0x2a30
+  __TEXT.__eh_frame: 0x55c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2108
+  __DATA_CONST.__objc_selrefs: 0x2110
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0x238
-  __DATA_CONST.__got: 0xae8
-  __AUTH_CONST.__const: 0x2bb0
-  __AUTH_CONST.__cfstring: 0x6860
+  __DATA_CONST.__got: 0xab8
+  __AUTH_CONST.__const: 0x2a88
+  __AUTH_CONST.__cfstring: 0x6880
   __AUTH_CONST.__objc_const: 0x6e18
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__auth_got: 0x1568
+  __AUTH_CONST.__auth_got: 0x1550
   __AUTH.__objc_data: 0x1b0
   __AUTH.__data: 0x4d8
   __DATA.__objc_ivar: 0x3f0
-  __DATA.__data: 0xd80
-  __DATA.__bss: 0x3b20
+  __DATA.__data: 0xd10
+  __DATA.__bss: 0x3930
   __DATA.__common: 0x9
   __DATA_DIRTY.__objc_data: 0x1688
   __DATA_DIRTY.__data: 0xaf0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3423
-  Symbols:   4253
-  CStrings:  1273
+  Functions: 3403
+  Symbols:   4242
+  CStrings:  1269
 
Symbols:
+ _objc_msgSend$calendarWithIdentifier:
+ _objc_msgSend$timeZoneWithName:
- _NSLocalizedDescriptionKey
- ___swift_deallocate_boxed_opaque_existential_1
- _associated conformance 13FinHealthCore16AnnotatableTypesOSHAASQ
- _associated conformance 13FinHealthCore16AnnotatableTypesOs12CaseIterableAA8AllCasessADP_Sl
- _objc_msgSend$initWithDomain:code:userInfo:
- _symbolic Say_____G 13FinHealthCore16AnnotatableTypesO
- _symbolic _____ 10FinanceKit11TransactionV
- _symbolic _____ 13FinHealthCore16AnnotatableTypesO
- _symbolic _____y______G 10Foundation20PredicateExpressionsO8VariableV 10FinanceKit11TransactionV
- _symbolic _____y______QPG 10Foundation9PredicateV 10FinanceKit11TransactionV
- _symbolic _____y______QPGSg 10Foundation9PredicateV 10FinanceKit11TransactionV
- _symbolic _____y______y______G_____G 10Foundation20PredicateExpressionsO7KeyPathV AC8VariableV 10FinanceKit11TransactionV AA4UUIDV
- _symbolic _____y______y______y______G_____G_____y_AFGG 10Foundation20PredicateExpressionsO5EqualV AC7KeyPathV AC8VariableV 10FinanceKit11TransactionV AA4UUIDV AC5ValueV
CStrings:
+ "FinanceKitDataStore: failed to fetch annotations for account %s - %@"
+ "FinanceKitDataStore: failed to fetch annotations for transaction %s - %@"
+ "FinanceKitDataStore: failed to set annotations for account %s - %@"
+ "FinanceKitDataStore: failed to set annotations for transaction %s - %@"
+ "FinanceKitDataStore: fetching annotations for account %s"
+ "FinanceKitDataStore: fetching annotations for transaction %s"
+ "FinanceKitDataStore: setting annotations for account %s"
+ "FinanceKitDataStore: setting annotations for transaction %s"
+ "FinanceKitDataStore: successfully fetched annotations for account %s"
+ "FinanceKitDataStore: successfully fetched annotations for transaction %s"
+ "FinanceKitDataStore: successfully set annotations for account %s"
+ "FinanceKitDataStore: successfully set annotations for transaction %s"
+ "UTC"
- "Account"
- "Account not found"
- "FinanceKitDataStore"
- "FinanceKitDataStore: account not found for UUID %s"
- "FinanceKitDataStore: annotating id %s of type %s with key '%s'"
- "FinanceKitDataStore: deleting annotation for id %s of type %s with key '%s'"
- "FinanceKitDataStore: failed to annotate id %s of type %s - %@"
- "FinanceKitDataStore: failed to delete annotation for id %s of type %s - %@"
- "FinanceKitDataStore: failed to fetch annotation for id %s - %@"
- "FinanceKitDataStore: fetching annotation for id %s of type %s with key '%s'"
- "FinanceKitDataStore: no annotation found for id %s with key '%s'"
- "FinanceKitDataStore: successfully annotated id %s of type %s"
- "FinanceKitDataStore: successfully deleted annotation for id %s of type %s"
- "FinanceKitDataStore: successfully fetched annotation for id %s"
- "FinanceKitDataStore: transaction not found for UUID %s"
- "Transaction"
- "Transaction not found"
```
