## RelativeMotion

> `/System/Library/PrivateFrameworks/RelativeMotion.framework/Versions/A/RelativeMotion`

```diff

-272.0.1.0.0
-  __TEXT.__text: 0xa9d0
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_methlist: 0x6c4
+300.0.2.0.0
+  __TEXT.__text: 0xab90
+  __TEXT.__auth_stubs: 0x510
+  __TEXT.__objc_methlist: 0x89c
   __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0xdf4
+  __TEXT.__cstring: 0xe35
   __TEXT.__gcc_except_tab: 0x110
-  __TEXT.__oslogstring: 0x17d2
-  __TEXT.__unwind_info: 0x3d0
+  __TEXT.__oslogstring: 0x17f4
+  __TEXT.__unwind_info: 0x430
   __TEXT.__objc_classname: 0x1f2
-  __TEXT.__objc_methname: 0x1455
-  __TEXT.__objc_methtype: 0x65a
-  __TEXT.__objc_stubs: 0xce0
+  __TEXT.__objc_methname: 0x14a4
+  __TEXT.__objc_methtype: 0x675
+  __TEXT.__objc_stubs: 0xd00
   __DATA_CONST.__got: 0x128
   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x408
+  __DATA_CONST.__objc_selrefs: 0x498
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x290
+  __AUTH_CONST.__auth_got: 0x298
   __AUTH_CONST.__const: 0x550
-  __AUTH_CONST.__cfstring: 0x4e0
-  __AUTH_CONST.__objc_const: 0x1d50
+  __AUTH_CONST.__cfstring: 0x500
+  __AUTH_CONST.__objc_const: 0x1a50
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0x104
+  __DATA.__objc_ivar: 0x108
   __DATA.__data: 0x3a0
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D07E8CE6-C8FD-34D2-9207-10F5C0CB571B
-  Functions: 294
-  Symbols:   864
-  CStrings:  551
+  UUID: EB744AAF-AAF6-3852-BB4B-0506CF95B099
+  Functions: 334
+  Symbols:   939
+  CStrings:  555
 
Symbols:
+ -[RMConnectionClient endpointWasInterrupted:].cold.2
+ -[RMConnectionClient endpointWasInvalidated:].cold.2
+ -[RMConnectionClient endpointWasInvalidated:].cold.3
+ -[RMConnectionEndpoint handleXpcMessage:replyBlock:].cold.2
+ -[RMConnectionEndpoint handleXpcMessage:replyBlock:].cold.3
+ -[RMConnectionEndpoint handleXpcMessage:replyBlock:].cold.4
+ -[RMConnectionEndpoint handleXpcMessage:replyBlock:].cold.5
+ -[RMConnectionEndpoint handleXpcMessage:replyBlock:].cold.6
+ -[RMConnectionEndpoint requestStreamWithMessage:data:errorHandler:].cold.2
+ -[RMConnectionEndpoint sendMessage:withData:].cold.2
+ -[RMConnectionEndpoint startReceivingStreamOnConnection:errorHandler:].cold.2
+ -[RMConnectionEndpoint stopServingStream].cold.2
+ -[RMDummyDataManager dummyDataConfiguration].cold.1
+ -[RMInternalServiceClient parseSpiErrorReply:forMessage:].cold.1
+ -[RMInternalServiceClient parseSpiErrorReply:forMessage:].cold.2
+ -[RMMediaSession _resetTrackingForAllClients].cold.1
+ -[RMMediaSession _start].cold.1
+ -[RMMediaSession axHeadTrackingSettingChanged].cold.1
+ -[RMMediaSession isAXHeadTrackingSettingEnabled].cold.1
+ -[RMPose _initWithAttitude:consumedAuxTimestamp:receivedAuxTimestamp:machAbsTimestamp:presentationTimestamp:]
+ -[RMPose presentationTimestamp]
+ -[RMRelativeMotionManager initWithQueue:].cold.1
+ GCC_except_table55
+ OBJC_IVAR_$_RMPose._presentationTimestamp
+ _CLLogObjectForCategory_ConnectionClient_Default.cold.1
+ _CLLogObjectForCategory_IPC_Default.cold.1
+ _CLLogObjectForCategory_RelativeMotionManager_Default.cold.1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __128-[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:statusCallback:]_block_invoke.30.cold.1
+ __128-[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:statusCallback:]_block_invoke.cold.1
+ __128-[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:statusCallback:]_block_invoke.cold.2
+ __128-[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:statusCallback:]_block_invoke.cold.3
+ __128-[RMAudioListenerPoseManager startReceivingAudioListenerPoseUpdatesWithForceSessionRestart:poseCallbackInternal:statusCallback:]_block_invoke.cold.4
+ __23-[RMMediaSession _stop]_block_invoke.cold.1
+ __48-[RMInternalServiceClient listClientsWithReply:]_block_invoke_2.cold.1
+ __48-[RMInternalServiceClient listClientsWithReply:]_block_invoke_2.cold.2
+ __49-[RMConnectionEndpoint initWithConnection:queue:]_block_invoke.cold.1
+ __49-[RMConnectionEndpoint initWithConnection:queue:]_block_invoke.cold.2
+ __49-[RMConnectionEndpoint initWithConnection:queue:]_block_invoke.cold.3
+ __49-[RMConnectionEndpoint initWithConnection:queue:]_block_invoke.cold.4
+ __49-[RMConnectionEndpoint initWithConnection:queue:]_block_invoke.cold.5
+ __50-[RMInternalServiceClient getNumClientsWithReply:]_block_invoke_2.cold.1
+ __50-[RMInternalServiceClient getNumClientsWithReply:]_block_invoke_2.cold.2
+ __51-[RMConnectionEndpoint sendMessage:withData:reply:]_block_invoke.cold.1
+ __51-[RMConnectionEndpoint sendMessage:withData:reply:]_block_invoke.cold.2
+ __51-[RMConnectionEndpoint sendMessage:withData:reply:]_block_invoke.cold.3
+ __51-[RMConnectionEndpoint sendMessage:withData:reply:]_block_invoke.cold.4
+ __51-[RMConnectionEndpoint sendMessage:withData:reply:]_block_invoke.cold.5
+ __54-[RMConnectionEndpoint startServingStreamWithHandler:]_block_invoke.cold.1
+ __54-[RMConnectionEndpoint startServingStreamWithHandler:]_block_invoke.cold.2
+ __54-[RMConnectionEndpoint startServingStreamWithHandler:]_block_invoke.cold.3
+ __54-[RMConnectionEndpoint startServingStreamWithHandler:]_block_invoke.cold.4
+ __54-[RMInternalServiceClient disconnectClient:withReply:]_block_invoke_2.cold.1
+ __54-[RMInternalServiceClient disconnectClient:withReply:]_block_invoke_2.cold.2
+ __57-[RMInternalServiceClient disconnectAllClientsWithReply:]_block_invoke_2.cold.1
+ __57-[RMInternalServiceClient disconnectAllClientsWithReply:]_block_invoke_2.cold.2
+ __64-[RMConnectionClient requestStreamingWithMessage:data:callback:]_block_invoke.cold.1
+ __67-[RMConnectionEndpoint requestStreamWithMessage:data:errorHandler:]_block_invoke.100.cold.1
+ __67-[RMConnectionEndpoint requestStreamWithMessage:data:errorHandler:]_block_invoke.cold.1
+ __70-[RMConnectionEndpoint startReceivingStreamOnConnection:errorHandler:]_block_invoke.cold.1
+ __70-[RMConnectionEndpoint startReceivingStreamOnConnection:errorHandler:]_block_invoke.cold.2
+ __70-[RMConnectionEndpoint startReceivingStreamOnConnection:errorHandler:]_block_invoke.cold.3
+ __70-[RMConnectionEndpoint startReceivingStreamOnConnection:errorHandler:]_block_invoke.cold.4
+ __97-[RMRelativeMotionManager startReceivingAudioListenerPoseWithForceSessionRestart:statusCallback:]_block_invoke_2.cold.1
+ ___block_descriptor_40_e8_32bs_e37_v96?0{?={?=dddd}dqdddd}8"NSError"88l
+ ___block_descriptor_40_e8_32w_e37_v96?0{?={?=dddd}dqdddd}8"NSError"88l
+ _memcpy
+ _objc_msgSend$_initWithAttitude:consumedAuxTimestamp:receivedAuxTimestamp:machAbsTimestamp:presentationTimestamp:
+ _objc_msgSend$presentationTimestamp
- -[RMPose _initWithAttitude:consumedAuxTimestamp:receivedAuxTimestamp:machAbsTimestamp:]
- -[RMPose setMachAbsTimestamp:]
- GCC_except_table51
- ___block_descriptor_40_e8_32bs_e36_v88?0{?={?=dddd}dqddd}8"NSError"80l
- ___block_descriptor_40_e8_32w_e36_v88?0{?={?=dddd}dqddd}8"NSError"80l
- _objc_msgSend$_initWithAttitude:consumedAuxTimestamp:receivedAuxTimestamp:machAbsTimestamp:
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RelativeMotion/Common/RMConnectionClient.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RelativeMotion/Common/RMConnectionEndpoint.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RelativeMotion/RelativeMotion/RMDummyDataManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/RelativeMotion/RelativeMotion/RMRelativeMotionManager.m"
+ "@56@0:8@16d24d32d40d48"
+ "RMPose,q.x,%f,q.y,%f,q.z,%f,q.w,%f,consumedAuxTimestamp,%f,receivedAuxTimestamp,%f,machAbsTimestamp,%f,presentationTimestamp,%f,timestamp,%f"
+ "RMPoseEncodingKeyPresentationTimestamp"
+ "Td,R,N,V_machAbsTimestamp"
+ "Td,R,N,V_presentationTimestamp"
+ "[2{?=\"quaternion\"{?=\"x\"d\"y\"d\"z\"d\"w\"d}\"timestamp\"d\"error\"q\"consumedAuxTimestamp\"d\"receivedAuxTimestamp\"d\"machAbsTimestamp\"d\"presentationTimestamp\"d}]"
+ "[RelativeMotionManager] currentAudioListenerPose RMPose,q.x,%{private}f,q.y,%{private}f,q.z,%{private}f,q.w,%{private}f,consumedAuxTimestamp,%{private}f,receivedAuxTimestamp,%{private}f,machAbsTimestamp,%{private}f,presentationTimestamp,%{private}f,timestamp,%{private}f"
+ "_initWithAttitude:consumedAuxTimestamp:receivedAuxTimestamp:machAbsTimestamp:presentationTimestamp:"
+ "_presentationTimestamp"
+ "presentationTimestamp"
+ "v96@?0{?={?=dddd}dqdddd}8@\"NSError\"88"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RelativeMotion/Common/RMConnectionClient.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RelativeMotion/Common/RMConnectionEndpoint.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RelativeMotion/RelativeMotion/RMDummyDataManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/RelativeMotion/RelativeMotion/RMRelativeMotionManager.m"
- "@48@0:8@16d24d32d40"
- "RMPose,q.x,%f,q.y,%f,q.z,%f,q.w,%f,consumedAuxTimestamp,%f,receivedAuxTimestamp,%f,machAbsTimestamp,%f,timestamp,%f"
- "Td,N,V_machAbsTimestamp"
- "[2{?=\"quaternion\"{?=\"x\"d\"y\"d\"z\"d\"w\"d}\"timestamp\"d\"error\"q\"consumedAuxTimestamp\"d\"receivedAuxTimestamp\"d\"machAbsTimestamp\"d}]"
- "[RelativeMotionManager] currentAudioListenerPose RMPose,q.x,%{private}f,q.y,%{private}f,q.z,%{private}f,q.w,%{private}f,consumedAuxTimestamp,%{private}f,receivedAuxTimestamp,%{private}f,machAbsTimestamp,%{private}f,timestamp,%{private}f"
- "_initWithAttitude:consumedAuxTimestamp:receivedAuxTimestamp:machAbsTimestamp:"
- "setMachAbsTimestamp:"
- "v88@?0{?={?=dddd}dqddd}8@\"NSError\"80"

```
