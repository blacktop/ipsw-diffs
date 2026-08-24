## SSDragHelper

> `/System/Library/CoreServices/RemoteManagement/AppleVNCServer.bundle/Contents/Support/SSDragHelper.app/Contents/MacOS/SSDragHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-756.34.0.0.0
-  __TEXT.__text: 0x8384
-  __TEXT.__auth_stubs: 0xb10
-  __TEXT.__objc_stubs: 0x440
+756.36.5.2.0
+  __TEXT.__text: 0x9340
+  __TEXT.__auth_stubs: 0xc20
+  __TEXT.__objc_stubs: 0x480
   __TEXT.__objc_methlist: 0x74
-  __TEXT.__const: 0x68
-  __TEXT.__objc_methname: 0x2b2
-  __TEXT.__oslogstring: 0x10cb
-  __TEXT.__cstring: 0x1a63
+  __TEXT.__const: 0x70
+  __TEXT.__objc_methname: 0x2e9
+  __TEXT.__oslogstring: 0x14c5
+  __TEXT.__cstring: 0x1eee
   __TEXT.__objc_classname: 0x8
   __TEXT.__objc_methtype: 0x63
-  __TEXT.__unwind_info: 0x108
-  __DATA_CONST.__const: 0x80
-  __DATA_CONST.__cfstring: 0x300
+  __TEXT.__unwind_info: 0x120
+  __DATA_CONST.__const: 0xc0
+  __DATA_CONST.__cfstring: 0x320
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x590
-  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__auth_got: 0x618
+  __DATA_CONST.__got: 0xf0
   __DATA.__objc_const: 0x110
-  __DATA.__objc_selrefs: 0x130
+  __DATA.__objc_selrefs: 0x140
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x40
-  __DATA.__bss: 0x44
+  __DATA.__data: 0x58
+  __DATA.__bss: 0x54
   __DATA.__common: 0x1
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 85
-  Symbols:   214
-  CStrings:  268
+  Functions: 89
+  Symbols:   232
+  CStrings:  294
 
Symbols:
+ _CFRunLoopPerformBlock
+ _CFRunLoopWakeUp
+ _CGEventCreate
+ _CGEventCreateMouseEvent
+ _CGEventGetLocation
+ _CGEventPost
+ _CoreDragGetAttributes
+ __exit
+ _close
+ _getppid
+ _kCFRunLoopCommonModes
+ _kevent
+ _kqueue
+ _objc_enumerationMutation
+ _pthread_attr_destroy
+ _pthread_attr_init
+ _pthread_attr_setdetachstate
+ _pthread_create
CStrings:
+ " (CHANGED)"
+ " [moved]"
+ " [tick]"
+ "CGEventCreate(NULL) returned NULL; aborting drag"
+ "CoreDragStartDragging: startPoint=%.1f,%.1f"
+ "ExtractDropPath: AEDesc type='%s' size=%ld"
+ "Going to call exit"
+ "InputProc #%d: cursor=%.1f,%.1f attrsErr=%d attrs=0x%x InsideSender=%d%s processedEnter=%d%s%s"
+ "InputProc: drag entered remote receiver; sentinel write n=%zd"
+ "ParentDeathWatcherThread"
+ "ParentDeathWatcherThread kevent failed errno: %d (%s)"
+ "ParentDeathWatcherThread_block_invoke"
+ "PasteboardClear failed - %d (continuing)"
+ "SSDragHelper started already-orphaned (ppid=%d); exiting"
+ "Signaled event-loop ready"
+ "StartParentDeathWatcher"
+ "com.apple.screensharing.drag"
+ "countByEnumeratingWithState:objects:count:"
+ "distantPast"
+ "err from CoreDragStartDragging - %d (InputProc fired %d times)"
+ "kevent EV_ADD failed for parent pid %d (errno=%d); watcher disabled"
+ "kqueue() failed (errno=%d); parent-death watcher disabled"
+ "parent pid changed during watcher setup (was %d, now %d) -  exiting"
+ "parent process exited; setting cancel flag and kicking the main run loop for graceful drag teardown"
+ "parent-death watcher (main thread): CoreDragGetCurrentDrag=%p; calling CoreDragCancelDrag"
+ "parent-death watcher set for parent pid: %d"
+ "pthread_create for parent-death watcher failed (rc=%d); watcher disabled"
- "err from CoreDragStartDragging - %d"
```
