## AppleProResHWEncoder.videoencoder

> `/System/Library/VideoEncoders/AppleProResHWEncoder.videoencoder`

```diff

-600.45.0.0.0
-  __TEXT.__text: 0x209c8
+600.53.0.0.0
+  __TEXT.__text: 0x203c4
   __TEXT.__const: 0x746f0
   __TEXT.__gcc_except_tab: 0x310
   __TEXT.__cstring: 0x1491
-  __TEXT.__oslogstring: 0x4151
+  __TEXT.__oslogstring: 0x4140
   __TEXT.__unwind_info: 0x440
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__weak_got: 0x8

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 494
+  Functions: 496
   Symbols:   593
   CStrings:  414
 
CStrings:
+ "AppleProResHW (0x%x): %s(): Invalid Homography Matrix size: %zu, expected: %zu"
+ "ERROR AppleProResHW (0x%x): %d: %s(): LSC metadata keys not present in metadataDictionary\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): VDD metadata keys not present in metadataDictionary\n"
- "WARNING AppleProResHW (0x%x): %d: %s(): Invalid Homography Matrix size: %zu, expected: %zu\n"
- "WARNING AppleProResHW (0x%x): %d: %s(): LSC metadata keys not present in metadataDictionary\n"
- "WARNING AppleProResHW (0x%x): %d: %s(): VDD metadata keys not present in metadataDictionary\n"
```
