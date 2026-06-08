## libsystem_sandbox.dylib

> `/usr/lib/system/libsystem_sandbox.dylib`

```diff

-2680.120.12.0.0
-  __TEXT.__text: 0x38ac sha256:aefad3d5279e9a6582350f092fdd706540caec29c78cad8bfb54bdfdb33dae2f
-  __TEXT.__auth_stubs: 0x370 sha256:173908af3858c97f963caa55abcbeea6147460be9920db4e7757311a5311644a
-  __TEXT.__const: 0x178 sha256:c9c8a502ebe8b848dd4aec13344b24b53b5719af1578f3d97be44b2f798f9dd1
-  __TEXT.__cstring: 0x77f sha256:d8f45c029d71fdb3993c731fe5c95b0a8abb98baa1945b3926d1b262ca9b7473
-  __TEXT.__unwind_info: 0x1d0 sha256:cf67de275468fa972c952c06657f484ca973a84efd817438be60b32c62a616af
-  __DATA_CONST.__got: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
-  __DATA_CONST.__const: 0x60 sha256:447820b2117285e707a101a35673e2ab456ad3ee1185a2e8cc4e782469516a73
-  __AUTH_CONST.__auth_got: 0x1b8 sha256:360d579dbd14759b41afdf7fb5e80c0101e15150ae401d59f92a1e32d129f7cb
-  __AUTH_CONST.__const: 0x20 sha256:2d5cee33096bd186f3ae351fa9f03f8795b0722e969ea124f12a254c7fdd442e
+3033.0.0.0.1
+  __TEXT.__text: 0x3b58 sha256:0ee4b2c31199333524a8e443a38ae9a16dc5b1eaaa955e9276b8a1d305a014f3
+  __TEXT.__const: 0x180 sha256:e3f48a7a1f15d15279d8a32234a8da8144382c45251ac9e59e6531cbbc09cf51
+  __TEXT.__cstring: 0x84c sha256:a076726a4f331d091d17fad18bfab59e1165c45dbd2a51061834153814a98e38
+  __TEXT.__unwind_info: 0x1e0 sha256:d15b1d2a725c214384e1043b0f71559ac89b21a2ad8fdccd679743b1de36b527
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x68 sha256:e4e5b90ed47055634dbc98f9d66cc969b0394df8d736c71ef036a0a1e0dc3dcb
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x20 sha256:33c630395646bca4bfae5f5051f92c9ed658576be9a22d406152f619e2a8ad01
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0x13 sha256:aa2e47914c2266a5e7c77ea7a3640a9c1961c5aa652dfab0191b130258fd693a
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA_DIRTY.__bss: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  UUID: 7E03CA28-58FC-3B57-B0AB-739B9C7B206F
-  Functions: 135
-  Symbols:   256
-  CStrings:  70
+  UUID: 28C0D8B3-0977-38E5-BCC1-FD87E56C1487
+  Functions: 142
+  Symbols:   267
+  CStrings:  75
 
Symbols:
+ _kSandboxAppDataProtectionAnySigningId
+ _kSandboxAppDataProtectionPlatformTeamId
+ _sandbox_approval_category_fixup
+ _sandbox_check_and_query_approval_category
+ _sandbox_check_asr_parser
+ _sandbox_check_with_attrs
+ _sandbox_clear_approval_cache
+ _sandbox_integrity_check_app_bundle
+ _sandbox_register_app_data_protection
+ _sandbox_register_app_data_protection_exception
+ _sandbox_register_app_data_protection_package_exception
- __sandbox_register_app_bundle_0
- __sandbox_register_app_bundle_1
CStrings:
+ "%s: failed: %s storage class changed before protection"
+ "asr-parser-enter"
+ "kTCCServiceMediaLibrary-iMovie"
+ "sandbox_register_app_data_protection_exception"
+ "sandbox_register_app_data_protection_package_exception"

```
