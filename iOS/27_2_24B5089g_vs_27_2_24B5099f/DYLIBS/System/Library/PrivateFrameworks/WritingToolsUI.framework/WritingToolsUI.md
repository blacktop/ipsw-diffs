## WritingToolsUI

> `/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI`

```diff

-151.1.6.0.0
-  __TEXT.__text: 0x6a59c
-  __TEXT.__objc_methlist: 0x4d44
-  __TEXT.__const: 0x30a4
-  __TEXT.__cstring: 0x3737
-  __TEXT.__oslogstring: 0x212d
+151.1.9.0.0
+  __TEXT.__text: 0x6ad18
+  __TEXT.__objc_methlist: 0x4dcc
+  __TEXT.__const: 0x30b4
+  __TEXT.__cstring: 0x3777
+  __TEXT.__oslogstring: 0x21ed
   __TEXT.__gcc_except_tab: 0xdc8
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__swift5_typeref: 0xde2c
   __TEXT.__swift5_capture: 0x45c
-  __TEXT.__swift5_reflstr: 0xe3c
+  __TEXT.__swift5_reflstr: 0xe7c
   __TEXT.__swift5_assocty: 0x290
-  __TEXT.__constg_swiftt: 0xfec
-  __TEXT.__swift5_fieldmd: 0xcbc
+  __TEXT.__constg_swiftt: 0x1004
+  __TEXT.__swift5_fieldmd: 0xce0
   __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_proto: 0x194
   __TEXT.__swift5_types: 0xc0

   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift_as_cont: 0x20
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x25e8
+  __TEXT.__unwind_info: 0x2610
   __TEXT.__eh_frame: 0x8c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xe38
+  __DATA_CONST.__const: 0xe48
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3120
+  __DATA_CONST.__objc_selrefs: 0x3180
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__got: 0xa48
-  __AUTH_CONST.__const: 0x20f0
+  __AUTH_CONST.__const: 0x2108
   __AUTH_CONST.__cfstring: 0xfe0
-  __AUTH_CONST.__objc_const: 0x6968
+  __AUTH_CONST.__objc_const: 0x6a28
   __AUTH_CONST.__objc_intobj: 0x588
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__auth_got: 0xf60
-  __AUTH.__objc_data: 0x14b0
+  __AUTH.__objc_data: 0x14d0
   __AUTH.__data: 0x900
-  __DATA.__objc_ivar: 0x384
+  __DATA.__objc_ivar: 0x390
   __DATA.__data: 0x1ef0
-  __DATA.__common: 0x118
+  __DATA.__common: 0x120
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x90

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3015
-  Symbols:   3216
-  CStrings:  560
+  Functions: 3035
+  Symbols:   3227
+  CStrings:  562
 
Symbols:
+ -[WTMainPopoverViewController adaptivePresentationStyleForPresentationController:traitCollection:]
+ -[WTWritingToolsController _targetIsWebKitTextInput]
+ -[WTWritingToolsController _targetPrefersLimitedUI]
+ -[WTWritingToolsController canPerformRequestedToolOnCurrentSession]
+ -[_WTReplaceTextEffect clipsToDestinationRect]
+ -[_WTReplaceTextEffect setClipsToDestinationRect:]
+ -[_WTTextEffectView hasManagedFrame]
+ -[_WTTextEffectView replaceSourceEffect]
+ -[_WTTextEffectView setHasManagedFrame:]
+ -[_WTTextEffectView setReplaceSourceEffect:]
+ GCC_except_table10
+ GCC_except_table120
+ GCC_except_table126
+ GCC_except_table163
+ GCC_except_table179
+ GCC_except_table182
+ GCC_except_table226
+ GCC_except_table233
+ GCC_except_table235
+ GCC_except_table237
+ GCC_except_table82
+ _OBJC_IVAR_$__WTReplaceTextEffect._clipsToDestinationRect
+ _OBJC_IVAR_$__WTTextEffectView._hasManagedFrame
+ _OBJC_IVAR_$__WTTextEffectView._replaceSourceEffect
+ _keypath_get.30Tm
+ _keypath_get.32Tm
+ _keypath_get.40Tm
+ _keypath_get.52Tm
+ _keypath_set.33Tm
- GCC_except_table119
- GCC_except_table125
- GCC_except_table162
- GCC_except_table178
- GCC_except_table181
- GCC_except_table223
- GCC_except_table230
- GCC_except_table232
- GCC_except_table234
- GCC_except_table62
- GCC_except_table64
- GCC_except_table68
- GCC_except_table81
- _keypath_get.29Tm
- _keypath_get.31Tm
- _keypath_get.39Tm
- _keypath_get.51Tm
- _keypath_set.32Tm
CStrings:
+ "DebugForceUnsafeOutput"
+ "startWritingTools requestedTool=%ld isWritingToolsActive=%d precomputedLen=%lu replacesExisting=%d"
+ "startupOptions: editable=%d wantsInlineEditing=%d targetPrefersLimitedUI=%d isWebKitView=%d precomputedLen=%lu"
+ "targetPrefersLimitedUI"
- "C"
- "startWritingTools"
```
