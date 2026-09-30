## AppleKeyStore

> `/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore`

```diff

-2155.0.5.502.2
-  __TEXT.__text: 0x571e8
+2155.0.18.502.1
+  __TEXT.__text: 0x572f0
   __TEXT.__auth_stubs: 0x16b0
-  __TEXT.__const: 0xa4f0
-  __TEXT.__cstring: 0x2f43
-  __TEXT.__oslogstring: 0xf71
+  __TEXT.__const: 0xa540
+  __TEXT.__cstring: 0x2f53
+  __TEXT.__oslogstring: 0xf94
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__constg_swiftt: 0x730
   __TEXT.__swift5_typeref: 0x6b8

   __TEXT.__unwind_info: 0x1500
   __TEXT.__eh_frame: 0x18e8
   __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x5c10
+  __DATA_CONST.__const: 0x5c20
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0xb58

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: DC3E21F7-C424-3923-BE9A-671EA4FE3F16
-  Functions: 2520
-  Symbols:   3664
-  CStrings:  723
+  UUID: E783424F-16ED-3C74-A7FA-2A3F65349B87
+  Functions: 2521
+  Symbols:   3658
+  CStrings:  725
 
Symbols:
+ ___block_descriptor_tmp.127
+ ___block_descriptor_tmp.139
+ ___block_descriptor_tmp.149
+ ___block_descriptor_tmp.152
+ ___block_descriptor_tmp.168
+ ___block_literal_global.151
+ ___block_literal_global.154
+ ___block_literal_global.170
+ _convertMKBErrorToAKS
- ___block_descriptor_tmp.126
- ___block_descriptor_tmp.137
- ___block_descriptor_tmp.148
- ___block_descriptor_tmp.151
- ___block_descriptor_tmp.167
- ___block_literal_global.150
- ___block_literal_global.153
- ___block_literal_global.169
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_AppleKeyStore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_AppleKeyStore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_AppleKeyStore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_AppleKeyStore
Functions:
~ _OUTLINED_FUNCTION_4 : 16 -> 20
~ _aks_backup_unwrap_key : 212 -> 232
~ _AKSIdentityUnlockInternal : 632 -> 652
+ _convertMKBErrorToAKS
~ _AKSIdentityUnlockInternal.cold.5 : 200 -> 220
~ _AKSIdentityCopyGroupUUIDBytes.cold.1 : 204 -> 200
~ _AKSIdentityCopyGroupUUIDBytes.cold.2 : 204 -> 200
~ _AKSIdentityCopyUserUUIDBytes.cold.1 : 204 -> 200
~ _AKSIdentityCopyUserUUIDBytes.cold.2 : 204 -> 200
CStrings:
+ "/.exclave"
+ "Unexpected MobileKeyBag error: %d\n"

```
