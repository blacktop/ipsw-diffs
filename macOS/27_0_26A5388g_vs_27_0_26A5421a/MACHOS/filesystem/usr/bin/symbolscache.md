## symbolscache

> `/usr/bin/symbolscache`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__cfstring`

```diff

-64578.77.1.0.0
-  __TEXT.__text: 0xf4cc
+64578.82.2.0.0
+  __TEXT.__text: 0xfb8c
   __TEXT.__auth_stubs: 0x860
   __TEXT.__const: 0x36f
-  __TEXT.__gcc_except_tab: 0xa8c
-  __TEXT.__cstring: 0x1d3d
+  __TEXT.__gcc_except_tab: 0xb3c
+  __TEXT.__cstring: 0x1da2
   __TEXT.__oslogstring: 0x208
-  __TEXT.__unwind_info: 0x5e0
-  __DATA_CONST.__const: 0x578
+  __TEXT.__unwind_info: 0x608
+  __DATA_CONST.__const: 0x588
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__auth_got: 0x438
   __DATA_CONST.__got: 0xc0

   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/Versions/A/CoreSymbolication
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 289
+  Functions: 296
   Symbols:   165
-  CStrings:  231
+  CStrings:  240
 
CStrings:
+ "cpu_subtype"
+ "cpu_type"
+ "flags"
+ "has_dsym"
+ "metadata"
+ "region_count"
+ "source_info_count"
+ "symbol_count"
+ "text_length"
```
