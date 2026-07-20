## ContinuitySing

> `/System/Library/PrivateFrameworks/ContinuitySing.framework/ContinuitySing`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`

```diff

-758.0.0.122.2
-  __TEXT.__text: 0x5d484
-  __TEXT.__objc_methlist: 0x35d4
+761.0.0.0.3
+  __TEXT.__text: 0x5dc58
+  __TEXT.__objc_methlist: 0x3694
   __TEXT.__const: 0xfa4
   __TEXT.__gcc_except_tab: 0xb94
-  __TEXT.__cstring: 0x60e9
-  __TEXT.__oslogstring: 0x32b9
+  __TEXT.__cstring: 0x6169
+  __TEXT.__oslogstring: 0x3329
   __TEXT.__ustring: 0x2a
   __TEXT.__swift5_typeref: 0x9f6
   __TEXT.__swift5_fieldmd: 0x378

   __TEXT.__swift_as_cont: 0x120
   __TEXT.__swift5_assocty: 0xc8
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__unwind_info: 0x1870
+  __TEXT.__unwind_info: 0x1888
   __TEXT.__eh_frame: 0xf30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x16a8
+  __DATA_CONST.__const: 0x16d0
   __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x80
+  __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a90
+  __DATA_CONST.__objc_selrefs: 0x2af8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x268
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x9d8
   __AUTH_CONST.__const: 0x1400
   __AUTH_CONST.__cfstring: 0x2ee0
-  __AUTH_CONST.__objc_const: 0x7260
+  __AUTH_CONST.__objc_const: 0x7320
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0xd70
   __AUTH.__objc_data: 0x2118
   __AUTH.__data: 0x5b8
-  __DATA.__objc_ivar: 0x478
-  __DATA.__data: 0x968
+  __DATA.__objc_ivar: 0x484
+  __DATA.__data: 0x9c8
   __DATA.__bss: 0x9f8
   __DATA.__common: 0x68
   - /System/Library/Frameworks/AVKit.framework/AVKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1904
-  Symbols:   4111
-  CStrings:  937
+  Functions: 1915
+  Symbols:   4138
+  CStrings:  943
 
Symbols:
+ -[CSPlaybackManager beginScrubbing]
+ -[CSPlaybackManager isSeekable]
+ -[CSPlaybackManager seekToValue:]
+ -[CSPlaybackManager updateScrubbingValue:]
+ -[CSQueuePlaybackControlsView _updateTimelineInteractivity]
+ -[CSQueuePlaybackControlsView mediaTimelineControl:didChangeValue:]
+ -[CSQueuePlaybackControlsView mediaTimelineControlDidEndChanging:]
+ -[CSQueuePlaybackControlsView mediaTimelineControlWillBeginChanging:]
+ _CSRapportDeviceStatusPairedFlags
+ _OBJC_IVAR_$_CSPlaybackManager._pendingSeekActive
+ _OBJC_IVAR_$_CSPlaybackManager._pendingSeekValue
+ _OBJC_IVAR_$_CSQueuePlaybackControlsView._lastScrubValue
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVMediaTimelineControlDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AVMediaTimelineControlDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVMediaTimelineControlDelegate
+ __OBJC_$_PROTOCOL_REFS_AVMediaTimelineControlDelegate
+ __OBJC_LABEL_PROTOCOL_$_AVMediaTimelineControlDelegate
+ __OBJC_PROTOCOL_$_AVMediaTimelineControlDelegate
+ ___33-[CSPlaybackManager seekToValue:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ _objc_msgSend$_updateTimelineInteractivity
+ _objc_msgSend$beginScrubbing
+ _objc_msgSend$changePositionToElapsedInterval:
+ _objc_msgSend$isSeekable
+ _objc_msgSend$seekCommand
+ _objc_msgSend$seekToValue:
+ _objc_msgSend$updateScrubbingValue:
CStrings:
+ "%s: Requesting seek to %f"
+ "%s: Seek request completed. Request: %@"
+ "%s: error performing seek request: %@ error: %@"
+ "-[CSPlaybackManager seekToValue:]"
+ "-[CSPlaybackManager seekToValue:]_block_invoke"
+ "-[CSPlaybackManager seekToValue:]_block_invoke_2"
```
