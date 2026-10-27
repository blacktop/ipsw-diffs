## OSD

> `/System/Library/PrivateFrameworks/OSD.framework/Versions/A/OSD`

```diff

-2027.0.1.0.0
-  __TEXT.__text: 0x8b0
+2027.1.1.0.0
+  __TEXT.__text: 0x72c
   __TEXT.__objc_methlist: 0x130
   __TEXT.__const: 0x8
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__cstring: 0xd7
+  __TEXT.__cstring: 0x5e
   __TEXT.__unwind_info: 0xa8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd8
+  __DATA_CONST.__objc_selrefs: 0xb0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__got: 0x28
+  __DATA_CONST.__got: 0x20
   __AUTH_CONST.__const: 0x70
-  __AUTH_CONST.__cfstring: 0xc0
-  __AUTH_CONST.__objc_const: 0x250
+  __AUTH_CONST.__cfstring: 0x40
+  __AUTH_CONST.__objc_const: 0x230
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x14
+  __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x60
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
-  - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 22
-  Symbols:   109
-  CStrings:  11
+  Symbols:   100
+  CStrings:  4
 
Symbols:
- OBJC_IVAR_$_OSDManager._systemBanners
- _CGSSessionCopyCurrentSessionProperties
- _OBJC_CLASS_$_NSUserDefaults
- __os_feature_enabled_impl
- _objc_msgSend$boolForKey:
- _objc_msgSend$boolValue
- _objc_msgSend$initWithSuiteName:
- _objc_msgSend$objectForKey:
- _objc_msgSend$objectForKeyedSubscript:
Functions:
~ -[OSDManager remoteObjectProxyForGraphicType:] : 900 -> 568
~ -[OSDManager .cxx_destruct] : 68 -> 12
CStrings:
- "EnableSystemBanners"
- "Solarium"
- "SwiftUI"
- "SystemBanners"
- "com.apple.SystemBanner"
- "com.apple.controlcenter"
- "kCGSessionLoginDoneKey"
```
