## com.apple.driver.AppleHIDTransportMailbox

> `com.apple.driver.AppleHIDTransportMailbox`

```diff

-9100.28.1.0.0
+9100.29.1.0.0
   __TEXT.__const: 0xb5
-  __TEXT.__cstring: 0x243d
-  __TEXT_EXEC.__text: 0x15b34
+  __TEXT.__cstring: 0x2539
+  __TEXT_EXEC.__text: 0x16080
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0x1a0
-  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__auth_got: 0x1a8
+  __DATA_CONST.__got: 0xc0
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x10f8
+  __DATA_CONST.__const: 0x1118
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 501C5E6F-0A1E-3749-9F19-A76D8206EE8C
-  Functions: 316
+  UUID: 3DDFF63B-0257-3404-AD07-B4E54D7FD618
+  Functions: 319
   Symbols:   0
-  CStrings:  247
+  CStrings:  252
 
CStrings:
+ "[0x%llx][%llx][%s::%s]: Aborting in-progress report for interface %u"
+ "[0x%llx][%llx][%s::%s]: Disabling access to mailbox"
+ "[0x%llx][%llx][%s::%s]: Endpoint power state change, new:%lu old%lu"
+ "disableAccessGated"
+ "handleEndpointPowerStateChange_block_invoke"

```
