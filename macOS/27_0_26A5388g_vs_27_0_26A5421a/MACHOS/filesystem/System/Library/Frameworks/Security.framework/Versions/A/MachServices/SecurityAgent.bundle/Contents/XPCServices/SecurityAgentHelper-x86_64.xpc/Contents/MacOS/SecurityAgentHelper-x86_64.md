## SecurityAgentHelper-x86_64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/XPCServices/SecurityAgentHelper-x86_64.xpc/Contents/MacOS/SecurityAgentHelper-x86_64`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-55643.0.12.0.0
-  __TEXT.__text: 0x224a4
-  __TEXT.__stubs: 0x5b2
+55643.0.14.0.0
+  __TEXT.__text: 0x21d84
+  __TEXT.__stubs: 0x5a6
   __TEXT.__const: 0xe0
-  __TEXT.__objc_methname: 0x4faf
-  __TEXT.__oslogstring: 0x2941
+  __TEXT.__objc_methname: 0x4f47
+  __TEXT.__oslogstring: 0x2831
   __TEXT.__objc_classname: 0x32d
   __TEXT.__objc_methtype: 0x1750
-  __TEXT.__cstring: 0x1f97
-  __TEXT.__gcc_except_tab: 0x3e4
+  __TEXT.__cstring: 0x1f17
+  __TEXT.__gcc_except_tab: 0x3d0
   __TEXT.__ustring: 0xa86
   __TEXT.__dlopen_cstrs: 0xbd
-  __TEXT.__unwind_info: 0x788
+  __TEXT.__unwind_info: 0x768
   __TEXT.__eh_frame: 0x58
-  __DATA_CONST.__const: 0x778
-  __DATA_CONST.__cfstring: 0x1a20
+  __DATA_CONST.__const: 0x758
+  __DATA_CONST.__cfstring: 0x1a00
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__got: 0xbd8
-  __DATA.__objc_const: 0x6cb8
-  __DATA.__objc_selrefs: 0x1330
+  __DATA_CONST.__got: 0xbc0
+  __DATA.__objc_const: 0x6c70
+  __DATA.__objc_selrefs: 0x1318
   __DATA.__objc_ivar: 0x570
   __DATA.__objc_data: 0xc48
   __DATA.__data: 0x4a0
-  __DATA.__bss: 0x130
+  __DATA.__bss: 0x118
   __DATA.__common: 0x20
   __CGPreLoginApp.__cgpreloginapp: 0x0
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 784
-  Symbols:   527
-  CStrings:  1801
+  Functions: 768
+  Symbols:   524
+  CStrings:  1787
 
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
