## mount_apfs

> `/System/Library/Filesystems/apfs.fs/mount_apfs`

```diff

-2332.120.31.0.2
-  __TEXT.__text: 0x1c24
-  __TEXT.__auth_stubs: 0x430
-  __TEXT.__cstring: 0x7d8
+2632.0.15.0.1
+  __TEXT.__text: 0x1b88
+  __TEXT.__auth_stubs: 0x420
+  __TEXT.__cstring: 0x75b
   __TEXT.__const: 0x10
-  __TEXT.__unwind_info: 0x90
-  __DATA_CONST.__auth_got: 0x218
+  __TEXT.__unwind_info: 0x98
+  __DATA_CONST.__auth_got: 0x210
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x288
-  __DATA_CONST.__cfstring: 0x100
+  __DATA_CONST.__cfstring: 0xe0
   __DATA.__data: 0x210
   __DATA.__bss: 0x1000
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: F60AA40B-A608-3AAC-8464-C2D7450C88B1
+  UUID: BFC88574-B897-360A-BA40-D31AB0EF42F6
   Functions: 28
-  Symbols:   79
-  CStrings:  119
+  Symbols:   78
+  CStrings:  116
 
Symbols:
- _CFBooleanGetValue
Functions:
~ sub_100000954 : 3600 -> 3404
~ sub_10000177c -> sub_1000016b8 : 896 -> 332
~ sub_100001afc -> sub_100001804 : 332 -> 924
~ sub_100001ecc -> sub_100001e24 : 308 -> 320
CStrings:
+ ":cCg:M:o:P:rRnSs:u:E:T:"
+ "CACHE"
+ "[-o options] [-u UID] [-g GID] [-n] [-c [-r] | [-C]] [-s snapshot] [-P <im4p file> -M <im4m file> [-T <generic | brain>] [-E <generic | supplemental | pdi_nonce | mobile_asset]] <volume | device> <directory>"
- ":cCF:g:M:o:P:rRnSs:u:E:T:"
- "APFS Fusion is not guaranteed to work reliably on top of sparse images"
- "APFSComposited"
- "AppleAPFSContainerScheme"
- "[-o options] [-u UID] [-g GID] [-n] [-c [-r] | [-C|-F <tier2 device>]] [-s snapshot] [-P <im4p file> -M <im4m file> [-T <generic | brain>] [-E <generic | supplemental | pdi_nonce | mobile_asset]] <volume | device> <directory>"

```
