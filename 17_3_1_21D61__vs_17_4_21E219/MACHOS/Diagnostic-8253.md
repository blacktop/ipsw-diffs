## Diagnostic-8253

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8253.appex/Diagnostic-8253`

```diff

-27.0.0.0.0
-  __TEXT.__text: 0x11694
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_stubs: 0x700
+32.0.0.0.0
+  __TEXT.__text: 0x11674
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_stubs: 0x6c0
   __TEXT.__objc_methlist: 0xe0
-  __TEXT.__gcc_except_tab: 0x1d08
+  __TEXT.__gcc_except_tab: 0x1cc8
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x3725
+  __TEXT.__cstring: 0x3730
   __TEXT.__objc_classname: 0x1f
-  __TEXT.__objc_methname: 0x55f
+  __TEXT.__objc_methname: 0x54b
   __TEXT.__objc_methtype: 0x661
-  __TEXT.__unwind_info: 0x5a0
+  __TEXT.__unwind_info: 0x580
   __TEXT.__eh_frame: 0x60
-  __DATA_CONST.__auth_got: 0x330
+  __DATA_CONST.__auth_got: 0x338
   __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__const: 0x4d8
-  __DATA_CONST.__cfstring: 0x2c60
+  __DATA_CONST.__cfstring: 0x2c80
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x48
   __DATA_CONST.__objc_intobj: 0x120
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA.__objc_const: 0x238
-  __DATA.__objc_selrefs: 0x1e8
-  __DATA.__objc_classrefs: 0x50
+  __DATA.__objc_selrefs: 0x1d8
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/H10ISPServices.framework/H10ISPServices
   - /System/Library/PrivateFrameworks/JasperDepth.framework/JasperDepth
   - /System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 76DB7E2C-4165-3A60-9081-465D45C5494C
-  Functions: 207
+  UUID: AFFA57CC-34C9-343D-8A15-D54BEE39CC28
+  Functions: 205
   Symbols:   338
   CStrings:  861
 
Symbols:
+ _MGCopyAnswer
- _OBJC_CLASS_$_UIDevice
CStrings:
+ "HWModelStr"
- "currentDevice"
- "name"

```
