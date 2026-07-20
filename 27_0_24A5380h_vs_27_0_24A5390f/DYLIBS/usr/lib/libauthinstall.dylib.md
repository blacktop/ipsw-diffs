## libauthinstall.dylib

> `/usr/lib/libauthinstall.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-1155.0.3.0.0
-  __TEXT.__text: 0xb9248
+1155.0.4.0.0
+  __TEXT.__text: 0xb9544
   __TEXT.__objc_methlist: 0x2a64
   __TEXT.__cstring: 0x1ff7d
-  __TEXT.__const: 0x6456
-  __TEXT.__gcc_except_tab: 0x4560
+  __TEXT.__const: 0x64b6
+  __TEXT.__gcc_except_tab: 0x45bc
   __TEXT.__dlopen_cstrs: 0x63
   __TEXT.__oslogstring: 0x63da
-  __TEXT.__unwind_info: 0x2bf8
+  __TEXT.__unwind_info: 0x2c28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   - /usr/lib/updaters/libAppleTconUARPUpdater.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  Functions: 3796
-  Symbols:   5291
+  Functions: 3794
+  Symbols:   5293
   CStrings:  4747
 
Symbols:
+ _AMAuthInstallErrorFromAMSupportError
+ __ZN11ACFULogging14getUpdaterNameEv
CStrings:
+ "HelsinkiRestore-58.0.44"
+ "VinylRestore-178~3428"
+ "libauthinstall_device-1155.0.4"
- "HelsinkiRestore-58.0.42"
- "VinylRestore-178~2206"
- "libauthinstall_device-1155.0.3"
```
