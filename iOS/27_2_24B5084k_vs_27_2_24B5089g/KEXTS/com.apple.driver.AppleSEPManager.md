## com.apple.driver.AppleSEPManager

> `com.apple.driver.AppleSEPManager`

```diff

-928.40.4.0.0
-  __TEXT.__cstring: 0x1178f
+928.40.6.0.0
+  __TEXT.__cstring: 0x117ff
   __TEXT.__const: 0xdee2
-  __TEXT_EXEC.__text: 0x438e4
+  __TEXT_EXEC.__text: 0x43900
   __TEXT_EXEC.__auth_stubs: 0xb20
   __DATA.__data: 0x168
   __DATA.__common: 0xc48

   __DATA_CONST.__auth_ptr: 0x38
   Functions: 2544
   Symbols:   0
-  CStrings:  1493
+  CStrings:  1494
 
Functions:
~ __ZN12AppleSEPXART22_handle_sep_driven_msgEPNS_11XARTMessageE : 2220 -> 2248
CStrings:
+ "AppleSEP:WARNING: Received unsupported SEP secure storage analytics version (%d), skipping\n"
+ "in_msg_p->length == analytics_payload_len"
+ "in_msg_p->length >= sizeof(analytics.version)"
- "analytics.version == 1"
- "in_msg_p->length == sizeof(xart_analytics_t)"
```
