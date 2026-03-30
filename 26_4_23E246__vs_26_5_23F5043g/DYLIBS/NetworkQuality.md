## NetworkQuality

> `/System/Library/PrivateFrameworks/NetworkQuality.framework/NetworkQuality`

```diff

-194.100.10.0.0
-  __TEXT.__text: 0x21124
-  __TEXT.__auth_stubs: 0xc00
-  __TEXT.__objc_methlist: 0x1c88
+194.120.6.0.0
+  __TEXT.__text: 0x21384
+  __TEXT.__auth_stubs: 0xc10
+  __TEXT.__objc_methlist: 0x1cc0
   __TEXT.__const: 0x1a8
   __TEXT.__gcc_except_tab: 0x718
-  __TEXT.__cstring: 0x2b14
+  __TEXT.__cstring: 0x2b28
   __TEXT.__oslogstring: 0x2138
   __TEXT.__unwind_info: 0x678
   __TEXT.__objc_classname: 0x375
-  __TEXT.__objc_methname: 0x505a
+  __TEXT.__objc_methname: 0x517f
   __TEXT.__objc_methtype: 0xd9f
-  __TEXT.__objc_stubs: 0x40a0
-  __DATA_CONST.__got: 0x1e8
+  __TEXT.__objc_stubs: 0x41e0
+  __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__const: 0x6f0
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12a8
+  __DATA_CONST.__objc_selrefs: 0x1300
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x610
+  __AUTH_CONST.__auth_got: 0x618
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x1d60
-  __AUTH_CONST.__objc_const: 0x4378
+  __AUTH_CONST.__cfstring: 0x1dc0
+  __AUTH_CONST.__objc_const: 0x4418
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x820
-  __DATA.__objc_ivar: 0x4f8
+  __DATA.__objc_ivar: 0x508
   __DATA.__data: 0x360
   __DATA.__bss: 0x20
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2A5BE5C1-B59E-3E86-BD07-C436EC99BFB4
-  Functions: 712
-  Symbols:   2868
-  CStrings:  1949
+  UUID: AA8380F6-4822-3D37-982E-CDFE5EDA0B70
+  Functions: 717
+  Symbols:   2895
+  CStrings:  1971
 
Symbols:
+ -[NetworkQualityConfiguration enableProbeID]
+ -[NetworkQualityConfiguration setEnableProbeID:]
+ -[NetworkQualityServerConfiguration noTCPNotSentLowat]
+ -[NetworkQualityServerConfiguration setNoTCPNotSentLowat:]
+ -[WorkingLatencyURLSessionDelegate probeRequestWithID]
+ GCC_except_table71
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLQueryItem
+ _OBJC_IVAR_$_LatencyURLSessionDelegate._probeIDCounter
+ _OBJC_IVAR_$_NetworkQualityConfiguration._enableProbeID
+ _OBJC_IVAR_$_NetworkQualityHTTPServer.noTCPNotSentLowat
+ _OBJC_IVAR_$_NetworkQualityServerConfiguration._noTCPNotSentLowat
+ ___55-[WorkingLatencyURLSessionDelegate scheduleNewTaskSelf]_block_invoke.361
+ ___58-[WorkingLatencyURLSessionDelegate scheduleNewTaskForeign]_block_invoke.362
+ _nw_tcp_options_set_reduce_buffering
+ _objc_msgSend$array
+ _objc_msgSend$componentsWithURL:resolvingAgainstBaseURL:
+ _objc_msgSend$enableProbeID
+ _objc_msgSend$noTCPNotSentLowat
+ _objc_msgSend$probeRequestWithID
+ _objc_msgSend$queryItemWithName:value:
+ _objc_msgSend$queryItems
+ _objc_msgSend$setEnableProbeID:
+ _objc_msgSend$setQueryItems:
+ _objc_msgSend$setURL:
- GCC_except_table70
- ___55-[WorkingLatencyURLSessionDelegate scheduleNewTaskSelf]_block_invoke.352
- ___58-[WorkingLatencyURLSessionDelegate scheduleNewTaskForeign]_block_invoke.353
CStrings:
+ "%lu"
+ "TB,N,V_noTCPNotSentLowat"
+ "TB,V_enableProbeID"
+ "_enableProbeID"
+ "_noTCPNotSentLowat"
+ "_probeIDCounter"
+ "array"
+ "componentsWithURL:resolvingAgainstBaseURL:"
+ "enableProbeID"
+ "noTCPNotSentLowat"
+ "probeRequestWithID"
+ "queryItemWithName:value:"
+ "queryItems"
+ "setEnableProbeID:"
+ "setNoTCPNotSentLowat:"
+ "setQueryItems:"
+ "setURL:"
+ "t"

```
