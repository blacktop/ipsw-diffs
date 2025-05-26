## HearingUI

> `/System/Library/PrivateFrameworks/HearingUI.framework/HearingUI`

```diff

-403.0.0.0.0
-  __TEXT.__text: 0x31228
-  __TEXT.__auth_stubs: 0x1080
-  __TEXT.__objc_methlist: 0x249c
+406.1.3.0.0
+  __TEXT.__text: 0x31ac8
+  __TEXT.__auth_stubs: 0x1070
+  __TEXT.__objc_methlist: 0x252c
   __TEXT.__const: 0x9d4
-  __TEXT.__cstring: 0x1df8
-  __TEXT.__gcc_except_tab: 0x828
+  __TEXT.__cstring: 0x1ed8
+  __TEXT.__gcc_except_tab: 0x840
   __TEXT.__oslogstring: 0x3a4
   __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__swift5_typeref: 0x19fe

   __TEXT.__swift5_capture: 0x40
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x28
-  __TEXT.__unwind_info: 0xbf4
-  __TEXT.__objc_classname: 0x413
-  __TEXT.__objc_methname: 0x756b
+  __TEXT.__unwind_info: 0xc18
+  __TEXT.__objc_classname: 0x415
+  __TEXT.__objc_methname: 0x773b
   __TEXT.__objc_methtype: 0xc2e
-  __TEXT.__objc_stubs: 0x62a0
+  __TEXT.__objc_stubs: 0x6460
   __DATA_CONST.__got: 0x378
-  __DATA_CONST.__const: 0xd68
+  __DATA_CONST.__const: 0xd90
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x75e8
-  __DATA_CONST.__objc_selrefs: 0x1d60
+  __DATA_CONST.__objc_const: 0x7848
+  __DATA_CONST.__objc_selrefs: 0x1dd0
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__objc_const: 0xa60
-  __AUTH_CONST.__cfstring: 0x1b00
+  __AUTH_CONST.__cfstring: 0x1b40
   __AUTH_CONST.__const: 0x7b0
   __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__auth_got: 0x850
+  __AUTH_CONST.__auth_got: 0x848
   __AUTH.__objc_data: 0xc78
   __AUTH.__data: 0x348
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x2e0
+  __DATA.__objc_classrefs: 0x2e8
   __DATA.__objc_superrefs: 0xf8
-  __DATA.__objc_ivar: 0x348
+  __DATA.__objc_ivar: 0x350
   __DATA.__data: 0x6b8
   __DATA.__bss: 0x470
   __DATA.__common: 0x98

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1179
-  Symbols:   3903
-  CStrings:  1816
+  Functions: 1192
+  Symbols:   3948
+  CStrings:  1840
 
Symbols:
+ -[HACCContentViewController viewDidDisappear:]
+ -[HACCContentViewController viewWillAppear:]
+ -[HACCLiveListenButton _updateAXValueString]
+ -[HACCLiveListenButton accessibilityValueString]
+ -[HACCLiveListenButton accessibilityValue]
+ -[HACCLiveListenButton setAccessibilityValueString:]
+ -[HACCLiveListenButton subscribeListeners]
+ -[HACCLiveListenButton unsubscribeListeners]
+ -[HUICCMenuCheckmarkView subscribeListeners]
+ -[HUICCMenuCheckmarkView unsubscribeListeners]
+ -[HUISliderConfig minImageAction]
+ -[HUISliderConfig setMinImageAction:]
+ GCC_except_table13
+ GCC_except_table2
+ GCC_except_table20
+ GCC_except_table3
+ GCC_except_table36
+ _OBJC_CLASS_$_UIButton
+ _OBJC_IVAR_$_HACCLiveListenButton._accessibilityValueString
+ _OBJC_IVAR_$_HUISliderConfig._minImageAction
+ ___27-[HACCSlider _sliderConfig]_block_invoke
+ ___42-[HACCLiveListenButton subscribeListeners]_block_invoke
+ ___42-[HACCLiveListenButton subscribeListeners]_block_invoke_2
+ ___42-[HACCLiveListenButton subscribeListeners]_block_invoke_3
+ ___42-[HACCLiveListenButton subscribeListeners]_block_invoke_4
+ ___44-[HUICCMenuCheckmarkView subscribeListeners]_block_invoke
+ ___44-[HUICCMenuCheckmarkView subscribeListeners]_block_invoke_2
+ ___block_descriptor_40_e8_32w_e18_v16?0"UIAction"8lw32l8
+ ___block_literal_global.260
+ _objc_msgSend$_updateAXValueString
+ _objc_msgSend$accessibilityValueString
+ _objc_msgSend$actionWithHandler:
+ _objc_msgSend$addAction:forControlEvents:
+ _objc_msgSend$buttonWithType:
+ _objc_msgSend$minImageAction
+ _objc_msgSend$setAccessibilityValueString:
+ _objc_msgSend$setContentHorizontalAlignment:
+ _objc_msgSend$setImage:forState:
+ _objc_msgSend$setMinImageAction:
+ _objc_msgSend$subscribeListeners
+ _objc_msgSend$unregisterComfortSoundsModelUpdatesHandler:
+ _objc_msgSend$unregisterLiveListenLevelListener:
+ _objc_msgSend$unregisterLiveListenListener:
+ _objc_msgSend$unsubscribeListeners
- GCC_except_table32
- GCC_except_table8
- ___38-[HACCLiveListenButton initWithFrame:]_block_invoke
- ___38-[HACCLiveListenButton initWithFrame:]_block_invoke.259
- ___38-[HACCLiveListenButton initWithFrame:]_block_invoke_2
- ___38-[HACCLiveListenButton initWithFrame:]_block_invoke_2.260
- ___50-[HUICCMenuCheckmarkView initWithFrame:andModule:]_block_invoke_2
- ___50-[HUICCMenuCheckmarkView initWithFrame:andModule:]_block_invoke_3
- ___block_literal_global.265
- _objc_msgSend$addTarget:action:forEvents:
- _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "\x13\x13"
+ "%"
+ "-[HACCLiveListenButton subscribeListeners]"
+ "-[HACCLiveListenButton unsubscribeListeners]"
+ "-[HUICCMenuCheckmarkView subscribeListeners]"
+ "-[HUICCMenuCheckmarkView unsubscribeListeners]"
+ "Registering Comfort Sounds listener"
+ "T@\"NSString\",&,N,V_accessibilityValueString"
+ "T@\"UIAction\",&,N,V_minImageAction"
+ "Unregistering Comfort Sounds listener"
+ "Unregistering Live Listen listener"
+ "_accessibilityValueString"
+ "_minImageAction"
+ "_updateAXValueString"
+ "accessibilityValueString"
+ "actionWithHandler:"
+ "addAction:forControlEvents:"
+ "buttonWithType:"
+ "minImageAction"
+ "setAccessibilityValueString:"
+ "setContentHorizontalAlignment:"
+ "setImage:forState:"
+ "setMinImageAction:"
+ "subscribeListeners"
+ "unregisterComfortSoundsModelUpdatesHandler:"
+ "unregisterLiveListenLevelListener:"
+ "unregisterLiveListenListener:"
+ "unsubscribeListeners"
- "\x12\x13"
- "-[HACCLiveListenButton initWithFrame:]"
- "addTarget:action:forEvents:"
- "airpodsIcon"

```
