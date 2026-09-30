## NearbyInteraction

> `/System/Library/Frameworks/NearbyInteraction.framework/Versions/A/NearbyInteraction`

```diff

-  __TEXT.__text: 0x37370
-  __TEXT.__objc_methlist: 0x4098
-  __TEXT.__gcc_except_tab: 0x56c0
-  __TEXT.__cstring: 0x51e4
-  __TEXT.__const: 0x4e0
+  __TEXT.__text: 0x378a4
+  __TEXT.__objc_methlist: 0x40e8
+  __TEXT.__gcc_except_tab: 0x5748
+  __TEXT.__cstring: 0x525c
+  __TEXT.__const: 0x500
   __TEXT.__oslogstring: 0xe6b
   __TEXT.__swift5_typeref: 0x83
   __TEXT.__swift5_reflstr: 0x4b

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x2030
+  __TEXT.__unwind_info: 0x2060
   __TEXT.__eh_frame: 0x100
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x590
+  __DATA_CONST.__const: 0x598
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e00
+  __DATA_CONST.__objc_selrefs: 0x1e38
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0x40
-  __DATA_CONST.__got: 0x290
-  __AUTH_CONST.__const: 0xb68
-  __AUTH_CONST.__cfstring: 0x5960
-  __AUTH_CONST.__objc_const: 0x7668
+  __DATA_CONST.__got: 0x2b0
+  __AUTH_CONST.__const: 0xb88
+  __AUTH_CONST.__cfstring: 0x5a00
+  __AUTH_CONST.__objc_const: 0x76c8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x3d0
-  __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x4e4
+  __DATA.__objc_ivar: 0x4ec
   __DATA.__data: 0x3d0
   __DATA.__common: 0x12d
   __DATA.__bss: 0x580
-  __DATA_DIRTY.__objc_data: 0xcd0
+  __DATA_DIRTY.__objc_data: 0x10e0
   __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1528
-  Symbols:   3884
-  CStrings:  1633
+  Functions: 1536
+  Symbols:   3902
+  CStrings:  1643
 
Sections:
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
Symbols:
+ -[NIDLTDOAMeasurement initWithAnchorAddress:clusterInitiatorAddress:measurementType:coordinatesType:transmitTime:rawTransmitTime:receiveTime:rawReceiveTime:signalStrength:carrierFrequencyOffset:responderClockFrequencyOffset:coordinates:floorElevation:]
+ -[NIDLTDOAMeasurement rawReceiveTime]
+ -[NIDLTDOAMeasurement rawTransmitTime]
+ -[NIDLTDOAMeasurement setRawReceiveTime:]
+ -[NIDLTDOAMeasurement setRawTransmitTime:]
+ -[NISystemEventNotifier _setSMBClkCfg:]
+ GCC_except_table334
+ GCC_except_table335
+ GCC_except_table339
+ GCC_except_table345
+ OBJC_IVAR_$_NIDLTDOAMeasurement._rawReceiveTime
+ OBJC_IVAR_$_NIDLTDOAMeasurement._rawTransmitTime
+ __NISystemEventDictKey_SMBClkCfgValue
+ ___39-[NISystemEventNotifier _setSMBClkCfg:]_block_invoke
+ ___39-[NISystemEventNotifier _setSMBClkCfg:]_block_invoke_2
+ _objc_msgSend$initWithAnchorAddress:clusterInitiatorAddress:measurementType:coordinatesType:transmitTime:rawTransmitTime:receiveTime:rawReceiveTime:signalStrength:carrierFrequencyOffset:responderClockFrequencyOffset:coordinates:floorElevation:
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$rawReceiveTime
+ _objc_msgSend$rawTransmitTime
- GCC_except_table336
- GCC_except_table342
CStrings:
+ "Raw Receive Time: [%llu], "
+ "Raw Transmit Time: [%llu], "
+ "RawReceiveTime"
+ "RawTransmitTime"
+ "SystemEventDictKey_SMBClkCfgValue"
+ "\xa2"
- "\x82"

```
