## TranslationAPISupportExtension

> `/System/Library/ExtensionKit/Extensions/TranslationAPISupportExtension.appex/TranslationAPISupportExtension`

```diff

-285.1.0.0.0
-  __TEXT.__text: 0x18288
-  __TEXT.__auth_stubs: 0xfd0
+292.1.0.0.0
+  __TEXT.__text: 0x1b6f0
+  __TEXT.__auth_stubs: 0x10c0
   __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0xb08
-  __TEXT.__swift5_typeref: 0x1253
-  __TEXT.__cstring: 0x8eb
-  __TEXT.__objc_methname: 0x413
-  __TEXT.__swift5_reflstr: 0x21f
+  __TEXT.__const: 0xb38
+  __TEXT.__swift5_typeref: 0x125f
+  __TEXT.__cstring: 0x8e2
+  __TEXT.__objc_methname: 0x43e
+  __TEXT.__swift5_reflstr: 0x22f
   __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__constg_swiftt: 0x638
+  __TEXT.__constg_swiftt: 0x670
   __TEXT.__swift5_fieldmd: 0x254
-  __TEXT.__swift5_capture: 0x1ac
-  __TEXT.__oslogstring: 0x2dd
+  __TEXT.__swift5_capture: 0x1bc
+  __TEXT.__oslogstring: 0x49d
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x34

   __TEXT.__objc_classname: 0x25
   __TEXT.__objc_methtype: 0x152
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x6d0
-  __TEXT.__eh_frame: 0x5a0
-  __DATA_CONST.__auth_got: 0x7e8
-  __DATA_CONST.__got: 0x278
-  __DATA_CONST.__auth_ptr: 0x378
-  __DATA_CONST.__const: 0x6d0
+  __TEXT.__unwind_info: 0x708
+  __TEXT.__eh_frame: 0x5c8
+  __DATA_CONST.__auth_got: 0x860
+  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__auth_ptr: 0x398
+  __DATA_CONST.__const: 0x738
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA.__objc_const: 0x710
-  __DATA.__objc_selrefs: 0xe8
-  __DATA.__objc_data: 0x400
-  __DATA.__data: 0x940
-  __DATA.__bss: 0x870
+  __DATA.__objc_selrefs: 0xf8
+  __DATA.__objc_data: 0x438
+  __DATA.__data: 0x990
+  __DATA.__bss: 0x880
   __DATA.__common: 0x38
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/ExtensionKit.framework/ExtensionKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

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
-  Functions: 515
-  Symbols:   150
-  CStrings:  146
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 552
+  Symbols:   164
+  CStrings:  151
 
Symbols:
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$__LTTranslator
+ __swiftEmptySetSingleton
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _bzero
+ _objc_release_x27
+ _swift_release_n
CStrings:
+ "Unable to cancel downloads because unexpectedly have nil source or target locale when trying to cancel downloads, which shouldn't happen; source: %!s(MISSING); target: %!s(MISSING)"
+ "Unhandled status"
+ "User approved downloads; requested download of: %!{(MISSING)public}s"
+ "User cancelled downloads; requesting removal of: %!{(MISSING)public}s"
+ "User wants to cancel downloads; some languages are already installed so not removing all languages; languages shown: %!{(MISSING)public}s; languages to remove: %!{(MISSING)public}s"
+ "_cachedOriginallyInstalledLanguageIdentifiers"
+ "addLanguages:useCellular:"
+ "removeLanguages:"
- "Contradictory frame constraints specified."
- "Download started"
- "languagesService"

```
