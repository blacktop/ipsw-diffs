## AccessibilityFoundation

> `/System/Library/PrivateFrameworks/AccessibilitySupport.framework/Versions/A/Frameworks/AccessibilityFoundation.framework/Versions/A/AccessibilityFoundation`

```diff

-  __TEXT.__text: 0x48fec
-  __TEXT.__objc_methlist: 0x6c2c
-  __TEXT.__const: 0x2b8
+  __TEXT.__text: 0x49900
+  __TEXT.__objc_methlist: 0x6c8c
+  __TEXT.__const: 0x2c0
   __TEXT.__cstring: 0x4d4f
-  __TEXT.__oslogstring: 0xd20
-  __TEXT.__gcc_except_tab: 0x37c
+  __TEXT.__oslogstring: 0xe34
+  __TEXT.__gcc_except_tab: 0x35c
   __TEXT.__dlopen_cstrs: 0x117
   __TEXT.__dof_Accessibi: 0x609
-  __TEXT.__unwind_info: 0x1648
+  __TEXT.__unwind_info: 0x1660
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3f80
+  __DATA_CONST.__objc_selrefs: 0x3fb8
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x88
-  __DATA_CONST.__got: 0x608
-  __AUTH_CONST.__const: 0x10f0
+  __DATA_CONST.__got: 0x618
+  __AUTH_CONST.__const: 0x1110
   __AUTH_CONST.__cfstring: 0x6a60
-  __AUTH_CONST.__objc_const: 0xb2e0
+  __AUTH_CONST.__objc_const: 0xb340
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1568
   __AUTH.__data: 0x58
-  __DATA.__objc_ivar: 0x3e4
+  __DATA.__objc_ivar: 0x3ec
   __DATA.__data: 0x540
-  __DATA.__bss: 0x4a0
+  __DATA.__bss: 0x4b0
   __DATA_DIRTY.__objc_data: 0x208
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/Accessibility.framework/Versions/A/Accessibility

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2633
-  Symbols:   5878
-  CStrings:  1847
+  Functions: 2646
+  Symbols:   5909
+  CStrings:  1849
 
Sections:
~ __TEXT.__dof_Accessibi : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[AXFScreen initWithCGDisplayID:]
+ -[_AXFScreenSourceHardware _currentScreensWithMainScreen:totalScreenBounds:]
+ -[_AXFScreenSourceHardware _refreshScreenInfosIfDisplayConfigurationChanged]
+ -[_AXFScreenSourceHardware dealloc]
+ -[_AXFScreenSourceHardware displayConfigurationSignature]
+ -[_AXFScreenSourceHardware lastDisplayConfigurationCheckTime]
+ -[_AXFScreenSourceHardware setDisplayConfigurationSignature:]
+ -[_AXFScreenSourceHardware setLastDisplayConfigurationCheckTime:]
+ AXFSecondsForMachTicks
+ AXFSecondsForMachTicks.onceToken
+ AXFSecondsForMachTicks.secondsPerTick
+ GCC_except_table10
+ OBJC_IVAR_$__AXFScreenSourceHardware._displayConfigurationSignature
+ OBJC_IVAR_$__AXFScreenSourceHardware._lastDisplayConfigurationCheckTime
+ _AXFConvertRectFromQuartzToCocoaSpace
+ _AXFCurrentDisplayConfigurationSignature
+ _AXFSecondsForMachTicks
+ _CGDisplayBounds
+ _CGDisplayCopyDisplayMode
+ _CGDisplayModeGetPixelWidth
+ _CGDisplayModeGetWidth
+ _CGDisplayModeRelease
+ _CGGetActiveDisplayList
+ _CGMainDisplayID
+ _NSStringFromRect
+ ___AXFSecondsForMachTicks_block_invoke
+ _mach_absolute_time
+ _mach_timebase_info
+ _objc_msgSend$_currentScreensWithMainScreen:totalScreenBounds:
+ _objc_msgSend$_refreshScreenInfosIfDisplayConfigurationChanged
+ _objc_msgSend$initWithCGDisplayID:
- GCC_except_table7
CStrings:
+ "AXFScreenSource: CG display[%u] displayID=%u main=%{BOOL}d NSScreen.frame=%{public}@ disagrees with CG frame=%{public}@; preferring CG"
+ "AXFScreenSource: CG display[%u] displayID=%u main=%{BOOL}d frame=%{public}@ scale=%.1f has NO matching NSScreen; using CG as source of truth"

```
