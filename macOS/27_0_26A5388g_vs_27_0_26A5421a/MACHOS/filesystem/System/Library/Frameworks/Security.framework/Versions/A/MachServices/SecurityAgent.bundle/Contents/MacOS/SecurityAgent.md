## SecurityAgent

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/MacOS/SecurityAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-55643.0.12.0.0
-  __TEXT.__text: 0x2cdfc
-  __TEXT.__auth_stubs: 0x12b0
-  __TEXT.__objc_stubs: 0x55c0
-  __TEXT.__objc_methlist: 0x2a0c
-  __TEXT.__const: 0x169
-  __TEXT.__cstring: 0x316c
+55643.0.14.0.0
+  __TEXT.__text: 0x2c308
+  __TEXT.__auth_stubs: 0x1240
+  __TEXT.__objc_stubs: 0x5580
+  __TEXT.__objc_methlist: 0x29e4
+  __TEXT.__const: 0x171
+  __TEXT.__cstring: 0x3115
   __TEXT.__gcc_except_tab: 0x404
-  __TEXT.__oslogstring: 0x3060
-  __TEXT.__objc_methname: 0x5acd
+  __TEXT.__oslogstring: 0x2e09
+  __TEXT.__objc_methname: 0x5a85
   __TEXT.__objc_classname: 0x618
   __TEXT.__objc_methtype: 0x1897
   __TEXT.__ustring: 0x187e
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__unwind_info: 0xa48
-  __DATA_CONST.__const: 0x958
-  __DATA_CONST.__cfstring: 0x2a60
+  __TEXT.__unwind_info: 0xa28
+  __DATA_CONST.__const: 0x938
+  __DATA_CONST.__cfstring: 0x2a40
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x968
+  __DATA_CONST.__auth_got: 0x930
   __DATA_CONST.__got: 0x568
   __DATA_CONST.__auth_ptr: 0x28
   __DATA.__objc_const: 0x4b18
-  __DATA.__objc_selrefs: 0x1bb8
+  __DATA.__objc_selrefs: 0x1ba0
   __DATA.__objc_ivar: 0x3c0
   __DATA.__objc_data: 0x1220
   __DATA.__data: 0x4a2
-  __DATA.__bss: 0x188
+  __DATA.__bss: 0x170
   __DATA.__common: 0x28
   __CGPreLoginApp.__cgpreloginapp: 0x0
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1147
-  Symbols:   742
-  CStrings:  2284
+  Functions: 1122
+  Symbols:   735
+  CStrings:  2264
 
Symbols:
- _AuthorizationMakeSafePlugin
- _AuthorizationRemoveSafePlugins
- _CFBundleCopyExecutableURL
- _SecRequirementCreateWithString
- _SecStaticCodeCheckValidity
- _SecStaticCodeCreateWithPath
- _dispatch_barrier_sync
CStrings:
+ "isSystemPlugin:"
+ "pathForPlugin:"
- "Actual number of connections = %d"
- "Clearing safe plugins cache"
- "Failed to create code requirement"
- "Failed to create static code for bundle %{public}@"
- "Failed to move plugin from %{public}@ to the safe location"
- "No safe path provided for %{public}@"
- "Passing request to the helper service with the safe path %{public}@"
- "Plugin %{public}@ eligibility check failed, plugin was not found"
- "Plugin is already at the safe path %{public}@"
- "Plugin not under SIP, requesting safe location"
- "SafePluginLoading"
- "The new safe location: %{public}@"
- "_plugin_safe_path"
- "anchor apple"
- "clearSafePluginCache"
- "com.apple.SecurityAgent.safePathQueue"
- "destroyRequest && _unprivilegedMechanismCreated"
- "initialize"
- "safePathForPlugin:"
- "safePluginLoadingEnabled"
- "setSafePathForPlugin:path:"
- "xpc_get_type(replyFromHelper) == XPC_TYPE_ERROR"
```
