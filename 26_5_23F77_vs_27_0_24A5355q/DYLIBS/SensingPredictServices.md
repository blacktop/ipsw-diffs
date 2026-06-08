## SensingPredictServices

> `/System/Library/PrivateFrameworks/SensingPredictServices.framework/SensingPredictServices`

```diff

-11.28.0.0.0
-  __TEXT.__text: 0x1748
-  __TEXT.__auth_stubs: 0x210
+20.26.0.0.1
+  __TEXT.__text: 0x16e0
   __TEXT.__objc_methlist: 0x270
-  __TEXT.__cstring: 0x477
+  __TEXT.__cstring: 0x47b
   __TEXT.__const: 0x8
-  __TEXT.__unwind_info: 0xe0
-  __TEXT.__objc_classname: 0x62
-  __TEXT.__objc_methname: 0x593
-  __TEXT.__objc_methtype: 0x17b
-  __TEXT.__objc_stubs: 0x2e0
-  __DATA_CONST.__got: 0x28
+  __TEXT.__unwind_info: 0xd8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x108
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_selrefs: 0x178
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x110
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x1a0
   __AUTH_CONST.__objc_const: 0x4f8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x38
   __DATA.__data: 0x1f0

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C461F971-6801-300D-B785-09A6B53B8BB1
+  UUID: 266039C5-01CD-3A67-B1B6-A27A41E122DE
   Functions: 67
-  Symbols:   273
-  CStrings:  168
+  Symbols:   275
+  CStrings:  64
 
Symbols:
+ ___block_literal_global.104
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x8
- ___block_literal_global.38
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[SPContext descriptionWithLevel:] : 232 -> 244
~ -[SPContextMonitor init] : 156 -> 148
~ -[SPContextMonitor setContextChangeFlags:] : 176 -> 172
~ ___42-[SPContextMonitor setContextChangeFlags:]_block_invoke : 104 -> 100
~ -[SPContextMonitor description] : 92 -> 76
~ -[SPContextMonitor activateWithCompletion:] : 160 -> 152
~ ___43-[SPContextMonitor activateWithCompletion:]_block_invoke : 272 -> 268
~ -[SPContextMonitor _activate:] : 596 -> 588
~ ___30-[SPContextMonitor _activate:]_block_invoke : 196 -> 208
~ ___30-[SPContextMonitor _activate:]_block_invoke_2 : 340 -> 336
~ -[SPContextMonitor _ensureXPCStarted] : 384 -> 376
~ -[SPContextMonitor _interrupted] : 204 -> 200
~ ___30-[SPContextMonitor invalidate]_block_invoke : 280 -> 276
~ -[SPContextMonitor _invalidated] : 372 -> 368
~ -[SPContextMonitor setDispatchQueue:] : 64 -> 12
CStrings:
- ".cxx_destruct"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "C"
- "C16@0:8"
- "I"
- "I16@0:8"
- "NSCoding"
- "NSSecureCoding"
- "SPContext"
- "SPXPCClientInterface"
- "SPXPCServiceInterface"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_dispatchQueue"
- "T@?,C,N,V_contextChangeHandler"
- "T@?,C,N,V_contextSignalUpdatedHandler"
- "T@?,C,N,V_interruptionHandler"
- "T@?,C,N,V_invalidationHandler"
- "TB,R"
- "TC,N,V_locationCategory"
- "TI,N,V_clientID"
- "TI,N,V_contextChangeFlags"
- "TI,R,N,V_noiseLevel"
- "_activate:"
- "_activateCalled"
- "_activateCompletion"
- "_clientID"
- "_contextChangeFlags"
- "_contextChangeHandler"
- "_contextSignalUpdatedHandler"
- "_dispatchQueue"
- "_ensureXPCStarted"
- "_interrupted"
- "_interruptionHandler"
- "_invalidateCalled"
- "_invalidateDone"
- "_invalidated"
- "_invalidationHandler"
- "_locationCategory"
- "_noiseLevel"
- "_reportError:"
- "_setQueue:"
- "_xpcCnx"
- "activateWithCompletion:"
- "clientID"
- "contextChangeFlags"
- "contextChangeHandler"
- "contextMonitorActivate:completion:"
- "contextMonitorContextChanged:"
- "contextMonitorUpdate:"
- "contextSignalUpdated:fusedState:"
- "contextSignalUpdatedHandler"
- "description"
- "descriptionWithLevel:"
- "dispatchQueue"
- "encodeInt64:forKey:"
- "encodeInteger:forKey:"
- "encodeWithCoder:"
- "init"
- "initWithCoder:"
- "initWithServiceName:"
- "interfaceWithProtocol:"
- "interruptionHandler"
- "invalidate"
- "invalidationHandler"
- "isSystemContext"
- "locationCategory"
- "noiseLevel"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "resume"
- "setClientID:"
- "setContextChangeFlags:"
- "setContextChangeHandler:"
- "setContextSignalUpdatedHandler:"
- "setDispatchQueue:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setLocationCategory:"
- "setRemoteObjectInterface:"
- "supportsSecureCoding"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v20@0:8I16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"SPContext\"16"
- "v24@0:8@\"SPContextMonitor\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v28@0:8@\"SPContext\"16I24"
- "v28@0:8@16I24"
- "v32@0:8@\"SPContextMonitor\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@?24"

```
