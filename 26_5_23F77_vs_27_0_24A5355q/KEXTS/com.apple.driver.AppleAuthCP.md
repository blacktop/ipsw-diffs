## com.apple.driver.AppleAuthCP

> `com.apple.driver.AppleAuthCP`

```diff

-174.100.2.0.0
-  __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x292b
-  __TEXT.__os_log: 0x12dd
-  __TEXT_EXEC.__text: 0x17ef4
+184.0.0.0.0
+  __TEXT.__const: 0x7c
+  __TEXT.__cstring: 0x2b50
+  __TEXT.__os_log: 0x16da
+  __TEXT_EXEC.__text: 0x1a414
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
-  __DATA.__common: 0x218
+  __DATA.__common: 0x240
   __DATA.__bss: 0x2
+  __DATA_CONST.__mod_init_func: 0x50
+  __DATA_CONST.__mod_term_func: 0x50
+  __DATA_CONST.__const: 0x5f60
+  __DATA_CONST.__kalloc_type: 0x780
   __DATA_CONST.__auth_got: 0x248
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__mod_init_func: 0x48
-  __DATA_CONST.__mod_term_func: 0x48
-  __DATA_CONST.__const: 0x58d8
-  __DATA_CONST.__kalloc_type: 0x6c0
-  UUID: 591B00CD-3DFC-38A0-99A2-5D23CA6447F8
-  Functions: 584
+  UUID: 068965E8-AFC9-3A2E-A7D8-EA3BD54FF661
+  Functions: 638
   Symbols:   0
-  CStrings:  419
+  CStrings:  457
 
CStrings:
+ "%s: Failed to access provider"
+ "%s: _read failed"
+ "%s: _write failed"
+ "%s: provider is not AppleAuthCPRelayInterface"
+ "%s: unexpected messageID: %x"
+ "%s: unexpected messageLength: %d"
+ "%s: unexpected startOfMessage: %d"
+ "%s:%s !certificate\n"
+ "%s:%s Found pack index on parent. Adding to componentIndex\n"
+ "%s:%s setProperty failed\n"
+ "%s:%s: A null buffer was provided!"
+ "%s:%s: Bus Error in SMC write: 0x%02X 0x%02X"
+ "%s:%s: Data + Address length %llu > Maximum %d"
+ "%s:%s: Data length %llu > Maximum %d"
+ "%s:%s: Data length is %llu but a null buffer was provided!"
+ "%s:%s: SMBS success"
+ "%s:%s: SMC Error in SMBC: 0x%02X"
+ "%s:%s: SMC Error in SMBD: 0x%02X"
+ "%s:%s: SMC Error in SMBG: 0x%02X"
+ "%s:%s: SMC Error in SMBS: 0x%02X"
+ "%s:%s: SMC Error in key write %u: 0x%02X"
+ "Area51AuthSMCRelayInterface"
+ "Area51AuthSMCRelayInterface::_read:%d: address:0x%x, failed:0x%x\n"
+ "Area51AuthSMCRelayInterface::_read:%d: data:0x%x, dataLength:%llu, failed:0x%x\n"
+ "Area51AuthSMCRelayInterface::_write:%d: address:0x%x, data:0x%x, dataLength:%d\n"
+ "Area51AuthSMCRelayInterface::transferData: Success!"
+ "Area51AuthSMCRelayInterface::transferData: Transfer failed after %d retries!"
+ "Area51AuthSMCRelayInterface::transferData:dir=%d add=%02x len=%llu"
+ "Area51AuthSMCRelayInterface::transferData:dir=%d add=NULL len=%llu"
+ "ComponentIndex"
+ "MogulAuthSMCRelayInterface::transferData: Success!"
+ "MogulAuthSMCRelayInterface::transferData: Transfer failed after %d retries!"
+ "MogulAuthSMCRelayInterface::transferData:dir=%d add=%02x len=%llu"
+ "MogulAuthSMCRelayInterface::transferData:dir=%d add=NULL len=%llu"
+ "PackIndex"
+ "ReadCommand response: %x %x %x %x %x %x %x %x %x %x %x %x\n"
+ "ReadCommand: %x %x %x %x %x %x %x %x %x %x %x %x\n"
+ "_getDeviceManufacturerData"
+ "_smcIICRegisterRead"
+ "_smcIICRegisterWrite"
+ "component-index"
+ "extSetCertificate"
+ "setCertificate"
+ "site.Area51AuthSMCRelayInterface"
- "%s: Failed to access MogulAuthSMCRelayInterface - This AuthCP service does not use I2C!"
- "%s: Failed to access MogulAuthSMCRelayInterface: Found %s"
- "MogulAuthSMCRelayInterface::_transferData: Success!"
- "MogulAuthSMCRelayInterface::_transferData: Transfer failed after %d retries!"
- "MogulAuthSMCRelayInterface::_transferData:dir=%d add=%02x len=%llu"
- "MogulAuthSMCRelayInterface::_transferData:dir=%d add=NULL len=%llu"

```
