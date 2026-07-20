## Ambient

> `/System/Library/PrivateFrameworks/Ambient.framework/Ambient`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`
- `__DATA.__data`

```diff

-107.0.0.0.0
-  __TEXT.__text: 0x5d2c
-  __TEXT.__objc_methlist: 0x9cc
+108.0.0.0.0
+  __TEXT.__text: 0x5da4
+  __TEXT.__objc_methlist: 0x9e4
   __TEXT.__const: 0x114
-  __TEXT.__cstring: 0x72a
+  __TEXT.__cstring: 0x771
   __TEXT.__gcc_except_tab: 0xd8
   __TEXT.__oslogstring: 0x5f2
   __TEXT.__unwind_info: 0x2f0

   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x800
+  __DATA_CONST.__objc_selrefs: 0x810
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x178
   __DATA_CONST.__got: 0x158
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x760
-  __AUTH_CONST.__objc_const: 0x1b18
+  __AUTH_CONST.__cfstring: 0x780
+  __AUTH_CONST.__objc_const: 0x1b48
   __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0xd0
+  __DATA.__objc_ivar: 0xd4
   __DATA.__data: 0x120
   __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0x280
+  __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 213
-  Symbols:   695
-  CStrings:  110
+  Functions: 215
+  Symbols:   699
+  CStrings:  112
 
Symbols:
+ -[AMAmbientDefaults motionDetectionWatchdogTimeoutSeconds]
+ -[AMAmbientDefaults setMotionDetectionWatchdogTimeoutSeconds:]
+ _OBJC_IVAR_$_AMAmbientDefaults._motionDetectionWatchdogTimeoutSeconds
+ _objc_msgSend$motionDetectionWatchdogTimeoutSeconds
CStrings:
+ "AMMotionDetectionWatchdogSeconds"
+ "motionDetectionWatchdogTimeoutSeconds"
```
