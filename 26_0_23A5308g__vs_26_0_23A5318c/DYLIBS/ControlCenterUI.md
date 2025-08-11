## ControlCenterUI

> `/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI`

```diff

-655.100.0.0.0
-  __TEXT.__text: 0xa25bc
+655.0.1.100.0
+  __TEXT.__text: 0xa27dc
   __TEXT.__auth_stubs: 0x2510
-  __TEXT.__objc_methlist: 0xa068
+  __TEXT.__objc_methlist: 0xa0c8
   __TEXT.__const: 0x233a
   __TEXT.__cstring: 0x7ab4
-  __TEXT.__gcc_except_tab: 0x828
-  __TEXT.__oslogstring: 0x3221
+  __TEXT.__gcc_except_tab: 0x85c
+  __TEXT.__oslogstring: 0x3291
   __TEXT.__dlopen_cstrs: 0x14e
   __TEXT.__constg_swiftt: 0x24fc
   __TEXT.__swift5_typeref: 0x25ec

   __TEXT.__unwind_info: 0x2820
   __TEXT.__eh_frame: 0x448
   __TEXT.__objc_classname: 0x15e0
-  __TEXT.__objc_methname: 0x1b896
-  __TEXT.__objc_methtype: 0x7b63
-  __TEXT.__objc_stubs: 0xbc40
+  __TEXT.__objc_methname: 0x1ba48
+  __TEXT.__objc_methtype: 0x7b66
+  __TEXT.__objc_stubs: 0xbc60
   __DATA_CONST.__got: 0xc20
   __DATA_CONST.__const: 0x1130
   __DATA_CONST.__objc_classlist: 0x380
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x560
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5ea8
+  __DATA_CONST.__objc_selrefs: 0x5ee0
   __DATA_CONST.__objc_protorefs: 0x200
   __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x68
   __AUTH_CONST.__auth_got: 0x1298
   __AUTH_CONST.__const: 0x3a18
   __AUTH_CONST.__cfstring: 0x2800
-  __AUTH_CONST.__objc_const: 0xf5a0
+  __AUTH_CONST.__objc_const: 0xf660
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH.__objc_data: 0x17a0
   __AUTH.__data: 0x768
-  __DATA.__objc_ivar: 0x678
+  __DATA.__objc_ivar: 0x688
   __DATA.__data: 0x3678
   __DATA.__bss: 0x1210
   __DATA.__common: 0x20

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6CF3DC8C-2CA0-33FD-8212-848F3EC9A002
-  Functions: 4422
-  Symbols:   9401
-  CStrings:  6299
+  UUID: 64506C4B-55CA-3F78-BC5A-1F1DBB172F46
+  Functions: 4430
+  Symbols:   9422
+  CStrings:  6313
 
Symbols:
+ -[CCUIHeaderPocketView cachedAdditionalHeight]
+ -[CCUIHeaderPocketView cachedIsDisplayingSensorStatus]
+ -[CCUIHeaderPocketView cachedVerticalSecondaryServiceDelta]
+ -[CCUIHeaderPocketView presentationState]
+ -[CCUIHeaderPocketView setCachedAdditionalHeight:]
+ -[CCUIHeaderPocketView setCachedIsDisplayingSensorStatus:]
+ -[CCUIHeaderPocketView setCachedVerticalSecondaryServiceDelta:]
+ -[CCUIHeaderPocketView setPresentationState:]
+ -[CCUIWiFiModuleViewController _glyphImageForState:currentSignalBars:forceSignalBars:network:applyConfiguration:]
+ _OBJC_IVAR_$_CCUIHeaderPocketView._cachedAdditionalHeight
+ _OBJC_IVAR_$_CCUIHeaderPocketView._cachedIsDisplayingSensorStatus
+ _OBJC_IVAR_$_CCUIHeaderPocketView._cachedVerticalSecondaryServiceDelta
+ _OBJC_IVAR_$_CCUIHeaderPocketView._presentationState
+ ___115-[CCUIMainViewController _getCameraSensorActivityData:micSensorActivityData:isMutedMic:isInactiveMicModeSelection:]_block_invoke.129
+ ___115-[CCUIMainViewController _getCameraSensorActivityData:micSensorActivityData:isMutedMic:isInactiveMicModeSelection:]_block_invoke_2.133
+ ___block_literal_global.128
+ ___block_literal_global.139
+ _objc_msgSend$_glyphImageForState:currentSignalBars:forceSignalBars:network:applyConfiguration:
+ _objc_msgSend$stringFromSensorType:
- -[CCUIWiFiModuleViewController _glyphImageForState:currentSignalBars:network:applyConfiguration:]
- ___115-[CCUIMainViewController _getCameraSensorActivityData:micSensorActivityData:isMutedMic:isInactiveMicModeSelection:]_block_invoke.128
- ___115-[CCUIMainViewController _getCameraSensorActivityData:micSensorActivityData:isMutedMic:isInactiveMicModeSelection:]_block_invoke_2.132
- ___block_literal_global.127
- ___block_literal_global.138
- _objc_msgSend$_glyphImageForState:currentSignalBars:network:applyConfiguration:
CStrings:
+ "@48@0:8q16@24B32@36B44"
+ "TB,N,V_cachedIsDisplayingSensorStatus"
+ "Td,N,V_cachedAdditionalHeight"
+ "Td,N,V_cachedVerticalSecondaryServiceDelta"
+ "[AV Modules] Context module context returning sensor activity data for sensor type: %{public}@, data: <%{public}@>"
+ "_cachedAdditionalHeight"
+ "_cachedIsDisplayingSensorStatus"
+ "_cachedVerticalSecondaryServiceDelta"
+ "_glyphImageForState:currentSignalBars:forceSignalBars:network:applyConfiguration:"
+ "cachedAdditionalHeight"
+ "cachedIsDisplayingSensorStatus"
+ "cachedVerticalSecondaryServiceDelta"
+ "setCachedAdditionalHeight:"
+ "setCachedIsDisplayingSensorStatus:"
+ "setCachedVerticalSecondaryServiceDelta:"
+ "stringFromSensorType:"
+ "\x91\xa21"
- "@44@0:8q16@24@32B40"
- "_glyphImageForState:currentSignalBars:network:applyConfiguration:"
- "\x81\xa2!"

```
