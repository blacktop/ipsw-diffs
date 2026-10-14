## CategoriesService

> `/System/Library/PrivateFrameworks/Categories.framework/XPCServices/CategoriesService.xpc/CategoriesService`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-58.1.5.0.0
-  __TEXT.__text: 0x4fe8
+58.1.7.1.0
+  __TEXT.__text: 0x5104
   __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_stubs: 0xec0
-  __TEXT.__objc_methlist: 0x3cc
+  __TEXT.__objc_stubs: 0xf20
+  __TEXT.__objc_methlist: 0x404
   __TEXT.__const: 0xc0
-  __TEXT.__objc_methname: 0xf12
-  __TEXT.__oslogstring: 0x62c
-  __TEXT.__cstring: 0x61c
+  __TEXT.__objc_methname: 0xfa3
+  __TEXT.__oslogstring: 0x66c
+  __TEXT.__cstring: 0x641
   __TEXT.__objc_classname: 0xbb
-  __TEXT.__objc_methtype: 0x2ce
-  __TEXT.__gcc_except_tab: 0x100
-  __TEXT.__unwind_info: 0x1d8
+  __TEXT.__objc_methtype: 0x34f
+  __TEXT.__gcc_except_tab: 0x10c
+  __TEXT.__unwind_info: 0x1e8
   __DATA_CONST.__const: 0x2c0
-  __DATA_CONST.__cfstring: 0xac0
+  __DATA_CONST.__cfstring: 0xae0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x218
   __DATA_CONST.__got: 0x1b8
-  __DATA.__objc_const: 0x7c0
-  __DATA.__objc_selrefs: 0x490
-  __DATA.__objc_ivar: 0x28
+  __DATA.__objc_const: 0x808
+  __DATA.__objc_selrefs: 0x4b0
+  __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 88
+  Functions: 91
   Symbols:   146
-  CStrings:  356
+  CStrings:  367
 
CStrings:
+ "-[Categories_Service appStoreCategoriesForBundleIDs:platform:origin:replyHandler:]"
+ "-[Categories_Service appStoreCategoriesForBundleIDs:platform:origin:replyHandler:]_block_invoke"
+ "@32@0:8@16q24"
+ "START: Media API lookup on behalf of %{private}@ (proxy: %{private}@): %{private}@"
+ "_lookupAppStoreUsing:platform:clientApplication:origin:withCompletionHandler:"
+ "_origin"
+ "appStoreCategoriesForBundleIDs:platform:origin:replyHandler:"
+ "com.apple.mobilesafari"
+ "initWithCallingProcess:origin:"
+ "platform is nil. Calling completionHandler"
+ "proxyAppBundleID"
+ "setProxyAppBundleID:"
+ "v48@0:8@\"NSArray\"16@\"NSString\"24q32@?<v@?@\"NSDictionary\"@\"NSError\">40"
+ "v48@0:8@16@24q32@?40"
+ "v56@0:8@16@24@32q40@?48"
- "-[Categories_Service appStoreCategoriesForBundleIDs:platform:replyHandler:]"
- "-[Categories_Service appStoreCategoriesForBundleIDs:platform:replyHandler:]_block_invoke"
- "START: Media API lookup on behalf of %{private}@: %{private}@"
- "_lookupAppStoreUsing:platform:clientApplication:withCompletionHandler:"
```
