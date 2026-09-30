## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

```diff

-3500.99.4.0.0
-  __TEXT.__text: 0x4ed50
+3500.99.4.11.1
+  __TEXT.__text: 0x4f10c
   __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0x6014
+  __TEXT.__objc_methlist: 0x6064
   __TEXT.__const: 0x822
-  __TEXT.__cstring: 0xa06d
-  __TEXT.__oslogstring: 0x6dc5
+  __TEXT.__cstring: 0xa0fd
+  __TEXT.__oslogstring: 0x6e87
   __TEXT.__gcc_except_tab: 0xe5c
   __TEXT.__dlopen_cstrs: 0x1bc
   __TEXT.__swift5_typeref: 0x102

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x15f0
+  __TEXT.__unwind_info: 0x1600
   __TEXT.__eh_frame: 0x138
   __TEXT.__objc_classname: 0x101d
-  __TEXT.__objc_methname: 0xdcad
+  __TEXT.__objc_methname: 0xddc0
   __TEXT.__objc_methtype: 0x23b0
-  __TEXT.__objc_stubs: 0x94e0
+  __TEXT.__objc_stubs: 0x95a0
   __DATA_CONST.__got: 0x6a8
   __DATA_CONST.__const: 0x1670
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2de8
+  __DATA_CONST.__objc_selrefs: 0x2e18
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x530
   __AUTH_CONST.__auth_got: 0x600
   __AUTH_CONST.__const: 0x5e8
   __AUTH_CONST.__cfstring: 0x49c0
-  __AUTH_CONST.__objc_const: 0x9ca0
+  __AUTH_CONST.__objc_const: 0x9cd0
   __AUTH_CONST.__objc_intobj: 0x960
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH.__objc_data: 0x1c28
   __AUTH.__data: 0xf0
-  __DATA.__objc_ivar: 0x670
+  __DATA.__objc_ivar: 0x674
   __DATA.__data: 0xf98
   __DATA.__bss: 0x510
   __DATA_DIRTY.__objc_data: 0x4b0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 305724B0-949C-342B-8067-474E44E11BC5
-  Functions: 2164
-  Symbols:   7414
-  CStrings:  4537
+  UUID: 5881B103-1D93-34E3-A2FF-20F138840049
+  Functions: 2171
+  Symbols:   7435
+  CStrings:  4551
 
Symbols:
+ -[SiriActivationService _overrideLockButtonStateIfNeededForRequestOptions:]
+ -[SiriActivationService _updateButtonSourceActiveOverride:activeOverride:]
+ -[SiriLongPressButtonSource _clearActiveOverride]
+ -[SiriLongPressButtonSource _shouldClearActiveOverrideOnInactiveTransition]
+ -[SiriLongPressButtonSource activeChangedTo:]
+ -[SiriLongPressButtonSource activeOverrideSpecified]
+ -[SiriLongPressButtonSource setActiveOverrideSpecified:]
+ GCC_except_table98
+ _OBJC_IVAR_$_SiriLongPressButtonSource._activeOverrideSpecified
+ ___block_literal_global.579
+ ___block_literal_global.584
+ _objc_msgSend$_clearActiveOverride
+ _objc_msgSend$_overrideLockButtonStateIfNeededForRequestOptions:
+ _objc_msgSend$_shouldClearActiveOverrideOnInactiveTransition
+ _objc_msgSend$_updateButtonSourceActiveOverride:activeOverride:
+ _objc_msgSend$activeOverrideSpecified
+ _objc_msgSend$setActiveOverrideSpecified:
- GCC_except_table96
- ___block_literal_global.576
- ___block_literal_global.581
CStrings:
+ "%s #activation Overriding lock button active override for Workout Buddy / Workout Voice Feedback"
+ "%s #activation activeOverride is specified and set to %d"
+ "%s #activation clearing active override"
+ "-[SiriActivationService _overrideLockButtonStateIfNeededForRequestOptions:]"
+ "-[SiriActivationService _updateButtonSourceActiveOverride:activeOverride:]"
+ "-[SiriLongPressButtonSource activeChangedTo:]"
+ "-[SiriLongPressButtonSource isActive]"
+ "TB,V_activeOverrideSpecified"
+ "_activeOverrideSpecified"
+ "_clearActiveOverride"
+ "_overrideLockButtonStateIfNeededForRequestOptions:"
+ "_shouldClearActiveOverrideOnInactiveTransition"
+ "_updateButtonSourceActiveOverride:activeOverride:"
+ "activeOverrideSpecified"
+ "setActiveOverrideSpecified:"
- "-[SiriActivationService presentationManager:updateButtonSourceActiveOverride:activeOverride:]"

```
