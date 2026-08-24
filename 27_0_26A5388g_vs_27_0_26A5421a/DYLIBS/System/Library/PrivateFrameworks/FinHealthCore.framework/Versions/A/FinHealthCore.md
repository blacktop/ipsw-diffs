## FinHealthCore

> `/System/Library/PrivateFrameworks/FinHealthCore.framework/Versions/A/FinHealthCore`

```diff

-1.9.1.28.0
-  __TEXT.__text: 0xf08c0
+1.9.1.29.0
+  __TEXT.__text: 0xecac4
   __TEXT.__objc_methlist: 0x35e4
-  __TEXT.__const: 0x3c48
-  __TEXT.__cstring: 0xa18a
-  __TEXT.__oslogstring: 0x3b5e
+  __TEXT.__const: 0x3ac8
+  __TEXT.__cstring: 0xa10a
+  __TEXT.__oslogstring: 0x3b8e
   __TEXT.__gcc_except_tab: 0xb04
-  __TEXT.__swift5_typeref: 0x189a
-  __TEXT.__constg_swiftt: 0xfa0
+  __TEXT.__swift5_typeref: 0x17fa
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
   __TEXT.__swift5_capture: 0x408
-  __TEXT.__swift_as_entry: 0x188
+  __TEXT.__swift_as_entry: 0x198
   __TEXT.__swift_as_ret: 0x1d4
-  __TEXT.__swift_as_cont: 0x340
+  __TEXT.__swift_as_cont: 0x324
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x29c8
-  __TEXT.__eh_frame: 0x51a0
+  __TEXT.__unwind_info: 0x2988
+  __TEXT.__eh_frame: 0x5048
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x20b0
+  __DATA_CONST.__objc_selrefs: 0x20b8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0x238
-  __DATA_CONST.__got: 0xaa0
-  __AUTH_CONST.__const: 0x3348
-  __AUTH_CONST.__cfstring: 0x6840
+  __DATA_CONST.__got: 0xa70
+  __AUTH_CONST.__const: 0x3220
+  __AUTH_CONST.__cfstring: 0x6860
   __AUTH_CONST.__objc_const: 0x6e18
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__auth_got: 0x1368
+  __AUTH_CONST.__auth_got: 0x1350
   __AUTH.__objc_data: 0x1b0
   __AUTH.__data: 0x4d8
   __DATA.__objc_ivar: 0x3f0
-  __DATA.__data: 0xd50
-  __DATA.__bss: 0x3b20
+  __DATA.__data: 0xcd0
+  __DATA.__bss: 0x3930
   __DATA.__common: 0x9
   __DATA_DIRTY.__objc_data: 0x1688
   __DATA_DIRTY.__data: 0xb00

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3412
-  Symbols:   4243
-  CStrings:  1252
+  Functions: 3392
+  Symbols:   4232
+  CStrings:  1248
 
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
