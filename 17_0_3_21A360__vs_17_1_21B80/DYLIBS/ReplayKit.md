## ReplayKit

> `/System/Library/Frameworks/ReplayKit.framework/ReplayKit`

```diff

-504.97.1.2.0
-  __TEXT.__text: 0x235a4
+524.10.0.0.0
+  __TEXT.__text: 0x23790
   __TEXT.__auth_stubs: 0x970
   __TEXT.__objc_methlist: 0x1c4c
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x3f1a
-  __TEXT.__oslogstring: 0x33f2
-  __TEXT.__gcc_except_tab: 0xf4
-  __TEXT.__unwind_info: 0x77c
+  __TEXT.__cstring: 0x3f95
+  __TEXT.__oslogstring: 0x3420
+  __TEXT.__gcc_except_tab: 0x130
+  __TEXT.__unwind_info: 0x790
   __TEXT.__objc_classname: 0x634
-  __TEXT.__objc_methname: 0x69aa
+  __TEXT.__objc_methname: 0x69a6
   __TEXT.__objc_methtype: 0x1993
   __TEXT.__objc_stubs: 0x44c0
   __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x758
+  __DATA_CONST.__const: 0x7a8
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xd0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7661D7BD-9F72-37EC-ADE2-72653A645616
-  Functions: 914
-  Symbols:   3347
-  CStrings:  2034
+  UUID: 29A7D312-912A-3404-B571-CCE13C41C9BE
+  Functions: 917
+  Symbols:   3356
+  CStrings:  2036
 
Symbols:
+ ___71-[RPStoreManager loadItemDetailsForBundleIdentifier:completionHandler:]_block_invoke.55
+ ___71-[RPStoreManager loadItemDetailsForBundleIdentifier:completionHandler:]_block_invoke.cold.1
+ ___71-[RPStoreManager loadItemDetailsForBundleIdentifier:completionHandler:]_block_invoke.cold.2
+ ___block_descriptor_48_e8_32bs40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_56_e8_32s40bs48r_e37_v24?0"AMSLookupResult"8"NSError"16lr48l8s32l8s40l8
+ _objc_msgSend$addFinishBlock:
- -[RPStoreManager loadItemDetailsForBundleIdentifier:completionHandler:].cold.1
- -[RPStoreManager loadItemDetailsForBundleIdentifier:completionHandler:].cold.2
- _objc_msgSend$resultWithError:
CStrings:
+ " [ERROR] %{public}s:%d RPStoreManager::AMSLookupItemArtwork::URLWithHeight could not find artwork with specified parameters"
+ " [ERROR] %{public}s:%d RPStoreManager::performLookupWithBundleIdentifiers could not complete lookup with error:%@"
+ "-[RPStoreManager loadItemDetailsForBundleIdentifier:completionHandler:]_block_invoke"
+ "addFinishBlock:"
+ "v24@?0@\"AMSLookupResult\"8@\"NSError\"16"
- "RPStoreManager::AMSLookupItemArtwork::URLWithHeight could not find artwork with specified parameters"
- "RPStoreManager::performLookupWithBundleIdentifiers could not complete lookup with error:%@"
- "resultWithError:"

```
