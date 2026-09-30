## SecurityAgent

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/MacOS/SecurityAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-55643.0.5.0.0
-  __TEXT.__text: 0x2c924
-  __TEXT.__auth_stubs: 0x1290
-  __TEXT.__objc_stubs: 0x5520
-  __TEXT.__objc_methlist: 0x29fc
+55643.0.12.0.0
+  __TEXT.__text: 0x2cdfc
+  __TEXT.__auth_stubs: 0x12b0
+  __TEXT.__objc_stubs: 0x55c0
+  __TEXT.__objc_methlist: 0x2a0c
   __TEXT.__const: 0x169
-  __TEXT.__cstring: 0x315a
-  __TEXT.__gcc_except_tab: 0x3e4
+  __TEXT.__cstring: 0x316c
+  __TEXT.__gcc_except_tab: 0x404
   __TEXT.__oslogstring: 0x3060
-  __TEXT.__objc_methname: 0x5a84
+  __TEXT.__objc_methname: 0x5acd
   __TEXT.__objc_classname: 0x618
-  __TEXT.__objc_methtype: 0x186a
+  __TEXT.__objc_methtype: 0x1897
   __TEXT.__ustring: 0x187e
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__unwind_info: 0xa40
-  __DATA_CONST.__const: 0x928
+  __TEXT.__unwind_info: 0xa48
+  __DATA_CONST.__const: 0x958
   __DATA_CONST.__cfstring: 0x2a60
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x958
-  __DATA_CONST.__got: 0x560
+  __DATA_CONST.__auth_got: 0x968
+  __DATA_CONST.__got: 0x568
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA.__objc_const: 0x4ad8
-  __DATA.__objc_selrefs: 0x1b90
-  __DATA.__objc_ivar: 0x3b8
+  __DATA.__objc_const: 0x4b18
+  __DATA.__objc_selrefs: 0x1bb8
+  __DATA.__objc_ivar: 0x3c0
   __DATA.__objc_data: 0x1220
   __DATA.__data: 0x4a2
   __DATA.__bss: 0x188

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1145
-  Symbols:   738
-  CStrings:  2276
+  Functions: 1147
+  Symbols:   742
+  CStrings:  2284
 
Symbols:
+ OBJC_IVAR_$_AgentMechanism._stateLock
+ _OBJC_CLASS_$_NSInvocation
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "SafePluginLoading"
+ "_stateLock"
+ "invocationWithMethodSignature:"
+ "methodSignatureForSelector:"
+ "safePluginLoadingEnabled"
+ "setArgument:atIndex:"
+ "setSelector:"
+ "setTarget:"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "beginSheetModalForWindow:modalDelegate:didEndSelector:contextInfo:"
```
