## SiriPlaybackControlFlowTools

> `/System/Library/FlowTools/Tools/SiriPlaybackControlFlowTools.flowtool/SiriPlaybackControlFlowTools`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`

```diff

-3610.10.1.0.0
-  __TEXT.__text: 0x18d60
-  __TEXT.__auth_stubs: 0xfe0
-  __TEXT.__objc_stubs: 0x20
-  __TEXT.__const: 0x2440
+3610.15.2.0.0
+  __TEXT.__text: 0x1fd94
+  __TEXT.__auth_stubs: 0x12d0
+  __TEXT.__objc_stubs: 0x100
+  __TEXT.__const: 0x2540
   __TEXT.__constg_swiftt: 0x3b8
-  __TEXT.__swift5_typeref: 0x79a
-  __TEXT.__swift5_reflstr: 0x4b3
-  __TEXT.__swift5_fieldmd: 0x80c
+  __TEXT.__swift5_typeref: 0x85a
+  __TEXT.__swift5_reflstr: 0x4e8
+  __TEXT.__swift5_fieldmd: 0x824
   __TEXT.__swift5_assocty: 0x2b8
   __TEXT.__swift5_proto: 0x1f0
   __TEXT.__swift5_types: 0x80
-  __TEXT.__swift5_capture: 0xd0
+  __TEXT.__swift5_capture: 0xe0
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__cstring: 0xb6d
+  __TEXT.__cstring: 0xd4d
   __TEXT.__objc_classname: 0x42
-  __TEXT.__objc_methname: 0xfe
-  __TEXT.__objc_methtype: 0x1
-  __TEXT.__oslogstring: 0x55a
-  __TEXT.__swift_as_entry: 0x3c
-  __TEXT.__swift_as_ret: 0x60
-  __TEXT.__swift_as_cont: 0x3c
-  __TEXT.__unwind_info: 0x8e8
-  __TEXT.__eh_frame: 0xa88
-  __DATA_CONST.__const: 0x14a8
+  __TEXT.__objc_methname: 0x186
+  __TEXT.__objc_methtype: 0x22
+  __TEXT.__oslogstring: 0xa6a
+  __TEXT.__swift_as_entry: 0x5c
+  __TEXT.__swift_as_ret: 0x94
+  __TEXT.__swift_as_cont: 0x44
+  __TEXT.__unwind_info: 0xa68
+  __TEXT.__eh_frame: 0xec8
+  __DATA_CONST.__const: 0x14f8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x7f8
-  __DATA_CONST.__got: 0x258
-  __DATA_CONST.__auth_ptr: 0x5f8
-  __DATA.__objc_const: 0x1f8
-  __DATA.__objc_selrefs: 0x8
-  __DATA.__data: 0x8a8
+  __DATA_CONST.__auth_got: 0x970
+  __DATA_CONST.__got: 0x2c0
+  __DATA_CONST.__auth_ptr: 0x628
+  __DATA.__objc_const: 0x238
+  __DATA.__objc_selrefs: 0x40
+  __DATA.__data: 0x920
   __DATA.__common: 0x268
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/FlowToolTypes.framework/FlowToolTypes
   - /System/Library/PrivateFrameworks/SiriPlaybackControlSupport.framework/SiriPlaybackControlSupport
   - /System/Library/PrivateFrameworks/ToolKit.framework/ToolKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 734
-  Symbols:   125
-  CStrings:  126
+  Functions: 873
+  Symbols:   148
+  CStrings:  159
 
Symbols:
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_AFPeerContentTuple
+ _OBJC_CLASS_$_AFPeerInfo
+ _OBJC_CLASS_$_AFSettingsConnection
+ _OBJC_CLASS_$_NSError
+ __NSConcreteStackBlock
+ __swiftEmptySetSingleton
+ _objc_allocWithZone
+ _objc_release_x19
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_retain_x20
+ _objc_retain_x27
+ _swift_continuation_resume
+ _swift_dynamicCast
+ _swift_dynamicCastObjCClass
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _swift_retain_x22
CStrings:
+ "#PlaybackControls MediaPlaybackControlsFlowTool: %{public}s from client AirPlay route %s"
+ "#PlaybackControls MediaPlaybackControlsFlowTool: %{public}s from client media route %s"
+ "#PlaybackControls MediaPlaybackControlsFlowTool: %{public}s from leader %s, deviceIdiom=%{public}s, isCompanionPaired=%{bool,public}d"
+ "#PlaybackControls MediaPlaybackControlsFlowTool: no media route for client %{private}s, reading %{public}s"
+ "#PlaybackControls MediaPlaybackControlsFlowTool: no streams, no now-playing app on the local device"
+ "#PlaybackControls MediaPlaybackControlsFlowTool: reading %{public}s locally"
+ "#PlaybackControls MediaPlaybackControlsFlowTool: targeted pause across %ld streams, naming %ld devices %s with %{public}s"
+ "#PlaybackControls MediaPlaybackControlsFlowTool: targeted pause suppress=%{bool}d"
+ "#PlaybackControls addActionSpecificParameters: seek_to_position %fs is past the end, seeking to %fs"
+ "#PlaybackControls prepareSeek: %fs means the end, but the content has no known length"
+ "#PlaybackControls prepareSeek: client's player unreachable, no duration to clamp to"
+ "#PlaybackControls prepareSeek: device=%s %s"
+ "#PlaybackControls resolveLanguageOption: no %s options on device=%s"
+ "Can't skip to the end: what's playing has no known length."
+ "Down-casted Array element failed to match the target type\nExpected "
+ "Fatal error"
+ "NSArray element failed to match the Swift Array Element type\nExpected "
+ "No devices to pause"
+ "No subtitle or audio language options are available."
+ "None of the named devices can be paused."
+ "Nothing is playing."
+ "RemoveSpeakerIntent"
+ "clientMediaRouteResolver"
+ "code"
+ "content"
+ "deviceInfo"
+ "domain"
+ "durationInfoLookup"
+ "getCrossDeviceContextWithCompletion:"
+ "init"
+ "language options"
+ "userInfo"
+ "v16@?0@\"NSArray\"8"
```
