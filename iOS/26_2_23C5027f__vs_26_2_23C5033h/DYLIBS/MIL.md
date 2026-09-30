## MIL

> `/System/Library/PrivateFrameworks/MIL.framework/MIL`

```diff

-3505.3.2.0.0
-  __TEXT.__text: 0x601978
+3510.2.1.0.0
+  __TEXT.__text: 0x601970
   __TEXT.__auth_stubs: 0xdc0
   __TEXT.__const: 0x3ea75
   __TEXT.__gcc_except_tab: 0x92c24
   __TEXT.__cstring: 0x13831
-  __TEXT.__oslogstring: 0x2fd
+  __TEXT.__oslogstring: 0x2fe
   __TEXT.__unwind_info: 0x166c0
   __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__const: 0x540

   __DATA.__common: 0x9f8
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 6770AF03-8B47-399F-ADBF-18CF7BC285FA
+  UUID: D74232B0-4BD4-3399-969D-69A7F96DDA36
   Functions: 17605
   Symbols:   56776
   CStrings:  2704
Functions:
~ __ZZN3MIL9Operators6Common5ios1512_GLOBAL__N_118ValidateLSTMHelperENSt3__110shared_ptrIKNS_8LocationEEEPKNS_17IRTensorValueTypeESB_SB_SB_PKNS_11IRValueTypeESE_NS4_12basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEESE_SE_SE_SE_ENK3$_0clESB_SB_RKSK_SN_RNS4_6vectorIiNSI_IiEEEESR_.cold.2 : 44 -> 36
CStrings:
+ "ProgramHashUtils::ValidateMemoryConstraints: Total estimated constant size (%zu bytes) significantly exceeds memory limit (%llu bytes) - consider adjusting maxConstantMemoryUsage"
- "ProgramHashUtils::ValidateMemoryConstraints: Total estimated constant size (%zu bytes) significantly exceeds memory limit (%zu bytes) - consider adjusting maxConstantMemoryUsage"

```
