## com.apple.driver.AppleSEPManager

> `com.apple.driver.AppleSEPManager`

```diff

-880.120.2.0.0
-  __TEXT.__cstring: 0x1124e
-  __TEXT.__const: 0x9517
-  __TEXT_EXEC.__text: 0x40f0c
+926.0.0.0.0
+  __TEXT.__cstring: 0x11437
+  __TEXT.__const: 0xded0
+  __TEXT_EXEC.__text: 0x419b4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x168
   __DATA.__common: 0xc48
   __DATA.__bss: 0x4e
-  __DATA_CONST.__auth_got: 0x578
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__auth_ptr: 0x38
   __DATA_CONST.__mod_init_func: 0xc0
   __DATA_CONST.__mod_term_func: 0xc0
-  __DATA_CONST.__const: 0x9c68
+  __DATA_CONST.__const: 0x9f30
   __DATA_CONST.__kalloc_type: 0xe00
   __DATA_CONST.__kalloc_var: 0x50
-  UUID: AACD64FC-0B89-39D2-A3E2-781FCB960BC0
-  Functions: 2490
+  __DATA_CONST.__auth_got: 0x580
+  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__auth_ptr: 0x38
+  UUID: C5E17BA6-3EF2-3278-89D5-71DF49574B61
+  Functions: 2516
   Symbols:   0
-  CStrings:  1458
+  CStrings:  1470
 
CStrings:
+ "\"SEP is being asked to sleep, but was never booted.\" @%s:%d"
+ "*out_struct.size_bytes_p >= sizeof(uint8_t) * epoch_slots_len"
+ "/arm-io/sep"
+ "AppleSEP:WARNING: %s: this command is removed\n"
+ "DispatchRemovedCommand"
+ "IOReturn AppleSEPXART::_xmsgSend(XARTMessage *, xart_buffer_config *, uint32_t)"
+ "IOReturn AppleSEPXART::_xmsgSendLocked(XARTMessage *, xart_buffer_config *, uint32_t *)"
+ "axi2af_parity_enable"
+ "bool AppleSEPManager::_hasMessageBox()"
+ "bool AppleSEPXART::_shouldHaveBootMessageTimeout()"
+ "no_monitors"
+ "out_struct.size_bytes_p != nullptr"
+ "sep_node"
+ "static IOReturn AppleSEPUserClient::DispatchGetEpochs(AppleSEPUserClient *, void *, IOExternalMethodArguments *)"
+ "timeout_ms != nullptr"
- "IOReturn AppleSEPXART::_xmsgSend(XARTMessage *, xart_buffer_config *)"
- "IOReturn AppleSEPXART::_xmsgSendLocked(XARTMessage *, xart_buffer_config *)"
- "USTUFF_LEN == piece_lens[PIECE_USTUFF]"

```
