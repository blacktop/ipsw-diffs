## continuitycaptured

> `/usr/libexec/continuitycaptured`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`

```diff

-764.42.8.0.0
-  __TEXT.__text: 0x2f8
-  __TEXT.__auth_stubs: 0x150
-  __TEXT.__objc_stubs: 0x80
+764.60.7.0.2
+  __TEXT.__text: 0x31c
+  __TEXT.__auth_stubs: 0x160
+  __TEXT.__objc_stubs: 0xa0
   __TEXT.__const: 0x10
   __TEXT.__oslogstring: 0x7f
   __TEXT.__cstring: 0xa6
-  __TEXT.__objc_methname: 0x43
+  __TEXT.__objc_methname: 0x52
   __TEXT.__unwind_info: 0x60
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xb0
-  __DATA_CONST.__got: 0x20
-  __DATA.__objc_selrefs: 0x20
+  __DATA_CONST.__auth_got: 0xb8
+  __DATA_CONST.__got: 0x28
+  __DATA.__objc_selrefs: 0x28
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 3
-  Symbols:   29
-  CStrings:  14
+  Symbols:   31
+  CStrings:  15
 
Symbols:
+ _OBJC_CLASS_$_CMContinuityCaptureCapabilitiesXPCServer
+ _objc_alloc_init
Functions:
~ sub_100000cb0 : 372 -> 408
CStrings:
+ "startListening"
```
