## SiriAppAccessMigrator

> `/System/Library/CoreServices/SiriAppAccessMigrator`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`

```diff

-3600.68.61.14.6
-  __TEXT.__text: 0xf34
-  __TEXT.__auth_stubs: 0x1f0
-  __TEXT.__objc_stubs: 0x120
+3605.23.1.4.1
+  __TEXT.__text: 0x10dc
+  __TEXT.__auth_stubs: 0x200
+  __TEXT.__objc_stubs: 0x160
   __TEXT.__const: 0x40
-  __TEXT.__oslogstring: 0x64b
-  __TEXT.__cstring: 0x180
-  __TEXT.__objc_methname: 0x8e
+  __TEXT.__oslogstring: 0x752
+  __TEXT.__cstring: 0x1f2
+  __TEXT.__objc_methname: 0xbc
   __TEXT.__unwind_info: 0x70
   __DATA_CONST.__const: 0x60
-  __DATA_CONST.__cfstring: 0x200
+  __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x100
-  __DATA_CONST.__got: 0x40
-  __DATA.__objc_selrefs: 0x48
+  __DATA_CONST.__auth_got: 0x108
+  __DATA_CONST.__got: 0x48
+  __DATA.__objc_selrefs: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/AssistantServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 5
-  Symbols:   45
-  CStrings:  50
+  Symbols:   47
+  CStrings:  59
 
Symbols:
+ _OBJC_CLASS_$_NSDictionary
+ _TCCAccessReset
Functions:
~ sub_100000a40 : 2976 -> 3400
CStrings:
+ "AppAccessExclusionListMigrationPerformedV2"
+ "Failed to reset kTCCServiceSiriAccess entries. Proceeding with migration anyway (writes are idempotent)."
+ "Pre-migration reset triggered (V1=%{BOOL}d, Linwood=%{BOOL}d). Resetting all kTCCServiceSiriAccess entries."
+ "SiriAvailability"
+ "Successfully reset kTCCServiceSiriAccess entries."
+ "com.apple.assistant.backedup"
+ "desiredOrchestrationMode"
+ "objectForKeyedSubscript:"
+ "unsignedIntegerValue"
```
