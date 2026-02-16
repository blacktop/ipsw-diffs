## FinishRestoreFromBackup

> `/usr/libexec/FinishRestoreFromBackup`

```diff

-2899.80.3.0.0
-  __TEXT.__text: 0x2e98
-  __TEXT.__auth_stubs: 0x4f0
+2969.100.18.0.0
+  __TEXT.__text: 0x2dd0
+  __TEXT.__auth_stubs: 0x500
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x1757
+  __TEXT.__cstring: 0x168d
   __TEXT.__unwind_info: 0xe8
-  __DATA_CONST.__auth_got: 0x278
-  __DATA_CONST.__got: 0x50
+  __DATA_CONST.__auth_got: 0x280
+  __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x14c0
-  __DATA_CONST.__cfstring: 0x80
+  __DATA_CONST.__cfstring: 0x20
   __DATA.__bss: 0x288
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/MobileObliteration.framework/MobileObliteration
   - /usr/lib/libSystem.B.dylib
-  UUID: 08FCEE6A-A728-34A3-88EE-821ED12B634A
-  Functions: 42
-  Symbols:   94
-  CStrings:  270
+  UUID: 36D8F04C-FB2E-3EDC-ABEA-3AB7491FF8C6
+  Functions: 51
+  Symbols:   96
+  CStrings:  258
 
Symbols:
+ _CFDictionaryCreateMutable
+ _CFDictionarySetValue
+ _Mobile_Obliterate
+ _kObliterationTypeKey
+ _kObliterationTypeMarkDirect
- _IOMainPort
- _IORegistryEntrySetCFProperty
- _bootstrap_port
CStrings:
- "%s setting the property %s to value %s"
- "0"
- "Could not get main port\n"
- "Could not get options entry from the device tree\n"
- "Failed"
- "IODeviceTree:/options"
- "IONVRAM-FORCESYNCNOW-PROPERTY"
- "Succeeded"
- "oblit-inprogress"

```
