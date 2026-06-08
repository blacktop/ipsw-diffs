## FaceTimeMigrator

> `/System/Library/DataClassMigrators/FaceTimeMigrator.migrator/FaceTimeMigrator`

```diff

-1969.600.51.2.5
-  __TEXT.__text: 0x11a4
-  __TEXT.__auth_stubs: 0x1b0
+1992.100.7.2.1
+  __TEXT.__text: 0x10e0
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__const: 0x58
   __TEXT.__cstring: 0xad
   __TEXT.__oslogstring: 0x24d
   __TEXT.__unwind_info: 0x70
-  __TEXT.__objc_classname: 0x19
-  __TEXT.__objc_methname: 0x196
-  __TEXT.__objc_methtype: 0x18
-  __TEXT.__objc_stubs: 0x200
-  __DATA_CONST.__got: 0x58
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x98
-  __AUTH_CONST.__auth_got: 0xe0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EBB9C208-BE49-3535-9F9B-DF5B343C3CA1
+  UUID: B01B577B-9E33-3157-ABA6-16B7F03DC9D2
   Functions: 6
-  Symbols:   46
-  CStrings:  59
+  Symbols:   47
+  CStrings:  36
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x25
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
Functions:
~ sub_239852c9c -> sub_23c47ac9c : 4036 -> 3896
~ sub_239853c60 -> sub_23c47bbd4 : 116 -> 112
~ sub_239853cd4 -> sub_23c47bc44 : 116 -> 112
~ sub_239853d48 -> sub_23c47bcb4 : 228 -> 180
CStrings:
- "@16@0:8"
- "B16@0:8"
- "RegistrationDataMigrator"
- "accountProperties"
- "accountPropertyForKey:"
- "accountTypeWithAccountTypeIdentifier:"
- "accountsWithAccountType:"
- "addObject:"
- "arrayWithObjects:"
- "boolValue"
- "countByEnumeratingWithState:objects:count:"
- "dataClassName"
- "didRestoreFromBackup"
- "estimatedDuration"
- "f16@0:8"
- "length"
- "objectForKey:"
- "performMigration"
- "registration"
- "removeAccount:withCompletionHandler:"
- "saveVerifiedAccount:withCompletionHandler:"
- "setAccountProperty:forKey:"
- "username"

```
