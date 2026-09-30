## coreaudiod

> `/usr/sbin/coreaudiod`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`

```diff

-481.0.0.0.0
-  __TEXT.__text: 0x1a314
-  __TEXT.__auth_stubs: 0xb20
+482.102.10.0.0
+  __TEXT.__text: 0x1a388
+  __TEXT.__auth_stubs: 0xb50
   __TEXT.__const: 0xbf0
-  __TEXT.__gcc_except_tab: 0x1cbc
-  __TEXT.__cstring: 0xdb7
+  __TEXT.__gcc_except_tab: 0x1cc0
+  __TEXT.__cstring: 0xe17
   __TEXT.__oslogstring: 0x51c
   __TEXT.__unwind_info: 0x978
   __DATA_CONST.__const: 0x10c0
   __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x598
+  __DATA_CONST.__auth_got: 0x5b0
   __DATA_CONST.__got: 0x118
   __DATA.__bss: 0x1a0
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 402
-  Symbols:   944
-  CStrings:  121
+  Symbols:   947
+  CStrings:  124
 
Symbols:
+ ___error
+ _confstr
+ _realpath$DARWIN_EXTSN
+ _sandbox_init_with_parameters
- _sandbox_init
Functions:
~ _main : 6284 -> 6400
CStrings:
+ "TMPDIR"
+ "failed to initialize temporary directory: %d\n"
+ "failed to resolve temporary directory: %d\n"
```
