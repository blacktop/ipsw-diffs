## authorizationhost

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/authorizationhost.bundle/Contents/MacOS/authorizationhost`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-55643.0.12.0.0
-  __TEXT.__text: 0x1af50
-  __TEXT.__auth_stubs: 0x1170
+55643.0.14.0.0
+  __TEXT.__text: 0x1a468
+  __TEXT.__auth_stubs: 0x10f0
   __TEXT.__lazy_helpers: 0x4ec
-  __TEXT.__objc_stubs: 0x1c60
-  __TEXT.__objc_methlist: 0x944
+  __TEXT.__objc_stubs: 0x1bc0
+  __TEXT.__objc_methlist: 0x924
   __TEXT.__const: 0x23d
-  __TEXT.__cstring: 0x1d4b
-  __TEXT.__objc_methname: 0x16a6
+  __TEXT.__cstring: 0x1cf4
+  __TEXT.__objc_methname: 0x1633
   __TEXT.__objc_classname: 0x1d9
   __TEXT.__objc_methtype: 0x799
-  __TEXT.__oslogstring: 0x2b45
+  __TEXT.__oslogstring: 0x28ee
   __TEXT.__gcc_except_tab: 0xf8
-  __TEXT.__unwind_info: 0x568
-  __DATA_CONST.__const: 0x4b0
-  __DATA_CONST.__cfstring: 0xb00
+  __TEXT.__unwind_info: 0x548
+  __DATA_CONST.__const: 0x490
+  __DATA_CONST.__cfstring: 0xae0
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0xb8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x8c8
+  __DATA_CONST.__auth_got: 0x888
   __DATA_CONST.__got: 0x210
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x1108
-  __DATA.__objc_selrefs: 0x7e8
+  __DATA.__objc_selrefs: 0x7b8
   __DATA.__objc_ivar: 0x84
   __DATA.__objc_data: 0x6e0
   __DATA.__lazy_load_got: 0x78
   __DATA.__data: 0x168
-  __DATA.__bss: 0xf8
+  __DATA.__bss: 0xe0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libcsfde.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpam.2.dylib
-  Functions: 778
-  Symbols:   507
-  CStrings:  998
+  Functions: 757
+  Symbols:   499
+  CStrings:  975
 
Symbols:
- _AuthorizationMakeSafePlugin
- _AuthorizationRemoveSafePlugins
- _CFBundleCopyBundleURL
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
- "bundlePath"
- "bundleWithURL:"
- "clearSafePluginCache"
- "com.apple.SecurityAgent.safePathQueue"
- "destroyRequest && _unprivilegedMechanismCreated"
- "initialize"
- "removeAllObjects"
- "safePathForPlugin:"
- "safePluginLoadingEnabled"
- "setSafePathForPlugin:path:"
- "xpc_get_type(replyFromHelper) == XPC_TYPE_ERROR"
```
