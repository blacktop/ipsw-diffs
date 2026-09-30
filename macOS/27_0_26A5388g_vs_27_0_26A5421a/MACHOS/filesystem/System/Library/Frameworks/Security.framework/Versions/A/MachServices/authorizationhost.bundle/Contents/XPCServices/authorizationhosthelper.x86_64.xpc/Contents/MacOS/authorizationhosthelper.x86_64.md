## authorizationhosthelper.x86_64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/authorizationhost.bundle/Contents/XPCServices/authorizationhosthelper.x86_64.xpc/Contents/MacOS/authorizationhosthelper.x86_64`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-55643.0.12.0.0
-  __TEXT.__text: 0x8280
-  __TEXT.__stubs: 0x2a6
+55643.0.14.0.0
+  __TEXT.__text: 0x7b30
+  __TEXT.__stubs: 0x294
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x4d2
-  __TEXT.__objc_methname: 0xea3
+  __TEXT.__cstring: 0x444
+  __TEXT.__objc_methname: 0xe2a
   __TEXT.__objc_classname: 0x11a
-  __TEXT.__objc_methtype: 0x6eb
-  __TEXT.__oslogstring: 0xe6b
-  __TEXT.__gcc_except_tab: 0xb8
-  __TEXT.__unwind_info: 0x2e0
+  __TEXT.__objc_methtype: 0x6dd
+  __TEXT.__oslogstring: 0xd5b
+  __TEXT.__gcc_except_tab: 0xa4
+  __TEXT.__unwind_info: 0x2b8
   __TEXT.__eh_frame: 0x58
-  __DATA_CONST.__const: 0x230
-  __DATA_CONST.__cfstring: 0x220
+  __DATA_CONST.__const: 0x1e0
+  __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
-  __DATA_CONST.__got: 0x4d0
-  __DATA.__objc_const: 0x1668
-  __DATA.__objc_selrefs: 0x418
+  __DATA_CONST.__got: 0x4b0
+  __DATA.__objc_const: 0x1620
+  __DATA.__objc_selrefs: 0x3f8
   __DATA.__objc_ivar: 0xf0
   __DATA.__objc_data: 0x778
   __DATA.__data: 0xc1
-  __DATA.__bss: 0x56
+  __DATA.__bss: 0x3e
   __DATA.__common: 0x18
   __CGPreLoginApp.__cgpreloginapp: 0x0
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 274
-  Symbols:   228
-  CStrings:  419
+  Functions: 256
+  Symbols:   224
+  CStrings:  402
 
Symbols:
- _AuthorizationRemoveSafePlugins
- __dispatch_queue_attr_concurrent
- __os_feature_enabled_impl
- _dispatch_barrier_sync
CStrings:
+ "isSystemPlugin:"
+ "pathForPlugin:"
- "/Library/Security/SecurityAgentPlugins/StagedPlugins/"
- "Actual number of connections = %d"
- "Clearing safe plugins cache"
- "Found plugin safe path %{public}@"
- "No safe path provided for %{public}@"
- "Plugin is already at the safe path %{public}@"
- "Rejecting unsafe plugin path: %{public}@"
- "SafePluginLoading"
- "SecurityAgent"
- "_plugin_safe_path"
- "clearSafePluginCache"
- "com.apple.SecurityAgent.safePathQueue"
- "initialize"
- "removeAllObjects"
- "safePathForPlugin:"
- "safePluginLoadingEnabled"
- "setSafePathForPlugin:path:"
- "stringByResolvingSymlinksInPath"
- "v32@0:8@16@24"
```
