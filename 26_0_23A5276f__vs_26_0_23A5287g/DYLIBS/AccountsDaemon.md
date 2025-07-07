## AccountsDaemon

> `/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon`

```diff

-1016.0.0.0.0
-  __TEXT.__text: 0x7abcc
-  __TEXT.__auth_stubs: 0x16d0
-  __TEXT.__objc_methlist: 0x3ba4
-  __TEXT.__const: 0x99c
+1018.0.0.0.0
+  __TEXT.__text: 0x7aae4
+  __TEXT.__auth_stubs: 0x16e0
+  __TEXT.__objc_methlist: 0x3bac
+  __TEXT.__const: 0x9b4
   __TEXT.__oslogstring: 0x894a
   __TEXT.__cstring: 0x3c73
   __TEXT.__gcc_except_tab: 0x2574
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__swift5_typeref: 0x530
-  __TEXT.__swift5_capture: 0x1ec
+  __TEXT.__swift5_typeref: 0x546
+  __TEXT.__swift5_capture: 0x210
   __TEXT.__swift5_reflstr: 0x1db
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__constg_swiftt: 0x330

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x50
   __TEXT.__swift5_types: 0x34
-  __TEXT.__swift_as_entry: 0x38
-  __TEXT.__swift_as_ret: 0x38
-  __TEXT.__unwind_info: 0x1c38
-  __TEXT.__eh_frame: 0x880
+  __TEXT.__swift_as_entry: 0x34
+  __TEXT.__swift_as_ret: 0x30
+  __TEXT.__unwind_info: 0x1bf8
+  __TEXT.__eh_frame: 0x848
   __TEXT.__objc_classname: 0x61e
   __TEXT.__objc_methname: 0xb2f4
   __TEXT.__objc_methtype: 0x2473

   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0xb78
-  __AUTH_CONST.__const: 0xa88
+  __AUTH_CONST.__auth_got: 0xb80
+  __AUTH_CONST.__const: 0xb00
   __AUTH_CONST.__cfstring: 0x3240
   __AUTH_CONST.__objc_const: 0x4960
   __AUTH_CONST.__objc_intobj: 0xd8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 127CDE9F-D4F5-3A85-A7F8-5C58A79DDF8C
-  Functions: 2240
+  UUID: 3819ABFF-D28B-320F-BB0C-F70ED6ACDDD0
+  Functions: 2236
   Symbols:   7138
   CStrings:  3476
 
Symbols:
+ +[ACDAuthenticationPluginManager _sanitizeError:]
+ __OBJC_$_CLASS_METHODS_ACDAuthenticationPluginManager
+ ___93-[ACDAuthenticationPluginManager renewCredentialsForAccount:accountStore:options:completion:]_block_invoke.49
+ ___93-[ACDAuthenticationPluginManager renewCredentialsForAccount:accountStore:options:completion:]_block_invoke.49.cold.1
+ ___93-[ACDAuthenticationPluginManager renewCredentialsForAccount:accountStore:options:completion:]_block_invoke.63
+ ___95-[ACDAuthenticationPluginManager discoverPropertiesForAccount:accountStore:options:completion:]_block_invoke.84
+ ___block_descriptor_88_e8_32s40s48s56s64s72w_e20_v24?0q8"NSError"16ls32l8s40l8w72l8s48l8s56l8s64l8
+ _block_copy_helper.51
+ _block_copy_helper.59
+ _block_copy_helper.65
+ _block_descriptor.53
+ _block_descriptor.61
+ _block_descriptor.67
+ _block_destroy_helper.52
+ _block_destroy_helper.60
+ _block_destroy_helper.66
+ _objectdestroy.53Tm
+ _symbolic ___________pSgIegyg_ So30ACAccountCredentialRenewResultV s5ErrorP
- -[ACDAuthenticationPluginManager _sanitizeError:]
- ___93-[ACDAuthenticationPluginManager renewCredentialsForAccount:accountStore:options:completion:]_block_invoke.48
- ___93-[ACDAuthenticationPluginManager renewCredentialsForAccount:accountStore:options:completion:]_block_invoke.48.cold.1
- ___93-[ACDAuthenticationPluginManager renewCredentialsForAccount:accountStore:options:completion:]_block_invoke.62
- ___95-[ACDAuthenticationPluginManager discoverPropertiesForAccount:accountStore:options:completion:]_block_invoke.83
- ___block_descriptor_88_e8_32s40s48s56s64s72w_e20_v24?0q8"NSError"16ls32l8s40l8s48l8w72l8s56l8s64l8
- _block_copy_helper.46
- _block_copy_helper.48
- _block_copy_helper.64
- _block_descriptor.48
- _block_descriptor.50
- _block_descriptor.66
- _block_destroy_helper.47
- _block_destroy_helper.49
- _block_destroy_helper.65
- _objectdestroy.46Tm
- _objectdestroy.52Tm

```
