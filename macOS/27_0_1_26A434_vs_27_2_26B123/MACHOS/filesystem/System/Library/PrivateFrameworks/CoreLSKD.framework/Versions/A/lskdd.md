## lskdd

> `/System/Library/PrivateFrameworks/CoreLSKD.framework/Versions/A/lskdd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_protorefs`
- `__DATA.__objc_classrefs`
- `__DATA.__objc_superrefs`
- `__DATA.__objc_data`

```diff

 0.0.0.0.0
-  __TEXT.__text: 0xc6c5c8
-  __TEXT.__auth_stubs: 0x280
+  __TEXT.__text: 0xc6ad04
+  __TEXT.__auth_stubs: 0x290
   __TEXT.__objc_stubs: 0x680
   __TEXT.__objc_methlist: 0x100
   __TEXT.__const: 0x1acaa0

   __TEXT.__objc_methtype: 0x18b
   __TEXT.__objc_methname: 0x5b4
   __TEXT.__info_plist: 0x4c8
-  __TEXT.__unwind_info: 0x5e8
+  __TEXT.__unwind_info: 0x5e0
   __TEXT.__eh_frame: 0x1f0
-  __DATA_CONST.__const: 0x52ae0
+  __DATA_CONST.__const: 0x52e80
   __DATA_CONST.__cfstring: 0x100
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x150
+  __DATA_CONST.__auth_got: 0x158
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x160

   __DATA.__objc_superrefs: 0x8
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x2648
+  __DATA.__data: 0x2638
   __DATA.__bss: 0x60
-  __DATA.__common: 0x1808
+  __DATA.__common: 0x1810
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 387
-  Symbols:   208
+  Symbols:   209
   CStrings:  108
 
Symbols:
+ _objc_retain
```
