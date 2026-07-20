## AACDependencies

> `/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACDependencies.framework/AACDependencies`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-55.0.0.0.0
-  __TEXT.__text: 0x1c88
-  __TEXT.__objc_methlist: 0x35c
+56.0.0.0.0
+  __TEXT.__text: 0x1cac
+  __TEXT.__objc_methlist: 0x374
   __TEXT.__const: 0x78
   __TEXT.__cstring: 0x80
   __TEXT.__unwind_info: 0xf8

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x408
+  __DATA_CONST.__objc_selrefs: 0x420
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__objc_const: 0xaf0
+  __AUTH_CONST.__objc_const: 0xb20
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x68
+  __DATA.__objc_ivar: 0x6c
   __DATA.__data: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 71
-  Symbols:   368
+  Functions: 73
+  Symbols:   373
   CStrings:  6
 
Symbols:
+ -[AEDSingleAppModeConfiguration allowsAutoCapitalization]
+ -[AEDSingleAppModeConfiguration setAllowsAutoCapitalization:]
+ _OBJC_IVAR_$_AEDSingleAppModeConfiguration._allowsAutoCapitalization
+ _objc_msgSend$allowsAutoCapitalization
+ _objc_msgSend$setAllowAutoCapitalization:
```
