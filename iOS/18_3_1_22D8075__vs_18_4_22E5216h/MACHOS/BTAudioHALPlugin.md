## BTAudioHALPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin`

```diff

-183.9.1.1.7
-  __TEXT.__text: 0x6809c
-  __TEXT.__auth_stubs: 0x1130
-  __TEXT.__objc_stubs: 0x1980
-  __TEXT.__init_offsets: 0x98
-  __TEXT.__objc_methlist: 0x908
-  __TEXT.__gcc_except_tab: 0x1ac4
-  __TEXT.__const: 0x175c
-  __TEXT.__cstring: 0x3f2a
-  __TEXT.__oslogstring: 0x103e5
+184.40.0.0.0
+  __TEXT.__text: 0x697d4
+  __TEXT.__auth_stubs: 0x1210
+  __TEXT.__objc_stubs: 0x19e0
+  __TEXT.__init_offsets: 0x9c
+  __TEXT.__objc_methlist: 0xcb4
+  __TEXT.__gcc_except_tab: 0x1b0c
+  __TEXT.__const: 0x179c
+  __TEXT.__cstring: 0x426a
+  __TEXT.__oslogstring: 0x10d4e
   __TEXT.__objc_classname: 0x130
-  __TEXT.__objc_methname: 0x2bc7
-  __TEXT.__objc_methtype: 0x1199
-  __TEXT.__unwind_info: 0x1760
-  __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0x8a8
-  __DATA_CONST.__got: 0x2a0
+  __TEXT.__objc_methname: 0x2bf3
+  __TEXT.__objc_methtype: 0x1169
+  __TEXT.__unwind_info: 0x1770
+  __TEXT.__eh_frame: 0x50
+  __DATA_CONST.__auth_got: 0x918
+  __DATA_CONST.__got: 0x2a8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x39c8
-  __DATA_CONST.__cfstring: 0x1080
+  __DATA_CONST.__const: 0x4100
+  __DATA_CONST.__cfstring: 0x1160
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x1dd0
-  __DATA.__objc_selrefs: 0x810
+  __DATA.__objc_const: 0x16c8
+  __DATA.__objc_selrefs: 0xa00
   __DATA.__objc_ivar: 0xf8
   __DATA.__objc_data: 0x320
   __DATA.__data: 0xb08
-  __DATA.__bss: 0xae48
+  __DATA.__bss: 0xae68
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/AudioServerApplication.framework/AudioServerApplication
   - /System/Library/PrivateFrameworks/AudioServerDriver.framework/AudioServerDriver
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 2204
-  Symbols:   435
-  CStrings:  2200
+  Functions: 2263
+  Symbols:   450
+  CStrings:  2277
 
Symbols:
+ __xpc_type_connection
+ _getprogname
+ _objc_release_x28
+ _xpc_array_create
+ _xpc_array_set_string
+ _xpc_connection_activate
+ _xpc_connection_cancel
+ _xpc_connection_get_audit_token
+ _xpc_connection_get_pid
+ _xpc_connection_set_target_queue
+ _xpc_copy_code_signing_identity_for_token
+ _xpc_dictionary_create_reply
+ _xpc_dictionary_get_remote_connection
+ _xpc_dictionary_get_uint64
+ _xpc_retain
CStrings:
+ "#Error BTAudioXpcConnection::SendUSBCEnabled null args"
+ "#Error BTAudioXpcConnection::SendUSBCEnabled null values[0]"
+ "%@"
+ "%@-%u"
+ "AppleAudioAccessoryDevice XPC connection for UID %@ connected to[ %d ] "
+ "AppleAudioAccessoryDevice::GetPropertyData"
+ "AppleAudioAccessoryDevice::GetPropertyDataSize"
+ "AppleAudioAccessoryDevice::HasProperty"
+ "AppleAudioAccessoryDevice::IsPropertySettable"
+ "AppleAudioAccessoryDevice::SetPropertyData"
+ "Audio Accessory XPC Connection Error: %s"
+ "Audio Accessory XPC Incoming Connection"
+ "Audio Accessory XPC Unexpected msgID sent %d"
+ "Audio Accessory XPC Unexpected server event: %{public}s\n"
+ "Audio Accessory XPC cannot recover not running in correct process"
+ "Audio Accessory XPC connection from %@"
+ "Audio Accessory XPC server invalid connection error: %{public}s\n"
+ "AudioAccessoryMsgIdAirPlaneModeOff"
+ "AudioAccessoryMsgIdAirPlaneModeOn"
+ "AudioAccessoryMsgIdBTConnected"
+ "AudioAccessoryMsgIdBTNotPaired"
+ "AudioAccessoryMsgIdBTOff"
+ "AudioAccessoryMsgIdBTPaired"
+ "AudioAccessoryMsgIdHideUSBPort"
+ "AudioAccessoryMsgIdHostAddress"
+ "AudioAccessoryMsgIdReturnAllPublishedUIDs"
+ "AudioAccessoryMsgIdStartPairingProcess"
+ "AudioAccessoryMsgIdUSBMonitorStart"
+ "AudioAccessoryMsgIdUSBPropertyChanged"
+ "AudioAccessoryMsgIdUSBPublished"
+ "AudioAccessoryMsgIdUSBUnpublished"
+ "AudioAccessoryMsgIdUnHideUSBPort"
+ "B56@0:8@16{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}24@48"
+ "Client %s XPC connection already exists, clean up old connection object."
+ "Client %s XPC connection was successfully established. %s"
+ "Client %s is not allowed to xpc into this service."
+ "Defaults writes for unified usb device are missing"
+ "DeviceType is not a3d so notify"
+ "DeviceUidString %s"
+ "Error, did NOT find HAL device for UID: %s, handling msg\n"
+ "Failed to allocate LC3 48K Encoder"
+ "Failed to initialize A3D device"
+ "Found Published A2DP Device %@, adding it to the list."
+ "Found Published HFP Device %@, adding it to the list."
+ "Initialize AppleAudioAccessoryDevice"
+ "Overwritting safety offset due to USB to %u"
+ "Received msgID ReturnAllPublishedUIDs getting data. "
+ "Registered audio plugin connection with audioaccessoryd"
+ "RequestRouteChange, logging for kBluetoothAudioDeviceTypeA3D"
+ "Send USBC for Address: %@ Status: %d"
+ "Starting XPC service for audioaccessoryd"
+ "USBCUnifiedDevice"
+ "Unified USBC Transprt is %s"
+ "UpdateCurrentBTAudioDevice kBluetoothAudioDeviceTypeA3D returning early"
+ "XPC incoming connection from %s %d"
+ "audiomxd"
+ "bundleIdentifier"
+ "com.apple.BTAudioHALPluginAccessories"
+ "com.apple.audioaccessoryd"
+ "com.apple.cloudpaird"
+ "containsString:"
+ "coreaudiod"
+ "getPropertyData: not enough space for the return value of kBluetoothAudioDevicePropertyForceRouteChange"
+ "getPropertyData: not enough space for the return value of kBluetoothAudioDevicePropertyGameModeEnable"
+ "getPropertyData: not enough space for the return value of kBluetoothAudioDevicePropertyHearingAssistEnrollmentStatus"
+ "getPropertyData: not enough space for the return value of kBluetoothAudioDevicePropertyPMEStatus"
+ "getPropertyData: not enough space for the return value of kBluetoothAudioDevicePropertyPersonalizedVolumeDRCEnable"
+ "kBTAudioMsgArgAllPublishedUIDs"
+ "kBTAudioMsgPropertyFixedMicRole not present"
+ "kBTAudioMsgPropertyInEarEnabled not present"
+ "kBTAudioMsgPropertyPrimaryBudSide not present"
+ "kBTAudioMsgPropertyUnifiedUSBCTransport"
+ "kBTAudioMsgUnifiedUSBCBTAddress"
+ "kBTAudioMsgUnifiedUSBCDict"
+ "kBTAudioMsgUnifiedUSBCStatus"
+ "kBluetoothAudioDeviceTypeA3D"
+ "mainBundle"
+ "mediaserverd"
+ "v40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}16"
+ "v48@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}16@40"
- "B56@0:8@16{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}24@48"
- "v40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}16"
- "v48@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}16@40"

```
