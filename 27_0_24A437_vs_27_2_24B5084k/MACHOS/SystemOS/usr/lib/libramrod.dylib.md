## libramrod.dylib

> `/usr/lib/libramrod.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__objc_classrefs`
- `__DATA.__data`

```diff

-3696.0.12.0.3
-  __TEXT.__text: 0xeea98
+3696.40.10.0.0
+  __TEXT.__text: 0xee548
   __TEXT.__objc_methlist: 0x119c
-  __TEXT.__cstring: 0x2be81
-  __TEXT.__const: 0x79110
+  __TEXT.__cstring: 0x2beef
+  __TEXT.__const: 0x79130
   __TEXT.__gcc_except_tab: 0xb6c
   __TEXT.__oslogstring: 0xb92
-  __TEXT.__unwind_info: 0x2a08
+  __TEXT.__unwind_info: 0x2a10
   __TEXT.__eh_frame: 0x388
   __TEXT.__objc_stubs: 0x2920
-  __TEXT.__auth_stubs: 0x2b40
+  __TEXT.__auth_stubs: 0x2b50
   __TEXT.__objc_classname: 0x18b
   __TEXT.__objc_methname: 0x29fe
   __TEXT.__objc_methtype: 0xb58

   __DATA_CONST.__objc_selrefs: 0xcd8
   __DATA_CONST.__got: 0x2c0
   __AUTH_CONST.__const: 0x20b8
-  __AUTH_CONST.__cfstring: 0xc480
+  __AUTH_CONST.__cfstring: 0xc4c0
   __AUTH_CONST.__objc_const: 0x1ad0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x15a8
+  __AUTH_CONST.__auth_got: 0x15b0
   __AUTH.__objc_data: 0x5a0
   __AUTH.__data: 0x318
   __DATA.__objc_classrefs: 0x128

   - /usr/lib/libz.1.dylib
   - /usr/lib/updaters/libAppleTypeCRetimerUpdater.dylib
   - /usr/lib/updaters/libBMCMCUUpdater.dylib
-  Functions: 2871
-  Symbols:   1892
-  CStrings:  6386
+  Functions: 2874
+  Symbols:   1896
+  CStrings:  6388
 
Symbols:
+ _kImg4TagStr_srvc
+ _ramrod_manifest_tag_is_valid
+ _ramrod_manifest_tag_is_valid_string
+ _strnlen
CStrings:
+ "%s: %s: FUD image at index %ld is not a well-formed firmware tag"
+ "%s: %s: unable to determine the preboot path"
```
