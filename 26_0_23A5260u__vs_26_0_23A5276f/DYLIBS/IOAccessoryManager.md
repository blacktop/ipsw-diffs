## IOAccessoryManager

> `/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`

```diff

-1110.0.0.0.1
-  __TEXT.__text: 0x64424
-  __TEXT.__auth_stubs: 0x1580
+1116.0.0.0.0
+  __TEXT.__text: 0x645f4
+  __TEXT.__auth_stubs: 0x1590
   __TEXT.__objc_methlist: 0x2e74
   __TEXT.__const: 0x360
-  __TEXT.__cstring: 0x5b66
-  __TEXT.__oslogstring: 0xbb03
+  __TEXT.__cstring: 0x5b93
+  __TEXT.__oslogstring: 0xbb7d
   __TEXT.__gcc_except_tab: 0x9f8
   __TEXT.__ustring: 0x146
   __TEXT.__unwind_info: 0xd28

   __TEXT.__objc_methtype: 0xff9
   __TEXT.__objc_stubs: 0x5ce0
   __DATA_CONST.__got: 0x488
-  __DATA_CONST.__const: 0xe40
+  __DATA_CONST.__const: 0xe60
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_selrefs: 0x1e40
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__auth_got: 0xad0
+  __AUTH_CONST.__auth_got: 0xad8
   __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x4360
+  __AUTH_CONST.__cfstring: 0x43a0
   __AUTH_CONST.__objc_const: 0x4c20
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x48

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsysdiagnose.dylib
-  UUID: F4D9EBAE-A186-3B55-8B29-EE4350B89260
+  UUID: D8E0CD93-06BB-319C-91CC-80CEEF5E94B6
   Functions: 1793
-  Symbols:   6631
-  CStrings:  3892
+  Symbols:   6640
+  CStrings:  3898
 
Symbols:
+ -[ACCTransportIOAccessoryManager setFeaturesFromAuthStatus:authCert:certType:].cold.27
+ -[ACCTransportIOAccessorySharedManager basePortForService:]
+ -[ACCTransportIOAccessorySharedManager basePortForService:].cold.1
+ -[ACCTransportIOAccessorySharedManager basePortForService:].cold.2
+ _ACCUserDefaultsKey_DisableMFi4CertSupport
+ _ACCUserDefaultsKey_MFi4AuthTimeoutValueS
+ ___59-[ACCTransportIOAccessorySharedManager basePortForService:]_block_invoke
+ ___59-[ACCTransportIOAccessorySharedManager basePortForService:]_block_invoke_2
+ ___block_literal_global.292
+ ___block_literal_global.294
+ _kCFACCUserDefaultsKey_DisableMFi4CertSupport
+ _kCFACCUserDefaultsKey_MFi4AuthTimeoutValueS
+ _mfaa_certificateManager_determineCertificateType
+ _objc_msgSend$basePortForService:
+ _objc_msgSend$initWithSet:
- -[ACCTransportIOAccessorySharedManager _basePortForService:]
- -[ACCTransportIOAccessorySharedManager _basePortForService:].cold.1
- -[ACCTransportIOAccessorySharedManager _basePortForService:].cold.2
- ___60-[ACCTransportIOAccessorySharedManager _basePortForService:]_block_invoke
- ___60-[ACCTransportIOAccessorySharedManager _basePortForService:]_block_invoke_2
- ___block_literal_global.286
- ___block_literal_global.288
- _objc_msgSend$_basePortForService:
- _objc_msgSend$setWithSet:
Functions:
~ _IOAccMgrNotifyEvent : 1172 -> 1360
~ _PortNotifyEvent : 1284 -> 1320
~ -[ACCTransportIOAccessoryManager setFeaturesFromAuthStatus:authCert:certType:] : 4704 -> 4884
~ -[ACCTransportIOAccessoryManager ioAccessoryChildPorts] : 92 -> 104
~ -[ACCTransportIOAccessoryManager eaProtocolChildPorts] : 92 -> 104
~ -[ACCTransportIOAccessoryManager authCPChildPorts] : 92 -> 104
~ -[ACCTransportIOAccessoryManager oobPairingChildPorts] : 92 -> 104
~ -[ACCTransportIOAccessoryManager configStreamChildPorts] : 92 -> 104
CStrings:
+ "%s: certType %d -> %d"
+ "DisableMFi4CertSupport"
+ "IOAccMgrNotifyEvent: ACCTransportIOAccessoryConfigStream service has been removed"
+ "MFi4AuthTimeoutValueS"
+ "PortNotifyEvent: ACCTransportIOAccessoryPort service has been removed"
+ "basePortForService:"
+ "initWithSet:"
- "PortNotifyEvent: reference/service has been removed"
- "_basePortForService:"
- "setWithSet:"

```
