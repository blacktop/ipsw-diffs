## ManagedConfiguration

> `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration`

```diff

-2432.62.4.0.0
-  __TEXT.__text: 0xf8f94
+2432.80.9.0.0
+  __TEXT.__text: 0xf931c
   __TEXT.__auth_stubs: 0x1760
   __TEXT.__objc_methlist: 0xb1fc
   __TEXT.__const: 0x13c4
-  __TEXT.__cstring: 0x17c4a
+  __TEXT.__cstring: 0x17cc9
   __TEXT.__oslogstring: 0x903f
-  __TEXT.__gcc_except_tab: 0x10c4
+  __TEXT.__gcc_except_tab: 0x10d4
+  __TEXT.__dlopen_cstrs: 0xac
   __TEXT.__ustring: 0x50
-  __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x3130
+  __TEXT.__unwind_info: 0x3158
   __TEXT.__objc_classname: 0xc99
-  __TEXT.__objc_methname: 0x1e303
+  __TEXT.__objc_methname: 0x1e312
   __TEXT.__objc_methtype: 0x236f
-  __TEXT.__objc_stubs: 0xdc40
+  __TEXT.__objc_stubs: 0xdc80
   __DATA_CONST.__got: 0xaa0
-  __DATA_CONST.__const: 0x4d28
+  __DATA_CONST.__const: 0x4d40
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d10
+  __DATA_CONST.__objc_selrefs: 0x5d20
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0xf8
   __AUTH_CONST.__auth_got: 0xbc0
   __AUTH_CONST.__const: 0x2090
-  __AUTH_CONST.__cfstring: 0x19260
+  __AUTH_CONST.__cfstring: 0x19280
   __AUTH_CONST.__objc_const: 0xd738
   __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH.__objc_data: 0x2328
   __DATA.__objc_ivar: 0x98c
   __DATA.__data: 0xc30
-  __DATA.__bss: 0xc59
+  __DATA.__bss: 0xc69
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x2f8
   __DATA_DIRTY.__bss: 0x208

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D4A2F657-CA0E-31B1-BAB1-63E565BF7C53
-  Functions: 5648
-  Symbols:   17396
-  CStrings:  12227
+  UUID: 14FBE772-9DEE-3D50-A345-0AC839ADE3B9
+  Functions: 5653
+  Symbols:   17411
+  CStrings:  12235
 
Symbols:
+ _LockdownModeLibraryCore.frameworkLibrary
+ _MCIsSystemLockdownModeEnabled
+ ___LockdownModeLibraryCore_block_invoke
+ ___getLockdownModeManagerClass_block_invoke
+ ___getLockdownModeManagerClass_block_invoke.cold.1
+ ___getLockdownModeManagerClass_block_invoke.cold.2
+ _audit_stringLockdownMode
+ _getLockdownModeManagerClass.softClass
+ _objc_msgSend$enabled
+ _objc_msgSend$shared
CStrings:
+ "Class getLockdownModeManagerClass(void)_block_invoke"
+ "LockdownModeManager"
+ "MCLockdownUtilities.m"
+ "enabled"
+ "shared"
+ "softlink:r:path:/System/Library/PrivateFrameworks/LockdownMode.framework/LockdownMode"
+ "void *LockdownModeLibrary(void)"

```
