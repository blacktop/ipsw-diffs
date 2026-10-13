## LocalAuthenticationPrivateUI

> `/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI`

```diff

-2319.40.43.0.0
-  __TEXT.__text: 0x30d00
-  __TEXT.__objc_methlist: 0x19bc
+2319.42.1.0.0
+  __TEXT.__text: 0x30fec
+  __TEXT.__objc_methlist: 0x1a1c
   __TEXT.__const: 0x918
-  __TEXT.__gcc_except_tab: 0x3804
+  __TEXT.__gcc_except_tab: 0x3868
   __TEXT.__cstring: 0xe18
-  __TEXT.__oslogstring: 0x51d
-  __TEXT.__unwind_info: 0x1648
+  __TEXT.__oslogstring: 0x570
+  __TEXT.__unwind_info: 0x1678
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x558
-  __DATA_CONST.__objc_classlist: 0xc8
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16d0
+  __DATA_CONST.__objc_selrefs: 0x1700
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x188
-  __DATA_CONST.__got: 0x3e0
+  __DATA_CONST.__got: 0x3e8
   __AUTH_CONST.__const: 0x718
   __AUTH_CONST.__cfstring: 0x8a0
-  __AUTH_CONST.__objc_const: 0x3c10
+  __AUTH_CONST.__objc_const: 0x3cb8
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_doubleobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x4b0
+  __AUTH.__objc_data: 0x500
   __DATA.__objc_ivar: 0x374
   __DATA.__data: 0x300
   __DATA_DIRTY.__objc_data: 0x320

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1000
-  Symbols:   1954
-  CStrings:  169
+  Functions: 1006
+  Symbols:   1972
+  CStrings:  170
 
Symbols:
+ +[LAUIPhysicalButtonGeometry sharedInstance]
+ -[LAUIPhysicalButtonGeometry _displayIndexForWindowScene:]
+ -[LAUIPhysicalButtonGeometry _isMultiSurfaceDevice]
+ -[LAUIPhysicalButtonGeometry _normalizedRect]
+ -[LAUIPhysicalButtonGeometry _rectFromAnswer:]
+ -[LAUIPhysicalButtonGeometry normalizedRectForWindowScene:]
+ GCC_except_table13
+ _CFDataGetLength
+ _LAUIPhysicalButtonNormalizedFrameForWindowScene
+ _MGCopyAnswerForDisplayAtIndex
+ _OBJC_CLASS_$_LAUIPhysicalButtonGeometry
+ _OBJC_METACLASS_$_LAUIPhysicalButtonGeometry
+ __OBJC_$_CLASS_METHODS_LAUIPhysicalButtonGeometry
+ __OBJC_$_CLASS_PROP_LIST_LAUIPhysicalButtonGeometry
+ __OBJC_$_INSTANCE_METHODS_LAUIPhysicalButtonGeometry
+ __OBJC_CLASS_RO_$_LAUIPhysicalButtonGeometry
+ __OBJC_METACLASS_RO_$_LAUIPhysicalButtonGeometry
+ __ZZ44+[LAUIPhysicalButtonGeometry sharedInstance]E14sharedInstance
+ __ZZ44+[LAUIPhysicalButtonGeometry sharedInstance]E9onceToken
+ __ZZ51-[LAUIPhysicalButtonGeometry _isMultiSurfaceDevice]E18multiSurfaceDevice
+ __ZZ51-[LAUIPhysicalButtonGeometry _isMultiSurfaceDevice]E9onceToken
+ ___44+[LAUIPhysicalButtonGeometry sharedInstance]_block_invoke
+ ___46-[LAUIPhysicalButtonView _purgeExportedHandle]_block_invoke
+ ___51-[LAUIPhysicalButtonGeometry _isMultiSurfaceDevice]_block_invoke
+ _kMGDisplayIndexedQueryUserIntentPhysicalButtonNormalizedCGRect
- __Z37LAUIPhysicalButtonHasMultipleDisplaysv
- __ZZ33LAUIPhysicalButtonNormalizedFrameE5frame
- __ZZ33LAUIPhysicalButtonNormalizedFrameE9onceToken
- __ZZ37LAUIPhysicalButtonHasMultipleDisplaysvE19hasMultipleDisplays
- __ZZ37LAUIPhysicalButtonHasMultipleDisplaysvE9onceToken
- ___LAUIPhysicalButtonNormalizedFrame_block_invoke
- ____Z37LAUIPhysicalButtonHasMultipleDisplaysv_block_invoke
CStrings:
+ "MG: no button rect for display %ld (error %d); falling back to the primary surface"
```
