## AppUserDataMigrator

> `/System/Library/DataClassMigrators/AppUserDataMigrator.migrator/AppUserDataMigrator`

```diff

-1513.80.6.0.0
-  __TEXT.__text: 0x10c4
-  __TEXT.__auth_stubs: 0x260
+1513.100.80.0.0
+  __TEXT.__text: 0x114c
+  __TEXT.__auth_stubs: 0x210
   __TEXT.__objc_stubs: 0x420
   __TEXT.__objc_methlist: 0x7c
   __TEXT.__const: 0x70

   __TEXT.__objc_methtype: 0x40
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x140
+  __DATA_CONST.__auth_got: 0x118
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x180

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DBCCCE22-663E-3D95-B6E4-3C26668B3B62
+  UUID: 2FB938E6-C6D3-3845-B0C9-260EE28C116D
   Functions: 22
-  Symbols:   82
+  Symbols:   77
   CStrings:  76
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x2
- _objc_retain_x23
- _objc_retain_x4
- _objc_retain_x8
Functions:
~ __CreateError : 64 -> 68
~ __CreateAndLogError : 64 -> 68
~ __CreateAndLogErrorV : 408 -> 432
~ __IsMalformedBundleError : 236 -> 252
~ _MICopyUnlocalizedDescriptionForContainerExtendedError : 104 -> 108
~ sub_13a4 -> sub_13d8 : 760 -> 800
~ _MIArrayContainsOnlyClass : 268 -> 272
~ _MIArrayFilteredToContainOnlyClass : 348 -> 356
~ _MIDictionaryContainsOnlyClasses : 224 -> 228
~ sub_1a5c -> sub_1ac8 : 156 -> 152
~ _MIStringifyObject : 144 -> 152
~ _MIArrayifyThing : 312 -> 324
~ _MICompareObjects : 128 -> 124
~ sub_1d40 -> sub_1db8 : 108 -> 116
~ sub_1df8 -> sub_1e78 : 276 -> 284

```
