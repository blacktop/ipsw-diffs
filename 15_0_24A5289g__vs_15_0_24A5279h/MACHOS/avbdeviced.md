## avbdeviced

> `/usr/sbin/avbdeviced`

```diff

-1300.22.0.0.0
-  __TEXT.__text: 0x45a40
-  __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_stubs: 0x5700
-  __TEXT.__objc_methlist: 0x15cc
-  __TEXT.__const: 0xfc
+1300.21.0.0.0
+  __TEXT.__text: 0x455b4
+  __TEXT.__auth_stubs: 0x440
+  __TEXT.__objc_stubs: 0x56e0
+  __TEXT.__objc_methlist: 0x15c4
+  __TEXT.__const: 0xf4
   __TEXT.__cstring: 0x1e18
-  __TEXT.__objc_methname: 0x66b2
-  __TEXT.__objc_classname: 0x429
-  __TEXT.__objc_methtype: 0x1068
-  __TEXT.__oslogstring: 0x3f60
-  __TEXT.__gcc_except_tab: 0x564
-  __TEXT.__unwind_info: 0x858
-  __DATA_CONST.__auth_got: 0x240
+  __TEXT.__objc_methname: 0x660e
+  __TEXT.__objc_classname: 0x414
+  __TEXT.__objc_methtype: 0x102c
+  __TEXT.__oslogstring: 0x3f1d
+  __TEXT.__gcc_except_tab: 0x518
+  __TEXT.__unwind_info: 0x848
+  __DATA_CONST.__auth_got: 0x230
   __DATA_CONST.__got: 0x2b0
   __DATA_CONST.__const: 0x1520
   __DATA_CONST.__cfstring: 0x1740
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x88
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x4e78
-  __DATA.__objc_selrefs: 0x19b0
+  __DATA.__objc_const: 0x4db0
+  __DATA.__objc_selrefs: 0x19a8
   __DATA.__objc_ivar: 0x2a4
   __DATA.__objc_data: 0x780
-  __DATA.__data: 0x670
+  __DATA.__data: 0x610
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AudioVideoBridging.framework/Versions/A/AudioVideoBridging

   - /System/Library/PrivateFrameworks/TimeSync.framework/Versions/A/TimeSync
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 782
-  Symbols:   177
+  Functions: 780
+  Symbols:   175
   CStrings:  275
 
Symbols:
- _NSStringFromClass
- _dispatch_after
CStrings:
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/AVBKit/MediaClocking/AVBMediaClockConnection.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/ADDReconnectController.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/AcquireMode/ADDAcquireMode.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/AcquireMode/ADDAcquireModeEntity.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/VirtualEntity/ADDVirtualAudioInputStream.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/VirtualEntity/ADDVirtualAudioOutputStream.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/VirtualEntity/ADDVirtualEntity.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/VirtualEntity/ADDVirtualMediaClockInputStream.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/VirtualEntity/ADDVirtualMediaClockOutputStream.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/VirtualEntityState/ADDEntityIDManager.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/VirtualEntityState/ADDVirtualEntityPersistentInfoManager.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/VirtualMode/ADDAudioDriver.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/VirtualMode/ADDVirtualAudio2.m"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/AVBKit/MediaClocking/AVBMediaClockConnection.m"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/ADDReconnectController.m"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/AcquireMode/ADDAcquireMode.m"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/AcquireMode/ADDAcquireModeEntity.m"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/VirtualEntity/ADDVirtualAudioInputStream.m"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/VirtualEntity/ADDVirtualAudioOutputStream.m"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/VirtualEntity/ADDVirtualEntity.m"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/VirtualEntity/ADDVirtualMediaClockInputStream.m"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/VirtualEntity/ADDVirtualMediaClockOutputStream.m"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/VirtualEntityState/ADDEntityIDManager.m"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/VirtualEntityState/ADDVirtualEntityPersistentInfoManager.m"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/VirtualMode/ADDAudioDriver.m"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_executables/avbdeviced/VirtualMode/ADDVirtualAudio2.m"

```
