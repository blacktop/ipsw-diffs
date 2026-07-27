## DeviceInterface

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/DeviceInterface.framework/Versions/A/DeviceInterface`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-228.160.2.0.0
-  __TEXT.__text: 0x7da8c
+228.160.3.0.0
+  __TEXT.__text: 0x7d9c4
   __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_methlist: 0x654c
+  __TEXT.__objc_methlist: 0x652c
   __TEXT.__const: 0x64
-  __TEXT.__cstring: 0x7de5
+  __TEXT.__cstring: 0x7ee4
   __TEXT.__gcc_except_tab: 0x4ec
-  __TEXT.__unwind_info: 0x1218
+  __TEXT.__unwind_info: 0x1208
   __TEXT.__eh_frame: 0xfc
   __TEXT.__objc_classname: 0xf57
-  __TEXT.__objc_methname: 0xe2ad
-  __TEXT.__objc_methtype: 0x5c37
+  __TEXT.__objc_methname: 0xe298
+  __TEXT.__objc_methtype: 0x5c26
   __TEXT.__objc_stubs: 0x6d80
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x68

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x25b8
   __AUTH_CONST.__auth_got: 0x378
-  __AUTH_CONST.__const: 0x8b0
+  __AUTH_CONST.__const: 0x850
   __AUTH_CONST.__cfstring: 0x760
   __AUTH_CONST.__objc_const: 0xdba8
   __AUTH.__objc_data: 0x2170
-  __AUTH.__data: 0x540
+  __AUTH.__data: 0x538
   __DATA.__objc_protorefs: 0x20
   __DATA.__objc_classrefs: 0x3f0
   __DATA.__objc_superrefs: 0x348

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 2667
-  Symbols:   5397
-  CStrings:  3349
+  Functions: 2661
+  Symbols:   5389
+  CStrings:  3350
 
Symbols:
+ -[RSMInterfaceKIS lockInterfaceForClient:protocolToken:]
+ -[RSMInterfaceKIS unregisterCallbacksForClient:]
+ -[RSMInterfaceKISClient lockInterfaceWithProtocolToken:]
+ -[RSMInterfaceKISClient unregisterCallbacks]
+ ___48-[RSMInterfaceKIS unregisterCallbacksForClient:]_block_invoke
+ ___56-[RSMInterfaceKIS lockInterfaceForClient:protocolToken:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0l
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
- ___33-[RSMInterfaceKIS cleanupClient:]_block_invoke
- ___36-[RSMInterfaceKIS setDoorbellTimer:]_block_invoke
- ___47-[RSMInterfaceKIS setDoorbellRequiredEndIndex:]_block_invoke
- ___70-[RSMInterfaceKIS lockInterfaceForClient:andCheckToken:protocolToken:]_block_invoke
- ___block_descriptor_41_e8_32s_e5_v8?0l
- ___block_descriptor_44_e8_32s_e5_v8?0l
- ___block_descriptor_65_e8_32s40s48r_e5_v8?0l
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
+ "RSMChannelInterfaceRSM[0x%llx]: Failed to lock RSM interface! Failed to start interface!"
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
