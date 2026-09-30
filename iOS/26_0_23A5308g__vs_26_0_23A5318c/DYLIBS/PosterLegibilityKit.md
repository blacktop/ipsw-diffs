## PosterLegibilityKit

> `/System/Library/PrivateFrameworks/PosterLegibilityKit.framework/PosterLegibilityKit`

```diff

-289.103.0.0.0
-  __TEXT.__text: 0x19ad0
-  __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_methlist: 0x1ae4
-  __TEXT.__const: 0x300
-  __TEXT.__cstring: 0xd3a
+290.105.0.0.0
+  __TEXT.__text: 0x1aa08
+  __TEXT.__auth_stubs: 0xcd0
+  __TEXT.__objc_methlist: 0x1ba4
+  __TEXT.__const: 0x310
+  __TEXT.__cstring: 0xeef
   __TEXT.__oslogstring: 0xdc4
-  __TEXT.__gcc_except_tab: 0x650
-  __TEXT.__unwind_info: 0x858
+  __TEXT.__gcc_except_tab: 0x67c
+  __TEXT.__unwind_info: 0x8b0
   __TEXT.__objc_classname: 0x4fa
-  __TEXT.__objc_methname: 0x46f2
-  __TEXT.__objc_methtype: 0xca6
-  __TEXT.__objc_stubs: 0x3740
-  __DATA_CONST.__got: 0x368
-  __DATA_CONST.__const: 0x8a0
+  __TEXT.__objc_methname: 0x4813
+  __TEXT.__objc_methtype: 0xcad
+  __TEXT.__objc_stubs: 0x38c0
+  __DATA_CONST.__got: 0x370
+  __DATA_CONST.__const: 0x8c8
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1150
+  __DATA_CONST.__objc_selrefs: 0x11b0
   __DATA_CONST.__objc_superrefs: 0xe8
-  __AUTH_CONST.__auth_got: 0x658
-  __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0xd20
-  __AUTH_CONST.__objc_const: 0x4e98
+  __AUTH_CONST.__auth_got: 0x678
+  __AUTH_CONST.__const: 0x280
+  __AUTH_CONST.__cfstring: 0x1120
+  __AUTH_CONST.__objc_const: 0x4e58
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x20c
+  __DATA.__objc_ivar: 0x204
   __DATA.__data: 0x540
-  __DATA.__bss: 0x100
+  __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F06CCDDF-1AF5-3C62-9773-EFF75351C4D5
-  Functions: 646
-  Symbols:   2739
-  CStrings:  1277
+  UUID: F8AD9E0C-AD1F-3B0B-8C7A-F3D7030153BC
+  Functions: 666
+  Symbols:   2782
+  CStrings:  1349
 
Symbols:
+ +[PLKLegibilityDescriptor performanceLegibilityDescriptorForStyle:options:].cold.1
+ +[PLKLegibilityDescriptor performanceLegibilityDescriptorForStyle:options:].cold.2
+ -[PLKLegibilityBackgroundContentDescriptor descriptionBuilderWithMultilinePrefix:]
+ -[PLKLegibilityContentDescriptor descriptionBuilderWithMultilinePrefix:]
+ -[PLKLegibilityContentDescriptor descriptionWithMultilinePrefix:]
+ -[PLKLegibilityContentDescriptor description]
+ -[PLKLegibilityContentDescriptor succinctDescriptionBuilder]
+ -[PLKLegibilityContentDescriptor succinctDescription]
+ -[PLKLegibilityDescriptor descriptionBuilderWithMultilinePrefix:]
+ -[PLKLegibilityDescriptor descriptionWithMultilinePrefix:]
+ -[PLKLegibilityDescriptor description]
+ -[PLKLegibilityDescriptor initWithStyle:foregroundContentDescriptor:backgroundContentDescriptor:]
+ -[PLKLegibilityDescriptor succinctDescriptionBuilder]
+ -[PLKLegibilityDescriptor succinctDescription]
+ -[PLKLegibilityForegroundContentDescriptor descriptionBuilderWithMultilinePrefix:]
+ -[PLKLegibilityView _commonInit]
+ -[PLKLegibilityView initWithFrame:]
+ -[PLKUILegibilitySettingsBackgroundContentDescriptor descriptionBuilderWithMultilinePrefix:]
+ _CGColorGetColorSpace
+ _CGColorSpaceGetName
+ _OBJC_EHTYPE_$_NSException
+ ___52+[PLKColorBoxes colorBoxesForAverageColor:contrast:]_block_invoke
+ ___52+[PLKColorBoxes colorBoxesForAverageColor:contrast:]_block_invoke.cold.1
+ ___75+[PLKLegibilityDescriptor performanceLegibilityDescriptorForStyle:options:]_block_invoke_2
+ ___block_descriptor_56_e8_32s_e21_C24?0d8"NSString"16ls32l8
+ ___block_literal_global.203
+ ___block_literal_global.257
+ __os_log_fault_impl
+ _defaultContentDescriptor.onceToken.255
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_msgSend$_commonInit
+ _objc_msgSend$allowsGroupOpacity
+ _objc_msgSend$appendBool:withName:
+ _objc_msgSend$appendFloat:withName:
+ _objc_msgSend$appendObject:withName:
+ _objc_msgSend$appendObject:withName:skipIfNil:
+ _objc_msgSend$cacheKey
+ _objc_msgSend$descriptionBuilderWithMultilinePrefix:
+ _objc_msgSend$descriptionWithMultilinePrefix:
+ _objc_msgSend$initWithStyle:foregroundContentDescriptor:backgroundContentDescriptor:
+ _objc_msgSend$succinctDescriptionBuilder
+ _objc_msgSend$usesUILegibility
+ _objc_msgSend$valueForKey:
+ _performanceLegibilityDescriptorForStyle:options:.legibilityDescriptorsDefault
+ _performanceLegibilityDescriptorForStyle:options:.legibilityDescriptorsNoVibrant
+ _performanceLegibilityDescriptorForStyle:options:.onceTokenDefault
+ _performanceLegibilityDescriptorForStyle:options:.onceTokenNoVibrant
- +[PLKColorBoxes colorBoxesForAverageColor:contrast:].cold.4
- +[PLKColorBoxes colorBoxesForAverageColor:contrast:].cold.5
- +[PLKColorBoxes colorBoxesForAverageColor:contrast:].cold.6
- +[PLKColorBoxes colorBoxesForAverageColor:contrast:].cold.7
- +[PLKColorBoxes colorBoxesForAverageColor:contrast:].cold.8
- +[PLKColorBoxes colorBoxesForImage:].cold.3
- +[PLKColorBoxes colorBoxesForImage:].cold.4
- +[PLKColorBoxes colorBoxesForImage:].cold.5
- _OBJC_IVAR_$_PLKLegibilityView._backgroundView
- _OBJC_IVAR_$_PLKLegibilityView._foregroundView
- ___assert_rtn
- ___block_literal_global.181
- _contrast.cold.1
- _defaultContentDescriptor.onceToken.179
- _objc_msgSend$initWithForegroundContentDescriptor:backgroundContentDescriptor:
- _performanceLegibilityDescriptorForStyle:options:.legibilityDescriptors
- _performanceLegibilityDescriptorForStyle:options:.onceToken
- _saturation.cold.1
CStrings:
+ "\t"
+ "%@ component out of bounds. value: %lu, color: %@, colorSpace: %@"
+ "(null)"
+ "@40@0:8Q16@24@32"
+ "C24@?0d8@\"NSString\"16"
+ "DarkContent"
+ "LightContent"
+ "T@\"UIView\",R,N,V_contentView"
+ "T@\"UIView\",R,N,V_shadowView"
+ "Unknown(%ld)"
+ "_commonInit"
+ "appendBool:withName:"
+ "appendFloat:withName:"
+ "appendObject:withName:"
+ "appendObject:withName:skipIfNil:"
+ "blue"
+ "colorMatrix"
+ "descriptionBuilderWithMultilinePrefix:"
+ "descriptionWithMultilinePrefix:"
+ "green"
+ "initWithFrame:"
+ "initWithStyle:foregroundContentDescriptor:backgroundContentDescriptor:"
+ "m11:%.3f m15:%.3f m21:%.3f m25:%.3f"
+ "red"
+ "succinctDescription"
+ "succinctDescriptionBuilder"
+ "valueForKey:"
- "0 <= lx && lx <= 255"
- "@\"UIView\""
- "T@\"UIView\",R,N,V_backgroundView"
- "T@\"UIView\",R,N,V_foregroundView"
- "_backgroundView"
- "_foregroundView"
- "round_to_uint8"

```
