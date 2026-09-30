## ScreensharingAgent

> `/System/Library/CoreServices/RemoteManagement/ScreensharingAgent.bundle/Contents/MacOS/ScreensharingAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-756.34.0.0.0
-  __TEXT.__text: 0x489b8
+756.36.5.2.0
+  __TEXT.__text: 0x4a8b4
   __TEXT.__auth_stubs: 0x1b90
   __TEXT.__objc_stubs: 0x2ac0
   __TEXT.__objc_methlist: 0xea8
-  __TEXT.__const: 0x6ca
-  __TEXT.__oslogstring: 0x8995
-  __TEXT.__cstring: 0x15d4d
-  __TEXT.__gcc_except_tab: 0xb4
+  __TEXT.__const: 0x6da
+  __TEXT.__oslogstring: 0x8dcc
+  __TEXT.__cstring: 0x16380
+  __TEXT.__gcc_except_tab: 0x12c
   __TEXT.__objc_methname: 0x2fe5
   __TEXT.__objc_classname: 0x1a1
   __TEXT.__objc_methtype: 0xa3c
-  __TEXT.__unwind_info: 0x6e8
-  __DATA_CONST.__const: 0x1278
+  __TEXT.__unwind_info: 0x788
+  __DATA_CONST.__const: 0x13b8
   __DATA_CONST.__cfstring: 0x880
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x68

   __DATA.__objc_ivar: 0xd0
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x3328
-  __DATA.__bss: 0x3274
-  __DATA.__common: 0x263d
+  __DATA.__bss: 0x32dc
+  __DATA.__common: 0x2645
   __CGPreLoginApp.__cgpreloginapp: 0x0
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 881
+  Functions: 912
   Symbols:   566
-  CStrings:  2262
+  CStrings:  2300
 
Symbols:
+ _CGEventPostToPid
- _objc_opt_respondsToSelector
CStrings:
+ "ApplyPendingCancelOnDragQueue"
+ "ApplyPendingCancelOnDragQueue_block_invoke"
+ "Applying deferred cancel (%s)"
+ "ArmDragHelperMouseUpGate_block_invoke"
+ "Buffering mouse-up at %d,%d (mask=0x%x)"
+ "CGEventCreate returned NULL"
+ "CreateSyntheticMouseMovementsOnDragQueue"
+ "Deferred synthetic mouse-down at %.1f %.1f"
+ "Dragged"
+ "FlushPendingMouseUpOnDragQueue"
+ "FlushSyntheticDownOnDragQueue"
+ "Generate mouse movement tick %d: %s -> helper pid %d at (%.0f,%.0f) pt"
+ "Moved"
+ "Posted LeftMouseDragged directly to helper pid %d at (%d,%d) pt"
+ "ResetDragHelperMouseUpGate_block_invoke"
+ "ScrapConnectionFinishInitialization"
+ "ScrapConnectionReadFileTransfer sessionID %d pathLen %d"
+ "ScrapConnectionReadFileTransfer: pathLen %d > MAXPATHLEN, dropping"
+ "Using buffered mouse-up pos %.0f,%.0f as synthetic down (captured was %.1f,%.1f)"
+ "agent_SSAgent_CancelDrag_rpc_block_invoke"
+ "agent_SSAgent_PostMouseEvent_rpc_block_invoke"
+ "backstop deadline reached (%d ticks); stopping"
+ "cancel safety timeout"
+ "com.apple.screensharing.agent.dragMouseEventQueue"
+ "current drag %ld  our dragcount %ld"
+ "deferred OpenDragHelperApp(cancel) result %d"
+ "deferred cancel skipped — newer drag has been armed"
+ "deferring cancel - SSDragHelper not in drag loop yet"
+ "flushing buffered mouse-up at %d,%d (%s)"
+ "helper EventLoopReady"
+ "helper entered receiver"
+ "kRFBDragHelperEnteredReceiver"
+ "kRFBDragHelperEventLoopReady"
+ "posting deferred synthetic mouse-down at %.1f,%.1f (%s)"
+ "recovering from dead helper pid:%d; relaunching"
+ "reset (drag ended)"
+ "safety timeout"
+ "safety timeout fired"
+ "skip deferred synthetic mouse-down — drag ended (%s)"
+ "slow-drag: cursor refresh from stale (%.1f,%.1f) pt to current (%.1f,%.1f) pt → (%.0f,%.0f) px at flush time"
- "ScrapConnectionFinishInitilization"
- "posted mouse down at %d %d"
```
