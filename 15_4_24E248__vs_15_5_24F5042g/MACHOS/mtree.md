## mtree

> `/usr/sbin/mtree`

```diff

-457.100.3.0.0
-  __TEXT.__text: 0x8d70
+457.120.2.0.0
+  __TEXT.__text: 0x8dd8
   __TEXT.__auth_stubs: 0x7a0
   __TEXT.__const: 0x6f7
-  __TEXT.__cstring: 0x14da
+  __TEXT.__cstring: 0x15bc
   __TEXT.__unwind_info: 0x198
   __TEXT.__eh_frame: 0x40
   __DATA_CONST.__auth_got: 0x3d0

   - /usr/lib/libSystem.B.dylib
   Functions: 139
   Symbols:   138
-  CStrings:  267
+  CStrings:  273
 
CStrings:
+ "miss returned non-zero rrval: %d\n"
+ "mtree exiting with a non-zero status: %d"
+ "mtree_verifyspec returned a non-zero status: %d"
+ "mval returned a non-zero mval: %d\n"
+ "rval returned a non-zero rval: %d\n"
+ "vwalk failed: r1: %d and r2: %d\n"

```
