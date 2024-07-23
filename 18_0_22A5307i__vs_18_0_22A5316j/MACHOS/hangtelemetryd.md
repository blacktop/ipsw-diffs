## hangtelemetryd

> `/usr/libexec/hangtelemetryd`

```diff

-323.0.0.0.0
-  __TEXT.__text: 0x1b20
-  __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_stubs: 0x280
+326.0.0.0.0
+  __TEXT.__text: 0x1aa0
+  __TEXT.__auth_stubs: 0x3c0
+  __TEXT.__objc_stubs: 0x240
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x1bf
-  __TEXT.__oslogstring: 0x4f9
+  __TEXT.__cstring: 0x1c4
+  __TEXT.__oslogstring: 0x520
   __TEXT.__info_plist: 0x453
-  __TEXT.__objc_methname: 0x198
-  __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__auth_got: 0x1f0
-  __DATA_CONST.__got: 0x68
+  __TEXT.__objc_methname: 0x171
+  __TEXT.__unwind_info: 0xa0
+  __DATA_CONST.__auth_got: 0x1e8
+  __DATA_CONST.__got: 0x60
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1f8
+  __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0xa0
+  __DATA.__objc_selrefs: 0x90
   __DATA.__data: 0x8
-  __DATA.__bss: 0x70
+  __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 29
-  Symbols:   80
-  CStrings:  67
+  Functions: 26
+  Symbols:   78
+  CStrings:  66
 
Symbols:
+ _sem_close
+ _sem_open
- _CFPreferencesCopyValue
- _OBJC_CLASS_$_NSString
- _objc_opt_isKindOfClass
- _objc_release_x24
CStrings:
+ "HTTelemetrySetRanThisBoot called twice"
+ "hangtelemetryd.onceatboot"
+ "sem_open() creation failed: %!{(MISSING)errno}d"
+ "sem_open() failed: %!{(MISSING)errno}d"
- "Unable to get boot UUID: %!{(MISSING)errno}d"
- "Unable to get boot session UUID"
- "isEqualToString:"
- "kern.bootsessionuuid"
- "stringWithUTF8String:"

```
