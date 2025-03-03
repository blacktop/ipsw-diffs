## cryptexd

> `/usr/libexec/cryptexd`

```diff

-493.100.42.0.0
-  __TEXT.__text: 0x4a254
-  __TEXT.__auth_stubs: 0x1d20
+493.100.51.0.0
+  __TEXT.__text: 0x4a9a0
+  __TEXT.__auth_stubs: 0x1d30
   __TEXT.__objc_stubs: 0x1620
   __TEXT.__objc_methlist: 0x844
   __TEXT.__const: 0x9d8
-  __TEXT.__gcc_except_tab: 0x1880
+  __TEXT.__gcc_except_tab: 0x18e0
   __TEXT.__objc_methname: 0x1649
   __TEXT.__objc_classname: 0xf9
   __TEXT.__objc_methtype: 0x3c9
-  __TEXT.__cstring: 0x3438
-  __TEXT.__oslogstring: 0x972b
-  __TEXT.__unwind_info: 0xb70
-  __DATA_CONST.__auth_got: 0xea0
+  __TEXT.__cstring: 0x34d5
+  __TEXT.__oslogstring: 0x9859
+  __TEXT.__unwind_info: 0xb98
+  __DATA_CONST.__auth_got: 0xea8
   __DATA_CONST.__got: 0x250
-  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x2a30
   __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_classlist: 0x90

   - /System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement
   - /System/Library/PrivateFrameworks/WatchdogServiceManagement.framework/WatchdogServiceManagement
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libcryptex_core.dylib

   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 894
-  Symbols:   563
-  CStrings:  1752
+  Functions: 899
+  Symbols:   564
+  CStrings:  1764
 
Symbols:
+ _wd_optin_service_unregister_sync
CStrings:
+ "%{public}s: Failed to unregister services with watchdog."
+ ".registered-for-watchdog"
+ "493.100.51"
+ "@(#)VERSION:Darwin Cryptex Manager Version 2.0.0: Tue Feb 25 22:06:17 PST 2025; root:libcryptex_executables-493.100.51~484/cryptexd/RELEASE_ARM64E"
+ "Darwin Cryptex Manager Version 2.0.0: Tue Feb 25 22:06:17 PST 2025; root:libcryptex_executables-493.100.51~484/cryptexd/RELEASE_ARM64E"
+ "Failed to %{public}s job %zu with watchdog"
+ "Unregister jobs from watchdog [no error]"
+ "Unregister jobs from watchdog: %@"
+ "Unregistered job with watchdog: %{public}@"
+ "_quire_parse_watchdog_service_descriptions"
+ "_quire_unbootstrap_watchdog_registration"
+ "_watchdog_unbootstrap_service"
+ "register"
+ "unregister"
+ "watchdog_process_service_descriptions"
+ "wd_optin_service_unregister_sync failed for job: %{public}@ %{darwin.errno}d"
+ "wd_optin_service_unregister_sync not supported."
- "493.100.42"
- "@(#)VERSION:Darwin Cryptex Manager Version 2.0.0: Sun Feb 16 10:54:20 PST 2025; root:libcryptex_executables-493.100.42~194/cryptexd/RELEASE_ARM64E"
- "Darwin Cryptex Manager Version 2.0.0: Sun Feb 16 10:54:20 PST 2025; root:libcryptex_executables-493.100.42~194/cryptexd/RELEASE_ARM64E"
- "Failed to register job %zu with watchdog"
- "watchdog_bootstrap_service_descriptions"

```
