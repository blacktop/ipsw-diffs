## authorizationhosthelper.arm64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/authorizationhost.bundle/Contents/XPCServices/authorizationhosthelper.arm64.xpc/Contents/MacOS/authorizationhosthelper.arm64`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-55643.0.12.0.0
-  __TEXT.__text: 0x7d50
-  __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_stubs: 0x1000
-  __TEXT.__objc_methlist: 0x78c
-  __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x4d1
+55643.0.14.0.0
+  __TEXT.__text: 0x75d8
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_stubs: 0xf80
+  __TEXT.__objc_methlist: 0x764
+  __TEXT.__const: 0xd0
+  __TEXT.__cstring: 0x443
   __TEXT.__objc_classname: 0x11a
-  __TEXT.__objc_methname: 0xea3
-  __TEXT.__objc_methtype: 0x6eb
-  __TEXT.__oslogstring: 0xc2c
-  __TEXT.__gcc_except_tab: 0xc4
-  __TEXT.__unwind_info: 0x2b8
-  __DATA_CONST.__const: 0x230
-  __DATA_CONST.__cfstring: 0x220
+  __TEXT.__objc_methname: 0xe2a
+  __TEXT.__objc_methtype: 0x6dd
+  __TEXT.__oslogstring: 0xb50
+  __TEXT.__gcc_except_tab: 0xac
+  __TEXT.__unwind_info: 0x2b0
+  __DATA_CONST.__const: 0x1e0
+  __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
-  __DATA_CONST.__auth_got: 0x3b0
-  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__auth_got: 0x398
+  __DATA_CONST.__got: 0x128
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0xb98
-  __DATA.__objc_selrefs: 0x530
+  __DATA.__objc_selrefs: 0x508
   __DATA.__objc_ivar: 0x78
   __DATA.__objc_data: 0x410
   __DATA.__data: 0xc1
-  __DATA.__bss: 0x56
+  __DATA.__bss: 0x3e
   __DATA.__common: 0x18
   __CGPreLoginApp.__cgpreloginapp: 0x0
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 283
-  Symbols:   229
-  CStrings:  419
+  Functions: 266
+  Symbols:   225
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
