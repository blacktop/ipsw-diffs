## AVFoundation

> `/System/Library/AccessibilityBundles/AVFoundation.axbundle/AVFoundation`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0xfb4
-  __TEXT.__auth_stubs: 0x2a0
+3036.2.0.0.0
+  __TEXT.__text: 0xe5c
   __TEXT.__objc_methlist: 0x124
-  __TEXT.__cstring: 0x192
   __TEXT.__const: 0x18
+  __TEXT.__cstring: 0x194
   __TEXT.__oslogstring: 0x95
-  __TEXT.__unwind_info: 0xd8
-  __TEXT.__objc_classname: 0xb8
-  __TEXT.__objc_methname: 0x4a1
-  __TEXT.__objc_methtype: 0xb2
-  __TEXT.__objc_stubs: 0x3e0
-  __DATA_CONST.__got: 0x68
+  __TEXT.__unwind_info: 0xc8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x148
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x158
+  __DATA_CONST.__got: 0x68
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x1a0
   __AUTH_CONST.__objc_const: 0x3f0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x8

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 71A2D8FB-9B36-3674-A640-9A5115640AF6
-  Functions: 33
-  Symbols:   210
-  CStrings:  102
+  UUID: F78D0CBB-77ED-3FAD-A531-8ED4421C688C
+  Functions: 29
+  Symbols:   205
+  CStrings:  38
 
Symbols:
+ ___86-[AXAVFoundationMediaDescriptionManager registerLegibilityTappingOnPlayer:playerItem:]_block_invoke.365
+ ___86-[AXAVFoundationMediaDescriptionManager registerLegibilityTappingOnPlayer:playerItem:]_block_invoke.366
+ ___block_literal_global.351
+ ___block_literal_global.360
+ ___block_literal_global.363
+ ___block_literal_global.54
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x23
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x8
- +[AXAVFoundationMediaDescriptionManager sharedManager].cold.1
- _OUTLINED_FUNCTION_0
- ___86-[AXAVFoundationMediaDescriptionManager registerLegibilityTappingOnPlayer:playerItem:]_block_invoke.344
- ___86-[AXAVFoundationMediaDescriptionManager registerLegibilityTappingOnPlayer:playerItem:]_block_invoke.345
- ___86-[AXAVFoundationMediaDescriptionManager registerLegibilityTappingOnPlayer:playerItem:]_block_invoke_3.cold.1
- ___86-[AXAVFoundationMediaDescriptionManager registerLegibilityTappingOnPlayer:playerItem:]_block_invoke_3.cold.2
- ___block_literal_global.330
- ___block_literal_global.339
- ___block_literal_global.342
- _objc_release_x24
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[AVPlayerItemAccessibility _attachToPlayer:] : 184 -> 176
~ +[AVPlayerAccessibility _accessibilityPerformValidations:] : 148 -> 140
~ +[AXAVFoundationGlue accessibilityInitializeBundle] : 152 -> 148
~ ___51+[AXAVFoundationGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ ___51+[AXAVFoundationGlue accessibilityInitializeBundle]_block_invoke_3 : 184 -> 176
~ _accessibilityLocalizedString : 184 -> 176
~ +[AXAVFoundationMediaDescriptionManager sharedManagerIfExists] : 60 -> 12
~ -[AXAVFoundationMediaDescriptionManager init] : 172 -> 168
~ -[AXAVFoundationMediaDescriptionManager registerLegibilityTappingOnPlayer:playerItem:] : 748 -> 704
~ ___86-[AXAVFoundationMediaDescriptionManager registerLegibilityTappingOnPlayer:playerItem:]_block_invoke_3 : 240 -> 336
~ -[AXAVFoundationMediaDescriptionManager _queue_itemNodeForPlayer:] : 344 -> 336
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"AXMVisionEngine\""
- "@\"NSMapTable\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@16@0:8"
- "@24@0:8@16"
- "AXAVFoundationGlue"
- "B16@0:8"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "SafeCategory"
- "TB,R,N"
- "__AVPlayerAccessibility_super"
- "__AVPlayerItemAccessibility_super"
- "_accessibilityPerformValidations:"
- "_engine"
- "_queue"
- "_queue_itemNodeForPlayer:"
- "_queue_nodeToPlayerMap"
- "_shouldAttachLegibilityOutputToItem:"
- "accessibilityInitializeBundle"
- "addResultHandler:"
- "addSourceNode:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "autoTriggerLegibilityEventsWithAVPlayerItem:"
- "ax_nonRedundantDescription"
- "bundleForClass:"
- "bundleIdentifier"
- "countByEnumeratingWithState:objects:count:"
- "hasPrefix:"
- "init"
- "initWithIdentifier:"
- "installSafeCategory:canInteractWithTargetClass:"
- "isTappingMediaDescriptions"
- "isTriggeringLegibilityEvents"
- "isVoiceOverInTheTripleClickMenu"
- "keyEnumerator"
- "localizedStringForKey:value:table:"
- "mainBundle"
- "objectForKey:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "registerLegibilityTappingOnPlayer:playerItem:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "setDebugBuild:"
- "setObject:forKey:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "sharedManager"
- "sharedManagerIfExists"
- "stringWithFormat:"
- "strongToWeakObjectsMapTable"
- "updateEngineConfiguration:"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8^{OpaqueFigPlaybackItem=}16"
- "validateClass:hasInstanceMethod:withFullSignature:"

```
