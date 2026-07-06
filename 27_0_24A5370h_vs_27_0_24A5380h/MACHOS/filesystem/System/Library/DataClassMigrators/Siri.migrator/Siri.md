## Siri

> `/System/Library/DataClassMigrators/Siri.migrator/Siri`

```diff

-  __TEXT.__text: 0x2edc
-  __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_stubs: 0x8e0
-  __TEXT.__objc_methlist: 0x140
-  __TEXT.__const: 0x1c
-  __TEXT.__cstring: 0x717
-  __TEXT.__oslogstring: 0x5de
+  __TEXT.__text: 0x3aec
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_stubs: 0xaa0
+  __TEXT.__objc_methlist: 0x19c
+  __TEXT.__const: 0x2c
+  __TEXT.__cstring: 0x855
+  __TEXT.__oslogstring: 0x928
   __TEXT.__objc_classname: 0xd
-  __TEXT.__objc_methname: 0x72f
-  __TEXT.__objc_methtype: 0x20
-  __TEXT.__unwind_info: 0xb8
+  __TEXT.__objc_methname: 0x8e2
+  __TEXT.__objc_methtype: 0x39
+  __TEXT.__unwind_info: 0xc8
   __DATA_CONST.__const: 0x10
-  __DATA_CONST.__cfstring: 0x520
+  __DATA_CONST.__cfstring: 0x620
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x1b8
-  __DATA_CONST.__got: 0xf0
+  __DATA_CONST.__auth_got: 0x230
+  __DATA_CONST.__got: 0x130
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x260
+  __DATA.__objc_selrefs: 0x2d0
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/VoiceServices.framework/VoiceServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 29
-  Symbols:   96
-  CStrings:  218
+  Functions: 36
+  Symbols:   119
+  CStrings:  265
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
Symbols:
+ _NSStringFromClass
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_NSString
+ _TCCAccessSetForBundleIdWithOptions
+ ___NSArray0__struct
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __os_feature_enabled_impl
+ _kTCCServiceSiri
+ _objc_enumerationMutation
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_release_x25
+ _objc_release_x27
+ _objc_release_x8
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x27
CStrings:
+ "%s %@ has unexpected type %@; ignoring."
+ "%s %@ read returned nil — pref absent, sandboxed, or unentitled."
+ "%s %@: read %lu raw entries, %lu valid string bundle IDs."
+ "%s %lu TCC write(s) failed; NOT marking migration complete — will retry on next migration."
+ "%s Failed to set TCC denial for bundle %@. [sources: LFTA=%@, ShowContent=%@, ShowApp=%@]"
+ "%s Marked %@ as denied in kTCCServiceSiri. [sources: LFTA=%@, ShowContent=%@, ShowApp=%@]"
+ "%s Marking one-time App Access exclusion list migration as complete."
+ "%s One-time App Access exclusion list migration has already been performed. Skipping."
+ "%s SiriSetup/restrict_access_ui FF is not enabled. Skipping (will retry on future migration)."
+ "%s Source counts — LFTA-off: %lu, Show-Content-off: %lu, Show-App-off: %lu, union to migrate: %lu."
+ "%s TCC write summary — succeeded: %lu, failed: %lu."
+ "+[SiriMigrator _parseBundleIdsFromPreferenceValue:forKey:]"
+ "-[SiriMigrator _performAppAccessExclusionListMigrationIfNeeded]"
+ "@32@0:8@16@24"
+ "AppAccessExclusionListMigrationPerformed"
+ "B24@0:8Q16"
+ "NO"
+ "SBSearchDisabledApps"
+ "SBSearchDisabledBundles"
+ "SiriCanLearnFromAppBlacklist"
+ "SiriSetup"
+ "YES"
+ "_bundleIdsWithLearnFromAppDisabled"
+ "_bundleIdsWithShowAppInSearchDisabled"
+ "_bundleIdsWithShowContentInSearchDisabled"
+ "_markAppAccessExclusionListMigrationPerformed"
+ "_parseBundleIdsFromPreferenceValue:forKey:"
+ "_performAppAccessExclusionListMigrationIfNeeded"
+ "_shouldMarkAppAccessExclusionListMigrationCompleteWithFailureCount:"
+ "addObject:"
+ "arrayWithCapacity:"
+ "com.apple.spotlightui"
+ "com.apple.suggestions"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "restrict_access_ui"
+ "setWithArray:"
+ "setWithSet:"
+ "unionSet:"

```
