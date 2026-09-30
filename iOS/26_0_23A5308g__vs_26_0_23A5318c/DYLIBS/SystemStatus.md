## SystemStatus

> `/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus`

```diff

-247.0.0.0.0
-  __TEXT.__text: 0x58174
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_methlist: 0x8150
+248.100.0.0.0
+  __TEXT.__text: 0x58104
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_methlist: 0x8170
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x3d15
+  __TEXT.__cstring: 0x3d37
   __TEXT.__oslogstring: 0x1469
   __TEXT.__gcc_except_tab: 0x470
   __TEXT.__unwind_info: 0x1fa0
   __TEXT.__objc_classname: 0x1a16
-  __TEXT.__objc_methname: 0xafe5
+  __TEXT.__objc_methname: 0xb0cd
   __TEXT.__objc_methtype: 0x171f
-  __TEXT.__objc_stubs: 0x5920
+  __TEXT.__objc_stubs: 0x5940
   __DATA_CONST.__got: 0x570
-  __DATA_CONST.__const: 0x19e8
+  __DATA_CONST.__const: 0x19c0
   __DATA_CONST.__objc_classlist: 0x580
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ed8
+  __DATA_CONST.__objc_selrefs: 0x1ee0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x3e8
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x368
+  __AUTH_CONST.__auth_got: 0x370
   __AUTH_CONST.__const: 0x8c0
-  __AUTH_CONST.__cfstring: 0x4620
-  __AUTH_CONST.__objc_const: 0xf048
+  __AUTH_CONST.__cfstring: 0x4640
+  __AUTH_CONST.__objc_const: 0xf088
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x50c
+  __DATA.__objc_ivar: 0x510
   __DATA.__data: 0xd28
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_ivar: 0xac

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8E14E056-A69E-3EEF-8447-9897CC7FBDF7
+  UUID: 063B9EBC-E3A7-3AA6-A272-34D4CE2E7D6F
   Functions: 3082
-  Symbols:   9319
-  CStrings:  3362
+  Symbols:   9321
+  CStrings:  3369
 
Symbols:
+ -[STMutableTelephonyStatusDomainData setUsingStewieConnectionOverInternet:]
+ -[STStatusDomainPublisherXPCServerHandle _internalQueue_resendDataIfNecessary]
+ -[STTelephonyStatusDomainData initWithSIMOneInfo:SIMTwoInfo:cellularRadioCapabilityEnabled:dualSIMEnabled:radioModuleDead:usingStewieForSOS:inactiveSOSEnabled:usingStewieConnection:usingStewieConnectionOverInternet:]
+ -[STTelephonyStatusDomainData isUsingStewieConnectionOverInternet]
+ GCC_except_table48
+ OBJC_IVAR_$_STTelephonyStatusDomainData._usingStewieConnectionOverInternet
+ _BSDispatchQueueCreateSerialWithQoS
+ ___39-[STTelephonyStatusDomainData isEqual:]_block_invoke_9
+ ___78-[STStatusDomainPublisherXPCServerHandle _internalQueue_resendDataIfNecessary]_block_invoke
+ ___78-[STStatusDomainPublisherXPCServerHandle _internalQueue_resendDataIfNecessary]_block_invoke.63
+ ___78-[STStatusDomainPublisherXPCServerHandle _internalQueue_resendDataIfNecessary]_block_invoke_2
+ ___78-[STStatusDomainPublisherXPCServerHandle _internalQueue_resendDataIfNecessary]_block_invoke_2.64
+ ___78-[STStatusDomainPublisherXPCServerHandle _internalQueue_resendDataIfNecessary]_block_invoke_3
+ ___78-[STStatusDomainPublisherXPCServerHandle _internalQueue_resendDataIfNecessary]_block_invoke_3.65
+ ___79-[STStatusDomainXPCServerHandle _internalQueue_reregisterForDomainsIfNecessary]_block_invoke
+ _objc_msgSend$isUsingStewieConnectionOverInternet
+ _objc_msgSend$setUsingStewieConnectionOverInternet:
- -[STStatusDomainPublisherXPCServerHandle _resendDataIfNecessary]
- -[STTelephonyStatusDomainData initWithSIMOneInfo:SIMTwoInfo:cellularRadioCapabilityEnabled:dualSIMEnabled:radioModuleDead:usingStewieForSOS:inactiveSOSEnabled:usingStewieConnection:]
- GCC_except_table49
- ___124-[STStatusDomainPublisherXPCServerHandle _internalQueue_mutateDataForDomain:discardingOnExit:wrappingCompletion:usingBlock:]_block_invoke_2
- ___64-[STStatusDomainPublisherXPCServerHandle _resendDataIfNecessary]_block_invoke.61
- ___64-[STStatusDomainPublisherXPCServerHandle _resendDataIfNecessary]_block_invoke.64
- ___64-[STStatusDomainPublisherXPCServerHandle _resendDataIfNecessary]_block_invoke_2
- ___64-[STStatusDomainPublisherXPCServerHandle _resendDataIfNecessary]_block_invoke_2.65
- ___64-[STStatusDomainPublisherXPCServerHandle _resendDataIfNecessary]_block_invoke_3
- ___64-[STStatusDomainPublisherXPCServerHandle _resendDataIfNecessary]_block_invoke_3.66
- ___64-[STStatusDomainPublisherXPCServerHandle _resendDataIfNecessary]_block_invoke_4
- ___64-[STStatusDomainPublisherXPCServerHandle _resendDataIfNecessary]_block_invoke_4.67
- ___65-[STStatusDomainXPCServerHandle _reregisterForDomainsIfNecessary]_block_invoke_2
- ___block_descriptor_72_e8_32s40s48bs56r_e5_v8?0ls32l8r56l8s40l8s48l8
- _objc_msgSend$remoteObjectProxyWithErrorHandler:
CStrings:
+ "TB,D,N,GisUsingStewieConnectionOverInternet"
+ "TB,R,N,GisUsingStewieConnectionOverInternet,V_usingStewieConnectionOverInternet"
+ "_usingStewieConnectionOverInternet"
+ "isUsingStewieConnectionOverInternet"
+ "setUsingStewieConnectionOverInternet:"
+ "usingStewieConnectionOverInternet"
- "remoteObjectProxyWithErrorHandler:"

```
