## com.apple.driver.AppleSEPManager

> `com.apple.driver.AppleSEPManager`

```diff

-928.0.2.0.0
-  __TEXT.__cstring: 0xd406
+928.40.6.0.0
+  __TEXT.__cstring: 0xd476
   __TEXT.__const: 0x56c
-  __TEXT_EXEC.__text: 0x3044c
+  __TEXT_EXEC.__text: 0x30468
   __TEXT_EXEC.__auth_stubs: 0x920
   __DATA.__data: 0x168
   __DATA.__common: 0xb08

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 1773
   Symbols:   2133
-  CStrings:  1168
+  CStrings:  1169
 
Functions:
~ __ZN12AppleSEPXART22_handle_sep_driven_msgEPNS_11XARTMessageE : 2304 -> 2332
CStrings:
+ "AppleSEP:WARNING: Received unsupported SEP secure storage analytics version (%d), skipping\n"
+ "in_msg_p->length == analytics_payload_len"
+ "in_msg_p->length >= sizeof(analytics.version)"
- "analytics.version == 1"
- "in_msg_p->length == sizeof(xart_analytics_t)"
```
