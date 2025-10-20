## DiagnosticExtensions

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions`

```diff

-133.2.0.0.0
-  __TEXT.__text: 0x162d4
+133.3.0.0.0
+  __TEXT.__text: 0x16334
   __TEXT.__auth_stubs: 0x9b0
   __TEXT.__objc_methlist: 0x10ac
   __TEXT.__const: 0x120
   __TEXT.__cstring: 0x103a
-  __TEXT.__oslogstring: 0x28d5
-  __TEXT.__gcc_except_tab: 0x600
+  __TEXT.__oslogstring: 0x291f
+  __TEXT.__gcc_except_tab: 0x5fc
   __TEXT.__unwind_info: 0x640
   __TEXT.__objc_classname: 0x229
-  __TEXT.__objc_methname: 0x313a
+  __TEXT.__objc_methname: 0x312d
   __TEXT.__objc_methtype: 0x591
   __TEXT.__objc_stubs: 0x2540
   __DATA_CONST.__got: 0x228

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EC6AB2DD-AEF1-32FF-BF2A-72CE2BA6BD24
-  Functions: 516
-  Symbols:   1986
-  CStrings:  1121
+  UUID: 38211171-F99F-3DF9-B5B1-DB0D63B12144
+  Functions: 515
+  Symbols:   1984
+  CStrings:  1122
 
Symbols:
+ _objc_msgSend$localizedStringForKey:value:table:
- _objc_msgSend$localizedStringForKey:value:table:localization:
Functions:
~ -[DEExtension _localizedStringFromPlistWithKey:localization:] : 344 -> 332
~ ___61-[DEExtension _localizedStringFromPlistWithKey:localization:]_block_invoke : 256 -> 384
- _OUTLINED_FUNCTION_7
~ -[DEExtension _localizedTextFromLocalizedStringKey:fallbackFileContentsKey:localization:].cold.1 : 116 -> 132
~ ___61-[DEExtension _localizedStringFromPlistWithKey:localization:]_block_invoke.cold.1 : 128 -> 124
CStrings:
+ "Could not find [%{public}@] for preferred localizations. Falling back to value in plist value"
+ "Ignoring given localization [%{public}@], user preferred languages instead."
+ "localizedStringForKey:value:table:"
- "Could not find [%{public}@] for localization [%{public}@]. Falling back to value in plist value"
- "localizedStringForKey:value:table:localization:"

```
