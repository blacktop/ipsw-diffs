## nt

> `/System/Library/PrivateFrameworks/nt.framework/Versions/A/nt`

```diff

-676.0.0.0.0
-  __TEXT.__text: 0x93e4
+682.0.0.0.0
+  __TEXT.__text: 0x94cc
   __TEXT.__const: 0x350
-  __TEXT.__cstring: 0xd3ef
-  __TEXT.__oslogstring: 0x20d
+  __TEXT.__cstring: 0xd403
+  __TEXT.__oslogstring: 0x278
   __TEXT.__gcc_except_tab: 0x294
   __TEXT.__unwind_info: 0x2d8
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libc++.1.dylib
   Functions: 112
   Symbols:   254
-  CStrings:  1848
+  CStrings:  1851
 
Functions:
~ __ZN3smb19insert_utf16_stringERK10oem_stringRPhS3_j : 940 -> 1172
CStrings:
+ "%s: Output buffer way too small, ndestbytes: %td"
+ "%s: numUniChars (%zu) exceeds numDestChars (%zu) for '%s'"
+ "insert_utf16_string"
```
