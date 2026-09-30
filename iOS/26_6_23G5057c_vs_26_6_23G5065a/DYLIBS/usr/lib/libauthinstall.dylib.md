## libauthinstall.dylib

> `/usr/lib/libauthinstall.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-  __TEXT.__text: 0x9d4f4
+  __TEXT.__text: 0x9d624
   __TEXT.__auth_stubs: 0x19f0
   __TEXT.__objc_methlist: 0x2a64
-  __TEXT.__cstring: 0x1f97c
-  __TEXT.__const: 0x6446
+  __TEXT.__cstring: 0x1f980
+  __TEXT.__const: 0x64a6
   __TEXT.__gcc_except_tab: 0x3710
   __TEXT.__dlopen_cstrs: 0x63
   __TEXT.__oslogstring: 0x53c
-  __TEXT.__unwind_info: 0x2910
+  __TEXT.__unwind_info: 0x2930
   __TEXT.__objc_classname: 0x8f6
   __TEXT.__objc_methname: 0x2fb8
   __TEXT.__objc_methtype: 0x952

   - /usr/lib/updaters/libAppleTconUARPUpdater.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  Functions: 3612
-  Symbols:   5259
+  Functions: 3613
+  Symbols:   5260
   CStrings:  5555
 
Symbols:
+ _AMAuthInstallErrorFromAMSupportError
CStrings:
+ "VinylRestore-146~1227"
+ "libauthinstall_device-1104.160.1.0.1"
- "VinylRestore-146~1195"
- "libauthinstall_device-1104.120.4"
```
