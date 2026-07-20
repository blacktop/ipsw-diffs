## Seeding

> `/System/Library/PrivateFrameworks/Seeding.framework/Versions/A/Seeding`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-129.0.0.0.0
-  __TEXT.__text: 0x22cb0
-  __TEXT.__objc_methlist: 0x197c
+130.0.0.0.0
+  __TEXT.__text: 0x22f4c
+  __TEXT.__objc_methlist: 0x199c
   __TEXT.__const: 0x120
-  __TEXT.__gcc_except_tab: 0x634
+  __TEXT.__gcc_except_tab: 0x714
   __TEXT.__cstring: 0x26c1
-  __TEXT.__oslogstring: 0x353f
-  __TEXT.__unwind_info: 0x9b0
+  __TEXT.__oslogstring: 0x35bf
+  __TEXT.__unwind_info: 0x9d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11e8
+  __DATA_CONST.__objc_selrefs: 0x11f8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x48
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x30
-  __DATA_CONST.__got: 0x2c0
+  __DATA_CONST.__got: 0x2c8
   __AUTH_CONST.__const: 0x10a0
   __AUTH_CONST.__cfstring: 0x1a60
-  __AUTH_CONST.__objc_const: 0x36f8
+  __AUTH_CONST.__objc_const: 0x3728
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xc8
+  __DATA.__objc_ivar: 0xcc
   __DATA.__data: 0x300
   __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0x730

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 821
-  Symbols:   1792
-  CStrings:  637
+  Functions: 825
+  Symbols:   1800
+  CStrings:  638
 
Symbols:
+ -[SDBetaManager cacheLockToken]
+ -[SDBetaManager init]
+ -[SDBetaManager setCacheLockToken:]
+ GCC_except_table101
+ GCC_except_table106
+ GCC_except_table125
+ GCC_except_table16
+ GCC_except_table37
+ GCC_except_table41
+ OBJC_IVAR_$_SDBetaManager._cacheLockToken
+ _objc_msgSend$cacheLockToken
+ _objc_msgSend$setCacheLockToken:
- GCC_except_table100
- GCC_except_table105
- GCC_except_table124
- GCC_except_table25
Functions:
+ -[SDBetaManager init]
~ -[SDBetaManager invalidateCache] : 164 -> 220
~ -[SDBetaManager isCacheValidForPlatforms:withMDMConfigurationDate:] : 652 -> 756
~ -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:language:completion:] : 2452 -> 2608
~ -[SDBetaManager cachePrograms:forPlatforms:] : 232 -> 292
~ -[SDBetaManager availableBetaProgramsForPlatforms:] : 420 -> 504
+ -[SDBetaManager cacheLockToken]
+ -[SDBetaManager postMigrationTasks]
~ -[SDBetaManager .cxx_destruct] : 80 -> 92
+ -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:language:completion:].cold.4
CStrings:
+ "Program cache was valid at check but empty at read for platforms [%ld]; a concurrent invalidate/reset raced the validity check."
```
