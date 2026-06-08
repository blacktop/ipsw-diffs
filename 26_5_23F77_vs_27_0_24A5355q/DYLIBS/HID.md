## HID

> `/System/Library/PrivateFrameworks/HID.framework/HID`

```diff

-2238.120.5.0.0
-  __TEXT.__text: 0x98b8
-  __TEXT.__auth_stubs: 0xe40
-  __TEXT.__objc_methlist: 0x1cc4
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x1ca7
-  __TEXT.__gcc_except_tab: 0x48
-  __TEXT.__oslogstring: 0x36c
-  __TEXT.__unwind_info: 0x660
-  __TEXT.__objc_classname: 0x511
-  __TEXT.__objc_methname: 0x341b
-  __TEXT.__objc_methtype: 0x6c2
-  __TEXT.__objc_stubs: 0xba0
-  __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__const: 0x470
-  __DATA_CONST.__objc_classlist: 0x38
+2353.0.0.0.1
+  __TEXT.__text: 0x13464
+  __TEXT.__objc_methlist: 0x248c
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x2203
+  __TEXT.__gcc_except_tab: 0x2e8
+  __TEXT.__oslogstring: 0x6cd
+  __TEXT.__dof_iohidfami: 0x28d
+  __TEXT.__unwind_info: 0x968
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x588
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1168
-  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_selrefs: 0x1580
+  __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x730
-  __AUTH_CONST.__cfstring: 0x880
-  __AUTH_CONST.__objc_const: 0xe40
+  __DATA_CONST.__got: 0x150
+  __AUTH_CONST.__const: 0x78
+  __AUTH_CONST.__cfstring: 0xe20
+  __AUTH_CONST.__objc_const: 0x1db8
   __AUTH_CONST.__objc_intobj: 0x558
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __DATA.__objc_ivar: 0xa0
-  __DATA.__data: 0x1900
-  __DATA_DIRTY.__objc_data: 0x230
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__data: 0x10
+  __DATA.__objc_ivar: 0x1ac
+  __DATA.__data: 0x19f0
+  __DATA.__bss: 0x20
+  __DATA_DIRTY.__objc_data: 0x500
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/TimeSync.framework/TimeSync
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CAB74390-57E0-3FF6-995A-C6E91ADABD20
-  Functions: 682
-  Symbols:   1934
-  CStrings:  1195
+  UUID: 705B6F51-298C-3377-A282-E20CFBDAC532
+  Functions: 977
+  Symbols:   2894
+  CStrings:  563
 
Symbols:
+ +[HIDEventService(VirtualEventService) virtualEventServiceWithDelegate:]
+ +[HIDEventService(VirtualEventService) virtualEventServiceWithDelegate:].cold.1
+ +[HIDLibElement withElementRef:]
+ +[HIDLibElement withElementStruct:parent:index:]
+ -[HIDEvent(HIDHeartRateEventPrivate) heartRateConfidence]
+ -[HIDEvent(HIDHeartRateEventPrivate) heartRateGenerationCount]
+ -[HIDEvent(HIDHeartRateEventPrivate) heartRateLocation]
+ -[HIDEvent(HIDHeartRateEventPrivate) heartRateRate]
+ -[HIDEvent(HIDHeartRateEventPrivate) setHeartRateConfidence:]
+ -[HIDEvent(HIDHeartRateEventPrivate) setHeartRateGenerationCount:]
+ -[HIDEvent(HIDHeartRateEventPrivate) setHeartRateLocation:]
+ -[HIDEvent(HIDHeartRateEventPrivate) setHeartRateRate:]
+ -[HIDEventService(VirtualEventService) isVirtualEventService]
+ -[HIDEventService(VirtualEventService) virtualServiceDelegate]
+ -[HIDEventService(VirtualEventService) virtualServiceDispatchEvent:]
+ -[HIDEventService(VirtualEventService) virtualServiceDispatchEvent:].cold.1
+ -[HIDEventService(VirtualEventService) virtualServiceTerminate]
+ -[HIDEventService(VirtualEventService) virtualServiceTerminate].cold.1
+ -[HIDLibElement .cxx_destruct]
+ -[HIDLibElement collectionCookie]
+ -[HIDLibElement collectionType]
+ -[HIDLibElement dataValue]
+ -[HIDLibElement dealloc]
+ -[HIDLibElement defaultValueRef]
+ -[HIDLibElement description]
+ -[HIDLibElement elementCookie]
+ -[HIDLibElement elementRef]
+ -[HIDLibElement elementStruct]
+ -[HIDLibElement initWithElementRef:]
+ -[HIDLibElement initWithElementStruct:parent:index:]
+ -[HIDLibElement integerValue]
+ -[HIDLibElement isConstant]
+ -[HIDLibElement isEqual:]
+ -[HIDLibElement isEqualToHIDLibElement:]
+ -[HIDLibElement isUpdated]
+ -[HIDLibElement length]
+ -[HIDLibElement psKey]
+ -[HIDLibElement reportID]
+ -[HIDLibElement setDataValue:]
+ -[HIDLibElement setDefaultValueRef:]
+ -[HIDLibElement setElementRef:]
+ -[HIDLibElement setIntegerValue:]
+ -[HIDLibElement setIsConstant:]
+ -[HIDLibElement setIsUpdated:]
+ -[HIDLibElement setPsKey:]
+ -[HIDLibElement setValueRef:]
+ -[HIDLibElement timestamp]
+ -[HIDLibElement type]
+ -[HIDLibElement unitExponent]
+ -[HIDLibElement unit]
+ -[HIDLibElement usageMax]
+ -[HIDLibElement usageMin]
+ -[HIDLibElement usagePage]
+ -[HIDLibElement usage]
+ -[HIDLibElement valueRef]
+ -[IOHIDDeviceClass .cxx_destruct]
+ -[IOHIDDeviceClass close:]
+ -[IOHIDDeviceClass connect]
+ -[IOHIDDeviceClass copyMatchingElements:elements:options:]
+ -[IOHIDDeviceClass copyMatchingElements:elements:options:].cold.1
+ -[IOHIDDeviceClass copyObsoleteDictionary:]
+ -[IOHIDDeviceClass createElements:outError:]
+ -[IOHIDDeviceClass createReportElements:outError:]
+ -[IOHIDDeviceClass createReportElements:outError:].cold.1
+ -[IOHIDDeviceClass dealloc]
+ -[IOHIDDeviceClass elementsSortedByCookie:]
+ -[IOHIDDeviceClass getAsyncEventSource:]
+ -[IOHIDDeviceClass getElement:]
+ -[IOHIDDeviceClass getElementCount:andReportCount:]
+ -[IOHIDDeviceClass getPort]
+ -[IOHIDDeviceClass getProperty:property:]
+ -[IOHIDDeviceClass getReport:reportID:report:reportLength:timeout:callback:context:options:]
+ -[IOHIDDeviceClass getValue:value:timeout:callback:context:options:]
+ -[IOHIDDeviceClass initConnect]
+ -[IOHIDDeviceClass initConnect].cold.1
+ -[IOHIDDeviceClass initElements]
+ -[IOHIDDeviceClass initPort]
+ -[IOHIDDeviceClass initQueue]
+ -[IOHIDDeviceClass initWithFactory:]
+ -[IOHIDDeviceClass open:]
+ -[IOHIDDeviceClass port]
+ -[IOHIDDeviceClass probe:service:outScore:]
+ -[IOHIDDeviceClass propertyForElementKey:]
+ -[IOHIDDeviceClass queryInterface:outInterface:]
+ -[IOHIDDeviceClass releaseReport:]
+ -[IOHIDDeviceClass runLoopSource]
+ -[IOHIDDeviceClass service]
+ -[IOHIDDeviceClass setInputReportCallback:reportLength:callback:context:options:]
+ -[IOHIDDeviceClass setInputReportWithTimeStampCallback:reportLength:callback:context:options:]
+ -[IOHIDDeviceClass setProperty:property:]
+ -[IOHIDDeviceClass setReport:reportID:report:reportLength:timeout:callback:context:options:]
+ -[IOHIDDeviceClass setValue:value:timeout:callback:context:options:]
+ -[IOHIDDeviceClass start:service:]
+ -[IOHIDDeviceClass start:service:].cold.1
+ -[IOHIDDeviceClass stop]
+ -[IOHIDDeviceClass valueAvailableCallback:]
+ -[IOHIDIUnknown2 dealloc]
+ -[IOHIDIUnknown2 init]
+ -[IOHIDIUnknown2 queryInterface:outInterface:]
+ -[IOHIDObsoleteDeviceClass allocOutputTransaction]
+ -[IOHIDObsoleteDeviceClass allocQueue]
+ -[IOHIDObsoleteDeviceClass copyMatchingElements:element:]
+ -[IOHIDObsoleteDeviceClass dealloc]
+ -[IOHIDObsoleteDeviceClass getElementValue:value:options:]
+ -[IOHIDObsoleteDeviceClass init]
+ -[IOHIDObsoleteDeviceClass queryInterface:outInterface:]
+ -[IOHIDObsoleteDeviceClass setElementValue:value:]
+ -[IOHIDObsoleteDeviceClass setInterruptReportHandlerCallback:reportBufferSize:callback:callbackTarget:callbackRefcon:]
+ -[IOHIDObsoleteDeviceClass setRemovalCallback:removalTarget:removalRefcon:]
+ -[IOHIDObsoleteDeviceClass start:service:]
+ -[IOHIDObsoleteQueueClass dealloc]
+ -[IOHIDObsoleteQueueClass getNextEvent:]
+ -[IOHIDObsoleteQueueClass initWithDevice:]
+ -[IOHIDObsoleteQueueClass queryInterface:outInterface:]
+ -[IOHIDObsoleteQueueClass setEventCallout:callbackTarget:callbackRefcon:]
+ -[IOHIDOutputTransactionClass dealloc]
+ -[IOHIDOutputTransactionClass getElementValue:value:options:]
+ -[IOHIDOutputTransactionClass initWithDevice:]
+ -[IOHIDOutputTransactionClass queryInterface:outInterface:]
+ -[IOHIDOutputTransactionClass setElementValue:value:options:]
+ -[IOHIDPlugin dealloc]
+ -[IOHIDPlugin initWithFactory:]
+ -[IOHIDPlugin init]
+ -[IOHIDPlugin probe:service:outScore:]
+ -[IOHIDPlugin start:service:]
+ -[IOHIDPlugin stop]
+ -[IOHIDQueueClass .cxx_destruct]
+ -[IOHIDQueueClass addElement:]
+ -[IOHIDQueueClass containsElement:pValue:]
+ -[IOHIDQueueClass copyNextValue:]
+ -[IOHIDQueueClass dealloc]
+ -[IOHIDQueueClass getAsyncEventSource:]
+ -[IOHIDQueueClass getDepth:]
+ -[IOHIDQueueClass initWithDevice:]
+ -[IOHIDQueueClass initWithDevice:port:source:]
+ -[IOHIDQueueClass initWithDevice:port:source:].cold.1
+ -[IOHIDQueueClass mapMemory]
+ -[IOHIDQueueClass mapMemory].cold.1
+ -[IOHIDQueueClass queryInterface:outInterface:]
+ -[IOHIDQueueClass queueCallback:msg:size:info:]
+ -[IOHIDQueueClass removeElement:]
+ -[IOHIDQueueClass setDepth:]
+ -[IOHIDQueueClass setValueAvailableCallback:context:]
+ -[IOHIDQueueClass setupAnalytics]
+ -[IOHIDQueueClass setupAnalytics].cold.1
+ -[IOHIDQueueClass signalQueueEmpty]
+ -[IOHIDQueueClass start]
+ -[IOHIDQueueClass start].cold.1
+ -[IOHIDQueueClass stop]
+ -[IOHIDQueueClass unmapMemory]
+ -[IOHIDQueueClass updateUsageAnalytics]
+ -[IOHIDTransactionClass .cxx_destruct]
+ -[IOHIDTransactionClass addElement:]
+ -[IOHIDTransactionClass clear]
+ -[IOHIDTransactionClass commit:timeout:callback:options:]
+ -[IOHIDTransactionClass containsElement:value:]
+ -[IOHIDTransactionClass dealloc]
+ -[IOHIDTransactionClass device]
+ -[IOHIDTransactionClass getAsyncEventSource:]
+ -[IOHIDTransactionClass getDirection:]
+ -[IOHIDTransactionClass getValue:value:options:]
+ -[IOHIDTransactionClass initWithDevice:]
+ -[IOHIDTransactionClass queryInterface:outInterface:]
+ -[IOHIDTransactionClass removeElement:]
+ -[IOHIDTransactionClass setDevice:]
+ -[IOHIDTransactionClass setDirection:]
+ -[IOHIDTransactionClass setValue:value:options:]
+ GCC_except_table10
+ GCC_except_table12
+ GCC_except_table13
+ GCC_except_table15
+ GCC_except_table24
+ GCC_except_table27
+ GCC_except_table29
+ GCC_except_table31
+ GCC_except_table34
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table44
+ GCC_except_table45
+ GCC_except_table46
+ GCC_except_table5
+ GCC_except_table6
+ GCC_except_table7
+ GCC_except_table8
+ OBJC_IVAR_$_IOHIDDeviceClass._port
+ OBJC_IVAR_$_IOHIDDeviceClass._queue
+ OBJC_IVAR_$_IOHIDDeviceClass._runLoopSource
+ OBJC_IVAR_$_IOHIDDeviceClass._service
+ OBJC_IVAR_$_IOHIDIUnknown2._vtbl
+ OBJC_IVAR_$_IOHIDObsoleteDeviceClass._interface
+ OBJC_IVAR_$_IOHIDObsoleteDeviceClass._notification
+ OBJC_IVAR_$_IOHIDObsoleteDeviceClass._notifyPort
+ OBJC_IVAR_$_IOHIDObsoleteDeviceClass._removalCallback
+ OBJC_IVAR_$_IOHIDObsoleteDeviceClass._removalRefcon
+ OBJC_IVAR_$_IOHIDObsoleteDeviceClass._removalTarget
+ OBJC_IVAR_$_IOHIDObsoleteDeviceClass._reportCallback
+ OBJC_IVAR_$_IOHIDObsoleteDeviceClass._reportCallbackRefcon
+ OBJC_IVAR_$_IOHIDObsoleteDeviceClass._reportCallbackTarget
+ OBJC_IVAR_$_IOHIDObsoleteQueueClass._eventCallback
+ OBJC_IVAR_$_IOHIDObsoleteQueueClass._eventCallbackRefcon
+ OBJC_IVAR_$_IOHIDObsoleteQueueClass._eventCallbackTarget
+ OBJC_IVAR_$_IOHIDObsoleteQueueClass._interface
+ OBJC_IVAR_$_IOHIDOutputTransactionClass._outputInterface
+ OBJC_IVAR_$_IOHIDPlugin._plugin
+ OBJC_IVAR_$_IOHIDPlugin._uuid
+ OBJC_IVAR_$_IOHIDQueueClass._depth
+ OBJC_IVAR_$_IOHIDQueueClass._device
+ OBJC_IVAR_$_IOHIDQueueClass._lastTail
+ OBJC_IVAR_$_IOHIDQueueClass._machPort
+ OBJC_IVAR_$_IOHIDQueueClass._port
+ OBJC_IVAR_$_IOHIDQueueClass._queue
+ OBJC_IVAR_$_IOHIDQueueClass._queueLock
+ OBJC_IVAR_$_IOHIDQueueClass._queueMemory
+ OBJC_IVAR_$_IOHIDQueueClass._queueMemorySize
+ OBJC_IVAR_$_IOHIDQueueClass._queueSizeChanged
+ OBJC_IVAR_$_IOHIDQueueClass._queueToken
+ OBJC_IVAR_$_IOHIDQueueClass._runLoopSource
+ OBJC_IVAR_$_IOHIDQueueClass._usageAnalytics
+ OBJC_IVAR_$_IOHIDQueueClass._valueAvailableCallback
+ OBJC_IVAR_$_IOHIDQueueClass._valueAvailableContext
+ OBJC_IVAR_$_IOHIDTransactionClass._callbackLock
+ OBJC_IVAR_$_IOHIDTransactionClass._device
+ OBJC_IVAR_$_IOHIDTransactionClass._direction
+ OBJC_IVAR_$_IOHIDTransactionClass._elements
+ OBJC_IVAR_$_IOHIDTransactionClass._interface
+ OBJC_IVAR_$_IOHIDTransactionClass._pendingCallbacks
+ _CFEqual
+ _CFGetRetainCount
+ _CFMachPortCreateRunLoopSource
+ _CFMachPortCreateWithPort
+ _CFMachPortInvalidate
+ _CFNumberCreate
+ _CFPlugInAddInstanceForFactory
+ _CFPlugInRemoveInstanceForFactory
+ _CFPropertyListCreateDeepCopy
+ _CFRetain
+ _CFStringCreateWithCString
+ _CFUUIDCreateFromUUIDBytes
+ _CFUUIDGetConstantUUIDWithBytes
+ _CFUUIDGetUUIDBytes
+ _DynamicButtonEventFields
+ _IOConnectCallAsyncMethod
+ _IOConnectCallAsyncScalarMethod
+ _IOConnectCallMethod
+ _IOConnectCallScalarMethod
+ _IOConnectMapMemory
+ _IOConnectSetCFProperty
+ _IOConnectUnmapMemory
+ _IODataQueueAllocateNotificationPort
+ _IODataQueueDequeue
+ _IODataQueuePeek
+ _IODispatchCalloutFromMessage
+ _IOHIDAnalyticsEventActivate
+ _IOHIDAnalyticsEventCancel
+ _IOHIDAnalyticsGetConsoleModeStatus
+ _IOHIDAnalyticsGetConsoleModeStatus.cold.1
+ _IOHIDAnalyticsHistogramEventCreate
+ _IOHIDAnalyticsHistogramEventSetIntegerValue
+ _IOHIDElementGetCollectionType
+ _IOHIDSessionGetEventSystem
+ _IOObjectGetClass
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryGetRegistryEntryID
+ _IOServiceClose
+ _IOServiceOpen
+ _NSClassFromString
+ _OBJC_CLASS_$_HIDLibElement
+ _OBJC_CLASS_$_IOHIDDeviceClass
+ _OBJC_CLASS_$_IOHIDIUnknown2
+ _OBJC_CLASS_$_IOHIDObsoleteDeviceClass
+ _OBJC_CLASS_$_IOHIDObsoleteQueueClass
+ _OBJC_CLASS_$_IOHIDOutputTransactionClass
+ _OBJC_CLASS_$_IOHIDPlugin
+ _OBJC_CLASS_$_IOHIDQueueClass
+ _OBJC_CLASS_$_IOHIDTransactionClass
+ _OBJC_CLASS_$_NSComparisonPredicate
+ _OBJC_CLASS_$_NSExpression
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSValue
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_IVAR_$_HIDLibElement._defaultValue
+ _OBJC_IVAR_$_HIDLibElement._element
+ _OBJC_IVAR_$_HIDLibElement._elementStruct
+ _OBJC_IVAR_$_HIDLibElement._isConstant
+ _OBJC_IVAR_$_HIDLibElement._isUpdated
+ _OBJC_IVAR_$_HIDLibElement._psKey
+ _OBJC_IVAR_$_IOHIDDeviceClass._callbackLock
+ _OBJC_IVAR_$_IOHIDDeviceClass._connect
+ _OBJC_IVAR_$_IOHIDDeviceClass._device
+ _OBJC_IVAR_$_IOHIDDeviceClass._deviceLock
+ _OBJC_IVAR_$_IOHIDDeviceClass._elements
+ _OBJC_IVAR_$_IOHIDDeviceClass._inputReportBuffer
+ _OBJC_IVAR_$_IOHIDDeviceClass._inputReportBufferLength
+ _OBJC_IVAR_$_IOHIDDeviceClass._inputReportCallback
+ _OBJC_IVAR_$_IOHIDDeviceClass._inputReportContext
+ _OBJC_IVAR_$_IOHIDDeviceClass._inputReportTimestampCallback
+ _OBJC_IVAR_$_IOHIDDeviceClass._machPort
+ _OBJC_IVAR_$_IOHIDDeviceClass._opened
+ _OBJC_IVAR_$_IOHIDDeviceClass._pendingCallbacks
+ _OBJC_IVAR_$_IOHIDDeviceClass._properties
+ _OBJC_IVAR_$_IOHIDDeviceClass._reportElements
+ _OBJC_IVAR_$_IOHIDDeviceClass._sortedElements
+ _OBJC_IVAR_$_IOHIDDeviceClass._tccGranted
+ _OBJC_IVAR_$_IOHIDDeviceClass._tccRequested
+ _OBJC_IVAR_$_IOHIDQueueClass._queueHeader
+ _OBJC_METACLASS_$_HIDLibElement
+ _OBJC_METACLASS_$_IOHIDDeviceClass
+ _OBJC_METACLASS_$_IOHIDIUnknown2
+ _OBJC_METACLASS_$_IOHIDObsoleteDeviceClass
+ _OBJC_METACLASS_$_IOHIDObsoleteQueueClass
+ _OBJC_METACLASS_$_IOHIDOutputTransactionClass
+ _OBJC_METACLASS_$_IOHIDPlugin
+ _OBJC_METACLASS_$_IOHIDQueueClass
+ _OBJC_METACLASS_$_IOHIDTransactionClass
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_9
+ _RosettaLibrary.libLibrary
+ _SetPropsPassthrough
+ __IOHIDElementCreateWithParentAndData
+ __IOHIDElementGetLength
+ __IOHIDElementSetDeviceInterface
+ __IOHIDEventSystemAddService
+ __IOHIDEventSystemGetEnumerationQueue
+ __IOHIDLogCategory
+ __IOHIDServiceCopyDispatchQueue
+ __IOHIDServiceCreateVirtual
+ __IOHIDServiceGetOwner
+ __IOHIDServiceTerminate
+ __IOHIDValueCopyToElementValueHeader
+ __IOHIDValueCreateWithElementValuePtr
+ __IOHIDValueCreateWithStruct
+ __IOHIDValueGetFlags
+ __NSConcreteGlobalBlock
+ __OBJC_$_CLASS_METHODS_HIDEvent(HIDEventDesc|HIDFramework|HIDVendorDefinedEvent|HIDVendorDefinedEventPrivate|HIDTemperatureEvent|HIDTemperatureEventPrivate|HIDAccelerometerEvent|HIDAccelerometerEventPrivate|HIDHeartRateEventPrivate|HIDGenericGestureEvent|HIDGenericGestureEventPrivate|HIDAmbientLightSensorEvent|HIDAmbientLightSensorEventPrivate|HIDTouchSensitiveButtonEventPrivate|HIDPowerEventPrivate|HIDForceEvent|HIDForceEventPrivate|HIDMotionGestureEvent|HIDMotionGestureEventPrivate|HIDForceStageEventPrivate|HIDGameControllerEvent|HIDGameControllerEventPrivate|HIDDigitizerEvent|HIDDigitizerEventPrivate|HIDCompassEvent|HIDCompassEventPrivate|HIDMotionActivityEvent|HIDMotionActivityEventPrivate|HIDBrightnessEvent|HIDBrightnessEventPrivate|HIDGyroEvent|HIDGyroEventPrivate|HIDButtonEvent|HIDButtonEventPrivate|HIDAtmosphericPressureEvent|HIDAtmosphericPressureEventPrivate|HIDHumidityEventPrivate|HIDScrollEvent|HIDScrollEventPrivate|HIDBiometricEvent|HIDBiometricEventPrivate|HIDLEDEvent|HIDLEDEventPrivate|HIDOrientationEvent|HIDOrientationEventPrivate|HIDProximityEvent|HIDProximityEventPrivate|HIDKeyboardEvent|HIDKeyboardEventPrivate|HIDPointerEvent|HIDPointerEventPrivate)
+ __OBJC_$_CLASS_METHODS_HIDEventService(HIDFramework|HIDFrameworkPrivate|VirtualEventService)
+ __OBJC_$_CLASS_METHODS_HIDLibElement
+ __OBJC_$_INSTANCE_METHODS_HIDEvent(HIDEventDesc|HIDFramework|HIDVendorDefinedEvent|HIDVendorDefinedEventPrivate|HIDTemperatureEvent|HIDTemperatureEventPrivate|HIDAccelerometerEvent|HIDAccelerometerEventPrivate|HIDHeartRateEventPrivate|HIDGenericGestureEvent|HIDGenericGestureEventPrivate|HIDAmbientLightSensorEvent|HIDAmbientLightSensorEventPrivate|HIDTouchSensitiveButtonEventPrivate|HIDPowerEventPrivate|HIDForceEvent|HIDForceEventPrivate|HIDMotionGestureEvent|HIDMotionGestureEventPrivate|HIDForceStageEventPrivate|HIDGameControllerEvent|HIDGameControllerEventPrivate|HIDDigitizerEvent|HIDDigitizerEventPrivate|HIDCompassEvent|HIDCompassEventPrivate|HIDMotionActivityEvent|HIDMotionActivityEventPrivate|HIDBrightnessEvent|HIDBrightnessEventPrivate|HIDGyroEvent|HIDGyroEventPrivate|HIDButtonEvent|HIDButtonEventPrivate|HIDAtmosphericPressureEvent|HIDAtmosphericPressureEventPrivate|HIDHumidityEventPrivate|HIDScrollEvent|HIDScrollEventPrivate|HIDBiometricEvent|HIDBiometricEventPrivate|HIDLEDEvent|HIDLEDEventPrivate|HIDOrientationEvent|HIDOrientationEventPrivate|HIDProximityEvent|HIDProximityEventPrivate|HIDKeyboardEvent|HIDKeyboardEventPrivate|HIDPointerEvent|HIDPointerEventPrivate)
+ __OBJC_$_INSTANCE_METHODS_HIDEventService(HIDFramework|HIDFrameworkPrivate|VirtualEventService)
+ __OBJC_$_INSTANCE_METHODS_HIDLibElement
+ __OBJC_$_INSTANCE_METHODS_IOHIDDeviceClass
+ __OBJC_$_INSTANCE_METHODS_IOHIDIUnknown2
+ __OBJC_$_INSTANCE_METHODS_IOHIDObsoleteDeviceClass
+ __OBJC_$_INSTANCE_METHODS_IOHIDObsoleteQueueClass
+ __OBJC_$_INSTANCE_METHODS_IOHIDOutputTransactionClass
+ __OBJC_$_INSTANCE_METHODS_IOHIDPlugin
+ __OBJC_$_INSTANCE_METHODS_IOHIDQueueClass
+ __OBJC_$_INSTANCE_METHODS_IOHIDTransactionClass
+ __OBJC_$_INSTANCE_VARIABLES_HIDLibElement
+ __OBJC_$_INSTANCE_VARIABLES_IOHIDDeviceClass
+ __OBJC_$_INSTANCE_VARIABLES_IOHIDIUnknown2
+ __OBJC_$_INSTANCE_VARIABLES_IOHIDObsoleteDeviceClass
+ __OBJC_$_INSTANCE_VARIABLES_IOHIDObsoleteQueueClass
+ __OBJC_$_INSTANCE_VARIABLES_IOHIDOutputTransactionClass
+ __OBJC_$_INSTANCE_VARIABLES_IOHIDPlugin
+ __OBJC_$_INSTANCE_VARIABLES_IOHIDQueueClass
+ __OBJC_$_INSTANCE_VARIABLES_IOHIDTransactionClass
+ __OBJC_$_PROP_LIST_HIDLibElement
+ __OBJC_$_PROP_LIST_IOHIDDeviceClass
+ __OBJC_CLASS_PROTOCOLS_$_HIDEvent(HIDEventDesc|HIDFramework|HIDVendorDefinedEvent|HIDVendorDefinedEventPrivate|HIDTemperatureEvent|HIDTemperatureEventPrivate|HIDAccelerometerEvent|HIDAccelerometerEventPrivate|HIDHeartRateEventPrivate|HIDGenericGestureEvent|HIDGenericGestureEventPrivate|HIDAmbientLightSensorEvent|HIDAmbientLightSensorEventPrivate|HIDTouchSensitiveButtonEventPrivate|HIDPowerEventPrivate|HIDForceEvent|HIDForceEventPrivate|HIDMotionGestureEvent|HIDMotionGestureEventPrivate|HIDForceStageEventPrivate|HIDGameControllerEvent|HIDGameControllerEventPrivate|HIDDigitizerEvent|HIDDigitizerEventPrivate|HIDCompassEvent|HIDCompassEventPrivate|HIDMotionActivityEvent|HIDMotionActivityEventPrivate|HIDBrightnessEvent|HIDBrightnessEventPrivate|HIDGyroEvent|HIDGyroEventPrivate|HIDButtonEvent|HIDButtonEventPrivate|HIDAtmosphericPressureEvent|HIDAtmosphericPressureEventPrivate|HIDHumidityEventPrivate|HIDScrollEvent|HIDScrollEventPrivate|HIDBiometricEvent|HIDBiometricEventPrivate|HIDLEDEvent|HIDLEDEventPrivate|HIDOrientationEvent|HIDOrientationEventPrivate|HIDProximityEvent|HIDProximityEventPrivate|HIDKeyboardEvent|HIDKeyboardEventPrivate|HIDPointerEvent|HIDPointerEventPrivate)
+ __OBJC_CLASS_RO_$_HIDLibElement
+ __OBJC_CLASS_RO_$_IOHIDDeviceClass
+ __OBJC_CLASS_RO_$_IOHIDIUnknown2
+ __OBJC_CLASS_RO_$_IOHIDObsoleteDeviceClass
+ __OBJC_CLASS_RO_$_IOHIDObsoleteQueueClass
+ __OBJC_CLASS_RO_$_IOHIDOutputTransactionClass
+ __OBJC_CLASS_RO_$_IOHIDPlugin
+ __OBJC_CLASS_RO_$_IOHIDQueueClass
+ __OBJC_CLASS_RO_$_IOHIDTransactionClass
+ __OBJC_METACLASS_RO_$_HIDLibElement
+ __OBJC_METACLASS_RO_$_IOHIDDeviceClass
+ __OBJC_METACLASS_RO_$_IOHIDIUnknown2
+ __OBJC_METACLASS_RO_$_IOHIDObsoleteDeviceClass
+ __OBJC_METACLASS_RO_$_IOHIDObsoleteQueueClass
+ __OBJC_METACLASS_RO_$_IOHIDOutputTransactionClass
+ __OBJC_METACLASS_RO_$_IOHIDPlugin
+ __OBJC_METACLASS_RO_$_IOHIDQueueClass
+ __OBJC_METACLASS_RO_$_IOHIDTransactionClass
+ __ZL11_addElementPvP14__IOHIDElementj
+ __ZL11_addElementPvjj
+ __ZL11_hasElementPvj
+ __ZL13_eventCalloutPviS_
+ __ZL13_getAsyncPortPv
+ __ZL13_getNextEventPvP16IOHIDEventStruct12UnsignedWidej
+ __ZL14_copyNextValuePvPP12__IOHIDValuejj
+ __ZL14_queueCallbackP12__CFMachPortP17mach_msg_header_tlPv
+ __ZL14_removeElementPvP14__IOHIDElementj
+ __ZL14_removeElementPvj
+ __ZL16_containsElementPvP14__IOHIDElementPhj
+ __ZL16_createAsyncPortPvPj
+ __ZL16_getEventCalloutPvPPFvS_iS_S_EPS_S3_
+ __ZL16_setEventCalloutPvPFvS_iS_S_ES_S_
+ __ZL20_getAsyncEventSourcePv
+ __ZL20_getAsyncEventSourcePvPPKv
+ __ZL23_createAsyncEventSourcePvPP17__CFRunLoopSource
+ __ZL26_setValueAvailableCallbackPvPFvS_iS_ES_
+ __ZL5_stopPv
+ __ZL5_stopPvj
+ __ZL6_startPv
+ __ZL6_startPvj
+ __ZL7_createPvjj
+ __ZL8_disposePv
+ __ZL9_getDepthPvPj
+ __ZL9_setDepthPvjj
+ __ZSt9terminatev
+ ___58-[IOHIDDeviceClass copyMatchingElements:elements:options:]_block_invoke
+ ___58-[IOHIDDeviceClass copyMatchingElements:elements:options:]_block_invoke.cold.1
+ ___63-[HIDEventService(VirtualEventService) virtualServiceTerminate]_block_invoke
+ ___68-[HIDEventService(VirtualEventService) virtualServiceDispatchEvent:]_block_invoke
+ ___72+[HIDEventService(VirtualEventService) virtualEventServiceWithDelegate:]_block_invoke
+ ___HIDVirtualServiceCopyEventCallback
+ ___HIDVirtualServiceCopyMatchingEventCallback
+ ___HIDVirtualServiceSetOutputEventCallback
+ ___HIDVirtualServiceUnscheduleFromDispatchQueueCallback
+ ___IOHIDAnalyticsGetConsoleModeStatus_block_invoke
+ ___IOHIDEventSystem_debug
+ _____loadFramework_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e44_v24?0"GPProcessMonitor"8"GPProcessInfo"16ls32l8
+ ___block_descriptor_48_e8_32s40s_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_literal_global
+ ___clang_call_terminate
+ ___cxa_begin_catch
+ ___gxx_personality_v0
+ ___loadFramework.gpHandle
+ ___loadFramework.gpOnce
+ __addElement
+ __addOutputElement
+ __addRef
+ __allocOutputTransaction
+ __allocQueue
+ __asyncCallback
+ __asyncCallback.cold.1
+ __asyncCallback.cold.2
+ __clear
+ __clearOutput
+ __close
+ __commit
+ __commitOutput
+ __containsElement
+ __copyMatchingElements
+ __create
+ __createAsyncEventSource
+ __createAsyncPort
+ __dispatch_main_q
+ __dispose
+ __getAsyncEventSource
+ __getAsyncPort
+ __getDirection
+ __getElementDefault
+ __getElementValue
+ __getOutputAsyncEventSource
+ __getProperty
+ __getReport
+ __getValue
+ __hasElement
+ __open
+ __os_log_impl
+ __portCallback
+ __probe
+ __queryElementValue
+ __queryInterface
+ __release
+ __removeElement
+ __removeOutputElement
+ __setDirection
+ __setElementDefault
+ __setElementValue
+ __setInputReportCallback
+ __setInputReportWithTimeStampCallback
+ __setInterruptReportHandlerCallback
+ __setProperty
+ __setRemovalCallback
+ __setReport
+ __setValue
+ __start
+ __startAllQueues
+ __stop
+ __stopAllQueues
+ __valueAvailableCallback
+ __virtualServiceID
+ _delegateObjectKey
+ _dispatch_once
+ _dlopen
+ _dlsym
+ _dynLinkrosetta_convert_to_rosetta_absolute_time
+ _dynLinkrosetta_is_current_process_translated
+ _free
+ _initrosetta_convert_to_rosetta_absolute_time
+ _initrosetta_is_current_process_translated
+ _interestCallback
+ _kCFAllocatorSystemDefault
+ _kCFBooleanTrue
+ _mach_port_mod_refs
+ _mach_task_self_
+ _malloc_type_calloc
+ _malloc_type_malloc
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_begin_catch
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyStruct
+ _objc_end_catch
+ _objc_getAssociatedObject
+ _objc_msgSend$addElement:
+ _objc_msgSend$allocOutputTransaction
+ _objc_msgSend$allocQueue
+ _objc_msgSend$arrayByAddingObjectsFromArray:
+ _objc_msgSend$boolValue
+ _objc_msgSend$clear
+ _objc_msgSend$close:
+ _objc_msgSend$code
+ _objc_msgSend$commit:timeout:callback:options:
+ _objc_msgSend$connect
+ _objc_msgSend$containsElement:pValue:
+ _objc_msgSend$containsElement:value:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$copyMatchingElements:element:
+ _objc_msgSend$copyMatchingElements:elements:options:
+ _objc_msgSend$copyNextValue:
+ _objc_msgSend$copyObsoleteDictionary:
+ _objc_msgSend$createElements:outError:
+ _objc_msgSend$createReportElements:outError:
+ _objc_msgSend$defaultValueRef
+ _objc_msgSend$elementCookie
+ _objc_msgSend$elementRef
+ _objc_msgSend$elementStruct
+ _objc_msgSend$elementsSortedByCookie:
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$expressionForConstantValue:
+ _objc_msgSend$expressionForKeyPath:
+ _objc_msgSend$filterUsingPredicate:
+ _objc_msgSend$getAsyncEventSource:
+ _objc_msgSend$getDepth:
+ _objc_msgSend$getDirection:
+ _objc_msgSend$getElement:
+ _objc_msgSend$getElementCount:andReportCount:
+ _objc_msgSend$getElementValue:value:options:
+ _objc_msgSend$getNextEvent:
+ _objc_msgSend$getPort
+ _objc_msgSend$getProperty:property:
+ _objc_msgSend$getReport:reportID:report:reportLength:timeout:callback:context:options:
+ _objc_msgSend$getValue:value:options:
+ _objc_msgSend$getValue:value:timeout:callback:context:options:
+ _objc_msgSend$indexOfObject:
+ _objc_msgSend$initConnect
+ _objc_msgSend$initElements
+ _objc_msgSend$initPort
+ _objc_msgSend$initQueue
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithDevice:port:source:
+ _objc_msgSend$initWithElementRef:
+ _objc_msgSend$initWithElementStruct:parent:index:
+ _objc_msgSend$initWithFactory:
+ _objc_msgSend$initWithLength:
+ _objc_msgSend$isEqualToHIDLibElement:
+ _objc_msgSend$isVirtualEventService
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$mapMemory
+ _objc_msgSend$mutableBytes
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$numberWithUnsignedLong:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$open:
+ _objc_msgSend$performSelector:
+ _objc_msgSend$pointerValue
+ _objc_msgSend$port
+ _objc_msgSend$predicateWithLeftExpression:rightExpression:modifier:type:options:
+ _objc_msgSend$probe:service:outScore:
+ _objc_msgSend$propertyForElementKey:
+ _objc_msgSend$queryInterface:outInterface:
+ _objc_msgSend$queueCallback:msg:size:info:
+ _objc_msgSend$releaseReport:
+ _objc_msgSend$removeElement:
+ _objc_msgSend$removeObject:
+ _objc_msgSend$replaceObjectAtIndex:withObject:
+ _objc_msgSend$runLoopSource
+ _objc_msgSend$setDefaultValueRef:
+ _objc_msgSend$setDepth:
+ _objc_msgSend$setElementValue:value:
+ _objc_msgSend$setElementValue:value:options:
+ _objc_msgSend$setEventCallout:callbackTarget:callbackRefcon:
+ _objc_msgSend$setInputReportCallback:reportLength:callback:context:options:
+ _objc_msgSend$setInputReportWithTimeStampCallback:reportLength:callback:context:options:
+ _objc_msgSend$setInterruptReportHandlerCallback:reportBufferSize:callback:callbackTarget:callbackRefcon:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setProperty:property:
+ _objc_msgSend$setRemovalCallback:removalTarget:removalRefcon:
+ _objc_msgSend$setReport:reportID:report:reportLength:timeout:callback:context:options:
+ _objc_msgSend$setUpdateHandler:
+ _objc_msgSend$setValue:value:options:
+ _objc_msgSend$setValue:value:timeout:callback:context:options:
+ _objc_msgSend$setValueAvailableCallback:context:
+ _objc_msgSend$setupAnalytics
+ _objc_msgSend$signalQueueEmpty
+ _objc_msgSend$start
+ _objc_msgSend$start:service:
+ _objc_msgSend$stop
+ _objc_msgSend$stringByReplacingCharactersInRange:withString:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$unit
+ _objc_msgSend$unitExponent
+ _objc_msgSend$unmapMemory
+ _objc_msgSend$updateUsageAnalytics
+ _objc_msgSend$valueAvailableCallback:
+ _objc_msgSend$valueWithPointer:
+ _objc_msgSend$withElementStruct:parent:index:
+ _objc_opt_new
+ _objc_release_x26
+ _objc_release_x28
+ _objc_retain_x1
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_setAssociatedObject
+ _objc_setProperty_atomic_copy
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _sel_getUid
+ _virtualEventServiceIdentifierKey
+ _virtualEventServiceWithDelegate:.callbacks
- GCC_except_table25
- __OBJC_$_CLASS_METHODS_HIDEvent(HIDEventDesc|HIDFramework|HIDVendorDefinedEvent|HIDVendorDefinedEventPrivate|HIDTemperatureEvent|HIDTemperatureEventPrivate|HIDAccelerometerEvent|HIDAccelerometerEventPrivate|HIDGenericGestureEvent|HIDGenericGestureEventPrivate|HIDAmbientLightSensorEvent|HIDAmbientLightSensorEventPrivate|HIDTouchSensitiveButtonEventPrivate|HIDPowerEventPrivate|HIDForceEvent|HIDForceEventPrivate|HIDMotionGestureEvent|HIDMotionGestureEventPrivate|HIDForceStageEventPrivate|HIDGameControllerEvent|HIDGameControllerEventPrivate|HIDDigitizerEvent|HIDDigitizerEventPrivate|HIDCompassEvent|HIDCompassEventPrivate|HIDMotionActivityEvent|HIDMotionActivityEventPrivate|HIDBrightnessEvent|HIDBrightnessEventPrivate|HIDGyroEvent|HIDGyroEventPrivate|HIDButtonEvent|HIDButtonEventPrivate|HIDAtmosphericPressureEvent|HIDAtmosphericPressureEventPrivate|HIDHumidityEventPrivate|HIDScrollEvent|HIDScrollEventPrivate|HIDBiometricEvent|HIDBiometricEventPrivate|HIDLEDEvent|HIDLEDEventPrivate|HIDOrientationEvent|HIDOrientationEventPrivate|HIDProximityEvent|HIDProximityEventPrivate|HIDKeyboardEvent|HIDKeyboardEventPrivate|HIDPointerEvent|HIDPointerEventPrivate)
- __OBJC_$_INSTANCE_METHODS_HIDEvent(HIDEventDesc|HIDFramework|HIDVendorDefinedEvent|HIDVendorDefinedEventPrivate|HIDTemperatureEvent|HIDTemperatureEventPrivate|HIDAccelerometerEvent|HIDAccelerometerEventPrivate|HIDGenericGestureEvent|HIDGenericGestureEventPrivate|HIDAmbientLightSensorEvent|HIDAmbientLightSensorEventPrivate|HIDTouchSensitiveButtonEventPrivate|HIDPowerEventPrivate|HIDForceEvent|HIDForceEventPrivate|HIDMotionGestureEvent|HIDMotionGestureEventPrivate|HIDForceStageEventPrivate|HIDGameControllerEvent|HIDGameControllerEventPrivate|HIDDigitizerEvent|HIDDigitizerEventPrivate|HIDCompassEvent|HIDCompassEventPrivate|HIDMotionActivityEvent|HIDMotionActivityEventPrivate|HIDBrightnessEvent|HIDBrightnessEventPrivate|HIDGyroEvent|HIDGyroEventPrivate|HIDButtonEvent|HIDButtonEventPrivate|HIDAtmosphericPressureEvent|HIDAtmosphericPressureEventPrivate|HIDHumidityEventPrivate|HIDScrollEvent|HIDScrollEventPrivate|HIDBiometricEvent|HIDBiometricEventPrivate|HIDLEDEvent|HIDLEDEventPrivate|HIDOrientationEvent|HIDOrientationEventPrivate|HIDProximityEvent|HIDProximityEventPrivate|HIDKeyboardEvent|HIDKeyboardEventPrivate|HIDPointerEvent|HIDPointerEventPrivate)
- __OBJC_$_INSTANCE_METHODS_HIDEventService(HIDFramework|HIDFrameworkPrivate)
- __OBJC_$_PROP_LIST_HIDEventService_$_HIDFramework
- __OBJC_CLASS_PROTOCOLS_$_HIDEvent(HIDEventDesc|HIDFramework|HIDVendorDefinedEvent|HIDVendorDefinedEventPrivate|HIDTemperatureEvent|HIDTemperatureEventPrivate|HIDAccelerometerEvent|HIDAccelerometerEventPrivate|HIDGenericGestureEvent|HIDGenericGestureEventPrivate|HIDAmbientLightSensorEvent|HIDAmbientLightSensorEventPrivate|HIDTouchSensitiveButtonEventPrivate|HIDPowerEventPrivate|HIDForceEvent|HIDForceEventPrivate|HIDMotionGestureEvent|HIDMotionGestureEventPrivate|HIDForceStageEventPrivate|HIDGameControllerEvent|HIDGameControllerEventPrivate|HIDDigitizerEvent|HIDDigitizerEventPrivate|HIDCompassEvent|HIDCompassEventPrivate|HIDMotionActivityEvent|HIDMotionActivityEventPrivate|HIDBrightnessEvent|HIDBrightnessEventPrivate|HIDGyroEvent|HIDGyroEventPrivate|HIDButtonEvent|HIDButtonEventPrivate|HIDAtmosphericPressureEvent|HIDAtmosphericPressureEventPrivate|HIDHumidityEventPrivate|HIDScrollEvent|HIDScrollEventPrivate|HIDBiometricEvent|HIDBiometricEventPrivate|HIDLEDEvent|HIDLEDEventPrivate|HIDOrientationEvent|HIDOrientationEventPrivate|HIDProximityEvent|HIDProximityEventPrivate|HIDKeyboardEvent|HIDKeyboardEventPrivate|HIDPointerEvent|HIDPointerEventPrivate)
- _objc_retain_x25
CStrings:
+ "!"
+ "!Ta"
+ "/System/Library/PrivateFrameworks/GamePolicy.framework/GamePolicy"
+ "/usr/lib/libRosetta.dylib"
+ "Built-In"
+ "CollectionCookie"
+ "Device is seized, reports will be dropped until the seizing client closes\n"
+ "DeviceUsagePairs"
+ "DuplicateIndex"
+ "ElementCookie"
+ "ElementCookieMax"
+ "ElementCookieMin"
+ "Failed to create IOHIDQueue plugin result: 0x%x\n"
+ "Failed to create queue\n"
+ "Failed to map memory: 0x%x\n"
+ "GPProcessMonitor"
+ "HasNullState"
+ "HasPreferredState"
+ "IOClass"
+ "IOConnectCallMethod(kIOHIDLibUserClientGetElementCount):%x\n"
+ "IOConnectCallMethod(kIOHIDLibUserClientGetElements):%x\n"
+ "IOConnectCallMethod(kIOHIDLibUserClientOpen):%x\n"
+ "IOHIDDeviceClass"
+ "IOHIDDeviceClass failed to retain service object with err %x\n"
+ "IOHIDDeviceForceInterfaceRematch"
+ "IOHIDDeviceSuspend"
+ "IOServiceOpen failed: 0x%x\n"
+ "IsArray"
+ "IsNonLinear"
+ "IsRelative"
+ "IsWrapping"
+ "Max"
+ "MaxReportBufferCount"
+ "Min"
+ "ReportBufferEntrySize"
+ "ReportCount"
+ "ReportID"
+ "ReportSize"
+ "ScaledMax"
+ "ScaledMin"
+ "Size"
+ "Transport"
+ "Unable to copy back value for element, unexpected cookie(%ld) expected:%d\n"
+ "Unable to copy back value for element, unexpected size(%d)\n"
+ "Unable to create queue analytics\n"
+ "UniqueID"
+ "Unit"
+ "UnitExponent"
+ "Unsupported matching criteria: %@ %@\n"
+ "Usage"
+ "UsageMax"
+ "UsageMin"
+ "UsagePage"
+ "UsagePercent"
+ "assertion failure: IOHIDEventSystem does not exist"
+ "assertion failure: Invalid object: instance is not a virtual event service"
+ "com.apple.hid.queueUsage"
+ "deviceQueue"
+ "dynamicButtonConfigurationGeneration"
+ "dynamicButtonConfigurationID"
+ "dynamicButtonForce"
+ "dynamicButtonNextThreshold"
+ "dynamicButtonPadID"
+ "dynamicButtonPositionID"
+ "dynamicButtonPositionY"
+ "dynamicButtonReleaseThreshold"
+ "dynamicButtonStageID"
+ "dynamicButtonThreshold"
+ "dynamicButtonTransition"
+ "dynamicButtonUsage"
+ "dynamicButtonUsagePage"
+ "element: %p type: %d uP: 0x%02x u: 0x%02x cookie: %d val: %ld"
+ "getValue(%#llx):%#x\n"
+ "isIdentifiedGame"
+ "kIOHIDLibUserClientPostElementValues(%#llx):%#x\n"
+ "kIOHIDLibUserClientPostElementValues(%llx):%x\n"
+ "kIOHIDLibUserClientResumeReports:%#x\n"
+ "kIOHIDLibUserClientUpdateElementValues(%#llx):%#x\n"
+ "monitorForCurrentProcess"
+ "queueType"
+ "rosetta_convert_to_rosetta_absolute_time"
+ "rosetta_is_current_process_translated"
+ "setValue(%#llx):%#x\n"
+ "staticSize"
+ "transport"
+ "usagePairs"
+ "v24@?0@\"GPProcessMonitor\"8@\"GPProcessInfo\"16"
+ "v32@?0@\"NSString\"8@\"NSNumber\"16^B24"
- "*16@0:8"
- ".cxx_destruct"
- "@\"<HIDVirtualEventServiceDelegate>\""
- "@\"HIDDevice\""
- "@\"HIDEventService\""
- "@\"HIDEventSystemClient\""
- "@\"HIDServiceClient\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"TSClockManager\""
- "@\"TSUserFilteredClock\""
- "@16@0:8"
- "@20@0:8I16"
- "@20@0:8i16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@32@0:8Q16I24I28"
- "@32@0:8Q16S24I28"
- "@32@0:8Q16o^@24"
- "@32@0:8q16@24"
- "@32@0:8q16o^@24"
- "@32@0:8r^v16q24"
- "@36@0:8I16Q20Q28"
- "@36@0:8Q16d24I32"
- "@40@0:8Q16I24C28I32I36"
- "@40@0:8Q16I24d28I36"
- "@40@0:8Q16S24S28I32I36"
- "@40@0:8Q16d24I32I36"
- "@44@0:8Q16d24d32I40"
- "@52@0:8Q16I24d28I36d40I48"
- "@52@0:8Q16S24S28I32*36I44I48"
- "@52@0:8Q16d24d32Q40I48"
- "@52@0:8Q16d24d32d40I48"
- "@56@0:8Q16I24d28d36d44I52"
- "@56@0:8Q16d24d32d40I48I52"
- "@60@0:8Q16d24d32d40d48I56"
- "@76@0:8Q16d24d32d40d48d56d64I72"
- "@?"
- "@?16@0:8"
- "AI"
- "Ai"
- "B"
- "B16@0:8"
- "B20@0:8I16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "B32@0:8@16o^@24"
- "B32@0:8q16o^@24"
- "B32@0:8q16q24"
- "B40@0:8@16@24@32"
- "B40@0:8@16Q24o^@32"
- "B40@0:8@16q24o^@32"
- "B40@0:8@?16@24o^@32"
- "B48@0:8@16o^@24q32@?40"
- "B56@0:8@16q24o^@32q40@?48"
- "B56@0:8^v16^q24q32q40o^@48"
- "B56@0:8r^v16q24q32q40o^@48"
- "B72@0:8^v16^q24q32q40o^@48q56@?64"
- "B72@0:8r^v16q24q32q40o^@48q56@?64"
- "C16@0:8"
- "HIDAccelerometerEvent"
- "HIDAccelerometerEventPrivate"
- "HIDAmbientLightSensorEvent"
- "HIDAmbientLightSensorEventPrivate"
- "HIDAtmosphericPressureEvent"
- "HIDAtmosphericPressureEventPrivate"
- "HIDBasicTimeSync"
- "HIDBiometricEvent"
- "HIDBiometricEventPrivate"
- "HIDBrightnessEvent"
- "HIDBrightnessEventPrivate"
- "HIDButtonEvent"
- "HIDButtonEventPrivate"
- "HIDCompassEvent"
- "HIDCompassEventPrivate"
- "HIDDigitizerEvent"
- "HIDDigitizerEventPrivate"
- "HIDEventDesc"
- "HIDEventSystemClient"
- "HIDForceEvent"
- "HIDForceEventPrivate"
- "HIDForceStageEventPrivate"
- "HIDFrameworkPrivate"
- "HIDGameControllerEvent"
- "HIDGameControllerEventPrivate"
- "HIDGenericGestureEvent"
- "HIDGenericGestureEventPrivate"
- "HIDGyroEvent"
- "HIDGyroEventPrivate"
- "HIDHumidityEventPrivate"
- "HIDKeyboardEvent"
- "HIDKeyboardEventPrivate"
- "HIDLEDEvent"
- "HIDLEDEventPrivate"
- "HIDManager"
- "HIDMotionActivityEvent"
- "HIDMotionActivityEventPrivate"
- "HIDMotionGestureEvent"
- "HIDMotionGestureEventPrivate"
- "HIDOrientationEvent"
- "HIDOrientationEventPrivate"
- "HIDPointerEvent"
- "HIDPointerEventPrivate"
- "HIDPowerEventPrivate"
- "HIDProximityEvent"
- "HIDProximityEventPrivate"
- "HIDScrollEvent"
- "HIDScrollEventPrivate"
- "HIDTemperatureEvent"
- "HIDTemperatureEventPrivate"
- "HIDTimeSync"
- "HIDTouchSensitiveButtonEventPrivate"
- "HIDTransaction"
- "HIDUserDevice"
- "HIDVendorDefinedEvent"
- "HIDVendorDefinedEventPrivate"
- "HIDVirtualEventService"
- "I16@0:8"
- "I24@0:8Q16"
- "IOReturn"
- "NSCopying"
- "Q16@0:8"
- "Q32@0:8@16o^@24"
- "S16@0:8"
- "T@\"<HIDVirtualEventServiceDelegate>\",W,V_delegate"
- "T@\"HIDElement\",R"
- "T@\"HIDEvent\",R"
- "T@\"HIDEventSystemClient\",&,V_client"
- "T@\"HIDServiceClient\",&,V_serviceClient"
- "T@\"NSArray\",R"
- "T@\"NSData\""
- "T@\"NSObject<OS_dispatch_queue>\",&,V_queue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "T@\"NSString\",R"
- "T@?,R,N,V_cancelHandler"
- "T@?,R,N,V_eventHandler"
- "TB,R"
- "TI"
- "TI,N"
- "TI,R"
- "TQ"
- "TQ,R"
- "Ti,R"
- "Tq"
- "Tq,R"
- "^v20@0:8I16"
- "^{?=Ib6b1b1*}16@0:8"
- "^{IONotificationPort=}"
- "^{__IOHIDEventSystemClient=}"
- "^{__IOHIDEventSystemClient=}16@0:8"
- "^{__IOHIDManager=}"
- "^{__IOHIDTransaction=}"
- "^{__IOHIDUserDevice=}"
- "^{__IOHIDValue=}16@0:8"
- "_activated"
- "_active"
- "_cancelHandler"
- "_client"
- "_clockID"
- "_delegate"
- "_device"
- "_deviceNotificationHandler"
- "_elementHandler"
- "_eventHandler"
- "_filterHandler"
- "_getReportHandler"
- "_handlerLock"
- "_inputReportHandler"
- "_manager"
- "_propertyChangedHandler"
- "_propertyNotify"
- "_propertyPort"
- "_queue"
- "_resetHandler"
- "_service"
- "_serviceClient"
- "_serviceHandler"
- "_setReportHandler"
- "_state"
- "_transaction"
- "_tsClock"
- "_tsMgr"
- "accelerometerEvent:x:y:z:options:"
- "activate"
- "addObject:"
- "allObjects"
- "ambientLightSensorEvent:level:options:"
- "appendEvent:"
- "arrayWithArray:"
- "arrayWithObjects:"
- "atmosphericPressureEvent:level:sequence:options:"
- "biometricEvent:eventType:level:options:"
- "brightnessEvent:currentBrightness:targetBrightness:transitionTime:options:"
- "buttonEvent:buttonMask:options:"
- "bytes"
- "cancel"
- "cancelHandler"
- "children"
- "client"
- "clockIdentifier"
- "clockWithClockIdentifier:"
- "close"
- "commitElements:direction:error:"
- "commitElements:direction:error:timeout:callback:"
- "commitElements:error:"
- "commitElements:error:timeout:callback:"
- "compassEvent:x:y:z:options:"
- "conformsToEventType:"
- "conformsToUsagePage:usage:"
- "convertFromDomainToMachAbsoluteTime:"
- "cookie"
- "copy"
- "copyEventMatching:forService:"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d16@0:8"
- "d20@0:8I16"
- "d24@0:8q16"
- "dataFromSyncedTime:error:"
- "dataValue"
- "dataValueForField:"
- "dataWithBytes:length:"
- "dealloc"
- "delegate"
- "description"
- "devices"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "digitizerEvent:transducerType:x:y:z:options:"
- "direction"
- "dispatchEvent:"
- "doubleValueForField:"
- "elementsMatching:"
- "enumerateFieldsWithBlock:"
- "errorWithDomain:code:userInfo:"
- "errorWithIOReturn:"
- "eventHandler"
- "eventMatching:"
- "eventStatistics"
- "findDevice"
- "findDeviceForServiceID:"
- "forceEvent:behavior:progress:stage:stageProgress:options:"
- "gameControllerEvent:controllerType:options:"
- "genericGestureEvent:gestureType:options:"
- "getAuditToken:"
- "getEventFields"
- "getReport:reportLength:withIdentifier:forType:error:"
- "getReport:reportLength:withIdentifier:forType:error:timeout:callback:"
- "gyroEvent:x:y:z:options:"
- "handleActivate"
- "handleCancel"
- "handlePropertyChange"
- "handlePropertyUpdate:"
- "handleReport:error:"
- "handleReport:withTimestamp:error:"
- "i16@0:8"
- "i32@0:8Q16Q24"
- "i40@0:8Q16Q24Q32"
- "init"
- "initInternal"
- "initWithBytes:length:"
- "initWithBytesNoCopy:length:freeWhenDone:"
- "initWithData:"
- "initWithDevice:"
- "initWithOptions:"
- "initWithProperties:"
- "initWithService:"
- "initWithType:"
- "initWithType:andAttributes:"
- "initWithType:timestamp:senderID:"
- "integerValue"
- "integerValueForField:"
- "isEqual:"
- "isEqualToHIDEvent:"
- "isEqualToString:"
- "isUserInput"
- "keyboardEvent:usagePage:usage:down:options:"
- "lEDEvent:ledMask:number:state:options:"
- "ledMask"
- "ledNumber"
- "ledState"
- "length"
- "lockState"
- "logicalMax"
- "logicalMin"
- "motionActivityEvent:activityType:confidence:options:"
- "motionGestureEvent:gestureType:progress:options:"
- "needsUngroupForLegacy"
- "newTestTimeSync"
- "notification:withProperty:forService:"
- "null"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "objectForKeyedSubscript:"
- "open"
- "openWithOptions:"
- "openWithOptions:error:"
- "options"
- "parent"
- "physicalMax"
- "physicalMin"
- "pointerEvent:x:y:z:buttonMask:options:"
- "polarDigitizerEvent:altitude:azimuth:quality:density:majorRadius:minorRadius:options:"
- "polarOrientationEvent:radius:azimuth:altitude:options:"
- "properties"
- "propertiesForKeys:"
- "propertyForKey:"
- "propertyForKey:forService:"
- "proximityEvent:detectionMask:options:"
- "q16@0:8"
- "q20@0:8I16"
- "qualityDigitizerEvent:quality:density:irregularity:majorRadius:minorRadius:accuracy:options:"
- "quaternionOrientationEvent:w:x:y:z:options:"
- "queue"
- "registerPropertyNotification:"
- "registerWithSystem"
- "removeAllEvents"
- "removeAllObjects"
- "removeEvent:"
- "removeObjectForKey:"
- "reportID"
- "reportSize"
- "scaleValue:"
- "scrollEvent:x:y:z:options:"
- "senderID"
- "serialize:error:"
- "service"
- "serviceClient"
- "serviceID"
- "services"
- "setAccelerometerSequence:"
- "setAccelerometerSubType:"
- "setAccelerometerType:"
- "setAccelerometerX:"
- "setAccelerometerY:"
- "setAccelerometerZ:"
- "setAmbientLightColorComponent0:"
- "setAmbientLightColorComponent1:"
- "setAmbientLightColorComponent2:"
- "setAmbientLightColorSpace:"
- "setAmbientLightDisplayBrightnessChanged:"
- "setAmbientLightSensorColorTemperature:"
- "setAmbientLightSensorIlluminance:"
- "setAmbientLightSensorLevel:"
- "setAmbientLightSensorRawChannel0:"
- "setAmbientLightSensorRawChannel1:"
- "setAmbientLightSensorRawChannel2:"
- "setAmbientLightSensorRawChannel3:"
- "setAtmosphericPressureLevel:"
- "setAtmosphericSequence:"
- "setBatchInputElementHandler:"
- "setBiometricEventType:"
- "setBiometricLevel:"
- "setBiometricTapCount:"
- "setBiometricUsage:"
- "setBiometricUsagePage:"
- "setButtonClickCount:"
- "setButtonMask:"
- "setButtonNumber:"
- "setButtonPressure:"
- "setButtonState:"
- "setCancelHandler:"
- "setClient:"
- "setCompassSequence:"
- "setCompassSubType:"
- "setCompassType:"
- "setCompassX:"
- "setCompassY:"
- "setCompassZ:"
- "setCurrentBrightness:"
- "setDataValue:"
- "setDelegate:"
- "setDeviceMatching:"
- "setDeviceNotificationHandler:"
- "setDigitizerAltitude:"
- "setDigitizerAuxiliaryPressure:"
- "setDigitizerAzimuth:"
- "setDigitizerButtonMask:"
- "setDigitizerChildEventMask:"
- "setDigitizerCollection:"
- "setDigitizerDensity:"
- "setDigitizerDidUpdateMask:"
- "setDigitizerEventMask:"
- "setDigitizerGenerationCount:"
- "setDigitizerIdentity:"
- "setDigitizerIndex:"
- "setDigitizerIrregularity:"
- "setDigitizerIsDisplayIntegrated:"
- "setDigitizerMajorRadius:"
- "setDigitizerMinorRadius:"
- "setDigitizerPressure:"
- "setDigitizerQuality:"
- "setDigitizerQualityRadiiAccuracy:"
- "setDigitizerRange:"
- "setDigitizerRoll:"
- "setDigitizerTiltX:"
- "setDigitizerTiltY:"
- "setDigitizerTouch:"
- "setDigitizerTwist:"
- "setDigitizerType:"
- "setDigitizerWillUpdateMask:"
- "setDigitizerX:"
- "setDigitizerY:"
- "setDigitizerZ:"
- "setDirection:"
- "setDispatchQueue:"
- "setDoubleValue:forField:"
- "setEventFilterHandler:"
- "setEventHandler:"
- "setForceBehavior:"
- "setForceProgress:"
- "setForceStage:"
- "setForceStageNextThreshold:"
- "setForceStageNormalizedForce:"
- "setForceStageNormalizedForceVelocity:"
- "setForceStagePressedThreshold:"
- "setForceStagePressure:"
- "setForceStageReleasedThreshold:"
- "setForceStageStage:"
- "setForceStageTransition:"
- "setGameControllerButtonL4:"
- "setGameControllerButtonM1:"
- "setGameControllerButtonM2:"
- "setGameControllerButtonM3:"
- "setGameControllerButtonM4:"
- "setGameControllerButtonR4:"
- "setGameControllerDirectionPadDown:"
- "setGameControllerDirectionPadLeft:"
- "setGameControllerDirectionPadRight:"
- "setGameControllerDirectionPadUp:"
- "setGameControllerFaceButtonA:"
- "setGameControllerFaceButtonB:"
- "setGameControllerFaceButtonX:"
- "setGameControllerFaceButtonY:"
- "setGameControllerJoyStickAxisRz:"
- "setGameControllerJoyStickAxisX:"
- "setGameControllerJoyStickAxisY:"
- "setGameControllerJoyStickAxisZ:"
- "setGameControllerShoulderButtonL1:"
- "setGameControllerShoulderButtonL2:"
- "setGameControllerShoulderButtonR1:"
- "setGameControllerShoulderButtonR2:"
- "setGameControllerThumbstickButtonLeft:"
- "setGameControllerThumbstickButtonRight:"
- "setGameControllerType:"
- "setGenericGestureTypeSwipeProgress:"
- "setGenericGestureTypeTapCount:"
- "setGetReportHandler:"
- "setGyroSequence:"
- "setGyroSubType:"
- "setGyroType:"
- "setGyroX:"
- "setGyroY:"
- "setGyroZ:"
- "setHumidityRH:"
- "setHumiditySequence:"
- "setInputElementHandler:"
- "setInputElementMatching:"
- "setInputReportHandler:"
- "setIntegerValue:"
- "setIntegerValue:forField:"
- "setKeyboardClickSpeed:"
- "setKeyboardDown:"
- "setKeyboardLongPress:"
- "setKeyboardMouseKeyToggle:"
- "setKeyboardPressCount:"
- "setKeyboardRepeat:"
- "setKeyboardSlowKeyPhase:"
- "setKeyboardStickyKeyPhase:"
- "setKeyboardStickyKeyToggle:"
- "setKeyboardUsage:"
- "setKeyboardUsagePage:"
- "setLedMask:"
- "setLedNumber:"
- "setLedState:"
- "setMatching:"
- "setMotionActivityActivityType:"
- "setMotionActivityConfidence:"
- "setMotionGestureGestureType:"
- "setMotionGestureProgress:"
- "setObject:forKeyedSubscript:"
- "setOptions:"
- "setOrientationAltitude:"
- "setOrientationAzimuth:"
- "setOrientationDeviceOrientationUsage:"
- "setOrientationQuatW:"
- "setOrientationQuatX:"
- "setOrientationQuatY:"
- "setOrientationQuatZ:"
- "setOrientationRadius:"
- "setOrientationTiltX:"
- "setOrientationTiltY:"
- "setOrientationTiltZ:"
- "setOutputEvent:forService:"
- "setPointerButtonMask:"
- "setPointerX:"
- "setPointerY:"
- "setPointerZ:"
- "setPowerMeasurement:"
- "setPowerSubType:"
- "setPowerType:"
- "setProbabilityLevel:"
- "setProperty:forKey:"
- "setProperty:forKey:and:"
- "setProperty:forKey:forService:"
- "setPropertyChangeHandler:forKey:error:"
- "setPropertyChangedHandler:matching:"
- "setProviderProperty:forKey:"
- "setProximityDetectionMask:"
- "setProximityLevel:"
- "setProximityProximityType:"
- "setQueue:"
- "setRemovalHandler:"
- "setReport:reportLength:withIdentifier:forType:error:"
- "setReport:reportLength:withIdentifier:forType:error:timeout:callback:"
- "setResetHandler:"
- "setScrollIsPixels:"
- "setScrollX:"
- "setScrollY:"
- "setScrollZ:"
- "setServiceClient:"
- "setServiceNotificationHandler:"
- "setSetReportHandler:"
- "setState:"
- "setTargetBrightness:"
- "setTemperatureLevel:"
- "setTimestamp:"
- "setTouchSensitiveButtonEventMask:"
- "setTouchSensitiveButtonMajorRadius:"
- "setTouchSensitiveButtonMinorRadius:"
- "setTouchSensitiveButtonNormalizedPositionDeltaX:"
- "setTouchSensitiveButtonNormalizedPositionDeltaY:"
- "setTouchSensitiveButtonNormalizedPositionX:"
- "setTouchSensitiveButtonNormalizedPositionY:"
- "setTouchSensitiveButtonTouch:"
- "setTouchSensitiveButtonUsage:"
- "setTouchSensitiveButtonUsagePage:"
- "setTransitionTime:"
- "setValueRef:"
- "setVendorDefinedUsage:"
- "setVendorDefinedUsagePage:"
- "setVendorDefinedVersion:"
- "setupPropertyNotifications"
- "sharedClockManager"
- "state"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "syncedTimeFromData:error:"
- "temperatureEvent:level:options:"
- "tiltDigitizerEvent:x:y:options:"
- "tiltOrientationEvent:x:y:z:options:"
- "timeSyncFromHIDDevice:"
- "timeSyncFromHIDEventService:"
- "timeSyncFromHIDServiceClient:"
- "timeSyncFromProtocol:"
- "timestamp"
- "type"
- "unit"
- "unitExponent"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "usage"
- "usagePage"
- "uuid"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v20@0:8I16"
- "v20@0:8S16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8^{?=[8I]}16"
- "v24@0:8^{__IOHIDValue=}16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8d16I24"
- "v28@0:8q16I24"
- "v32@0:8@?16@24"
- "valueRef"
- "vendorDefinedEvent:usagePage:usage:version:data:length:options:"
- "workIntervalCancel"
- "workIntervalFinish"
- "workIntervalStart:deadline:complexity:"
- "workIntervalUpdate:complexity:"
- "{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}"

```
