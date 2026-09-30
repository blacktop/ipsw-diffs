## BTAudioHALPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/Contents/MacOS/BTAudioHALPlugin`

```diff

-184.42.0.3.0
-  __TEXT.__text: 0x880e4
-  __TEXT.__auth_stubs: 0x11d0
-  __TEXT.__objc_stubs: 0x1e20
+185.4.0.0.0
+  __TEXT.__text: 0x7f30c
+  __TEXT.__auth_stubs: 0x1160
+  __TEXT.__objc_stubs: 0x11a0
   __TEXT.__init_offsets: 0xa8
-  __TEXT.__objc_methlist: 0xc9c
-  __TEXT.__gcc_except_tab: 0x2534
-  __TEXT.__const: 0x1a0c
-  __TEXT.__cstring: 0x4bb8
-  __TEXT.__oslogstring: 0x156e9
-  __TEXT.__objc_classname: 0x113
-  __TEXT.__objc_methname: 0x292b
-  __TEXT.__objc_methtype: 0x76c
-  __TEXT.__unwind_info: 0x1c48
+  __TEXT.__objc_methlist: 0x824
+  __TEXT.__gcc_except_tab: 0x219c
+  __TEXT.__const: 0x19cc
+  __TEXT.__cstring: 0x47e7
+  __TEXT.__oslogstring: 0x141cf
+  __TEXT.__objc_classname: 0xee
+  __TEXT.__objc_methname: 0x181d
+  __TEXT.__objc_methtype: 0x6ff
+  __TEXT.__unwind_info: 0x1aa8
   __TEXT.__eh_frame: 0xa8
-  __DATA_CONST.__auth_got: 0x8f8
-  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__auth_got: 0x8c0
+  __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x6278
-  __DATA_CONST.__cfstring: 0x15c0
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__const: 0x5ee8
+  __DATA_CONST.__cfstring: 0x1300
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x48
-  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x1678
-  __DATA.__objc_selrefs: 0xa18
-  __DATA.__objc_ivar: 0x138
-  __DATA.__objc_data: 0x370
+  __DATA.__objc_const: 0xe38
+  __DATA.__objc_selrefs: 0x658
+  __DATA.__objc_ivar: 0xb0
+  __DATA.__objc_data: 0x280
   __DATA.__data: 0xaa8
-  __DATA.__bss: 0xaef0
+  __DATA.__bss: 0xaec8
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2820
-  Symbols:   418
-  CStrings:  2718
+  Functions: 2652
+  Symbols:   409
+  CStrings:  2364
 
Symbols:
- _OBJC_CLASS_$_ASAControl
- _OBJC_CLASS_$_ASACoreAudio
- _TextToHardwareAddress
- _dispatch_queue_attr_make_with_autorelease_frequency
- _objc_setProperty_nonatomic_copy
- _xpc_array_set_uint64
- _xpc_connection_send_message_with_reply
- _xpc_dictionary_get_bool
- _xpc_dictionary_set_bool
CStrings:
- " NOT Streaming"
- " Streaming "
- "%02llX"
- "00:00:00:00:00:00"
- "11:11:22:33:44:55"
- "@\"ASAAudioDevice\""
- "@\"NSArray\""
- "@\"NSNumber\""
- "@\"USBMetric\""
- "A2DP SETUP Overwritting latency from %d to %d due to USBC setting up"
- "A2DP USB Overwritting latency from %d to %d due to USBC"
- "ADDING A USB DEVICE, No need to remove any device"
- "Adding USBC device with id:%@ %p"
- "All USB devices are gone, cleanup. Count of total USB devices found %lu"
- "BT connected, nothing to do here. Move on..."
- "BT is NOT paired!"
- "BT is off. Unhide USB-C port"
- "BT paired not connected, let's wait for publishing of A2DP port."
- "BT power state is off, continue with sending correct state %@"
- "BT state changed, BT is %s USB-C needs to be %s"
- "BTAddress is %@"
- "BTUnifiedAudioDevice: %d"
- "BTUnifiedAudioDevice: Connected device %@, unified device is %@"
- "BTUnifiedAudioDevice: Defaults writes for unified usb device are missing"
- "BTUnifiedAudioDevice: Disconnecting %@, unified address is %@"
- "BTUnifiedAudioDevice: Not a genuine Airpods, do not establish unified audio"
- "BTUnifiedAudioDevice: Setup unified audio device"
- "BTUnifiedAudioDevice: syncVolumeWithUSBC Found device matching %@"
- "BTUnifiedAudioDevice: syncVolumeWithUSBC Setting volume %f on device %@ propertySize %d"
- "BTUnifiedAudioDevice: syncVolumeWithUSBC no kAudioObjectPropertyControlList property"
- "BTUnifiedAudioDevice:Found device matching %@"
- "BTUnifiedAudioDevice:No USB devices found"
- "BTUnifiedAudioDevice:Setting %s on device %@"
- "BTUnifiedAudioDevice:syncVolumeWithUSBC volume applied on control %@"
- "Bluetooth not connected yet; Forcing reconfig %@"
- "Calling BTHAL for BTAddress : %@ and state : %d"
- "Calling SendUSBEnabled on XPC from AppleAudioAccessoryDevice"
- "Can't sync volume with usbc, invalid device"
- "Checking if we need to remove devices"
- "Connected USB device with ID %@ disable airplane mode"
- "Connected USB device with ID %@ enable airplane mode on."
- "Connected USB device with ID %@ hide it."
- "Connected USB device with ID %@ unhide it."
- "Created hostSideUSBInfo %@"
- "Current active USB-C device %{private}@ stream state changed to %@"
- "Delayed Control Centre Update on USBC: Cancelling current Dispatch"
- "Device Address: %@ for index: %ld, btAddr: %@"
- "Device doesn't have USB latency!!!"
- "Device doesn't have USB safetyOffset!!!"
- "Device is already hidden nothing to do."
- "Didn't get a message we can understand"
- "Dropping volume update from %d volume for %@ is %f"
- "Error AudioAccessoryMsgIdHostAddress from reply"
- "Error AudioAccessoryMsgIdUSBPublished from reply"
- "Error, AudioAccessoryMsgIdHostAddress was Invalidated"
- "Error, AudioAccessoryMsgIdHostAddress was interrupted."
- "Error, AudioAccessoryMsgIdUSBPublished was Invalidated"
- "Error, AudioAccessoryMsgIdUSBPublished was interrupted."
- "Error, Invalid XPC connection, return"
- "Error, sending unknown to BTHAL for BTAddress : %@"
- "Error, unable to pair to device %@"
- "Error, unable to read AUAPropertySelectorDeviceBluetoothAddress."
- "Error, unable to read kAudioDevicePropertyDeviceIsRunningSomewhere."
- "Force reconfig"
- "ForceRoute RECONFIG due to USB-C updating to UID %@"
- "ForceRoute Reconfigure comparing USB-C connected device %@ to device %@"
- "Found USB device with modelName %@ and boxUID %@ %@"
- "Found device UID: %@"
- "Genuine AirPods forcing reconfig %@"
- "GetLosslessUSBID %@"
- "GetMyBTAddress %@"
- "Got stream state for non-routed device %{private}@  current routed device is %{private}@ stream state changed to %@"
- "HIDING device with UID %@"
- "Hidden"
- "Initiating pairing process with %@"
- "Invalid address passed through xpc!"
- "MUTE COMMAND"
- "NOT Genuine AirPods dropping connection %@"
- "NULL"
- "No USB device connected"
- "Not able to create hostSideUSBInfo due to  err=%d"
- "Not streaming usbc audio as wireless splitter is enabled"
- "NotHidden"
- "Q"
- "REMOVING A USB DEVICE with BT_UID %@ usbUID is %@"
- "Received reply to start USB monitoring  %@"
- "Received usb BT information %@"
- "Remove listeners for device with id%@"
- "Sending Delayed Control Center update for updating Spatial UI on USBC"
- "SetLosslessUSBID %@"
- "SetMyBTAddress %@"
- "Setting dictionary of %@ on the 515c USB device"
- "Setting host side address as 0x%.2x:%.2x:%.2x:%.2x:%.2x:%.2x"
- "Something went wrong both address and USB UID are null"
- "Something went wrong bt address is void"
- "Start monitoring USB routes."
- "Stop USB routes changed under device  %d"
- "T@\"ASAAudioDevice\",&,N,V_usbDevice"
- "T@\"NSArray\",C,N,V_fwVersion"
- "T@\"NSMutableDictionary\",&,N,V_hostSideUSBInfo"
- "T@\"NSMutableDictionary\",&,N,V_usbAudioDeviceList"
- "T@\"NSNumber\",C,N,V_color"
- "T@\"NSNumber\",C,N,V_featureBitmask"
- "T@\"NSNumber\",C,N,V_pairingMode"
- "T@\"NSNumber\",C,N,V_pid"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_usbQueue"
- "T@\"NSString\",C,N,V_btAddress"
- "T@\"NSString\",C,N,V_currentBTDeviceUID"
- "T@\"NSString\",C,N,V_currentRoutedUSBDeviceUID"
- "T@\"NSString\",C,N,V_modelID"
- "T@\"NSString\",C,N,V_name"
- "T@\"NSString\",C,N,V_usbUID"
- "T@\"USBMetric\",&,N,V_usbMetric"
- "TB,N,V_btPowerState"
- "TB,N,V_currentRoutedDeviceIsUnified"
- "TB,N,V_currentRoutedUSBDeviceStreaming"
- "TB,N,V_isCurrentRoute"
- "TB,N,V_isStreaming"
- "TI,N,V_safetyOffset"
- "TI,N,V_usbLatency"
- "TQ,N,V_usbIOStartTs"
- "TQ,N,V_usbRoutedTs"
- "Telling audioaccessoryd USB-C Device is PUBLISHED with UID %{private}@ is connected with BT address %{private}@"
- "Telling audioaccessoryd USB-C Device is UNPUBLISHED with UID %{private}@ is with BT address %{private}@"
- "Telling audioaccessoryd USB-C stream state changed"
- "Telling audioaccessoryd device %@ is AirPlane Mode Off"
- "Telling audioaccessoryd device %@ is AirPlane Mode On"
- "Telling audioaccessoryd device %@ is ready to pair"
- "Ti,N,V_audioTypeDuringPlugin"
- "Ti,N,V_durationPlaybackUnifiedAudio"
- "Ti,N,V_durationRoutedUnifiedAudio"
- "Ti,N,V_spatialStatusLongestDurationUnifiedAudio"
- "Ti,N,V_totalCountBTOnly"
- "Ti,N,V_totalCountCallUnifiedAudio"
- "Ti,N,V_totalCountSiriUnifiedAudio"
- "Ti,N,V_totalCountUSBCOnly"
- "Ti,N,V_totalCountUnifiedAudio"
- "Trying to reconfig %@"
- "UNHIDING device with UID %@"
- "UNMUTE COMMAND"
- "USB-C Error unable to create host info"
- "USB-C Stats '%@'  '%@' sent to CoreAnalytics with result %u"
- "USBC PerformConfigChange A2DP route is valid"
- "USBC PerformConfigChange, mCurrentAudioDevice %p, mHeadphoneAudioDevice %p, ref %p mA2DPAudioDevice %p, mHFPAudioDevice %p"
- "USBCManager"
- "USBDevice"
- "USBDeviceManager"
- "USBMetric"
- "Unable to find device with BT Address %@"
- "Updating A2DP latency to the new USB latency %u"
- "Updating A2DP outputSafetyOffset to USB %u"
- "Updating Host Address %s"
- "_audioTypeDuringPlugin"
- "_btAddress"
- "_btPowerState"
- "_color"
- "_currentBTDeviceUID"
- "_currentRoutedDeviceIsUnified"
- "_currentRoutedUSBDeviceStreaming"
- "_currentRoutedUSBDeviceUID"
- "_durationPlaybackUnifiedAudio"
- "_durationRoutedUnifiedAudio"
- "_featureBitmask"
- "_fwVersion"
- "_hostSideUSBInfo"
- "_isCurrentRoute"
- "_isStreaming"
- "_modelID"
- "_name"
- "_pairingMode"
- "_pid"
- "_safetyOffset"
- "_spatialStatusLongestDurationUnifiedAudio"
- "_totalCountBTOnly"
- "_totalCountCallUnifiedAudio"
- "_totalCountSiriUnifiedAudio"
- "_totalCountUSBCOnly"
- "_totalCountUnifiedAudio"
- "_usbAudioDeviceList"
- "_usbDevice"
- "_usbIOStartTs"
- "_usbLatency"
- "_usbMetric"
- "_usbQueue"
- "_usbRoutedTs"
- "_usbUID"
- "addUSBAudioDevice:withModelID:"
- "appendString:"
- "audioDeviceObjectIDs"
- "audioDevices"
- "audioTypeDuringPlugin"
- "boxUID"
- "boxes"
- "btAddress"
- "btPowerState"
- "bt_addr"
- "bt_pid"
- "cleanUSBInformation"
- "color"
- "com.apple.Bluetooth.USBCInfo"
- "currentBTDeviceUID"
- "currentRoutedDeviceIsUnified"
- "currentRoutedUSBDeviceStreaming"
- "currentRoutedUSBDeviceUID"
- "deviceUID"
- "disableAirPlaneModeForUSBPortWithUID:"
- "durationPlaybackUnifiedAudio"
- "durationRoutedUnifiedAudio"
- "enableAirPlaneModeForUSBPortWithUID:"
- "featureBitmask"
- "feature_bitmask"
- "fwVersion"
- "fw_vers"
- "getMainGlobalProperty:withData:ofSize:withQualifier:ofSize:"
- "getMainOutputProperty:withData:ofSize:withQualifier:ofSize:"
- "getPropertyData: not enough space for the return value of kBluetoothAudioDevicePropertyAlternateTransport"
- "getUSBColor:"
- "getUSBFWVersion:"
- "getUSBFeatureBitmask:"
- "getUSBModelID:"
- "getUSBName:"
- "getUSBPairingMode:"
- "getUSBPid:"
- "hasMainOutputProperty:"
- "hasProperty:scope:ofElement:"
- "hideUSBPortWithUID:UpdateAirPodsState:"
- "hostSideUSBInfo"
- "initWithAudioObjectID:"
- "initWithBTAddress:"
- "initWithUnsignedInt:"
- "isAcquired"
- "isCurrentRoute"
- "isMainGlobalPropertySettable:"
- "isStreaming"
- "kAccAudioMsgArgBTAddress"
- "kAccAudioMsgArgUSBColor"
- "kAccAudioMsgArgUSBDeviceAirPlaneModeOff"
- "kAccAudioMsgArgUSBDeviceAirPlaneModeOn"
- "kAccAudioMsgArgUSBDeviceBTAddress"
- "kAccAudioMsgArgUSBDeviceHiddenState"
- "kAccAudioMsgArgUSBDevicePairingState"
- "kAccAudioMsgArgUSBDeviceStreamingState"
- "kAccAudioMsgArgUSBFeatureBitMask"
- "kAccAudioMsgArgUSBFwVersion"
- "kAccAudioMsgArgUSBHostBTAddress"
- "kAccAudioMsgArgUSBID"
- "kAccAudioMsgArgUSBModelID"
- "kAccAudioMsgArgUSBName"
- "kAccAudioMsgArgUSBPairingMode"
- "kAccAudioMsgArgUSBPid"
- "longLongValue"
- "modelID"
- "modelName"
- "needToRemoveUSBDeviceFromList:"
- "objectAtIndexedSubscript:"
- "onQueue:forMainGlobalProperty:addListener:"
- "onQueue:forMainGlobalProperty:removeListener:"
- "onQueue:forProperty:scope:ofElement:addListener:"
- "onQueue:forProperty:scope:ofElement:removeListener:"
- "outputLatency"
- "outputSafetyOffset"
- "pairingMode"
- "playbackOverUSBChanged changed"
- "playbackOverUSBChanged:"
- "processUSBDeviceBluetoothInformation:withBTAddress:"
- "propertyChangeBTAddress changed"
- "propertyChangeBTAddress:"
- "registerUSBDeviceNotification:"
- "removeUSBAudioDevice:"
- "safetyOffset"
- "sendPingToUSBDevice:"
- "sendUSBcMetric"
- "setAcquired:"
- "setAudioTypeDuringPlugin:"
- "setBtAddress:"
- "setBtPowerState:"
- "setColor:"
- "setCurrentBTDeviceUID:"
- "setCurrentRoutedDeviceIsUnified:"
- "setCurrentRoutedUSBDeviceStreaming:"
- "setCurrentRoutedUSBDeviceUID:"
- "setDurationPlaybackUnifiedAudio:"
- "setDurationRoutedUnifiedAudio:"
- "setFeatureBitmask:"
- "setFwVersion:"
- "setHostSideUSBInfo:"
- "setIsCurrentRoute:"
- "setIsStreaming:"
- "setMainGlobalProperty:withData:ofSize:withQualifier:ofSize:"
- "setMainOutputProperty:withData:ofSize:withQualifier:ofSize:"
- "setModelID:"
- "setName:"
- "setPairingMode:"
- "setPid:"
- "setSafetyOffset:"
- "setSpatialStatusLongestDurationUnifiedAudio:"
- "setTotalCountBTOnly:"
- "setTotalCountCallUnifiedAudio:"
- "setTotalCountSiriUnifiedAudio:"
- "setTotalCountUSBCOnly:"
- "setTotalCountUnifiedAudio:"
- "setUSBcUnified, ForceRoute Reconfigure due to USB-C being gone"
- "setUSBcUnified, ForceRoute Reconfigure due to USB-C updating to UID %@"
- "setUsbAudioDeviceList:"
- "setUsbDevice:"
- "setUsbIOStartTs:"
- "setUsbLatency:"
- "setUsbMetric:"
- "setUsbQueue:"
- "setUsbRoutedTs:"
- "setUsbUID:"
- "sharedCoreAudioObject"
- "sizeOfMainOutputProperty:withQualifier:ofSize:"
- "source"
- "spatialStatusLongestDurationUnifiedAudio"
- "startPairingProcess:"
- "totalCountBTOnly"
- "totalCountCallUnifiedAudio"
- "totalCountSiriUnifiedAudio"
- "totalCountUSBCOnly"
- "totalCountUnifiedAudio"
- "unHideUSBPortWithUID:UpdateAirPodsState:"
- "unsignedLongValue"
- "updateHostSideInfo"
- "updateHostSideLocalBTAddress:withState:"
- "usbAudioDeviceList"
- "usbDevice"
- "usbIOStartTs"
- "usbLatency"
- "usbMetric"
- "usbQueue"
- "usbRoutedTs"
- "usbUID"
- "v20@0:8I16"
- "v24@0:8Q16"
- "v32@0:8@16^{__CFDictionary=}24"
- "v32@?0@\"NSString\"8@\"USBDevice\"16^B24"

```
