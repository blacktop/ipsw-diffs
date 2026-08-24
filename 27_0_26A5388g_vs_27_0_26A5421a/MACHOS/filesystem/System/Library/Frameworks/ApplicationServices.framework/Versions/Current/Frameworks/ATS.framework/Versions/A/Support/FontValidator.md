## FontValidator

> `/System/Library/Frameworks/ApplicationServices.framework/Versions/Current/Frameworks/ATS.framework/Versions/A/Support/FontValidator`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-600.0.0.0.0
-  __TEXT.__text: 0x126e0
+601.0.0.0.0
+  __TEXT.__text: 0x12754
   __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_stubs: 0xbe0
+  __TEXT.__objc_stubs: 0xc00
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x2a0
   __TEXT.__cstring: 0x42a9
-  __TEXT.__gcc_except_tab: 0xf58
+  __TEXT.__gcc_except_tab: 0xf7c
   __TEXT.__const: 0x16c
   __TEXT.__ustring: 0xdea
   __TEXT.__dlopen_cstrs: 0xf3
-  __TEXT.__objc_methname: 0xaea
+  __TEXT.__objc_methname: 0xb01
   __TEXT.__objc_classname: 0x51
   __TEXT.__objc_methtype: 0xdf
   __TEXT.__unwind_info: 0x4d0

   __DATA_CONST.__got: 0x168
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x740
-  __DATA.__objc_selrefs: 0x390
+  __DATA.__objc_selrefs: 0x398
   __DATA.__objc_ivar: 0x58
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x180

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 263
-  Symbols:   952
-  CStrings:  692
+  Symbols:   953
+  CStrings:  693
 
Symbols:
+ _objc_msgSend$URLByStandardizingPath
Functions:
~ __ZL21GetSimplifiedCTReportP14ProcessURLInfoP12NSDictionaryji : 3952 -> 4068
CStrings:
+ "3.0.2"
+ "URLByStandardizingPath"
- "3.0.1"
```
