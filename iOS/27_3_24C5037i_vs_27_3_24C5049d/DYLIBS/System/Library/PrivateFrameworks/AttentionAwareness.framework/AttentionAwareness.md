## AttentionAwareness

> `/System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness`

```diff

-265.60.1.0.2
-  __TEXT.__text: 0x3cca0
-  __TEXT.__objc_methlist: 0x2a2c
+265.60.4.0.3
+  __TEXT.__text: 0x3db94
+  __TEXT.__objc_methlist: 0x2a8c
   __TEXT.__const: 0x5f4
-  __TEXT.__cstring: 0x452c
+  __TEXT.__cstring: 0x463d
   __TEXT.__swift5_typeref: 0x13c
   __TEXT.__swift5_capture: 0xf0
   __TEXT.__swift5_reflstr: 0x8a

   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__gcc_except_tab: 0x8dc
-  __TEXT.__oslogstring: 0x5d3f
-  __TEXT.__unwind_info: 0x11b8
+  __TEXT.__gcc_except_tab: 0x8c4
+  __TEXT.__oslogstring: 0x5fd0
+  __TEXT.__unwind_info: 0x11e0
   __TEXT.__eh_frame: 0x2f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1540
+  __DATA_CONST.__objc_selrefs: 0x1580
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x40
-  __DATA_CONST.__got: 0x2c0
-  __AUTH_CONST.__const: 0x6f0
-  __AUTH_CONST.__cfstring: 0x1ee0
-  __AUTH_CONST.__objc_const: 0x5758
+  __DATA_CONST.__got: 0x2c8
+  __AUTH_CONST.__const: 0x730
+  __AUTH_CONST.__cfstring: 0x1f40
+  __AUTH_CONST.__objc_const: 0x57c8
   __AUTH_CONST.__weak_auth_got: 0x8
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x758
+  __AUTH_CONST.__auth_got: 0x750
   __AUTH.__objc_data: 0x130
-  __DATA.__objc_ivar: 0x580
-  __DATA.__data: 0xb70
+  __DATA.__objc_ivar: 0x58c
+  __DATA.__data: 0xb78
   __DATA_DIRTY.__objc_data: 0xd28
   __DATA_DIRTY.__data: 0x68
-  __DATA_DIRTY.__bss: 0x160
+  __DATA_DIRTY.__bss: 0x140
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1164
-  Symbols:   2310
-  CStrings:  905
+  Functions: 1176
+  Symbols:   2330
+  CStrings:  924
 
Symbols:
+ -[AWAVFoundationAttentionStreamer setInnerDisplayActive:]
+ -[AWAttentionAwareService innerDisplayStateChanging:]
+ -[AWAttentionSampler setInnerDisplayActive:]
+ -[AWAttentionStreamer setInnerDisplayStateWithMask:innerDisplayActive:]
+ -[AWPearlAttentionSampler setInnerDisplayActive:]
+ -[AWScheduler innerDisplayStateChanging:]
+ -[ScreenStateObserver backlight:activatingWithEvent:]
+ -[ScreenStateObserver backlight:deactivatingWithEvent:]
+ -[ScreenStateObserver dealloc]
+ -[ScreenStateObserver observeValueForKeyPath:ofObject:change:context:]
+ -[ScreenStateObserver startObservingPrimaryDisplayRegion]
+ -[ScreenStateObserver updateDisplayState:]
+ GCC_except_table121
+ GCC_except_table167
+ GCC_except_table168
+ GCC_except_table172
+ GCC_except_table359
+ GCC_except_table371
+ GCC_except_table390
+ GCC_except_table453
+ GCC_except_table47
+ GCC_except_table49
+ GCC_except_table51
+ GCC_except_table522
+ GCC_except_table526
+ GCC_except_table53
+ GCC_except_table540
+ GCC_except_table546
+ GCC_except_table55
+ GCC_except_table551
+ GCC_except_table555
+ GCC_except_table559
+ GCC_except_table564
+ GCC_except_table568
+ GCC_except_table57
+ GCC_except_table572
+ GCC_except_table639
+ GCC_except_table663
+ GCC_except_table736
+ GCC_except_table85
+ GCC_except_table890
+ GCC_except_table896
+ GCC_except_table926
+ GCC_except_table933
+ GCC_except_table935
+ GCC_except_table937
+ GCC_except_table938
+ GCC_except_table948
+ GCC_except_table950
+ GCC_except_table961
+ GCC_except_table963
+ _NSKeyValueChangeNewKey
+ _OBJC_IVAR_$_AVFoundationOperation._frames
+ _OBJC_IVAR_$_AWAVFoundationAttentionStreamer._innerDisplayActive
+ _OBJC_IVAR_$_AWPearlAttentionSampler._innerDisplayActive
+ _OBJC_IVAR_$_ScreenStateObserver._avdevice
+ _OBJC_IVAR_$_ScreenStateObserver._innerDisplayActive
+ _PrimaryDisplayRegionContext
+ ___42-[ScreenStateObserver updateDisplayState:]_block_invoke
+ ___53-[AWAttentionAwareService innerDisplayStateChanging:]_block_invoke
+ ___54-[ScreenStateObserver initWithCallbackQueue:observer:]_block_invoke_2
+ ___70-[ScreenStateObserver observeValueForKeyPath:ofObject:change:context:]_block_invoke
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___doesPlatformSupportAutoDimRGBFaceDetect_block_invoke
+ ___isAccessibilityAttentionToggleEnabled_block_invoke
+ ___isAccessibilityAttentionToggleEnabled_block_invoke_2
+ ___isRGBFaceDetectEnabledViaOverride_block_invoke
+ _doesPlatformSupportAutoDimRGBFaceDetect.onceToken
+ _doesPlatformSupportAutoDimRGBFaceDetect.supported
+ _getAVFoundationDevice
+ _isAccessibilityAttentionToggleEnabled
+ _isAccessibilityAttentionToggleEnabled.accessibilityValue
+ _isAccessibilityAttentionToggleEnabled.onceToken
+ _isAccessibilityAttentionToggleEnabled.queue
+ _isRGBFaceDetectEnabledViaOverride.enabled
+ _isRGBFaceDetectEnabledViaOverride.onceToken
- -[AWAVFoundationAttentionStreamer isAttentionAwareFeaturesEnabled]
- -[AWAVFoundationAttentionStreamer setIsAttentionAwareFeaturesEnabled:]
- -[AWPearlAttentionStreamer isAttentionAwareFeaturesEnabled]
- -[AWPearlAttentionStreamer setIsAttentionAwareFeaturesEnabled:]
- -[ScreenStateObserver backlight:performingEvent:]
- GCC_except_table122
- GCC_except_table123
- GCC_except_table169
- GCC_except_table170
- GCC_except_table174
- GCC_except_table351
- GCC_except_table363
- GCC_except_table382
- GCC_except_table446
- GCC_except_table447
- GCC_except_table46
- GCC_except_table48
- GCC_except_table50
- GCC_except_table515
- GCC_except_table519
- GCC_except_table52
- GCC_except_table533
- GCC_except_table539
- GCC_except_table54
- GCC_except_table544
- GCC_except_table548
- GCC_except_table552
- GCC_except_table557
- GCC_except_table56
- GCC_except_table561
- GCC_except_table565
- GCC_except_table632
- GCC_except_table656
- GCC_except_table728
- GCC_except_table84
- GCC_except_table882
- GCC_except_table888
- GCC_except_table914
- GCC_except_table918
- GCC_except_table925
- GCC_except_table927
- GCC_except_table929
- GCC_except_table940
- GCC_except_table942
- GCC_except_table947
- GCC_except_table953
- _BLSBacklightStateIsActive
- _OBJC_IVAR_$_AWAVFoundationAttentionStreamer._isAttentionAwareFeaturesEnabled
- _OBJC_IVAR_$_AWPearlAttentionStreamer._isAttentionAwareFeaturesEnabled
- ___49-[ScreenStateObserver backlight:performingEvent:]_block_invoke
- ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
- ___isPearlDisabledViaAccessibility_block_invoke
- ___isPearlDisabledViaAccessibility_block_invoke_2
- _isPearlDisabledViaAccessibility.accessibilityValue
- _isPearlDisabledViaAccessibility.onceToken
- _isPearlDisabledViaAccessibility.queue
CStrings:
+ " Inner display active"
+ "%13.5f: %@ does not report a primary display region"
+ "%13.5f: %@ ignoring sample with deadline %13.5f for client %@ since the inner display is active"
+ "%13.5f: Inner display %s primary"
+ "%13.5f: Inner display active, not starting attention stream"
+ "%13.5f: Inner display state changed to %s"
+ "%13.5f: Primary display region: %ld"
+ "%13.5f: User has Attention Aware features off, cannot start streaming operation with AVFoundation"
+ "%30s:%-4d: %13.5f: %@ does not report a primary display region"
+ "%30s:%-4d: %13.5f: %@ ignoring sample with deadline %13.5f for client %@ since the inner display is active"
+ "%30s:%-4d: %13.5f: Inner display %s primary"
+ "%30s:%-4d: %13.5f: Inner display state changed to %s"
+ "%30s:%-4d: %13.5f: Primary display region: %ld"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AttentionAwareness/Framework/XPCService/Device States/ScreenStateObserver.m"
+ "Active"
+ "Inactive"
+ "active"
+ "com.apple.AttentionAwareness.attentionAccessibilitySettingsChanged"
+ "inactive"
+ "inner display %s"
+ "primaryDisplayRegion"
- "%30s:%-4d: %13.5f: Pearl disabled via accessibility; disabling FaceDetect"
- "com.apple.AttentionAwareness.pearlAccessibilitySettingsChanged"
```
