## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

```diff

-1267.332.0.0.0
-  __TEXT.__text: 0x4b7834
-  __TEXT.__auth_stubs: 0x25d0
-  __TEXT.__objc_stubs: 0x980
-  __TEXT.__init_offsets: 0x4c4
-  __TEXT.__objc_methlist: 0x31c
-  __TEXT.__const: 0xb10d6
-  __TEXT.__gcc_except_tab: 0x56e54
-  __TEXT.__oslogstring: 0x4e2be
-  __TEXT.__cstring: 0x27fcf
-  __TEXT.__objc_methname: 0xd93
-  __TEXT.__objc_classname: 0x7b
-  __TEXT.__objc_methtype: 0xb71
+1267.336.0.0.0
+  __TEXT.__text: 0x48b738
+  __TEXT.__auth_stubs: 0x2500
+  __TEXT.__objc_stubs: 0x760
+  __TEXT.__init_offsets: 0x4c0
+  __TEXT.__objc_methlist: 0x134
+  __TEXT.__gcc_except_tab: 0x540ac
+  __TEXT.__const: 0xb07be
+  __TEXT.__cstring: 0x2767a
+  __TEXT.__objc_classname: 0x34
   __TEXT.__swift5_typeref: 0x133
   __TEXT.__swift5_capture: 0x158
+  __TEXT.__oslogstring: 0x4cd6e
+  __TEXT.__objc_methname: 0x5db
   __TEXT.__constg_swiftt: 0xf8
   __TEXT.__swift5_reflstr: 0x4c
   __TEXT.__swift5_fieldmd: 0x68
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x8
+  __TEXT.__objc_methtype: 0x22f
   __TEXT.__dof_VirtualAu: 0x303
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0xff08
+  __TEXT.__unwind_info: 0xf2f0
   __TEXT.__eh_frame: 0x7a8
-  __DATA_CONST.__auth_got: 0x1300
-  __DATA_CONST.__got: 0x498
-  __DATA_CONST.__auth_ptr: 0x78
-  __DATA_CONST.__const: 0x241c8
-  __DATA_CONST.__cfstring: 0x3c40
-  __DATA_CONST.__objc_classlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__auth_got: 0x1298
+  __DATA_CONST.__got: 0x448
+  __DATA_CONST.__auth_ptr: 0x70
+  __DATA_CONST.__const: 0x23db8
+  __DATA_CONST.__cfstring: 0x39c0
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x20
-  __DATA.__objc_const: 0xc60
-  __DATA.__objc_selrefs: 0x370
-  __DATA.__objc_ivar: 0x24
-  __DATA.__objc_data: 0x308
-  __DATA.__data: 0x508
-  __DATA.__bss: 0x20e08
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA.__objc_const: 0x398
+  __DATA.__objc_selrefs: 0x210
+  __DATA.__objc_ivar: 0x18
+  __DATA.__objc_data: 0x268
+  __DATA.__data: 0x338
+  __DATA.__bss: 0x211a0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /System/Library/PrivateFrameworks/CPMS.framework/CPMS
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
+  - /System/Library/PrivateFrameworks/CiderAudioServer.framework/CiderAudioServer
   - /System/Library/PrivateFrameworks/IAP.framework/IAP
   - /System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices
   - /System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10194
-  Symbols:   750
-  CStrings:  10798
+  Functions: 9832
+  Symbols:   727
+  CStrings:  10493
 
Symbols:
+ _OBJC_CLASS_$_CiderService
- _NSStringFromClass
- _NSStringFromSelector
- _OBJC_CLASS_$_NSArray
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSError
- _OBJC_CLASS_$_NSNumber
- _OBJC_CLASS_$_NSURL
- _OBJC_CLASS_$_NSXPCInterface
- _OBJC_CLASS_$_NSXPCListener
- __ZNKSt3__123__match_any_but_newlineIcE6__execERNS_7__stateIcEE
- __ZNKSt3__16locale4nameEv
- __ZNSt3__111regex_errorC1ENS_15regex_constants10error_typeE
- __ZNSt3__111regex_errorD1Ev
- __ZNSt3__115__get_classnameEPKcb
- __ZNSt3__120__get_collation_nameEPKc
- __ZNSt3__16localeC1ERKS0_
- __ZNSt3__16localeC1Ev
- __ZNSt3__17collateIcE2idE
- __ZTINSt3__111regex_errorE
- ___cxa_atexit
- _objc_opt_isKindOfClass
- _objc_retainBlock
- _objc_retain_x3
- _objc_retain_x5
CStrings:
+ "@@ Strips Oct 23 2024 22:57:49"
+ "Device_HAL_Common.mm"
+ "IsSimulatedDevice:"
+ "SendRouteConfiguration:withError:"
+ "ServiceIsRunning"
+ "StartService"
+ "StopService"
+ "Sub port type kVirtualAudioPortSubTypeHeadsetWiredDefault is forbidden"
+ "VirtualAudio_PlugIn.mm"
- " big-endian"
- " high-aligned"
- " little-endian"
- " low-aligned"
- " signed"
- " unsigned"
- "!InCider::IsRunning()"
- "#16@0:8"
- "$1$4:$3"
- "%!s(MISSING):%!d(MISSING) ADS disabled and ads::Kernel object destroyed"
- "%!s(MISSING):%!d(MISSING) ADS enabled and ads::Kernel object constructed"
- "%!s(MISSING):%!d(MISSING) Connected device named %!s(MISSING) with ID %!u(MISSING). Sleeping to allow all properties to properly populate"
- "%!s(MISSING):%!d(MISSING) Couldn't launch InCider service"
- "%!s(MISSING):%!d(MISSING) Couldn't shut down InCider service"
- "%!s(MISSING):%!d(MISSING) Device with ID %!u(MISSING) (MAC-transformed uid '%!s(MISSING)') serialized to `%!s(MISSING)`."
- "%!s(MISSING):%!d(MISSING) Disconnecting device named %!s(MISSING) with ID %!u(MISSING). Sleeping to allow all properties to properly populate"
- "%!s(MISSING):%!d(MISSING) EXCEPTION (std::logic_error) [%!s(MISSING) is true]: \"InCider must be running to send route config\""
- "%!s(MISSING):%!d(MISSING) EXCEPTION (std::logic_error) [%!s(MISSING) is true]: \"InCider must be running to send session config\""
- "%!s(MISSING):%!d(MISSING) Error: couldn't convert result for property [%!s(MISSING)/%!s(MISSING)/%!u(MISSING)] to %!s(MISSING) on device with ID %!u(MISSING)"
- "%!s(MISSING):%!d(MISSING) Existing XPC connection interrupted, cleared reporter optionals"
- "%!s(MISSING):%!d(MISSING) Existing XPC connection invalidated, cleared reporter optionals"
- "%!s(MISSING):%!d(MISSING) Failed to serialize device with ID %!u(MISSING) (MAC-transformed uid '%!s(MISSING)') to `%!s(MISSING)`. Is your filesystem RW-mounted?"
- "%!s(MISSING):%!d(MISSING) InCider object constructed"
- "%!s(MISSING):%!d(MISSING) InCider object destroyed"
- "%!s(MISSING):%!d(MISSING) Kernel checked if device with AOID %!u(MISSING) is connected (%!s(MISSING))"
- "%!s(MISSING):%!d(MISSING) Kernel checked if device with UUID %!s(MISSING) is connected (%!s(MISSING))"
- "%!s(MISSING):%!d(MISSING) Kernel connected ADS device with UUID %!s(MISSING) without error"
- "%!s(MISSING):%!d(MISSING) Kernel connected ADS devices with UUIDs %!s(MISSING) without error"
- "%!s(MISSING):%!d(MISSING) Kernel disconnected ADS device with AOID %!u(MISSING) without error"
- "%!s(MISSING):%!d(MISSING) Kernel disconnected ADS device with UUID %!s(MISSING) without error"
- "%!s(MISSING):%!d(MISSING) Kernel disconnected ADS devices with AOIDs %!s(MISSING) without error"
- "%!s(MISSING):%!d(MISSING) Kernel disconnected ADS devices with UUIDs %!s(MISSING) without error"
- "%!s(MISSING):%!d(MISSING) Kernel disconnected all ADS devices without error"
- "%!s(MISSING):%!d(MISSING) Kernel encountered error %!s(MISSING) checking if device with ID %!u(MISSING) has property [%!s(MISSING)/%!s(MISSING)/%!u(MISSING)]"
- "%!s(MISSING):%!d(MISSING) Kernel encountered error %!s(MISSING) connecting %!l(MISSING)u ADS devices"
- "%!s(MISSING):%!d(MISSING) Kernel encountered error %!s(MISSING) connecting ADS device with dictionary %!s(MISSING)"
- "%!s(MISSING):%!d(MISSING) Kernel encountered error %!s(MISSING) disconnecting ADS device with AOID %!u(MISSING)"
- "%!s(MISSING):%!d(MISSING) Kernel encountered error %!s(MISSING) disconnecting ADS device with UUID %!s(MISSING)"
- "%!s(MISSING):%!d(MISSING) Kernel encountered error %!s(MISSING) disconnecting ADS devices with AOIDs %!s(MISSING)"
- "%!s(MISSING):%!d(MISSING) Kernel encountered error %!s(MISSING) disconnecting ADS devices with UUIDs %!s(MISSING)"
- "%!s(MISSING):%!d(MISSING) Kernel encountered error %!s(MISSING) disconnecting all ADS devices"
- "%!s(MISSING):%!d(MISSING) Kernel encountered error %!s(MISSING) getting UUID for newly connected ADS device with AOID %!d(MISSING)"
- "%!s(MISSING):%!d(MISSING) Kernel encountered error %!s(MISSING) getting property [%!s(MISSING)/%!s(MISSING)/%!u(MISSING)] on device with ID %!u(MISSING)"
- "%!s(MISSING):%!d(MISSING) Kernel encountered error %!s(MISSING) getting property data size for [%!s(MISSING)/%!s(MISSING)/%!u(MISSING)] on device with ID %!u(MISSING)"
- "%!s(MISSING):%!d(MISSING) Kernel encountered error %!s(MISSING) retrieving AOID for UUID %!s(MISSING)"
- "%!s(MISSING):%!d(MISSING) Kernel encountered error %!s(MISSING) retrieving UUID for AOID %!u(MISSING)"
- "%!s(MISSING):%!d(MISSING) Kernel encountered error %!s(MISSING) setting property [%!s(MISSING)/%!s(MISSING)/%!u(MISSING)] on device with ID %!u(MISSING) with privilege"
- "%!s(MISSING):%!d(MISSING) Kernel encountered error retrieving ADS plugin AOID -- ADS is not enabled"
- "%!s(MISSING):%!d(MISSING) Kernel retrieved ADS device map: %!s(MISSING)"
- "%!s(MISSING):%!d(MISSING) Kernel retrieved ADS plugin AOID %!u(MISSING) without error"
- "%!s(MISSING):%!d(MISSING) Kernel retrieved AOID %!u(MISSING) for UUID %!s(MISSING) without error"
- "%!s(MISSING):%!d(MISSING) Kernel retrieved UUID %!s(MISSING) for AOID %!u(MISSING) without error"
- "%!s(MISSING):%!d(MISSING) Kernel successfully checked if device with ID %!u(MISSING) has property [%!s(MISSING)/%!s(MISSING)/%!u(MISSING)] (%!s(MISSING))"
- "%!s(MISSING):%!d(MISSING) Kernel successfully got property [%!s(MISSING)/%!s(MISSING)/%!u(MISSING)] on device with ID %!u(MISSING)"
- "%!s(MISSING):%!d(MISSING) Kernel successfully got property data size for [%!s(MISSING)/%!s(MISSING)/%!u(MISSING)] on device with ID %!u(MISSING)"
- "%!s(MISSING):%!d(MISSING) Kernel successfully set property [%!s(MISSING)/%!s(MISSING)/%!u(MISSING)] on device with ID %!u(MISSING) with privilege"
- "%!s(MISSING):%!d(MISSING) Launched InCider service"
- "%!s(MISSING):%!d(MISSING) New XPC connection created"
- "%!s(MISSING):%!d(MISSING) Pre-kernel CiderObject encountered nil parameter in method %!@(MISSING)"
- "%!s(MISSING):%!d(MISSING) Pre-kernel CiderObject was unable to parse NSArray input as std::vector<AudioObjectID>"
- "%!s(MISSING):%!d(MISSING) Pre-kernel CiderObject was unable to parse NSArray input as std::vector<ascf::DictionaryRef>"
- "%!s(MISSING):%!d(MISSING) Pre-kernel CiderObject was unable to parse NSArray input as std::vector<std::string>"
- "%!s(MISSING):%!d(MISSING) Request to launch InCider but it is already running => no-op"
- "%!s(MISSING):%!d(MISSING) Request to shut down InCider but it is not running => no-op"
- "%!s(MISSING):%!d(MISSING) Shut down InCider service"
- "%!s(MISSING):%!d(MISSING) Skipped attempt to serialize control (AudioObjectID %!u(MISSING)) with AudioClassID %!u(MISSING) (%!s(MISSING)): unknown type"
- "%!s(MISSING):%!d(MISSING) Skipped attempt to serialize control (AudioObjectID %!u(MISSING)): device does not have property kAudioObjectPropertyClass"
- "%!s(MISSING):%!d(MISSING) Skipped attempt to serialize device with ID %!u(MISSING) (uid '%!s(MISSING)'): device is simulated via ADS"
- "%!s(MISSING):%!d(MISSING) Skipped attempt to serialize stream format: %!s(MISSING). ASBD: %!s(MISSING)"
- "%!s(MISSING):%!d(MISSING) Stored reply block for new reporter and sent route configuration"
- "%!s(MISSING):%!d(MISSING) Stored reply block for new reporter and sent session configuration"
- "%!s(MISSING):%!d(MISSING) Stored reply block for reporter, no route configuration present"
- "%!s(MISSING):%!d(MISSING) Stored reply block for reporter, no session configuration present"
- "%!s(MISSING):%!d(MISSING) Stored reply block for same reporter, no route configuration sent"
- "%!s(MISSING):%!d(MISSING) Stored reply block for same reporter, no session configuration sent"
- "%!s(MISSING):%!d(MISSING) Stored route configuration and reported to OutCider"
- "%!s(MISSING):%!d(MISSING) Stored route configuration, no reporter present"
- "%!s(MISSING):%!d(MISSING) Stored session configuration and reported to OutCider"
- "%!s(MISSING):%!d(MISSING) Stored session configuration, no reporter present"
- "%!s(MISSING):%!d(MISSING) ads::Kernel object destroyed, but could not disable ADS"
- "%!s(MISSING):%!d(MISSING) catchAndLogException: encountered CAException %!s(MISSING)"
- "%!s(MISSING):%!d(MISSING) catchAndLogException: encountered std::exception %!s(MISSING)"
- "%!s(MISSING):%!d(MISSING) catchAndLogException: encountered unspecified error"
- "%!d(MISSING) ch, %!f(MISSING) Hz, %!s(MISSING) (0x%!X(MISSING)) "
- "%!d(MISSING) bits/channel, %!d(MISSING) bytes/packet, %!d(MISSING) frames/packet, %!d(MISSING) bytes/frame"
- "%!d(MISSING) frames/packet"
- "%!d(MISSING).%!d(MISSING)"
- "%!s(MISSING)-bit%!s(MISSING)%!s(MISSING) %!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)"
- "'it doesn't"
- "(([0-9a-fA-F]{2}:){4})([0-9a-fA-F]{2}):([0-9a-fA-F]{2})"
- ", deinterleaved"
- "@\"CiderObject\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16^{AudioObjectPropertyAddress=III}24@32"
- "@@ Strips Oct 16 2024 14:56:35"
- "ADSKernel.mm"
- "ADSKernelQueue"
- "ASBD is not valid because !(asbd.mFormatFlags & kAudioFormatFlagIsFloat) && (asbd.mBitsPerChannel > 24)."
- "ASBD is not valid because (asbd.mBytesPerFrame * asbd.mFramesPerPacket == asbd.mBytesPerPacket) and asbd.mFormatID == kAudioFormatLinearPCM returned false."
- "ASBD is not valid because not (asbd.mBitsPerChannel * asbd.mChannelsPerFrame / 8 == asbd.mBytesPerFrame) and asbd.mFormatID == kAudioFormatLinearPCM."
- "ASBD is not valid because sample rate was less than 0"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "CiderDelegate"
- "CiderObject"
- "CiderProtocol"
- "Device could not enable ADS"
- "Device does not have ADS"
- "DeviceSerializationUtilities.mm"
- "Device_HAL_Common.cpp"
- "InCider must be running to send route config"
- "InCider must be running to send session config"
- "InCider.mm"
- "Invalid LoggingScope."
- "KernelUtilities.h"
- "NSObject"
- "NSXPCListenerDelegate"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "VirtualAudio_PlugIn.cpp"
- "Vv16@0:8"
- "We should never throw here. Successfully connecting a list of ads::Device then failing to get their UUIDs?"
- "^{_NSZone=}16@0:8"
- "activate"
- "ads::Kernel::connectADSDevice"
- "ads::Kernel::connectADSDevices"
- "ads::Kernel::disconnectADSDeviceByAOID"
- "ads::Kernel::disconnectADSDeviceByUUID"
- "ads::Kernel::disconnectADSDeviceByUUIDs"
- "ads::Kernel::disconnectADSDevicesByAOIDs"
- "ads::Kernel::disconnectAllADSDevices"
- "ads::Kernel::getADSPluginAOID"
- "ads::Kernel::getAOIDForUUID"
- "ads::Kernel::getPropertyData"
- "ads::Kernel::getPropertyDataSize"
- "ads::Kernel::getPropertyData_TypeRef"
- "ads::Kernel::getUUIDForAOID"
- "ads::Kernel::hasProperty"
- "ads::Kernel::serializeNonADSDevices"
- "ads::Kernel::setPropertyDataPrivileged"
- "ads::Kernel::setPropertyDataPrivileged_TypeRef"
- "array"
- "audiovaluerange"
- "autorelease"
- "basic description"
- "bits per channel"
- "boolean"
- "btaudioendvolumeramp"
- "bytes"
- "bytes per frame"
- "bytes per packet"
- "can be content default"
- "can be system default"
- "channel A"
- "channel B"
- "channels per frame"
- "class"
- "clearInvalidationHandler"
- "clearReporterOpts"
- "com.apple.virtualaudio.cider"
- "conformsToProtocol:"
- "connectADSDevice:withReply:"
- "connectADSDevices:withReply:"
- "controls"
- "create"
- "custom"
- "dB range"
- "debugDescription"
- "description"
- "destroy"
- "dictionary"
- "disconnectADSDeviceByAOID:withReply:"
- "disconnectADSDeviceByUUID:withReply:"
- "disconnectADSDevicesByAOIDs:withReply:"
- "disconnectADSDevicesByUUIDs:withReply:"
- "disconnectAllADSDevices:"
- "element"
- "errorWithDomain:code:userInfo:"
- "fileURLWithPath:"
- "float"
- "format flags"
- "format id"
- "frames per packet"
- "from %!d(MISSING)-bit source, "
- "from UNKNOWN source bit depth, "
- "getADSDeviceMap:"
- "getADSPluginAOID:"
- "getAOIDForUUID:withReply:"
- "getPropertyDataSize:withInAddress:withInQualifierData:withReply:"
- "getPropertyDataSize:withInAddress:withReply:"
- "getPropertyData_Arithmetic:withInAddress:withInQualifierData:withReply:"
- "getPropertyData_Arithmetic:withInAddress:withReply:"
- "getPropertyData_Array:withInAddress:withReply:"
- "getPropertyData_Dict:withInAddress:withReply:"
- "getPropertyData_NSHelper:withInAddress:withClass:"
- "getPropertyData_String:withInAddress:withReply:"
- "getUUIDForAOID:withReply:"
- "hasProperty:withInAddress:withReply:"
- "hash"
- "initWithMachServiceName:"
- "int"
- "integer"
- "interfaceWithProtocol:"
- "is input"
- "isDeviceWithAOIDConnected:withReply:"
- "isDeviceWithUUIDConnected:withReply:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "it does"
- "it is"
- "it isn't"
- "items"
- "latency"
- "length"
- "level"
- "listener:shouldAcceptNewConnection:"
- "mCurrentConnection"
- "mKernelPtr"
- "mObject"
- "max sample rate"
- "min sample rate"
- "model"
- "number"
- "numberWithUnsignedInt:"
- "packed in %!d(MISSING) bytes"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "registerForRouteReport:"
- "registerForSessionReport:"
- "release"
- "requires set request"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "ring buffer frame size"
- "safety offset"
- "sample rate"
- "scope"
- "selector"
- "self"
- "serializeNonADSDevices:"
- "setDelegate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setPropertyDataPrivileged_Arithmetic:withInAddress:withInData:withReply:"
- "setPropertyDataPrivileged_Arithmetic:withInAddress:withInQualifierData:withInData:withReply:"
- "setPropertyDataPrivileged_Array:withInAddress:withInData:withReply:"
- "setPropertyDataPrivileged_Dict:withInAddress:withInData:withReply:"
- "setPropertyDataPrivileged_NSHelper:withInAddress:withInData:"
- "setPropertyDataPrivileged_String:withInAddress:withInData:withReply:"
- "settable"
- "slider"
- "stereo pan"
- "streams"
- "string"
- "superclass"
- "supported formats"
- "terminal type"
- "transport type"
- "unpacked in %!d(MISSING) bytes"
- "uuid"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSDictionary\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\"@\"NSArray\">16"
- "v24@0:8@?<v@?@\"NSError\"@\"NSDictionary\">16"
- "v24@0:8@?<v@?@\"NSError\"@\"NSNumber\">16"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\"@\"NSArray\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\"@\"NSString\">24"
- "v32@0:8@\"NSNumber\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSNumber\"16@?<v@?@\"NSError\"@\"NSString\">24"
- "v32@0:8@\"NSNumber\"16@?<v@?@\"NSError\"B>24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\"@\"NSNumber\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\"B>24"
- "v32@0:8@16@?24"
- "v40@0:8@\"NSNumber\"16^{AudioObjectPropertyAddress=III}24@?<v@?@\"NSError\"@\"NSArray\">32"
- "v40@0:8@\"NSNumber\"16^{AudioObjectPropertyAddress=III}24@?<v@?@\"NSError\"@\"NSData\">32"
- "v40@0:8@\"NSNumber\"16^{AudioObjectPropertyAddress=III}24@?<v@?@\"NSError\"@\"NSDictionary\">32"
- "v40@0:8@\"NSNumber\"16^{AudioObjectPropertyAddress=III}24@?<v@?@\"NSError\"@\"NSString\">32"
- "v40@0:8@\"NSNumber\"16^{AudioObjectPropertyAddress=III}24@?<v@?@\"NSError\"B>32"
- "v40@0:8@\"NSNumber\"16^{AudioObjectPropertyAddress=III}24@?<v@?@\"NSError\"I>32"
- "v40@0:8@16^{AudioObjectPropertyAddress=III}24@?32"
- "v48@0:8@\"NSNumber\"16^{AudioObjectPropertyAddress=III}24@\"NSArray\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSNumber\"16^{AudioObjectPropertyAddress=III}24@\"NSData\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSNumber\"16^{AudioObjectPropertyAddress=III}24@\"NSData\"32@?<v@?@\"NSError\"@\"NSData\">40"
- "v48@0:8@\"NSNumber\"16^{AudioObjectPropertyAddress=III}24@\"NSData\"32@?<v@?@\"NSError\"I>40"
- "v48@0:8@\"NSNumber\"16^{AudioObjectPropertyAddress=III}24@\"NSDictionary\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSNumber\"16^{AudioObjectPropertyAddress=III}24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v48@0:8@16^{AudioObjectPropertyAddress=III}24@32@?40"
- "v56@0:8@\"NSNumber\"16^{AudioObjectPropertyAddress=III}24@\"NSData\"32@\"NSData\"40@?<v@?@\"NSError\">48"
- "v56@0:8@16^{AudioObjectPropertyAddress=III}24@32@40@?48"
- "writeToURL:atomically:"
- "zone"
- "{pair<NSError *, NSObject<NSSecureCoding> *>=@@}40@0:8@16^{AudioObjectPropertyAddress=III}24#32"
- "{shared_ptr<ads::Kernel>=\"__ptr_\"^{Kernel}\"__cntrl_\"^{__shared_weak_count}}"

```
