## AVFoundation

> `/System/Library/AccessibilityBundles/AVFoundation.axbundle/AVFoundation`

```diff

-3005.4.9.0.0
-  __TEXT.__text: 0x182c
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_methlist: 0x114
-  __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x178
-  __TEXT.__oslogstring: 0x21f
-  __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__unwind_info: 0x108
-  __TEXT.__objc_classname: 0x7c
-  __TEXT.__objc_methname: 0x606
-  __TEXT.__objc_methtype: 0xb9
-  __TEXT.__objc_stubs: 0x560
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x170
-  __DATA_CONST.__objc_classlist: 0x20
+3005.4.13.0.0
+  __TEXT.__text: 0xf3c
+  __TEXT.__auth_stubs: 0x2c0
+  __TEXT.__objc_methlist: 0x124
+  __TEXT.__cstring: 0x192
+  __TEXT.__const: 0x18
+  __TEXT.__oslogstring: 0x95
+  __TEXT.__unwind_info: 0xd8
+  __TEXT.__objc_classname: 0xb8
+  __TEXT.__objc_methname: 0x4a1
+  __TEXT.__objc_methtype: 0xb2
+  __TEXT.__objc_stubs: 0x3e0
+  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b0
-  __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1a8
+  __DATA_CONST.__objc_selrefs: 0x148
+  __DATA_CONST.__objc_superrefs: 0x18
+  __AUTH_CONST.__auth_got: 0x168
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x180
-  __AUTH_CONST.__objc_const: 0x2d0
+  __AUTH_CONST.__cfstring: 0x1a0
+  __AUTH_CONST.__objc_const: 0x3f0
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x8
   __DATA.__bss: 0x8

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8420C883-2372-3A9E-A4CA-71DF847837D3
-  Functions: 40
-  Symbols:   245
-  CStrings:  116
+  UUID: D14A4176-FEEF-37DF-B70E-9F3FB8169CE4
+  Functions: 32
+  Symbols:   210
+  CStrings:  102
 
Symbols:
+ +[AVPlayerItemAccessibility _accessibilityPerformValidations:]
+ +[AVPlayerItemAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[AVPlayerItemAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[AVPlayerItemAccessibility _attachToPlayer:]
+ -[AXAVFoundationMediaDescriptionManager registerLegibilityTappingOnPlayer:playerItem:]
+ _OBJC_CLASS_$_AVPlayerItemAccessibility
+ _OBJC_CLASS_$___AVPlayerItemAccessibility_super
+ _OBJC_METACLASS_$_AVPlayerItemAccessibility
+ _OBJC_METACLASS_$___AVPlayerItemAccessibility_super
+ __OBJC_$_CLASS_METHODS_AVPlayerItemAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_AVPlayerItemAccessibility
+ __OBJC_CLASS_RO_$_AVPlayerItemAccessibility
+ __OBJC_CLASS_RO_$___AVPlayerItemAccessibility_super
+ __OBJC_METACLASS_RO_$_AVPlayerItemAccessibility
+ __OBJC_METACLASS_RO_$___AVPlayerItemAccessibility_super
+ ___86-[AXAVFoundationMediaDescriptionManager registerLegibilityTappingOnPlayer:playerItem:]_block_invoke
+ ___86-[AXAVFoundationMediaDescriptionManager registerLegibilityTappingOnPlayer:playerItem:]_block_invoke.305
+ ___86-[AXAVFoundationMediaDescriptionManager registerLegibilityTappingOnPlayer:playerItem:]_block_invoke.306
+ ___86-[AXAVFoundationMediaDescriptionManager registerLegibilityTappingOnPlayer:playerItem:]_block_invoke_2
+ ___86-[AXAVFoundationMediaDescriptionManager registerLegibilityTappingOnPlayer:playerItem:]_block_invoke_3
+ ___86-[AXAVFoundationMediaDescriptionManager registerLegibilityTappingOnPlayer:playerItem:]_block_invoke_3.cold.1
+ ___86-[AXAVFoundationMediaDescriptionManager registerLegibilityTappingOnPlayer:playerItem:]_block_invoke_3.cold.2
+ _objc_msgSend$registerLegibilityTappingOnPlayer:playerItem:
+ _objc_release_x25
- -[AVPlayerAccessibility _accessibilityAsyncObserveAVPlayerIfNeeded]
- -[AVPlayerAccessibility init]
- -[AVPlayerAccessibility willChangeValueForKey:]
- -[AXAVFoundationMediaDescriptionManager beginObservingPlayer:]
- -[AXAVFoundationMediaDescriptionManager endObservingPlayer:]
- -[AXAVFoundationMediaDescriptionManager observeValueForKeyPath:ofObject:change:context:]
- GCC_except_table18
- GCC_except_table9
- _AXRuntimeLogCommon
- _NSKeyValueChangeNewKey
- _NSKeyValueChangeNotificationIsPriorKey
- _NSKeyValueChangeOldKey
- _OBJC_CLASS_$_AVPlayerItem
- __Unwind_Resume
- ___60-[AXAVFoundationMediaDescriptionManager endObservingPlayer:]_block_invoke
- ___60-[AXAVFoundationMediaDescriptionManager endObservingPlayer:]_block_invoke_2
- ___60-[AXAVFoundationMediaDescriptionManager endObservingPlayer:]_block_invoke_3
- ___62-[AXAVFoundationMediaDescriptionManager beginObservingPlayer:]_block_invoke
- ___62-[AXAVFoundationMediaDescriptionManager beginObservingPlayer:]_block_invoke.305
- ___62-[AXAVFoundationMediaDescriptionManager beginObservingPlayer:]_block_invoke_2
- ___62-[AXAVFoundationMediaDescriptionManager beginObservingPlayer:]_block_invoke_3
- ___62-[AXAVFoundationMediaDescriptionManager beginObservingPlayer:]_block_invoke_3.cold.1
- ___62-[AXAVFoundationMediaDescriptionManager beginObservingPlayer:]_block_invoke_3.cold.2
- ___67-[AVPlayerAccessibility _accessibilityAsyncObserveAVPlayerIfNeeded]_block_invoke
- ___88-[AXAVFoundationMediaDescriptionManager observeValueForKeyPath:ofObject:change:context:]_block_invoke
- ___88-[AXAVFoundationMediaDescriptionManager observeValueForKeyPath:ofObject:change:context:]_block_invoke.310
- ___Block_byref_object_copy_
- ___Block_byref_object_dispose_
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
- ___objc_personality_v0
- __dispatch_main_q
- _dispatch_async
- _objc_msgSend$_accessibilityAsyncObserveAVPlayerIfNeeded
- _objc_msgSend$_accessibilityBoolValueForKey:
- _objc_msgSend$_accessibilitySetBoolValue:forKey:
- _objc_msgSend$_queue_itemNodeForPlayer:
- _objc_msgSend$addObserver:forKeyPath:options:context:
- _objc_msgSend$beginObservingPlayer:
- _objc_msgSend$boolValue
- _objc_msgSend$endAutoTriggerOfLegibilityEvents
- _objc_msgSend$isEqualToString:
- _objc_msgSend$objectForKeyedSubscript:
- _objc_msgSend$removeObjectForKey:
- _objc_msgSend$removeObserver:forKeyPath:context:
- _objc_msgSend$removeSourceNode:
- _objc_opt_isKindOfClass
- _objc_release_x24
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
- _objc_retain_x23
CStrings:
+ "@"
+ "AVPlayerItem"
+ "AVPlayerItemAccessibility"
+ "B32@0:8@16@24"
+ "__AVPlayerItemAccessibility_super"
+ "_attachToPlayer:"
+ "registerLegibilityTappingOnPlayer:playerItem:"
- "AX will begin observing player=%p because UIAccessibilityIsVoiceOverRunning=%ld or isVoiceOverInTheTripleClickMenu=%ld"
- "AX will not begin observing player=%p because UIAccessibilityIsVoiceOverRunning=0 and isVoiceOverInTheTripleClickMenu=0"
- "AXBeganObservingKey"
- "Did observe change on. path:'%@' object:%@ change:%@"
- "No legibility node found for player: %@"
- "Will begin observing player: %@"
- "Will end observing player: %@"
- "_accessibilityAsyncObserveAVPlayerIfNeeded"
- "_accessibilityBoolValueForKey:"
- "_accessibilitySetBoolValue:forKey:"
- "addObserver:forKeyPath:options:context:"
- "beginObservingPlayer:"
- "boolValue"
- "currentItem"
- "endAutoTriggerOfLegibilityEvents"
- "endObservingPlayer:"
- "isEqualToString:"
- "objectForKeyedSubscript:"
- "observeValueForKeyPath:ofObject:change:context:"
- "removeObjectForKey:"
- "removeObserver:forKeyPath:context:"
- "removeSourceNode:"
- "v48@0:8@16@24@32^v40"
- "willChangeValueForKey:"

```
