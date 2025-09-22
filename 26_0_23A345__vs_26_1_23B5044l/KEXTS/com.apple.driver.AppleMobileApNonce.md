## com.apple.driver.AppleMobileApNonce

> `com.apple.driver.AppleMobileApNonce`

```diff

-49.0.0.0.0
-  __TEXT.__cstring: 0x1910
+51.0.0.0.0
+  __TEXT.__cstring: 0x1961
   __TEXT.__const: 0x12
-  __TEXT_EXEC.__text: 0x3fc0
+  __TEXT_EXEC.__text: 0x4018
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xc70
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: B8499CC4-57BA-32CA-BB2A-C85766F2B41E
+  UUID: D4C4DE8E-FD09-3403-8453-FC5958F72A52
   Functions: 102
   Symbols:   0
-  CStrings:  158
+  CStrings:  159
 
Functions:
~ __ZN18AppleMobileApNonce10_readNonceEPP8OSString : 852 -> 940
CStrings:
+ "%s%s:\n%s    _readNonce get slot info: possible_proposed_nonce_slot_state=%d, possible_proposed_nonce_slot_id=%d\n"
+ "%s%s:\n%s    _readNonce: get booted slot failed\n"
- "%s%s:\n%s    _readNonce get slot info: current_slot_state=%d, _nonce_slot_id=%d\n"

```
