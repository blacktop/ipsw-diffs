## libCoreKE.dylib

> `/usr/lib/libCoreKE.dylib`

```diff

 0.0.0.0.0
-  __TEXT.__text: 0x1c6e8a0
-  __TEXT.__auth_stubs: 0x890
+  __TEXT.__text: 0x1a9f57c
+  __TEXT.__auth_stubs: 0x8b0
   __TEXT.__objc_stubs: 0x80
-  __TEXT.__const: 0xdd9a4
+  __TEXT.__const: 0xdd134
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__cstring: 0x1e53
+  __TEXT.__cstring: 0x1f56
   __TEXT.__objc_methname: 0x5b
-  __TEXT.__unwind_info: 0xab8
-  __TEXT.__eh_frame: 0x88
-  __DATA_CONST.__auth_got: 0x458
+  __TEXT.__unwind_info: 0xb80
+  __TEXT.__eh_frame: 0x80
+  __DATA_CONST.__auth_got: 0x468
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x1df80
+  __DATA_CONST.__const: 0x1ca60
   __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_selrefs: 0x20
-  __DATA.__data: 0x51a0
-  __DATA.__bss: 0x51
+  __DATA.__data: 0x5278
+  __DATA.__bss: 0x71
   __DATA.__common: 0xbb8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B4A8C3D0-0999-3A17-8566-20186FDBCCDA
-  Functions: 495
-  Symbols:   172
-  CStrings:  358
+  UUID: B35E20DD-CC41-3760-8812-83A672248B3F
+  Functions: 751
+  Symbols:   174
+  CStrings:  366
 
Symbols:
+ _ccder_sizeof_implicit_raw_octet_string
+ _vsnprintf
CStrings:
+ "%s:%s%d{%s}:%s%s%s%s%s%u:%s %s%s%s[%04zu,%04zu): %s%s%s%s\n"
+ "%s:%s%d{%s}:%s%s%s%s%s%u:%s %sdump %s (len = %zd)%s%s\n"
+ "%s:%s%d{%s}:%s%s%s%s%s%u:%s Failed to load in-kernel backup bag: 0x%08x%s\n"
+ "%s:%s%d{%s}:%s%s%s%s%s%u:%s Failed to unlock in-kernel backup bag with prederived secret: 0x%08x%s\n"
+ "%s:%s%d{%s}:%s%s%s%s%s%u:%s Failed to unlock in-kernel backup bag: 0x%08x%s\n"
+ "%s:%s%d{%s}:%s%s%s%s%s%u:%s Failed to unwrap backup bag as DER: 0x%08x%s\n"
+ "%s:%s%d{%s}:%s%s%s%s%s%u:%s Unwrapped DER backup bag%s\n"
+ "%s:%s%d{%s}:%s%s%s%s%s%u:%s aks connection failed%s\n"
+ "%s:%s%d{%s}:%s%s%s%s%s%u:%s bad 1%s\n"
+ "%s:%s%d{%s}:%s%s%s%s%s%u:%s bad 2%s\n"
+ "%s:%s%d{%s}:%s%s%s%s%s%u:%s fail%s\n"
+ "%s:%s%d{%s}:%s%s%s%s%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n"
+ "%s:%s%d{%s}:%s%s%s%s%s%u:%s ioreg: %d, boot_arg: %d%s\n"
+ "%s:%s%d{%s}:%s%s%s%s%s%u:%s overflow%s\n"
+ "AKSGetStashStats"
+ "_aks_backup_enable_volume"
+ "_aks_change_secret_epilogue"
+ "_aks_recover_with_escrow_bag"
+ "_aks_se_get_reset_token_for_memento_secret"
+ "_aks_set_configuration"
+ "_aks_set_system_with_passcode"
+ "_aks_unlock_bag"
+ "_aks_unlock_with_sync_bag"
+ "aks_change_secret_with_kek"
+ "aks_enable_cache_flow"
+ "aks_get_icsc_srp"
+ "aks_reset_iteration_count"
+ "aks_se_get_passcode_derivation"
+ "aks_se_memento_secret_drop"
+ "aks_se_recover_with_acm"
+ "aks_unlock_device_with_acm"
- "%s%s:%s%s%s%s%u:%s%u:%s %s%s%s[%04zu,%04zu): %s%s%s%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s %sdump %s (len = %zd)%s%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to load in-kernel backup bag: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to unlock in-kernel backup bag with prederived secret: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to unlock in-kernel backup bag: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to unwrap backup bag as DER: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Unwrapped DER backup bag%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s aks connection failed%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s bad 1%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s bad 2%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s fail%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s ioreg: %d, boot_arg: %d%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s overflow%s\n"
- "aks_backup_enable_volume"
- "aks_change_secret_epilogue"
- "aks_change_secret_opts"
- "aks_recover_with_escrow_bag"
- "aks_se_get_reset_token_for_memento_secret"
- "aks_set_configuration"
- "aks_set_system_with_passcode"
- "aks_unlock_bag"
- "aks_unlock_with_sync_bag"

```
