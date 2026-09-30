## bputil

> `/usr/bin/bputil`

```diff

-265.80.1.0.0
-  __TEXT.__text: 0xb868
-  __TEXT.__auth_stubs: 0x650
+265.100.17.0.0
+  __TEXT.__text: 0xbf10
+  __TEXT.__auth_stubs: 0x640
   __TEXT.__objc_stubs: 0x680
-  __TEXT.__const: 0xcc0
-  __TEXT.__cstring: 0x3e07
+  __TEXT.__const: 0xcd0
+  __TEXT.__cstring: 0x3dbf
   __TEXT.__oslogstring: 0x160
   __TEXT.__gcc_except_tab: 0xe4
   __TEXT.__objc_methname: 0x414
-  __TEXT.__unwind_info: 0x1b8
-  __DATA_CONST.__auth_got: 0x338
+  __TEXT.__unwind_info: 0x1f8
+  __DATA_CONST.__auth_got: 0x330
   __DATA_CONST.__got: 0x110
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x450

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 57A79D66-CF4C-3166-8DAA-384232393D2C
-  Functions: 115
-  Symbols:   144
-  CStrings:  371
+  UUID: C4E51434-6D98-33A7-B780-5C0E095E8075
+  Functions: 194
+  Symbols:   143
+  CStrings:  368
 
Symbols:
- _bootpolicy_update_sip_flags
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/BootPolicy_executables/bputil/bputil.m"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/BootPolicy_executables/shared/image4.c"
+ "0.1.13"
+ "acm_context != ((void*)0)"
+ "image4_decode_local_policy(policy_data, policy_size, &output_decoded_policy, ((void*)0), 0)"
+ "p != ((void*)0)"
+ "p != ((void*)0) && p->type == 0x01"
+ "p != ((void*)0) && p->type == 0x02"
+ "p != ((void*)0) && p->type == 0x04 && p->value.data.size == 48"
+ "p != ((void*)0) && p->type == 0x04 && p->value.data.size == sizeof(env_data->vuid)"
+ "sip0_exists"
- "-V"
- "-h"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/BootPolicy_executables/bputil/bputil.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/BootPolicy_executables/shared/image4.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/tmp/bputil.XXXXXXXX"
- "0.1.12"
- "Failed to disable System Integrity Protection: %d"
- "acm_context != ((void *)0)"
- "image4_decode_local_policy(policy_data, policy_size, &output_decoded_policy, ((void *)0), 0)"
- "p != ((void *)0)"
- "p != ((void *)0) && p->type == 0x01"
- "p != ((void *)0) && p->type == 0x02"
- "p != ((void *)0) && p->type == 0x04 && p->value.data.size == 48"
- "p != ((void *)0) && p->type == 0x04 && p->value.data.size == sizeof(env_data->vuid)"

```
