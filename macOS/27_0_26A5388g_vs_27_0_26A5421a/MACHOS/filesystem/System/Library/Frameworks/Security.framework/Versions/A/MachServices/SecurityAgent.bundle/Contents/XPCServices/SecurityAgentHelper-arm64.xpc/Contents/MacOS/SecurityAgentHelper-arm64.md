## SecurityAgentHelper-arm64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/XPCServices/SecurityAgentHelper-arm64.xpc/Contents/MacOS/SecurityAgentHelper-arm64`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-55643.0.12.0.0
-  __TEXT.__text: 0x1ee48
-  __TEXT.__auth_stubs: 0xf50
-  __TEXT.__objc_stubs: 0x4880
-  __TEXT.__objc_methlist: 0x208c
+55643.0.14.0.0
+  __TEXT.__text: 0x1e728
+  __TEXT.__auth_stubs: 0xf30
+  __TEXT.__objc_stubs: 0x4820
+  __TEXT.__objc_methlist: 0x206c
   __TEXT.__const: 0x130
-  __TEXT.__objc_methname: 0x4e58
-  __TEXT.__oslogstring: 0x22d4
+  __TEXT.__objc_methname: 0x4df0
+  __TEXT.__oslogstring: 0x21f8
   __TEXT.__objc_classname: 0x32d
   __TEXT.__objc_methtype: 0x1745
-  __TEXT.__cstring: 0x1f97
-  __TEXT.__gcc_except_tab: 0x3e4
+  __TEXT.__cstring: 0x1f17
+  __TEXT.__gcc_except_tab: 0x3d0
   __TEXT.__ustring: 0xa86
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__unwind_info: 0x7b8
-  __DATA_CONST.__const: 0x788
-  __DATA_CONST.__cfstring: 0x1a20
+  __TEXT.__unwind_info: 0x7a8
+  __DATA_CONST.__const: 0x768
+  __DATA_CONST.__cfstring: 0x1a00
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x7b8
-  __DATA_CONST.__got: 0x430
+  __DATA_CONST.__auth_got: 0x7a8
+  __DATA_CONST.__got: 0x420
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x31b0
-  __DATA.__objc_selrefs: 0x1828
+  __DATA.__objc_selrefs: 0x1808
   __DATA.__objc_ivar: 0x2b8
   __DATA.__objc_data: 0x8c0
   __DATA.__data: 0x4a0
-  __DATA.__bss: 0x130
+  __DATA.__bss: 0x118
   __DATA.__common: 0x20
   __CGPreLoginApp.__cgpreloginapp: 0x0
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 810
-  Symbols:   527
-  CStrings:  1783
+  Functions: 794
+  Symbols:   524
+  CStrings:  1769
 
Symbols:
- _AuthorizationRemoveSafePlugins
- __dispatch_queue_attr_concurrent
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
- "_plugin_safe_path"
- "clearSafePluginCache"
- "com.apple.SecurityAgent.safePathQueue"
- "initialize"
- "safePathForPlugin:"
- "safePluginLoadingEnabled"
- "setSafePathForPlugin:path:"
- "stringByResolvingSymlinksInPath"
```
