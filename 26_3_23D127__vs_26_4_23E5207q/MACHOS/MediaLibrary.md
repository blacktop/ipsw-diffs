## MediaLibrary

> `/System/Library/DataClassMigrators/MediaLibrary.migrator/MediaLibrary`

```diff

-4025.400.4.0.0
-  __TEXT.__text: 0xa28
+4025.500.40.0.0
+  __TEXT.__text: 0xa5c
   __TEXT.__auth_stubs: 0x180
   __TEXT.__objc_stubs: 0x2c0
   __TEXT.__objc_methlist: 0x50
   __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x148
+  __TEXT.__gcc_except_tab: 0x130
   __TEXT.__cstring: 0xe8
   __TEXT.__objc_methname: 0x28d
   __TEXT.__oslogstring: 0x2db

   - /System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FB3BE541-D209-3C0F-A12B-43547159D408
+  UUID: F04EF409-FEEB-3691-8506-AFD89D606F08
   Functions: 7
   Symbols:   39
   CStrings:  67
Symbols:
+ _objc_retain_x19
+ _objc_retain_x20
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x8
Functions:
~ sub_c4c : 320 -> 324
~ sub_d8c -> sub_d90 : 1840 -> 1884
~ sub_14c8 -> sub_14f8 : 320 -> 324

```
