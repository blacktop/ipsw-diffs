## IOSurfaceAccelerator

> `/System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator`

```diff

-151.25.0.0.0
-  __TEXT.__text: 0x2e7c
+154.20.0.0.0
+  __TEXT.__text: 0x308c
   __TEXT.__auth_stubs: 0x360
-  __TEXT.__cstring: 0xda1
+  __TEXT.__cstring: 0xe66
   __TEXT.__const: 0x50
   __TEXT.__unwind_info: 0x118
   __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x398
+  __DATA_CONST.__const: 0x3b0
   __AUTH_CONST.__auth_got: 0x1b0
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0xa60
+  __AUTH_CONST.__cfstring: 0xac0
   __DATA_DIRTY.__data: 0x20
   __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 92445463-F22B-3519-AE08-842FB0C5EE1A
-  Functions: 77
-  Symbols:   296
-  CStrings:  251
+  UUID: 11C2C698-B6AF-3939-8B28-5992961BECCE
+  Functions: 80
+  Symbols:   304
+  CStrings:  260
 
Symbols:
+ _IOSurfaceAcceleratorSetProperty
+ _IOSurfaceAcceleratorSetProperty.cold.1
+ _kIOSurfaceAcceleratorBorderFillOddSizeYCbCrAlpha
+ _kIOSurfaceAcceleratorBorderFillOddSizeYCbCrEnable
+ _kIOSurfaceAcceleratorBorderFillOddSizeYCbCrLuma
+ _parsePropertiesHelper
Functions:
~ _IOSurfaceAcceleratorCreate : 712 -> 656
~ _prepareTransformBuffersAndOptions : 3304 -> 3412
+ _IOSurfaceAcceleratorSetProperty.cold.1
- __ZL10getBooleanPK14__CFDictionaryPK10__CFString
+ _parsePropertiesHelper
+ _IOSurfaceAcceleratorSetProperty
+ _IOSurfaceAcceleratorCreate.cold.2
CStrings:
+ "BorderFillOddSizeYCbCrAlpha"
+ "BorderFillOddSizeYCbCrEnable"
+ "BorderFillOddSizeYCbCrLuma"
+ "Failed to parse client property\n"
+ "Failed to parse client property for: %d\n"
+ "Failed to set client property for: %d\n"

```
