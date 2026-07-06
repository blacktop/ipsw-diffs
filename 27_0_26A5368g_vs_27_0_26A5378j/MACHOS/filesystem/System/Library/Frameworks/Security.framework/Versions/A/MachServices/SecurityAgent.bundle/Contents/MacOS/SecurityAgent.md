## SecurityAgent

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/MacOS/SecurityAgent`

```diff

-  __TEXT.__text: 0x2c694
-  __TEXT.__auth_stubs: 0x1280
-  __TEXT.__objc_stubs: 0x5500
-  __TEXT.__objc_methlist: 0x29f4
+  __TEXT.__text: 0x2c924
+  __TEXT.__auth_stubs: 0x1290
+  __TEXT.__objc_stubs: 0x5520
+  __TEXT.__objc_methlist: 0x29fc
   __TEXT.__const: 0x169
-  __TEXT.__cstring: 0x3147
+  __TEXT.__cstring: 0x315a
   __TEXT.__gcc_except_tab: 0x3e4
-  __TEXT.__oslogstring: 0x2f8c
-  __TEXT.__objc_methname: 0x5a5c
+  __TEXT.__oslogstring: 0x3060
+  __TEXT.__objc_methname: 0x5a84
   __TEXT.__objc_classname: 0x618
   __TEXT.__objc_methtype: 0x186a
   __TEXT.__ustring: 0x187e
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__unwind_info: 0xa28
+  __TEXT.__unwind_info: 0xa40
   __DATA_CONST.__const: 0x928
   __DATA_CONST.__cfstring: 0x2a60
   __DATA_CONST.__objc_classlist: 0x1d0

   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x950
-  __DATA_CONST.__got: 0x548
+  __DATA_CONST.__auth_got: 0x958
+  __DATA_CONST.__got: 0x560
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA.__objc_const: 0x4ab8
-  __DATA.__objc_selrefs: 0x1b88
-  __DATA.__objc_ivar: 0x3b4
+  __DATA.__objc_const: 0x4ad8
+  __DATA.__objc_selrefs: 0x1b90
+  __DATA.__objc_ivar: 0x3b8
   __DATA.__objc_data: 0x1220
   __DATA.__data: 0x4a2
   __DATA.__bss: 0x188

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1139
-  Symbols:   736
-  CStrings:  2578
+  Functions: 1145
+  Symbols:   738
+  CStrings:  2584
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ OBJC_IVAR_$_AgentMechanism._pluginUnavailable
+ _CFBundleIsArchitectureLoadable
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "AgentMechanism [%{public}@:%{public}@] plugin unavailable, falling back to no-op"
+ "No plugin at path: %{public}@, errno: %d (%s)"
+ "Plugin %{public}@ requires unsupported architecture"
+ "Plugin %{public}@ requires x86_64 but Rosetta is not available"
+ "_pluginUnavailable"
+ "plugin-unavailable"
+ "setPluginUnavailable"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "No plugin at path: %{public}@"

```
