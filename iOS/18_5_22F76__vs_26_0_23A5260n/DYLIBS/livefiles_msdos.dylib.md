## livefiles_msdos.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_msdos.dylib`

```diff

-747.120.3.0.0
-  __TEXT.__text: 0x1996c
-  __TEXT.__auth_stubs: 0x420
+788.0.0.0.0
+  __TEXT.__text: 0x19b38
+  __TEXT.__auth_stubs: 0x430
   __TEXT.__const: 0x4da0
-  __TEXT.__oslogstring: 0x4561
-  __TEXT.__cstring: 0x6e0
+  __TEXT.__oslogstring: 0x458b
+  __TEXT.__cstring: 0x707
   __TEXT.__unwind_info: 0x270
   __TEXT.__objc_methname: 0xe2
   __TEXT.__objc_stubs: 0xe0
-  __DATA_CONST.__got: 0x18
+  __DATA_CONST.__got: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x218
+  __AUTH_CONST.__auth_got: 0x220
   __AUTH.__data: 0x140
   __DATA.__data: 0x165
   __DATA.__common: 0x18

   - /System/Library/PrivateFrameworks/LiveFS.framework/LiveFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0D50DA8B-B152-3E8C-BF5F-5075789A9DAB
+  UUID: AAD60028-6DAE-3804-9981-46AA66D541F2
   Functions: 185
-  Symbols:   347
-  CStrings:  423
+  Symbols:   349
+  CStrings:  427
 
Symbols:
+ __os_log_default
+ _memchr
Functions:
~ _FSOPS_CopyVolumeLabel : 120 -> 500
~ _msdos_sync_interal : 536 -> 572
~ _MSDOS_SetAttrToDirEntry : 2384 -> 2396
~ _MSDOS_GetAttrFromDirEntry : 1224 -> 1212
~ _FILEOPS_FreeUnusedPreAllocatedClusters : 672 -> 680
~ _MSDOS_Rename : 4092 -> 4084
~ _CONV_Unistr255ToUTF8 : 840 -> 836
~ _CONV_LabelUTF8ToUTF16LocalEncoding : 312 -> 348
~ _DIROPS_LookForDirEntry : 2608 -> 2620
CStrings:
+ "\"*+,./:;<=>?[\\]|"
+ "%s: Illegal character: %c"
+ "%s: empty label"
+ "FSOPS_CopyVolumeLabel"

```
