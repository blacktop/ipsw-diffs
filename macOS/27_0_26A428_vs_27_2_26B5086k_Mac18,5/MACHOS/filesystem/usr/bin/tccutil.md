## tccutil

> `/usr/bin/tccutil`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`

```diff

-913.3.3.0.0
-  __TEXT.__text: 0xd74
-  __TEXT.__auth_stubs: 0x320
-  __TEXT.__objc_stubs: 0x180
-  __TEXT.__cstring: 0x471
+918.0.0.0.0
+  __TEXT.__text: 0x15c8
+  __TEXT.__auth_stubs: 0x370
+  __TEXT.__objc_stubs: 0x200
+  __TEXT.__cstring: 0x513
   __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__objc_methname: 0xfc
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__gcc_except_tab: 0x108
+  __TEXT.__objc_methname: 0x139
+  __TEXT.__unwind_info: 0x120
   __DATA_CONST.__const: 0xd0
-  __DATA_CONST.__cfstring: 0x60
+  __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x1a0
-  __DATA_CONST.__got: 0x48
-  __DATA.__objc_selrefs: 0x60
+  __DATA_CONST.__objc_arraydata: 0x28
+  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA_CONST.__auth_got: 0x1c8
+  __DATA_CONST.__got: 0x60
+  __DATA.__objc_selrefs: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 28
-  Symbols:   65
-  CStrings:  43
+  Functions: 38
+  Symbols:   74
+  CStrings:  51
 
Symbols:
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableDictionary
+ _TCCServiceCopyNames
+ __DefaultRuneLocale
+ ___maskrune
+ _access
+ _putchar
+ _strlen
+ _tcc_server_create
- _tcc_server_singleton_default
CStrings:
+ "%s%s"
+ "%s:\n"
+ "Usage:\ntccutil reset SERVICE [BUNDLE_ID]\ntccutil list [-s SERVICE | -b BUNDLE_ID | -s SERVICE -b BUNDLE_ID]\n\nCommands:\n  reset SERVICE [BUNDLE_ID]          Reset TCC state for SERVICE (optionally for BUNDLE_ID)\n  list                               Show all TCC service names\n  list -s SERVICE                    Show all bundle IDs with a record for SERVICE\n  list -b BUNDLE_ID                  Show all services with a record for BUNDLE_ID\n  list -s SERVICE -b BUNDLE_ID       Show granted or denied for BUNDLE_ID and SERVICE\n                                      (exit 0 if granted, 1 denied, 2 limited)\n"
+ "Usage: tccutil list [-s SERVICE | -b BUNDLE_ID | -s SERVICE -b BUNDLE_ID]"
+ "addObject:"
+ "array"
+ "dictionary"
+ "kTCCServicePrototype3Rights"
+ "kTCCServicePrototype4Rights"
+ "limited"
+ "objectForKeyedSubscript:"
+ "setObject:forKeyedSubscript:"
- "Error: %s"
- "Usage:\ntccutil reset SERVICE [BUNDLE_ID]\ntccutil list (-s SERVICE | -b BUNDLE_ID | -s SERVICE -b BUNDLE_ID)\n\nCommands:\n  reset SERVICE [BUNDLE_ID]          Reset TCC state for SERVICE (optionally for BUNDLE_ID)\n  list -s SERVICE                    Show all bundle IDs with a record for SERVICE\n  list -b BUNDLE_ID                  Show all services with a record for BUNDLE_ID\n  list -s SERVICE -b BUNDLE_ID       Show granted or denied for BUNDLE_ID and SERVICE\n  (SERVICE may omit the 'kTCCService' prefix)"
- "Usage: tccutil list (-s SERVICE | -b BUNDLE_ID | -s SERVICE -b BUNDLE_ID)"
- "localizedDescription"
```
