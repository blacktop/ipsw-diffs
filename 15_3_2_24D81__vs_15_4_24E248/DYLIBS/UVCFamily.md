## UVCFamily

> `/System/Library/PrivateFrameworks/UVCFamily.framework/Versions/A/UVCFamily`

```diff

 466.80.2.0.0
-  __TEXT.__text: 0x1a3e0
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_methlist: 0xaa0
+  __TEXT.__text: 0x19424
+  __TEXT.__auth_stubs: 0x540
+  __TEXT.__objc_methlist: 0xc5c
   __TEXT.__const: 0xe0
   __TEXT.__cstring: 0x156f
   __TEXT.__oslogstring: 0x24fc
-  __TEXT.__gcc_except_tab: 0x694
-  __TEXT.__unwind_info: 0x4f8
+  __TEXT.__gcc_except_tab: 0x6a8
+  __TEXT.__unwind_info: 0x530
   __TEXT.__objc_classname: 0x1c5
   __TEXT.__objc_methname: 0x225a
   __TEXT.__objc_methtype: 0x8c5

   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7a8
+  __DATA_CONST.__objc_selrefs: 0x830
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x2a8
+  __AUTH_CONST.__auth_got: 0x2b0
   __AUTH_CONST.__const: 0x490
   __AUTH_CONST.__cfstring: 0x1180
-  __AUTH_CONST.__objc_const: 0x2b60
+  __AUTH_CONST.__objc_const: 0x2840
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x410

   - /System/Library/Frameworks/IOUSBHost.framework/Versions/A/IOUSBHost
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 03C2A88B-1F42-3B73-85BF-DB366D739E0F
-  Functions: 452
-  Symbols:   1143
+  UUID: 09FE2389-0BC6-3900-8ECB-BCD7203F93CE
+  Functions: 442
+  Symbols:   1122
   CStrings:  1103
 
Symbols:
+ -[UVCUSBDeviceStreamingInterface getStreamPipe:alternateSetting:].cold.1
+ GCC_except_table38
+ GCC_except_table53
+ UVCFamilyLog.cold.1
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ __MergedGlobals
+ _memcmp
+ convertTimeToNanoSec.cold.1
+ enableUVCSignpost.cold.1
+ getHostTimeInNanoSec.cold.1
+ uvcDebugLogEnabled.cold.1
- -[UVCDeviceControl initWithAttributes:type:entityID:delegate:].cold.1
- -[UVCDeviceControl parseControl].cold.1
- -[UVCDeviceControl parseControl].cold.2
- -[UVCDeviceControl parseControl].cold.3
- -[UVCDeviceControl parseControl].cold.4
- -[UVCDeviceControl setCurrentValue:error:].cold.1
- -[UVCDeviceControl setCurrentValue:error:].cold.2
- -[UVCDeviceControl setCurrentValue:error:].cold.3
- -[UVCUSBDevice getConfigurationDescriptorForInterface:].cold.1
- -[UVCUSBDevice getConfigurationDescriptorForInterface:].cold.2
- -[UVCUSBDevice getUSBInterfaceServiceForMatching:].cold.1
- -[UVCUSBDevice getUSBInterfaceServiceForMatching:].cold.2
- -[UVCUSBDevice getUSBInterfaceServiceForMatching:].cold.3
- -[UVCUSBDevice getUSBInterfaceServiceForMatching:].cold.4
- -[UVCUSBDevice initWithInterface:queue:streamDataHandler:stateNotificationHandler:].cold.1
- -[UVCUSBDevice setupWithAssociation:hostDevice:].cold.1
- -[UVCUSBDevice setupWithAssociation:hostDevice:].cold.2
- -[UVCUSBDevice setupWithAssociation:hostDevice:].cold.3
- -[UVCUSBDeviceControlInterface handleControlInterruptData:].cold.1
- -[UVCUSBDeviceControlInterface handleInterruptData:].cold.1
- -[UVCUSBDeviceControlInterface handleStreamInterruptData:].cold.1
- -[UVCUSBDeviceControlInterface initWithInterface:stateHandler:attributes:].cold.1
- -[UVCUSBDeviceInterface initWithInterface:attributes:].cold.1
- -[UVCUSBDeviceInterface parseConfigurationDescriptor].cold.1
- -[UVCUSBDeviceStreamingInterface doIsochStream:streamFormat:frameInterval:error:].cold.1
- -[UVCUSBDeviceStreamingInterface doProbeControl:frameRate:probeData:error:].cold.1
- -[UVCUSBDeviceStreamingInterface doProbeControl:frameRate:probeData:error:].cold.2
- -[UVCUSBDeviceStreamingInterface initWithInterface:stateHandler:dataHandler:attributes:].cold.1
- -[UVCUSBDeviceStreamingInterface initWithInterface:stateHandler:dataHandler:attributes:].cold.2
- -[UVCUSBDeviceStreamingInterface initWithInterface:stateHandler:dataHandler:attributes:].cold.3
- -[UVCVirtualDevice parseConfigurationDescriptor:configurationDescriptor:].cold.1
- -[UVCVirtualDevice parseConfigurationDescriptor:configurationDescriptor:].cold.2
- -[UVCVirtualDevice parseInterfaceDescriptor:configurationDescriptor:].cold.1
- -[UVCVirtualDevice parseInterfaceDescriptor:configurationDescriptor:].cold.2
- _cameraTerminalControls
- _encodingUnitControls
- _processingUnitControls
- createControls.cold.1
- createControls.cold.10
- createControls.cold.11
- createControls.cold.12
- createControls.cold.13
- createControls.cold.14
- createControls.cold.15
- createControls.cold.16
- createControls.cold.2
- createControls.cold.3
- createControls.cold.4
- createControls.cold.5
- createControls.cold.6
- createControls.cold.7
- createControls.cold.8
- createControls.cold.9
- getDiscreteFrameBasedFrameIntervals.cold.1
- getDiscreteFrameIntervals.cold.1

```
