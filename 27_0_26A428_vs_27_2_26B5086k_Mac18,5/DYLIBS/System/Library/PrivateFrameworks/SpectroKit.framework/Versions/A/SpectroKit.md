## SpectroKit

> `/System/Library/PrivateFrameworks/SpectroKit.framework/Versions/A/SpectroKit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-11.11.5.0.0
-  __TEXT.__text: 0x1e46c
-  __TEXT.__objc_methlist: 0x1f50
-  __TEXT.__const: 0xf4
-  __TEXT.__oslogstring: 0x3f6
+11.11.7.0.0
+  __TEXT.__text: 0x1e678
+  __TEXT.__objc_methlist: 0x1f68
+  __TEXT.__const: 0x104
+  __TEXT.__oslogstring: 0x470
   __TEXT.__cstring: 0x2520
   __TEXT.__gcc_except_tab: 0xf08
   __TEXT.__ustring: 0xb2
-  __TEXT.__unwind_info: 0x8b8
+  __TEXT.__unwind_info: 0x8c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1440
+  __DATA_CONST.__objc_selrefs: 0x1450
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x3f8
-  __DATA_CONST.__got: 0x248
+  __DATA_CONST.__got: 0x250
   __AUTH_CONST.__const: 0x1d0
   __AUTH_CONST.__cfstring: 0x3660
-  __AUTH_CONST.__objc_const: 0x3118
+  __AUTH_CONST.__objc_const: 0x3148
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x898
   __AUTH_CONST.__objc_arrayobj: 0x78

   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x910
-  __DATA.__objc_ivar: 0x2a0
+  __DATA.__objc_ivar: 0x2a4
   __DATA.__data: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 699
-  Symbols:   1765
-  CStrings:  519
+  Functions: 703
+  Symbols:   1773
+  CStrings:  521
 
Symbols:
+ -[Spectro serialLock]
+ -[Spectro setSerialLock:]
+ OBJC_IVAR_$_Spectro._serialLock
+ _OBJC_CLASS_$_NSLock
+ _cfsetspeed
+ _objc_msgSend$setSerialLock:
+ _serialSetBaudRate
+ serialSetBaudRate
CStrings:
+ "97"
+ "serialSetBaudRate: tcgetattr failed - %{public}s(%{public}d)"
+ "serialSetBaudRate: tcsetattr failed - %{public}s(%{public}d)"
- "96"
```
