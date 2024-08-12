## UniversalDrag

> `/System/Library/PrivateFrameworks/UniversalDrag.framework/UniversalDrag`

```diff

-3.0.0.0.0
-  __TEXT.__text: 0x64718
-  __TEXT.__auth_stubs: 0x1c90
-  __TEXT.__objc_methlist: 0x134
-  __TEXT.__cstring: 0x2e11
-  __TEXT.__const: 0x5b20
-  __TEXT.__constg_swiftt: 0x2764
-  __TEXT.__swift5_typeref: 0x1b71
+4.2.0.0.0
+  __TEXT.__text: 0x6a7b0
+  __TEXT.__auth_stubs: 0x1d00
+  __TEXT.__objc_methlist: 0x15c
+  __TEXT.__cstring: 0x2e87
+  __TEXT.__const: 0x6600
+  __TEXT.__constg_swiftt: 0x29e0
+  __TEXT.__swift5_typeref: 0x1df1
   __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_reflstr: 0xcad
-  __TEXT.__swift5_fieldmd: 0x1bb8
-  __TEXT.__swift5_assocty: 0x180
-  __TEXT.__swift5_proto: 0x500
-  __TEXT.__swift5_types: 0x244
-  __TEXT.__oslogstring: 0x1ab0
-  __TEXT.__swift5_capture: 0x560
-  __TEXT.__swift5_protos: 0x4c
-  __TEXT.__swift5_mpenum: 0x7c
-  __TEXT.__unwind_info: 0x1d90
-  __TEXT.__eh_frame: 0x28c0
+  __TEXT.__swift5_reflstr: 0xdfe
+  __TEXT.__swift5_fieldmd: 0x1e2c
+  __TEXT.__swift5_assocty: 0x198
+  __TEXT.__swift5_proto: 0x5ac
+  __TEXT.__swift5_types: 0x274
+  __TEXT.__oslogstring: 0x1dd0
+  __TEXT.__swift5_capture: 0x574
+  __TEXT.__swift5_protos: 0x50
+  __TEXT.__swift5_mpenum: 0x78
+  __TEXT.__unwind_info: 0x1fd0
+  __TEXT.__eh_frame: 0x2a78
   __TEXT.__objc_classname: 0x5a
-  __TEXT.__objc_methname: 0xb74
+  __TEXT.__objc_methname: 0xbe1
   __TEXT.__objc_methtype: 0x265
-  __DATA_CONST.__got: 0x550
-  __DATA_CONST.__const: 0xc0
-  __DATA_CONST.__objc_classlist: 0x180
+  __DATA_CONST.__got: 0x568
+  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x358
+  __DATA_CONST.__objc_selrefs: 0x3b0
   __DATA_CONST.__objc_protorefs: 0x20
-  __AUTH_CONST.__auth_got: 0xe48
-  __AUTH_CONST.__auth_ptr: 0xbd8
-  __AUTH_CONST.__const: 0x3780
-  __AUTH_CONST.__objc_const: 0x2ca0
-  __AUTH.__objc_data: 0xa08
-  __AUTH.__data: 0x2a20
-  __DATA.__data: 0x1610
-  __DATA.__bss: 0x9800
-  __DATA.__common: 0x150
+  __AUTH_CONST.__auth_got: 0xe80
+  __AUTH_CONST.__auth_ptr: 0xbc0
+  __AUTH_CONST.__const: 0x3ba8
+  __AUTH_CONST.__objc_const: 0x2df8
+  __AUTH.__objc_data: 0xa00
+  __AUTH.__data: 0x2b88
+  __DATA.__data: 0x17f8
+  __DATA.__bss: 0xad00
+  __DATA.__common: 0x158
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
+  - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3029
-  Symbols:   796
-  CStrings:  579
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 3258
+  Symbols:   861
+  CStrings:  605
 
Symbols:
+ _OBJC_CLASS_$_CATransaction
+ _OBJC_CLASS_$__UIDragMonitorSessionPreviewUpdate
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _swift_unknownObjectUnownedDestroy
+ _swift_unknownObjectUnownedInit
+ _swift_unknownObjectUnownedLoadStrong
CStrings:
+ "Destination failed to request data in time"
+ "Drag relay session failed"
+ "DragSurrogateCoordinator: cancelling while prepared, but before began"
+ "Drop not accepted"
+ "Received an update for an item outside our known range -- ignoring it."
+ "UIDragRelaySessionDelegate: didUpdateDragPreviews -- applying updated previews"
+ "UIDragRelaySessionDelegate: didUpdateDragPreviews -- ignoring preview updates because they are reflexive"
+ "UIDragRelaySessionDelegate: dragRelaySession(didEndDragWithDrop:%!{(MISSING)bool}d)"
+ "UIDragRelaySessionDelegate: dragRelaySessionDidBegin"
+ "UIDragRelaySessionDelegate: dragRelaySessionDidEndDataTransfer"
+ "UIDragRelaySessionDelegate: dragRelaySessionDidFail"
+ "_TtC13UniversalDrag16DragPresentation"
+ "_TtC13UniversalDrag20DragPresentationItem"
+ "_boundContext"
+ "addCommitHandler:forPhase:"
+ "anchorPoint"
+ "badge transitioned to %!l(MISSING)d"
+ "badgeStyle"
+ "badgeStyle"
+ "badgeUpdate"
+ "begin"
+ "commit"
+ "components"
+ "didBeginCompletion"
+ "dragForwardingCoordinator activated, but was missing presentation or contents"
+ "dragForwardingCoordinator activated, but was missing presentation or contents"
+ "got empty previews"
+ "hasSeenPreviewsFromOtherSources"
+ "index"
+ "isFromCurrentSession"
+ "presentation"
+ "presentation update doesn't contain previews changes"
+ "preview"
+ "preview"
+ "previewUpdates"
+ "privateDragPresentation"
+ "shieldWindow: commit handler dispatched to MAIN QUEUE"
+ "shieldWindow: viewDidLoad"
+ "shieldWindow: waited too long (> %!f(MISSING) seconds) for shield to render"
+ "size"
+ "surrogate: create shield window"
+ "surrogate: requesting drag relay session start"
+ "surrogate: updatePresentation"
+ "surrogateBeganTracking"
+ "updatePresentation"
+ "waitForRenderingWithTimeout:"
- "Mismatch in expeceted preview count, ignoring preview updates"
- "Requesting drag relay session start"
- "UIDragRelaySessionDelegate: dragDidBegin"
- "UIDragRelaySessionDelegate: dragDidEnd"
- "UIDragRelaySessionDelegate: dragFailed"
- "_TtC13UniversalDrag11DragSession"
- "_isPointerTouch"
- "didAppearCompletion"
- "dragForwardingCoordinator activated, but was missing session or contents"
- "dragForwardingCoordinator activated, but was missing session or contents"
- "ios surrogate: beginDrag"
- "previews"
- "privateDragSession"
- "requestPreviews"
- "session"
- "shiledWindow: viewDidLoad"
- "surrogate: load shield window"
- "surrogate: updatePreviews"
- "v20@0:8B16"
- "viewDidAppear:"

```
