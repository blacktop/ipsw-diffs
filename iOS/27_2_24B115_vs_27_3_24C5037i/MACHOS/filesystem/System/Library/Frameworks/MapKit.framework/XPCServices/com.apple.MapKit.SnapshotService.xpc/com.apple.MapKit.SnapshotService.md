## com.apple.MapKit.SnapshotService

> `/System/Library/Frameworks/MapKit.framework/XPCServices/com.apple.MapKit.SnapshotService.xpc/com.apple.MapKit.SnapshotService`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2552.31.6.17.14
-  __TEXT.__text: 0x2264
-  __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_stubs: 0x820
-  __TEXT.__objc_methlist: 0x27c
-  __TEXT.__const: 0xb8
+2552.32.9.10.5
+  __TEXT.__text: 0x2a2c
+  __TEXT.__auth_stubs: 0x430
+  __TEXT.__objc_stubs: 0x8a0
+  __TEXT.__objc_methlist: 0x2a4
+  __TEXT.__const: 0xe0
   __TEXT.__dlopen_cstrs: 0x41
-  __TEXT.__gcc_except_tab: 0xec
-  __TEXT.__cstring: 0x2c5
-  __TEXT.__objc_methname: 0x870
+  __TEXT.__gcc_except_tab: 0x100
+  __TEXT.__cstring: 0x328
+  __TEXT.__objc_methname: 0x8d8
   __TEXT.__objc_classname: 0x6a
-  __TEXT.__objc_methtype: 0x293
-  __TEXT.__oslogstring: 0x2c1
-  __TEXT.__unwind_info: 0x138
+  __TEXT.__objc_methtype: 0x2a0
+  __TEXT.__oslogstring: 0x463
+  __TEXT.__unwind_info: 0x158
   __DATA_CONST.__const: 0x1b8
-  __DATA_CONST.__cfstring: 0xa0
+  __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0x210
+  __DATA_CONST.__auth_got: 0x228
   __DATA_CONST.__got: 0xa0
-  __DATA.__objc_const: 0x590
-  __DATA.__objc_selrefs: 0x2d0
-  __DATA.__objc_ivar: 0x3c
+  __DATA.__objc_const: 0x5c0
+  __DATA.__objc_selrefs: 0x2f0
+  __DATA.__objc_ivar: 0x40
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/VectorKit.framework/VectorKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 43
-  Symbols:   93
-  CStrings:  195
+  Functions: 50
+  Symbols:   96
+  CStrings:  211
 
Symbols:
+ _GEOConfigGetDouble
+ _dispatch_after
+ _dispatch_time
CStrings:
+ "B"
+ "Cleaned up request %{public}llu for process %d (usedPixels %ld)"
+ "Ignoring cleanup for request %{public}llu from process %d (never started)"
+ "Keeping serialization slot for process %d (owned by request %{public}llu, not %{public}llu)"
+ "MapKitConfig_SnapshotServiceQueuedRequestTimeout"
+ "Pixel accounting went negative (%ld) cleaning up request %{public}llu"
+ "Starting snapshot request %{public}llu for process %d (usedPixels %ld, pending %lu)"
+ "TB,N,GisStarted,V_started"
+ "Timed out request %{public}llu for process %d after waiting %{public}.1f s in the queue"
+ "Timed out waiting for an available snapshot slot."
+ "_started"
+ "_timeOutQueuedRequest:"
+ "containsObject:"
+ "isStarted"
+ "setStarted:"
+ "started"
+ "v20@0:8B16"
- "Starting snapshot request %{public}llu for process %d"
```
