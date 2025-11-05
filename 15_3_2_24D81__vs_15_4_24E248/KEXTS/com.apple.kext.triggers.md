## com.apple.kext.triggers

> `com.apple.kext.triggers`

```diff

 322.0.0.0.0
   __TEXT.__cstring: 0x3ab
   __TEXT.__const: 0x48
-  __TEXT_EXEC.__text: 0x2760
+  __TEXT_EXEC.__text: 0x2840
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xf0
   __DATA.__bss: 0x3c
   __DATA_CONST.__auth_got: 0x210
-  __DATA_CONST.__got: 0x20
+  __DATA_CONST.__got: 0x18
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__kalloc_type: 0x80
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: F3F51BE3-AF4C-3F48-AC03-A9076388FFA2
+  UUID: CB57EE59-BB6A-3553-8450-F10C0B6B7847
   Functions: 35
   Symbols:   120
   CStrings:  21
Functions:
~ _trigger_resolve : 948 -> 952
~ _trigger_free : 204 -> 200
~ _unmount_triggered_mounts : 656 -> 672
~ _trigger_make_unresolved : 208 -> 204
~ _autofs_mount : 860 -> 912
~ _autofs_unmount : 584 -> 596
~ _autofs_readsubdir : 744 -> 776
~ _autofs_lookup : 728 -> 760
~ _autofs_mount_subtrigger : 820 -> 904

```
