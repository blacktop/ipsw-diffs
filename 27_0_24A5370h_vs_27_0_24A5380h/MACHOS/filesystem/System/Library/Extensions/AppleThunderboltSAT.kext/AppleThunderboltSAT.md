## AppleThunderboltSAT

> `/System/Library/Extensions/AppleThunderboltSAT.kext/AppleThunderboltSAT`

```diff

-  __TEXT.__cstring: 0x10b31
+  __TEXT.__cstring: 0x10dcf
   __TEXT.__const: 0x50
-  __TEXT_EXEC.__text: 0x23744
-  __TEXT_EXEC.__auth_stubs: 0x540
+  __TEXT_EXEC.__text: 0x23fe0
+  __TEXT_EXEC.__auth_stubs: 0x570
   __DATA.__data: 0x7f0
   __DATA.__common: 0x589
-  __DATA.__bss: 0x28
+  __DATA.__bss: 0x3c
   __DATA_CONST.__mod_init_func: 0x78
   __DATA_CONST.__mod_term_func: 0x78
   __DATA_CONST.__const: 0x4c18
   __DATA_CONST.__kalloc_type: 0x400
   __DATA_CONST.__kalloc_var: 0x2d0
-  __DATA_CONST.__auth_got: 0x2a0
+  __DATA_CONST.__auth_got: 0x2b8
   __DATA_CONST.__got: 0xe8
-  Functions: 552
-  Symbols:   3501
-  CStrings:  1019
+  Functions: 557
+  Symbols:   3535
+  CStrings:  1026
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ __Z20sat_push_msg_to_userPKcz
+ __Z22sat_clear_msgs_to_userv
+ __Z22sat_get_msg_to_user_atjR15sat_msg_to_user
+ __Z26sat_get_msgs_to_user_countR21sat_msg_to_user_count
+ __ZL14gSatMsgsToUser
+ __ZL17gSatMsgToUserLock
+ __ZL23gSatMsgsToUserTruncated
+ __ZN7OSArray12withCapacityEj
+ __ZNK23AppleThunderboltSATPort18getTBTRouterNumberEv
+ __ZZN23AppleThunderboltSATPort13sendDirectiveERK15sat_directive_tE20kalloc_type_view_809
+ __ZZN23AppleThunderboltSATPort13sendDirectiveERK15sat_directive_tE20kalloc_type_view_819
+ __ZZN23AppleThunderboltSATPort13sendDirectiveERK15sat_directive_tE20kalloc_type_view_883
+ _strlcpy
+ _vsnprintf
- __ZZN23AppleThunderboltSATPort13sendDirectiveERK15sat_directive_tE20kalloc_type_view_804
- __ZZN23AppleThunderboltSATPort13sendDirectiveERK15sat_directive_tE20kalloc_type_view_814
- __ZZN23AppleThunderboltSATPort13sendDirectiveERK15sat_directive_tE20kalloc_type_view_878
CStrings:
+ "1.0.101"
+ "112"
+ "21:03:53"
+ "Jun 30 2026"
+ "LinkDevice: routerID %d portID %d - remote ring mask is invalid, looks like sat-vsa=1 boot-arg missing on the capturing side"
+ "SATLinkDevice<%p>::activateInternal WARNING: looks like sat-vsa=1 boot-arg missing on the capturing side. routerID %d, portID %d, remote_tx_mask=%u, remote_rx_mask=%u"
+ "SATUserClient<%p>::externalMethod - kSAT_ClearMsgsToUser\n"
+ "SATUserClient<%p>::externalMethod - kSAT_GetMsgToUserByIndex - index = %llu\n"
+ "SATUserClient<%p>::externalMethod - kSAT_GetMsgToUserByIndex ERROR: sanitization check failed\n"
+ "SATUserClient<%p>::externalMethod - kSAT_GetMsgsToUserCount\n"
+ "SATUserClient<%p>::externalMethod - kSAT_GetMsgsToUserCount ERROR: sanitization check failed\n"
- "1.0.99"
- "109.0.0.0.1"
- "19:38:50"
- "Jun 18 2026"

```
