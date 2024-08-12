## SiriAutoComplete

> `/System/Library/PrivateFrameworks/SiriAutoComplete.framework/SiriAutoComplete`

```diff

-3400.118.1.0.0
-  __TEXT.__text: 0x30470
-  __TEXT.__auth_stubs: 0x11b0
-  __TEXT.__const: 0x15a0
-  __TEXT.__cstring: 0xe77
-  __TEXT.__constg_swiftt: 0xb90
-  __TEXT.__swift5_typeref: 0x7a1
-  __TEXT.__swift5_reflstr: 0x3e8
-  __TEXT.__swift5_fieldmd: 0x6d4
-  __TEXT.__oslogstring: 0x206c
-  __TEXT.__swift5_proto: 0x130
-  __TEXT.__swift5_types: 0xa0
+3401.8.1.0.0
+  __TEXT.__text: 0x343f8
+  __TEXT.__auth_stubs: 0x1270
+  __TEXT.__const: 0x1530
+  __TEXT.__cstring: 0xf47
+  __TEXT.__constg_swiftt: 0xb94
+  __TEXT.__swift5_typeref: 0x7f9
+  __TEXT.__swift5_reflstr: 0x478
+  __TEXT.__swift5_fieldmd: 0x6f4
+  __TEXT.__oslogstring: 0x22cc
+  __TEXT.__swift5_proto: 0x128
+  __TEXT.__swift5_types: 0x9c
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_capture: 0x60
-  __TEXT.__unwind_info: 0xc40
-  __TEXT.__eh_frame: 0x16c0
-  __TEXT.__objc_methname: 0x5ee
-  __DATA_CONST.__got: 0x280
-  __DATA_CONST.__const: 0x110
-  __DATA_CONST.__objc_classlist: 0x98
+  __TEXT.__unwind_info: 0xce0
+  __TEXT.__eh_frame: 0x1898
+  __TEXT.__objc_methname: 0x5ff
+  __DATA_CONST.__got: 0x2b8
+  __DATA_CONST.__const: 0x150
+  __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2a0
-  __AUTH_CONST.__auth_got: 0x8d8
-  __AUTH_CONST.__auth_ptr: 0x2f8
-  __AUTH_CONST.__const: 0xea8
-  __AUTH_CONST.__objc_const: 0xcb8
-  __AUTH.__objc_data: 0x280
-  __AUTH.__data: 0xf50
-  __DATA.__data: 0x6d0
-  __DATA.__common: 0x90
-  __DATA.__bss: 0x1d00
+  __AUTH_CONST.__auth_got: 0x938
+  __AUTH_CONST.__auth_ptr: 0x338
+  __AUTH_CONST.__const: 0xda8
+  __AUTH_CONST.__objc_const: 0xe10
+  __AUTH.__objc_data: 0x230
+  __AUTH.__data: 0xb88
+  __DATA.__data: 0x608
+  __DATA.__common: 0x88
+  __DATA.__bss: 0x1c00
+  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__data: 0x580
+  __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1125
-  Symbols:   494
-  CStrings:  284
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 1181
+  Symbols:   521
+  CStrings:  297
 
Symbols:
+ _OBJC_CLASS_$_LNAutoShortcut
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_retain_x28
+ _swift_deallocPartialClassInstance
CStrings:
+ "%!s(MISSING) Error: The intentClass of the objects being unioned should be the same: %!s(MISSING) and %!s(MISSING)"
+ "%!s(MISSING): %!s(MISSING) is in the deny list but has empty parameters and parameterCombinations. The entire INIntent  %!s(MISSING) is denied."
+ "%!s(MISSING): Not adding any parameter combinations for intent class %!s(MISSING) since areAllParametersDenied = YES"
+ "%!s(MISSING): Not adding intent class %!s(MISSING), parameter combination: %!s(MISSING)"
+ "%!s(MISSING): Not adding intent class %!s(MISSING), parameter combination: %!s(MISSING) since it contains a denied parameter: '%!s(MISSING)'"
+ "%!s(MISSING): loaded %!l(MISSING)d intents"
+ "SiriAutoCompleteIndexBuilder updateIndexForAppInstall with %!s(MISSING)"
+ "SiriAutoCompleteIndexBuilder updateIndexForAppInstall:%!s(MISSING) not able to get app metadata. Not updating index"
+ "SiriAutoCompleteIndexBuilder: index build is not enabled. Not running updateIndexForAppInstall"
+ "SiriAutoCompleteIndexBuilder: index build upon first installation is currently disabled"
+ "SiriKitIntentSource: processPlayMediaIntent - playlist does not have identifier, skipping this title '%!s(MISSING)'"
+ "_TtC16SiriAutoComplete12DeniedIntent"
+ "appShortcutProvider"
+ "areAllParametersDenied"
+ "autoShortcutsForBundleIdentifier:localeIdentifier:completion:"
+ "deniedIntentLookup"
+ "deniedParameters"
+ "deviceLibraryPersistentID"
+ "eligibilityCriteria"
+ "x-sampplaylist://device"
+ "x-sampplaylist://sirisync"
- "%!s(MISSING): Not adding intent class %!s(MISSING), parameter combination: %!s(MISSING) to the index"
- "%!s(MISSING): loaded %!l(MISSING)d records"
- "INCreateNoteIntent"
- "INSendMessageIntent"
- "SiriAutoCompleteIndexBuilder no-op updateIndexForAppInstall with %!s(MISSING)"
- "SiriAutoCompleteIndexBuilder: index build is not enabled. Not running first index build post OS install"
- "Unexpected error encountered during reindexing while attempting to delete the AutoComplete search index: %!s(MISSING)"
- "autoShortcutsForLocaleIdentifier:completion:"
- "v24@?0@\"NSDictionary\"8@\"NSError\"16"

```
