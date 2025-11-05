## mtree

> `/usr/sbin/mtree`

```diff

-448.80.1.0.0
-  __TEXT.__text: 0x8b78
+457.100.3.0.0
+  __TEXT.__text: 0x8d70
   __TEXT.__auth_stubs: 0x7a0
   __TEXT.__const: 0x6f7
-  __TEXT.__cstring: 0x142f
-  __TEXT.__unwind_info: 0x1a8
+  __TEXT.__cstring: 0x14da
+  __TEXT.__unwind_info: 0x198
   __TEXT.__eh_frame: 0x40
   __DATA_CONST.__auth_got: 0x3d0
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x130
   __DATA_CONST.__cfstring: 0x20
-  __DATA.__data: 0x200
+  __DATA.__data: 0x300
   __DATA.__bss: 0x830
   __DATA.__common: 0x4f8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
-  UUID: 2A22F7DC-F16D-31AD-8788-904193B276C7
-  Functions: 140
+  UUID: 272C7CBA-24B6-363D-8B5A-1DE9D65103A8
+  Functions: 139
   Symbols:   138
-  CStrings:  266
+  CStrings:  268
 
CStrings:
+ " purgeable=%llu"
+ "%spurgeable expected %llu found %llu for file %s\n"
+ "get_purgeable_flags: fsctl failed for path <%s>"
+ "line %d, invalid value for purgeable: %s"
+ "purgeable"
+ "purgeable=%llu"
- "-"
- ".."
- "0"
- "1"

```
