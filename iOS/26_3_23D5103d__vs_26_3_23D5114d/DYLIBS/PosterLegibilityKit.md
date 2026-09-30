## PosterLegibilityKit

> `/System/Library/PrivateFrameworks/PosterLegibilityKit.framework/PosterLegibilityKit`

```diff

-304.3.4.1.0
-  __TEXT.__text: 0x1ad94
-  __TEXT.__auth_stubs: 0xd00
+304.3.8.100.0
+  __TEXT.__text: 0x1ae6c
+  __TEXT.__auth_stubs: 0xd10
   __TEXT.__objc_methlist: 0x1ba4
   __TEXT.__const: 0x310
   __TEXT.__cstring: 0xf52
   __TEXT.__oslogstring: 0xe6d
-  __TEXT.__gcc_except_tab: 0x700
+  __TEXT.__gcc_except_tab: 0x704
   __TEXT.__unwind_info: 0x8b0
   __TEXT.__objc_classname: 0x4fb
-  __TEXT.__objc_methname: 0x4806
+  __TEXT.__objc_methname: 0x4831
   __TEXT.__objc_methtype: 0xd0f
-  __TEXT.__objc_stubs: 0x3880
+  __TEXT.__objc_stubs: 0x38a0
   __DATA_CONST.__got: 0x378
   __DATA_CONST.__const: 0x8a0
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11a8
+  __DATA_CONST.__objc_selrefs: 0x11b0
   __DATA_CONST.__objc_superrefs: 0xe8
-  __AUTH_CONST.__auth_got: 0x690
+  __AUTH_CONST.__auth_got: 0x698
   __AUTH_CONST.__const: 0x280
   __AUTH_CONST.__cfstring: 0x1180
   __AUTH_CONST.__objc_const: 0x4ed8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7027C479-BA99-3337-B0A8-1DB220957053
+  UUID: 8C9D89A4-E2E4-3D9D-8B8F-4BAFF588D701
   Functions: 666
-  Symbols:   2787
-  CStrings:  1361
+  Symbols:   2789
+  CStrings:  1362
 
Symbols:
+ ___120+[PLKCachedLegibilityContentDataSource attributedStringContentDataSourceForMaxSize:scale:cacheProvider:metricsProvider:]_block_invoke.112
+ ___block_literal_global.99
+ _objc_msgSend$flatMap:continuationScheduler:
+ _objc_msgSend$globalAsyncScheduler
+ _objc_retain_x28
- ___120+[PLKCachedLegibilityContentDataSource attributedStringContentDataSourceForMaxSize:scale:cacheProvider:metricsProvider:]_block_invoke.111
- ___block_literal_global.98
- _objc_msgSend$flatMap:
Functions:
~ -[PLKLegibilityContentDataSource legibilityContentForObject:legibilityDescriptor:] : 916 -> 944
~ -[PLKCachedLegibilityContentDataSource removeContentForObjects:legibilityDescriptors:] : 1252 -> 1308
~ -[PLKCachedImageGenerator imageFutureForObject:persistenceOptions:context:] : 1016 -> 1028
~ -[PLKCachedImageGenerator prewarmObjects:context:] : 1196 -> 1252
~ -[PLKCachedImageGenerator removeImagesForCacheKeys:] : 764 -> 796
~ -[PLKLegibilityContent initWithContentImageFuture:legibilityDescriptor:renderer:] : 308 -> 340
CStrings:
+ "flatMap:continuationScheduler:"
+ "globalAsyncScheduler"
- "flatMap:"

```
