## CoreThreadRadio

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/Versions/A/CoreThreadRadio`

```diff

-275.0.104.0.0
-  __TEXT.__text: 0x1f66c
-  __TEXT.__auth_stubs: 0x9a0
+275.0.502.0.0
+  __TEXT.__text: 0x21e00
+  __TEXT.__auth_stubs: 0x9f0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x598
-  __TEXT.__const: 0x9a8
-  __TEXT.__gcc_except_tab: 0x3798
-  __TEXT.__cstring: 0x2a91
-  __TEXT.__oslogstring: 0xec5
-  __TEXT.__unwind_info: 0xeb8
-  __TEXT.__objc_classname: 0x87
-  __TEXT.__objc_methname: 0x14f1
-  __TEXT.__objc_methtype: 0x16c3
-  __TEXT.__objc_stubs: 0x6c0
-  __DATA_CONST.__got: 0x120
+  __TEXT.__objc_methlist: 0x8b8
+  __TEXT.__const: 0x9b0
+  __TEXT.__gcc_except_tab: 0x3b94
+  __TEXT.__cstring: 0x2cfe
+  __TEXT.__oslogstring: 0xf7f
+  __TEXT.__unwind_info: 0x1020
+  __TEXT.__objc_classname: 0x125
+  __TEXT.__objc_methname: 0x1eef
+  __TEXT.__objc_methtype: 0x1753
+  __TEXT.__objc_stubs: 0xb20
+  __DATA_CONST.__got: 0x138
   __DATA_CONST.__const: 0x388
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x380
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x4e0
-  __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x780
-  __AUTH_CONST.__cfstring: 0x540
-  __AUTH_CONST.__objc_const: 0xdb8
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0xd8
+  __DATA_CONST.__objc_selrefs: 0x4b0
+  __DATA_CONST.__objc_superrefs: 0x40
+  __AUTH_CONST.__auth_got: 0x508
+  __AUTH_CONST.__auth_ptr: 0x18
+  __AUTH_CONST.__const: 0x7e0
+  __AUTH_CONST.__cfstring: 0x8a0
+  __AUTH_CONST.__objc_const: 0x16a8
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x144
   __DATA.__data: 0xe4
   __DATA.__common: 0x4
-  __DATA.__bss: 0x210
+  __DATA.__bss: 0x228
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/AppleSauce.framework/Versions/A/AppleSauce

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 538
-  Symbols:   1409
-  CStrings:  840
+  Functions: 615
+  Symbols:   1636
+  CStrings:  978
 
