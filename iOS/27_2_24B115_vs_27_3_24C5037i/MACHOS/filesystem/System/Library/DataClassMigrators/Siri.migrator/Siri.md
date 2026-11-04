## Siri

> `/System/Library/DataClassMigrators/Siri.migrator/Siri`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-3605.31.1.11.2
-  __TEXT.__text: 0x46bc
-  __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__objc_stubs: 0xc60
-  __TEXT.__objc_methlist: 0x218
+3610.11.2.0.0
+  __TEXT.__text: 0x4438
+  __TEXT.__auth_stubs: 0x4b0
+  __TEXT.__objc_stubs: 0xc40
+  __TEXT.__objc_methlist: 0x20c
   __TEXT.__const: 0x34
-  __TEXT.__cstring: 0xa14
-  __TEXT.__oslogstring: 0xf28
+  __TEXT.__cstring: 0x997
+  __TEXT.__oslogstring: 0xe4c
   __TEXT.__objc_classname: 0xd
-  __TEXT.__objc_methname: 0xbc6
+  __TEXT.__objc_methname: 0xb99
   __TEXT.__objc_methtype: 0x90
   __TEXT.__unwind_info: 0x118
   __DATA_CONST.__const: 0x10
-  __DATA_CONST.__cfstring: 0x740
+  __DATA_CONST.__cfstring: 0x700
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x268
+  __DATA_CONST.__auth_got: 0x260
   __DATA_CONST.__got: 0x138
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x340
+  __DATA.__objc_selrefs: 0x338
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 46
-  Symbols:   126
-  CStrings:  262
+  Functions: 45
+  Symbols:   125
+  CStrings:  253
 
Symbols:
+ __AFPublicPreferencesBoolValueForKey
- _AFIsLinwoodFFEnabled
- __AFSupportPreferencesBoolValueForKey
Functions:
~ sub_d0c : 512 -> 504
- sub_37ec
CStrings:
- "%s Device is not an internal install. Skipping."
- "%s Feature is not enabled. Skipping."
- "%s Marking one-time reset as complete."
- "%s One-time reset has already been performed. Skipping."
- "%s Setting opt-in value to unspecified."
- "-[SiriMigrator _performInternalSiriDataSharingResetIfNeeded]"
- "InternalSiriDataSharingResetPerformed"
- "SiriMigratorInternalReset"
- "_performInternalSiriDataSharingResetIfNeeded"
```
