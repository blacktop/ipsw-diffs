## FinHealthCore

> `/System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore`

```diff

-1.8.1.46.0
-  __TEXT.__text: 0x6c39c
-  __TEXT.__auth_stubs: 0x1d80
-  __TEXT.__objc_methlist: 0x3234
-  __TEXT.__const: 0xde8
-  __TEXT.__cstring: 0x8d22
-  __TEXT.__oslogstring: 0x2379
-  __TEXT.__gcc_except_tab: 0xc7c
-  __TEXT.__swift5_typeref: 0x85e
+1.8.1.48.0
+  __TEXT.__text: 0x754f4
+  __TEXT.__auth_stubs: 0x1d70
+  __TEXT.__objc_methlist: 0x32c4
+  __TEXT.__const: 0xdf8
+  __TEXT.__cstring: 0x8d62
+  __TEXT.__oslogstring: 0x2479
+  __TEXT.__gcc_except_tab: 0xc78
+  __TEXT.__swift5_typeref: 0x886
   __TEXT.__swift5_capture: 0x348
   __TEXT.__constg_swiftt: 0x488
   __TEXT.__swift5_reflstr: 0x2a4

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x1480
-  __TEXT.__eh_frame: 0x13c8
-  __TEXT.__objc_classname: 0x694
-  __TEXT.__objc_methname: 0x87f0
+  __TEXT.__unwind_info: 0x14a0
+  __TEXT.__eh_frame: 0x13f8
+  __TEXT.__objc_classname: 0x695
+  __TEXT.__objc_methname: 0x8a40
   __TEXT.__objc_methtype: 0x8f2
-  __TEXT.__objc_stubs: 0x5e60
+  __TEXT.__objc_stubs: 0x5ec0
   __DATA_CONST.__got: 0x6b0
-  __DATA_CONST.__const: 0x1858
+  __DATA_CONST.__const: 0x1860
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f48
+  __DATA_CONST.__objc_selrefs: 0x1fa8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0xed0
+  __AUTH_CONST.__auth_got: 0xec8
   __AUTH_CONST.__const: 0x1848
-  __AUTH_CONST.__cfstring: 0x5fc0
-  __AUTH_CONST.__objc_const: 0x61c8
+  __AUTH_CONST.__cfstring: 0x6020
+  __AUTH_CONST.__objc_const: 0x6288
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH.__objc_data: 0x670
-  __DATA.__objc_ivar: 0x3d0
-  __DATA.__data: 0x540
+  __DATA.__objc_ivar: 0x3e0
+  __DATA.__data: 0x550
   __DATA.__bss: 0xd70
   __DATA.__common: 0x9
   __DATA_DIRTY.__objc_data: 0xf68

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9F49F6FB-12B2-3CB0-B9D4-78B29B089DF8
-  Functions: 1891
-  Symbols:   5073
-  CStrings:  3448
+  UUID: 51ECC303-BAEB-3F87-ADBA-28765722AFBF
+  Functions: 1909
+  Symbols:   5106
+  CStrings:  3479
 
Symbols:
+ -[FHBankConnectDescriptionCleaner _cleanDescriptionForTransaction:]
+ -[FHBankConnectDescriptionCleaner _homogenizeMerchantPattern:]
+ -[FHBankConnectDescriptionCleaner _topMerchantPatternsFromDescription:]
+ -[FHBankConnectDescriptionCleaner setTopMerchantHomogenizeKey:]
+ -[FHBankConnectDescriptionCleaner setTopMerchantKey:]
+ -[FHBankConnectDescriptionCleaner setTopMerchantMatchPatternsKey:]
+ -[FHBankConnectDescriptionCleaner setTopMerchantPatterns:]
+ -[FHBankConnectDescriptionCleaner topMerchantHomogenizeKey]
+ -[FHBankConnectDescriptionCleaner topMerchantKey]
+ -[FHBankConnectDescriptionCleaner topMerchantMatchPatternsKey]
+ -[FHBankConnectDescriptionCleaner topMerchantPatterns]
+ -[FHTransaction bankConnectTransactionHasBeenUpdatedFrom:]
+ _FHTopMerchantRegexPatterns
+ _OBJC_IVAR_$_FHBankConnectDescriptionCleaner._topMerchantHomogenizeKey
+ _OBJC_IVAR_$_FHBankConnectDescriptionCleaner._topMerchantKey
+ _OBJC_IVAR_$_FHBankConnectDescriptionCleaner._topMerchantMatchPatternsKey
+ _OBJC_IVAR_$_FHBankConnectDescriptionCleaner._topMerchantPatterns
+ _objc_msgSend$_cleanDescriptionForTransaction:
+ _objc_msgSend$_homogenizeMerchantPattern:
+ _objc_msgSend$_topMerchantPatternsFromDescription:
+ _objc_msgSend$bankConnectTransactionHasBeenUpdatedFrom:
+ _symbolic ______Say_____Gt 10Foundation4UUIDV 10FinanceKit11TransactionV7InsightO
+ _symbolic _____y_____Say_____GG s18_DictionaryStorageC 10Foundation4UUIDV 10FinanceKit11TransactionV7InsightO
- _objc_msgSend$getTransactionInternalState:
- _objc_release_x11
CStrings:
+ "1.2"
+ "Current Grouping Version: %@"
+ "Error creating homogenize regex: %@"
+ "Error creating top merchant match regex: %@"
+ "Error while getting transaction insights: %@"
+ "FinanceKitDataStore : fhAccountsDict = %{private}s"
+ "Grouping Schema Will Update to %@"
+ "HOMOGENIZE_PATTERNS"
+ "MATCH_PATTERNS"
+ "No updated data for transaction with identifier: %@\nNot recomputing insights"
+ "T@\"NSDictionary\",C,N,V_topMerchantPatterns"
+ "T@\"NSString\",C,N,V_topMerchantHomogenizeKey"
+ "T@\"NSString\",C,N,V_topMerchantKey"
+ "T@\"NSString\",C,N,V_topMerchantMatchPatternsKey"
+ "TOP_MERCHANT_PATTERNS"
+ "_cleanDescriptionForTransaction:"
+ "_homogenizeMerchantPattern:"
+ "_topMerchantHomogenizeKey"
+ "_topMerchantKey"
+ "_topMerchantMatchPatternsKey"
+ "_topMerchantPatterns"
+ "_topMerchantPatternsFromDescription:"
+ "bankConnectTransactionHasBeenUpdatedFrom:"
+ "setTopMerchantHomogenizeKey:"
+ "setTopMerchantKey:"
+ "setTopMerchantMatchPatternsKey:"
+ "setTopMerchantPatterns:"
+ "topMerchantHomogenizeKey"
+ "topMerchantKey"
+ "topMerchantMatchPatternsKey"
+ "topMerchantPatterns"
- "1.0"
- "FinanceKitDataStore : fhAccountsDict = %s "
- "Grouping Schema Will Update"

```
