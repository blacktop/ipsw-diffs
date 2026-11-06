## PhotosFileProvider

> `/System/Applications/Photos.app/Contents/PlugIns/PhotosFileProvider.appex/Contents/MacOS/PhotosFileProvider`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-911.0.134.0.0
-  __TEXT.__text: 0x2e1c
-  __TEXT.__auth_stubs: 0x1f0
+916.58.114.0.0
+  __TEXT.__text: 0x2f50
+  __TEXT.__auth_stubs: 0x200
   __TEXT.__objc_stubs: 0xac0
   __TEXT.__objc_methlist: 0x11c
   __TEXT.__const: 0x48
   __TEXT.__objc_methname: 0xa9b
-  __TEXT.__oslogstring: 0x64f
+  __TEXT.__oslogstring: 0x6a1
   __TEXT.__cstring: 0x27b
   __TEXT.__objc_classname: 0x40
   __TEXT.__objc_methtype: 0xdf

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0x100
-  __DATA_CONST.__got: 0x128
+  __DATA_CONST.__auth_got: 0x108
+  __DATA_CONST.__got: 0x130
   __DATA.__objc_const: 0x2e0
   __DATA.__objc_selrefs: 0x2e0
   __DATA.__objc_ivar: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 36
-  Symbols:   78
-  CStrings:  176
+  Symbols:   80
+  CStrings:  177
 
Symbols:
+ _PXAsyncShareFileProviderErrorDomain
+ _PXAsyncShareFileProviderErrorIsProvenanceFatal
Functions:
~ sub_100001508 : 572 -> 880
CStrings:
+ "[ContentProvenance] Item materialization failed with a fatal provenance error: %@"
```
