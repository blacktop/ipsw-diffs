## com.apple.filesystems.cddafs

> `com.apple.filesystems.cddafs`

```diff

 269.0.0.0.0
   __TEXT.__cstring: 0x191
   __TEXT.__const: 0x968
-  __TEXT_EXEC.__text: 0x28dc
+  __TEXT_EXEC.__text: 0x2994
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2d8
   __DATA.__bss: 0x8

   __DATA_CONST.__auth_got: 0x260
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__kalloc_type: 0x180
-  UUID: 4CD3924A-80AF-301E-BA9A-ABA8548BC775
-  Functions: 46
-  Symbols:   164
+  UUID: 8C433ED5-3069-3E24-98B6-CF306A2A3218
+  Functions: 44
+  Symbols:   163
   CStrings:  23
 
Symbols:
- AddDirectoryEntry.cold.1
Functions:
~ _CreateBufferFromIORegistry : 652 -> 648
~ _CreateNewCDDANode : 284 -> 288
~ _CalculateSize : 240 -> 260
~ _ParseTOC : 520 -> 552
~ _CDDA_Mount : 668 -> 672
~ _CDDA_VFSGetAttributes : 460 -> 480
~ _CDDA_Lookup : 412 -> 428
~ _CDDA_Read : 1112 -> 1152
~ _AddDirectoryEntry : 356 -> 364
~ _CDDA_PageIn : 1192 -> 1248
~ _CDDA_GetAttributes : 532 -> 568
~ _CDDA_Pathconf : 128 -> 112
- sub_fffffe000b97a3e8
~ _BuildCDAIFFHeader : 132 -> 144
- AddDirectoryEntry.cold.1

```
