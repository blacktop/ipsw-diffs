## CarPlay

> `/System/Library/Frameworks/CarPlay.framework/CarPlay`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-537.3.0.0.0
-  __TEXT.__text: 0x6f144
-  __TEXT.__objc_methlist: 0x9a40
+540.1.0.0.0
+  __TEXT.__text: 0x6f68c
+  __TEXT.__objc_methlist: 0x9a78
   __TEXT.__const: 0x552
-  __TEXT.__cstring: 0x59b6
-  __TEXT.__oslogstring: 0x3436
+  __TEXT.__cstring: 0x5a26
+  __TEXT.__oslogstring: 0x34d6
   __TEXT.__gcc_except_tab: 0x9bc
   __TEXT.__constg_swiftt: 0x1f8
   __TEXT.__swift5_typeref: 0x13d

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_fieldmd: 0x7c
-  __TEXT.__unwind_info: 0x1f78
+  __TEXT.__unwind_info: 0x1f70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1f18
+  __DATA_CONST.__const: 0x1f50
   __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x2e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4350
+  __DATA_CONST.__objc_selrefs: 0x4368
   __DATA_CONST.__objc_protorefs: 0x160
   __DATA_CONST.__objc_superrefs: 0x348
   __DATA_CONST.__got: 0x860
   __AUTH_CONST.__const: 0xbc8
-  __AUTH_CONST.__cfstring: 0x5640
-  __AUTH_CONST.__objc_const: 0x214e0
+  __AUTH_CONST.__cfstring: 0x5680
+  __AUTH_CONST.__objc_const: 0x21510
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x6c8
   __AUTH.__objc_data: 0x48
-  __DATA.__objc_ivar: 0xa34
+  __DATA.__objc_ivar: 0xa38
   __DATA.__data: 0x2050
   __DATA.__bss: 0x590
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3374
-  Symbols:   7875
-  CStrings:  1090
+  Functions: 3382
+  Symbols:   7883
+  CStrings:  1094
 
Symbols:
+ +[CPRouteDetail routeDetailWithInfo:]
+ +[CPRouteDetail routeDetailWithParking:]
+ -[CPInterfaceController _setupTemplateVersionAndSupportedSelectorsWithCompletion:]
+ -[CPInterfaceController lastOverlaidTemplate]
+ -[CPInterfaceController setLastOverlaidTemplate:]
+ -[CPMapPanel setSections:]
+ -[CPNavigationAlert setShowsCloseButton:]
+ -[CPNavigationAlert showsCloseButton]
+ -[CPTemplateApplicationDashboardScene _updateSceneTraitsAndPushTraitsToScreen:callParentWillTransitionToTraitCollection:]
+ -[CPTemplateApplicationInstrumentClusterScene _updateSceneTraitsAndPushTraitsToScreen:callParentWillTransitionToTraitCollection:]
+ -[CPTemplateApplicationScene _updateSceneTraitsAndPushTraitsToScreen:callParentWillTransitionToTraitCollection:]
+ GCC_except_table132
+ GCC_except_table23
+ GCC_except_table29
+ GCC_except_table60
+ GCC_except_table77
+ _CPRouteDetailStringForType
+ _OBJC_IVAR_$_CPInterfaceController._lastOverlaidTemplate
+ _OBJC_IVAR_$_CPNavigationAlert._showsCloseButton
+ ___64-[CPInterfaceController hideOverlayTemplateAnimated:completion:]_block_invoke_2
+ ___65-[CPInterfaceController showOverlayTemplate:animated:completion:]_block_invoke_2
+ ___82-[CPInterfaceController _setupTemplateVersionAndSupportedSelectorsWithCompletion:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e18_v24?0Q8"NSSet"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ _objc_msgSend$_panelForIdentifier:
+ _objc_msgSend$_setupTemplateVersionAndSupportedSelectorsWithCompletion:
- -[CPInterfaceController _completeSetupWithCompletion:]
- -[CPRouteDetail labelTintColor]
- -[CPRouteDetail setLabelTintColor:]
- -[CPTemplateApplicationDashboardScene _updateSceneTraitsAndPushTraitsToScreen:]
- -[CPTemplateApplicationInstrumentClusterScene _updateSceneTraitsAndPushTraitsToScreen:]
- -[CPTemplateApplicationScene _updateSceneTraitsAndPushTraitsToScreen:]
- GCC_except_table130
- GCC_except_table25
- GCC_except_table58
- GCC_except_table75
- _OBJC_IVAR_$_CPRouteDetail._labelTintColor
- ___54-[CPInterfaceController _completeSetupWithCompletion:]_block_invoke
- ___54-[CPInterfaceController templateIdentifierDidDismiss:]_block_invoke_2
- ___block_descriptor_48_e8_32s40bs_e18_v24?0Q8"NSSet"16ls32l8s40l8
- _objc_msgSend$_completeSetupWithCompletion:
- _objc_msgSend$hideOverlayTemplateAnimated:completion:
- _objc_msgSend$labelTintColor
- _objc_msgSend$setLabelTintColor:
CStrings:
+ "A navigation alert is currently showing. Call dismissNavigationAlertAnimated:completion: first."
+ "CPMapTemplate did not push because remote does not support"
+ "Finished setting up template version and supported selectors."
+ "Info"
+ "No panel matching id %@ found, must be an options panel"
+ "Parking"
+ "kCPNavigationAlertShowsCloseButtonKey"
- ", labelTintColor=%@"
- "No panel matching id %@ found"
- "labelTintColor"
```
