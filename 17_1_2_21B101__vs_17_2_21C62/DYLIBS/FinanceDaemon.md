## FinanceDaemon

> `/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon`

```diff

-143.7.1.1.0
-  __TEXT.__text: 0x1583e8
-  __TEXT.__auth_stubs: 0x4630
+143.7.13.0.0
+  __TEXT.__text: 0x15de4c
+  __TEXT.__auth_stubs: 0x4770
   __TEXT.__objc_methlist: 0x3c8
-  __TEXT.__const: 0x40c8
-  __TEXT.__cstring: 0x9971
+  __TEXT.__const: 0x4278
+  __TEXT.__cstring: 0x9dc1
   __TEXT.__oslogstring: 0x2b
-  __TEXT.__swift5_typeref: 0x2552
-  __TEXT.__swift5_fieldmd: 0x1bc0
-  __TEXT.__constg_swiftt: 0x1fdc
-  __TEXT.__swift5_reflstr: 0x23f3
-  __TEXT.__swift5_protos: 0x84
-  __TEXT.__swift5_proto: 0x358
-  __TEXT.__swift5_types: 0x1f0
-  __TEXT.__swift5_capture: 0x135c
+  __TEXT.__swift5_typeref: 0x259a
+  __TEXT.__swift5_fieldmd: 0x1c54
+  __TEXT.__constg_swiftt: 0x20a8
+  __TEXT.__swift5_reflstr: 0x2433
+  __TEXT.__swift5_protos: 0x88
+  __TEXT.__swift5_proto: 0x36c
+  __TEXT.__swift5_types: 0x1fc
+  __TEXT.__swift5_capture: 0x1388
   __TEXT.__swift5_assocty: 0x458
-  __TEXT.__unwind_info: 0x53a8
-  __TEXT.__eh_frame: 0xe8f4
+  __TEXT.__unwind_info: 0x5a2c
+  __TEXT.__eh_frame: 0xee2c
   __TEXT.__objc_classname: 0xe7
-  __TEXT.__objc_methname: 0x2ab4
+  __TEXT.__objc_methname: 0x2aed
   __TEXT.__objc_methtype: 0x5b6
   __TEXT.__objc_stubs: 0x120
-  __DATA_CONST.__got: 0x958
+  __DATA_CONST.__got: 0x998
   __DATA_CONST.__const: 0x1c8
-  __DATA_CONST.__objc_classlist: 0x118
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3318
-  __DATA_CONST.__objc_selrefs: 0xb10
+  __DATA_CONST.__objc_const: 0x33f0
+  __DATA_CONST.__objc_selrefs: 0xb28
   __AUTH_CONST.__objc_const: 0x230
-  __AUTH_CONST.__const: 0x5ec8
-  __AUTH_CONST.__auth_got: 0x2320
+  __AUTH_CONST.__const: 0x60e8
+  __AUTH_CONST.__auth_got: 0x23c0
   __AUTH.__objc_data: 0x458
-  __AUTH.__data: 0x1fe0
+  __AUTH.__data: 0x20a8
   __DATA.__objc_protorefs: 0xb8
-  __DATA.__objc_classrefs: 0x278
+  __DATA.__objc_classrefs: 0x280
   __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x280
-  __DATA.__data: 0x27c8
-  __DATA.__bss: 0x5990
+  __DATA.__data: 0x2818
+  __DATA.__bss: 0x5c10
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x1a8
   __DATA_DIRTY.__data: 0x1770

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E4D05D6A-94D6-36A2-B8DB-B814737C8811
-  Functions: 4866
-  Symbols:   1526
-  CStrings:  1314
+  UUID: BE46DE17-BD85-329C-95DF-9FA92936609C
+  Functions: 4942
+  Symbols:   1539
+  CStrings:  1333
 
Symbols:
+ _NSMergeByPropertyObjectTrumpMergePolicy
+ _OBJC_CLASS_$_LSApplicationExtensionRecord
+ __DATA__TtC13FinanceDaemon24InstitutionMatchingCache
+ __IVARS__TtC13FinanceDaemon24InstitutionMatchingCache
+ __METACLASS_DATA__TtC13FinanceDaemon24InstitutionMatchingCache
+ ___swift_memcpy424_8
+ _associated conformance 13FinanceDaemon29InstitutionMatchingCacheErrorOSHAASQ
+ _block_copy_helper.28
+ _block_descriptor.30
+ _block_destroy_helper.29
+ _objectdestroy.2Tm
+ _objectdestroy.8Tm
+ _symbolic $s13FinanceDaemon0bA16StoreEnvironmentP
+ _symbolic So7NSArrayCIeyBy_
+ _symbolic _____ 10FinanceKit18BankConnectConsentV
+ _symbolic _____ 13FinanceDaemon0bA30StoreEnvironmentImplementationV
+ _symbolic _____ 13FinanceDaemon24InstitutionMatchingCacheC
+ _symbolic _____ 13FinanceDaemon29InstitutionMatchingCacheErrorO
+ _symbolic _____Sg 10FinanceKit11InstitutionV3XPCC
+ _symbolic _____Sg 10FinanceKit18RawBankConnectDataO20InstitutionsResponseV
- ___swift_memcpy416_8
- _block_copy_helper.25
- _block_descriptor.27
- _block_destroy_helper.26
- _symbolic So7NSArrayCSgSo7NSErrorCSgIeyByy_
CStrings:
+ "Added cache entry for pass serial: %s"
+ "Asked to add institutions response to cache for pass serial: %s. response: %s"
+ "Asked to remove expired responses from cache for expiration: %s"
+ "Error obtaining cached response for serial: %s error: %@"
+ "Error removing expired cached responses: %@"
+ "Failed to add response: %s to cache for serial: %s Error: %@"
+ "Failed to complete connection authorization: %@."
+ "Failed to fetch the institutions. Payment pass doesn't have the associatedApplicationIdentifiers: %s."
+ "Failed to get consent from store for institutionID: %s. Unable to revoke the token."
+ "Failed to validate account matching for pass with fpanID: %s. Account(%s) doesn't match the pass, but account(%s) does."
+ "Failed to validate account matching for pass with fpanID: %s. Can't find an account that matches the pass."
+ "Removed the following expired results from cache: %s"
+ "Response expiration not valid. Expiration: %s. Returning."
+ "Retrieving institutions response from cache for pass serial: %s"
+ "Returning cached response: %s from cache for pass serial: %s"
+ "Successfully cleaned up local consent for institutionID: %s."
+ "Successfully revoked consent for institutionID: %s."
+ "Unable to revoke consent for institutionID: %s, failed with error: %@. The consent has been removed from the device."
+ "_TtC13FinanceDaemon24InstitutionMatchingCache"
+ "context"
+ "fkPaymentPass"
+ "initWithBundleIdentifier:error:"
+ "lastTransactionsRefreshFailureValue == nil"
+ "passSerial"
+ "v32@0:8@\"XPCInstitution\"16@?<v@?@\"NSArray\">24"
- "Error while trying to call complete consent: %@."
- "Failed to get consent for institutionID: %s."
- "Failed to revoke consent for institutionID: %s."
- "Failed to validate account matching for pass with fpanID: %s.\nAccount(%s) doesn't match the pass,\nbut account(%s) does."
- "Failed to validate account matching for pass with fpanID: %s.\nCan't find an account that matches the pass."
- "v32@0:8@\"XPCInstitution\"16@?<v@?@\"NSArray\"@\"NSError\">24"

```
