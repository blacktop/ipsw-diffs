## ThreadNetwork

> `/System/Library/Frameworks/ThreadNetwork.framework/Versions/A/ThreadNetwork`

```diff

-442.0.0.0.0
-  __TEXT.__text: 0xf770
+446.0.5.0.0
+  __TEXT.__text: 0xfb64
   __TEXT.__objc_methlist: 0xe18
   __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x1913
-  __TEXT.__oslogstring: 0xc67
+  __TEXT.__cstring: 0x1931
+  __TEXT.__oslogstring: 0xc8f
   __TEXT.__gcc_except_tab: 0x190
   __TEXT.__unwind_info: 0x3e8
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x830
+  __DATA_CONST.__objc_selrefs: 0x840
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__got: 0x138

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 399
-  Symbols:   906
-  CStrings:  235
+  Functions: 400
+  Symbols:   912
+  CStrings:  237
 
Symbols:
+ _CTCSAddRuntimeResolvedClasses
+ _NSClassFromString
+ _NSStringFromClass
+ _class_getImageName
+ _objc_msgSend$domain
+ _objc_msgSend$isEqualToString:
Functions:
~ ___64+[XPCInterface CTCSGetExpectedClassesForOptionsOverXPCInterface]_block_invoke : 320 -> 348
+ _CTCSAddRuntimeResolvedClasses
~ ___73+[XPCInterface CTCSExpectedXPCInterfaceClassesForAllActiveDataSetRecords]_block_invoke : 380 -> 408
~ ___35-[THClient retrieveAllCredentials:]_block_invoke : 680 -> 760
~ ___57-[THClient retrieveCredentialsForBorderAgent:completion:]_block_invoke : 524 -> 604
~ ___59-[THClient retrieveCredentialsForExtendedPANID:completion:]_block_invoke : 428 -> 508
~ ___41-[THClient retrieveAllActiveCredentials:]_block_invoke : 680 -> 784
~ -[THClient handleActiveNearbyNetworksResponse:error:isInternal:completion:] : 720 -> 824
CStrings:
+ "%s: allowing %{public}@ from %{public}s"
+ "CTCSAddRuntimeResolvedClasses"
```
