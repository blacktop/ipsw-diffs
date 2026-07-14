## MediaToolbox

> `/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-  __TEXT.__text: 0xb85820
+  __TEXT.__text: 0xb85bb4
   __TEXT.__auth_stubs: 0xb510
   __TEXT.__objc_methlist: 0x250c
-  __TEXT.__const: 0x2ba50
-  __TEXT.__cstring: 0x6cbc1
-  __TEXT.__oslogstring: 0x5971a
+  __TEXT.__const: 0x2ba40
+  __TEXT.__cstring: 0x6cbd9
+  __TEXT.__oslogstring: 0x5975b
   __TEXT.__ustring: 0x23e
   __TEXT.__gcc_except_tab: 0x1154
   __TEXT.__dlopen_cstrs: 0x21e

   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x5aa0
-  __AUTH_CONST.__const: 0x418e8
+  __AUTH_CONST.__const: 0x41918
   __AUTH_CONST.__cfstring: 0x51060
   __AUTH_CONST.__objc_const: 0x4e48
   __AUTH_CONST.__objc_intobj: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 41259
-  Symbols:   43411
-  CStrings:  21742
+  Functions: 41262
+  Symbols:   43410
+  CStrings:  21744
 
Symbols:
+ _favd_evictExpiredFrames
+ _piqca_evictExpiredFrames
- _OUTLINED_FUNCTION_969
- _OUTLINED_FUNCTION_970
- _OUTLINED_FUNCTION_971
CStrings:
+ "<<<< FAVD >>>> %s: %p: evicting expired frames in image queue %p"
+ "favd_evictExpiredFrames"
```
