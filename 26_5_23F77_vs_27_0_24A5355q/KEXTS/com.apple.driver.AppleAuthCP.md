## com.apple.driver.AppleAuthCP

> `com.apple.driver.AppleAuthCP`

```diff

-174.100.2.0.0
-  __TEXT.__const: 0x40 sha256:b3d8d7569faf25f26633991c970f0e77bd230596bec384e638631dcc77008d6c
-  __TEXT.__cstring: 0x292b sha256:cd3c3769fa31d5f31041f170cb59e79c8a6c6907f29d99582c227115d37fde59
-  __TEXT.__os_log: 0x12dd sha256:1d7673ac6aa36e6b294534431282fb2400792d7839b05b32ea216c63987299f5
-  __TEXT_EXEC.__text: 0x17ef4 sha256:321dc380e83a98495f9230ff0622a633716e95a0939c131ce9e4605263b40b32
+184.0.0.0.0
+  __TEXT.__const: 0x7c sha256:15dfa319a217f87107df3353daab83527f3fafcb31756297cf1da761af150326
+  __TEXT.__cstring: 0x2b50 sha256:ed9880b31836ae5778587f937060677277541f992c803608dd49fa8c329f7b05
+  __TEXT.__os_log: 0x16da sha256:df6659ac745e5a9f62deebaa1f76ddb1d8598829def050ab4d06efa60ad709c3
+  __TEXT_EXEC.__text: 0x1a414 sha256:2120f524ce84fb2046cc1a81f9326a631a7418e536c08f1f32665e91064e9f4a
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x188 sha256:0da68eebc8257debe11295e750571d7209b307405770a1eb03a57ea068026058
-  __DATA.__common: 0x218 sha256:7d73a488b95b99a42237504643b79aa49c55a9aad3cd97e58518f093d3e095df
+  __DATA.__data: 0x188 sha256:cf44043ba6c71858e3731ce96cd1d99d3f5c58ea1b1e5f4a6f07a7c114bec2ee
+  __DATA.__common: 0x240 sha256:1a0295f4bf5986c5f74eca9153a6a4cb10b073a01a76ba4a457fd862c78966a4
   __DATA.__bss: 0x2 sha256:96a296d224f285c67bee93c30f8a309157f0daa35dc5b87e410b78630a09cfc7
-  __DATA_CONST.__auth_got: 0x248 sha256:65a00aa6d4649535055a941efb3e887a3baf6a017c8c6c607f72f13b9b7322a3
-  __DATA_CONST.__got: 0xd0 sha256:cf42aca9aaf2c85362ae77d1936aac5b78090fa66be480a451c07ea0f97b8345
-  __DATA_CONST.__auth_ptr: 0x18 sha256:d3e4e53bb556cf3033581b8838d580426880f19f14730b165d65bfd75d228f15
-  __DATA_CONST.__mod_init_func: 0x48 sha256:667e84c8c393c2d800cad16e2991315c314710fb5ae98bb28568ad8f8b5b8593
-  __DATA_CONST.__mod_term_func: 0x48 sha256:1bc787209ed1848e4388e6210f87d74e74548061fa6a375a057d91f3e3b765ce
-  __DATA_CONST.__const: 0x58d8 sha256:2ce2aecaf6fd1119e90b92bc2f63b5aa912efdd983246c3d294422f4333656c4
-  __DATA_CONST.__kalloc_type: 0x6c0 sha256:b1e9fbe3d13fce824e88eee9c94a926f1bc6890a9cbde5632c2a3ba39c8aecb8
-  UUID: 591B00CD-3DFC-38A0-99A2-5D23CA6447F8
-  Functions: 584
+  __DATA_CONST.__mod_init_func: 0x50 sha256:5594169b167b2861ad9c201cdd4323dcdd0eb4624c3b5344abba38e39f4cb013
+  __DATA_CONST.__mod_term_func: 0x50 sha256:9db3596935cda04840fba4838acad8bbe6f30f371e74bb0480046ec4eee57ecd
+  __DATA_CONST.__const: 0x5f60 sha256:4fa106bb3f84870ec920ea2fdecdeae9fd23d34a558681590c3028cde8624757
+  __DATA_CONST.__kalloc_type: 0x780 sha256:00b7479cbce1b5ed59d2396e47d21d0c651abee2cd7230c3fa2e3699f965a224
+  __DATA_CONST.__auth_got: 0x248 sha256:16e0c23dc7c5bf550e5e5d481ecc87ee5ce282335daef5178a25538602d495f3
+  __DATA_CONST.__got: 0xd0 sha256:909f11c841fd71507a1f9bf58661982a99fb6cedb33c6fc3c1f01d2c31700293
+  __DATA_CONST.__auth_ptr: 0x18 sha256:86d0c3b4d612092c69fe0d4b678f21810803a6abbad30b1f3ed8fbd33d4bf6a9
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
