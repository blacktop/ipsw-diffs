## UserFontManager

> `/System/Library/PrivateFrameworks/FontServices.framework/XPCServices/UserFontManager.xpc/UserFontManager`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-169.0.0.0.0
-  __TEXT.__text: 0x88fc
-  __TEXT.__auth_stubs: 0x400
+173.0.0.0.0
+  __TEXT.__text: 0x9c20
+  __TEXT.__auth_stubs: 0x440
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_stubs: 0x1140
-  __TEXT.__objc_methlist: 0x600
+  __TEXT.__objc_stubs: 0x1200
+  __TEXT.__objc_methlist: 0x624
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0xb85
+  __TEXT.__cstring: 0x1107
   __TEXT.__objc_classname: 0x8c
-  __TEXT.__objc_methname: 0x1229
-  __TEXT.__objc_methtype: 0x488
-  __TEXT.__gcc_except_tab: 0x19c
-  __TEXT.__unwind_info: 0x288
-  __DATA_CONST.__const: 0x478
-  __DATA_CONST.__cfstring: 0xc80
+  __TEXT.__objc_methname: 0x12f8
+  __TEXT.__objc_methtype: 0x4e1
+  __TEXT.__gcc_except_tab: 0x1d4
+  __TEXT.__unwind_info: 0x2c0
+  __DATA_CONST.__const: 0x4e0
+  __DATA_CONST.__cfstring: 0xf60
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x210
-  __DATA_CONST.__got: 0x120
-  __DATA.__objc_const: 0x4c0
-  __DATA.__objc_selrefs: 0x618
+  __DATA_CONST.__auth_got: 0x230
+  __DATA_CONST.__got: 0x128
+  __DATA.__objc_const: 0x4c8
+  __DATA.__objc_selrefs: 0x648
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x124

   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 124
-  Symbols:   135
-  CStrings:  375
+  Functions: 135
+  Symbols:   145
+  CStrings:  408
 
Symbols:
+ _AppReplacementDictionaryByRemovingIdentifier
+ _AppReplacementDictionaryByRenamingIdentifier
+ _AppReplacementIdentifierIsWellFormed
+ _FontProviderAppInfoIsWellFormed
+ _FontProviderFontsInfoIsWellFormed
+ _NSLocalizedDescriptionKey
+ _memchr
+ _objc_autorelease
+ _objc_release_x9
+ _objc_retainBlock
CStrings:
+ "\"%@\" is already a font provider (%@); refusing to merge with \"%@\" (%@)"
+ ".."
+ "/"
+ "App Replacement: \"%@\" already migrated to \"%@\""
+ "App Replacement: \"%@\" had an empty provider directory (%@) from a check-in; discarding it and migrating \"%@\" in"
+ "App Replacement: \"%@\" is not a known font provider, nothing to migrate"
+ "App Replacement: %@"
+ "App Replacement: dropped provider preference \"%@\" for \"%@\""
+ "App Replacement: entered replaceFontData in UserFontManager, \"%@\" -> \"%@\""
+ "App Replacement: migrated font provider \"%@\" -> \"%@\" (uuid %@ unchanged)"
+ "App Replacement: provider half done, handing the consumer half to fontservicesd"
+ "App Replacement: provider half failed, not attempting the consumer half"
+ "App Replacement: provider state migrated but issued-font bookkeeping did not, for \"%@\" -> \"%@\""
+ "App Replacement: re-keyed the identifier -> UUID mapping"
+ "App Replacement: refusing to build a path from a mapping value that is not a UUID: \"%@\""
+ "App Replacement: replaceFontData complete for \"%@\" -> \"%@\""
+ "B40@0:8@16@24^@32"
+ "_migrateProviderStateFromIdentifier:toIdentifier:error:"
+ "app info missing or malformed for %@"
+ "com.apple.FontServices.AppReplacementExtension"
+ "containsString:"
+ "could not reach fontservicesd to serialize the provider re-key; nothing was migrated"
+ "initWithUUIDString:"
+ "installFonts received malformed appInfo; dropping the connection."
+ "length"
+ "malformed identifier"
+ "migrateIssuedFontsForIdentifier:toIdentifier:"
+ "replaceFontDataFromIdentifier:toIdentifier:completionHandler:"
+ "source and destination are the same identifier"
+ "uninstallFonts received malformed appInfo; dropping the connection."
+ "updateAppInfo: rejecting malformed appInfo for identifier %@."
+ "v16@?0@\"NSError\"8"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@16@24@?32"
- "app info missing for %@"
```
