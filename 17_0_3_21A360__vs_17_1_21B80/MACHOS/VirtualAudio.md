## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

```diff

-1203.1.14.30.3
-  __TEXT.__text: 0x43d774
-  __TEXT.__auth_stubs: 0x2120
-  __TEXT.__objc_stubs: 0x5e0
-  __TEXT.__init_offsets: 0x494
+1203.2.9.30.1
+  __TEXT.__text: 0x4432ec
+  __TEXT.__auth_stubs: 0x2150
+  __TEXT.__objc_stubs: 0x660
+  __TEXT.__init_offsets: 0x4a0
   __TEXT.__objc_methlist: 0x128
-  __TEXT.__const: 0xb03db
-  __TEXT.__gcc_except_tab: 0x450ec
-  __TEXT.__oslogstring: 0x49c7d
-  __TEXT.__cstring: 0x26f83
-  __TEXT.__objc_methname: 0x72c
+  __TEXT.__const: 0xb0443
+  __TEXT.__gcc_except_tab: 0x455bc
+  __TEXT.__oslogstring: 0x4a5f3
+  __TEXT.__cstring: 0x27167
+  __TEXT.__objc_methname: 0x76a
   __TEXT.__objc_classname: 0x4a
   __TEXT.__objc_methtype: 0x473
   __TEXT.__dof_VirtualAu: 0x303
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualAu0: 0x2aa
-  __TEXT.__unwind_info: 0xe260
+  __TEXT.__unwind_info: 0xe4d0
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x10a0
+  __DATA_CONST.__auth_got: 0x10b8
   __DATA_CONST.__got: 0x388
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x20ba8
-  __DATA_CONST.__cfstring: 0x38c0
+  __DATA_CONST.__const: 0x21228
+  __DATA_CONST.__cfstring: 0x3920
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x728
-  __DATA.__objc_selrefs: 0x218
+  __DATA.__objc_selrefs: 0x238
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x88
   __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x480
-  __DATA.__bss: 0x16f9c
+  __DATA.__data: 0x4d8
+  __DATA.__bss: 0x1743c
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9811
-  Symbols:   676
-  CStrings:  10281
+  Functions: 10008
+  Symbols:   679
+  CStrings:  10350
 
Symbols:
+ __os_signpost_emit_with_name_impl
+ _os_signpost_enabled
+ _os_signpost_id_generate
CStrings:
+ "!InCider::IsRunning()"
+ "%25s:%-5d Bluetooth audio device with UID \"%s\": setting routability to %s"
+ "%25s:%-5d Bluetooth audio port with UID \"%s\": headset status %s, effective in ear state: %s"
+ "%25s:%-5d Couldn't launch InCider service"
+ "%25s:%-5d Couldn't shut down InCider service"
+ "%25s:%-5d Defaults key %s was defined to %s. %sabling VA's InCider service."
+ "%25s:%-5d Device %@ VolumeCurveProperty returned array of zeroes."
+ "%25s:%-5d EXCEPTION (std::logic_error) [%s is true]: \"InCider must be running to send route config\""
+ "%25s:%-5d EXCEPTION (std::logic_error) [%s is true]: \"InCider must be running to send session config\""
+ "%25s:%-5d HasProperty(%s): %d"
+ "%25s:%-5d InCider object constructed"
+ "%25s:%-5d InCider object destroyed"
+ "%25s:%-5d Launched InCider service"
+ "%25s:%-5d PlaybackDosimetry : Volume map contains all zeroes, fallback to default"
+ "%25s:%-5d Refreshing input stream %p for stream format preference change."
+ "%25s:%-5d Request to launch InCider but it is already running => no-op"
+ "%25s:%-5d Request to shut down InCider but it is not running => no-op"
+ "%25s:%-5d Returning Last connected quiesceable wired port: %s"
+ "%25s:%-5d Shut down InCider service"
+ "%25s:%-5d Stored route configuration and reported to OutCider"
+ "%25s:%-5d Stored route configuration, no reporter present"
+ "%25s:%-5d Stored session configuration and reported to OutCider"
+ "%25s:%-5d Stored session configuration, no reporter present"
+ "%25s:%-5d VA's InCider service requires an internal build. Ignored defaults check for %s."
+ "@@ Strips Oct  5 2023 21:05:07"
+ "ActivateForLastInWins, Primary route = %s, Abstract route =%s"
+ "ActivateForNormal, Primary route = %s, Abstract route = %s"
+ "ActiveNonWirelessPorts"
+ "Attempting to build concrete route(s) for abstract route %s. inMode: %s; inDisallowedPorts:%s; inDisallowedPortTypes:%s; inVADCoupling: %s; inDeviceType: %s; inPermitUnroutablePorts: %u."
+ "Begin updating port routability, ownership = %d"
+ "BuildAlternateRoutesAndActivateForLastInWins"
+ "BuildAlternateRoutesAndActivateForNormal"
+ "BuiltInPorts"
+ "ConnectedPorts"
+ "EnableCider"
+ "GetPorts"
+ "GetPorts for category = %s, candidate ports = %s, disallowed ports = %s"
+ "HandleInEarStatusEvent"
+ "HandleOwnershipEvent"
+ "InCider must be running to send route config"
+ "InCider must be running to send session config"
+ "LogTimeTaken"
+ "PV_BuildConcreteFromAbstract"
+ "Query for ConnectedPortsForRouteConfiguration"
+ "Query for kActiveNonWirelessPortsForRouteConfiguration"
+ "Query for kVirtualAudioPlugInPropertyBuiltInPortsForCategory"
+ "Route change begins"
+ "Route change ends"
+ "RouteChange"
+ "SetOwnership"
+ "Setting kVirtualAudioPortPropertyOwnsSharedAudioConnection to %d"
+ "Sub port type kVirtualAudioPortSubTypeUSBDefault is forbidden"
+ "Updating InEarStatus for BT ports because headset status is %d"
+ "VA Initialization"
+ "VAInitialization"
+ "activate"
+ "com.apple.virtualaudio.cider"
+ "initWithMachServiceName:"
+ "invalidate"
+ "setDelegate:"
- "%25s:%-5d InEarState for port with name \"%s\", UID \"%s\", and type '%s'is : %u"
- "@@ Strips Aug 11 2023 21:00:51"
- "btie: "

```
