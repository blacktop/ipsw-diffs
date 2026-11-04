## IOSurfaceAccelerator

> `/System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator`

```diff

-200.69.0.0.0
-  __TEXT.__text: 0x30d8
-  __TEXT.__cstring: 0xf8c
-  __TEXT.__const: 0x50
-  __TEXT.__unwind_info: 0x1a0
+200.74.0.0.0
+  __TEXT.__text: 0x3344
+  __TEXT.__cstring: 0xfed
+  __TEXT.__const: 0x58
+  __TEXT.__unwind_info: 0x1a8
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x3c0
+  __DATA_CONST.__const: 0x3e0
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0xb20

   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 86
-  Symbols:   223
-  CStrings:  178
+  Functions: 89
+  Symbols:   228
+  CStrings:  180
 
Symbols:
+ _IOSurfaceLookup
+ _IOSurfaceSetBulkAttachments2
+ __NSConcreteStackBlock
+ ___IOSurfaceAcceleratorGetHistogram_block_invoke
+ _applyGuestIOSurfaceBulkAttachmentKeys
Functions:
~ _IOSurfaceAcceleratorCreate : 656 -> 664
~ _IOSurfaceAcceleratorGetHistogram : 256 -> 260
+ ___IOSurfaceAcceleratorGetHistogram_block_invoke
~ _IOSurfaceAcceleratorParavirtProcessGuestData : 224 -> 332
+ _applyGuestIOSurfaceBulkAttachmentKeys
CStrings:
+ "applyGuestIOSurfaceBulkAttachmentKeys"
+ "paravirt: failed to attach colour keys to surface %u: %#x\n"
```
