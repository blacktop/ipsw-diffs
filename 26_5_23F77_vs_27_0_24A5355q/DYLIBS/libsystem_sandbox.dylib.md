## libsystem_sandbox.dylib

> `/usr/lib/system/libsystem_sandbox.dylib`

```diff

-2680.120.12.0.0
-  __TEXT.__text: 0x38ac
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__const: 0x178
-  __TEXT.__cstring: 0x77f
-  __TEXT.__unwind_info: 0x1d0
-  __DATA_CONST.__got: 0x8
-  __DATA_CONST.__const: 0x60
-  __AUTH_CONST.__auth_got: 0x1b8
+3033.0.0.0.1
+  __TEXT.__text: 0x3b58
+  __TEXT.__const: 0x180
+  __TEXT.__cstring: 0x84c
+  __TEXT.__unwind_info: 0x1e0
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x68
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0x13
   __DATA.__bss: 0x10
   __DATA_DIRTY.__bss: 0x8

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
