## DeviceInterface

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/DeviceInterface.framework/Versions/A/DeviceInterface`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__DATA.__data`

```diff

-289.0.0.0.0
-  __TEXT.__text: 0x8c168
-  __TEXT.__objc_methlist: 0x7044
+291.0.0.0.0
+  __TEXT.__text: 0x8c01c
+  __TEXT.__objc_methlist: 0x7034
   __TEXT.__const: 0x64
-  __TEXT.__cstring: 0x9c02
+  __TEXT.__cstring: 0x9ca8
   __TEXT.__gcc_except_tab: 0x470
   __TEXT.__oslogstring: 0x49
   __TEXT.__unwind_info: 0x1278
   __TEXT.__eh_frame: 0xd4
-  __TEXT.__objc_stubs: 0x7da0
+  __TEXT.__objc_stubs: 0x7d80
   __TEXT.__auth_stubs: 0x8e0
   __TEXT.__objc_classname: 0x100e
-  __TEXT.__objc_methname: 0xf8b4
-  __TEXT.__objc_methtype: 0x5c98
+  __TEXT.__objc_methname: 0xf89f
+  __TEXT.__objc_methtype: 0x5c87
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x3a0
   __DATA_CONST.__objc_protolist: 0x68

   __AUTH_CONST.__objc_const: 0xf138
   __AUTH_CONST.__auth_got: 0x480
   __AUTH.__objc_data: 0x2440
-  __AUTH.__data: 0x5a8
+  __AUTH.__data: 0x5a0
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x438
   __DATA.__objc_superrefs: 0x390

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 2925
-  Symbols:   5964
+  Functions: 2920
+  Symbols:   5958
   CStrings:  3690
 
Symbols:
+ -[RSMInterfaceKIS lockInterfaceForClient:protocolToken:]
+ -[RSMInterfaceKIS unregisterCallbacksForClient:]
+ -[RSMInterfaceKISClient lockInterfaceWithProtocolToken:]
+ -[RSMInterfaceKISClient unregisterCallbacks]
+ _objc_msgSend$lockInterfaceForClient:protocolToken:
+ _objc_msgSend$lockInterfaceWithProtocolToken:
+ _objc_msgSend$unregisterCallbacks
+ _objc_msgSend$unregisterCallbacksForClient:
+ _rsm_interface_client_unregister_callbacks
+ _rsm_interface_kis_unregister_callbacks
- -[RSMInterfaceKIS lockInterfaceForClient:andCheckToken:protocolToken:]
- -[RSMInterfaceKIS setDoorbellRequiredEndIndex:]
- -[RSMInterfaceKIS setDoorbellTimer:]
- -[RSMInterfaceKISClient lockInterfaceAndCheckToken:protocolToken:]
- -[RSMInterfaceKISClient setDoorbellRequiredEndIndex:]
- -[RSMInterfaceKISClient setDoorbellTimer:]
- ___36-[RSMInterfaceKIS setDoorbellTimer:]_block_invoke
- _objc_msgSend$doorbellTimerMS
- _objc_msgSend$lockInterfaceAndCheckToken:protocolToken:
- _objc_msgSend$lockInterfaceForClient:andCheckToken:protocolToken:
- _objc_msgSend$setDoorbellRequiredEndIndex:
- _objc_msgSend$setDoorbellTimer:
- _rsm_interface_client_set_doorbell_required_end_index
- _rsm_interface_client_set_doorbell_timer
- _rsm_interface_kis_set_doorbell_required_end_index
- _rsm_interface_kis_set_doorbell_timer
CStrings:
+ "B32@0:8@16Q24"
+ "RSMChannelInterfaceRSM[0x%llx]: Failed to read protocol for initial doorbell seed! Failed to start interface!"
+ "RSMChannelInterfaceRSM[0x%llx]: Failed to register command callbacks! Failed to start interface!"
+ "RSMChannelInterfaceRSM[0x%llx]: Failed to register doorbell callbacks! Failed to start interface!"
+ "lockInterfaceForClient:protocolToken:"
+ "lockInterfaceWithProtocolToken:"
+ "unregisterCallbacks"
+ "unregisterCallbacksForClient:"
- "%s registerCommandReceivedCallbacksResult %d"
- "-[TADFUInterfaceRSM initWithRSMInterfaceID:rsmManager:protocolToken:doorbells:doorbellCount:]"
- "B28@0:8B16Q20"
- "B36@0:8@16B24Q28"
- "lockInterfaceAndCheckToken:protocolToken:"
- "lockInterfaceForClient:andCheckToken:protocolToken:"
- "setDoorbellRequiredEndIndex:"
- "setDoorbellTimer:"
```
