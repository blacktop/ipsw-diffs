## HomeUI

> `/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI`

```diff

-1136.3.4.1.1
-  __TEXT.__text: 0x6a3788
+1136.3.5.1.3
+  __TEXT.__text: 0x6a3760
   __TEXT.__auth_stubs: 0x74a0
-  __TEXT.__objc_methlist: 0x4f2bc
+  __TEXT.__objc_methlist: 0x4f2c4
   __TEXT.__const: 0x11218
   __TEXT.__dlopen_cstrs: 0x2a0
-  __TEXT.__cstring: 0x47880
+  __TEXT.__cstring: 0x4785f
   __TEXT.__swift5_typeref: 0xc4fe
   __TEXT.__swift5_fieldmd: 0x4a6c
   __TEXT.__constg_swiftt: 0x8f58

   __TEXT.__swift5_protos: 0x58
   __TEXT.__swift5_proto: 0x778
   __TEXT.__swift5_types: 0x568
-  __TEXT.__oslogstring: 0x26cbd
+  __TEXT.__oslogstring: 0x26cb0
   __TEXT.__swift5_capture: 0x2a64
   __TEXT.__swift_as_entry: 0x2a0
   __TEXT.__swift_as_ret: 0x2c0
   __TEXT.__swift5_mpenum: 0x4c
-  __TEXT.__gcc_except_tab: 0x9e5c
+  __TEXT.__gcc_except_tab: 0x9e88
   __TEXT.__ustring: 0x7e
-  __TEXT.__unwind_info: 0x17590
+  __TEXT.__unwind_info: 0x175a8
   __TEXT.__eh_frame: 0xb340
-  __TEXT.__objc_classname: 0xcad1
-  __TEXT.__objc_methname: 0xae738
+  __TEXT.__objc_classname: 0xcad2
+  __TEXT.__objc_methname: 0xae79b
   __TEXT.__objc_methtype: 0x15e75
-  __TEXT.__objc_stubs: 0x6c640
+  __TEXT.__objc_stubs: 0x6c660
   __DATA_CONST.__got: 0x6408
   __DATA_CONST.__const: 0xf058
   __DATA_CONST.__objc_classlist: 0x27c0
   __DATA_CONST.__objc_catlist: 0x208
   __DATA_CONST.__objc_protolist: 0x1270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21ca0
+  __DATA_CONST.__objc_selrefs: 0x21cb0
   __DATA_CONST.__objc_protorefs: 0x6b0
   __DATA_CONST.__objc_superrefs: 0x1ea8
   __DATA_CONST.__objc_arraydata: 0x9c0
   __AUTH_CONST.__auth_got: 0x3a60
   __AUTH_CONST.__const: 0x128a0
-  __AUTH_CONST.__cfstring: 0x22780
-  __AUTH_CONST.__objc_const: 0x8c640
+  __AUTH_CONST.__cfstring: 0x22760
+  __AUTH_CONST.__objc_const: 0x8c670
   __AUTH_CONST.__objc_intobj: 0x1c38
   __AUTH_CONST.__objc_arrayobj: 0x4f8
   __AUTH_CONST.__objc_dictobj: 0x5c8

   __AUTH_CONST.__objc_floatobj: 0x40
   __AUTH.__objc_data: 0x1a648
   __AUTH.__data: 0x3278
-  __DATA.__objc_ivar: 0x1870
+  __DATA.__objc_ivar: 0x1874
   __DATA.__data: 0x10538
   __DATA.__objc_stublist: 0x40
   __DATA.__bss: 0xd7d0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 11B75323-8C5E-3D92-B566-C8B08228906F
-  Functions: 38111
-  Symbols:   88202
-  CStrings:  43150
+  UUID: 626F4E06-CFF0-31A4-87AE-0A60873C2F76
+  Functions: 38114
+  Symbols:   88212
+  CStrings:  43151
 
Symbols:
+ -[HUClipScrubberDataSource setSnapshotQueue:]
+ -[HUClipScrubberDataSource snapshotQueue]
+ _OBJC_IVAR_$_HUClipScrubberDataSource._snapshotQueue
+ ___50-[HUClipScrubberDataSource _addDiffableDataSource]_block_invoke.18
+ ___53-[HUClipScrubberDataSource _updateSnapshotForEditing]_block_invoke
+ ___86-[HUClipScrubberDataSource _snapshotForEvents:updatedIdentifiers:replacedIdentifiers:]_block_invoke.31
+ ___86-[HUClipScrubberDataSource _updateSnapshotWithUpdatedIdentifiers:replacedIdentifiers:]_block_invoke
+ _objc_msgSend$snapshotQueue
+ _objc_msgSend$updatePlaybackPositionToDate:usingClip:
- -[HUCameraEventRecordingCell description]
- ___50-[HUClipScrubberDataSource _addDiffableDataSource]_block_invoke.17
- ___86-[HUClipScrubberDataSource _snapshotForEvents:updatedIdentifiers:replacedIdentifiers:]_block_invoke.28
- _objc_msgSend$updatePlaybackPositionToDate:withEvent:
CStrings:
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_snapshotQueue"
+ "_snapshotQueue"
+ "com.apple.Home.HUClipScrubberDataSource.snapshotQueue"
+ "setSnapshotQueue:"
+ "snapshotQueue"
+ "updatePlaybackPositionToDate:usingClip:"
- "%s %@ → %@"
- "-[HUNCCameraScrubberViewController playbackEngine:didUpdateEventCache:]"
- "updatePlaybackPositionToDate:withEvent:"

```
