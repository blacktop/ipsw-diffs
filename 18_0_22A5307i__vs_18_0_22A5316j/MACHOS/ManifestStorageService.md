## ManifestStorageService

> `/System/Library/PrivateFrameworks/MobileAsset.framework/XPCServices/ManifestStorageService.xpc/ManifestStorageService`

```diff

-1290.0.0.0.8
-  __TEXT.__text: 0x209c
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0x21c
+1309.0.0.0.8
+  __TEXT.__text: 0x27e4
+  __TEXT.__auth_stubs: 0x3f0
+  __TEXT.__objc_stubs: 0x880
+  __TEXT.__objc_methlist: 0x234
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0xddd
-  __TEXT.__objc_methname: 0xa04
-  __TEXT.__objc_classname: 0xbb
-  __TEXT.__objc_methtype: 0x26f
+  __TEXT.__cstring: 0xfc4
+  __TEXT.__objc_methname: 0xb03
+  __TEXT.__objc_classname: 0xb9
+  __TEXT.__objc_methtype: 0x2bc
   __TEXT.__oslogstring: 0x17
-  __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__unwind_info: 0x100
-  __DATA_CONST.__auth_got: 0x1c8
+  __TEXT.__gcc_except_tab: 0xb4
+  __TEXT.__unwind_info: 0x118
+  __DATA_CONST.__auth_got: 0x208
   __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0xf0
-  __DATA_CONST.__cfstring: 0xd40
+  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__cfstring: 0xe80
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x250
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x7a8
-  __DATA.__objc_selrefs: 0x278
+  __DATA.__objc_const: 0x7c8
+  __DATA.__objc_selrefs: 0x2b0
   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x120

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 59
-  Symbols:   101
-  CStrings:  295
+  Functions: 62
+  Symbols:   109
+  CStrings:  318
 
Symbols:
+ ___error
+ _free
+ _malloc_type_calloc
+ _objc_release_x25
+ _objc_release_x28
+ _objc_retain_x23
+ _rename
+ _renamex_np
CStrings:
+ "\x05"
+ "-[MAManifestStorageService _parseSelector:assetType:specifier:]"
+ "-[MAManifestStorageService commitStagedManifestsForSelectors:]"
+ "-[MAManifestStorageService commitStagedManifestsForSelectors:completion:]_block_invoke"
+ "-[MAManifestStorageService storeManifest:infoPlist:stage:]"
+ "-[MAManifestStorageService storeManifest:infoPlist:stage:completion:]_block_invoke"
+ "02:31:49"
+ ":"
+ "@36@0:8@16@24B32"
+ "B40@0:8@16^@24^@32"
+ "Commit %!s(MISSING) -> %!s(MISSING) failed: %!d(MISSING) %!s(MISSING)"
+ "Commit %!s(MISSING) -> %!s(MISSING) succeeded"
+ "Commit failed: %!@(MISSING)"
+ "Committing staged manifests"
+ "Failed to create containing directory: %!@(MISSING)"
+ "Invalid selector: %!@(MISSING)"
+ "Jul 12 2024"
+ "Selector missing type or specifier: %!@(MISSING)"
+ "Staged manifest does not exist: %!@(MISSING)"
+ "Storing manifest (stage = %!i(MISSING))"
+ "T@\"NSDictionary\",&,V_commitErrorsBySelector"
+ "_commitErrorsBySelector"
+ "_manifestPathForAssetType:specifier:stage:"
+ "_parseSelector:assetType:specifier:"
+ "commitErrorsBySelector"
+ "commitStagedManifestsForSelectors:"
+ "commitStagedManifestsForSelectors:completion:"
+ "componentsSeparatedByString:"
+ "count"
+ "fileExistsAtPath:"
+ "fileSystemRepresentation"
+ "objectAtIndexedSubscript:"
+ "setCommitErrorsBySelector:"
+ "staged"
+ "storeManifest:infoPlist:stage:"
+ "storeManifest:infoPlist:stage:completion:"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@16@?24"
+ "v44@0:8@\"NSData\"16@\"NSData\"24B32@?<v@?@\"NSError\">36"
+ "v44@0:8@16@24B32@?36"
- "\x02"
- "\x04"
- "-[MAManifestStorageService storeManifest:infoPlist:]"
- "-[MAManifestStorageService storeManifest:infoPlist:completion:]_block_invoke"
- "15:49:25"
- "@\"MAManifestStorageServiceOverrides\""
- "Jun 30 2024"
- "Storing manifest"
- "T@\"MAManifestStorageServiceOverrides\",&,V_overrides"
- "_manifestPathForAssetType:specifier:"
- "_overrides"
- "_setOverrides:"
- "overrides"
- "setOverrides:"
- "storeManifest:infoPlist:"
- "storeManifest:infoPlist:completion:"
- "v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"NSError\">32"

```
