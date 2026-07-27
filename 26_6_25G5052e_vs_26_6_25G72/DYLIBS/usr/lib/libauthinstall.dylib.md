## libauthinstall.dylib

> `/usr/lib/libauthinstall.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__auth_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__objc_classrefs`
- `__DATA.__objc_superrefs`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-1104.120.4.0.0
-  __TEXT.__text: 0x9f490
+1104.160.1.0.1
+  __TEXT.__text: 0x9f5c0
   __TEXT.__auth_stubs: 0x1ad0
   __TEXT.__objc_methlist: 0x262c
-  __TEXT.__cstring: 0x217da
-  __TEXT.__const: 0xc1db
+  __TEXT.__cstring: 0x217de
+  __TEXT.__const: 0xc23b
   __TEXT.__gcc_except_tab: 0x2a88
   __TEXT.__dlopen_cstrs: 0x63
   __TEXT.__oslogstring: 0x53c
-  __TEXT.__unwind_info: 0x26c8
+  __TEXT.__unwind_info: 0x26e8
   __TEXT.__eh_frame: 0xb4
   __TEXT.__objc_classname: 0x901
   __TEXT.__objc_methname: 0x2a4a

   - /usr/lib/libz.1.dylib
   - /usr/lib/updaters/libAppleTconUARPUpdater.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  Functions: 3681
-  Symbols:   5401
+  Functions: 3682
+  Symbols:   5402
   CStrings:  5599
 
Symbols:
+ _AMAuthInstallErrorFromAMSupportError
CStrings:
+ "libauthinstall-1104.160.1.0.1"
- "libauthinstall-1104.120.4"
```
