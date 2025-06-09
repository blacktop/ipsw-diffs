## IntlPreferences

> `/System/Library/PrivateFrameworks/IntlPreferences.framework/IntlPreferences`

```diff

-454.500.0.0.0
-  __TEXT.__text: 0x19980
+464.4.0.0.0
+  __TEXT.__text: 0x19b78
   __TEXT.__auth_stubs: 0xb30
-  __TEXT.__objc_methlist: 0x10f4
-  __TEXT.__const: 0x172
-  __TEXT.__cstring: 0x12b5
-  __TEXT.__oslogstring: 0xe47
+  __TEXT.__objc_methlist: 0x112c
+  __TEXT.__const: 0x182
+  __TEXT.__cstring: 0x12c5
+  __TEXT.__oslogstring: 0xe7c
   __TEXT.__gcc_except_tab: 0x220
   __TEXT.__dlopen_cstrs: 0x20a
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x5a
-  __TEXT.__unwind_info: 0x590
+  __TEXT.__unwind_info: 0x5a0
   __TEXT.__objc_classname: 0x2da
-  __TEXT.__objc_methname: 0x3abc
-  __TEXT.__objc_methtype: 0x41b
-  __TEXT.__objc_stubs: 0x3360
-  __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__const: 0x668
+  __TEXT.__objc_methname: 0x3b47
+  __TEXT.__objc_methtype: 0x43b
+  __TEXT.__objc_stubs: 0x33e0
+  __DATA_CONST.__got: 0x2d8
+  __DATA_CONST.__const: 0x648
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1010
+  __DATA_CONST.__objc_selrefs: 0x1030
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x300
   __AUTH_CONST.__auth_got: 0x5a8
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x1aa0
-  __AUTH_CONST.__objc_const: 0x1618
+  __AUTH_CONST.__cfstring: 0x1a80
+  __AUTH_CONST.__objc_const: 0x1620
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x78

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: DA6A5E97-D825-35CC-BB0D-D5FBBBFE5614
-  Functions: 431
-  Symbols:   1871
-  CStrings:  1210
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  UUID: 214D0B64-B6ED-3C66-9A4C-0EDCEF31EEDB
+  Functions: 436
+  Symbols:   1879
+  CStrings:  1214
 
Symbols:
+ +[IntlUtility _setPreferredLanguage:forBundleID:].cold.1
+ +[IntlUtility checkForDiscoveredLanguages:]
+ +[NSLocale(IntlPreferencesAdditions) _inputModesToEnableForLocale:]
+ +[NSLocale(IntlPreferencesAdditions) enableDefaultInputModesForCurrentLocale]
+ +[NSLocale(IntlPreferencesAdditions) enableInputModesForLocale:addToFront:]
+ GCC_except_table81
+ GCC_except_table85
+ ___43+[IntlUtility checkForDiscoveredLanguages:]_block_invoke
+ ___46+[IntlUtility preferredLanguagesForBundleIDs:]_block_invoke.243
+ ___49+[IntlUtility _setPreferredLanguage:forBundleID:]_block_invoke.250
+ ___block_literal_global.119
+ ___block_literal_global.260
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_IntlPreferences
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_IntlPreferences
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_IntlPreferences
+ _objc_msgSend$_inputModesToEnableForLocale:
+ _objc_msgSend$checkForDiscoveredLanguages:
+ _objc_msgSend$enableDefaultInputModesForCurrentLocale
+ _objc_msgSend$enableInputModesForLocale:addToFront:
+ _objc_msgSend$reverseObjectEnumerator
+ _objc_msgSend$suggestedInputModesForLocales:
- GCC_except_table79
- GCC_except_table83
- ___46+[IntlUtility preferredLanguagesForBundleIDs:]_block_invoke.246
- ___49+[IntlUtility _setPreferredLanguage:forBundleID:]_block_invoke.253
- ___block_literal_global.120
- ___block_literal_global.263
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_IntlPreferences
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_IntlPreferences
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_IntlPreferences
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_IntlPreferences
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_IntlPreferences
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_IntlPreferences
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_IntlPreferences
- _objc_msgSend$arrayWithObject:
- _objc_msgSend$suggestedInputModesForCurrentLocale
CStrings:
+ "AlternateCalendarExpansion"
+ "App bundle for ID %{private}@ doesn't exist, exiting"
+ "_inputModesToEnableForLocale:"
+ "checkForDiscoveredLanguages:"
+ "enableDefaultInputModesForCurrentLocale"
+ "enableInputModesForLocale:addToFront:"
+ "numberingSystems"
+ "reverseObjectEnumerator"
+ "suggestedInputModesForLocales:"
+ "v24@0:8@?<v@?@\"NSDictionary\">16"
- "HinduCalendar"
- "arrayWithObject:"
- "hanidays"
- "hebr"
- "suggestedInputModesForCurrentLocale"

```
