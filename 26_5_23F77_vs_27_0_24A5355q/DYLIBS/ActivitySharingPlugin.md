## ActivitySharingPlugin

> `/System/Library/Health/Plugins/ActivitySharingPlugin.bundle/ActivitySharingPlugin`

```diff

-2026.5.1.0.0
-  __TEXT.__text: 0xfd0
-  __TEXT.__auth_stubs: 0x140
-  __TEXT.__objc_methlist: 0x24c
+2027.0.11.0.0
+  __TEXT.__text: 0xe4c
+  __TEXT.__objc_methlist: 0x254
   __TEXT.__const: 0x10
   __TEXT.__oslogstring: 0x2bf
   __TEXT.__cstring: 0x592
-  __TEXT.__unwind_info: 0x98
-  __TEXT.__objc_classname: 0x5d
-  __TEXT.__objc_methname: 0x3cb
-  __TEXT.__objc_methtype: 0x1ac
-  __TEXT.__objc_stubs: 0x1a0
-  __DATA_CONST.__got: 0x100
+  __TEXT.__unwind_info: 0x90
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x160
+  __DATA_CONST.__objc_selrefs: 0x168
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xa8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x100
-  __AUTH_CONST.__objc_const: 0x2a0
+  __AUTH_CONST.__objc_const: 0x2a8
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0x180
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C56AFDE4-CC23-324E-BD9D-00AA69037CFE
+  UUID: 6349641C-4954-3E96-8D54-ADD4EDE7FC67
   Functions: 20
-  Symbols:   60
-  CStrings:  105
+  Symbols:   57
+  CStrings:  26
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
- _objc_release_x23
- _objc_release_x24
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x20
- _objc_retain_x21
- _objc_retain_x22
CStrings:
- "#16@0:8"
- "@\"<HDHealthDaemonExtension>\"24@0:8@\"<HDHealthDaemon>\"16"
- "@\"<HDProfileExtension>\"24@0:8@\"HDProfile\"16"
- "@\"NSArray\"16@0:8"
- "@\"NSArray\"24@0:8q16"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "ASActivitySharingPlugin"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"<HDHealthDaemon>\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "HDDatabaseSchemaProvider"
- "HDPlugin"
- "HDTaskServerClassProvider"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_createTableSQLStringForCompetitionLists"
- "_dropTableSQLStringForCompetitionLists"
- "_dropTableSQLStringForCompetitions"
- "addMigrationForSchema:toVersion:foreignKeyStatus:handler:"
- "arrayWithObjects:count:"
- "autorelease"
- "behavior"
- "class"
- "conformsToProtocol:"
- "currentSchemaVersionForProtectionClass:"
- "daemon"
- "databaseEntitiesForProtectionClass:"
- "debugDescription"
- "description"
- "executeSQL:error:bindingHandler:enumerationHandler:"
- "extensionForHealthDaemon:"
- "extensionForProfile:"
- "handleDatabaseObliteration"
- "hash"
- "init"
- "initWithProfile:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pluginIdentifier"
- "profileType"
- "protectedDatabase"
- "q24@0:8q16"
- "registerMigrationStepsForProtectionClass:migrator:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "schemaName"
- "self"
- "shouldLoadPluginForDaemon:"
- "stringWithFormat:"
- "superclass"
- "supportsActivitySharing"
- "taskServerClasses"
- "v16@0:8"
- "v32@0:8q16@\"HDDatabaseMigrator\"24"
- "v32@0:8q16@24"
- "zone"

```
