## AppUserDataMigrator

> `/System/Library/DataClassMigrators/AppUserDataMigrator.migrator/AppUserDataMigrator`

```diff

-1513.120.7.0.0
-  __TEXT.__text: 0x114c
-  __TEXT.__auth_stubs: 0x210
+1655.0.0.0.0
+  __TEXT.__text: 0x10dc
+  __TEXT.__auth_stubs: 0x260
   __TEXT.__objc_stubs: 0x420
   __TEXT.__objc_methlist: 0x7c
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x23d
+  __TEXT.__const: 0x68
+  __TEXT.__cstring: 0x240
   __TEXT.__objc_methname: 0x358
-  __TEXT.__objc_classname: 0x35
+  __TEXT.__objc_classname: 0x32
   __TEXT.__objc_methtype: 0x40
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x118
-  __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0x140
+  __DATA_CONST.__got: 0x90
   __DATA.__objc_const: 0x128
   __DATA.__objc_selrefs: 0x130
   __DATA.__objc_ivar: 0x4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E0A89609-3395-36E1-A2DB-A97F8B645FA9
+  UUID: 2DE2C88E-2D18-3822-AD03-A327691EC6E0
   Functions: 22
-  Symbols:   77
+  Symbols:   82
   CStrings:  76
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x4
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
Functions:
~ __CreateError : 68 -> 64
~ __CreateAndLogError : 68 -> 64
~ __CreateAndLogErrorV : 432 -> 408
~ __IsMalformedBundleError : 252 -> 236
~ _MICopyUnlocalizedDescriptionForContainerExtendedError : 108 -> 104
~ sub_1384 -> sub_1350 : 72 -> 76
~ sub_13d8 -> sub_13a8 : 800 -> 760
~ sub_16f8 -> sub_16a0 : 16 -> 20
~ sub_1708 -> sub_16b4 : 16 -> 20
~ _MIArrayFilteredToContainOnlyClass : 356 -> 352
~ _MIDictionaryContainsOnlyClasses : 228 -> 224
~ sub_1ac8 -> sub_1a70 : 152 -> 156
~ _MIStringifyObject : 152 -> 144
~ _MIArrayifyThing : 324 -> 312
~ _MICompareObjects : 124 -> 128
~ sub_1db8 -> sub_1d54 : 116 -> 108
~ sub_1e78 -> sub_1e0c : 284 -> 280

```
