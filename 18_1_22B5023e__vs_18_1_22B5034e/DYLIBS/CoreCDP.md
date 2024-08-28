## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`

```diff

-383.0.0.0.0
-  __TEXT.__text: 0x4a2ac
+383.2.0.0.0
+  __TEXT.__text: 0x4af88
   __TEXT.__auth_stubs: 0x1000
-  __TEXT.__objc_methlist: 0x2a64
+  __TEXT.__objc_methlist: 0x2aa4
   __TEXT.__const: 0x1124
-  __TEXT.__gcc_except_tab: 0x10b0
-  __TEXT.__oslogstring: 0x7fec
-  __TEXT.__cstring: 0x4e7f
+  __TEXT.__gcc_except_tab: 0x10f0
+  __TEXT.__oslogstring: 0x81a7
+  __TEXT.__cstring: 0x4ee3
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x12f0
+  __TEXT.__unwind_info: 0x1310
   __TEXT.__objc_classname: 0x6eb
-  __TEXT.__objc_methname: 0x811b
-  __TEXT.__objc_methtype: 0x18c9
-  __TEXT.__objc_stubs: 0x4940
+  __TEXT.__objc_methname: 0x820d
+  __TEXT.__objc_methtype: 0x1968
+  __TEXT.__objc_stubs: 0x4980
   __DATA_CONST.__got: 0x488
-  __DATA_CONST.__const: 0x2b98
+  __DATA_CONST.__const: 0x2bf0
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d38
+  __DATA_CONST.__objc_selrefs: 0x1d70
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__auth_got: 0x810
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x530
-  __AUTH_CONST.__cfstring: 0x3240
-  __AUTH_CONST.__objc_const: 0x9530
+  __AUTH_CONST.__cfstring: 0x32a0
+  __AUTH_CONST.__objc_const: 0x95a0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x690

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1856
-  Symbols:   2640
-  CStrings:  2938
+  Functions: 1874
+  Symbols:   2664
+  CStrings:  2959
 
Symbols:
+ _CDP_FOLLOWUP_ADP_STATE_HEALING
CStrings:
+ "requestNewURLBagIfNecessaryWithCompletion:"
+ "\"Creating context for ADP State healing CFU\""
+ "\"Received isWalrusStatusMismatchDetectionEnabled = %!d(MISSING)\""
+ "isWalrusStatusMismatchDetectionEnabledWithCompletion:"
+ "v24@0:8@?<v@?@\"CDPCombinedWalrusStatus\"@\"NSError\">16"
+ "\"Error %!@(MISSING) getting isWalrusStatusMismatchDetectionEnabled from URLBag, returning false\""
+ "combinedWalrusStatus:"
+ "\"isWalrusStatusMismatchDetectionEnabled has overrider set, returning false\""
+ "Vv32@0:8@\"CDPContext\"16@?<v@?@\"CDPCombinedWalrusStatus\"@\"NSError\">24"
+ "combinedWalrusStatusWithContext:completion:"
+ "mismatchDetected"
+ "contextForADPStateHealing"
+ "isWalrusStatusMismatchDetectionEnabled"
+ "combinedWalrusStatusWithCompletion:"
+ "@\"CDPCombinedWalrusStatus\"24@0:8^@16"
+ "kADPStateHealing"
+ "\"Failed to fetch walrus combined status with error: %!@(MISSING)\""
+ "\"XPC Error while fetching walrus combined status: %!{(MISSING)public}@\""
+ "\"Walrus combined status %!@(MISSING)\""
+ "disableWalrusStatusMismatchDetectionEnabled"
+ "Walrus: Fetching combined status."

```
