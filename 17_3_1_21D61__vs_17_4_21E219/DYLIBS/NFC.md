## NFC

> `/System/Library/CoreAccessories/PlugIns/Transports/NFC.transport/NFC`

```diff

-898.80.3.0.0
-  __TEXT.__text: 0xb6a8
+919.100.33.0.0
+  __TEXT.__text: 0xb740
   __TEXT.__auth_stubs: 0x790
   __TEXT.__objc_methlist: 0x218
-  __TEXT.__cstring: 0xa3f
-  __TEXT.__const: 0x12b0
-  __TEXT.__oslogstring: 0x17a1
+  __TEXT.__cstring: 0xb41
+  __TEXT.__const: 0x1330
+  __TEXT.__oslogstring: 0x17a2
   __TEXT.__gcc_except_tab: 0x80
   __TEXT.__dlopen_cstrs: 0xc2
   __TEXT.__unwind_info: 0x1d0
   __TEXT.__objc_classname: 0x67
-  __TEXT.__objc_methname: 0xdb0
+  __TEXT.__objc_methname: 0xdc2
   __TEXT.__objc_methtype: 0x38a
   __TEXT.__objc_stubs: 0xd80
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x728
+  __DATA_CONST.__const: 0x7b8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x7c0
   __DATA_CONST.__objc_selrefs: 0x3b8
+  __DATA_CONST.__objc_classrefs: 0x70
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__cfstring: 0xbc0
+  __AUTH_CONST.__cfstring: 0xce0
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__objc_const: 0xd8
   __AUTH_CONST.__objc_intobj: 0x30

   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x3d8
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_classrefs: 0x70
-  __DATA.__objc_superrefs: 0x8
   __DATA.__objc_ivar: 0x50
   __DATA.__data: 0x120
   __DATA.__bss: 0x90

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 189
-  Symbols:   914
-  CStrings:  457
+  Symbols:   932
+  CStrings:  468
 
Symbols:
+ -[AccessoryTransportPluginNFC _requiresMfi40Auth:].cold.1
+ _ACCUserDefaultsKey_ForceAccInfoUpdateRelaySupport
+ _ACCUserDefaultsKey_ForceMFi4AuthOverNFC
+ _ACCUserDefaultsKey_IgnoreAccInfoUpdateRelaySupport
+ _ACCUserDefaultsKey_IgnoreAuthReset
+ _ACCUserDefaultsKey_MFi4ECDSADisallow
+ _ACCUserDefaultsKey_MFi4ECDSAOnly
+ _ACCUserDefaultsKey_MFi4SigmaIRequired
+ _ACCUserDefaultsKey_PacketLoggingPlainTextOnly
+ _ACCUserDefaultsKey_PretendNoDeviceIdentityCerts
+ ___block_literal_global.229
+ ___block_literal_global.231
+ _kCFACCUserDefaultsKey_ForceAccInfoUpdateRelaySupport
+ _kCFACCUserDefaultsKey_ForceMFi4AuthOverNFC
+ _kCFACCUserDefaultsKey_IgnoreAccInfoUpdateRelaySupport
+ _kCFACCUserDefaultsKey_IgnoreAuthReset
+ _kCFACCUserDefaultsKey_MFi4ECDSADisallow
+ _kCFACCUserDefaultsKey_MFi4ECDSAOnly
+ _kCFACCUserDefaultsKey_MFi4SigmaIRequired
+ _kCFACCUserDefaultsKey_PacketLoggingPlainTextOnly
+ _kCFACCUserDefaultsKey_PretendNoDeviceIdentityCerts
- -[AccessoryTransportPluginNFC sendOutgoingData:forEndpointWithUUID:connectionUUID:].cold.9
- ___block_literal_global.202
- ___block_literal_global.204
CStrings:
+ "%s: %@ requiresAuth %d -> %d"
+ "-[AccessoryTransportPluginNFC _requiresMfi40Auth:]"
+ "ForceAccInfoUpdateRelaySupport"
+ "ForceMFi4AuthOverNFC"
+ "IgnoreAccInfoUpdateRelaySupport"
+ "IgnoreAuthReset"
+ "MFi4ECDSADisallow"
+ "MFi4ECDSAOnly"
+ "MFi4SigmaIRequired"
+ "NFC transport plugin: _closeReaderSession: set _connectedTag = nil"
+ "NFC transport plugin: _closeReaderSession: set _readerSession = nil"
+ "NFC transport plugin: sendOutgoingData: sameTagId? %@ ?= %@"
+ "PacketLoggingPlainTextOnly"
+ "PretendNoDeviceIdentityCerts"
+ "T@\"NSString\",?,R,C"
- "NFC transport plugin: _closeReaderSession: _connectedTag = nil"
- "NFC transport plugin: _closeReaderSession: _readerSession = nil"
- "NFC transport plugin: sendOutgoingData"
- "NFC transport plugin: sendOutgoingData: sameTagId? %@ %@"

```
