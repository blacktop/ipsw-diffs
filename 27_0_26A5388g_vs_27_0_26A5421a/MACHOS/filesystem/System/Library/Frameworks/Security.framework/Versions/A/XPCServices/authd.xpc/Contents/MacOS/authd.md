## authd

> `/System/Library/Frameworks/Security.framework/Versions/A/XPCServices/authd.xpc/Contents/MacOS/authd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-62460.0.55.0.1
-  __TEXT.__text: 0x27e44
-  __TEXT.__auth_stubs: 0x13e0
+62460.1.2.0.0
+  __TEXT.__text: 0x26438
+  __TEXT.__auth_stubs: 0x1380
   __TEXT.__lazy_helpers: 0x63c
-  __TEXT.__objc_stubs: 0xda0
+  __TEXT.__objc_stubs: 0xc00
   __TEXT.__objc_methlist: 0x154
-  __TEXT.__const: 0xb20
-  __TEXT.__cstring: 0x2f86
-  __TEXT.__oslogstring: 0x5056
+  __TEXT.__const: 0xb10
+  __TEXT.__cstring: 0x2ea9
+  __TEXT.__oslogstring: 0x4bda
   __TEXT.__dlopen_cstrs: 0x5d
-  __TEXT.__gcc_except_tab: 0xe78
-  __TEXT.__objc_methname: 0xace
+  __TEXT.__gcc_except_tab: 0xd70
+  __TEXT.__objc_methname: 0x9c0
   __TEXT.__objc_classname: 0xf
   __TEXT.__objc_methtype: 0x140
-  __TEXT.__unwind_info: 0x648
-  __DATA_CONST.__const: 0x23a0
-  __DATA_CONST.__cfstring: 0x11a0
+  __TEXT.__unwind_info: 0x618
+  __DATA_CONST.__const: 0x22c8
+  __DATA_CONST.__cfstring: 0x10e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0xa00
-  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__auth_got: 0x9d0
+  __DATA_CONST.__got: 0x190
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x230
-  __DATA.__objc_selrefs: 0x378
+  __DATA.__objc_selrefs: 0x310
   __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0x50
   __DATA.__lazy_load_got: 0x98
   __DATA.__data: 0xa0
-  __DATA.__bss: 0x390
+  __DATA.__bss: 0x368
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 477
-  Symbols:   404
-  CStrings:  1097
+  Functions: 465
+  Symbols:   397
+  CStrings:  1046
 
Symbols:
- _OBJC_CLASS_$_NSMutableIndexSet
- _chown
- _getgid
- _getuid
- _lstat
- _strndup
- _xpc_dictionary_get_bool
CStrings:
- ""
- "-%@"
- "."
- ".."
- "/"
- "/Library/Security/SecurityAgentPlugins/StagedPlugins"
- "A plugin path is required for install operation"
- "AUTHORIZATION_STAGE_PLUGIN"
- "After permissions were fixed, %{public}@ was removed"
- "B16@?0@\"NSString\"8"
- "Cannot stat plugin path %{public}s: %{darwin.errno}d"
- "Clearing stagedir %{public}@"
- "Client missing required entitlement: %{public}s"
- "Copying plugin from %{public}@ to %{public}@"
- "Error getting content of %{public}@: %{public}@"
- "Failed again to remove %{public}@: %{public}@"
- "Failed to copy plugin to secure location: %{public}@"
- "Failed to create NSString from plugin path"
- "Failed to create staging directory: %{public}@"
- "Failed to move existing staged plugin: %{public}@"
- "Failed to remove %{public}@: %{public}@"
- "Failed to remove existing staged plugin: %{public}@"
- "Failed to set permissions on staging directory"
- "Going to stage plugin %{public}s"
- "Going to unstage plugins for %d"
- "Invalid plugin name: %{public}@"
- "Invalid plugin path provided"
- "Moving existing staged plugin from %{public}@ to %{public}@"
- "Non-fatal error: failed to fully clean stage dir"
- "Plugin %{public}@ copied to the secure location %{public}@"
- "Plugin %{public}s is already safe"
- "Rejecting symlink plugin path %{public}s"
- "Successfully removed staged plugin: %{public}@"
- "UUID"
- "_bool"
- "_plugin_path"
- "_plugin_safe_path"
- "addIndex:"
- "agent: staged plugins cleanup"
- "array"
- "com.apple.private.Authorization.SPI"
- "com.apple.security.auth.plugin.access"
- "containsIndex:"
- "containsString:"
- "copyItemAtPath:toPath:error:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "fileExistsAtPath:"
- "moveItemAtPath:toPath:error:"
- "removeIndex:"
- "removeItemAtPath:error:"
- "stringByAppendingFormat:"
```
