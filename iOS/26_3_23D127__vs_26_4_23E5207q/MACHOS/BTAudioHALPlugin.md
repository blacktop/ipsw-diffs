## BTAudioHALPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin`

```diff

-193.9.0.0.0
-  __TEXT.__text: 0x7b3e4
-  __TEXT.__auth_stubs: 0x12e0
-  __TEXT.__objc_stubs: 0x2720
+194.22.1.1.1
+  __TEXT.__text: 0x78d98
+  __TEXT.__auth_stubs: 0x12f0
+  __TEXT.__objc_stubs: 0x2700
   __TEXT.__init_offsets: 0xa0
-  __TEXT.__objc_methlist: 0x1164
-  __TEXT.__gcc_except_tab: 0x1fd4
-  __TEXT.__const: 0x185c
-  __TEXT.__cstring: 0x4a84
-  __TEXT.__oslogstring: 0x142cb
+  __TEXT.__objc_methlist: 0x1154
+  __TEXT.__gcc_except_tab: 0x2294
+  __TEXT.__const: 0x189c
+  __TEXT.__cstring: 0x4e65
+  __TEXT.__oslogstring: 0x14994
   __TEXT.__objc_classname: 0x155
-  __TEXT.__objc_methname: 0x3e7c
-  __TEXT.__objc_methtype: 0x120f
-  __TEXT.__unwind_info: 0x1a68
+  __TEXT.__objc_methname: 0x3e2c
+  __TEXT.__objc_methtype: 0x120c
+  __TEXT.__unwind_info: 0x1b10
   __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__auth_got: 0x980
+  __DATA_CONST.__auth_got: 0x988
   __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x4c30
+  __DATA_CONST.__const: 0x4c68
   __DATA_CONST.__cfstring: 0x1620
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0x1f48
-  __DATA.__objc_selrefs: 0xe08
-  __DATA.__objc_ivar: 0x184
+  __DATA.__objc_const: 0x1f08
+  __DATA.__objc_selrefs: 0xe00
+  __DATA.__objc_ivar: 0x17c
   __DATA.__objc_data: 0x410
   __DATA.__data: 0xb08
-  __DATA.__bss: 0x16f58
+  __DATA.__bss: 0x16f60
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 000532C9-7CE2-3657-9207-8BEF47819A5A
-  Functions: 2647
-  Symbols:   467
-  CStrings:  2994
+  UUID: 9FA05CD8-92E1-36EA-9364-F32D7F160811
+  Functions: 2708
+  Symbols:   468
+  CStrings:  3038
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_release_x23
+ _wmemchr
+ _xpc_connection_send_message_with_reply_sync
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
CStrings:
+ " not supported"
+ "/AppleInternal/Library/BuildRoots/4~CIZWugD3SYIfyzX9TZ6E2VDN61_FDBud-98IE44/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZWugD3SYIfyzX9TZ6E2VDN61_FDBud-98IE44/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "A2DPAudioDevice Invalidate"
+ "Accessory Communication DeviceUidString %s"
+ "Accessory Communication XPC Incoming Connection"
+ "Accessory Communication XPC Unexpected server event: %{public}s\n"
+ "Accessory Communication XPC cannot recover - not running in correct process"
+ "Accessory Communication XPC connection error: %{public}s"
+ "Accessory Communication XPC connection from %@"
+ "Accessory Communication XPC connection interrupted"
+ "Accessory Communication XPC connection invalid"
+ "Accessory Communication XPC incoming connection from %s %d"
+ "Accessory Communication XPC server invalid connection error: %{public}s\n"
+ "Accessory Communication XPC unexpected message type: %{public}s"
+ "Accessory Communication msgID %u"
+ "Audio Message %d from Audio Device UID: %s\n"
+ "AudioAccessoryMsgId3PPropertyChange"
+ "AudioAccessoryMsgId3PSupportedFeatures"
+ "AudioAccessoryMsgId3PSupportedFeaturesChange"
+ "BTAudioAccessoryDevice is NULL, Cannot process AAD message"
+ "BTAudioPersonalizedVolumeDevice::NotifyManualVolumeChanged manualVolumeUpdate %@ shouldUpdateBuds %d"
+ "BTUnifiedAudioDevice BT Address is not yet set"
+ "Client %s is not allowed to xpc into accessory communication service."
+ "Device Ownership kBTAudioMsgPropertyOwnershipEnabled is %u"
+ "Device supports ownership %u"
+ "Error Query3pBTProperties from reply"
+ "Error, 3rd Party Property Query Was Interrupted"
+ "Error, 3rd Party Property Query Was Invalidated"
+ "Failed to create accessory communication XPC server"
+ "FarfieldMic is %{public}s"
+ "High quality FarfieldMic is %s"
+ "High quality FarfieldMic is supported"
+ "PersonalHQTranslatorTransport"
+ "PrePublishHandler called for deviceType: %lld"
+ "Publish Message from Audio Device UID: %s\n"
+ "Received Additional Supported features"
+ "Received a dictionary with values %@"
+ "Registered audio plugin connection for accessory communication"
+ "Requesting 3rd Party Supported features to AudioAccessoryd"
+ "Starting XPC service for accessory communication"
+ "ThirdPartyAudioSwitching"
+ "Unhandled messageID received from AAD for 3rd Party Headset msgID : %llu"
+ "Unified Device is NULL"
+ "Unified Device is NULL, won't Request 3rd Party Supported Feature"
+ "UpdateAudioDeviceProperties Failed due to NULL AudioDevice"
+ "audioaccessoryd hasn't registered a connection"
+ "com.apple.AudioAccessoryCommunication.xpc"
+ "kBTAudioMsgFarfieldMicHQTransportSupported"
+ "kBTAudioMsgPropertyOwnershipEnabled"
+ "kBTAudioMsgPropertyOwnershipSupported"
- "@?"
- "BTAudioPersonalizedVolumeDevice::NotifyManualVolumeChanged _sendManualVolumeUpdate %d manualVolumeUpdate %@ shouldUpdateBuds %d"
- "BTUnifiedAudioDevice::startManualVolumeUpdateTimer: reached the time limit"
- "Publish Message from Audio Device UID: %@\n"
- "_manualUpdateDispatchBlock"
- "_sendManualVolumeUpdate"
- "startManualVolumeUpdateTimer"

```
