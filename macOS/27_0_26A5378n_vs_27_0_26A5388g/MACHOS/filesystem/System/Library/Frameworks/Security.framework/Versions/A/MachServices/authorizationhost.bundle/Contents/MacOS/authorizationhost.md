## authorizationhost

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/authorizationhost.bundle/Contents/MacOS/authorizationhost`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-55643.0.5.0.0
-  __TEXT.__text: 0x1b078
-  __TEXT.__auth_stubs: 0x1150
+55643.0.12.0.0
+  __TEXT.__text: 0x1af50
+  __TEXT.__auth_stubs: 0x1170
   __TEXT.__lazy_helpers: 0x4ec
-  __TEXT.__objc_stubs: 0x1c40
-  __TEXT.__objc_methlist: 0x93c
-  __TEXT.__const: 0x22d
-  __TEXT.__cstring: 0x1d39
-  __TEXT.__objc_methname: 0x1682
+  __TEXT.__objc_stubs: 0x1c60
+  __TEXT.__objc_methlist: 0x944
+  __TEXT.__const: 0x23d
+  __TEXT.__cstring: 0x1d4b
+  __TEXT.__objc_methname: 0x16a6
   __TEXT.__objc_classname: 0x1d9
-  __TEXT.__objc_methtype: 0x76c
+  __TEXT.__objc_methtype: 0x799
   __TEXT.__oslogstring: 0x2b45
   __TEXT.__gcc_except_tab: 0xf8
   __TEXT.__unwind_info: 0x568
-  __DATA_CONST.__const: 0x510
+  __DATA_CONST.__const: 0x4b0
   __DATA_CONST.__cfstring: 0xb00
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arraydata: 0xb8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x8b8
+  __DATA_CONST.__auth_got: 0x8c8
   __DATA_CONST.__got: 0x210
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA.__objc_const: 0x10e8
-  __DATA.__objc_selrefs: 0x7e0
-  __DATA.__objc_ivar: 0x80
+  __DATA.__objc_const: 0x1108
+  __DATA.__objc_selrefs: 0x7e8
+  __DATA.__objc_ivar: 0x84
   __DATA.__objc_data: 0x6e0
   __DATA.__lazy_load_got: 0x78
   __DATA.__data: 0x168

   - /usr/lib/libcsfde.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpam.2.dylib
-  Functions: 781
-  Symbols:   504
-  CStrings:  994
+  Functions: 778
+  Symbols:   507
+  CStrings:  998
 
Symbols:
+ OBJC_IVAR_$_AgentMechanism._stateLock
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "SafePluginLoading"
+ "_stateLock"
+ "safePluginLoadingEnabled"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
```
