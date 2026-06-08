## splashboardd

> `/usr/libexec/splashboardd`

```diff

-308.4.1.0.0
-  __TEXT.__text: 0x5af4
-  __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_stubs: 0x16e0
-  __TEXT.__objc_methlist: 0x4e4
+318.100.0.0.0
+  __TEXT.__text: 0x5768
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_stubs: 0x1800
+  __TEXT.__objc_methlist: 0x4e8
   __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x43a
-  __TEXT.__gcc_except_tab: 0x360
-  __TEXT.__objc_methname: 0x16cb
-  __TEXT.__objc_classname: 0xcb
-  __TEXT.__objc_methtype: 0x36d
-  __TEXT.__oslogstring: 0xa40
-  __TEXT.__unwind_info: 0x228
-  __DATA_CONST.__auth_got: 0x348
-  __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0x270
-  __DATA_CONST.__cfstring: 0x3a0
+  __TEXT.__cstring: 0x542
+  __TEXT.__gcc_except_tab: 0x31c
+  __TEXT.__objc_methname: 0x1760
+  __TEXT.__objc_classname: 0xe6
+  __TEXT.__objc_methtype: 0x49f
+  __TEXT.__oslogstring: 0xa86
+  __TEXT.__unwind_info: 0x1d8
+  __DATA_CONST.__const: 0x2c0
+  __DATA_CONST.__cfstring: 0x400
   __DATA_CONST.__objc_classlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x10
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x930
-  __DATA.__objc_selrefs: 0x730
-  __DATA.__objc_ivar: 0x58
+  __DATA_CONST.__auth_got: 0x378
+  __DATA_CONST.__got: 0x208
+  __DATA.__objc_const: 0xd60
+  __DATA.__objc_selrefs: 0x768
+  __DATA.__objc_ivar: 0x6c
   __DATA.__objc_data: 0x230
-  __DATA.__data: 0xc0
+  __DATA.__data: 0x120
   __DATA.__bss: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ACFF75B3-0BF4-3B05-87F4-0AE393252B02
-  Functions: 138
-  Symbols:   186
-  CStrings:  439
+  UUID: E258D217-E524-30A6-AD7E-C5F3D2DEC8B2
+  Functions: 143
+  Symbols:   187
+  CStrings:  467
 
Symbols:
+ _NSStringFromClass
+ _NSStringFromSelector
+ _OBJC_CLASS_$_BSServiceConnection
+ _OBJC_CLASS_$_BSServiceConnectionListener
+ _OBJC_CLASS_$_BSServiceConnectionListenerConfiguration
+ _OBJC_CLASS_$_BSServiceDispatchQueue
+ _OBJC_CLASS_$_BSServiceQuality
+ _OBJC_CLASS_$_BSServicesConfiguration
+ _XBApplicationLaunchImageDomainName
+ _XBServiceLaunchImageInterface
+ __bs_set_crash_log_message
+ __os_log_default
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x8
- OBJC_IVAR_$_BSBaseXPCServer._queue
- _BSDeserializeBSXPCEncodableObjectFromXPCDictionaryWithKey
- _BSPIDForXPCConnection
- _BSProcessDescriptionForPID
- _BSSerializeDataToXPCDictionaryWithKey
- _OBJC_CLASS_$_BSAuditToken
- _OBJC_CLASS_$_BSBaseXPCServer
- _OBJC_CLASS_$_BSXPCReply
- _OBJC_METACLASS_$_BSBaseXPCServer
- _XBLaunchImageProviderMessageKeyCaptureInfo
- _XBLaunchImageProviderMessageKeyCompatibilityInfo
- _XBLaunchImageProviderMessageKeyContextID
- _XBLaunchImageProviderMessageKeyCreateCaptureInfo
- _XBLaunchImageProviderMessageKeyError
- _XBLaunchImageProviderMessageKeyLaunchRequest
- _XBLaunchImageProviderMessageKeyMessageType
- _XBLaunchImageProviderMessageKeyWithTimeout
- _objc_retain_x25
- _objc_retain_x26
- _xpc_dictionary_get_bool
- _xpc_dictionary_get_int64
- _xpc_dictionary_set_int64
CStrings:
+ "-[XBLaunchImageProviderServer activate]_block_invoke"
+ "@\"<BSInvalidatable>\""
+ "@\"BSServiceConnectionListener\""
+ "@\"BSServiceConnectionListenerConfiguration\""
+ "@\"BSServiceDispatchQueue\""
+ "@\"NSString\""
+ "@40@0:8@16@24@32"
+ "UTF8String"
+ "XBServiceLaunchImageClientInterface"
+ "_domain"
+ "_domainToken"
+ "_listener"
+ "_listenerConfig"
+ "_listenerQueue"
+ "activate"
+ "activateManualDomain:"
+ "assertBarrierOnQueue"
+ "boolValue"
+ "configurationWithDomain:service:"
+ "configure:"
+ "contextWrapperForAppInfo:launchRequest:captureOptions:"
+ "currentContext"
+ "domain must be non-null since listenerConfig is non-null"
+ "domain must be null since listenerConfig is null"
+ "endpoint"
+ "failure in %{public}@ of <%{public}@:%p> (%{public}@:%i) : %{public}@"
+ "getLaunchImageForApp:launchRequest:createCaptureInfo:withTimeout:reply:"
+ "initWithConfig:domain:serviceInterface:"
+ "listenerWithConfiguration:handler:"
+ "numberWithUnsignedInt:"
+ "performAsync:"
+ "preheat"
+ "queueWithName:serviceQuality:"
+ "remoteToken"
+ "setInterface:"
+ "setInterfaceTarget:"
+ "setInvalidationHandler:"
+ "setQueue:"
+ "userInteractive"
+ "v16@?0@\"<BSServiceListenerConnectionConfiguring>\"8"
+ "v16@?0@\"BSServiceConnection<BSServiceConnectionContext>\"8"
+ "v16@?0@\"BSServiceListenerConnection\"8"
+ "v56@0:8@\"XBApplicationLaunchCompatibilityInfo\"16@\"XBLaunchStateRequest\"24@\"NSNumber\"32@\"NSNumber\"40@?<v@?@\"NSNumber\"@\"XBLaunchCaptureInformation\"@\"XBLaunchImageError\">48"
+ "v56@0:8@16@24@32@40@?48"
- "-[XBLaunchImageProviderServer run]_block_invoke"
- "@24@0:8@16"
- "I64@0:8@16@24@32^@40q48^@56"
- "_handlePreheat:forClient:"
- "_onMain_createLaunchWindowForClient:withLaunchRequest:appInfo:captureInfo:captureOptions:error:"
- "_queue_handleGetLaunchImage:forClient:"
- "_removeTransactionWorkForClient:"
- "_setTransactionWork:forClient:"
- "_transactionWorkForClient:"
- "bs_secureEncoded"
- "connection"
- "initWithServiceName:"
- "queue"
- "queue_clientAdded:"
- "queue_clientRemoved:"
- "queue_handleMessage:client:"
- "replyForMessage:"
- "sendReply:"
- "tokenFromXPCConnection:"
- "v16@?0@\"NSObject<OS_xpc_object>\"8"

```
