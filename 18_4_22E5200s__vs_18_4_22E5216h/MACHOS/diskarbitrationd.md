## diskarbitrationd

> `/usr/libexec/diskarbitrationd`

```diff

-490.100.12.0.0
-  __TEXT.__text: 0x19468
-  __TEXT.__auth_stubs: 0x1660
+490.100.19.502.1
+  __TEXT.__text: 0x18fe8
+  __TEXT.__auth_stubs: 0x1690
   __TEXT.__objc_stubs: 0x520
   __TEXT.__objc_methlist: 0xc8
-  __TEXT.__cstring: 0x2ce3
+  __TEXT.__cstring: 0x2cbf
   __TEXT.__const: 0x78
   __TEXT.__oslogstring: 0xb
   __TEXT.__gcc_except_tab: 0xd4

   __TEXT.__objc_methtype: 0x102
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x5b8
-  __DATA_CONST.__auth_got: 0xb40
-  __DATA_CONST.__got: 0x118
+  __DATA_CONST.__auth_got: 0xb58
+  __DATA_CONST.__got: 0x120
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xb10
-  __DATA_CONST.__cfstring: 0x1e60
+  __DATA_CONST.__const: 0xd48
+  __DATA_CONST.__cfstring: 0x1e00
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 492
-  Symbols:   404
-  CStrings:  630
+  - /usr/lib/libutil.dylib
+  Functions: 490
+  Symbols:   408
+  CStrings:  631
 
Symbols:
+ _CFStringFind
+ _CFStringGetMaximumSizeForEncoding
+ _CFStringTrimWhitespace
+ _freemntopts
+ _getmnt_silent
+ _getmntopts
- _CFStringCreateCopy
- _CFStringLowercase
CStrings:
+ "-s"
+ "Failed to copy argument"
+ "Failed to get mnt opts"
+ "Failed to malloc buffer"
+ "atime"
+ "automounted"
+ "browse"
+ "defwrite"
+ "exec"
+ "follow"
+ "groupquota"
+ "noperm"
+ "perm"
+ "protect"
+ "s"
+ "userquota"
- "  set disk encoding, id = %@, encoding = %d."
- "-o-e=%d"
- "-o="
- "-odev"
- "-oexec"
- "-onodev"
- "-onoexec"
- "-onoowners"
- "-onosuid"
- "-oowners"
- "-ordonly"
- "-orw"
- "-osuid"
- "no"
- "unable to set disk encoding, id = %s (status code 0x%08X)."

```
