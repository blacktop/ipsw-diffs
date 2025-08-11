## RemoteManagement

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement`

```diff

-580.0.0.0.0
-  __TEXT.__text: 0x46324
-  __TEXT.__auth_stubs: 0x1470
-  __TEXT.__objc_methlist: 0x1b68
-  __TEXT.__const: 0x13ec
-  __TEXT.__cstring: 0x2937
-  __TEXT.__oslogstring: 0x47eb
+582.0.0.0.0
+  __TEXT.__text: 0x48ac0
+  __TEXT.__auth_stubs: 0x1500
+  __TEXT.__objc_methlist: 0x1b88
+  __TEXT.__const: 0x13fc
+  __TEXT.__cstring: 0x2967
+  __TEXT.__oslogstring: 0x491b
   __TEXT.__gcc_except_tab: 0x4b8
-  __TEXT.__swift5_typeref: 0x60b
+  __TEXT.__swift5_typeref: 0x629
   __TEXT.__swift5_capture: 0x7c
-  __TEXT.__constg_swiftt: 0x988
-  __TEXT.__swift5_reflstr: 0x2e3
-  __TEXT.__swift5_fieldmd: 0x47c
+  __TEXT.__constg_swiftt: 0x9a0
+  __TEXT.__swift5_reflstr: 0x303
+  __TEXT.__swift5_fieldmd: 0x488
   __TEXT.__swift5_proto: 0xfc
   __TEXT.__swift5_types: 0x78
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xf28
-  __TEXT.__eh_frame: 0x16e0
+  __TEXT.__unwind_info: 0xf80
+  __TEXT.__eh_frame: 0x1810
   __TEXT.__objc_classname: 0x370
-  __TEXT.__objc_methname: 0x5948
-  __TEXT.__objc_methtype: 0x87b
-  __TEXT.__objc_stubs: 0x2e80
-  __DATA_CONST.__got: 0x580
+  __TEXT.__objc_methname: 0x5a03
+  __TEXT.__objc_methtype: 0x890
+  __TEXT.__objc_stubs: 0x2ec0
+  __DATA_CONST.__got: 0x588
   __DATA_CONST.__const: 0x638
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1370
+  __DATA_CONST.__objc_selrefs: 0x1388
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
-  __AUTH_CONST.__auth_got: 0xa48
+  __AUTH_CONST.__auth_got: 0xa90
   __AUTH_CONST.__const: 0xb50
   __AUTH_CONST.__cfstring: 0x1ae0
   __AUTH_CONST.__objc_const: 0x2e48
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__objc_data: 0x770
-  __AUTH.__data: 0xaa0
+  __AUTH.__objc_data: 0x778
+  __AUTH.__data: 0xab0
   __DATA.__objc_ivar: 0xc8
-  __DATA.__data: 0x6a0
+  __DATA.__data: 0x6b0
   __DATA.__bss: 0x20c0
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x460

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 88984390-2077-3D72-A200-1741775BE4E9
-  Functions: 1346
-  Symbols:   2961
-  CStrings:  1847
+  UUID: 1E2FC101-22A4-341B-8B85-AB694721D81C
+  Functions: 1368
+  Symbols:   2970
+  CStrings:  1856
 
Symbols:
+ +[RMManagedKeychainController removeAssetsNotMatchingStoreIdentifiers:scope:personaID:error:]
+ +[RMManagedKeychainController removeAssetsNotMatchingStoreIdentifiers:scope:personaID:error:].cold.1
+ _objc_msgSend$removeAssetsNotMatchingStoreIdentifiers:scope:persona:error:
+ _objc_msgSend$unassignAssetsNotMatchingStoreIdentifiers:scope:persona:error:
+ _symbolic SS3key_t
+ _symbolic _____ySSG s11_SetStorageC
+ _symbolic _____ySsG s23_ContiguousArrayStorageC
CStrings:
+ "Declaration key '%s' has unexpected format: does not match"
+ "Declaration key format is wrong: "
+ "Removing asset with key '%s' as it doesn't match valid store identifiers"
+ "Unassigning assets for configuration '%s' as it doesn't match valid store identifiers"
+ "removeAssetsNotMatchingStoreIdentifiers with %lu store identifiers"
+ "removeAssetsNotMatchingStoreIdentifiers:scope:persona:error:"
+ "removeAssetsNotMatchingStoreIdentifiers:scope:personaID:error:"
+ "unassignAssetsNotMatchingStoreIdentifiers:scope:persona:error:"

```
