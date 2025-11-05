## GameControllerFoundation

> `/System/Library/PrivateFrameworks/GameControllerFoundation.framework/Versions/A/GameControllerFoundation`

```diff

-12.3.1.0.0
-  __TEXT.__text: 0x662c0
-  __TEXT.__auth_stubs: 0x1260
-  __TEXT.__objc_methlist: 0x55ec
-  __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0x6301
-  __TEXT.__gcc_except_tab: 0x29ec
-  __TEXT.__oslogstring: 0x2fd9
+12.4.12.0.0
+  __TEXT.__text: 0x75fec
+  __TEXT.__auth_stubs: 0x1280
+  __TEXT.__objc_methlist: 0x6694
+  __TEXT.__const: 0x118
+  __TEXT.__gcc_except_tab: 0x337c
+  __TEXT.__cstring: 0x6b0d
+  __TEXT.__oslogstring: 0x3159
   __TEXT.__ustring: 0x58
-  __TEXT.__unwind_info: 0x1e34
-  __TEXT.__objc_classname: 0x169c
-  __TEXT.__objc_methname: 0x7e5e
-  __TEXT.__objc_methtype: 0x254a
-  __TEXT.__objc_stubs: 0x4d60
-  __DATA_CONST.__got: 0x130
+  __TEXT.__unwind_info: 0x20f8
+  __TEXT.__eh_frame: 0x48
+  __TEXT.__objc_classname: 0x176b
+  __TEXT.__objc_methname: 0x89e2
+  __TEXT.__objc_methtype: 0x29c7
+  __TEXT.__objc_stubs: 0x5240
+  __DATA_CONST.__got: 0x4c8
   __DATA_CONST.__const: 0xb00
-  __DATA_CONST.__objc_classlist: 0x448
-  __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x148
+  __DATA_CONST.__objc_classlist: 0x468
+  __DATA_CONST.__objc_catlist: 0x70
+  __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x100a0
-  __DATA_CONST.__objc_selrefs: 0x1a20
-  __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_classrefs: 0x438
-  __DATA_CONST.__objc_superrefs: 0x410
-  __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__cfstring: 0x6520
-  __AUTH_CONST.__objc_const: 0x4208
-  __AUTH_CONST.__const: 0x1600
-  __AUTH_CONST.__objc_intobj: 0x228
-  __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x948
-  __AUTH.__objc_data: 0x2ad0
+  __DATA_CONST.__objc_selrefs: 0x1ca8
+  __DATA_CONST.__objc_protorefs: 0xb8
+  __DATA_CONST.__objc_superrefs: 0x430
+  __DATA_CONST.__objc_arraydata: 0x140
+  __AUTH_CONST.__auth_got: 0x958
+  __AUTH_CONST.__const: 0x18a0
+  __AUTH_CONST.__cfstring: 0x6b00
+  __AUTH_CONST.__objc_const: 0x140e0
+  __AUTH_CONST.__objc_intobj: 0x240
+  __AUTH_CONST.__objc_dictobj: 0x78
+  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH.__objc_data: 0x2c10
   __AUTH.__data: 0x10b0
-  __DATA.__objc_ivar: 0x764
-  __DATA.__data: 0xf60
+  __DATA.__objc_ivar: 0x7fc
+  __DATA.__data: 0x1080
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x198
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B8E42A1A-1D61-3156-9A16-9AB2F754C5FF
-  Functions: 2496
-  Symbols:   6436
-  CStrings:  3970
+  UUID: 72CCA5BE-A30F-3C0A-800C-CF5B842AF76C
+  Functions: 2844
+  Symbols:   7047
+  CStrings:  4207
 
Symbols:
+ +[GCConfigXPCServiceServiceConnection connection:withClient:].cold.1
+ +[GCConsoleUserMonitor sharedInstance].cold.1
+ +[GCDisposable withCleanupHandler:]
+ +[GCFuture allocWithZone:].cold.1
+ +[GCFuture alloc].cold.1
+ +[GCFuture cancelledFuture].cold.1
+ +[GCFuture futureOnQueue:withBlock:].cold.1
+ +[GCFuture futureOnQueue:withOptions:block:].cold.1
+ +[GCFuture futureWithBlock:].cold.1
+ +[GCFuture futureWithError:].cold.1
+ +[GCFuture futureWithLabel:block:].cold.1
+ +[GCFuture futureWithLabel:onQueue:block:].cold.1
+ +[GCFuture futureWithOptions:block:].cold.1
+ +[GCFuture futureWithResult:].cold.1
+ +[GCGenericDeviceDataProcessorExpressionModel(Serialization) modelWithDictionaryRepresentation:error:].cold.1
+ +[GCGenericDeviceMotionEventDriverModel description]
+ +[GCGenericDeviceMotionEventDriverModel supportsSecureCoding]
+ +[GCGenericDeviceMotionEventDriverModel(Serialization) modelWithDictionaryRepresentation:error:]
+ +[GCGenericDeviceMotionEventDriverModelBuilder modelClass]
+ +[GCIPCRemoteIncomingConnection sharedConnectionWorkloop].cold.1
+ +[GCIPCRemoteOutgoingConnection sharedConnectionWorkloop].cold.1
+ +[GCOperation allocWithZone:].cold.1
+ +[GCOperation alloc].cold.1
+ +[GCVersion currentSourceVersion].cold.1
+ +[NSBundle(GC) GameControllerFoundationBundle].cold.1
+ +[NSBundle(GC) GameControllerFrameworkBundle].cold.1
+ +[NSValue(GC) gc_valueWithSimdFloat4x4:]
+ +[_GCDeviceDriverServiceConnection connectionToServiceInDriver:withClient:].cold.1
+ +[_GCDeviceDriverServiceConnection connectionToServiceInDriver:withClient:].cold.2
+ -[GCConfigXPCServiceServiceConnection initWithConnection:serviceVendor:].cold.1
+ -[GCConfigXPCServiceServiceConnection initWithConnection:serviceVendor:].cold.2
+ -[GCConfigurationAssetManagementServiceXPCProxy initWithService:].cold.1
+ -[GCConfigurationAssetXPCProxy initWithAsset:].cold.1
+ -[GCDevicePhysicalInputCapacitiveButtonElementDescription setTouchedThreshold:]
+ -[GCDevicePhysicalInputCapacitiveButtonElementDescription touchedThreshold]
+ -[GCDevicePhysicalInputSourceDescription initWithElementAliases:localizedName:symbol:direction:].cold.1
+ -[GCDevicePhysicalInputSymbolDescription initWithSFSymbolsName:].cold.1
+ -[GCDisposable .cxx_destruct]
+ -[GCDisposable dealloc]
+ -[GCDisposable initWithCleanupHandler:]
+ -[GCFLocalizedString initWithKey:sourceBundle:table:]
+ -[GCGenericDeviceDataAddExpressionModel(Compilation) buildExpressionWithContext:error:]
+ -[GCGenericDeviceDataAddExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]
+ -[GCGenericDeviceDataAddExpressionModelBuilder build].cold.1
+ -[GCGenericDeviceDataAddExpressionModelBuilder build].cold.2
+ -[GCGenericDeviceDataBitTestExpressionModel(Compilation) buildExpressionWithContext:error:]
+ -[GCGenericDeviceDataBitTestExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]
+ -[GCGenericDeviceDataBitTestExpressionModelBuilder build].cold.1
+ -[GCGenericDeviceDataBitTestExpressionModelBuilder build].cold.2
+ -[GCGenericDeviceDataBitTestExpressionModelBuilder build].cold.3
+ -[GCGenericDeviceDataBitTestExpressionModelBuilder build].cold.4
+ -[GCGenericDeviceDataClampExpressionModel(Compilation) buildExpressionWithContext:error:]
+ -[GCGenericDeviceDataClampExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]
+ -[GCGenericDeviceDataClampExpressionModelBuilder build].cold.1
+ -[GCGenericDeviceDataConstantExpressionModel(Compilation) buildExpressionWithContext:error:]
+ -[GCGenericDeviceDataConstantExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]
+ -[GCGenericDeviceDataElementExistsExpressionModel(Compilation) buildExpressionWithContext:error:]
+ -[GCGenericDeviceDataElementExistsExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]
+ -[GCGenericDeviceDataElementExistsExpressionModelBuilder build].cold.1
+ -[GCGenericDeviceDataElementExistsExpressionModelBuilder build].cold.2
+ -[GCGenericDeviceDataElementExistsExpressionModelBuilder build].cold.3
+ -[GCGenericDeviceDataInputElementAttributeExpressionModel(Compilation) buildExpressionWithContext:error:]
+ -[GCGenericDeviceDataInputElementAttributeExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]
+ -[GCGenericDeviceDataInputElementAttributeExpressionModelBuilder build].cold.1
+ -[GCGenericDeviceDataInputElementAttributeExpressionModelBuilder build].cold.2
+ -[GCGenericDeviceDataInputElementValueExpressionModel(Compilation) buildExpressionWithContext:error:]
+ -[GCGenericDeviceDataInputElementValueExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]
+ -[GCGenericDeviceDataInputElementValueExpressionModelBuilder build].cold.1
+ -[GCGenericDeviceDataInterpolateExpressionModel(Compilation) buildExpressionWithContext:error:]
+ -[GCGenericDeviceDataInterpolateExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]
+ -[GCGenericDeviceDataInterpolateExpressionModelBuilder build].cold.1
+ -[GCGenericDeviceDataInterpolateExpressionModelBuilder build].cold.2
+ -[GCGenericDeviceDataInterpolateExpressionModelBuilder build].cold.3
+ -[GCGenericDeviceDataInterpolateExpressionModelBuilder build].cold.4
+ -[GCGenericDeviceDataInterpolateExpressionModelBuilder build].cold.5
+ -[GCGenericDeviceDataMultiplyExpressionModel(Compilation) buildExpressionWithContext:error:]
+ -[GCGenericDeviceDataMultiplyExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]
+ -[GCGenericDeviceDataMultiplyExpressionModelBuilder build].cold.1
+ -[GCGenericDeviceDataMultiplyExpressionModelBuilder build].cold.2
+ -[GCGenericDeviceDataProcessorExpressionModel(Compilation) buildExpressionWithContext:error:]
+ -[GCGenericDeviceDataProcessorExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]
+ -[GCGenericDeviceDataRumbleMotorValueExpressionModelBuilder build].cold.1
+ -[GCGenericDeviceDataSDLHatFunctionExpressionModel(Compilation) buildExpressionWithContext:error:]
+ -[GCGenericDeviceDataSDLHatFunctionExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]
+ -[GCGenericDeviceDataSDLHatFunctionExpressionModelBuilder build].cold.1
+ -[GCGenericDeviceDataSDLHatFunctionExpressionModelBuilder build].cold.2
+ -[GCGenericDeviceDataSDLHatFunctionExpressionModelBuilder build].cold.3
+ -[GCGenericDeviceDataSDLHatFunctionExpressionModelBuilder build].cold.4
+ -[GCGenericDeviceDataSDLHatFunctionExpressionModelBuilder build].cold.5
+ -[GCGenericDeviceDataSDLHatFunctionExpressionModelBuilder build].cold.6
+ -[GCGenericDeviceDriverModel motion]
+ -[GCGenericDeviceDriverModelBuilder build].cold.1
+ -[GCGenericDeviceDriverModelBuilder motion]
+ -[GCGenericDeviceDriverModelBuilder setMotion:]
+ -[GCGenericDeviceDriverPropertiesModelBuilder build].cold.1
+ -[GCGenericDeviceDriverPropertyModelBuilder build].cold.1
+ -[GCGenericDeviceDriverPropertyModelBuilder build].cold.2
+ -[GCGenericDeviceElementModelBuilder build].cold.1
+ -[GCGenericDeviceElementModelBuilder build].cold.2
+ -[GCGenericDeviceInputEventDriverModelBuilder build].cold.1
+ -[GCGenericDeviceModelBuilder build].cold.1
+ -[GCGenericDeviceMotionEventDriverModel .cxx_destruct]
+ -[GCGenericDeviceMotionEventDriverModel accelerometerXExpression]
+ -[GCGenericDeviceMotionEventDriverModel accelerometerYExpression]
+ -[GCGenericDeviceMotionEventDriverModel accelerometerZExpression]
+ -[GCGenericDeviceMotionEventDriverModel copyWithZone:]
+ -[GCGenericDeviceMotionEventDriverModel debugDescription]
+ -[GCGenericDeviceMotionEventDriverModel encodeWithCoder:]
+ -[GCGenericDeviceMotionEventDriverModel gyroXExpression]
+ -[GCGenericDeviceMotionEventDriverModel gyroYExpression]
+ -[GCGenericDeviceMotionEventDriverModel gyroZExpression]
+ -[GCGenericDeviceMotionEventDriverModel hash]
+ -[GCGenericDeviceMotionEventDriverModel initWithCoder:]
+ -[GCGenericDeviceMotionEventDriverModel init]
+ -[GCGenericDeviceMotionEventDriverModel isEqual:]
+ -[GCGenericDeviceMotionEventDriverModelBuilder .cxx_destruct]
+ -[GCGenericDeviceMotionEventDriverModelBuilder accelerometerXExpression]
+ -[GCGenericDeviceMotionEventDriverModelBuilder accelerometerYExpression]
+ -[GCGenericDeviceMotionEventDriverModelBuilder accelerometerZExpression]
+ -[GCGenericDeviceMotionEventDriverModelBuilder build]
+ -[GCGenericDeviceMotionEventDriverModelBuilder gyroXExpression]
+ -[GCGenericDeviceMotionEventDriverModelBuilder gyroYExpression]
+ -[GCGenericDeviceMotionEventDriverModelBuilder gyroZExpression]
+ -[GCGenericDeviceMotionEventDriverModelBuilder hash]
+ -[GCGenericDeviceMotionEventDriverModelBuilder init]
+ -[GCGenericDeviceMotionEventDriverModelBuilder initializeWithModel:]
+ -[GCGenericDeviceMotionEventDriverModelBuilder isEqual:]
+ -[GCGenericDeviceMotionEventDriverModelBuilder reset]
+ -[GCGenericDeviceMotionEventDriverModelBuilder setAccelerometerXExpression:]
+ -[GCGenericDeviceMotionEventDriverModelBuilder setAccelerometerYExpression:]
+ -[GCGenericDeviceMotionEventDriverModelBuilder setAccelerometerZExpression:]
+ -[GCGenericDeviceMotionEventDriverModelBuilder setGyroXExpression:]
+ -[GCGenericDeviceMotionEventDriverModelBuilder setGyroYExpression:]
+ -[GCGenericDeviceMotionEventDriverModelBuilder setGyroZExpression:]
+ -[GCGenericDevicePhysicalInputButtonModel pressedThreshold]
+ -[GCGenericDevicePhysicalInputButtonModel sourcePressedValueExtendedEventFieldIndex]
+ -[GCGenericDevicePhysicalInputButtonModel sourceTouchedValueExtendedEventFieldIndex]
+ -[GCGenericDevicePhysicalInputButtonModel touchedThreshold]
+ -[GCGenericDevicePhysicalInputButtonModelBuilder pressedThreshold]
+ -[GCGenericDevicePhysicalInputButtonModelBuilder setPressedThreshold:]
+ -[GCGenericDevicePhysicalInputButtonModelBuilder setSourcePressedValueExtendedEventFieldIndex:]
+ -[GCGenericDevicePhysicalInputButtonModelBuilder setSourceTouchedValueExtendedEventFieldIndex:]
+ -[GCGenericDevicePhysicalInputButtonModelBuilder setTouchedThreshold:]
+ -[GCGenericDevicePhysicalInputButtonModelBuilder sourcePressedValueExtendedEventFieldIndex]
+ -[GCGenericDevicePhysicalInputButtonModelBuilder sourceTouchedValueExtendedEventFieldIndex]
+ -[GCGenericDevicePhysicalInputButtonModelBuilder touchedThreshold]
+ -[GCGenericDevicePhysicalInputElementModelBuilder build].cold.1
+ -[GCGenericDevicePhysicalInputElementModelBuilder build].cold.2
+ -[GCGenericDevicePhysicalInputElementModelBuilder build].cold.3
+ -[GCGenericDevicePhysicalInputModelBuilder build].cold.1
+ -[GCGenericDeviceRumbleActuatorModelBuilder build].cold.1
+ -[GCGenericDeviceRumbleModelBuilder build].cold.1
+ -[GCGenericDeviceRumbleModelBuilder build].cold.2
+ -[GCGenericDeviceRumbleModelBuilder build].cold.3
+ -[GCGenericDeviceRumbleModelBuilder build].cold.4
+ -[GCGenericDeviceRumbleOutputFieldModelBuilder build].cold.1
+ -[GCGenericDeviceRumbleOutputFieldModelBuilder build].cold.2
+ -[GCGenericDeviceRumbleOutputFieldModelBuilder build].cold.3
+ -[GCGenericDeviceRumbleOutputModelBuilder build].cold.1
+ -[GCGenericDeviceRumbleOutputModelBuilder build].cold.2
+ -[GCHIDDeviceInput setInputElementMatching:].cold.1
+ -[GCHIDDeviceInput setInputElementMatching:].cold.2
+ -[GCHIDDeviceInput setInputElements:].cold.2
+ -[GCHIDDeviceInput setInputElements:].cold.3
+ -[GCHIDEventSystemClient _observationListForType:]
+ -[GCHIDEventSystemClient activate]
+ -[GCHIDEventSystemClient conformsToProtocol:]
+ -[GCHIDEventSystemClient dealloc]
+ -[GCHIDEventSystemClient initWithQueue:type:attributes:]
+ -[GCHIDEventSystemClient initWithQueue:type:attributes:environment:]
+ -[GCHIDEventSystemClient initWithQueue:type:attributes:functions:]
+ -[GCHIDEventSystemClient invalidate]
+ -[GCHIDEventSystemClient queue]
+ -[GCHIDEventSystemClient registerEventHandler:]
+ -[GCHIDEventSystemClient registerEventObserver:]
+ -[GCHIDEventSystemClient registerServicesChangedHandler:notifyExisting:]
+ -[GCHIDEventSystemClient registerServicesChangedObserver:notifyExisting:]
+ -[GCHIDEventSystemClient serviceForRegistryID:]
+ -[GCHIDEventSystemClient services]
+ -[GCHIDEventSystemClient setCancelHandler:]
+ -[GCHIDEventSystemClient setEventCallBack:target:context:]
+ -[GCHIDEventSystemClient setEventCallBack:target:context:].cold.1
+ -[GCHIDEventSystemClient setEventCallBack:target:context:].cold.2
+ -[GCHIDEventSystemClient setMatching:]
+ -[GCHIDEventSystemClient setMatchingMultiple:]
+ -[GCHIDEventSystemClient setServicesChangedCallback:target:context:]
+ -[GCHIDEventSystemClient setServicesChangedCallback:target:context:].cold.1
+ -[GCHIDEventSystemClient unregisterEventObserver:]
+ -[GCHIDEventSystemClient unregisterServicesChangedObserver:notifyExisting:]
+ -[GCHIDServiceInfo initWithService:queue:functions:]
+ -[GCHIDServiceInfo initWithService:queue:functions:].cold.1
+ -[GCHIDServiceInfo initWithService:queue:functions:].cold.2
+ -[GCHIDServiceInfo serviceID]
+ -[GCIOIterator initWithPort:objectClass:error:].cold.1
+ -[GCIONotificationPort setQueue:cancellationHandler:].cold.1
+ -[GCIORegistryEntry setProperty:forKey:].cold.1
+ -[GCOperation _startAsynchronouslyIfNeeded].cold.3
+ -[GCOperation initOnQueue:withOptions:].cold.1
+ -[GCVersion initWithString:].cold.1
+ -[NSArray(GC) gc_arrayByRemovingObject:]
+ -[NSArray(GC) gc_requiredObjectAtIndex:ofClass:].cold.1
+ -[NSArray(GC) gc_requiredObjectAtIndex:ofClass:error:].cold.1
+ -[NSDictionary(GC) gc_dictionaryByRemovingObjectsForKeys:].cold.1
+ -[NSDictionary(GC) gc_objectForKey:ofClass:].cold.1
+ -[NSDictionary(GC) gc_objectForKey:ofClass:error:].cold.1
+ -[NSDictionary(GC) gc_requiredObjectForKey:ofClass:].cold.1
+ -[NSDictionary(GC) gc_requiredObjectForKey:ofClass:].cold.2
+ -[NSDictionary(GC) gc_requiredObjectForKey:ofClass:error:].cold.1
+ -[NSSet(GC) gc_member:]
+ -[NSValue(GC) gc_simdFloat4x4Value]
+ -[NSXPCConnection(GC) gc_peerBundleIdentifier]
+ -[NSXPCConnection(GC) gc_peerTeamIdentifier]
+ -[_GCAsyncFuture _initOnQueue:withOptions:block:].cold.1
+ -[_GCDeviceConfigurationEvaluator viableConfigurations:deviceOwners:].cold.9
+ -[_GCDeviceDBBundle initWithBundle:error:].cold.1
+ -[_GCDeviceDBBundleDevice initWithBundle:dictionary:error:].cold.1
+ -[_GCDeviceDBBundleDevice initWithBundle:dictionary:error:].cold.2
+ -[_GCDeviceDBBundleDevice initWithBundle:dictionary:error:].cold.3
+ -[_GCDeviceDBBundleDevice initWithBundle:dictionary:error:].cold.4
+ -[_GCDeviceDBBundleDevice initWithBundle:dictionary:error:].cold.5
+ -[_GCDeviceDBBundleDevice initWithBundle:dictionary:error:].cold.6
+ -[_GCDeviceDBPersonality initWithDictionary:error:].cold.1
+ -[_GCDeviceDBPersonality initWithDictionary:error:].cold.2
+ -[_GCDeviceDBPersonality initWithDictionary:error:].cold.3
+ -[_GCDeviceDBPersonality initWithURL:error:].cold.1
+ -[_GCDeviceDriverServiceConnection initWithDriverConnection:serviceVendor:].cold.1
+ -[_GCDeviceDriverServiceConnection initWithDriverConnection:serviceVendor:].cold.2
+ -[_GCDeviceOnDiskDB initWithBundles:].cold.1
+ -[_GCGenericPhysicalDevicePending initWithHIDService:manager:].cold.1
+ -[_GCGenericPhysicalDevicePending initWithHIDService:manager:].cold.2
+ -[_IOGCFastPathProxyClient handleMessage:].cold.1
+ -[_IOGCFastPathProxyClient handleMessage:].cold.2
+ -[__GCHIDSystemObservation DO_OBSERVER_CALLOUT_FOR_EVENT:FROM:]
+ -[__GCHIDSystemObservation NOTIFY_OBSERVER_SERVICES_CHANGED:ADDED_SERVICES:REMOVED_SERVICES:]
+ -[__GCHIDSystemObservation dealloc]
+ -[__GCHIDSystemObservation initWithEventHandler:]
+ -[__GCHIDSystemObservation initWithEventObserver:]
+ -[__GCHIDSystemObservation initWithServiceHandler:]
+ -[__GCHIDSystemObservation initWithServiceObserver:]
+ -[__GCHIDSystemObservation init]
+ GCC_except_table28
+ GCC_except_table37
+ GCHIDDeviceAttributesPredicateFromMatchingDictionary.cold.1
+ GCLookupService.cold.1
+ GCPrepareIOCFPlugInVtbl.cold.1
+ IOGCDeviceInterfacePrepareObjCVtbl.cold.1
+ IOGCFastPathClientInterfacePrepareObjCVtbl.cold.1
+ IOGCFastPathControlQueueInterfacePrepareObjCVtbl.cold.1
+ IOGCFastPathInputQueueCancel.cold.2
+ IOGCFastPathInputQueueInterfacePrepareObjCVtbl.cold.1
+ IOGCFastPathReaderInterfacePrepareObjCVtbl.cold.1
+ IOGCFastPathReaderReset.cold.1
+ IOGCFastPathSampleContainerInterfacePrepareObjCVtbl.cold.1
+ OBJC_IVAR_$_GCDevicePhysicalInputCapacitiveButtonElementDescription._touchedThreshold
+ OBJC_IVAR_$_GCDisposable._handler
+ OBJC_IVAR_$_GCGenericDeviceDriverModel._motion
+ OBJC_IVAR_$_GCGenericDeviceDriverModelBuilder._motion
+ OBJC_IVAR_$_GCGenericDeviceMotionEventDriverModel._accelerometerXExpression
+ OBJC_IVAR_$_GCGenericDeviceMotionEventDriverModel._accelerometerYExpression
+ OBJC_IVAR_$_GCGenericDeviceMotionEventDriverModel._accelerometerZExpression
+ OBJC_IVAR_$_GCGenericDeviceMotionEventDriverModel._gyroXExpression
+ OBJC_IVAR_$_GCGenericDeviceMotionEventDriverModel._gyroYExpression
+ OBJC_IVAR_$_GCGenericDeviceMotionEventDriverModel._gyroZExpression
+ OBJC_IVAR_$_GCGenericDeviceMotionEventDriverModelBuilder._accelerometerXExpression
+ OBJC_IVAR_$_GCGenericDeviceMotionEventDriverModelBuilder._accelerometerYExpression
+ OBJC_IVAR_$_GCGenericDeviceMotionEventDriverModelBuilder._accelerometerZExpression
+ OBJC_IVAR_$_GCGenericDeviceMotionEventDriverModelBuilder._gyroXExpression
+ OBJC_IVAR_$_GCGenericDeviceMotionEventDriverModelBuilder._gyroYExpression
+ OBJC_IVAR_$_GCGenericDeviceMotionEventDriverModelBuilder._gyroZExpression
+ OBJC_IVAR_$_GCGenericDevicePhysicalInputButtonModel._pressedThreshold
+ OBJC_IVAR_$_GCGenericDevicePhysicalInputButtonModel._sourcePressedValueExtendedEventFieldIndex
+ OBJC_IVAR_$_GCGenericDevicePhysicalInputButtonModel._sourceTouchedValueExtendedEventFieldIndex
+ OBJC_IVAR_$_GCGenericDevicePhysicalInputButtonModel._touchedThreshold
+ OBJC_IVAR_$_GCGenericDevicePhysicalInputButtonModelBuilder._pressedThreshold
+ OBJC_IVAR_$_GCGenericDevicePhysicalInputButtonModelBuilder._sourcePressedValueExtendedEventFieldIndex
+ OBJC_IVAR_$_GCGenericDevicePhysicalInputButtonModelBuilder._sourceTouchedValueExtendedEventFieldIndex
+ OBJC_IVAR_$_GCGenericDevicePhysicalInputButtonModelBuilder._touchedThreshold
+ OBJC_IVAR_$_GCHIDEventSystemClient._activated
+ OBJC_IVAR_$_GCHIDEventSystemClient._cancelHandler
+ OBJC_IVAR_$_GCHIDEventSystemClient._cancelled
+ OBJC_IVAR_$_GCHIDEventSystemClient._client
+ OBJC_IVAR_$_GCHIDEventSystemClient._eventObservations
+ OBJC_IVAR_$_GCHIDEventSystemClient._functions
+ OBJC_IVAR_$_GCHIDEventSystemClient._isEventMonitor
+ OBJC_IVAR_$_GCHIDEventSystemClient._queue
+ OBJC_IVAR_$_GCHIDEventSystemClient._serviceObservations
+ OBJC_IVAR_$_GCHIDEventSystemClient._services
+ OBJC_IVAR_$_GCHIDServiceInfo._functions
+ OBJC_IVAR_$___GCHIDSystemObservation._client
+ OBJC_IVAR_$___GCHIDSystemObservation._invalid
+ OBJC_IVAR_$___GCHIDSystemObservation._listEntry
+ OBJC_IVAR_$___GCHIDSystemObservation._observer
+ OBJC_IVAR_$___GCHIDSystemObservation._observerIsBlock
+ OBJC_IVAR_$___GCHIDSystemObservation._type
+ _CFDictionaryRemoveAllValues
+ _CopyBundleIdentifierAndTeamFromApplicationIdentifier
+ _HIDEventObservationListRemoveObserver
+ _HIDObservationListAdd
+ _IOGCDeviceGetPlugInInterface.cold.1
+ _IOGCDeviceGetPlugInInterface.cold.2
+ _IOHIDEventSystemClientActivate
+ _IOHIDEventSystemClientCancel
+ _IOHIDEventSystemClientCopyServiceForRegistryID
+ _IOHIDEventSystemClientCopyServices
+ _IOHIDEventSystemClientCreateWithType
+ _IOHIDEventSystemClientRegisterDeviceMatchingCallback
+ _IOHIDEventSystemClientRegisterEventCallback
+ _IOHIDEventSystemClientSetCancelHandler
+ _IOHIDEventSystemClientSetDispatchQueue
+ _IOHIDEventSystemClientSetMatchingMultiple
+ _IOHIDServiceClientRegisterRemovalCallback
+ _OBJC_CLASS_$_GCDisposable
+ _OBJC_CLASS_$_GCGenericDeviceMotionEventDriverModel
+ _OBJC_CLASS_$_GCGenericDeviceMotionEventDriverModelBuilder
+ _OBJC_CLASS_$_GCHIDEventSystemClient
+ _OBJC_CLASS_$_NSValue
+ _OBJC_CLASS_$___GCHIDSystemObservation
+ _OBJC_METACLASS_$_GCDisposable
+ _OBJC_METACLASS_$_GCGenericDeviceMotionEventDriverModel
+ _OBJC_METACLASS_$_GCGenericDeviceMotionEventDriverModelBuilder
+ _OBJC_METACLASS_$_GCHIDEventSystemClient
+ _OBJC_METACLASS_$___GCHIDSystemObservation
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _ZL28__immutablePlaceholderFuturev.cold.1
+ __104-[GCGenericDeviceDataAddExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke.107
+ __106-[GCGenericDeviceDataClampExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke.119
+ __108-[GCGenericDeviceDataBitTestExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke.158
+ __109-[GCGenericDeviceDataMultiplyExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke.107
+ __112-[GCGenericDeviceDataInterpolateExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke.161
+ __114-[GCGenericDeviceDataElementExistsExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke.120
+ __115-[GCGenericDeviceDataSDLHatFunctionExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke.179
+ __43-[_GCGenericDeviceManager claimHIDService:]_block_invoke.cold.1
+ __64-[_GCGenericDeviceManager acceptFilterConnection:forHIDService:]_block_invoke.cold.3
+ __72-[GCHIDEventSystemClient registerServicesChangedHandler:notifyExisting:]_block_invoke.cold.1
+ __73-[GCHIDEventSystemClient registerServicesChangedObserver:notifyExisting:]_block_invoke.cold.1
+ __75-[GCHIDEventSystemClient unregisterServicesChangedObserver:notifyExisting:]_block_invoke.cold.1
+ __GCHIDDeviceAttributesPredicateFromMatchingDictionary_block_invoke.cold.1
+ __GCHIDDeviceAttributesPredicateFromMatchingDictionary_block_invoke.cold.2
+ __GCHIDDeviceAttributesPredicateFromMatchingDictionary_block_invoke.cold.3
+ __GCHIDDeviceAttributesPredicateFromMatchingDictionary_block_invoke.cold.4
+ __GCHIDDeviceAttributesPredicateFromMatchingDictionary_block_invoke.cold.5
+ __MergedGlobals
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSBundle_$_GC
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSError_$_GCIPCErrorDomain
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSException_$_GC
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSValue_$_GC
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_HIDDevice_$_Snapshot
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSArray_$_GC
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDictionary_$_GC
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSException_$_GC
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSMutableArray_$_GC
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSMutableSet_$_GC
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSSet_$_GC
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSString_$_GC
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSValue_$_GC
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSXPCConnection_$_GC
+ __OBJC_$_CATEGORY_NSValue_$_GC
+ __OBJC_$_CATEGORY_NSXPCConnection_$_GC
+ __OBJC_$_CLASS_METHODS_GCDisposable
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDataAddExpressionModel
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDataAddExpressionModelBuilder
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDataBitTestExpressionModel
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDataBitTestExpressionModelBuilder
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDataClampExpressionModel
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDataClampExpressionModelBuilder
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDataConstantExpressionModel
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDataConstantExpressionModelBuilder
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDataElementExistsExpressionModelBuilder
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDataInputElementAttributeExpressionModelBuilder
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDataInputElementValueExpressionModelBuilder
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDataInterpolateExpressionModel
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDataInterpolateExpressionModelBuilder
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDataMultiplyExpressionModel
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDataMultiplyExpressionModelBuilder
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDataProcessorExpressionModelBuilder
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDataRumbleMotorValueExpressionModelBuilder
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceDataSDLHatFunctionExpressionModelBuilder
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceModelBuilder
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceMotionEventDriverModel(Serialization)
+ __OBJC_$_CLASS_METHODS_GCGenericDeviceMotionEventDriverModelBuilder
+ __OBJC_$_CLASS_METHODS_GCGenericDevicePhysicalInputButtonModelBuilder
+ __OBJC_$_CLASS_METHODS_GCGenericDevicePhysicalInputDpadModelBuilder
+ __OBJC_$_CLASS_METHODS_GCGenericDevicePhysicalInputElementModelBuilder
+ __OBJC_$_CLASS_PROP_LIST_GCGenericDeviceMotionEventDriverModel
+ __OBJC_$_CLASS_PROP_LIST_GCGenericDeviceMotionEventDriverModelBuilder
+ __OBJC_$_INSTANCE_METHODS_GCDisposable
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceDataElementExistsExpressionModel(Compilation)
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceDataInputElementAttributeExpressionModel(Compilation)
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceDataInputElementValueExpressionModel(Compilation)
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceDataSDLHatFunctionExpressionModel(Compilation)
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceDriverModel
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceDriverPropertiesModel
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceDriverPropertyModel
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceElementModel
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceInputEventDriverModel
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceInputGamepadEventFieldModel
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceModel
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceMotionEventDriverModel
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceMotionEventDriverModelBuilder
+ __OBJC_$_INSTANCE_METHODS_GCGenericDevicePhysicalInputElementModel
+ __OBJC_$_INSTANCE_METHODS_GCGenericDevicePhysicalInputModel
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceRumbleActuatorModel
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceRumbleModel
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceRumbleOutputFieldModel
+ __OBJC_$_INSTANCE_METHODS_GCGenericDeviceRumbleOutputModel
+ __OBJC_$_INSTANCE_METHODS_GCHIDEventSystemClient
+ __OBJC_$_INSTANCE_METHODS___GCHIDSystemObservation
+ __OBJC_$_INSTANCE_VARIABLES_GCDisposable
+ __OBJC_$_INSTANCE_VARIABLES_GCGenericDeviceMotionEventDriverModel
+ __OBJC_$_INSTANCE_VARIABLES_GCGenericDeviceMotionEventDriverModelBuilder
+ __OBJC_$_INSTANCE_VARIABLES_GCHIDEventSystemClient
+ __OBJC_$_INSTANCE_VARIABLES___GCHIDSystemObservation
+ __OBJC_$_PROP_LIST_GCGenericDeviceMotionEventDriverModel
+ __OBJC_$_PROP_LIST_GCGenericDeviceMotionEventDriverModelBuilder
+ __OBJC_$_PROP_LIST_GCHIDEventSystemClient
+ __OBJC_$_PROP_LIST_GCHIDSystemEventProviding
+ __OBJC_$_PROP_LIST_GCHIDSystemServiceInfo
+ __OBJC_$_PROP_LIST_GCHIDSystemServiceProviding
+ __OBJC_$_PROP_LIST_NSUserDefaults_$_GC
+ __OBJC_$_PROP_LIST_NSValue_$_GC
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCHIDSystemEventProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCHIDSystemServiceInfo
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCHIDSystemServiceProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GCHIDSystemEventProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GCHIDSystemServiceInfo
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GCHIDSystemServiceProviding
+ __OBJC_$_PROTOCOL_REFS_GCHIDSystemEventProviding
+ __OBJC_$_PROTOCOL_REFS_GCHIDSystemServiceInfo
+ __OBJC_$_PROTOCOL_REFS_GCHIDSystemServiceProviding
+ __OBJC_CATEGORY_PROTOCOLS_$_NSUserDefaults_$_GC
+ __OBJC_CLASS_PROTOCOLS_$_GCGenericDeviceMotionEventDriverModel
+ __OBJC_CLASS_PROTOCOLS_$_GCHIDEventSystemClient
+ __OBJC_CLASS_PROTOCOLS_$_HIDElement(Snapshot|GC)
+ __OBJC_CLASS_RO_$_GCDisposable
+ __OBJC_CLASS_RO_$_GCGenericDeviceMotionEventDriverModel
+ __OBJC_CLASS_RO_$_GCGenericDeviceMotionEventDriverModelBuilder
+ __OBJC_CLASS_RO_$_GCHIDEventSystemClient
+ __OBJC_CLASS_RO_$___GCHIDSystemObservation
+ __OBJC_LABEL_PROTOCOL_$_GCHIDSystemEventProviding
+ __OBJC_LABEL_PROTOCOL_$_GCHIDSystemServiceInfo
+ __OBJC_LABEL_PROTOCOL_$_GCHIDSystemServiceProviding
+ __OBJC_METACLASS_RO_$_GCDisposable
+ __OBJC_METACLASS_RO_$_GCGenericDeviceMotionEventDriverModel
+ __OBJC_METACLASS_RO_$_GCGenericDeviceMotionEventDriverModelBuilder
+ __OBJC_METACLASS_RO_$_GCHIDEventSystemClient
+ __OBJC_METACLASS_RO_$___GCHIDSystemObservation
+ __OBJC_PROTOCOL_$_GCHIDSystemEventProviding
+ __OBJC_PROTOCOL_$_GCHIDSystemServiceInfo
+ __OBJC_PROTOCOL_$_GCHIDSystemServiceProviding
+ __OBJC_PROTOCOL_REFERENCE_$_GCHIDSystemEventProviding
+ __ServiceMatchedCallback.cold.1
+ __ServiceRemovedCallback.cold.1
+ ___101-[GCGenericDeviceDataInputElementValueExpressionModel(Compilation) buildExpressionWithContext:error:]_block_invoke
+ ___104-[GCGenericDeviceDataAddExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke
+ ___104-[GCGenericDeviceDataAddExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_2
+ ___104-[GCGenericDeviceDataAddExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_3
+ ___105-[GCGenericDeviceDataInputElementAttributeExpressionModel(Compilation) buildExpressionWithContext:error:]_block_invoke
+ ___106-[GCGenericDeviceDataClampExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke
+ ___106-[GCGenericDeviceDataClampExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_2
+ ___106-[GCGenericDeviceDataClampExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_3
+ ___106-[GCGenericDeviceDataClampExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_4
+ ___106-[GCGenericDeviceDataClampExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_5
+ ___108-[GCGenericDeviceDataBitTestExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke
+ ___108-[GCGenericDeviceDataBitTestExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_2
+ ___108-[GCGenericDeviceDataBitTestExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_3
+ ___108-[GCGenericDeviceDataBitTestExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_4
+ ___108-[GCGenericDeviceDataBitTestExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_5
+ ___108-[GCGenericDeviceDataBitTestExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_6
+ ___108-[GCGenericDeviceDataBitTestExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_7
+ ___109-[GCGenericDeviceDataMultiplyExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke
+ ___109-[GCGenericDeviceDataMultiplyExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_2
+ ___109-[GCGenericDeviceDataMultiplyExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_3
+ ___112-[GCGenericDeviceDataInterpolateExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke
+ ___112-[GCGenericDeviceDataInterpolateExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_2
+ ___112-[GCGenericDeviceDataInterpolateExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_3
+ ___112-[GCGenericDeviceDataInterpolateExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_4
+ ___112-[GCGenericDeviceDataInterpolateExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_5
+ ___112-[GCGenericDeviceDataInterpolateExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_6
+ ___112-[GCGenericDeviceDataInterpolateExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_7
+ ___112-[GCGenericDeviceDataInterpolateExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_8
+ ___112-[GCGenericDeviceDataInterpolateExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_9
+ ___114-[GCGenericDeviceDataElementExistsExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke
+ ___114-[GCGenericDeviceDataElementExistsExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_2
+ ___114-[GCGenericDeviceDataElementExistsExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_3
+ ___115-[GCGenericDeviceDataSDLHatFunctionExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke
+ ___115-[GCGenericDeviceDataSDLHatFunctionExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_10
+ ___115-[GCGenericDeviceDataSDLHatFunctionExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_11
+ ___115-[GCGenericDeviceDataSDLHatFunctionExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_2
+ ___115-[GCGenericDeviceDataSDLHatFunctionExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_3
+ ___115-[GCGenericDeviceDataSDLHatFunctionExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_4
+ ___115-[GCGenericDeviceDataSDLHatFunctionExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_5
+ ___115-[GCGenericDeviceDataSDLHatFunctionExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_6
+ ___115-[GCGenericDeviceDataSDLHatFunctionExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_7
+ ___115-[GCGenericDeviceDataSDLHatFunctionExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_8
+ ___115-[GCGenericDeviceDataSDLHatFunctionExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke_9
+ ___118-[GCGenericDeviceDataInputElementValueExpressionModel(Compilation) buildReactiveExpressionWithContext:consumer:error:]_block_invoke
+ ___34-[GCHIDEventSystemClient activate]_block_invoke
+ ___46-[GCHIDEventSystemClient setMatchingMultiple:]_block_invoke
+ ___72-[GCHIDEventSystemClient registerServicesChangedHandler:notifyExisting:]_block_invoke
+ ___73-[GCHIDEventSystemClient registerServicesChangedObserver:notifyExisting:]_block_invoke
+ ___75-[GCHIDEventSystemClient unregisterServicesChangedObserver:notifyExisting:]_block_invoke
+ ___87-[GCGenericDeviceDataAddExpressionModel(Compilation) buildExpressionWithContext:error:]_block_invoke
+ ___89-[GCGenericDeviceDataClampExpressionModel(Compilation) buildExpressionWithContext:error:]_block_invoke
+ ___91-[GCGenericDeviceDataBitTestExpressionModel(Compilation) buildExpressionWithContext:error:]_block_invoke
+ ___92-[GCGenericDeviceDataConstantExpressionModel(Compilation) buildExpressionWithContext:error:]_block_invoke
+ ___92-[GCGenericDeviceDataMultiplyExpressionModel(Compilation) buildExpressionWithContext:error:]_block_invoke
+ ___95-[GCGenericDeviceDataInterpolateExpressionModel(Compilation) buildExpressionWithContext:error:]_block_invoke
+ ___97-[GCGenericDeviceDataElementExistsExpressionModel(Compilation) buildExpressionWithContext:error:]_block_invoke
+ ___98-[GCGenericDeviceDataSDLHatFunctionExpressionModel(Compilation) buildExpressionWithContext:error:]_block_invoke
+ ___EventCallback
+ ___ServiceMatchedCallback
+ ___ServiceRemovedCallback
+ ____EventCallback_block_invoke.cold.1
+ _____EventCallback_block_invoke
+ ___block_descriptor_40_e8_32bs_e48_v32?0"GCHIDInputElement"8^{__IOHIDValue=}16d24l
+ ___block_descriptor_40_e8_32o_e29_"GCHIDServiceInfo"24?08Q16l
+ ___block_descriptor_48_e8_32o40o_e5_v8?0l
+ ___block_descriptor_48_e8_32s40s_e5_d8?0l
+ ___block_descriptor_49_e8_32bs40bs_e5_d8?0l
+ ___block_descriptor_56_e8_32bs40r48r_e8_v16?0d8l
+ ___block_descriptor_56_e8_32o_e5_v8?0l
+ ___block_descriptor_57_e8_32bs40r48r_e8_v16?0d8l
+ ___block_descriptor_64_e8_32o40r_e23_"GCHIDServiceInfo"8?0l
+ ___block_descriptor_65_e8_32bs40bs48bs56bs_e5_d8?0l
+ ___block_descriptor_66_e8_32bs40r48r56r_e8_v16?0d8l
+ ___block_descriptor_73_e8_32bs40r48r56r64r_e8_v16?0d8l
+ ___block_descriptor_80_e8_32bs40bs48bs56bs64bs72bs_e5_d8?0l
+ ___block_descriptor_80_e8_32bs40r48r56r64r72r_e8_v16?0d8l
+ ___block_descriptor_88_e8_32bs40r48r56r64r72r80r_e8_v16?0d8l
+ ___copy_helper_block_e8_32b40b48b56b64b72b
+ ___copy_helper_block_e8_32b40r48r
+ ___copy_helper_block_e8_32b40r48r56r
+ ___copy_helper_block_e8_32b40r48r56r64r
+ ___copy_helper_block_e8_32b40r48r56r64r72r
+ ___copy_helper_block_e8_32b40r48r56r64r72r80r
+ ___copy_helper_block_e8_32o40o
+ ___copy_helper_block_e8_32o40r
+ ___destroy_helper_block_e8_32o40o
+ ___destroy_helper_block_e8_32o40r
+ ___destroy_helper_block_e8_32s40r48r
+ ___destroy_helper_block_e8_32s40r48r56r
+ ___destroy_helper_block_e8_32s40r48r56r64r
+ ___destroy_helper_block_e8_32s40r48r56r64r72r
+ ___destroy_helper_block_e8_32s40r48r56r64r72r80r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s
+ _gc_log_configuration.cold.1
+ _gc_log_device.cold.1
+ _gc_log_device_configuration.cold.1
+ _gc_log_devicedb.cold.1
+ _gc_log_generic_device.cold.1
+ _gc_log_hid.cold.1
+ _gc_log_hid_input.cold.1
+ _gc_log_iokit.cold.1
+ _gc_log_ipc.cold.1
+ _gc_log_localizedstring.cold.1
+ _gc_log_runtime_issue.cold.1
+ _gc_log_user_monitor.cold.1
+ _objc_msgSend$accelerometerXExpression
+ _objc_msgSend$accelerometerYExpression
+ _objc_msgSend$accelerometerZExpression
+ _objc_msgSend$anyObject
+ _objc_msgSend$buildExpression:error:
+ _objc_msgSend$buildExpressionWithContext:error:
+ _objc_msgSend$buildReactiveExpression:consumer:error:
+ _objc_msgSend$buildReactiveExpressionWithContext:consumer:error:
+ _objc_msgSend$elementWithIdentifier:
+ _objc_msgSend$gc_member:
+ _objc_msgSend$gc_peerBundleIdentifier
+ _objc_msgSend$getValue:size:
+ _objc_msgSend$gyroXExpression
+ _objc_msgSend$gyroYExpression
+ _objc_msgSend$gyroZExpression
+ _objc_msgSend$handleHIDEvent:from:
+ _objc_msgSend$initWithObjects:
+ _objc_msgSend$initWithQueue:type:attributes:functions:
+ _objc_msgSend$initWithService:queue:functions:
+ _objc_msgSend$inputElementWithIdentifier:
+ _objc_msgSend$motion
+ _objc_msgSend$pressedThreshold
+ _objc_msgSend$registerScaled:valueChangedHandler:
+ _objc_msgSend$scaledValue:
+ _objc_msgSend$services
+ _objc_msgSend$servicesDidChange:withAddedServices:removedServices:
+ _objc_msgSend$setAccelerometerXExpression:
+ _objc_msgSend$setAccelerometerYExpression:
+ _objc_msgSend$setAccelerometerZExpression:
+ _objc_msgSend$setGyroXExpression:
+ _objc_msgSend$setGyroYExpression:
+ _objc_msgSend$setGyroZExpression:
+ _objc_msgSend$setMatchingMultiple:
+ _objc_msgSend$setMotion:
+ _objc_msgSend$setPressedThreshold:
+ _objc_msgSend$setSourcePressedValueExtendedEventFieldIndex:
+ _objc_msgSend$setSourceTouchedValueExtendedEventFieldIndex:
+ _objc_msgSend$setTouchedThreshold:
+ _objc_msgSend$sourcePressedValueExtendedEventFieldIndex
+ _objc_msgSend$sourceTouchedValueExtendedEventFieldIndex
+ _objc_msgSend$touchedThreshold
+ _objc_msgSend$valueForElementKey:
+ _objc_msgSend$valueWithBytes:objCType:
+ _objc_storeWeakOrNil
+ gcfLocalizedStringCache.cold.1
- -[GCGenericDeviceDataAddExpressionModel(Compilation) _buildPullExpressionWithOverrideBuilder:error:]
- -[GCGenericDeviceDataBitTestExpressionModel(Compilation) _buildPullExpressionWithOverrideBuilder:error:]
- -[GCGenericDeviceDataClampExpressionModel(Compilation) _buildPullExpressionWithOverrideBuilder:error:]
- -[GCGenericDeviceDataConstantExpressionModel(Compilation) _buildPullExpressionWithOverrideBuilder:error:]
- -[GCGenericDeviceDataInterpolateExpressionModel(Compilation) _buildPullExpressionWithOverrideBuilder:error:]
- -[GCGenericDeviceDataMultiplyExpressionModel(Compilation) _buildPullExpressionWithOverrideBuilder:error:]
- -[GCGenericDeviceDataProcessorExpressionModel(Compilation) _buildPullExpressionWithOverrideBuilder:error:]
- -[GCGenericDeviceDataProcessorExpressionModel(Compilation) buildPullExpressionWithOverrideBuilder:error:]
- -[GCGenericDevicePhysicalInputButtonModel sourceExtendedEventFieldIndex]
- -[GCGenericDevicePhysicalInputButtonModelBuilder setSourceExtendedEventFieldIndex:]
- -[GCGenericDevicePhysicalInputButtonModelBuilder sourceExtendedEventFieldIndex]
- -[IOGCFastPathProxyConnection _initWithService:withProxyService:error:].cold.1
- -[IOGCFastPathProxyConnection _initWithService:withProxyService:error:].cold.2
- -[NSXPCConnection gc_peerBundleIdentifier]
- -[_GCConfigurationBundleLocator _onqueue_asset_updateBundles].cold.1
- -[_GCConfigurationBundleLocator _onqueue_asset_updateBundles].cold.2
- -[_GCConfigurationBundleLocator _onqueue_filesystem_updateBundles].cold.1
- -[_GCConfigurationBundleLocator _onqueue_filesystem_updateBundles].cold.2
- -[_GCDisposable .cxx_destruct]
- -[_GCDisposable dealloc]
- -[_GCDisposable initWithCleanupHandler:]
- -[_GCFLocalizedString initWithKey:sourceBundle:table:locale:].cold.1
- -[_GCGenericDeviceManager _onqueue_relinquishHIDService:].cold.1
- -[_GCGenericDeviceManager _onqueue_relinquishHIDService:].cold.2
- IOGCDeviceCreate.cold.1
- IOGCDeviceCreate.cold.2
- IOGCFastPathClientCreate.cold.1
- IOGCFastPathClientCreate.cold.2
- IOGCFastPathClientCreateWithPlugInInterface.cold.1
- IOGCFastPathClientCreateWithPlugInInterface.cold.2
- IOGCFastPathClientCreateWithPlugInInterface.cold.3
- IOGCFastPathClientCreateWithPlugInInterface.cold.4
- IOGCFastPathInputQueueCreateWithOptions.cold.1
- IOGCFastPathInputQueueCreateWithOptions.cold.2
- IOGCFastPathInputQueueCreateWithOptions.cold.3
- IOGCFastPathReaderCreate.cold.1
- IOGCFastPathReaderCreate.cold.2
- IOGCFastPathReaderCreate.cold.3
- OBJC_IVAR_$_GCGenericDevicePhysicalInputButtonModel._sourceExtendedEventFieldIndex
- OBJC_IVAR_$_GCGenericDevicePhysicalInputButtonModelBuilder._sourceExtendedEventFieldIndex
- OBJC_IVAR_$__GCDisposable._handler
- _OBJC_CLASS_$__GCDisposable
- _OBJC_METACLASS_$__GCDisposable
- _RoyaReplayInputQueueVtable
- _RoyaReplayInputSampleContainerVtable
- __IOHIDQueueInputElementValueCallback.cold.1
- __OBJC_$_CLASS_METHODS_GCGenericDeviceDataAddExpressionModel(Compilation)
- __OBJC_$_CLASS_METHODS_GCGenericDeviceDataAddExpressionModelBuilder(Serialization)
- __OBJC_$_CLASS_METHODS_GCGenericDeviceDataBitTestExpressionModel(Compilation)
- __OBJC_$_CLASS_METHODS_GCGenericDeviceDataBitTestExpressionModelBuilder(Serialization)
- __OBJC_$_CLASS_METHODS_GCGenericDeviceDataClampExpressionModel(Compilation)
- __OBJC_$_CLASS_METHODS_GCGenericDeviceDataClampExpressionModelBuilder(Serialization)
- __OBJC_$_CLASS_METHODS_GCGenericDeviceDataConstantExpressionModel(Compilation)
- __OBJC_$_CLASS_METHODS_GCGenericDeviceDataConstantExpressionModelBuilder(Serialization)
- __OBJC_$_CLASS_METHODS_GCGenericDeviceDataElementExistsExpressionModelBuilder(Serialization)
- __OBJC_$_CLASS_METHODS_GCGenericDeviceDataInputElementAttributeExpressionModelBuilder(Serialization)
- __OBJC_$_CLASS_METHODS_GCGenericDeviceDataInputElementValueExpressionModelBuilder(Serialization)
- __OBJC_$_CLASS_METHODS_GCGenericDeviceDataInterpolateExpressionModel(Compilation)
- __OBJC_$_CLASS_METHODS_GCGenericDeviceDataInterpolateExpressionModelBuilder(Serialization)
- __OBJC_$_CLASS_METHODS_GCGenericDeviceDataMultiplyExpressionModel(Compilation)
- __OBJC_$_CLASS_METHODS_GCGenericDeviceDataMultiplyExpressionModelBuilder(Serialization)
- __OBJC_$_CLASS_METHODS_GCGenericDeviceDataProcessorExpressionModelBuilder(Serialization)
- __OBJC_$_CLASS_METHODS_GCGenericDeviceDataRumbleMotorValueExpressionModelBuilder(Serialization)
- __OBJC_$_CLASS_METHODS_GCGenericDeviceDataSDLHatFunctionExpressionModelBuilder(Serialization)
- __OBJC_$_CLASS_METHODS_GCGenericDeviceModelBuilder(Serialization)
- __OBJC_$_CLASS_METHODS_GCGenericDevicePhysicalInputButtonModelBuilder(Serialization)
- __OBJC_$_CLASS_METHODS_GCGenericDevicePhysicalInputDpadModelBuilder(Serialization)
- __OBJC_$_CLASS_METHODS_GCGenericDevicePhysicalInputElementModelBuilder(Serialization)
- __OBJC_$_CLASS_METHODS_NSBundle(GC)
- __OBJC_$_CLASS_METHODS_NSError(GCIPCErrorDomain|GC)
- __OBJC_$_CLASS_METHODS_NSException(GC)
- __OBJC_$_INSTANCE_METHODS_GCGenericDeviceDataElementExistsExpressionModel
- __OBJC_$_INSTANCE_METHODS_GCGenericDeviceDataInputElementAttributeExpressionModel
- __OBJC_$_INSTANCE_METHODS_GCGenericDeviceDataInputElementValueExpressionModel
- __OBJC_$_INSTANCE_METHODS_GCGenericDeviceDataSDLHatFunctionExpressionModel
- __OBJC_$_INSTANCE_METHODS_GCGenericDeviceDriverModel(Serialization)
- __OBJC_$_INSTANCE_METHODS_GCGenericDeviceDriverPropertiesModel(Serialization)
- __OBJC_$_INSTANCE_METHODS_GCGenericDeviceDriverPropertyModel(Serialization)
- __OBJC_$_INSTANCE_METHODS_GCGenericDeviceElementModel(Serialization)
- __OBJC_$_INSTANCE_METHODS_GCGenericDeviceInputEventDriverModel(Serialization)
- __OBJC_$_INSTANCE_METHODS_GCGenericDeviceInputGamepadEventFieldModel(Serialization)
- __OBJC_$_INSTANCE_METHODS_GCGenericDeviceModel(Serialization)
- __OBJC_$_INSTANCE_METHODS_GCGenericDevicePhysicalInputElementModel(Serialization)
- __OBJC_$_INSTANCE_METHODS_GCGenericDevicePhysicalInputModel(Serialization)
- __OBJC_$_INSTANCE_METHODS_GCGenericDeviceRumbleActuatorModel(Serialization)
- __OBJC_$_INSTANCE_METHODS_GCGenericDeviceRumbleModel(Serialization)
- __OBJC_$_INSTANCE_METHODS_GCGenericDeviceRumbleOutputFieldModel(Serialization)
- __OBJC_$_INSTANCE_METHODS_GCGenericDeviceRumbleOutputModel(Serialization)
- __OBJC_$_INSTANCE_METHODS_HIDDevice(Snapshot)
- __OBJC_$_INSTANCE_METHODS_NSArray(GC)
- __OBJC_$_INSTANCE_METHODS_NSDictionary(GC)
- __OBJC_$_INSTANCE_METHODS_NSException(GC)
- __OBJC_$_INSTANCE_METHODS_NSMutableArray(GC)
- __OBJC_$_INSTANCE_METHODS_NSMutableSet(GC)
- __OBJC_$_INSTANCE_METHODS_NSSet(GC)
- __OBJC_$_INSTANCE_METHODS_NSString(GC)
- __OBJC_$_INSTANCE_METHODS__GCDisposable
- __OBJC_$_INSTANCE_VARIABLES__GCDisposable
- __OBJC_CLASS_PROTOCOLS_$_HIDElement(GC)
- __OBJC_CLASS_PROTOCOLS_$_NSUserDefaults(GC)
- __OBJC_CLASS_RO_$__GCDisposable
- __OBJC_METACLASS_RO_$__GCDisposable
- ___100-[GCGenericDeviceDataAddExpressionModel(Compilation) _buildPullExpressionWithOverrideBuilder:error:]_block_invoke
- ___102-[GCGenericDeviceDataClampExpressionModel(Compilation) _buildPullExpressionWithOverrideBuilder:error:]_block_invoke
- ___104-[GCGenericDeviceDataBitTestExpressionModel(Compilation) _buildPullExpressionWithOverrideBuilder:error:]_block_invoke
- ___105-[GCGenericDeviceDataConstantExpressionModel(Compilation) _buildPullExpressionWithOverrideBuilder:error:]_block_invoke
- ___105-[GCGenericDeviceDataMultiplyExpressionModel(Compilation) _buildPullExpressionWithOverrideBuilder:error:]_block_invoke
- ___108-[GCGenericDeviceDataInterpolateExpressionModel(Compilation) _buildPullExpressionWithOverrideBuilder:error:]_block_invoke
- ___block_descriptor_64_e8_32bs40bs48bs56bs_e5_d8?0l
- __unnamed_array_storage
- _gc_log_localizedstring.Log
- _gc_log_localizedstring.onceToken
- _objc_msgSend$_buildPullExpressionWithOverrideBuilder:error:
- _objc_msgSend$buildPullExpressionWithOverrideBuilder:error:
- _objc_msgSend$setSourceExtendedEventFieldIndex:
- _objc_msgSend$sourceExtendedEventFieldIndex
- _unnamed_array_storage.131
- _unnamed_array_storage.23
- _unnamed_array_storage.27
CStrings:
+ "#WARNING Duplicate HID Service Matched: serviceID='%#010llx'"
+ "#WARNING Un-tracked HID Service Removed: serviceID='%#010llx'"
+ "(?=\"object\"@\"handler\"@?)"
+ "*** Client is not configured to receive events.  The callback will never be invoked."
+ "*** This property may not be mutated after client activation."
+ "<%@ %p> {\n\t accelerometerXExpression = %@\n\t accelerometerYExpression = %@\n\t accelerometerZExpression = %@\n\t gyroXExpression = %@\n\t gyroYExpression = %@\n\t gyroZExpression = %@\n}"
+ "<%@ %p> {\n\t elements = %@\n\t properties = %@\n\t input = %@\n\t motion = %@\n\t rumble = %@\n}"
+ "@\"<GCHIDSystemServiceInfo>\"24@0:8Q16"
+ "@\"GCGenericDeviceMotionEventDriverModel\""
+ "@\"GCHIDEventSystemClient\""
+ "@\"GCHIDServiceInfo\"24@?0@8Q16"
+ "@\"GCHIDServiceInfo\"8@?0"
+ "@\"NSNumber\"24@0:8@\"NSString\"16"
+ "@\"NSObject<OS_dispatch_queue>\"16@0:8"
+ "@\"NSSet\"16@0:8"
+ "@24@0:8@?<v@?^{__IOHIDEvent=}@?<@\"<GCHIDSystemServiceInfo>\"@?>>16"
+ "@24@0:8Q16"
+ "@28@0:8@?16B24"
+ "@28@0:8@?<v@?@\"NSSet\"@\"NSArray\"@\"NSArray\">16B24"
+ "@32@0:8@\"NSString\"16#24"
+ "@36@0:8@16i24@28"
+ "@40@0:8@16@?24o^@32"
+ "@40@0:8^{__IOHIDServiceClient=}16@24r^{GCHIDServiceClientFunctions=^?^?^?}32"
+ "@44@0:8@16i24@28@36"
+ "@44@0:8@16i24@28r^{GCHIDEventSystemClientFunctions=^?^?^?^?^?^?^?^?^?^?^{GCHIDServiceClientFunctions}}36"
+ "@80@0:8{?=[4]}16"
+ "@?32@0:8@16o^@24"
+ "AccelerometerXExpression"
+ "AccelerometerYExpression"
+ "AccelerometerZExpression"
+ "Context is tot tracking any elements."
+ "Context is tot tracking any input elements."
+ "Element with identifier '%@' does not have a '%@' attribute."
+ "Element with identifier '%@' has an '%@' attribute, but it's not a number."
+ "Failed to build expression closure for '%@'."
+ "GCDisposable"
+ "GCGenericDeviceMotionEventDriverModel"
+ "GCGenericDeviceMotionEventDriverModelBuilder"
+ "GCHIDEventSystemClient"
+ "GCHIDEventSystemClient.m"
+ "GCHIDSystemEventProviding"
+ "GCHIDSystemServiceInfo"
+ "GCHIDSystemServiceProviding"
+ "GyroXExpression"
+ "GyroYExpression"
+ "GyroZExpression"
+ "HID Service Matched: serviceID='%#010llx'"
+ "HID Service Removed: serviceID='%#010llx'"
+ "Invalid 'Element Exists' expression."
+ "Invalid 'Input Element Attribute' expression."
+ "Invalid 'Input Element Value' expression."
+ "Motion"
+ "Motion Event Driver"
+ "Not tracking any element with identifier %@"
+ "PressedValueThreshold"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",C,N,V_accelerometerXExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",C,N,V_accelerometerYExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",C,N,V_accelerometerZExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",C,N,V_gyroXExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",C,N,V_gyroYExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",C,N,V_gyroZExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",R,C,V_accelerometerXExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",R,C,V_accelerometerYExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",R,C,V_accelerometerZExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",R,C,V_gyroXExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",R,C,V_gyroYExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",R,C,V_gyroZExpression"
+ "T@\"GCGenericDeviceMotionEventDriverModel\",C,N,V_motion"
+ "T@\"GCGenericDeviceMotionEventDriverModel\",R,C,V_motion"
+ "T@\"NSObject<OS_dispatch_queue>\",R"
+ "T@\"NSSet\",R"
+ "T@\"NSSet\",R,V_services"
+ "Td,N,V_pressedThreshold"
+ "Td,N,V_touchedThreshold"
+ "Td,R,V_pressedThreshold"
+ "Td,R,V_touchedThreshold"
+ "Tf,N,V_touchedThreshold"
+ "The 'falseExpression' sub-expression failed to build."
+ "The 'inputExpression' sub-expression failed to build."
+ "The 'inputMaxExpression' sub-expression failed to build."
+ "The 'inputMinExpression' sub-expression failed to build."
+ "The 'leftExpression' sub-expression failed to build."
+ "The 'maskExpression' sub-expression failed to build."
+ "The 'maxExpression' sub-expression failed to build."
+ "The 'minExpression' sub-expression failed to build."
+ "The 'outputMaxExpression' sub-expression failed to build."
+ "The 'outputMinExpression' sub-expression failed to build."
+ "The 'rightExpression' sub-expression failed to build."
+ "The 'trueExpression' sub-expression failed to build."
+ "TouchedValueSource"
+ "TouchedValueThreshold"
+ "Tq,N,V_sourcePressedValueExtendedEventFieldIndex"
+ "Tq,N,V_sourceTouchedValueExtendedEventFieldIndex"
+ "Tq,R,V_sourcePressedValueExtendedEventFieldIndex"
+ "Tq,R,V_sourceTouchedValueExtendedEventFieldIndex"
+ "T{?=[4]},R"
+ "Unsupported valueType."
+ "[HID Event System Client] Activate"
+ "[HID Event System Client] Cancelled"
+ "[HID Event System Client] Notify HID Service Matched"
+ "[HID Event System Client] Notify HID Service Removed"
+ "^{__IOHIDEventSystemClient=}"
+ "__GCHIDSystemObservation"
+ "_accelerometerXExpression"
+ "_accelerometerYExpression"
+ "_accelerometerZExpression"
+ "_client"
+ "_eventObservations"
+ "_functions"
+ "_gyroXExpression"
+ "_gyroYExpression"
+ "_gyroZExpression"
+ "_isEventMonitor"
+ "_listEntry"
+ "_motion"
+ "_observer"
+ "_observerIsBlock"
+ "_serviceObservations"
+ "_services"
+ "_sourcePressedValueExtendedEventFieldIndex"
+ "_sourceTouchedValueExtendedEventFieldIndex"
+ "_touchedThreshold"
+ "accelerometerXExpression"
+ "accelerometerYExpression"
+ "accelerometerZExpression"
+ "anyObject"
+ "buildExpression:error:"
+ "buildExpressionWithContext:error:"
+ "buildReactiveExpression:consumer:error:"
+ "buildReactiveExpressionWithContext:consumer:error:"
+ "elementWithIdentifier:"
+ "gc_arrayByRemovingObject:"
+ "gc_member:"
+ "gc_peerBundleIdentifier"
+ "gc_peerTeamIdentifier"
+ "gc_simdFloat4x4Value"
+ "gc_valueWithSimdFloat4x4:"
+ "getValue:size:"
+ "gyroXExpression"
+ "gyroYExpression"
+ "gyroZExpression"
+ "handleHIDEvent:from:"
+ "initWithKey:sourceBundle:table:"
+ "initWithObjects:"
+ "initWithQueue:type:attributes:"
+ "initWithQueue:type:attributes:environment:"
+ "initWithQueue:type:attributes:functions:"
+ "initWithService:queue:functions:"
+ "inputElementWithIdentifier:"
+ "motion"
+ "r^{GCHIDEventSystemClientFunctions=^?^?^?^?^?^?^?^?^?^?^{GCHIDServiceClientFunctions}}"
+ "r^{GCHIDServiceClientFunctions=^?^?^?}"
+ "registerEventHandler:"
+ "registerEventObserver:"
+ "registerServicesChangedHandler:notifyExisting:"
+ "registerServicesChangedObserver:notifyExisting:"
+ "serviceForRegistryID:"
+ "serviceID"
+ "services"
+ "servicesDidChange:withAddedServices:removedServices:"
+ "setAccelerometerXExpression:"
+ "setAccelerometerYExpression:"
+ "setAccelerometerZExpression:"
+ "setEventCallBack:target:context:"
+ "setGyroXExpression:"
+ "setGyroYExpression:"
+ "setGyroZExpression:"
+ "setMatching:"
+ "setMatchingMultiple:"
+ "setMotion:"
+ "setServicesChangedCallback:target:context:"
+ "setSourcePressedValueExtendedEventFieldIndex:"
+ "setSourceTouchedValueExtendedEventFieldIndex:"
+ "setTouchedThreshold:"
+ "sourcePressedValueExtendedEventFieldIndex"
+ "sourceTouchedValueExtendedEventFieldIndex"
+ "touchedThreshold"
+ "unregisterEventObserver:"
+ "unregisterServicesChangedObserver:notifyExisting:"
+ "v16@?0d8"
+ "v24@0:8@\"<GCHIDSystemEventObserver>\"16"
+ "v28@0:8@\"<GCHIDSystemServiceMatchObserver>\"16B24"
+ "v32@?0@\"GCHIDInputElement\"8^{__IOHIDValue=}16d24"
+ "v40@0:8^?16^v24^v32"
+ "valueWithBytes:objCType:"
+ "withCleanupHandler:"
+ "{?=\"tqe_next\"@\"__GCHIDSystemObservation\"\"tqe_prev\"^@}"
+ "{?=[4]}16@0:8"
+ "{HIDSystemObservationList=\"lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"count\"I\"tqh_first\"@\"__GCHIDSystemObservation\"\"tqh_last\"^@\"primaryHandler\"{?=\"callback\"^v\"target\"Q\"context\"Q}}"
+ "{simd_float4x4_layout=[4{simd_float4_layout=ffff}]}"
- "<%@ %p> {\n\t elements = %@\n\t properties = %@\n\t input = %@\n\t rumble = %@\n}"
- "@?32@0:8@?16o^@24"
- "Tq,N,V_sourceExtendedEventFieldIndex"
- "Tq,R,V_sourceExtendedEventFieldIndex"
- "_GCDisposable"
- "_buildPullExpressionWithOverrideBuilder:error:"
- "_sourceExtendedEventFieldIndex"
- "buildPullExpressionWithOverrideBuilder:error:"
- "setSourceExtendedEventFieldIndex:"
- "sourceExtendedEventFieldIndex"

```
