## appleh16camerad

> `/usr/libexec/appleh16camerad`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-6.201.0.0.0
-  __TEXT.__text: 0x8439c
+6.203.1.0.0
+  __TEXT.__text: 0x846e4
   __TEXT.__auth_stubs: 0x1fd0
   __TEXT.__objc_stubs: 0x1400
   __TEXT.__objc_methlist: 0x270
-  __TEXT.__gcc_except_tab: 0x2104
+  __TEXT.__gcc_except_tab: 0x2118
   __TEXT.__const: 0x2dc0
-  __TEXT.__cstring: 0x8b97
-  __TEXT.__oslogstring: 0x5f4f
+  __TEXT.__cstring: 0x8bbe
+  __TEXT.__oslogstring: 0x5fb6
   __TEXT.__objc_methname: 0x1590
   __TEXT.__objc_classname: 0x88
   __TEXT.__objc_methtype: 0x1121
-  __TEXT.__unwind_info: 0x1f00
+  __TEXT.__unwind_info: 0x1f30
   __DATA_CONST.__const: 0xb710
   __DATA_CONST.__cfstring: 0x33a0
   __DATA_CONST.__objc_classlist: 0x18

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1702
+  Functions: 1713
   Symbols:   903
-  CStrings:  2037
+  CStrings:  2041
 
CStrings:
+ "%s - assistant failed to load setfiles: 0x%08x\n"
+ "%s: CloseInterfaceToSavageCam without a matching open\n"
+ "6.203.1"
+ "ISP_BuildAndLoadSetfile"
+ "LoadSetfiles"
- "6.201"
```
