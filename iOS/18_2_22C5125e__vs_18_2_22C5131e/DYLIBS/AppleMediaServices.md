## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

-8.2.19.0.0
-  __TEXT.__text: 0x7f4c08
+8.2.22.0.0
+  __TEXT.__text: 0x7f59cc
   __TEXT.__auth_stubs: 0x44b0
-  __TEXT.__objc_methlist: 0x1e478
-  __TEXT.__cstring: 0x27858
+  __TEXT.__objc_methlist: 0x1e500
+  __TEXT.__cstring: 0x2794e
   __TEXT.__const: 0x5d804
   __TEXT.__swift5_typeref: 0x38c5
   __TEXT.__swift5_reflstr: 0x1b78

   __TEXT.__swift5_capture: 0x1a44
   __TEXT.__swift5_mpenum: 0x48
   __TEXT.__swift5_protos: 0x70
-  __TEXT.__oslogstring: 0x2d140
+  __TEXT.__oslogstring: 0x2d22c
   __TEXT.__gcc_except_tab: 0x16ecc
   __TEXT.__dlopen_cstrs: 0x8d3
   __TEXT.__ustring: 0x1b2
-  __TEXT.__unwind_info: 0x119b0
+  __TEXT.__unwind_info: 0x119f0
   __TEXT.__eh_frame: 0xc4c0
   __TEXT.__objc_classname: 0x3a83
-  __TEXT.__objc_methname: 0x3f8be
+  __TEXT.__objc_methname: 0x3fa41
   __TEXT.__objc_methtype: 0x6f82
-  __TEXT.__objc_stubs: 0x2c5a0
-  __DATA_CONST.__got: 0x1820
-  __DATA_CONST.__const: 0xbe20
+  __TEXT.__objc_stubs: 0x2c680
+  __DATA_CONST.__got: 0x1828
+  __DATA_CONST.__const: 0xbea0
   __DATA_CONST.__objc_classlist: 0x1218
   __DATA_CONST.__objc_catlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x350
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe060
+  __DATA_CONST.__objc_selrefs: 0xe0b0
   __DATA_CONST.__objc_protorefs: 0x170
   __DATA_CONST.__objc_superrefs: 0xc38
   __DATA_CONST.__objc_arraydata: 0x518
   __AUTH_CONST.__auth_got: 0x2270
-  __AUTH_CONST.__auth_ptr: 0xa08
-  __AUTH_CONST.__const: 0x29df8
-  __AUTH_CONST.__cfstring: 0x20580
-  __AUTH_CONST.__objc_const: 0x39cd8
+  __AUTH_CONST.__auth_ptr: 0xa40
+  __AUTH_CONST.__const: 0x29e18
+  __AUTH_CONST.__cfstring: 0x20660
+  __AUTH_CONST.__objc_const: 0x39d38
   __AUTH_CONST.__objc_intobj: 0xc78
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x118

   __AUTH.__data: 0xea8
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x5
-  __DATA.__objc_ivar: 0x176c
-  __DATA.__data: 0x5580
+  __DATA.__objc_ivar: 0x1774
+  __DATA.__data: 0x55b0
   __DATA.__bss: 0xa319
   __DATA.__common: 0xb48
   __DATA_DIRTY.__objc_ivar: 0x64c
   __DATA_DIRTY.__objc_data: 0x53e0
-  __DATA_DIRTY.__data: 0x1a00
-  __DATA_DIRTY.__bss: 0x3770
+  __DATA_DIRTY.__data: 0x19f8
+  __DATA_DIRTY.__bss: 0x3780
   __DATA_DIRTY.__common: 0x88
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 21812
-  Symbols:   19060
-  CStrings:  19971
+  Functions: 21833
+  Symbols:   19080
+  CStrings:  19997
 
Symbols:
+ _AMSChannelPostLinkingActionURL
CStrings:
+ "%!{(MISSING)public}@: [%!{(MISSING)public}@] Failed to fetch area identifiers (error: %!{(MISSING)public}@)"
+ "%!{(MISSING)public}@: [%!{(MISSING)public}@] Fetched area identifiers: %!{(MISSING)public}@"
+ "%!{(MISSING)public}@: [%!{(MISSING)public}@] Fetching area identifiers (namespaces: %!{(MISSING)public}@)"
+ "%!{(MISSING)public}@: [%!{(MISSING)public}@] Fetching area identifiers (topics: %!{(MISSING)public}@)"
+ "%!{(MISSING)public}@: [%!{(MISSING)public}@] Post linking action failed. Error: %!{(MISSING)public}@."
+ "%!{(MISSING)public}@Fetching treatments (areaIDs: %!{(MISSING)public}@)"
+ "@\"AMSPromise\"16@?0@\"AMSChannelLinkResult\"8"
+ "@\"AMSPromise\"24@?0@\"AMSChannelLinkResult\"8@\"NSError\"16"
+ "T@\"NSSet\",R,N,V_postLinkingFields"
+ "T@\"NSString\",R,N,V_subscriptionId"
+ "Unexpectedly completed with no result or error!"
+ "_chainedLinkingResult:"
+ "_postLinkingActionURLRequestWithResult:"
+ "_postLinkingFields"
+ "_postLinkingParametersWithResult:account:"
+ "_processPostLinkingActionsWithResult:"
+ "_processPostLinkingMetricsWithResult:error:"
+ "_subscriptionId"
+ "activeTreatmentsForAreas:"
+ "applyOverlayMetrics:"
+ "getChannelPostLinkingAction"
+ "iCloudPartition"
+ "icloud-partition"
+ "postLinkingFields"
+ "replaceOverlayMetrics:"
+ "sharedWebUIPageConfig"
+ "subId"
+ "subscriptionId"
- "%!{(MISSING)public}@: [%!{(MISSING)public}@] Fetching areas (namespaces: %!{(MISSING)public}@)"
- "%!{(MISSING)public}@: [%!{(MISSING)public}@] Fetching areas (topics: %!{(MISSING)public}@)"
- "%!{(MISSING)public}@Fetching treatments (areas: %!{(MISSING)public}@)"
- "_currentTreatmentsForAreas:"

```
