## AACDependencies

> `/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Versions/A/Frameworks/AACDependencies.framework/Versions/A/AACDependencies`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-55.0.0.0.0
-  __TEXT.__text: 0x1cac
-  __TEXT.__objc_methlist: 0x4ac
+56.0.0.0.0
+  __TEXT.__text: 0x1cbc
+  __TEXT.__objc_methlist: 0x4c4
   __TEXT.__const: 0x60
   __TEXT.__cstring: 0x78
   __TEXT.__gcc_except_tab: 0x3c

   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x298
+  __DATA_CONST.__objc_selrefs: 0x2a8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__got: 0x60
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0xbc0
+  __AUTH_CONST.__objc_const: 0xbf0
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x80
+  __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x180
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 85
-  Symbols:   263
+  Functions: 87
+  Symbols:   266
   CStrings:  7
 
Symbols:
+ -[AEDSingleAppModeConfiguration allowsAutoCapitalization]
+ -[AEDSingleAppModeConfiguration setAllowsAutoCapitalization:]
+ OBJC_IVAR_$_AEDSingleAppModeConfiguration._allowsAutoCapitalization
```
