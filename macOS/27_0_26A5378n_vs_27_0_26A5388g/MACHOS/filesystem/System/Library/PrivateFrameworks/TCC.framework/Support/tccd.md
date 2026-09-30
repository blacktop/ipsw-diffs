## tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-909.0.0.0.0
-  __TEXT.__text: 0x865b8
+910.0.0.0.0
+  __TEXT.__text: 0x86650
   __TEXT.__auth_stubs: 0x1600
   __TEXT.__objc_stubs: 0x9620
   __TEXT.__objc_methlist: 0x409c

   __TEXT.__const: 0x638
   __TEXT.__gcc_except_tab: 0x31a8
   __TEXT.__objc_methname: 0xf866
-  __TEXT.__oslogstring: 0xe38d
+  __TEXT.__oslogstring: 0xe415
   __TEXT.__objc_classname: 0x4ae
   __TEXT.__objc_methtype: 0x149f
   __TEXT.__unwind_info: 0x1568

   __DATA.__objc_data: 0xf50
   __DATA.__data: 0x348
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x364
-  __DATA.__common: 0x20
+  __DATA.__bss: 0x35c
+  __DATA.__common: 0x30
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2521
+  Functions: 2522
   Symbols:   502
-  CStrings:  5055
+  CStrings:  5056
 
CStrings:
+ "ManagedSettings: ignoring Location profile update for %{private}@ - disclosure already acknowledged, managed_overrides record preserved"
```
