## tailspind

> `usr/libexec/tailspind`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

 250.2.0.0.0
-  __TEXT.__text: 0xbf54
-  __TEXT.__auth_stubs: 0x9f0
+  __TEXT.__text: 0xbdc0
+  __TEXT.__auth_stubs: 0x9d0
   __TEXT.__objc_stubs: 0x620
   __TEXT.__objc_methlist: 0x1f4
   __TEXT.__const: 0x114
-  __TEXT.__cstring: 0xf6c
+  __TEXT.__cstring: 0xf53
   __TEXT.__objc_methname: 0xa14
-  __TEXT.__oslogstring: 0x2164
+  __TEXT.__oslogstring: 0x209a
   __TEXT.__objc_classname: 0x18
   __TEXT.__objc_methtype: 0xfb
   __TEXT.__gcc_except_tab: 0x238
-  __TEXT.__unwind_info: 0x380
-  __DATA_CONST.__auth_got: 0x508
+  __TEXT.__unwind_info: 0x378
+  __DATA_CONST.__auth_got: 0x4f8
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x3b8

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 241
-  Symbols:   200
-  CStrings:  373
+  Functions: 242
+  Symbols:   198
+  CStrings:  368
 
Symbols:
- __os_feature_enabled_impl
- _tailspin_buffer_size_set
CStrings:
- "Game mode disabled and detected default buffer size. Setting buffer size override"
- "Game mode enabled and detected non-default buffer size set by tailspin. Resetting buffer size"
- "IntelligenceFlow"
- "Linwood"
- "feature enabled: %{bool}d"
```
