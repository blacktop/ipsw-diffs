## CoreThreadRadio

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio`

```diff

-275.0.104.0.0
-  __TEXT.__text: 0x1ef68
-  __TEXT.__auth_stubs: 0xb00
+275.0.502.0.0
+  __TEXT.__text: 0x21474
+  __TEXT.__auth_stubs: 0xb70
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x598
-  __TEXT.__const: 0x9a8
-  __TEXT.__gcc_except_tab: 0x3764
-  __TEXT.__cstring: 0x2a91
-  __TEXT.__oslogstring: 0xec5
-  __TEXT.__unwind_info: 0xea8
-  __TEXT.__objc_classname: 0x87
-  __TEXT.__objc_methname: 0x14f1
-  __TEXT.__objc_methtype: 0x16c3
-  __TEXT.__objc_stubs: 0x6c0
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x428
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__objc_methlist: 0x8b8
+  __TEXT.__const: 0x9b0
+  __TEXT.__gcc_except_tab: 0x3b50
+  __TEXT.__cstring: 0x2cfe
+  __TEXT.__oslogstring: 0xf7f
+  __TEXT.__unwind_info: 0x1010
+  __TEXT.__objc_classname: 0x125
+  __TEXT.__objc_methname: 0x1eef
+  __TEXT.__objc_methtype: 0x1753
+  __TEXT.__objc_stubs: 0xb20
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__const: 0x478
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x380
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x590
-  __AUTH_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__objc_selrefs: 0x4b0
+  __DATA_CONST.__objc_superrefs: 0x40
+  __AUTH_CONST.__auth_got: 0x5c8
+  __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x6d8
-  __AUTH_CONST.__cfstring: 0x540
-  __AUTH_CONST.__objc_const: 0xdb8
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0xd8
+  __AUTH_CONST.__cfstring: 0x8a0
+  __AUTH_CONST.__objc_const: 0x16a8
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x144
   __DATA.__data: 0xe4
   __DATA.__common: 0x4
+  __DATA.__bss: 0x18
   __DATA_DIRTY.__bss: 0x210
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 532
-  Symbols:   858
-  CStrings:  840
+  Functions: 605
+  Symbols:   951
+  CStrings:  978
 
Symbols:
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
+ __Z57CtrXpcClient_threadMeshInfoForHomeMetrics_response_helperRN6CtrXPC6ResultEN3xpc4dictE
+ __Z58CtrXpcClient_threadMeshInfoForHomeMetrics_interface_helperN3xpc4dictEPv
+ __ZN6CtrXPC6Client28threadMeshInfoForHomeMetricsEP36Ctr_getThreadInfoForMetricsInputList
+ _objc_alloc_init
+ _objc_autoreleaseReturnValue
+ _objc_opt_class
+ _objc_release_x9
+ _objc_retainBlock
+ _objc_retain_x26
+ _objc_setProperty_atomic
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
