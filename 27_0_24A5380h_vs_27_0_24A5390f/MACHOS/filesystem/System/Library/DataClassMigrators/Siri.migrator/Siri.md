## Siri

> `/System/Library/DataClassMigrators/Siri.migrator/Siri`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-3600.68.39.1.1
-  __TEXT.__text: 0x3aec
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0x19c
-  __TEXT.__const: 0x2c
-  __TEXT.__cstring: 0x855
-  __TEXT.__oslogstring: 0x928
+3600.68.45.0.0
+  __TEXT.__text: 0x3c1c
+  __TEXT.__auth_stubs: 0x460
+  __TEXT.__objc_stubs: 0xb60
+  __TEXT.__objc_methlist: 0x1a8
+  __TEXT.__const: 0x34
+  __TEXT.__cstring: 0x861
+  __TEXT.__oslogstring: 0x966
   __TEXT.__objc_classname: 0xd
-  __TEXT.__objc_methname: 0x8e2
+  __TEXT.__objc_methname: 0x940
   __TEXT.__objc_methtype: 0x39
-  __TEXT.__unwind_info: 0xc8
+  __TEXT.__unwind_info: 0xd0
   __DATA_CONST.__const: 0x10
-  __DATA_CONST.__cfstring: 0x620
+  __DATA_CONST.__cfstring: 0x600
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x230
+  __DATA_CONST.__auth_got: 0x238
   __DATA_CONST.__got: 0x130
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x2d0
+  __DATA.__objc_selrefs: 0x300
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 36
-  Symbols:   119
-  CStrings:  215
+  Functions: 37
+  Symbols:   120
+  CStrings:  222
 
Symbols:
+ _OBJC_CLASS_$_APApplication
+ _objc_release_x26
+ _objc_retainAutoreleaseReturnValue
- _kTCCServiceSiri
- _objc_retain_x27
CStrings:
+ "%s AppProtection: locked=%lu."
+ "%s Failed to set TCC denial for bundle %@. [sources: ShowContent=%@, ShowApp=%@, Locked=%@]"
+ "%s Marked %@ as denied in kTCCServiceSiriAccess. [sources: ShowContent=%@, ShowApp=%@, Locked=%@]"
+ "%s Source counts — Show-Content-off: %lu, Show-App-off: %lu, Locked: %lu, Hidden (excluded): %lu, union to migrate: %lu."
+ "-[SiriMigrator _bundleIdsWithLockedApps]"
+ "_bundleIdsWithHiddenApps"
+ "_bundleIdsWithLockedApps"
+ "allObjects"
+ "hiddenAppBundleIdentifiers"
+ "kTCCServiceSiriAccess"
+ "lockedAppBundleIdentifiers"
+ "minusSet:"
+ "set"
- "%s Failed to set TCC denial for bundle %@. [sources: LFTA=%@, ShowContent=%@, ShowApp=%@]"
- "%s Marked %@ as denied in kTCCServiceSiri. [sources: LFTA=%@, ShowContent=%@, ShowApp=%@]"
- "%s Source counts — LFTA-off: %lu, Show-Content-off: %lu, Show-App-off: %lu, union to migrate: %lu."
- "SiriCanLearnFromAppBlacklist"
- "_bundleIdsWithLearnFromAppDisabled"
- "com.apple.suggestions"
```
