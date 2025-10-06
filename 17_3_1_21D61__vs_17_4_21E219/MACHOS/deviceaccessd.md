## deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

-200.10.0.0.0
+200.11.0.0.0
   __TEXT.__text: 0xccf0
   __TEXT.__auth_stubs: 0xad0
   __TEXT.__objc_stubs: 0x1480

   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0xc8
+  __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x8d8
   __DATA.__objc_selrefs: 0x5a0
-  __DATA.__objc_classrefs: 0xc8
-  __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x90
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x288

   - /System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E6DC4924-B9EF-33BB-B85C-E707C362FBEB
+  UUID: E5CB0CB0-1B86-3D26-A64E-73B2825E0B8A
   Functions: 150
   Symbols:   218
   CStrings:  661

```
