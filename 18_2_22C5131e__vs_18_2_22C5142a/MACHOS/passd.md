## passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

-1591.3.9.1.0
-  __TEXT.__text: 0x50f604
-  __TEXT.__auth_stubs: 0x4fe0
-  __TEXT.__objc_stubs: 0x6a440
-  __TEXT.__objc_methlist: 0x2bd5c
+1591.3.11.0.0
+  __TEXT.__text: 0x510dbc
+  __TEXT.__auth_stubs: 0x5000
+  __TEXT.__objc_stubs: 0x6a500
+  __TEXT.__objc_methlist: 0x2bd9c
   __TEXT.__const: 0x191a
-  __TEXT.__cstring: 0x596cb
-  __TEXT.__objc_classname: 0x693f
-  __TEXT.__objc_methtype: 0x12395
-  __TEXT.__gcc_except_tab: 0x9594
-  __TEXT.__objc_methname: 0x9566a
-  __TEXT.__oslogstring: 0x4c34d
+  __TEXT.__cstring: 0x5979b
+  __TEXT.__objc_classname: 0x6940
+  __TEXT.__objc_methtype: 0x123a9
+  __TEXT.__gcc_except_tab: 0x95b0
+  __TEXT.__objc_methname: 0x957d2
+  __TEXT.__oslogstring: 0x4c6dd
   __TEXT.__ustring: 0x14
   __TEXT.__swift5_typeref: 0x102a
   __TEXT.__constg_swiftt: 0xb7c

   __TEXT.__swift5_types: 0xa0
   __TEXT.__swift5_capture: 0xa94
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x11498
+  __TEXT.__unwind_info: 0x114c8
   __TEXT.__eh_frame: 0xe1c
-  __DATA_CONST.__auth_got: 0x2800
+  __DATA_CONST.__auth_got: 0x2810
   __DATA_CONST.__got: 0x32e0
   __DATA_CONST.__auth_ptr: 0x2e0
-  __DATA_CONST.__const: 0x2b3c0
-  __DATA_CONST.__cfstring: 0x2eae0
+  __DATA_CONST.__const: 0x2b3e8
+  __DATA_CONST.__cfstring: 0x2eb60
   __DATA_CONST.__objc_classlist: 0x16f0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x568

   __DATA_CONST.__objc_arrayobj: 0x4f8
   __DATA_CONST.__objc_dictobj: 0x280
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x457e0
-  __DATA.__objc_selrefs: 0x1cf58
-  __DATA.__objc_ivar: 0x25cc
+  __DATA.__objc_const: 0x45878
+  __DATA.__objc_selrefs: 0x1cf88
+  __DATA.__objc_ivar: 0x25d4
   __DATA.__objc_data: 0xeff0
   __DATA.__data: 0x4b20
   __DATA.__bss: 0x1390

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 24283
-  Symbols:   3013
-  CStrings:  32578
+  Functions: 24356
+  Symbols:   3015
+  CStrings:  32599
 
Symbols:
+ _PKGetLastProductCacheUpdateTimestamp
+ _PKSetLastProductCacheUpdateTimestamp
CStrings:
+ "\x13\x1f\n\x1c"
+ "Activity already exists for PDFetchStaticPaymentSetupFeaturesActivityIdentifier, not scheduling."
+ "Cache update internal for PDStaticPaymentSetupFeaturesCacheUpdateActivityIdentifier is too short, at %lf. This is likely a config error. Ignoring."
+ "Fetched %ld static payment setup features in the background, for %@"
+ "PDFetchStaticPaymentSetupFeaturesActivityIdentifier"
+ "PDPaymentSetupFeaturesCoordinator: Server fetch blocked, returning cached payment setup features for: %@"
+ "PDPaymentSetupFeaturesCoordinatorClientIdentifier"
+ "PDStaticPaymentSetupFeaturesCacheUpdateActivityIdentifier"
+ "Removing prefetch activity with interval %f for PDStaticPaymentSetupFeaturesCacheUpdateActivityIdentifier."
+ "Scheduled Payment Setup Feature Cache Update"
+ "Scheduling PDFetchStaticPaymentSetupFeaturesActivityIdentifier with criteria: %@"
+ "Scheduling PDStaticPaymentSetupFeaturesCacheUpdateActivityIdentifier with criteria: %@"
+ "Skip updating product cache, last update timestamp: %@, product response timestamp: %@"
+ "Skipping scheduling prefetch for PDStaticPaymentSetupFeaturesCacheUpdateActivityIdentifier. Activity already exists with interval %f."
+ "_cachedPaymentSetupFeaturesForSourceApplicationID:useStaticContent:blockServerFetch:completion:"
+ "_fetchPaymentSetupFeaturesForSourceApplicationID:useStaticContent:blockServerFetch:completion:"
+ "_storeServerPaymentSetupFeatures:productsResponse:isStaticContent:priorDirtyStateIdentifier:"
+ "_suspendTransactionUpdates"
+ "hasCachedPaymentSetupFeatures:"
+ "paymentSetupFeaturesCacheUpdateIntervalForRegion:"
+ "repeatInterval"
+ "scheduleStaticPaymentSetupFeaturesCacheUpdateWithInterval:"
+ "scheduleStaticPaymentSetupFeaturesFetchForSourceApplicationID:"
+ "staticPaymentSetupFeaturesForSourceApplicationID:blockServerFetch:completion:"
+ "unscheduleStaticPaymentSetupFeaturesCacheUpdate"
+ "v44@0:8@16@24B32@36"
- "\x1f\r\x1c"
- "_cachedPaymentSetupFeaturesForSourceApplicationID:useStaticContent:completion:"
- "_fetchPaymentSetupFeaturesForSourceApplicationID:useStaticContent:completion:"
- "_storeServerPaymentSetupFeatures:productsResponse:priorDirtyStateIdentifier:"
- "staticPaymentSetupFeaturesForSourceApplicationID:completion:"

```
