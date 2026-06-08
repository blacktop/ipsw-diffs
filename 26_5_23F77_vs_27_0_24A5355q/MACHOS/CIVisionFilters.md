## CIVisionFilters

> `/System/Library/CoreImage/CIVisionFilters.cifilter/CIVisionFilters`

```diff

-1592.120.2.0.0
-  __TEXT.__text: 0x1054
-  __TEXT.__auth_stubs: 0x230
+1653.0.0.120.2
+  __TEXT.__text: 0x1b14
+  __TEXT.__auth_stubs: 0x440
   __TEXT.__objc_stubs: 0x360
-  __TEXT.__objc_methlist: 0x134
+  __TEXT.__objc_methlist: 0x148
   __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x24a
+  __TEXT.__cstring: 0x29a
+  __TEXT.__gcc_except_tab: 0x138
   __TEXT.__objc_classname: 0x58
-  __TEXT.__objc_methname: 0x372
-  __TEXT.__objc_methtype: 0xa9
+  __TEXT.__objc_methname: 0x380
+  __TEXT.__objc_methtype: 0xb1
   __TEXT.__oslogstring: 0x39
-  __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__auth_got: 0x120
-  __DATA_CONST.__got: 0xf8
+  __TEXT.__unwind_info: 0x100
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__cfstring: 0x240
   __DATA_CONST.__objc_classlist: 0x20

   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__auth_got: 0x230
+  __DATA_CONST.__got: 0xf8
   __DATA.__objc_const: 0x2f0
-  __DATA.__objc_selrefs: 0x130
+  __DATA.__objc_selrefs: 0x138
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x140
   __DATA.__bss: 0x10

   - /System/Library/Frameworks/CoreImage.framework/CoreImage
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/Vision.framework/Vision
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C2A1E01A-23D8-35D9-84A6-23214A2D4F3B
-  Functions: 26
-  Symbols:   78
-  CStrings:  95
+  UUID: 30F67F4D-4FEC-3EC7-90B1-D0EECEAAD5F8
+  Functions: 37
+  Symbols:   112
+  CStrings:  98
 
Symbols:
+ _CFGetTypeID
+ _CVPixelBufferGetTypeID
+ _IOSurfaceGetBaseAddressOfPlane
+ _IOSurfaceGetBytesPerRowOfPlane
+ _IOSurfaceGetCompressionTypeOfPlane
+ _IOSurfaceGetHeightOfPlane
+ _IOSurfaceGetPixelFormat
+ _IOSurfaceGetPlaneCount
+ _IOSurfaceGetTypeID
+ _IOSurfaceGetWidthOfPlane
+ _IOSurfaceLockPlane
+ _IOSurfaceUnlockPlane
+ __Unwind_Resume
+ ___gxx_personality_v0
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x8
+ _objc_retain
+ _objc_retainAutorelease
+ _objc_retain_x1
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_storeStrong
+ _puts
- _objc_setProperty_nonatomic
CStrings:
+ ".cxx_destruct"
+ "Error: a compressed surface/buffer cannot be accessed via its base address."
+ "v16@0:8"

```
