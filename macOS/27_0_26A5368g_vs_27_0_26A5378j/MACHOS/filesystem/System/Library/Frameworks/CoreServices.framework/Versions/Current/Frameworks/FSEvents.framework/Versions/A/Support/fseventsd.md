## fseventsd

> `/System/Library/Frameworks/CoreServices.framework/Versions/Current/Frameworks/FSEvents.framework/Versions/A/Support/fseventsd`

```diff

-  __TEXT.__text: 0x173ec
+  __TEXT.__text: 0x175d0
   __TEXT.__auth_stubs: 0xe40
-  __TEXT.__cstring: 0x1019
+  __TEXT.__cstring: 0x1056
   __TEXT.__const: 0x1a8
   __TEXT.__oslogstring: 0x3308
   __TEXT.__unwind_info: 0x370

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 403
+  Functions: 404
   Symbols:   255
-  CStrings:  518
+  CStrings:  521
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__common : content changed
Symbols:
+ _basename_r
- _basename
CStrings:
+ "bname != NULL && bname_size > 0"
+ "com.apple.fseventsd.%s.%d.%s"
+ "nameForPID"
+ "system.unknown"
- "com.apple.fseventsd.%s.%d"

```
