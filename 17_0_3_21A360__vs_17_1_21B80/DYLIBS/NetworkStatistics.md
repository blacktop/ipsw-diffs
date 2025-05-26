## NetworkStatistics

> `/System/Library/PrivateFrameworks/NetworkStatistics.framework/NetworkStatistics`

```diff

-195.0.6.0.0
-  __TEXT.__text: 0x2b7d4
-  __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_methlist: 0x3e34
-  __TEXT.__cstring: 0x403c
+195.40.3.0.0
+  __TEXT.__text: 0x2c3dc
+  __TEXT.__auth_stubs: 0xa80
+  __TEXT.__objc_methlist: 0x3f0c
+  __TEXT.__cstring: 0x40f5
   __TEXT.__oslogstring: 0x217d
   __TEXT.__const: 0x11c
   __TEXT.__gcc_except_tab: 0x2ec
-  __TEXT.__unwind_info: 0x9a0
-  __TEXT.__objc_classname: 0x4b5
-  __TEXT.__objc_methname: 0x7348
+  __TEXT.__unwind_info: 0x9d4
+  __TEXT.__objc_classname: 0x4ef
+  __TEXT.__objc_methname: 0x7504
   __TEXT.__objc_methtype: 0x7b54
-  __TEXT.__objc_stubs: 0x4900
+  __TEXT.__objc_stubs: 0x4a40
   __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x7f8
-  __DATA_CONST.__objc_classlist: 0x178
+  __DATA_CONST.__const: 0x818
+  __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6b50
-  __DATA_CONST.__objc_selrefs: 0x1820
+  __DATA_CONST.__objc_const: 0x6c38
+  __DATA_CONST.__objc_selrefs: 0x1870
   __DATA_CONST.__objc_arraydata: 0x228
-  __AUTH_CONST.__cfstring: 0x3cc0
-  __AUTH_CONST.__objc_const: 0xea0
+  __AUTH_CONST.__cfstring: 0x3d60
+  __AUTH_CONST.__objc_const: 0xf78
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x540
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_classrefs: 0x1c8
-  __DATA.__objc_superrefs: 0x110
-  __DATA.__objc_ivar: 0x718
+  __AUTH_CONST.__auth_got: 0x550
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_classrefs: 0x1d8
+  __DATA.__objc_superrefs: 0x120
+  __DATA.__objc_ivar: 0x728
   __DATA.__data: 0x508
   __DATA.__common: 0x18
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0xdc0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x60

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1466
-  Symbols:   4719
-  CStrings:  2426
+  Functions: 1482
+  Symbols:   4783
+  CStrings:  2447
 
Symbols:
+ +[NWStatsInterfaceRegistry sharedInstance]
+ -[NWStatsInterfaceRegistry .cxx_destruct]
+ -[NWStatsInterfaceRegistry addInterfaceIndexToRegistry:]
+ -[NWStatsInterfaceRegistry addVPNBytesForInterfaceIndex:fromSnapshot:]
+ -[NWStatsInterfaceRegistry getState]
+ -[NWStatsInterfaceRegistry init]
+ -[NWStatsInterfaceRegistry isTrackingInterfaceIndex:]
+ -[NWStatsInterfaceRegistry machOUUIDBelongsToVPNProvider:]
+ -[NWStatsInterfaceRegistry subtractVPNBytesForVPNProviderAppUUID:fromSnapshot:]
+ -[NWStatsInterfaceSource description]
+ -[NWStatsProtocolSnapshot donateBytesToAccumulator]
+ -[NWStatsProtocolSnapshot removeBytesFromAccumulator]
+ -[VPNInterfaceByteCountAccumulator addBytesToAttributeToVPNProviderFromSnapshot:]
+ -[VPNInterfaceByteCountAccumulator init]
+ -[VPNInterfaceByteCountAccumulator subtractBytesAttributedToVPNProviderFromSnapshot:]
+ _OBJC_CLASS_$_NWStatsInterfaceRegistry
+ _OBJC_CLASS_$_VPNInterfaceByteCountAccumulator
+ _OBJC_IVAR_$_NWStatsInterfaceRegistry._interfaceByteAccumulators
+ _OBJC_IVAR_$_NWStatsInterfaceRegistry._machOUUIDLookups
+ _OBJC_IVAR_$_NWStatsInterfaceRegistry._neQueriedInterfaceIndexes
+ _OBJC_IVAR_$_VPNInterfaceByteCountAccumulator._currentVPNInterfaceByteCounts
+ _OBJC_METACLASS_$_NWStatsInterfaceRegistry
+ _OBJC_METACLASS_$_VPNInterfaceByteCountAccumulator
+ __OBJC_$_CLASS_METHODS_NWStatsInterfaceRegistry
+ __OBJC_$_INSTANCE_METHODS_NWStatsInterfaceRegistry
+ __OBJC_$_INSTANCE_METHODS_VPNInterfaceByteCountAccumulator
+ __OBJC_$_INSTANCE_VARIABLES_NWStatsInterfaceRegistry
+ __OBJC_$_INSTANCE_VARIABLES_VPNInterfaceByteCountAccumulator
+ __OBJC_CLASS_RO_$_NWStatsInterfaceRegistry
+ __OBJC_CLASS_RO_$_VPNInterfaceByteCountAccumulator
+ __OBJC_METACLASS_RO_$_NWStatsInterfaceRegistry
+ __OBJC_METACLASS_RO_$_VPNInterfaceByteCountAccumulator
+ ___42+[NWStatsInterfaceRegistry sharedInstance]_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ _ne_session_map_interface_to_provider_uuid
+ _objc_msgSend$addBytesToAttributeToVPNProviderFromSnapshot:
+ _objc_msgSend$addInterfaceIndexToRegistry:
+ _objc_msgSend$addVPNBytesForInterfaceIndex:fromSnapshot:
+ _objc_msgSend$donateBytesToAccumulator
+ _objc_msgSend$isTrackingInterfaceIndex:
+ _objc_msgSend$machOUUIDBelongsToVPNProvider:
+ _objc_msgSend$removeBytesFromAccumulator
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$subtractBytesAttributedToVPNProviderFromSnapshot:
+ _objc_msgSend$subtractVPNBytesForVPNProviderAppUUID:fromSnapshot:
+ _sharedInstance.pred
+ _sharedInstance.sharedInstance
+ _uuid_unparse
CStrings:
+ "Accumulated interface bytes - %@"
+ "Looked up machO UUIDs - %@"
+ "NWStatsInterfaceRegistry"
+ "NWStatsInterfaceRegistry:"
+ "NWStatsInterfaceSource with srcref %lld interface %u threshold %lld"
+ "Queried interface indexes - %@"
+ "VPNInterfaceByteCountAccumulator"
+ "_currentVPNInterfaceByteCounts"
+ "_interfaceByteAccumulators"
+ "_machOUUIDLookups"
+ "_neQueriedInterfaceIndexes"
+ "addBytesToAttributeToVPNProviderFromSnapshot:"
+ "addInterfaceIndexToRegistry:"
+ "addVPNBytesForInterfaceIndex:fromSnapshot:"
+ "donateBytesToAccumulator"
+ "isTrackingInterfaceIndex:"
+ "machOUUIDBelongsToVPNProvider:"
+ "removeBytesFromAccumulator"
+ "sharedInstance"
+ "subtractBytesAttributedToVPNProviderFromSnapshot:"
+ "subtractVPNBytesForVPNProviderAppUUID:fromSnapshot:"

```
