## FinanceKit

> `/System/Library/Frameworks/FinanceKit.framework/FinanceKit`

```diff

-144.37.1.0.0
-  __TEXT.__text: 0x59dc54
+144.41.2.0.0
+  __TEXT.__text: 0x59d738
   __TEXT.__auth_stubs: 0x4aa0
-  __TEXT.__objc_methlist: 0x3fa0
+  __TEXT.__objc_methlist: 0x3fb0
   __TEXT.__const: 0x32f54
-  __TEXT.__cstring: 0x196e1
+  __TEXT.__cstring: 0x19881
   __TEXT.__oslogstring: 0x2df
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__swift5_typeref: 0xd27e
-  __TEXT.__swift5_capture: 0x236c
+  __TEXT.__swift5_typeref: 0xd270
+  __TEXT.__swift5_capture: 0x2300
   __TEXT.__constg_swiftt: 0xd464
   __TEXT.__swift5_reflstr: 0x8e93
   __TEXT.__swift5_fieldmd: 0xdf38

   __TEXT.__swift5_proto: 0x308c
   __TEXT.__swift5_types: 0x11d4
   __TEXT.__swift5_mpenum: 0xf0
-  __TEXT.__unwind_info: 0x19fd8
-  __TEXT.__eh_frame: 0x27e84
+  __TEXT.__unwind_info: 0x19fa0
+  __TEXT.__eh_frame: 0x27e44
   __TEXT.__objc_classname: 0x855
-  __TEXT.__objc_methname: 0xd5f6
+  __TEXT.__objc_methname: 0xd60e
   __TEXT.__objc_methtype: 0x15cb
-  __TEXT.__objc_stubs: 0x10a0
+  __TEXT.__objc_stubs: 0x10c0
   __DATA_CONST.__got: 0xe00
   __DATA_CONST.__const: 0x2dd0
   __DATA_CONST.__objc_classlist: 0x8f0

   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xfac8
-  __DATA_CONST.__objc_selrefs: 0x3160
+  __DATA_CONST.__objc_selrefs: 0x3168
   __DATA_CONST.__objc_protorefs: 0x160
   __DATA_CONST.__objc_classrefs: 0x520
   __DATA_CONST.__objc_superrefs: 0x1b0
   __AUTH_CONST.__objc_const: 0x2968
   __AUTH_CONST.__cfstring: 0x520
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__const: 0x27a10
+  __AUTH_CONST.__const: 0x27950
   __AUTH_CONST.__auth_got: 0x2560
   __AUTH.__objc_data: 0x6008
-  __AUTH.__data: 0x9c40
+  __AUTH.__data: 0x9c38
   __DATA.__objc_ivar: 0x3a8
   __DATA.__objc_data: 0x730
-  __DATA.__data: 0x10e78
+  __DATA.__data: 0x10e90
   __DATA.__bss: 0x5ac40
   __DATA.__common: 0x190
   __DATA_DIRTY.__objc_data: 0x2050
-  __DATA_DIRTY.__data: 0x33c8
+  __DATA_DIRTY.__data: 0x33b8
   __DATA_DIRTY.__bss: 0xe00
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 72CDABBB-EDFB-3945-92CA-2AC25F78C573
-  Functions: 36635
-  Symbols:   9869
-  CStrings:  4925
+  UUID: 2D41F2D8-4442-3DAF-9A17-040366AD5C0C
+  Functions: 36625
+  Symbols:   9871
+  CStrings:  4933
 
Symbols:
+ -[FKBankConnectTermsAndConditions shouldNotifyAboutChanges]
+ _objc_msgSend$shouldNotifyAboutChanges
+ _symbolic _____y_____Sg_____G s13ManagedBufferC 10FinanceKit16CoreDataProviderC So16os_unfair_lock_sV
- _symbolic So20FKPaymentTransactionC
- _symbolic _____Sg 10FinanceKit22ManagedInternalAccountC
CStrings:
+ "Could not create background CoreDataProvider: %@"
+ "Deleting PassKit transaction with transactionID: %s for fpanID: %s."
+ "FinanceKit/FinanceStore+MapsOrderTracking.swift"
+ "Ignoring transaction, payment pass with fpanID: %s is not linked with Bank Connect."
+ "Importing PassKit transactions for %s."
+ "Inserting or updating a PassKit payment transaction with ID:\n%s and payment hash: %s."
+ "No PassKit transactions, aborting."
+ "Successfully imported PassKit transactions."
+ "Successfully inserted or updated PassKit payment transaction."
+ "shouldNotifyAboutChanges"
- "Transaction does not have payment hash and will not be handled"
- "Will not update payment transaction with %s\nbecause pass with %s is not linked with\nBank Connect account."

```
