## Seeding

> `/System/Library/PrivateFrameworks/Seeding.framework/Seeding`

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
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-129.0.0.0.0
-  __TEXT.__text: 0x1d3b8
-  __TEXT.__objc_methlist: 0x16a4
+130.0.0.0.0
+  __TEXT.__text: 0x1d62c
+  __TEXT.__objc_methlist: 0x16c4
   __TEXT.__const: 0x108
-  __TEXT.__gcc_except_tab: 0x540
+  __TEXT.__gcc_except_tab: 0x620
   __TEXT.__cstring: 0x21ef
-  __TEXT.__oslogstring: 0x31e2
-  __TEXT.__unwind_info: 0x850
+  __TEXT.__oslogstring: 0x3262
+  __TEXT.__unwind_info: 0x878
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1170
+  __DATA_CONST.__objc_selrefs: 0x1180
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x30
-  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__got: 0x2b8
   __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__cfstring: 0x1aa0
-  __AUTH_CONST.__objc_const: 0x2c30
+  __AUTH_CONST.__objc_const: 0x2c60
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0xc0
+  __DATA.__objc_ivar: 0xc4
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0x730

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 699
-  Symbols:   1628
-  CStrings:  600
+  Functions: 703
+  Symbols:   1635
+  CStrings:  601
 
Symbols:
+ -[SDBetaManager cacheLockToken]
+ -[SDBetaManager init]
+ -[SDBetaManager setCacheLockToken:]
+ GCC_except_table21
+ GCC_except_table28
+ GCC_except_table33
+ GCC_except_table79
+ GCC_except_table82
+ GCC_except_table97
+ _OBJC_IVAR_$_SDBetaManager._cacheLockToken
+ _objc_msgSend$cacheLockToken
+ _objc_msgSend$setCacheLockToken:
- GCC_except_table20
- GCC_except_table27
- GCC_except_table78
- GCC_except_table81
- GCC_except_table96
Functions:
+ -[SDBetaManager init]
~ -[SDBetaManager invalidateCache] : 160 -> 212
~ -[SDBetaManager isCacheValidForPlatforms:withMDMConfigurationDate:] : 604 -> 704
~ -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:language:completion:] : 2376 -> 2520
~ -[SDBetaManager cachePrograms:forPlatforms:] : 216 -> 272
~ -[SDBetaManager availableBetaProgramsForPlatforms:] : 412 -> 484
+ -[SDBetaManager cacheLockToken]
+ -[SDBetaManager postMigrationTasks]
~ -[SDBetaManager .cxx_destruct] : 80 -> 92
+ -[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:disableBuildPrefixMatching:language:completion:].cold.4
CStrings:
+ "Program cache was valid at check but empty at read for platforms [%ld]; a concurrent invalidate/reset raced the validity check."
```
