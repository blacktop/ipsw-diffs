## ClipServices

> `/System/Library/PrivateFrameworks/ClipServices.framework/ClipServices`

```diff

-1039.1.0.0.0
-  __TEXT.__text: 0x375c0
+1040.1.0.0.0
+  __TEXT.__text: 0x37954
   __TEXT.__objc_methlist: 0x3254
   __TEXT.__gcc_except_tab: 0xa6c
-  __TEXT.__cstring: 0x3f4a
-  __TEXT.__const: 0x110
-  __TEXT.__oslogstring: 0x480d
+  __TEXT.__cstring: 0x3fce
+  __TEXT.__const: 0x118
+  __TEXT.__oslogstring: 0x48a8
   __TEXT.__dlopen_cstrs: 0x2e4
   __TEXT.__unwind_info: 0x1630
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__got: 0x4d0
   __AUTH_CONST.__const: 0x620
-  __AUTH_CONST.__cfstring: 0x34a0
+  __AUTH_CONST.__cfstring: 0x3500
   __AUTH_CONST.__objc_const: 0x5158
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1491
-  Symbols:   2495
-  CStrings:  832
+  Functions: 1492
+  Symbols:   2494
+  CStrings:  841
 
Symbols:
- ___62-[CPSImageDownloader _downloadImageWithURL:completionHandler:]_block_invoke_4
Functions:
~ -[CPSImageDownloader _downloadImageWithURL:completionHandler:] : 600 -> 828
~ -[CPSClipMetadata canUpdateOnPhysicalInvocation] : 204 -> 240
~ -[CPSAppInfoFetcher lookUpClipMetadataByBundleID:sourceBundleID:URL:downloadIconIfNeeded:skipCaching:completionHandler:] : 1004 -> 1196
~ -[CPSAppInfoFetcher _downloadIconIfNeeded:sourceBundleID:completionHandler:] : 652 -> 860
~ -[CPSAppInfoFetcher _lookUpClipDemoAMSMetadataWithBundleID:completion:] : 484 -> 668
+ -[CPSClipMetadata canUpdateOnPhysicalInvocation].cold.1
CStrings:
+ "<ams-bag>"
+ "<none>"
+ "<unattributed>"
+ "CPSAppInfoFetcher.demoMetadata"
+ "CPSAppInfoFetcher.icon"
+ "CPSAppInfoFetcher.metadata"
+ "CPSEgress site=%{public}s host=%{sensitive}@ attributedTo=%{public}@"
+ "CPSImageDownloader"
+ "Failed to update or install an app clip on physical invocation. Reason: size too big."
```
