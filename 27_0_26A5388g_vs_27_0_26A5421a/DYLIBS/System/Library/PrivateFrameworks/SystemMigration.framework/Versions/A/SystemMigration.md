## SystemMigration

> `/System/Library/PrivateFrameworks/SystemMigration.framework/Versions/A/SystemMigration`

```diff

-6164.0.5.0.0
-  __TEXT.__text: 0x1009c0
-  __TEXT.__objc_methlist: 0x10570
+6164.1.2.0.0
+  __TEXT.__text: 0x1009b8
+  __TEXT.__objc_methlist: 0x105a0
   __TEXT.__const: 0x214
-  __TEXT.__gcc_except_tab: 0x3910
-  __TEXT.__cstring: 0x232ca
+  __TEXT.__gcc_except_tab: 0x3924
+  __TEXT.__cstring: 0x2321a
   __TEXT.__oslogstring: 0x402
   __TEXT.__ustring: 0x147c
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0x1a
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x31f0
+  __TEXT.__unwind_info: 0x31f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xc38
-  __DATA_CONST.__objc_classlist: 0x5d8
+  __DATA_CONST.__const: 0xc58
+  __DATA_CONST.__objc_classlist: 0x5e0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8330
+  __DATA_CONST.__objc_selrefs: 0x8328
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x4b0
-  __DATA_CONST.__objc_arraydata: 0x6c8
-  __DATA_CONST.__got: 0xec0
+  __DATA_CONST.__objc_arraydata: 0x6b8
+  __DATA_CONST.__got: 0xec8
   __AUTH_CONST.__const: 0x1bd0
-  __AUTH_CONST.__cfstring: 0x19440
-  __AUTH_CONST.__objc_const: 0x16d78
+  __AUTH_CONST.__cfstring: 0x19480
+  __AUTH_CONST.__objc_const: 0x16e08
   __AUTH_CONST.__objc_intobj: 0x690
-  __AUTH_CONST.__objc_arrayobj: 0x450
+  __AUTH_CONST.__objc_arrayobj: 0x438
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x9a8
-  __AUTH.__objc_data: 0x3a10
+  __AUTH_CONST.__auth_got: 0x9a0
+  __AUTH.__objc_data: 0x3a60
   __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0x121c
   __DATA.__data: 0x1310

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5617
-  Symbols:   13004
-  CStrings:  4006
+  Functions: 5619
+  Symbols:   13009
+  CStrings:  4007
 
Symbols:
+ +[SMMigrationCookieModeTransformer allowsReverseTransformation]
+ +[SMMigrationCookieModeTransformer transformedValueClass]
+ -[SMMigrationCookieModeTransformer transformedValue:]
+ GCC_except_table71
+ GCC_except_table79
+ _OBJC_CLASS_$_SMMigrationCookieModeTransformer
+ _OBJC_METACLASS_$_SMMigrationCookieModeTransformer
+ __OBJC_$_CLASS_METHODS_SMMigrationCookieModeTransformer
+ __OBJC_$_INSTANCE_METHODS_SMMigrationCookieModeTransformer
+ __OBJC_CLASS_RO_$_SMMigrationCookieModeTransformer
+ __OBJC_METACLASS_RO_$_SMMigrationCookieModeTransformer
- -[SMPaths treatRosettaAsUserContent]
- GCC_except_table72
- GCC_except_table80
- GCC_except_table83
- _objc_msgSend$treatRosettaAsUserContent
- _rosetta_is_translation_available_on_volume
CStrings:
+ "BaseSystemShove"
+ "EraseAllContentsAndSettings"
+ "FAILED"
+ "OK"
+ "SMMigrationCookieModeTransformer"
+ "TemplateMigration"
+ "TemplateMigrationAndBaseSystemShove"
+ "[BOOT PREP] Boot-once failed: %@"
+ "[BOOT PREP] Boot-once set"
+ "[BOOT PREP] Boot-once timed out"
+ "[BOOT PREP] Failed to resolve APFS Preboot UUID"
+ "[BOOT PREP] Failed to write templateMigration cookie to '%s': %@"
+ "[BOOT PREP] Preparing BaseSystem boot with mode %@"
+ "[BOOT PREP] Result: boot-once=%@, cookie=%@, plist=%@"
+ "[BOOT PREP] Unsupported mode: %@"
+ "[BOOT PREP] Wrote templateMigration cookie: mode=%@, path='%@', prebootUUID=%@"
+ "[BOOT PREP] templateMigration cookie write %@"
+ "succeeded"
- "%@ in writing the basesystem cookie"
- "-[SMPaths treatRosettaAsUserContent]"
- "11.5"
- "Rosetta Status: Already installed on target."
- "Rosetta Status: No comparison (target) system during Migration. Assuming Rosetta content would be system content."
- "Rosetta Status: Source version can be migrated."
- "Rosetta Status: Source version is not migratable"
- "Rosetta Status: Upgrade/Update context - treating as system content for reaping."
- "Successful in blessing"
- "Template migration cookie with mode %lu has been successfully written to disk."
- "Unable to bless - %@"
- "Unable to bless - timedout"
- "Unable to determine APFS Preboot UUID."
- "Unable to write template migration cookie to: '%s'. %@"
- "Unsupported migration mode: %lu"
- "Unsusccessful"
- "[SMPaths] Found Rosetta receipt on source, classifying as user non-system receipt: %@"
```
