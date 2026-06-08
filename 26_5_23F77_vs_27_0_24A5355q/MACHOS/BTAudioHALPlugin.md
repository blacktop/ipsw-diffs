## BTAudioHALPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin`

```diff

-195.7.1.2.0
-  __TEXT.__text: 0x78b44
-  __TEXT.__auth_stubs: 0x12d0
-  __TEXT.__objc_stubs: 0x2700
+2700.37.0.0.0
+  __TEXT.__text: 0x76df4
+  __TEXT.__auth_stubs: 0x1370
+  __TEXT.__objc_stubs: 0x27e0
   __TEXT.__init_offsets: 0xa0
-  __TEXT.__objc_methlist: 0x1154
-  __TEXT.__gcc_except_tab: 0x2298
-  __TEXT.__const: 0x189c
-  __TEXT.__cstring: 0x4be1
-  __TEXT.__oslogstring: 0x149ae
-  __TEXT.__objc_classname: 0x155
-  __TEXT.__objc_methname: 0x3e2c
-  __TEXT.__objc_methtype: 0x120c
-  __TEXT.__unwind_info: 0x1b08
+  __TEXT.__objc_methlist: 0x11cc
+  __TEXT.__gcc_except_tab: 0x1f0c
+  __TEXT.__const: 0x18bc
+  __TEXT.__cstring: 0x4dea
+  __TEXT.__oslogstring: 0x15687
+  __TEXT.__objc_methname: 0x3f5f
+  __TEXT.__objc_classname: 0x154
+  __TEXT.__objc_methtype: 0x1257
+  __TEXT.__unwind_info: 0x1bb0
   __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__auth_got: 0x978
-  __DATA_CONST.__got: 0x2c8
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x4c68
-  __DATA_CONST.__cfstring: 0x1620
+  __DATA_CONST.__const: 0x4bd8
+  __DATA_CONST.__cfstring: 0x16a0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0x1f08
-  __DATA.__objc_selrefs: 0xe00
-  __DATA.__objc_ivar: 0x17c
+  __DATA_CONST.__auth_got: 0x9c8
+  __DATA_CONST.__got: 0x2c8
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA.__objc_const: 0x1f78
+  __DATA.__objc_selrefs: 0xe50
+  __DATA.__objc_ivar: 0x184
   __DATA.__objc_data: 0x410
   __DATA.__data: 0xb08
-  __DATA.__bss: 0x16f60
+  __DATA.__bss: 0x16f80
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: BC7A25A5-5728-3C40-99F9-B69782476ED1
-  Functions: 2708
-  Symbols:   466
-  CStrings:  3037
+  UUID: FF54D556-8EA9-32E4-AFAD-A2965C2D8250
+  Functions: 2749
+  Symbols:   476
+  CStrings:  3125
 
Symbols:
+ _CFStringHasSuffix
+ _dispatch_barrier_async
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _xpc_array_append_value
+ _xpc_array_get_count
CStrings:
+ "#Error BTAudioXpcConnection::Send3PSpatialSupportChanged null args"
+ "#Error BTAudioXpcConnection::Send3PSpatialSupportChanged null values[0]"
+ "-leca"
+ "A2DPAudioDevice::GetCalculateBufferFrameSize returning %d for HAL Request : %d"
+ "A2DPAudioDevice::GetCalculateBufferFrameSize with HAL Request : %d"
+ "Accessory.AudioPublish.XPC Received Message on Incoming Connection %s"
+ "AudioAccessoryMsgIdAADCommunicationStart"
+ "AudioAccessoryMsgIdReturnCurrentUSBDevices"
+ "AudioRoutingImprovementsForCarKits"
+ "BTAudioAVNotificationMonitor: Deallocation complete"
+ "BTAudioAVNotificationMonitor: Ignoring notification during deallocation"
+ "BTAudioAVNotificationMonitor: Main queue drained safely"
+ "BTAudioAVNotificationMonitor: Proceeding with deallocation despite timeout"
+ "BTAudioAVNotificationMonitor: Shutdown sequence complete"
+ "BTAudioAVNotificationMonitor: Starting deallocation"
+ "BTAudioAVNotificationMonitor: Starting shutdown sequence"
+ "BTAudioAVNotificationMonitor: Timeout waiting for _manualVolumeUpdatesQueue to drain"
+ "BTAudioAVNotificationMonitor: Timeout waiting for _mediaAVNotificationQueue to drain"
+ "BTAudioAVNotificationMonitor: Volume queue drained safely"
+ "BTAudioAVNotificationMonitor: Warning - shutdown() was not called before dealloc, calling now"
+ "BTDebug"
+ "BTStreamingHostDataGrid"
+ "CoreAudioServices"
+ "Detected"
+ "Enable3PSpatialAudioExtension_iOS"
+ "Failed adding USBC device due to bad deviceUID"
+ "Failed to inform audioaccessoryd as xpc connection is NULL"
+ "ForceInputOverAMP"
+ "Forcing Input over AMP due to defaults write"
+ "HFP Codec game with Call %d"
+ "HFPAudioDevice::GetCalculateBufferFrameSize returning %d for HAL Request : %d"
+ "HFPAudioDevice::GetCalculateBufferFrameSize with HAL Request : %d"
+ "HostGrid Anchor c:%llu,len:%u,Q:%f~%u,curr:%f,Seq:%x"
+ "HostGrid HFP threshold %d"
+ "HostGrid Q:%f~%u,S:%zu,ATs:%f,R:%zu"
+ "HostGrid Reset"
+ "HostGrid jumped back c:%llu,Q:%f~%u,curr:%f,ATs:%f"
+ "HostGrid jumped back history: currSampleTime[0..4]=%f,%f,%f,%f,%f"
+ "HostGrid jumped back history: mInQStartSampleTime[0..4]=%f,%f,%f,%f,%f"
+ "HostGrid jumped back history: mSessionAnchorSampleTime[0..4]=%f,%f,%f,%f,%f"
+ "HostGrid reA prevATs:%f,prevQ:%f~%u,drop:%f,Q:%f~%u,curr:%f,ATs:%f,Seq:%u , @ %llu"
+ "HostGrid should not come here c:%llu,Q:%f~%u,curr:%f,ATs:%f"
+ "Incompatible HID device connection status update: previous=%s, current=%s"
+ "Initial Incompatible HID device connection status: %{public}s"
+ "Missing bundleID, This is not expected.: return Spatial & HT disabled"
+ "Negotiated Frame Size,HAL Request : %d BTHAL Proposed %u for game"
+ "Not Detected"
+ "Not going to be relaunching %s due to com.apple.coreaudio BTDebug True"
+ "Received %s - %@"
+ "Received componentManufacturer: %s, componentType: %s, componentSubType: %s, componentFlags: %x, componentFlagsMask: %x"
+ "Received kBTAudioMsgPropertyInRangeDetected with value : %s"
+ "Remote Device In Range Supported %s"
+ "Returning %zu USB devices to audioaccessoryd"
+ "Send spatial support enabled %u"
+ "Shankar Received Unhandled Message on Server %@"
+ "TB,V_isBeingDeallocated"
+ "TI,N,V_deviceID"
+ "Update Remote Device In Range Support to %s"
+ "Update Supported Feature Dict : %@ : %@"
+ "UpdateSpatialPerAppMode BundleID invalid, skipping"
+ "Updated In Range State to %s"
+ "Wireless Splitter: unifiedDevice1 is %@ unifiedDevice2 is %@"
+ "[%{public}@] UpdateSpatialConfigChange called with nil bundleID, ignoring spatial config update"
+ "[%{public}@] UpdateSpatialConfigChange called with null accessory device"
+ "_isBeingDeallocated"
+ "cleanupResources"
+ "com.apple.accessory.AudioDevice.xpc"
+ "componentFlags"
+ "componentFlagsMask"
+ "componentManufacturer"
+ "componentSubType"
+ "componentType"
+ "connected"
+ "detected"
+ "disconnected"
+ "drainNotificationQueueSafely"
+ "getPropertyData: not enough space for the return value of kBluetoothAudioDevicePropertyRemoteDeviceInRangeDetected"
+ "getPropertyData: not enough space for the return value of kBluetoothAudioDevicePropertySpatialExtensionCompDescription"
+ "inChangeInfo is NULL, and can't process kAudioDevicePropertyLatency"
+ "inChangeInfo is NULL, and can't process kAudioDevicePropertyStreams"
+ "inChangeInfo is NULL, and can't process kBluetoothAudioDevicePropertyAudioContentType"
+ "isBeingDeallocated"
+ "kAccAudioMsgArgCurrentUSBDevices"
+ "kBTAudioMsgProperty3pSpatialSupport"
+ "kBTAudioMsgPropertyInRangeDetected"
+ "kBTAudioMsgPropertyInRangeDetectionSupported"
+ "kBTAudioMsgSpatialExtensionIdentifier"
+ "mAudioAccessorydConnection is NULL, cannot send USBDevicePublished"
+ "mCurrentAudioDevice is NULL, and can't process kAudioDevicePropertyStreams"
+ "not detected"
+ "peripheral:didCompleteChannelSoundingSession:"
+ "peripheral:didReceiveChannelSoundingProcedureResults:error:"
+ "removeAllNotificationListeners"
+ "setDeviceID:"
+ "setIsBeingDeallocated:"
+ "shutdown"
+ "v40@0:8@\"CBPeripheral\"16@\"CBChannelSoundingProcedureResults\"24@\"NSError\"32"
- "Auto"
- "BTAudioAVNotificationMonitor: dealloc"
- "FiedLeft"
- "HAL received kBTAudioMsgPropertyIncompatibleHidConnected:%u -> %u"
- "HFPAudioDevice InitializePublishedProperties no hid connect property, publish stereo"
- "HFPAudioDevice InitializePublishedProperties, mIncompatibleHidUpdateNeeded:%u"
- "HFPStereo game with Call %d"
- "Idle"
- "Updated Automatic Non HeadTracked Spatial : %d"
- "Updated Find My Playback : %d"
- "Updated Siri Use device Mic : %d"
- "left"
- "off head"
- "xpc_get_type(absoluteVolumeProp) == XPC_TYPE_BOOL"

```
