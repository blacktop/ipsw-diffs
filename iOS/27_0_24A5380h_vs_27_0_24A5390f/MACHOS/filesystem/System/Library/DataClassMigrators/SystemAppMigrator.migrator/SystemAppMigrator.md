## SystemAppMigrator

> `/System/Library/DataClassMigrators/SystemAppMigrator.migrator/SystemAppMigrator`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1663.0.0.0.1
-  __TEXT.__text: 0x7d38
+1673.0.0.0.0
+  __TEXT.__text: 0x8454
   __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_stubs: 0x16c0
-  __TEXT.__objc_methlist: 0x62c
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x2cb1
-  __TEXT.__gcc_except_tab: 0x1b8
-  __TEXT.__objc_methname: 0x1ec0
+  __TEXT.__objc_stubs: 0x1780
+  __TEXT.__objc_methlist: 0x644
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x3029
+  __TEXT.__gcc_except_tab: 0x1e4
+  __TEXT.__objc_methname: 0x1f99
   __TEXT.__objc_classname: 0xa6
-  __TEXT.__objc_methtype: 0x3cf
+  __TEXT.__objc_methtype: 0x3df
   __TEXT.__oslogstring: 0x142
-  __TEXT.__unwind_info: 0x1f0
-  __DATA_CONST.__const: 0x328
-  __DATA_CONST.__cfstring: 0x1660
+  __TEXT.__unwind_info: 0x208
+  __DATA_CONST.__const: 0x350
+  __DATA_CONST.__cfstring: 0x17e0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__auth_got: 0x2e0
   __DATA_CONST.__got: 0x1a0
   __DATA.__objc_const: 0x880
-  __DATA.__objc_selrefs: 0x750
+  __DATA.__objc_selrefs: 0x780
   __DATA.__objc_ivar: 0x50
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x120

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 129
-  Symbols:   182
-  CStrings:  545
+  Functions: 131
+  Symbols:   181
+  CStrings:  564
 
Symbols:
- _kMISValidationOptionAllowLaunchWarning
CStrings:
+ "B32@0:8^@16^@24"
+ "MISystemAppMigrator: Failed to load internal superseded apps from %@ : %@"
+ "MISystemAppMigrator: Found invalid key type %@ in superseded apps plist's '%@' dictionary"
+ "MISystemAppMigrator: Found invalid value type %@ in superseded apps plist's '%@' dictionary"
+ "MISystemAppMigrator: Internal superseded apps plist had array value for '%@' key that had non-string objects in it"
+ "MISystemAppMigrator: Internal superseded apps plist was malformed"
+ "MISystemAppMigrator: Internal superseded apps plist was missing '%@' key with a dictionary value"
+ "MISystemAppMigrator: Internal superseded apps plist was missing '%@' key with an array value"
+ "MISystemAppMigrator: Internal superseded apps plist was not a dictionary"
+ "MISystemAppMigrator: Using %lu additional superseded apps and %lu replaced apps additions found in internal additions plist"
+ "NULL"
+ "ReplacedAppsRequiringMatchingUninstallState"
+ "SupersededApps"
+ "_copyInternalSupersededAppAdditions:internalReplacedAppsRequiringMachingUninstallState:"
+ "addEntriesFromDictionary:"
+ "dictionaryWithContentsOfURL:error:"
+ "hasInternalContent"
+ "internalSupersededAppAdditionsPlistURL"
+ "unionSet:"
```
