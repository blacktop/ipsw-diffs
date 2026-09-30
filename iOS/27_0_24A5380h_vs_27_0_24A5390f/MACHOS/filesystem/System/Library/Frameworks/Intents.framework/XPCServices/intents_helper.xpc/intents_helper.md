## intents_helper

> `/System/Library/Frameworks/Intents.framework/XPCServices/intents_helper.xpc/intents_helper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-4016.0.43.5.0
+4016.0.45.3.0
   __TEXT.__text: 0x1b10
-  __TEXT.__auth_stubs: 0x350
+  __TEXT.__auth_stubs: 0x360
+  __TEXT.__lazy_helpers: 0x54
   __TEXT.__objc_stubs: 0x6e0
   __TEXT.__objc_methlist: 0x284
   __TEXT.__const: 0x60

   __TEXT.__objc_methtype: 0x38a
   __TEXT.__cstring: 0x3a5
   __TEXT.__oslogstring: 0x226
-  __TEXT.__unwind_info: 0xd0
+  __TEXT.__unwind_info: 0xd8
   __DATA_CONST.__const: 0xf0
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x1b8
-  __DATA_CONST.__got: 0x118
+  __DATA_CONST.__auth_got: 0x1c0
+  __DATA_CONST.__got: 0x110
   __DATA.__objc_const: 0x358
   __DATA.__objc_selrefs: 0x2a0
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x120
+  __DATA.__lazy_load_got: 0x8
+  __DATA.__data: 0x124
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
-  - /System/Library/Frameworks/IntentsUI.framework/IntentsUI
   - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 23
-  Symbols:   100
+  Symbols:   101
   CStrings:  163
 
Symbols:
+ __dyld_lazy_load
```
