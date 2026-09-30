## XOJIT

> `/System/Library/PrivateFrameworks/XOJIT.framework/XOJIT`

```diff

-83.0.0.0.0
-  __TEXT.__text: 0x255d08
+84.0.0.0.0
+  __TEXT.__text: 0x256438
   __TEXT.__init_offsets: 0x11c
-  __TEXT.__const: 0x1e79c
-  __TEXT.__oslogstring: 0x16e
+  __TEXT.__const: 0x1e7ac
+  __TEXT.__oslogstring: 0x1cd
   __TEXT.__swift5_typeref: 0x28a
-  __TEXT.__cstring: 0x7ba5b
+  __TEXT.__cstring: 0x7bb02
   __TEXT.__swift5_capture: 0x34
   __TEXT.__swift5_reflstr: 0x252
   __TEXT.__swift5_assocty: 0x28

   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x18
-  __DATA_CONST.__orc_runtime: 0x7b03b8
+  __DATA_CONST.__orc_runtime: 0x7b03b0
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x8da8
   __AUTH_CONST.__objc_const: 0x770
   __AUTH_CONST.__weak_auth_got: 0x48
-  __AUTH_CONST.__auth_got: 0x948
+  __AUTH_CONST.__auth_got: 0x968
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0xa68
   __DATA.__data: 0xb18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8523
-  Symbols:   10287
-  CStrings:  19850
+  Functions: 8524
+  Symbols:   10291
+  CStrings:  19855
 
Symbols:
+ __ZN4llvm3sys2fs14setPermissionsERKNS_5TwineENS1_5permsE
+ _chmod
+ _geteuid
+ _getpwuid_r
Functions:
~ __ZN4llvm6detail18UniqueFunctionBaseINS_8ExpectedINSt3__110unique_ptrINS_7jitlink20JITLinkMemoryManagerENS3_14default_deleteIS6_EEEEEEJRNS_3orc15SimpleRemoteEPCEEE8CallImplIZN5xojit12createXPCEPCEP17_xpc_connection_sjNS4_INSB_14TaskDispatcherENS7_ISJ_EEEEE3$_0EESA_PvSD_ : 2252 -> 3900
+ __ZN4llvm3sys2fs14setPermissionsERKNS_5TwineENS1_5permsE
CStrings:
+ "\", who will need to log in and run a preview to reset the permissions"
+ "). This directory is owned by user \""
+ "Could not reset permissions on oop-jit code file directory "
+ "Failed to set 0777 permissions on %{public}s: %{public}s"
+ "Failed to stat %{public}s: %{public}s"
```
