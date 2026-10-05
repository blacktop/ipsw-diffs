## LocalAuthentication

> `/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`

```diff

-2319.40.35.0.1
-  __TEXT.__text: 0x331e8
-  __TEXT.__objc_methlist: 0x3710
-  __TEXT.__const: 0x324
+2319.40.43.0.0
+  __TEXT.__text: 0x331fc
+  __TEXT.__objc_methlist: 0x3728
+  __TEXT.__const: 0x314
   __TEXT.__gcc_except_tab: 0xab8
   __TEXT.__cstring: 0x1960
   __TEXT.__dlopen_cstrs: 0x1cd

   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c10
+  __DATA_CONST.__objc_selrefs: 0x1c20
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__got: 0x600

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1501
-  Symbols:   2868
+  Functions: 1503
+  Symbols:   2870
   CStrings:  538
 
Symbols:
+ -[LAContext optionDisableAutomaticPasscodeFallback]
+ -[LAContext setOptionDisableAutomaticPasscodeFallback:]
Functions:
+ -[LAContext optionDisableAutomaticPasscodeFallback]
+ -[LAContext localizedReason]
```
