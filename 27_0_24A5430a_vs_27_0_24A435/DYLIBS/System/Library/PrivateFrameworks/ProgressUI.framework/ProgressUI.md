## ProgressUI

> `/System/Library/PrivateFrameworks/ProgressUI.framework/ProgressUI`

```diff

 2858.0.0.0.0
-  __TEXT.__text: 0x325c
-  __TEXT.__objc_methlist: 0x41c
+  __TEXT.__text: 0x3470
+  __TEXT.__objc_methlist: 0x434
   __TEXT.__const: 0x248
   __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__cstring: 0x99e
+  __TEXT.__cstring: 0xa53
   __TEXT.__unwind_info: 0x148
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x448
+  __DATA_CONST.__objc_selrefs: 0x458
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__got: 0x108
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x640
+  __AUTH_CONST.__cfstring: 0x6a0
   __AUTH_CONST.__objc_const: 0xb30
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x88

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 58
-  Symbols:   369
-  CStrings:  88
+  Functions: 60
+  Symbols:   381
+  CStrings:  92
 
Symbols:
+ -[PUIProgressWindow _copyDisplayBootRotationNumberFromIORegistry]
+ -[PUIProgressWindow _isV68Device]
+ GCC_except_table20
+ _CFDataGetBytePtr
+ _CFDataGetLength
+ _CFDataGetTypeID
+ _CFGetTypeID
+ _IOObjectRelease
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryFromPath
+ _kIOMainPortDefault
+ _objc_msgSend$_copyDisplayBootRotationNumberFromIORegistry
+ _objc_msgSend$_isV68Device
- GCC_except_table18
CStrings:
+ "IODeviceTree:/product/display1"
+ "PUIProgressWindow ignoring unrecognized IORegistry boot rotation %@"
+ "PUIProgressWindow using IORegistry display boot rotation %@"
+ "display-boot-rotation"
```
