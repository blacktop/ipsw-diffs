## UniversalDrag

> `/System/Library/PrivateFrameworks/UniversalDrag.framework/UniversalDrag`

```diff

-11.0.0.0.0
-  __TEXT.__text: 0x6c0e0
-  __TEXT.__auth_stubs: 0x1d00
-  __TEXT.__objc_methlist: 0x16c
-  __TEXT.__cstring: 0x2e97
-  __TEXT.__const: 0x6640
-  __TEXT.__constg_swiftt: 0x2a54
-  __TEXT.__swift5_typeref: 0x1e17
-  __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_reflstr: 0xe2e
-  __TEXT.__swift5_fieldmd: 0x1e44
+16.0.0.0.0
+  __TEXT.__text: 0x6e548
+  __TEXT.__auth_stubs: 0x1db0
+  __TEXT.__objc_methlist: 0x17c
+  __TEXT.__cstring: 0x3017
+  __TEXT.__const: 0x6740
+  __TEXT.__constg_swiftt: 0x2af0
+  __TEXT.__swift5_typeref: 0x1eaf
+  __TEXT.__swift5_builtin: 0x17c
+  __TEXT.__swift5_reflstr: 0xeae
+  __TEXT.__swift5_fieldmd: 0x1e9c
   __TEXT.__swift5_assocty: 0x198
-  __TEXT.__swift5_proto: 0x5ac
-  __TEXT.__swift5_types: 0x274
-  __TEXT.__oslogstring: 0x2165
-  __TEXT.__swift5_capture: 0x580
+  __TEXT.__swift5_proto: 0x5b8
+  __TEXT.__swift5_types: 0x27c
+  __TEXT.__oslogstring: 0x23f5
+  __TEXT.__swift5_capture: 0x5e0
   __TEXT.__swift5_protos: 0x50
   __TEXT.__swift5_mpenum: 0x84
-  __TEXT.__unwind_info: 0x1fc8
+  __TEXT.__unwind_info: 0x2028
   __TEXT.__eh_frame: 0x2a68
-  __TEXT.__objc_classname: 0x5a
-  __TEXT.__objc_methname: 0xc1a
-  __TEXT.__objc_methtype: 0x287
-  __DATA_CONST.__got: 0x568
-  __DATA_CONST.__const: 0x100
+  __TEXT.__objc_classname: 0xa0
+  __TEXT.__objc_methname: 0xd96
+  __TEXT.__objc_methtype: 0x40c
+  __DATA_CONST.__got: 0x5a0
+  __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0x188
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3c0
-  __DATA_CONST.__objc_protorefs: 0x20
-  __AUTH_CONST.__auth_got: 0xe80
-  __AUTH_CONST.__auth_ptr: 0xbe8
-  __AUTH_CONST.__const: 0x3b80
-  __AUTH_CONST.__objc_const: 0x2e58
-  __AUTH.__objc_data: 0xa08
-  __AUTH.__data: 0x2be8
-  __DATA.__data: 0x17f8
-  __DATA.__bss: 0xad00
+  __DATA_CONST.__objc_selrefs: 0x3e8
+  __DATA_CONST.__objc_protorefs: 0x38
+  __AUTH_CONST.__auth_got: 0xed8
+  __AUTH_CONST.__auth_ptr: 0xbd0
+  __AUTH_CONST.__const: 0x3cb8
+  __AUTH_CONST.__objc_const: 0x3068
+  __AUTH.__objc_data: 0xa58
+  __AUTH.__data: 0x2c08
+  __DATA.__data: 0x19a8
+  __DATA.__bss: 0xae80
   __DATA.__common: 0x158
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3293
-  Symbols:   888
-  CStrings:  622
+  Functions: 3349
+  Symbols:   907
+  CStrings:  664
 
Symbols:
+ _OBJC_CLASS_$_OS_dispatch_source
+ _OBJC_CLASS_$_UIDropInteraction
+ _objc_release_x9
CStrings:
+ "@\"UIDropProposal\"32@0:8@\"UIDropInteraction\"16@\"<UIDropSession>\"24"
+ "@\"UITargetedDragPreview\"40@0:8@\"UIDropInteraction\"16@\"UIDragItem\"24@\"UITargetedDragPreview\"32"
+ "@40@0:8@16@24@32"
+ "B32@0:8@\"UIDropInteraction\"16@\"<UIDropSession>\"24"
+ "B32@0:8@16@24"
+ "DragForwarder_iOS: iOS doesn't support scale factors other than 1.0"
+ "DragSurrogateCoordinator: ignoring %!{(MISSING)public}s while completed"
+ "DragSurrogateCoordinator: set badge style (while active)%!s(MISSING)"
+ "DragSurrogateCoordinator: set badge style (while preparing) %!s(MISSING)"
+ "DragSurrogateCoordinator: set badge style (while starting)%!s(MISSING)"
+ "DragSurrogate_iOS: readyToResumeEventsHandler"
+ "OS_dispatch_source"
+ "OS_dispatch_source_timer"
+ "ShieldViewController: failed to receieve dropInteraction proposal in a timely fashion. Resuming HID event delivery, but the drag operation will fail."
+ "ShieldViewController: received drop interaction proposal. Calling completion handler to resume HID event delivery."
+ "UIDropInteractionDelegate"
+ "addInteraction:"
+ "dragMonitorSession didConcludeDragNormally %!{(MISSING)bool}d"
+ "dropInteraction:canHandleSession:"
+ "dropInteraction:concludeDrop:"
+ "dropInteraction:item:willAnimateDropWithAnimator:"
+ "dropInteraction:performDrop:"
+ "dropInteraction:previewForDroppingItem:withDefault:"
+ "dropInteraction:sessionDidEnd:"
+ "dropInteraction:sessionDidEnter:"
+ "dropInteraction:sessionDidExit:"
+ "dropInteraction:sessionDidUpdate:"
+ "hasCalledResumeHandler"
+ "initWithDelegate:"
+ "previewScaleFactor"
+ "readyToResumeEventsHandler"
+ "setAllowsHitTesting:"
+ "surrogate: iOS doesn't support scale factors other than 1.0"
+ "timeout waiting for next chunck of data"
+ "touchesBeganHandler"
+ "unknown badge style: "
+ "v32@0:8@\"UIDropInteraction\"16@\"<UIDropSession>\"24"
+ "v40@0:8@\"UIDropInteraction\"16@\"UIDragItem\"24@\"<UIDragAnimating>\"32"
+ "v40@0:8@16@24@32"
+ "watchdogTimer"

```
