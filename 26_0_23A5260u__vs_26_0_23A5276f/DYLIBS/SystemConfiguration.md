## SystemConfiguration

> `/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration`

```diff

-1385.0.0.0.0
-  __TEXT.__text: 0x79f58
-  __TEXT.__auth_stubs: 0x1f80
+1385.0.4.0.0
+  __TEXT.__text: 0x79a08
+  __TEXT.__auth_stubs: 0x1f10
   __TEXT.__const: 0x2b0
-  __TEXT.__cstring: 0x64db
+  __TEXT.__cstring: 0x64bf
   __TEXT.__oslogstring: 0x58b0
   __TEXT.__unwind_info: 0xca0
   __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0x2d38
-  __AUTH_CONST.__auth_got: 0xfc0
+  __DATA_CONST.__const: 0x2cc0
+  __AUTH_CONST.__auth_got: 0xf88
   __AUTH_CONST.__const: 0xbf0
   __AUTH_CONST.__cfstring: 0x6d20
   __DATA.__data: 0x158

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  UUID: BCFFF7AF-60DE-3CF2-86D0-2B67071E9AE7
-  Functions: 1286
-  Symbols:   3770
-  CStrings:  2913
+  UUID: A39EC146-A0A6-33BC-9B8A-31257C07C689
+  Functions: 1283
+  Symbols:   3748
+  CStrings:  2911
 
Symbols:
+ _____SCNetworkConnectionScheduleWithRunLoop_block_invoke.131
+ ___block_descriptor_tmp.111
+ ___block_descriptor_tmp.126
+ ___block_descriptor_tmp.128
+ ___block_descriptor_tmp.129
+ ___block_descriptor_tmp.133
+ ___block_descriptor_tmp.137
+ ___block_descriptor_tmp.90
+ ___block_literal_global.113
- _SCNetworkConnectionTriggerOnDemandIfNeeded.cold.1
- ___SCNetworkConnectionTriggerOnDemandIfNeeded_block_invoke
- ___SCNetworkConnectionTriggerOnDemandIfNeeded_block_invoke.cold.1
- ___SCNetworkConnectionTriggerOnDemandIfNeeded_block_invoke_2
- ___SCNetworkConnectionTriggerOnDemandIfNeeded_block_invoke_2.cold.1
- ___SCNetworkConnectionTriggerOnDemandIfNeeded_block_invoke_3
- _____SCNetworkConnectionScheduleWithRunLoop_block_invoke.137
- ___block_descriptor_tmp.139
- ___block_descriptor_tmp.140
- ___block_descriptor_tmp.142
- ___block_descriptor_tmp.28
- ___block_descriptor_tmp.96
- _dispatch_time
- _ne_session_copy_policy_match
- _ne_session_policy_match_get_service
- _ne_session_policy_match_get_service_action
- _ne_session_policy_match_get_service_type
- _proc_pidinfo
- _xpc_dictionary_set_bool
CStrings:
- "is-on-demand"
- "match-hostname"

```
