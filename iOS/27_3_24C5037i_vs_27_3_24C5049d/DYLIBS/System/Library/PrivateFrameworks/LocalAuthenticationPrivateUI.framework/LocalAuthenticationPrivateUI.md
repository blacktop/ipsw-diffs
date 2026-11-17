## LocalAuthenticationPrivateUI

> `/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI`

```diff

-2319.60.18.0.0
-  __TEXT.__text: 0x310e4
-  __TEXT.__objc_methlist: 0x1a1c
+2319.60.22.0.0
+  __TEXT.__text: 0x30f24
+  __TEXT.__objc_methlist: 0x19ec
   __TEXT.__const: 0x938
-  __TEXT.__gcc_except_tab: 0x3888
-  __TEXT.__cstring: 0xe18
-  __TEXT.__oslogstring: 0x5af
-  __TEXT.__unwind_info: 0x1680
+  __TEXT.__gcc_except_tab: 0x387c
+  __TEXT.__cstring: 0xdef
+  __TEXT.__oslogstring: 0x5a5
+  __TEXT.__unwind_info: 0x1668
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1710
+  __DATA_CONST.__objc_selrefs: 0x1708
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x188
-  __DATA_CONST.__got: 0x3e8
-  __AUTH_CONST.__const: 0x718
-  __AUTH_CONST.__cfstring: 0x8a0
+  __DATA_CONST.__got: 0x3f0
+  __AUTH_CONST.__const: 0x6f8
+  __AUTH_CONST.__cfstring: 0x880
   __AUTH_CONST.__objc_const: 0x3cb8
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x2d0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1007
-  Symbols:   1972
-  CStrings:  171
+  Functions: 1001
+  Symbols:   1960
+  CStrings:  170
 
Symbols:
+ _LACDisplayIndexFromLACSurfaceType
+ _OBJC_CLASS_$_LACMobileGestalt
+ _OBJC_CLASS_$_LACUIWindowSceneSurfaceMonitor
- -[LAUIPhysicalButtonGeometry _displayIndexForWindowScene:]
- -[LAUIPhysicalButtonGeometry _isMultiSurfaceDevice]
- -[LAUIPhysicalButtonGeometry _normalizedRect]
- -[LAUIPhysicalButtonGeometry _rectFromAnswer:]
- _CFDataGetBytePtr
- _CFDataGetLength
- _CFDataGetTypeID
- _CFGetTypeID
- _MGCopyAnswer
- _MGCopyAnswerForDisplayAtIndex
- _MGGetLogicalDeviceDisplayCount
- __ZZ51-[LAUIPhysicalButtonGeometry _isMultiSurfaceDevice]E18multiSurfaceDevice
- __ZZ51-[LAUIPhysicalButtonGeometry _isMultiSurfaceDevice]E9onceToken
- ___51-[LAUIPhysicalButtonGeometry _isMultiSurfaceDevice]_block_invoke
- _kMGDisplayIndexedQueryUserIntentPhysicalButtonNormalizedCGRect
CStrings:
+ "MG: no button rect for display %ld; falling back to the primary surface"
+ "MG: querying the button rect for display %ld (surface type %ld)"
- "MG: no button rect for display %ld (error %d); falling back to the primary surface"
- "UserIntentPhysicalButtonNormalizedCGRect"
- "no surface type for scene; falling back to the primary surface"
```
