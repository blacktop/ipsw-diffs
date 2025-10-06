## mount_apfs

> `/System/Library/Filesystems/apfs.fs/mount_apfs`

```diff

-2632.40.6.0.1
-  __TEXT.__text: 0x1b88
+2632.40.13.0.1
+  __TEXT.__text: 0x1ba0
   __TEXT.__auth_stubs: 0x420
-  __TEXT.__cstring: 0x75b
+  __TEXT.__cstring: 0x768
   __TEXT.__const: 0x10
   __TEXT.__unwind_info: 0x98
   __DATA_CONST.__auth_got: 0x210

   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 56F51991-61F8-317E-A06F-BEB6D0F78D3C
+  UUID: 034A8B85-6C6B-3D40-85AF-042101C74573
   Functions: 28
   Symbols:   78
-  CStrings:  116
+  CStrings:  117
 
Functions:
~ sub_100000954 : 3404 -> 3428
CStrings:
+ "[-o options] [-u UID] [-g GID] [-n] [-c [-r] | [-C]] [-s snapshot] [-P <im4p file> -M <im4m file> [-T <generic | brain>] [-E <generic | supplemental | pdi_nonce | mobile_asset | smac>]] <volume | device> <directory>"
+ "smac"
- "[-o options] [-u UID] [-g GID] [-n] [-c [-r] | [-C]] [-s snapshot] [-P <im4p file> -M <im4m file> [-T <generic | brain>] [-E <generic | supplemental | pdi_nonce | mobile_asset]] <volume | device> <directory>"

```
