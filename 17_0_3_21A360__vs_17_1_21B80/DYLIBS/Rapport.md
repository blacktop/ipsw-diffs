## Rapport

> `/System/Library/PrivateFrameworks/Rapport.framework/Rapport`

```diff

-500.60.4.0.0
-  __TEXT.__text: 0x6eb24
+510.71.1.0.0
+  __TEXT.__text: 0x6f610
   __TEXT.__auth_stubs: 0x1120
-  __TEXT.__objc_methlist: 0x7098
-  __TEXT.__const: 0x1c1d
-  __TEXT.__cstring: 0x11968
+  __TEXT.__objc_methlist: 0x70d8
+  __TEXT.__const: 0x1c35
+  __TEXT.__cstring: 0x11b02
   __TEXT.__gcc_except_tab: 0xf58
   __TEXT.__oslogstring: 0x588
-  __TEXT.__unwind_info: 0x17c0
+  __TEXT.__unwind_info: 0x17d8
   __TEXT.__objc_classname: 0x8ed
-  __TEXT.__objc_methname: 0xe94e
-  __TEXT.__objc_methtype: 0x2602
-  __TEXT.__objc_stubs: 0x7da0
+  __TEXT.__objc_methname: 0xeadc
+  __TEXT.__objc_methtype: 0x2633
+  __TEXT.__objc_stubs: 0x7ec0
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x2160
+  __DATA_CONST.__const: 0x2168
   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xdf20
-  __DATA_CONST.__objc_selrefs: 0x31c0
+  __DATA_CONST.__objc_const: 0xdf60
+  __DATA_CONST.__objc_selrefs: 0x3208
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__objc_const: 0x360
-  __AUTH_CONST.__cfstring: 0x4240
+  __AUTH_CONST.__cfstring: 0x44e0
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x78

   __DATA.__objc_protorefs: 0x90
   __DATA.__objc_classrefs: 0x250
   __DATA.__objc_superrefs: 0x198
-  __DATA.__objc_ivar: 0xf80
+  __DATA.__objc_ivar: 0xf88
   __DATA.__data: 0x1718
   __DATA.__bss: 0x118
   __DATA.__common: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 70D40A45-BA20-356B-808A-68B2F403578C
-  Functions: 2945
-  Symbols:   9272
-  CStrings:  6106
+  UUID: 3F467AE9-9014-3083-A2F5-AB65472104AA
+  Functions: 2954
+  Symbols:   9299
+  CStrings:  6162
 
Symbols:
+ -[RPCompanionLinkDevice isEqualToDeviceBasic:]
+ -[RPConnection _getCurrentProcessName]
+ -[RPConnection _logConnectionInvalidatedWithError:]
+ -[RPConnectionMetrics logConnectionWithDeviceModelFrom:deviceModelTo:error:initiator:isOnDemand:isStereoPair:lifetime:linkType:]
+ -[RPConnectionMetrics logMessageForClient:length:linkType:]
+ -[RPConnectionMetrics rttMetrics]
+ -[RPConnectionMetrics setRttMetrics:]
+ -[RPNearFieldController _synchronousRemoteObjectProxy]
+ _OBJC_IVAR_$_RPConnection._activatedTicks
+ _OBJC_IVAR_$_RPConnection._initiator
+ _OBJC_IVAR_$_RPConnectionMetrics._rttMetrics
+ _RPDeviceClassToString
+ ___54-[RPNearFieldController _synchronousRemoteObjectProxy]_block_invoke
+ ___block_literal_global.1252
+ _objc_msgSend$_getCurrentProcessName
+ _objc_msgSend$_logConnectionInvalidatedWithError:
+ _objc_msgSend$_synchronousRemoteObjectProxy
+ _objc_msgSend$cbDevice
+ _objc_msgSend$logConnectionWithDeviceModelFrom:deviceModelTo:error:initiator:isOnDemand:isStereoPair:lifetime:linkType:
+ _objc_msgSend$logMessageForClient:length:linkType:
+ _objc_msgSend$nearbyInfoV2TempAuthTagData
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
- -[RPConnectionMetrics metrics]
- -[RPConnectionMetrics setMetrics:]
- _OBJC_IVAR_$_RPConnectionMetrics._metrics
- ___block_literal_global.1244
CStrings:
+ "$\x12\"\x11\x13\x11\x11!\"\x11\xbb\x17\x1f\r\x13"
+ "%{error}"
+ "-[RPNearFieldController _synchronousRemoteObjectProxy]_block_invoke"
+ "510.71.1"
+ "AudioAccessory"
+ "DirectLink"
+ "FPGA"
+ "Failed to retrieve synchronous remote object proxy with error:%@\n"
+ "IdentityProofsVerify RP: %s, %#ll{flags} current status flags %#ll{flags}\n"
+ "Mac"
+ "NoError"
+ "RealityDevice"
+ "T@\"NSMutableDictionary\",&,N,V_rttMetrics"
+ "Uknown"
+ "_activatedTicks"
+ "_getCurrentProcessName"
+ "_initiator"
+ "_logConnectionInvalidatedWithError:"
+ "_rttMetrics"
+ "_synchronousRemoteObjectProxy"
+ "com.apple.rapport.metrics.connection"
+ "com.apple.rapport.metrics.message"
+ "deviceModelFrom"
+ "deviceModelTo"
+ "iPad"
+ "iPhone"
+ "iPod"
+ "initiator"
+ "isEqualToDeviceBasic:"
+ "isOnDemand"
+ "isStereoPair"
+ "lengthKB"
+ "lifetime"
+ "logConnectionWithDeviceModelFrom:deviceModelTo:error:initiator:isOnDemand:isStereoPair:lifetime:linkType:"
+ "logMessageForClient:length:linkType:"
+ "nearbyInfoV2TempAuthTagData"
+ "rttMetrics"
+ "setRttMetrics:"
+ "stringWithCString:encoding:"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "v36@0:8@16Q24i32"
+ "v68@0:8@16@24@32@40B48B52Q56i64"
- "\x13\x12\"\x11\x13\x11\x11!\"\x11\xbb\x17\x1f\r\x13"
- "500.60.4"
- "IdentityProofsVerify RP: %s, %#ll{flags}\n"
- "T@\"NSMutableDictionary\",&,N,V_metrics"
- "_metrics"
- "metrics"
- "setMetrics:"

```
