## seputil

> `/usr/libexec/seputil`

```diff

-842.0.0.0.0
-  __TEXT.__text: 0x17608
+842.60.7.502.1
+  __TEXT.__text: 0x177a0
   __TEXT.__auth_stubs: 0xa40
   __TEXT.__const: 0xbfc
-  __TEXT.__cstring: 0x5d69
+  __TEXT.__cstring: 0x5eaf
   __TEXT.__oslogstring: 0x93
   __TEXT.__gcc_except_tab: 0x264
-  __TEXT.__unwind_info: 0x480
+  __TEXT.__unwind_info: 0x488
   __DATA_CONST.__auth_got: 0x528
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x158
   __DATA_CONST.__cfstring: 0x80
-  __DATA.__data: 0xbe0
+  __DATA.__data: 0xc00
   __DATA.__common: 0xc
   __DATA.__bss: 0x8bd
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 429
+  Functions: 430
   Symbols:   195
-  CStrings:  717
+  CStrings:  722
 
CStrings:
+ "\t\t--read-file              Test seputil file reading functionality, Requires infile and outfile\n"
+ "%!s(MISSING): Writing to output file failed in read file test\n"
+ "%!s(MISSING): fd_to_buf read more data than max permissible limit (max_len = %!d(MISSING))\n"
+ "%!s(MISSING): fd_to_buf returned NULL in read file test\n"
+ "%!s(MISSING): fd_to_buf returned false\n"
+ "input file too large in fd_to_buf (max size %!z(MISSING)u)\n"
+ "read failed in fd_to_buf\n"
+ "read-file"
+ "realloc failed in fd_to_buf for size %!z(MISSING)u\n"
- "can't read file\n"
- "file too large in fd_to_buf (was %!l(MISSING)lu, max %!l(MISSING)u)\n"
- "fstat failed\n"
- "malloc (%!l(MISSING)u) failed\n"

```