Symbols:
+ +[CtrAccessorySpecificThreadInfoInput supportsSecureCoding]
+ +[CtrAccessorySpecificThreadInfoInputArray supportsSecureCoding]
+ +[CtrAccessorySpecificThreadInfoOutput supportsSecureCoding]
+ +[CtrAccessorySpecificThreadInfoOutputArray supportsSecureCoding]
+ -[CtrAccessorySpecificThreadInfoInput .cxx_destruct]
+ -[CtrAccessorySpecificThreadInfoInput accessoryManufacturer]
+ -[CtrAccessorySpecificThreadInfoInput accessoryModel]
+ -[CtrAccessorySpecificThreadInfoInput browseStatus]
+ -[CtrAccessorySpecificThreadInfoInput communicationProtocol]
+ -[CtrAccessorySpecificThreadInfoInput consecutiveFailureCount]
+ -[CtrAccessorySpecificThreadInfoInput consecutiveSuccessCount]
+ -[CtrAccessorySpecificThreadInfoInput durationSecondsSinceLastSuccessfulRequest]
+ -[CtrAccessorySpecificThreadInfoInput encodeWithCoder:]
+ -[CtrAccessorySpecificThreadInfoInput errorCode]
+ -[CtrAccessorySpecificThreadInfoInput hapCoAPTokenInfo]
+ -[CtrAccessorySpecificThreadInfoInput hapThreadAccessoryCapabilities]
+ -[CtrAccessorySpecificThreadInfoInput hostName]
+ -[CtrAccessorySpecificThreadInfoInput initData:accessoryModel:hostName:serviceInstanceName:ipv6Address:browseStatus:resolveStatus:transactionStatus:isWrite:isLinkFallback:communicationProtocol:hapThreadAccessoryCapabilities:errorCode:hapTokenInfo:matterSessionInfo:consecutiveFailureCount:consecutiveSuccessCount:durationSecondsSinceLastSuccessfulRequest:]
+ -[CtrAccessorySpecificThreadInfoInput initWithCoder:]
+ -[CtrAccessorySpecificThreadInfoInput ipv6Address]
+ -[CtrAccessorySpecificThreadInfoInput isLinkFallBack]
+ -[CtrAccessorySpecificThreadInfoInput isWrite]
+ -[CtrAccessorySpecificThreadInfoInput matterSessionInfo]
+ -[CtrAccessorySpecificThreadInfoInput resolveStatus]
+ -[CtrAccessorySpecificThreadInfoInput serviceInstanceName]
+ -[CtrAccessorySpecificThreadInfoInput transactionStatus]
+ -[CtrAccessorySpecificThreadInfoInputArray .cxx_destruct]
+ -[CtrAccessorySpecificThreadInfoInputArray addObject:]
+ -[CtrAccessorySpecificThreadInfoInputArray count]
+ -[CtrAccessorySpecificThreadInfoInputArray encodeWithCoder:]
+ -[CtrAccessorySpecificThreadInfoInputArray initWithCoder:]
+ -[CtrAccessorySpecificThreadInfoInputArray init]
+ -[CtrAccessorySpecificThreadInfoInputArray inputArray]
+ -[CtrAccessorySpecificThreadInfoInputArray insertObject:atIndex:]
+ -[CtrAccessorySpecificThreadInfoInputArray objectAtIndex:]
+ -[CtrAccessorySpecificThreadInfoInputArray removeObjectAtIndex:]
+ -[CtrAccessorySpecificThreadInfoInputArray setInputArray:]
+ -[CtrAccessorySpecificThreadInfoOutput encodeWithCoder:]
+ -[CtrAccessorySpecificThreadInfoOutput initWithAccessorySpecificThreadInfoOutput:threadMeshUnderlyingStatusBitmap:threadTXError:threadTXUnderlyingStatusBitmap:threadRXUnderlyingStatusBitmap:srpError:srpUnderlyingStatusBitmap:]
+ -[CtrAccessorySpecificThreadInfoOutput initWithCoder:]
+ -[CtrAccessorySpecificThreadInfoOutput srpError]
+ -[CtrAccessorySpecificThreadInfoOutput srpUnderlyingStatusBitmap]
+ -[CtrAccessorySpecificThreadInfoOutput threadMeshError]
+ -[CtrAccessorySpecificThreadInfoOutput threadMeshUnderlyingStatusBitmap]
+ -[CtrAccessorySpecificThreadInfoOutput threadRXUnderlyingStatusBitmap]
+ -[CtrAccessorySpecificThreadInfoOutput threadTXError]
+ -[CtrAccessorySpecificThreadInfoOutput threadTXUnderlyingStatusBitmap]
+ -[CtrAccessorySpecificThreadInfoOutputArray .cxx_destruct]
+ -[CtrAccessorySpecificThreadInfoOutputArray addObject:]
+ -[CtrAccessorySpecificThreadInfoOutputArray count]
+ -[CtrAccessorySpecificThreadInfoOutputArray encodeWithCoder:]
+ -[CtrAccessorySpecificThreadInfoOutputArray initWithCoder:]
+ -[CtrAccessorySpecificThreadInfoOutputArray init]
+ -[CtrAccessorySpecificThreadInfoOutputArray insertObject:atIndex:]
+ -[CtrAccessorySpecificThreadInfoOutputArray objectAtIndex:]
+ -[CtrAccessorySpecificThreadInfoOutputArray outputArray]
+ -[CtrAccessorySpecificThreadInfoOutputArray removeObjectAtIndex:]
+ -[CtrAccessorySpecificThreadInfoOutputArray setOutputArray:]
+ -[CtrClient threadMeshInfoForHomeMetrics:completionHandler:]
+ -[CtrClient threadMeshInfoForHomeMetrics:completionHandler:].cold.1
+ -[CtrClient threadMeshInfoForHomeMetrics:completionHandler:].cold.2
+ -[CtrClient threadMeshInfoForHomeMetrics:completionHandler:].cold.3
+ GCC_except_table102
+ GCC_except_table112
+ GCC_except_table121
+ GCC_except_table125
+ GCC_except_table128
+ GCC_except_table133
+ GCC_except_table136
+ GCC_except_table139
+ GCC_except_table147
+ GCC_except_table150
+ GCC_except_table157
+ GCC_except_table162
+ GCC_except_table165
+ GCC_except_table171
+ GCC_except_table175
+ GCC_except_table178
+ GCC_except_table186
+ GCC_except_table190
+ GCC_except_table198
+ GCC_except_table40
+ GCC_except_table41
+ GCC_except_table66
+ GCC_except_table86
+ GCC_except_table97
+ GCC_except_table99
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoInput._accessoryManufacturer
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoInput._accessoryModel
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoInput._browseStatus
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoInput._communicationProtocol
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoInput._consecutiveFailureCount
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoInput._consecutiveSuccessCount
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoInput._durationSecondsSinceLastSuccessfulRequest
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoInput._errorCode
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoInput._hapCoAPTokenInfo
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoInput._hapThreadAccessoryCapabilities
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoInput._hostName
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoInput._ipv6Address
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoInput._isLinkFallBack
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoInput._isWrite
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoInput._matterSessionInfo
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoInput._resolveStatus
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoInput._serviceInstanceName
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoInput._transactionStatus
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoInputArray._inputArray
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoOutput._srpError
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoOutput._srpUnderlyingStatusBitmap
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoOutput._threadMeshError
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoOutput._threadMeshUnderlyingStatusBitmap
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoOutput._threadRXUnderlyingStatusBitmap
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoOutput._threadTXError
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoOutput._threadTXUnderlyingStatusBitmap
+ OBJC_IVAR_$_CtrAccessorySpecificThreadInfoOutputArray._outputArray
+ _OBJC_CLASS_$_CtrAccessorySpecificThreadInfoInput
+ _OBJC_CLASS_$_CtrAccessorySpecificThreadInfoInputArray
+ _OBJC_CLASS_$_CtrAccessorySpecificThreadInfoOutput
+ _OBJC_CLASS_$_CtrAccessorySpecificThreadInfoOutputArray
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_METACLASS_$_CtrAccessorySpecificThreadInfoInput
+ _OBJC_METACLASS_$_CtrAccessorySpecificThreadInfoInputArray
+ _OBJC_METACLASS_$_CtrAccessorySpecificThreadInfoOutput
+ _OBJC_METACLASS_$_CtrAccessorySpecificThreadInfoOutputArray
+ _OBJC_METACLASS_$_NSMutableArray
+ _Z57CtrXpcClient_threadMeshInfoForHomeMetrics_response_helperRN6CtrXPC6ResultEN3xpc4dictE.cold.1
+ _Z57CtrXpcClient_threadMeshInfoForHomeMetrics_response_helperRN6CtrXPC6ResultEN3xpc4dictE.cold.2
+ __60-[CtrClient threadMeshInfoForHomeMetrics:completionHandler:]_block_invoke.14
+ __60-[CtrClient threadMeshInfoForHomeMetrics:completionHandler:]_block_invoke.15
+ __Block_byref_object_copy_.18
+ __Block_byref_object_copy_.32
+ __Block_byref_object_dispose_.19
+ __Block_byref_object_dispose_.33
+ __OBJC_$_CLASS_METHODS_CtrAccessorySpecificThreadInfoInput
+ __OBJC_$_CLASS_METHODS_CtrAccessorySpecificThreadInfoInputArray
+ __OBJC_$_CLASS_METHODS_CtrAccessorySpecificThreadInfoOutput
+ __OBJC_$_CLASS_METHODS_CtrAccessorySpecificThreadInfoOutputArray
+ __OBJC_$_CLASS_PROP_LIST_CtrAccessorySpecificThreadInfoInput
+ __OBJC_$_CLASS_PROP_LIST_CtrAccessorySpecificThreadInfoInputArray
+ __OBJC_$_CLASS_PROP_LIST_CtrAccessorySpecificThreadInfoOutput
+ __OBJC_$_CLASS_PROP_LIST_CtrAccessorySpecificThreadInfoOutputArray
+ __OBJC_$_INSTANCE_METHODS_CtrAccessorySpecificThreadInfoInput
+ __OBJC_$_INSTANCE_METHODS_CtrAccessorySpecificThreadInfoInputArray
+ __OBJC_$_INSTANCE_METHODS_CtrAccessorySpecificThreadInfoOutput
+ __OBJC_$_INSTANCE_METHODS_CtrAccessorySpecificThreadInfoOutputArray
+ __OBJC_$_INSTANCE_VARIABLES_CtrAccessorySpecificThreadInfoInput
+ __OBJC_$_INSTANCE_VARIABLES_CtrAccessorySpecificThreadInfoInputArray
+ __OBJC_$_INSTANCE_VARIABLES_CtrAccessorySpecificThreadInfoOutput
+ __OBJC_$_INSTANCE_VARIABLES_CtrAccessorySpecificThreadInfoOutputArray
+ __OBJC_$_PROP_LIST_CtrAccessorySpecificThreadInfoInput
+ __OBJC_$_PROP_LIST_CtrAccessorySpecificThreadInfoInputArray
+ __OBJC_$_PROP_LIST_CtrAccessorySpecificThreadInfoOutput
+ __OBJC_$_PROP_LIST_CtrAccessorySpecificThreadInfoOutputArray
+ __OBJC_CLASS_PROTOCOLS_$_CtrAccessorySpecificThreadInfoInput
+ __OBJC_CLASS_PROTOCOLS_$_CtrAccessorySpecificThreadInfoInputArray
+ __OBJC_CLASS_PROTOCOLS_$_CtrAccessorySpecificThreadInfoOutput
+ __OBJC_CLASS_PROTOCOLS_$_CtrAccessorySpecificThreadInfoOutputArray
+ __OBJC_CLASS_RO_$_CtrAccessorySpecificThreadInfoInput
+ __OBJC_CLASS_RO_$_CtrAccessorySpecificThreadInfoInputArray
+ __OBJC_CLASS_RO_$_CtrAccessorySpecificThreadInfoOutput
+ __OBJC_CLASS_RO_$_CtrAccessorySpecificThreadInfoOutputArray
+ __OBJC_METACLASS_RO_$_CtrAccessorySpecificThreadInfoInput
+ __OBJC_METACLASS_RO_$_CtrAccessorySpecificThreadInfoInputArray
+ __OBJC_METACLASS_RO_$_CtrAccessorySpecificThreadInfoOutput
+ __OBJC_METACLASS_RO_$_CtrAccessorySpecificThreadInfoOutputArray
+ __Z57CtrXpcClient_threadMeshInfoForHomeMetrics_response_helperRN6CtrXPC6ResultEN3xpc4dictE
+ __Z58CtrXpcClient_threadMeshInfoForHomeMetrics_interface_helperN3xpc4dictEPv
+ __ZL47kThreadEntitlementsThreadMeshInfoForHomeMetrics
+ __ZN22Ctr_getThreadInfoInputC2ERKS_
+ __ZN22Ctr_getThreadInfoInputD1Ev
+ __ZN36Ctr_getThreadInfoForMetricsInputListD1Ev
+ __ZN6CtrXPC6Client28threadMeshInfoForHomeMetricsEP36Ctr_getThreadInfoForMetricsInputList
+ ___60-[CtrClient threadMeshInfoForHomeMetrics:completionHandler:]_block_invoke
+ ___60-[CtrClient threadMeshInfoForHomeMetrics:completionHandler:]_block_invoke_2
+ ___block_descriptor_40_ea8_32r_e5_v8?0l
+ ___block_descriptor_56_ea8_32r40r_e5_v8?0l
+ ___copy_helper_block_ea8_32r
+ ___copy_helper_block_ea8_32r40r
+ ___destroy_helper_block_ea8_32r
+ ___destroy_helper_block_ea8_32r40r
+ _objc_alloc_init
+ _objc_autoreleaseReturnValue
+ _objc_msgSend$accessoryManufacturer
+ _objc_msgSend$accessoryModel
+ _objc_msgSend$addObject:
+ _objc_msgSend$browseStatus
+ _objc_msgSend$communicationProtocol
+ _objc_msgSend$consecutiveFailureCount
+ _objc_msgSend$consecutiveSuccessCount
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$durationSecondsSinceLastSuccessfulRequest
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$errorCode
+ _objc_msgSend$hapCoAPTokenInfo
+ _objc_msgSend$hapThreadAccessoryCapabilities
+ _objc_msgSend$hostName
+ _objc_msgSend$initData:accessoryModel:hostName:serviceInstanceName:ipv6Address:browseStatus:resolveStatus:transactionStatus:isWrite:isLinkFallback:communicationProtocol:hapThreadAccessoryCapabilities:errorCode:hapTokenInfo:matterSessionInfo:consecutiveFailureCount:consecutiveSuccessCount:durationSecondsSinceLastSuccessfulRequest:
+ _objc_msgSend$initWithAccessorySpecificThreadInfoOutput:threadMeshUnderlyingStatusBitmap:threadTXError:threadTXUnderlyingStatusBitmap:threadRXUnderlyingStatusBitmap:srpError:srpUnderlyingStatusBitmap:
+ _objc_msgSend$inputArray
+ _objc_msgSend$insertObject:atIndex:
+ _objc_msgSend$ipv6Address
+ _objc_msgSend$isLinkFallBack
+ _objc_msgSend$isWrite
+ _objc_msgSend$matterSessionInfo
+ _objc_msgSend$outputArray
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$resolveStatus
+ _objc_msgSend$serviceInstanceName
+ _objc_msgSend$srpError
+ _objc_msgSend$srpUnderlyingStatusBitmap
+ _objc_msgSend$threadMeshError
+ _objc_msgSend$threadMeshUnderlyingStatusBitmap
+ _objc_msgSend$threadRXUnderlyingStatusBitmap
+ _objc_msgSend$threadTXError
+ _objc_msgSend$threadTXUnderlyingStatusBitmap
+ _objc_msgSend$transactionStatus
+ _objc_opt_class
+ _objc_retainBlock
+ _objc_setProperty_atomic
- GCC_except_table100
- GCC_except_table106
- GCC_except_table116
- GCC_except_table123
- GCC_except_table127
- GCC_except_table130
- GCC_except_table134
- GCC_except_table137
- GCC_except_table146
- GCC_except_table149
- GCC_except_table156
- GCC_except_table158
- GCC_except_table164
- GCC_except_table170
- GCC_except_table174
- GCC_except_table176
- GCC_except_table181
- GCC_except_table189
- GCC_except_table197
- GCC_except_table43
- GCC_except_table95
- GCC_except_table98
- __Block_byref_object_copy_.25
- __Block_byref_object_dispose_.26
CStrings:
+ "\x15"
+ "%s Cannot allocate memory for inputList"
+ "%s threadInfoForMetricsInputList is empty"
+ "%s valid completion handler was not provided"
+ "-[CtrClient threadMeshInfoForHomeMetrics:completionHandler:]"
+ "@152@0:8@16@24@32@40@48q56q64q72B80B84q88q96Q104Q112Q120Q128Q136Q144"
+ "@24@0:8Q16"
+ "@72@0:8q16Q24q32Q40Q48q56Q64"
+ "CtrAccessorySpecificThreadInfoInput"
+ "CtrAccessorySpecificThreadInfoInputArray"
+ "CtrAccessorySpecificThreadInfoOutput"
+ "CtrAccessorySpecificThreadInfoOutputArray"
+ "Get Thread Info for Metrics succeeded send to server ... \n"
+ "Q"
+ "Q16@0:8"
+ "T@\"NSMutableArray\",&,V_inputArray"
+ "T@\"NSMutableArray\",&,V_outputArray"
+ "T@\"NSString\",R,V_accessoryManufacturer"
+ "T@\"NSString\",R,V_accessoryModel"
+ "T@\"NSString\",R,V_hostName"
+ "T@\"NSString\",R,V_ipv6Address"
+ "T@\"NSString\",R,V_serviceInstanceName"
+ "TB,R,V_isLinkFallBack"
+ "TB,R,V_isWrite"
+ "TQ,R,V_consecutiveFailureCount"
+ "TQ,R,V_consecutiveSuccessCount"
+ "TQ,R,V_durationSecondsSinceLastSuccessfulRequest"
+ "TQ,R,V_errorCode"
+ "TQ,R,V_hapCoAPTokenInfo"
+ "TQ,R,V_matterSessionInfo"
+ "TQ,R,V_srpUnderlyingStatusBitmap"
+ "TQ,R,V_threadMeshUnderlyingStatusBitmap"
+ "TQ,R,V_threadRXUnderlyingStatusBitmap"
+ "TQ,R,V_threadTXUnderlyingStatusBitmap"
+ "Tq,R,V_browseStatus"
+ "Tq,R,V_communicationProtocol"
+ "Tq,R,V_hapThreadAccessoryCapabilities"
+ "Tq,R,V_resolveStatus"
+ "Tq,R,V_srpError"
+ "Tq,R,V_threadMeshError"
+ "Tq,R,V_threadTXError"
+ "Tq,R,V_transactionStatus"
+ "_accessoryManufacturer"
+ "_accessoryModel"
+ "_browseStatus"
+ "_communicationProtocol"
+ "_consecutiveFailureCount"
+ "_consecutiveSuccessCount"
+ "_durationSecondsSinceLastSuccessfulRequest"
+ "_errorCode"
+ "_hapCoAPTokenInfo"
+ "_hapThreadAccessoryCapabilities"
+ "_hostName"
+ "_inputArray"
+ "_ipv6Address"
+ "_isLinkFallBack"
+ "_isWrite"
+ "_matterSessionInfo"
+ "_outputArray"
+ "_resolveStatus"
+ "_serviceInstanceName"
+ "_srpError"
+ "_srpUnderlyingStatusBitmap"
+ "_threadMeshError"
+ "_threadMeshUnderlyingStatusBitmap"
+ "_threadRXUnderlyingStatusBitmap"
+ "_threadTXError"
+ "_threadTXUnderlyingStatusBitmap"
+ "_transactionStatus"
+ "accessoryManufacturer"
+ "accessoryModel"
+ "addObject:"
+ "browseStatus"
+ "com.apple.private.fillmore.threadMeshInfoForHomeMetrics"
+ "communicationProtocol"
+ "consecutiveFailureCount"
+ "consecutiveSuccessCount"
+ "decodeIntegerForKey:"
+ "decodeObjectOfClass:forKey:"
+ "durationSecondsSinceLastSuccessfulRequest"
+ "encodeInteger:forKey:"
+ "errorCode"
+ "hapCoAPTokenInfo"
+ "hapThreadAccessoryCapabilities"
+ "hostName"
+ "initData:accessoryModel:hostName:serviceInstanceName:ipv6Address:browseStatus:resolveStatus:transactionStatus:isWrite:isLinkFallback:communicationProtocol:hapThreadAccessoryCapabilities:errorCode:hapTokenInfo:matterSessionInfo:consecutiveFailureCount:consecutiveSuccessCount:durationSecondsSinceLastSuccessfulRequest:"
+ "initWithAccessorySpecificThreadInfoOutput:threadMeshUnderlyingStatusBitmap:threadTXError:threadTXUnderlyingStatusBitmap:threadRXUnderlyingStatusBitmap:srpError:srpUnderlyingStatusBitmap:"
+ "inputArray"
+ "insertObject:atIndex:"
+ "ipAddress"
+ "ipv6Address"
+ "isLinkFallBack"
+ "isLinkFallback"
+ "isWrite"
+ "matterSessionInfo"
+ "outputArray"
+ "removeObjectAtIndex:"
+ "resolveStatus"
+ "serviceInstanceName"
+ "setInputArray:"
+ "setOutputArray:"
+ "srpError"
+ "srpStatusBitmap"
+ "srpUnderlyingStatusBitmap"
+ "threadMeshError"
+ "threadMeshInfoForHomeMetrics"
+ "threadMeshInfoForHomeMetrics:completionHandler:"
+ "threadMeshStatusBitmap"
+ "threadMeshUnderlyingStatusBitmap"
+ "threadRXUnderlyingStatusBitmap"
+ "threadRxStatusBitmap"
+ "threadTXError"
+ "threadTXUnderlyingStatusBitmap"
+ "threadTxError"
+ "threadTxStatusBitmap"
+ "transactionStatus"
+ "v24@0:8Q16"
+ "v32@0:8@16Q24"

```
