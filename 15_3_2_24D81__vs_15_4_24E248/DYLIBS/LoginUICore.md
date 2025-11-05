## LoginUICore

> `/System/Library/PrivateFrameworks/LoginUIKit.framework/Versions/A/Frameworks/LoginUICore.framework/Versions/A/LoginUICore`

```diff

-370.3.2.0.0
-  __TEXT.__text: 0x2af8
+370.5.3.0.0
+  __TEXT.__text: 0x2afc
   __TEXT.__auth_stubs: 0x550
   __TEXT.__const: 0xf8
   __TEXT.__cstring: 0x179e
-  __TEXT.__unwind_info: 0xc8
+  __TEXT.__unwind_info: 0xd0
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0x448
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/login.framework/Versions/A/Frameworks/loginsupport.framework/Versions/A/loginsupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 881EC732-D484-3875-AB67-DF2ED0F564AC
-  Functions: 22
-  Symbols:   263
+  UUID: 62275E9A-EAEE-36B5-A70D-0F7FDD2523F8
+  Functions: 27
+  Symbols:   270
   CStrings:  538
 
Symbols:
+ LUICGetBootStyle.cold.1
+ LUICopyColorForOptions.cold.1
+ LUICopyColorForOptions.cold.2
+ LUICreateUserImageFromImageWithOptions.cold.1
+ LUIGetImageForIdentifierWithOptions.cold.1
+ LUIGetImageForIdentifierWithOptions.cold.2
+ _LUIGetImageForIdentifier.cold.1
Functions:
~ _LUICopyColorForOptions : 704 -> 672
~ _LUICGetBootStyle : 68 -> 56
~ _LUIGetImageForIdentifierWithOptions : 1284 -> 1264
~ _LUICreateUserImageFromImageWithOptions : 756 -> 740
~ __LUIGetImageForIdentifier : 176 -> 160

```
