## BTAudioHALPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin`

```diff

-  __TEXT.__text: 0x7ccd4
+  __TEXT.__text: 0x7d47c
   __TEXT.__auth_stubs: 0x1370
   __TEXT.__objc_stubs: 0x2800
   __TEXT.__init_offsets: 0xa4
   __TEXT.__objc_methlist: 0x118c
   __TEXT.__gcc_except_tab: 0x2064
-  __TEXT.__const: 0x1aac
+  __TEXT.__const: 0x1a9c
   __TEXT.__cstring: 0x4f78
-  __TEXT.__oslogstring: 0x16233
+  __TEXT.__oslogstring: 0x16af8
   __TEXT.__objc_methname: 0x3ecc
   __TEXT.__objc_classname: 0x154
   __TEXT.__objc_methtype: 0x1257
-  __TEXT.__unwind_info: 0x1cd8
+  __TEXT.__unwind_info: 0x1cd0
   __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__const: 0x5318
+  __DATA_CONST.__const: 0x5338
   __DATA_CONST.__cfstring: 0x16a0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x20

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 2861
+  Functions: 2872
   Symbols:   476
-  CStrings:  3176
+  CStrings:  3194
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
~ __DATA.__bss : content changed
CStrings:
+ "BTAudioAVNotificationMonitor: choosePickableRoute — _systemController is nil, cannot query pickable route"
+ "BTAudioAVNotificationMonitor: choosePickableRoute — route is not BT headphones/headset (route=%@), clearing _currentDeviceUID %@"
+ "BTAudioAVNotificationMonitor: choosePickableRoute — skipping, monitor is shutting down"
+ "BTAudioAVNotificationMonitor: processManualVolumeUpdates — skipping enabled=%d, monitor is shutting down"
+ "BTAudioAVNotificationMonitor: registerPersonalizedVolumeListener block — skipping device %u (%@), monitor shut down before block executed"
+ "BTAudioAVNotificationMonitor: registerPersonalizedVolumeListener mirror block — skipping address mirror for %@, monitor shut down"
+ "BTAudioAVNotificationMonitor: registerPersonalizedVolumeListener — skipping device %u (%@), monitor is shutting down"
+ "BTAudioAVNotificationMonitor: removeAllNotificationListeners — skipping, _systemController is nil (subscription may have failed at init)"
+ "BTAudioAVNotificationMonitor: sendManualVolumeUpdate — skipping volume=%u uid=%@, monitor is shutting down"
+ "BTAudioAVNotificationMonitor: unRegisterPersonalizedVolumeListener block — skipping device %u (%@), monitor shut down before block executed"
+ "BTAudioAVNotificationMonitor: unRegisterPersonalizedVolumeListener mirror block — skipping address removal for %@, monitor shut down"
+ "BTAudioAVNotificationMonitor: unRegisterPersonalizedVolumeListener — skipping device %u (%@), monitor is shutting down"
+ "BTAudioAVNotificationMonitor: updateVolumeDelta — _systemController is nil, cannot forward delta=%f to MXSystemController"
+ "BTAudioAVNotificationMonitor: updateVolumeDelta — skipping delta=%f, monitor is shutting down"
+ "BTAudioAVNotificationMonitor: updateVolumeForCategories — _systemController is nil, cannot forward media=%f tel=%f voice=%f to MXSystemController"
+ "BTAudioAVNotificationMonitor: updateVolumeForCategories — skipping media=%f tel=%f voice=%f, monitor is shutting down"
+ "HostGrid Anchor c:%llu,len:%u,Q:%f~%u,curr:%f,bufSize:%u,Seq:%x"
+ "HostGrid jumped back c:%llu,Q:%f~%u,curr:%f,ATs:%f,bufSize:%u"
+ "HostGrid reA drop:%f >= bufSize:%u, forcing re-anchor; prevATs:%f,prevQ:%f~%u,curr:%f,ATs:%f"
+ "HostGrid reA prevATs:%f,prevQ:%f~%u,drop:%f,Q:%f~%u,curr:%f,ATs:%f,bufSize:%u,Seq:%u , @ %llu"
+ "HostGrid should not come here c:%llu,Q:%f~%u,curr:%f,ATs:%f,bufSize:%u"
+ "InvalidateAllUnifiedAudioDevices: skipping BTAudioAVNotificationMonitor shutdown — transient XPC disconnect, monitor remains active for reconnect"
- "HostGrid Anchor c:%llu,len:%u,Q:%f~%u,curr:%f,Seq:%x"
- "HostGrid jumped back c:%llu,Q:%f~%u,curr:%f,ATs:%f"
- "HostGrid reA prevATs:%f,prevQ:%f~%u,drop:%f,Q:%f~%u,curr:%f,ATs:%f,Seq:%u , @ %llu"
- "HostGrid should not come here c:%llu,Q:%f~%u,curr:%f,ATs:%f"

```
