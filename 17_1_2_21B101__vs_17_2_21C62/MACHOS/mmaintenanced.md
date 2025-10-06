## mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

-127.0.0.0.0
-  __TEXT.__text: 0x1317c
-  __TEXT.__auth_stubs: 0xa50
+131.0.0.0.0
+  __TEXT.__text: 0x1322c
+  __TEXT.__auth_stubs: 0xa60
   __TEXT.__init_offsets: 0x4
   __TEXT.__oslogstring: 0x162b
-  __TEXT.__cstring: 0xf69
+  __TEXT.__cstring: 0xf67
   __TEXT.__const: 0x4e8
   __TEXT.__gcc_except_tab: 0x728
-  __TEXT.__unwind_info: 0x69c
+  __TEXT.__unwind_info: 0x6a4
   __TEXT.__eh_frame: 0x88
-  __DATA_CONST.__auth_got: 0x530
+  __DATA_CONST.__auth_got: 0x538
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__const: 0xae0
   __DATA_CONST.__cfstring: 0x60
   __DATA.__data: 0x188
-  __DATA.__common: 0x84
+  __DATA.__common: 0x8c
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: EA5CF97A-6837-3D63-9D01-C78322AF3D9E
+  UUID: 35A05A62-C556-3B71-A518-A87C04A2DC38
   Functions: 427
-  Symbols:   217
-  CStrings:  311
+  Symbols:   218
+  CStrings:  313
 
Symbols:
+ _fdopen
CStrings:
+ "Internal"
+ "SELECT DISTINCT addr FROM ecc_errors_v2 WHERE correctable = ? AND time >= ?;"
+ "SELECT DISTINCT addr FROM ecc_errors_v2 WHERE correctable = ?;"
+ "kern.osreleasetype"
- "SELECT addr, COUNT(*) FROM ecc_errors_v2 WHERE correctable = ? AND time >= ? GROUP BY addr;"
- "SELECT addr, COUNT(*) FROM ecc_errors_v2 WHERE correctable = ? GROUP BY addr;"

```
