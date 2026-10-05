## IntlPreferences

> `/System/Library/PrivateFrameworks/IntlPreferences.framework/IntlPreferences`

```diff

-498.0.0.0.0
-  __TEXT.__text: 0x1b5b8
-  __TEXT.__objc_methlist: 0x1204
-  __TEXT.__const: 0x200
-  __TEXT.__cstring: 0x12e5
-  __TEXT.__oslogstring: 0xfec
-  __TEXT.__gcc_except_tab: 0x234
+500.1.1.0.0
+  __TEXT.__text: 0x1c8f0
+  __TEXT.__objc_methlist: 0x122c
+  __TEXT.__const: 0x220
+  __TEXT.__cstring: 0x1385
+  __TEXT.__oslogstring: 0x160c
+  __TEXT.__gcc_except_tab: 0x21c
   __TEXT.__dlopen_cstrs: 0x20a
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x76
-  __TEXT.__unwind_info: 0x7a0
+  __TEXT.__unwind_info: 0x7d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6c8
+  __DATA_CONST.__const: 0x740
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10c8
+  __DATA_CONST.__objc_selrefs: 0x1108
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x300
-  __DATA_CONST.__got: 0x320
+  __DATA_CONST.__got: 0x330
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x1a80
-  __AUTH_CONST.__objc_const: 0x1648
+  __AUTH_CONST.__cfstring: 0x1ae0
+  __AUTH_CONST.__objc_const: 0x1650
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x610
-  __AUTH.__objc_data: 0xa0
+  __AUTH_CONST.__auth_got: 0x618
   __DATA.__objc_ivar: 0x60
   __DATA.__data: 0x190
-  __DATA_DIRTY.__objc_data: 0x690
+  __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 474
-  Symbols:   993
-  CStrings:  338
+  Functions: 487
+  Symbols:   1006
+  CStrings:  356
 
Symbols:
+ +[IntlUtility _forwardPreferredLanguagesToWatchAppForCompanionBundleID:languages:context:completion:]
+ +[IntlUtility _migratePreferredLanguageFromBundleID:sourceContainerPath:toBundleID:destinationContainerPath:carriedLanguages:error:]
+ GCC_except_table100
+ GCC_except_table108
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_NSError
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ __CFPreferencesSynchronizeWithContainer
+ ___101+[IntlUtility _forwardPreferredLanguagesToWatchAppForCompanionBundleID:languages:context:completion:]_block_invoke
+ ___101+[IntlUtility _forwardPreferredLanguagesToWatchAppForCompanionBundleID:languages:context:completion:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8
+ __appleLanguagesInContainer
- GCC_except_table107
- GCC_except_table99
CStrings:
+ "### [%{public}@]: Per-app language migration failed: could not synchronize AppleLanguages for %{private}@"
+ "### [%{public}@]: Watch language forward (%{public}@) failed: could not query install state for %{private}@: %{public}@ (domain %{public}@ code %ld)"
+ "### [%{public}@]: Watch language forward (%{public}@) failed: could not write preferences for %{private}@: %{public}@ (domain %{public}@ code %ld)"
+ "### [%{public}@]: Watch language forward (%{public}@) failed: no watch app bundle ID for %{private}@: %{public}@ (domain %{public}@ code %ld)"
+ "Empty bundle identifier or container path"
+ "Failed to synchronize AppleLanguages for the destination app"
+ "[%{public}@]: Per-app language migration complete: %{private}@ -> %{private}@, override language [%{public}@], %lu entries"
+ "[%{public}@]: Per-app language migration complete: [%{public}@] resolves to the default for %{private}@, so nothing was recorded"
+ "[%{public}@]: Per-app language migration complete: source %{private}@ had no override to carry over"
+ "[%{public}@]: Per-app language migration rejected: empty bundle identifier or container path"
+ "[%{public}@]: Per-app language migration skipped: source and destination are the same app"
+ "[%{public}@]: Watch language forward (%{public}@) complete: %{private}@ -> %{private}@, %lu entries"
+ "[%{public}@]: Watch language forward (%{public}@) deferred: no watch app installed for %{private}@"
+ "[%{public}@]: Watch language forward (%{public}@) skipped: no AppConduit connection"
+ "[%{public}@]: Watch language forward (%{public}@) skipped: no active paired watch"
+ "[IntlUtility]: Per-app language migration could not read the destination bundle for %{private}@; carrying the override over"
+ "com.apple.IntlPreferences.PerAppLanguageMigration"
+ "v12@?0B8"
```
