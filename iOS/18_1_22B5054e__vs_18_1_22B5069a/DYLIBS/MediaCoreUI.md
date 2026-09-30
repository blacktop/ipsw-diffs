## MediaCoreUI

> `/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI`

```diff

-4024.200.12.0.0
-  __TEXT.__text: 0x25dec0
-  __TEXT.__auth_stubs: 0x5120
+4024.210.1.0.0
+  __TEXT.__text: 0x25ae20
+  __TEXT.__auth_stubs: 0x50f0
   __TEXT.__objc_methlist: 0xd88
-  __TEXT.__const: 0x16724
-  __TEXT.__cstring: 0x89eb
-  __TEXT.__swift5_typeref: 0x139d8
-  __TEXT.__constg_swiftt: 0xe160
+  __TEXT.__const: 0x164f4
+  __TEXT.__cstring: 0x881b
+  __TEXT.__swift5_typeref: 0x139de
+  __TEXT.__constg_swiftt: 0xdf3c
   __TEXT.__swift5_builtin: 0x3e8
-  __TEXT.__swift5_reflstr: 0x64a6
-  __TEXT.__swift5_fieldmd: 0x75c0
-  __TEXT.__swift5_assocty: 0x22e0
-  __TEXT.__swift5_proto: 0xa0c
-  __TEXT.__swift5_types: 0x904
-  __TEXT.__swift5_capture: 0x2e98
+  __TEXT.__swift5_reflstr: 0x63f6
+  __TEXT.__swift5_fieldmd: 0x7504
+  __TEXT.__swift5_assocty: 0x22c8
+  __TEXT.__swift5_proto: 0xa04
+  __TEXT.__swift5_types: 0x8fc
+  __TEXT.__swift5_capture: 0x2e20
   __TEXT.__oslogstring: 0x2fac
   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_mpenum: 0x94
-  __TEXT.__unwind_info: 0x8378
-  __TEXT.__eh_frame: 0x50f8
+  __TEXT.__unwind_info: 0x82e0
+  __TEXT.__eh_frame: 0x5048
   __TEXT.__objc_classname: 0x350
   __TEXT.__objc_methname: 0x73dd
   __TEXT.__objc_methtype: 0x3450
   __TEXT.__objc_stubs: 0x40
   __DATA_CONST.__got: 0x17b8
-  __DATA_CONST.__const: 0x8a8
-  __DATA_CONST.__objc_classlist: 0x338
+  __DATA_CONST.__const: 0x8b0
+  __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1568
   __DATA_CONST.__objc_protorefs: 0x108
-  __AUTH_CONST.__auth_got: 0x2898
-  __AUTH_CONST.__auth_ptr: 0x21a0
-  __AUTH_CONST.__const: 0x151b0
-  __AUTH_CONST.__objc_const: 0xc478
-  __AUTH.__objc_data: 0x1e40
-  __AUTH.__data: 0x3938
-  __DATA.__data: 0x7f60
-  __DATA.__bss: 0xadb0
+  __AUTH_CONST.__auth_got: 0x2880
+  __AUTH_CONST.__auth_ptr: 0x2110
+  __AUTH_CONST.__const: 0x15050
+  __AUTH_CONST.__objc_const: 0xc2e8
+  __AUTH.__objc_data: 0x1dc8
+  __AUTH.__data: 0x36e8
+  __DATA.__data: 0x7f00
+  __DATA.__bss: 0xac90
   __DATA.__common: 0x4d0
   __DATA_DIRTY.__objc_data: 0x1218
-  __DATA_DIRTY.__data: 0x81f8
+  __DATA_DIRTY.__data: 0x8228
   __DATA_DIRTY.__bss: 0x9b80
   __DATA_DIRTY.__common: 0x4a0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 12422
-  Symbols:   854
-  CStrings:  2735
+  Functions: 12355
+  Symbols:   852
+  CStrings:  2722
 
Symbols:
+ _UIFontTextStyleCaption1
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- _UIFontTextStyleCaption2
CStrings:
+ "If you're seeing this, you're impacted by rdar://124036991. If your log is using String(describing:), this error will go away in 18.2. If not, please use String(describing:). To resolve this error immediately, log an unwrapped String instead."
+ "MediaCoreUI.WindowWidthReaderViewController"
+ "_TtC11MediaCoreUI31WindowWidthReaderViewController"
+ "_scrubberCurrentTime"
- "If you're seeing this, you're impacted by rdar://124036991. If your log is using String(describing:), this error will go away in 18.1. If not, please use String(describing:). To resolve this error immediately, log an unwrapped String instead."
- "MediaCoreUI.BlurLayer"
- "MediaCoreUI.LiveColorAdjustmentsLayer"
- "MediaCoreUI.Mask"
- "MediaCoreUI.SnapshotColorAdjustmentsLayer"
- "MediaCoreUI.WindowPropertiesReaderViewController"
- "NowPlayingScrubberProgressAnimation"
- "_TtC11MediaCoreUI16ScrubberPlayhead"
- "_TtC11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A36WindowPropertiesReaderViewController"
- "_displayScale"
- "_leadingTimestampTime"
- "_maximumFramesPerSecond"
- "_playheadPositionTime"
- "currentTime"
- "playhead"
- "playheadPositionTimeLastSet"
- "timelineUpdateInterval"

```
