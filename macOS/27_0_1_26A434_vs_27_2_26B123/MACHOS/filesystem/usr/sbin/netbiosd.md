## netbiosd

> `/usr/sbin/netbiosd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-676.0.0.0.0
-  __TEXT.__text: 0x26f50
+682.0.0.0.0
+  __TEXT.__text: 0x27038
   __TEXT.__auth_stubs: 0xfc0
   __TEXT.__init_offsets: 0x18
   __TEXT.__const: 0x758
   __TEXT.__gcc_except_tab: 0x1710
-  __TEXT.__oslogstring: 0x16b2
-  __TEXT.__cstring: 0xf2ca
+  __TEXT.__oslogstring: 0x171d
+  __TEXT.__cstring: 0xf2de
   __TEXT.__unwind_info: 0x11f8
   __DATA_CONST.__const: 0x7c90
   __DATA_CONST.__cfstring: 0x340

   - /usr/lib/libc++.1.dylib
   Functions: 758
   Symbols:   1279
-  CStrings:  2319
+  CStrings:  2322
 
Functions:
~ __ZN3smb19insert_utf16_stringERK10oem_stringRPhS3_j : 940 -> 1172
CStrings:
+ "%s: Output buffer way too small, ndestbytes: %td"
+ "%s: numUniChars (%zu) exceeds numDestChars (%zu) for '%s'"
+ "insert_utf16_string"
```
