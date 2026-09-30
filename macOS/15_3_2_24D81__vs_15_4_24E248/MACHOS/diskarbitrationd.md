## diskarbitrationd

> `/usr/libexec/diskarbitrationd`

```diff

-490.81.1.0.0
-  __TEXT.__text: 0x1b948
-  __TEXT.__auth_stubs: 0x1690
+490.100.20.0.1
+  __TEXT.__text: 0x1b5e0
+  __TEXT.__auth_stubs: 0x16d0
   __TEXT.__objc_stubs: 0x520
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x8c
-  __TEXT.__cstring: 0x314c
+  __TEXT.__objc_methlist: 0xc8
+  __TEXT.__cstring: 0x31cd
   __TEXT.__const: 0x78
   __TEXT.__oslogstring: 0xb
   __TEXT.__gcc_except_tab: 0xd8

   __TEXT.__objc_methname: 0x475
   __TEXT.__objc_methtype: 0x102
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x608
-  __DATA_CONST.__auth_got: 0xb58
+  __TEXT.__unwind_info: 0x5f8
+  __DATA_CONST.__auth_got: 0xb78
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xb58
-  __DATA_CONST.__cfstring: 0x1f00
+  __DATA_CONST.__const: 0xd90
+  __DATA_CONST.__cfstring: 0x1ea0
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
   __DATA.__data: 0x178
   __DATA.__bss: 0xde8
-  __DATA.__common: 0xc0
+  __DATA.__common: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/FSKit.framework/Versions/A/FSKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BFB50F85-EFAF-3BCC-BC20-F4BA2544A556
-  Functions: 527
-  Symbols:   412
-  CStrings:  917
+  - /usr/lib/libutil.dylib
+  UUID: 8BBF2970-B268-3B17-8E4B-30D357D26811
+  Functions: 521
+  Symbols:   416
+  CStrings:  918
 
Symbols:
+ _CFStringFind
+ _CFStringGetMaximumSizeForEncoding
+ _CFStringTrimWhitespace
+ _freemntopts
+ _getmnt_silent
+ _getmntopts
+ _renamex_np
- _CFStringCreateCopy
- _CFStringLowercase
- _SANDBOX_CHECK_NOFOLLOW
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
- " sandbox check for file-write-unlink failed on %@"
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
- "file-write-unlink"
- "no"
- "unable to set disk encoding, id = %s (status code 0x%08X)."

```
