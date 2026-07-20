## sandboxd

> `/usr/libexec/sandboxd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__dof_sandboxd`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-3051.0.30.0.0
+3051.0.42.0.2
   __TEXT.__text: 0x33a04
   __TEXT.__auth_stubs: 0x1600
   __TEXT.__objc_stubs: 0x27a0
   __TEXT.__objc_methlist: 0x10c4
   __TEXT.__const: 0x83b0
-  __TEXT.__cstring: 0x20068
+  __TEXT.__cstring: 0x200ab
   __TEXT.__oslogstring: 0x2512
   __TEXT.__objc_classname: 0x233
   __TEXT.__objc_methname: 0x2b70

   __DATA.__objc_selrefs: 0xc10
   __DATA.__objc_ivar: 0x144
   __DATA.__objc_data: 0x7d8
-  __DATA.__data: 0xe3d8
+  __DATA.__data: 0xe3f8
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xb10
   __DATA.__common: 0x30

   - /usr/lib/swift/libswiftos.dylib
   Functions: 991
   Symbols:   523
-  CStrings:  6023
+  CStrings:  6025
 
CStrings:
+ "CISP_CMD_CH_LED_STROBE_IVFM_SET"
+ "CISP_CMD_SET_SECURE_ISP_DEBUG_MODE"
+ "Jul 14 2026"
- "Jun 29 2026"
```
