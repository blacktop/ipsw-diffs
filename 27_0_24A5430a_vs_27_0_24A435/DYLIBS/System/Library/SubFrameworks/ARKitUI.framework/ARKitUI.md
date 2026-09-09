## ARKitUI

> `/System/Library/SubFrameworks/ARKitUI.framework/ARKitUI`

```diff

 781.0.7.0.0
-  __TEXT.__text: 0x2b478
-  __TEXT.__objc_methlist: 0x2950
-  __TEXT.__const: 0x938
-  __TEXT.__cstring: 0xdb4
-  __TEXT.__oslogstring: 0x1830
+  __TEXT.__text: 0x2b9b4
+  __TEXT.__objc_methlist: 0x2988
+  __TEXT.__const: 0x948
+  __TEXT.__oslogstring: 0x192e
+  __TEXT.__cstring: 0xdcf
   __TEXT.__gcc_except_tab: 0xcd8
-  __TEXT.__unwind_info: 0xc18
+  __TEXT.__unwind_info: 0xc20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2288
+  __DATA_CONST.__objc_selrefs: 0x22c0
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__got: 0x590
-  __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0xc20
-  __AUTH_CONST.__objc_const: 0x75c8
+  __AUTH_CONST.__const: 0x3c0
+  __AUTH_CONST.__cfstring: 0xc60
+  __AUTH_CONST.__objc_const: 0x7648
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x10e0
-  __DATA.__objc_ivar: 0x588
+  __DATA.__objc_ivar: 0x594
   __DATA.__data: 0x380
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 979
-  Symbols:   3047
-  CStrings:  230
+  Functions: 987
+  Symbols:   3060
+  CStrings:  235
 
Symbols:
+ -[ARCoachingAnimationView updateGlyphForDisplayRegionIfNeeded:]
+ -[ARCoachingOverlayView displayRegionOverrideEnabled]
+ -[ARCoachingOverlayView displayRegionOverride]
+ -[ARCoachingOverlayView setDisplayRegionOverride:]
+ -[ARCoachingOverlayView setDisplayRegionOverrideEnabled:]
+ _ARCoachingDeviceGlyphNameForDisplayRegion
+ _ARDeviceIsV68
+ _OBJC_IVAR_$_ARCoachingAnimationView._currentGlyphName
+ _OBJC_IVAR_$_ARCoachingOverlayView._displayRegionOverride
+ _OBJC_IVAR_$_ARCoachingOverlayView._displayRegionOverrideEnabled
+ _objc_msgSend$displayRegion
+ _objc_msgSend$setDisplayRegion:
+ _objc_msgSend$updateGlyphForDisplayRegionIfNeeded:
CStrings:
+ "%{public}@ <%p>: Coaching display region glyph changed (%@ -> %@), rebuilding renderer"
+ "%{public}@ <%p>: Overriding ARFrame display region to be %ld"
+ "Call ARCoachingDeviceGlyphNameForDisplayRegion on %@ instead. Falling back to unspecified display region."
+ "DeviceF-V68"
+ "DeviceG-V68"
+ "\xf0r"
- "\xf0b"
```
