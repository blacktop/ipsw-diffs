## Diagnostic-8079

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8079.appex/Diagnostic-8079`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1374.0.5.0.0
-  __TEXT.__text: 0x8944
+1374.0.27.0.0
+  __TEXT.__text: 0x8b58
   __TEXT.__auth_stubs: 0x550
   __TEXT.__objc_stubs: 0x2400
   __TEXT.__objc_methlist: 0xb94

   __TEXT.__objc_methtype: 0x36f
   __TEXT.__const: 0x88
   __TEXT.__gcc_except_tab: 0x118
-  __TEXT.__oslogstring: 0xabc
+  __TEXT.__oslogstring: 0xbf7
   __TEXT.__unwind_info: 0x228
   __DATA_CONST.__const: 0x260
   __DATA_CONST.__cfstring: 0xc80

   - /usr/lib/libobjc.A.dylib
   Functions: 240
   Symbols:   185
-  CStrings:  692
+  CStrings:  700
 
Functions:
~ sub_1000085ac : 280 -> 400
~ sub_100008b2c -> sub_100008ba4 : 756 -> 848
~ sub_100008e20 -> sub_100008ef4 : 156 -> 228
~ sub_100008ec4 -> sub_100008fe0 : 472 -> 592
~ sub_10000909c -> sub_100009230 : 180 -> 308
CStrings:
+ "Device does not have Exclaves. Skipping stat capture."
+ "Display pipe stats captured"
+ "Exclaves is not supported, skipping status."
+ "Exclaves is supported."
+ "Platform has display pipe stats, preparing to capture"
+ "Retrieving display pipe stats..."
+ "Returning %lu stats for display pipe client"
+ "Starting display pipe stat capture"
```
