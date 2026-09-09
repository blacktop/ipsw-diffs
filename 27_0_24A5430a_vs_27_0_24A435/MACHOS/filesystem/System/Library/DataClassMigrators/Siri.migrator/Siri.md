## Siri

> `/System/Library/DataClassMigrators/Siri.migrator/Siri`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-3600.68.61.11.9
-  __TEXT.__text: 0x3d14
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_stubs: 0xb80
-  __TEXT.__objc_methlist: 0x1b4
+3600.68.61.11.11
+  __TEXT.__text: 0x3f80
+  __TEXT.__auth_stubs: 0x470
+  __TEXT.__objc_stubs: 0xbc0
+  __TEXT.__objc_methlist: 0x1d0
   __TEXT.__const: 0x34
-  __TEXT.__cstring: 0x894
-  __TEXT.__oslogstring: 0x987
+  __TEXT.__cstring: 0x90c
+  __TEXT.__oslogstring: 0xa79
   __TEXT.__objc_classname: 0xd
-  __TEXT.__objc_methname: 0x963
-  __TEXT.__objc_methtype: 0x39
-  __TEXT.__unwind_info: 0xd0
+  __TEXT.__objc_methname: 0x9d3
+  __TEXT.__objc_methtype: 0x47
+  __TEXT.__unwind_info: 0xd8
   __DATA_CONST.__const: 0x10
-  __DATA_CONST.__cfstring: 0x640
+  __DATA_CONST.__cfstring: 0x680
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x230
+  __DATA_CONST.__auth_got: 0x240
   __DATA_CONST.__got: 0x130
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x308
+  __DATA.__objc_selrefs: 0x318
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 38
-  Symbols:   119
-  CStrings:  225
+  Functions: 40
+  Symbols:   121
+  CStrings:  234
 
Symbols:
+ _AFIsLinwoodUserSettingOn
+ __AFPreferencesSiriDataSharingOptInStatusVersionWithContext
CStrings:
+ "%s Already performed. Skipping."
+ "%s Opting out Siri Data Sharing for Siri AI user at opt-in version 2.0 (version left unchanged)."
+ "%s hasSiriAIEnabled=%{BOOL}d optInStatusVersion=%ld — cohort does not apply. Marking complete without writing."
+ "-[SiriMigrator _performSiriAIDataSharingOptOutV2IfNeeded]"
+ "B28@0:8B16Q20"
+ "SiriAIDataSharingOptOutV2Completed"
+ "SiriMigratorSiriAIOptOutV2"
+ "_performSiriAIDataSharingOptOutV2IfNeeded"
+ "_shouldOptOutSiriAIDataSharingForHasSiriAIEnabled:optInStatusVersion:"
```
