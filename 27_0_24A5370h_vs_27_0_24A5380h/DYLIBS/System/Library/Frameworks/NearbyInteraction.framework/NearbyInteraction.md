## NearbyInteraction

> `/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`

```diff

-  __TEXT.__text: 0x36158
-  __TEXT.__objc_methlist: 0x4328
-  __TEXT.__gcc_except_tab: 0x5938
-  __TEXT.__cstring: 0x512f
-  __TEXT.__const: 0x500
+  __TEXT.__text: 0x36640
+  __TEXT.__objc_methlist: 0x4378
+  __TEXT.__gcc_except_tab: 0x59bc
+  __TEXT.__cstring: 0x51a7
+  __TEXT.__const: 0x520
   __TEXT.__oslogstring: 0x1369
   __TEXT.__swift5_typeref: 0x83
   __TEXT.__swift5_reflstr: 0x4b

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x2180
+  __TEXT.__unwind_info: 0x21a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd30
+  __DATA_CONST.__const: 0xd38
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f90
+  __DATA_CONST.__objc_selrefs: 0x1fc8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x40
-  __DATA_CONST.__got: 0x2b0
-  __AUTH_CONST.__const: 0x438
-  __AUTH_CONST.__cfstring: 0x5a20
-  __AUTH_CONST.__objc_const: 0x7928
+  __DATA_CONST.__got: 0x2d0
+  __AUTH_CONST.__const: 0x458
+  __AUTH_CONST.__cfstring: 0x5ac0
+  __AUTH_CONST.__objc_const: 0x7988
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x458
-  __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x500
+  __DATA.__objc_ivar: 0x508
   __DATA.__data: 0x4f0
-  __DATA.__bss: 0x5a0
+  __DATA.__bss: 0x590
   __DATA.__common: 0x153
-  __DATA_DIRTY.__objc_data: 0xd20
-  __DATA_DIRTY.__bss: 0x98
+  __DATA_DIRTY.__objc_data: 0x1130
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1560
-  Symbols:   5539
-  CStrings:  1656
+  Functions: 1568
+  Symbols:   5565
+  CStrings:  1666
 
Sections:
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
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
+ GCC_except_table25
+ GCC_except_table363
+ GCC_except_table364
+ GCC_except_table368
+ GCC_except_table372
+ _OBJC_IVAR_$_NIDLTDOAMeasurement._rawReceiveTime
+ _OBJC_IVAR_$_NIDLTDOAMeasurement._rawTransmitTime
+ __NISystemEventDictKey_SMBClkCfgValue
+ ___39-[NISystemEventNotifier _setSMBClkCfg:]_block_invoke
+ ___39-[NISystemEventNotifier _setSMBClkCfg:]_block_invoke_2
+ _objc_msgSend$initWithAnchorAddress:clusterInitiatorAddress:measurementType:coordinatesType:transmitTime:rawTransmitTime:receiveTime:rawReceiveTime:signalStrength:carrierFrequencyOffset:responderClockFrequencyOffset:coordinates:floorElevation:
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$rawReceiveTime
+ _objc_msgSend$rawTransmitTime
- GCC_except_table365
- GCC_except_table369
CStrings:
+ "Raw Receive Time: [%llu], "
+ "Raw Transmit Time: [%llu], "
+ "RawReceiveTime"
+ "RawTransmitTime"
+ "SystemEventDictKey_SMBClkCfgValue"
+ "\xa2"
- "\x82"

```
