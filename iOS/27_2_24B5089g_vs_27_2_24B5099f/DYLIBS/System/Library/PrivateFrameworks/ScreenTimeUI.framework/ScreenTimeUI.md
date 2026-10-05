## ScreenTimeUI

> `/System/Library/PrivateFrameworks/ScreenTimeUI.framework/ScreenTimeUI`

```diff

-655.1.9.1.0
-  __TEXT.__text: 0x6665c
-  __TEXT.__objc_methlist: 0x1968
-  __TEXT.__const: 0x3014
+655.1.12.0.0
+  __TEXT.__text: 0x6670c
+  __TEXT.__objc_methlist: 0x1970
+  __TEXT.__const: 0x3024
   __TEXT.__cstring: 0x2eba
   __TEXT.__gcc_except_tab: 0x4f4
   __TEXT.__oslogstring: 0x3513

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1940
+  __DATA_CONST.__objc_selrefs: 0x1950
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__got: 0xba8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2030
-  Symbols:   1976
+  Functions: 2031
+  Symbols:   1977
   CStrings:  529
 
Symbols:
+ -[UIImage(STImageAdditions) iconFromPrecomposedImage:platform:migratedToNewScreenTime:]
Functions:
~ -[STIconCache imageForBundleIdentifier:completionHandler:] : 1372 -> 1412
~ -[STIconCache _handleiTunesResponseForAppInfo:response:data:error:completionHandler:] : 844 -> 884
~ -[STIconCache imageForBundleIdentifier:] : 1172 -> 1204
~ -[STIconCache _handleiTunesResponseForAppInfo:response:data:error:] : 688 -> 724
~ -[UIImage(STImageAdditions) iconFromPrecomposedImage:platform:] : 540 -> 8
+ -[UIImage(STImageAdditions) iconFromPrecomposedImage:platform:migratedToNewScreenTime:]
```
