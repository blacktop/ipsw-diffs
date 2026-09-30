## audioaccessoryd

> `/System/Library/CoreServices/audioaccessoryd`

```diff

-  __TEXT.__text: 0x23d010
+  __TEXT.__text: 0x2403fc
   __TEXT.__auth_stubs: 0x3700
-  __TEXT.__objc_stubs: 0x1afc0
-  __TEXT.__objc_methlist: 0xccc4
-  __TEXT.__const: 0x4f00
+  __TEXT.__objc_stubs: 0x1b020
+  __TEXT.__objc_methlist: 0xcd34
+  __TEXT.__const: 0x4ed0
   __TEXT.__gcc_except_tab: 0x4ff4
-  __TEXT.__cstring: 0x4bf13
+  __TEXT.__cstring: 0x4c1f3
   __TEXT.__objc_classname: 0xf43
-  __TEXT.__objc_methname: 0x27095
-  __TEXT.__objc_methtype: 0x3d39
-  __TEXT.__oslogstring: 0x9d2a
+  __TEXT.__objc_methname: 0x27205
+  __TEXT.__objc_methtype: 0x3d49
+  __TEXT.__oslogstring: 0x9fba
   __TEXT.__ustring: 0x10
-  __TEXT.__swift5_typeref: 0x1ec4
-  __TEXT.__constg_swiftt: 0x20dc
-  __TEXT.__swift5_reflstr: 0x1b9b
-  __TEXT.__swift5_fieldmd: 0x198c
+  __TEXT.__swift5_typeref: 0x1ee4
+  __TEXT.__constg_swiftt: 0x2104
+  __TEXT.__swift5_reflstr: 0x1bbb
+  __TEXT.__swift5_fieldmd: 0x1998
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_assocty: 0x228
-  __TEXT.__swift5_capture: 0x1f5c
+  __TEXT.__swift5_capture: 0x1f94
   __TEXT.__swift5_proto: 0x3a4
   __TEXT.__swift5_types: 0x120
   __TEXT.__swift_as_entry: 0x7c

   __TEXT.__swift_as_cont: 0xe8
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x66f0
-  __TEXT.__eh_frame: 0x2ca8
-  __DATA_CONST.__const: 0xc730
-  __DATA_CONST.__cfstring: 0xafc0
+  __TEXT.__unwind_info: 0x6770
+  __TEXT.__eh_frame: 0x2d78
+  __DATA_CONST.__const: 0xc818
+  __DATA_CONST.__cfstring: 0xb060
   __DATA_CONST.__objc_classlist: 0x368
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x170

   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__auth_got: 0x1b90
-  __DATA_CONST.__got: 0xd48
+  __DATA_CONST.__got: 0xe00
   __DATA_CONST.__auth_ptr: 0x7b8
-  __DATA.__objc_const: 0x1c910
-  __DATA.__objc_selrefs: 0x7e90
-  __DATA.__objc_ivar: 0x14e4
-  __DATA.__objc_data: 0x2fe0
-  __DATA.__data: 0x5480
+  __DATA.__objc_const: 0x1c970
+  __DATA.__objc_selrefs: 0x7eb8
+  __DATA.__objc_ivar: 0x14ec
+  __DATA.__objc_data: 0x3258
+  __DATA.__data: 0x52b0
   __DATA.__bss: 0x7630
   __DATA.__common: 0x3a8
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10827
+  Functions: 10873
   Symbols:   1518
-  CStrings:  15960
+  CStrings:  16002
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__bss : content changed
~ __DATA.__common : content changed
CStrings:
+ "### Missing BT address in head tracking state message"
+ "-[BTAudioDriverController _headTrackingStateChangedMessageReceived:]"
+ "-[SR3PRoutingDaemon _headTrackingStateChanged:btAddress:]"
+ "Activate message missing deviceConfiguration, cannot register connection"
+ "HeadTrackingStateChanged: Could not resolve UUID for %@, skipping notification"
+ "HeadTrackingStateChanged: No BT address provided"
+ "HeadTrackingStateChanged: Spatial head tracking %s for %@"
+ "New write client connected, pending device UUID registration"
+ "No registered write connection for UUID %s, head tracking state not sent"
+ "Notification: spatial head tracking changed to %{bool}d for UUID %s"
+ "Received head tracking notification with missing userInfo"
+ "Registered write connection for device UUID: %s on activate (total: %ld)"
+ "SR3PHeadTracking"
+ "SRSpatialHeadTrackingBTAddressKey"
+ "SRSpatialHeadTrackingDeviceUUIDKey"
+ "SRSpatialHeadTrackingEnabledKey"
+ "SRSpatialHeadTrackingStateChangedNotification"
+ "Sent head tracking state %{bool}d to write client for UUID %s"
+ "Spatial head tracking state changed: %s for %@"
+ "TB,R,V_spatialHeadTrackingEnabled"
+ "Using forced value for head tracking support %u"
+ "Write client disconnected for UUID(s) %s (remaining: %ld)"
+ "Write connection for UUID %s already registered, skipping"
+ "XPC listener not activated"
+ "XPC listeners deactivated"
+ "_headTrackingStateChanged:btAddress:"
+ "_headTrackingStateChangedMessageReceived:"
+ "_spatialHeadTrackingEnabled"
+ "_spatialHeadTrackingEnabledPerDevice"
+ "_writeDataListenerConnections"
+ "handleHeadTrackingStateChanged:"
+ "headTrackingState"
+ "headTrackingStateChanged:btAddress:"
+ "kAccAudioMsgArgHeadTrackingEnabled"
+ "kBTAudioMsgProperty3pHeadTrackingSupport"
+ "spatialHeadTrackingEnabled"
- "New write client connected to AudioAccessorySensor XPC service"

```
