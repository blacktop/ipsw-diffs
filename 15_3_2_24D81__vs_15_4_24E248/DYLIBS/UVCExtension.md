## UVCExtension

> `/System/Library/PrivateFrameworks/UVCExtension.framework/Versions/A/UVCExtension`

```diff

 466.80.2.0.0
-  __TEXT.__text: 0x29ccc
+  __TEXT.__text: 0x291e8
   __TEXT.__auth_stubs: 0x800
-  __TEXT.__objc_methlist: 0xd84
+  __TEXT.__objc_methlist: 0xf64
   __TEXT.__const: 0x100
-  __TEXT.__gcc_except_tab: 0xca4
+  __TEXT.__gcc_except_tab: 0xcb4
   __TEXT.__cstring: 0x18d0
   __TEXT.__oslogstring: 0x2aa3
-  __TEXT.__unwind_info: 0x7c8
+  __TEXT.__unwind_info: 0x7c0
   __TEXT.__objc_classname: 0x23b
   __TEXT.__objc_methname: 0x31a4
   __TEXT.__objc_methtype: 0x7df

   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc58
+  __DATA_CONST.__objc_selrefs: 0xce0
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x70
   __AUTH_CONST.__auth_got: 0x410
   __AUTH_CONST.__const: 0xeb0
   __AUTH_CONST.__cfstring: 0x1900
-  __AUTH_CONST.__objc_const: 0x2980
+  __AUTH_CONST.__objc_const: 0x2610
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8082DF38-9B14-3E74-9D31-54C738B478D1
-  Functions: 560
-  Symbols:   1670
+  UUID: E0E56F3C-5626-34B9-B2BF-B74070C68826
+  Functions: 641
+  Symbols:   1745
   CStrings:  1439
 
Symbols:
+ +[UVCExtensionSystemPreferredDeviceManager sharedInstance].cold.1
+ -[UVCExtensionAppleDisplayDevice resetManualFraming].cold.1
+ -[UVCExtensionAppleDisplayDevice setCenterStageFramingStyle:].cold.1
+ -[UVCExtensionAppleDisplayDevice setPanningTranslation:].cold.1
+ -[UVCExtensionAppleDisplayDevice setStartPanningAtPoint:].cold.1
+ -[UVCExtensionProvider activate].cold.1
+ -[UVCExtensionProvider waitForSessionActivation].cold.1
+ -[UVCExtensionStream commitStream:error:].cold.1
+ -[UVCExtensionStream commitStream:error:].cold.2
+ GCC_except_table82
+ UVCExtensionLog.cold.1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_50
+ _OUTLINED_FUNCTION_51
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __MergedGlobals
- -[UVCExtensionAppleDisplayDevice setCFForDefaultStreamInterface:error:].cold.1
- -[UVCExtensionAppleDisplayDevice setRollProperty:error:].cold.1
- -[UVCExtensionAppleDisplayDevice setRollProperty:error:].cold.2
- -[UVCExtensionAppleDisplayDevice setRollProperty:error:].cold.3
- -[UVCExtensionAppleDisplayDevice setRollProperty:error:].cold.4
- -[UVCExtensionAppleDisplayStream sendSampleBuffer:discontinuity:hostTimeInNanoseconds:].cold.1
- -[UVCExtensionAppleStream handleProcessingError:].cold.1
- -[UVCExtensionAppleStream handleProcessingError:].cold.2
- -[UVCExtensionAppleStream handleProcessingError:].cold.3
- -[UVCExtensionDevice getCMIOPropertySelector:].cold.1
- -[UVCExtensionDevice getPropertyStateForControl:].cold.1
- -[UVCExtensionDevice getPropertyStateForControlValue:].cold.1
- -[UVCExtensionDevice initWithInterface:provider:].cold.1
- -[UVCExtensionDevice postDeviceTermination:].cold.1
- -[UVCExtensionDevice setPropertyStateForControl:value:error:].cold.1
- -[UVCExtensionDevice setPropertyStateForControlValue:value:error:].cold.1
- -[UVCExtensionDevice setupExtensionDeviceSync:].cold.1
- -[UVCExtensionDevice setupProperties].cold.1
- -[UVCExtensionDevice setupProperties].cold.2
- -[UVCExtensionDevice setupProperties].cold.3
- -[UVCExtensionDevice setupStreams].cold.1
- -[UVCExtensionDevice setupStreams].cold.2
- -[UVCExtensionProvider initWithBundleID:queue:].cold.1
- -[UVCExtensionProvider setupMatching].cold.1
- -[UVCExtensionProvider setupPowerStateListener].cold.1
- -[UVCExtensionProvider setupServerPort].cold.1
- -[UVCExtensionStream initWithDevice:uvcFormats:source:attributes:].cold.1
- -[UVCExtensionStream initWithDevice:uvcFormats:source:attributes:].cold.2
- -[UVCExtensionStream initWithDevice:uvcFormats:source:attributes:].cold.3
- -[UVCExtensionStream setActiveFormatIndex:].cold.1
- -[UVCExtensionStream setActiveFrameDuration:].cold.1
- -[UVCExtensionStream setActiveMaxFrameDuration:].cold.1
- GetLocBundle.bundle
- GetLocBundle.once

```
