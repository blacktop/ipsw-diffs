## cryptexctl.research

> `/System/Library/SecurityResearch/usr/bin/cryptexctl.research`

```diff

-475.80.3.0.0
-  __TEXT.__text: 0x2d4d4
-  __TEXT.__auth_stubs: 0x17f0
+493.101.1.0.0
+  __TEXT.__text: 0x2d238
+  __TEXT.__auth_stubs: 0x1850
   __TEXT.__objc_stubs: 0x20
-  __TEXT.__const: 0x615a
-  __TEXT.__cstring: 0xa924
-  __TEXT.__oslogstring: 0x3973
+  __TEXT.__const: 0x6162
+  __TEXT.__cstring: 0xa9a9
+  __TEXT.__oslogstring: 0x3a3a
   __TEXT.__ustring: 0xa
-  __TEXT.__gcc_except_tab: 0xf0
+  __TEXT.__gcc_except_tab: 0x114
   __TEXT.__objc_methname: 0x16
-  __TEXT.__unwind_info: 0x698
-  __DATA_CONST.__auth_got: 0xc08
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x5d50
-  __DATA_CONST.__cfstring: 0x640
+  __TEXT.__unwind_info: 0x6d8
+  __DATA_CONST.__auth_got: 0xc38
+  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__auth_ptr: 0x40
+  __DATA_CONST.__const: 0x5df0
+  __DATA_CONST.__cfstring: 0x660
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__subcommands: 0xb0
   __DATA_CONST.__objc_dupclass: 0x68
   __DATA.__objc_selrefs: 0x8
   __DATA.__data: 0x448
-  __DATA.__bss: 0xdc8
+  __DATA.__bss: 0xdd8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: F0B77573-BC83-344A-86DB-FD32D0C581BF
+  UUID: A6EB85F9-C7D6-31F0-BDCB-AB18B2FB0343
   Functions: 626
-  Symbols:   441
-  CStrings:  1521
+  Symbols:   447
+  CStrings:  1529
 
Symbols:
+ _AMDeviceCopyPersonalizationIdentifiersWithError
+ _CFDictionaryApplyFunction
+ _CFDictionaryCreateMutableCopy
+ _cryptex_attr_set_uninstall_flags
+ _cryptex_uninstall
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
- __cryptex_uninstall_by_name
CStrings:
+ "%{public}s: AMDeviceCopyPersonalizationIdentifiersWithError: %@"
+ "%{public}s: CFDictionaryCreateMutableCopy: %@"
+ "%{public}s: Device does not have Ap,SikaFuse"
+ "%{public}s: identifiers = %@"
+ "%{public}s: incomplete or invalid identifiers: %@"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/Symbols/cryptexctl.research"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/libcryptex_executables/cryptexctl/cmd/create.c"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/libcryptex_executables/hlutil/amfi.c"
+ "493.101.1"
+ "@(#)VERSION:Darwin Cryptex Management Interface Version 2.0.0: Sat Mar 15 18:20:31 PDT 2025; root:libcryptex_executables-493.101.1~13/cryptexctl/WEN_ETA_ARM64E"
+ "Ap,SikaFuse"
+ "B16@?0^{__CFError=}8"
+ "Darwin Cryptex Management Interface Version 2.0.0: Sat Mar 15 18:20:31 PDT 2025; root:libcryptex_executables-493.101.1~13/cryptexctl/WEN_ETA_ARM64E"
+ "ESDM"
+ "ESDM = %#x"
+ "Failed to bootstrap cryptex contents."
+ "Failed to start session"
+ "Failed to unload cryptex trust cache."
+ "No matching cryptex found"
+ "Session %s not found"
+ "V:o:rI:HqA:R:B:C:E:D:P:S:p:s:N:F:T:Y:L:d:M"
+ "_amfi_load_trust_cache"
+ "assertion failure: \"(*__error())\" -> %llu"
+ "assertion failure: \"bytes > 0\" -> %llu"
+ "assertion failure: \"error\" -> %llu"
+ "assertion failure: \"fcheck_np(cursor, fr, 1)\" -> %llu"
+ "assertion failure: \"kr\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_destroy(&sfa)\" -> %llu"
+ "assertion failure: \"strstr(path, mntpath) == path\" -> %llu"
+ "assertion failure: \"strstr(path, root_path) == path\" -> %llu"
+ "assertion failure: \"trust_cache_rem_cfg_str_valid(rem_cfg_str)\" -> %llu"
+ "could not find AppleMobileFileIntegrity %{darwin.errno}d"
+ "uninstall failed\n%s"
- "%{public}s: incomplete or invalid query results: %@"
- ".."
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Binaries/libcryptex_executables/install/Symbols/cryptexctl.research"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/libcryptex_executables/cryptexctl/cmd/create.c"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/libcryptex_executables/hlutil/amfi.c"
- "0x"
- "475.80.3"
- "@(#)VERSION:Darwin Cryptex Management Interface Version 2.0.0: Thu Dec 19 22:57:58 PST 2024; root:libcryptex_executables-475.80.3~217/cryptexctl/WEN_ETA_ARM64E"
- "Darwin Cryptex Management Interface Version 2.0.0: Thu Dec 19 22:57:58 PST 2024; root:libcryptex_executables-475.80.3~217/cryptexctl/WEN_ETA_ARM64E"
- "No matching cryptex found in the bundle"
- "Session not found"
- "V:o:rI:HqA:R:B:C:E:D:P:S:p:s:N:F:T:Y:L:M"
- "amfi_load_trust_cache"
- "assertion failure: \"(*__error())\" -> %lld"
- "assertion failure: \"bytes > 0\" -> %lld"
- "assertion failure: \"error\" -> %lld"
- "assertion failure: \"fcheck_np(cursor, fr, 1)\" -> %lld"
- "assertion failure: \"kr\" -> %lld"
- "assertion failure: \"posix_spawn_file_actions_destroy(&sfa)\" -> %lld"
- "assertion failure: \"strstr(path, mntpath) == path\" -> %lld"
- "assertion failure: \"strstr(path, root_path) == path\" -> %lld"
- "assertion failure: \"trust_cache_rem_cfg_str_valid(rem_cfg_str)\" -> %lld"
- "could not find AppleMobileFileIntegrity"
- "dt"
- "os"
- "uninstall failed"

```
