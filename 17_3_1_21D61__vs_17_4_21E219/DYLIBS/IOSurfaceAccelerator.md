## IOSurfaceAccelerator

> `/System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator`

```diff

-146.8.31.0.0
-  __TEXT.__text: 0x2728
-  __TEXT.__auth_stubs: 0x300
-  __TEXT.__cstring: 0xbac
-  __TEXT.__const: 0x40
-  __TEXT.__unwind_info: 0xe4
+147.0.26.0.0
+  __TEXT.__text: 0x2970
+  __TEXT.__auth_stubs: 0x320
+  __TEXT.__cstring: 0xc56
+  __TEXT.__const: 0x58
+  __TEXT.__unwind_info: 0xf0
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x960
-  __AUTH_CONST.__auth_got: 0x180
+  __DATA_CONST.__const: 0x348
+  __AUTH_CONST.__cfstring: 0x9c0
+  __AUTH_CONST.__auth_got: 0x190
   __DATA.__data: 0x8
   __DATA_DIRTY.__const: 0x60
   __DATA_DIRTY.__data: 0x20

   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 007AAAE6-5817-3A37-BDCC-0A650D29174E
-  Functions: 57
-  Symbols:   232
-  CStrings:  224
+  UUID: 46EC1E7D-301E-35C1-BD62-1F50C244E63E
+  Functions: 58
+  Symbols:   238
+  CStrings:  234
 
Symbols:
+ _IOSurfaceAcceleratorGetTransformEstimation
+ _IOSurfaceGetHeight
+ _IOSurfaceGetWidth
+ _kIOSurfaceAcceleratorDutyCycleDuration
+ _kIOSurfaceAcceleratorDutyCycleHistogramDuration
+ _kIOSurfaceAcceleratorPriorityBand
CStrings:
+ "DutyCycleDuration"
+ "Failed to set client property for: %s\n"
+ "HighPriority (kIOSurfaceAcceleratorHighPriorityCString) deprecated!\n"
+ "HistogramDuration"
+ "MailBox"
+ "PriorityBand"
+ "Ring"

```
