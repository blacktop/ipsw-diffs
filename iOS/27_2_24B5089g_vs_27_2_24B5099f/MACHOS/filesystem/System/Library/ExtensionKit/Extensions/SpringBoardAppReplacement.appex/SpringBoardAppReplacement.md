## SpringBoardAppReplacement

> `/System/Library/ExtensionKit/Extensions/SpringBoardAppReplacement.appex/SpringBoardAppReplacement`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_data`

```diff

-4637.1.8.101.0
-  __TEXT.__text: 0x140
-  __TEXT.__auth_stubs: 0xd0
-  __TEXT.__objc_stubs: 0xa0
-  __TEXT.__objc_methlist: 0x13c
-  __TEXT.__objc_methname: 0x1f3
-  __TEXT.__objc_classname: 0x3c
-  __TEXT.__objc_methtype: 0xf5
-  __TEXT.__unwind_info: 0x60
+4637.1.12.101.0
+  __TEXT.__text: 0x27c
+  __TEXT.__auth_stubs: 0x100
+  __TEXT.__objc_stubs: 0x140
+  __TEXT.__objc_methlist: 0x164
+  __TEXT.__const: 0x10
+  __TEXT.__objc_methname: 0x26f
+  __TEXT.__oslogstring: 0x4e
+  __TEXT.__objc_classname: 0x51
+  __TEXT.__objc_methtype: 0x111
+  __TEXT.__unwind_info: 0x68
   __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x10
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x70
-  __DATA_CONST.__got: 0x8
-  __DATA.__objc_const: 0x1f8
-  __DATA.__objc_selrefs: 0xd8
+  __DATA_CONST.__auth_got: 0x88
+  __DATA_CONST.__got: 0x10
+  __DATA.__objc_const: 0x208
+  __DATA.__objc_selrefs: 0x108
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0xc0
+  __DATA.__data: 0x120
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2
-  Symbols:   22
-  CStrings:  50
+  Functions: 3
+  Symbols:   26
+  CStrings:  60
 
Symbols:
+ _OBJC_CLASS_$_NSXPCInterface
+ _SBLogCommon
+ __os_log_impl
+ _objc_release_x25
+ _objc_retain_x20
+ _os_log_type_enabled
- _objc_release
- _objc_retain_x19
CStrings:
+ "Accepting app replacement connection from pid %d"
+ "B24@0:8@\"NSXPCConnection\"16"
+ "Replace icons for %@ with %@"
+ "_EXConnectionHandler"
+ "interfaceWithProtocol:"
+ "processIdentifier"
+ "replaceApplicationIconsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:options:"
+ "resume"
+ "setExportedInterface:"
+ "setExportedObject:"
+ "shouldAcceptXPCConnection:"
- "replaceApplicationIconsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:"
```
