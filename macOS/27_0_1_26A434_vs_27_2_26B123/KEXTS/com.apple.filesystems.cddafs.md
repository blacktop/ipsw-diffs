## com.apple.filesystems.cddafs

> `com.apple.filesystems.cddafs`

```diff

-274.0.0.0.0
+276.40.1.0.0
   __TEXT.__cstring: 0x199
   __TEXT.__const: 0x968
-  __TEXT_EXEC.__text: 0x2994
-  __TEXT_EXEC.__auth_stubs: 0x4c0
+  __TEXT_EXEC.__text: 0x2a58
+  __TEXT_EXEC.__auth_stubs: 0x4d0
   __DATA.__data: 0x2d8
   __DATA.__bss: 0x8
   __DATA.__common: 0x8
   __DATA_CONST.__kalloc_type: 0x180
-  __DATA_CONST.__auth_got: 0x260
+  __DATA_CONST.__auth_got: 0x268
   __DATA_CONST.__got: 0x20
   Functions: 46
-  Symbols:   162
+  Symbols:   163
   CStrings:  24
 
Symbols:
+ CDDA_Mount.kalloc_type_view_355
+ CDDA_Unmount.kalloc_type_view_473
+ _vnode_recycle
- CDDA_Mount.kalloc_type_view_336
- CDDA_Unmount.kalloc_type_view_454
Functions:
~ _CreateBufferFromIORegistry : 592 -> 624
~ _DisposeBufferFromIORegistry : 24 -> 8
~ _CalculateSize : 248 -> 312
~ _ParseTOC : 608 -> 648
~ _CDDA_Mount : 676 -> 752
```
