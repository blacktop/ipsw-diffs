## System

> `/System/Library/CoreAccessories/PlugIns/Platform/System.platform/System`

```diff

-  __TEXT.__text: 0x4ef0
+  __TEXT.__text: 0x4ea8
   __TEXT.__objc_methlist: 0x600
   __TEXT.__cstring: 0x68b
   __TEXT.__const: 0x60

   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x34
-  __DATA.__data: 0x240
-  __DATA.__bss: 0x30
+  __DATA.__data: 0x200
+  __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x38
+  __DATA_DIRTY.__data: 0x78
+  __DATA_DIRTY.__bss: 0x18
   __DATA_DIRTY.__common: 0x20
-  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 134
-  Symbols:   666
+  Symbols:   665
   CStrings:  140
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__objc_data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
- _objc_retain_x23
Functions:
~ -[ACCPlatformPluginSystem _observeApplicationState:] : 328 -> 256

```
