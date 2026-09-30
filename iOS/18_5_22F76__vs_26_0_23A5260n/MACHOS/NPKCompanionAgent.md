## NPKCompanionAgent

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent`

```diff

-1216.24.0.0.0
-  __TEXT.__text: 0x41dec
+1256.0.0.0.0
+  __TEXT.__text: 0x425e8
   __TEXT.__auth_stubs: 0xd00
-  __TEXT.__objc_stubs: 0x76e0
-  __TEXT.__objc_methlist: 0x3250
+  __TEXT.__objc_stubs: 0x7740
+  __TEXT.__objc_methlist: 0x3378
   __TEXT.__const: 0xf8
   __TEXT.__gcc_except_tab: 0x12a4
-  __TEXT.__cstring: 0x23f6
-  __TEXT.__objc_methname: 0xb977
+  __TEXT.__cstring: 0x25cf
+  __TEXT.__objc_methname: 0xbb7b
   __TEXT.__oslogstring: 0x9149
   __TEXT.__objc_classname: 0x6c1
-  __TEXT.__objc_methtype: 0x3356
-  __TEXT.__unwind_info: 0xdb8
+  __TEXT.__objc_methtype: 0x3487
+  __TEXT.__unwind_info: 0xdc8
   __DATA_CONST.__auth_got: 0x690
   __DATA_CONST.__got: 0x6c8
   __DATA_CONST.__const: 0x1df8

   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x59d8
-  __DATA.__objc_selrefs: 0x2698
+  __DATA.__objc_const: 0x5a48
+  __DATA.__objc_selrefs: 0x2708
   __DATA.__objc_ivar: 0x1a8
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0xc00

   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit
+  - /System/Library/PrivateFrameworks/NanoPassKitUI.framework/NanoPassKitUI
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/PairedSync.framework/PairedSync

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E0B51D42-52EB-33B0-AF42-2E45C77BA823
-  Functions: 1094
+  UUID: 3C4317BF-A318-3E7F-97B5-F5688B3B75B1
+  Functions: 1104
   Symbols:   440
-  CStrings:  2733
+  CStrings:  2763
 
Symbols:
+ _NPKSupportedBarcodesFromDataAccessor
- _NPKSupportedBarcodeFromDataAccessor
CStrings:
+ "-[NPDCompanionPassLibrary authorizationStatusForCapability:handler:]"
+ "-[NPDCompanionPassLibrary hasPassWithUniqueID:handler:]"
+ "-[NPDCompanionPassLibrary passesWithPrimaryPaymentApplicationStates:handler:]"
+ "-[NPDCompanionPassLibrary refreshActiveOrScheduledFlights]"
+ "-[NPDCompanionPassLibrary requestAuthorizationForCapability:handler:]"
+ "-[NPDCompanionPassLibrary resetAuthorizationForCapability:handler:]"
+ "-[NPDCompanionPassLibrary simulateFlightUpdate:forPassUniqueID:handler:]"
+ "addSharedFlight:fromSenderAddress:handler:"
+ "allPaymentApplicationUsageSummaries:"
+ "allPaymentApplicationUsageSummariesWithCompletion:"
+ "authorizationStatusForCapability:handler:"
+ "currentSecureElementSnapshot:"
+ "getIdentityPassesOfTypes:handler:"
+ "getPassesOfCardType:handler:"
+ "hasPassWithUniqueID:handler:"
+ "initWithPasses:states:annotations:catalog:"
+ "passesWithPrimaryPaymentApplicationStates:handler:"
+ "reclaimUnusedSEMemory:"
+ "refreshActiveOrScheduledFlights"
+ "requestAuthorizationForCapability:handler:"
+ "resetAuthorizationForCapability:handler:"
+ "setBarcodes:"
+ "simulateFlightUpdate:forPassUniqueID:handler:"
+ "v24@0:8@?<v@?@\"PKProvisioningSEStorageSnapshot\"@\"NSError\">16"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSSet\">24"
+ "v32@0:8@\"NSSet\"16@?<v@?@\"NSSet\">24"
+ "v32@0:8q16@?24"
+ "v32@0:8q16@?<v@?>24"
+ "v32@0:8q16@?<v@?@\"NSSet\">24"
+ "v32@0:8q16@?<v@?q>24"
+ "v40@0:8@\"PKFlight\"16@\"NSString\"24@?<v@?B>32"
+ "v40@0:8@\"PKFlight\"16@\"NSString\"24@?<v@?Q>32"
- "initWithPasses:annotationsByPassUniqueID:accounts:catalog:"
- "setBarcode:"

```
