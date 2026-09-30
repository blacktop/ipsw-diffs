## com.apple.driver.AppleUSBDeviceNCM

> `com.apple.driver.AppleUSBDeviceNCM`

```diff

-397.0.0.0.0
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x103b
-  __TEXT_EXEC.__text: 0x8d40
-  __TEXT_EXEC.__auth_stubs: 0x650
+404.0.0.0.0
+  __TEXT.__cstring: 0x1009
+  __TEXT.__const: 0x80
+  __TEXT_EXEC.__text: 0x892c
+  __TEXT_EXEC.__auth_stubs: 0x630
   __DATA.__data: 0xc8
   __DATA.__common: 0xd8
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x3c10
+  __DATA_CONST.__const: 0x3bf0
   __DATA_CONST.__kalloc_type: 0x140
-  __DATA_CONST.__auth_got: 0x328
+  __DATA_CONST.__auth_got: 0x318
   __DATA_CONST.__got: 0xb8
-  Functions: 229
-  Symbols:   862
-  CStrings:  134
+  Functions: 225
+  Symbols:   855
+  CStrings:  131
 
Symbols:
+ __ZNK21AppleUSBDeviceNCMData11getFeaturesEv
- _ZN21AppleUSBDeviceNCMData17submitPacketGatedEPhj
- __ZN21AppleUSBDeviceNCMData17submitPacketGatedEPhj
- __ZN21AppleUSBDeviceNCMData21latchNCMControlConfigEv
- __ZN21AppleUSBDeviceNCMData22isTRMUnrestrictedByEDTEv
- __ZNK19IONetworkController11getFeaturesEv
- ____ZN21AppleUSBDeviceNCMData21latchNCMControlConfigEv_block_invoke
- _mbuf_adj
- _mbuf_copyback
CStrings:
- "disable-transport-rm"
- "ncm-no-trm"
- "submitPacketGated"
```
