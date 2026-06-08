## AccessoryHID

> `/System/Library/PrivateFrameworks/AccessoryHID.framework/AccessoryHID`

```diff

-1147.120.2.0.0
-  __TEXT.__text: 0x3610
-  __TEXT.__auth_stubs: 0x380
+1176.0.26.502.1
+  __TEXT.__text: 0x3260
   __TEXT.__objc_methlist: 0x294
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x1c5
+  __TEXT.__cstring: 0x1c9
   __TEXT.__oslogstring: 0x424
   __TEXT.__gcc_except_tab: 0xac
   __TEXT.__unwind_info: 0x128
-  __TEXT.__objc_classname: 0x5c
-  __TEXT.__objc_methname: 0x766
-  __TEXT.__objc_methtype: 0x3aa
-  __TEXT.__objc_stubs: 0x440
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x188
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1c8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x220
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1d0
-  __AUTH_CONST.__const: 0x80
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0x348
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x14
   __DATA.__data: 0x1f8
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x40
   __DATA.__common: 0xc
   __DATA_DIRTY.__data: 0x20
   __DATA_DIRTY.__common: 0x10

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 65B7254D-3CEC-3A0D-B1DE-5467685CC3C3
-  Functions: 67
-  Symbols:   330
-  CStrings:  189
+  UUID: D64CF664-8C75-395A-B9E9-63A0A195CF7E
+  Functions: 71
+  Symbols:   338
+  CStrings:  61
 
Symbols:
+ __MergedGlobals.4
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_tmp.3
+ ___block_literal_global.142
+ ___logObjectForModule_block_invoke
+ ___logObjectForModule_block_invoke.cold.1
+ _logObjectForModule.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x26
+ _objc_retain_x8
- _OUTLINED_FUNCTION_8
- __MergedGlobals.2
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
- _objc_retain_x23
- _objc_retain_x24
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<AccessoryHIDClientProtocol>\""
- "@\"<AccessoryHIDXPCServerProtocol>\""
- "@\"NSLock\""
- "@\"NSMutableDictionary\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "AccessoryHIDClient"
- "AccessoryHIDXPCClientProtocol"
- "AccessoryHIDXPCServerProtocol"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<AccessoryHIDClientProtocol>\",W,N,V_delegate"
- "T@\"<AccessoryHIDXPCServerProtocol>\",&,N,V_remoteObject"
- "T@\"NSLock\",&,N,V_registeredHIDDescriptorsLock"
- "T@\"NSMutableDictionary\",&,V_registeredHIDDescriptors"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",&,N,V_serverConnection"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_delegate"
- "_registeredHIDDescriptors"
- "_registeredHIDDescriptorsLock"
- "_remoteObject"
- "_serverConnection"
- "autorelease"
- "class"
- "componentUpdate:componentID:enabled:withReply:"
- "conformsToProtocol:"
- "connectToServer"
- "countByEnumeratingWithState:objects:count:"
- "createHIDDescriptor:"
- "dealloc"
- "debugDescription"
- "delegate"
- "deleteHIDDescriptor:"
- "description"
- "getReport:componentID:reportType:reportID:withReply:"
- "getReportResponse:componentID:reportType:reportID:report:withReply:"
- "hash"
- "hidDescriptor:active:"
- "inReport:componentID:report:withReply:"
- "init"
- "initConnection:"
- "initWithDelegate:"
- "initWithMachServiceName:options:"
- "initWithUnsignedInt:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lock"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "outReport:componentID:report:withReply:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "processGetReportResponse:reportType:reportID:forUUID:"
- "processInReport:forUUID:"
- "registerHIDDescriptor:componentID:dictionary:withReply:"
- "registeredHIDDescriptors"
- "registeredHIDDescriptorsLock"
- "release"
- "remoteObject"
- "remoteObjectProxyWithErrorHandler:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "sendGetReportForType:andID:fromUUID:"
- "sendOutReport:fromUUID:"
- "serverConnection"
- "setDelegate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setObject:forKey:"
- "setRegisteredHIDDescriptors:"
- "setRegisteredHIDDescriptorsLock:"
- "setRemoteObject:"
- "setRemoteObjectInterface:"
- "setServerConnection:"
- "superclass"
- "unlock"
- "unregisterAllDescriptors:withReply:"
- "unregisterHIDDescriptor:componentID:withReply:"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B>16"
- "v28@0:8@16B24"
- "v32@0:8@\"NSString\"16@?<v@?B>24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v36@0:8@\"NSString\"16S24@?<v@?B>28"
- "v36@0:8@16S24@?28"
- "v40@0:8@16@24@32"
- "v44@0:8@\"NSString\"16@\"NSNumber\"24B32@?<v@?B>36"
- "v44@0:8@\"NSString\"16S24@\"NSData\"28@?<v@?B>36"
- "v44@0:8@\"NSString\"16S24@\"NSDictionary\"28@?<v@?@\"NSString\">36"
- "v44@0:8@16@24B32@?36"
- "v44@0:8@16S24@28@?36"
- "v48@0:8@\"NSString\"16@\"NSNumber\"24@\"NSData\"32@?<v@?B>40"
- "v48@0:8@16@24@32@?40"
- "v52@0:8@\"NSString\"16S24C28C32@\"NSData\"36@?<v@?B>44"
- "v52@0:8@16S24C28C32@36@?44"
- "v56@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@?<v@?B>48"
- "v56@0:8@16@24@32@40@?48"
- "zone"

```
