## diskarbitrationd

> `/usr/libexec/diskarbitrationd`

```diff

-490.82.1.0.0
-  __TEXT.__text: 0x19264
-  __TEXT.__auth_stubs: 0x1660
+490.100.19.502.1
+  __TEXT.__text: 0x18fe8
+  __TEXT.__auth_stubs: 0x1690
   __TEXT.__objc_stubs: 0x520
-  __TEXT.__objc_methlist: 0x8c
-  __TEXT.__cstring: 0x2bfa
+  __TEXT.__objc_methlist: 0xc8
+  __TEXT.__cstring: 0x2cbf
   __TEXT.__const: 0x78
   __TEXT.__oslogstring: 0xb
   __TEXT.__gcc_except_tab: 0xd4

   __TEXT.__objc_methname: 0x475
   __TEXT.__objc_methtype: 0x102
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x5c8
-  __DATA_CONST.__auth_got: 0xb40
-  __DATA_CONST.__got: 0x118
+  __TEXT.__unwind_info: 0x5b8
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
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x1d0
+  __DATA.__objc_const: 0x168
   __DATA.__objc_selrefs: 0x188
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x130
   __DATA.__bss: 0xda8
-  __DATA.__common: 0xc0
+  __DATA.__common: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 495
-  Symbols:   404
-  CStrings:  625
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
+ " added volume id = %@  mountpath %@ to danglingVolumeList."
+ "-s"
+ "Failed to copy argument"
+ "Failed to get mnt opts"
+ "Failed to malloc buffer"
+ "atime"
+ "automounted"
+ "browse"
+ "dangling device present ignore mountpoint %@"
+ "dangling mountpoint present ignore mountpoint %@"
+ "defwrite"
+ "exec"
+ "follow"
+ "gDADanglingVolumeList"
+ "groupquota"
+ "noperm"
+ "perm"
+ "protect"
+ "removed volume from danglingVolumeList, id = %@, success."
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
