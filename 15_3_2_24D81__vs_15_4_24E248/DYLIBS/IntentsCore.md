## IntentsCore

> `/System/Library/PrivateFrameworks/IntentsCore.framework/Versions/A/IntentsCore`

```diff

-3208.0.0.0.0
-  __TEXT.__text: 0x123c8
+3506.0.1.0.0
+  __TEXT.__text: 0x123a4
   __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0xc00
+  __TEXT.__objc_methlist: 0xe3c
   __TEXT.__const: 0x90
+  __TEXT.__dlopen_cstrs: 0x16a
   __TEXT.__gcc_except_tab: 0x278
   __TEXT.__cstring: 0x1a64
   __TEXT.__oslogstring: 0x13c2
-  __TEXT.__dlopen_cstrs: 0x16a
-  __TEXT.__unwind_info: 0x420
+  __TEXT.__unwind_info: 0x428
   __TEXT.__objc_classname: 0x30b
   __TEXT.__objc_methname: 0x385f
   __TEXT.__objc_methtype: 0x7a2

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd30
+  __DATA_CONST.__objc_selrefs: 0xdc0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x278
   __AUTH_CONST.__const: 0x9f0
   __AUTH_CONST.__cfstring: 0x5a0
-  __AUTH_CONST.__objc_const: 0x22a8
+  __AUTH_CONST.__objc_const: 0x1ec0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AE8A6B61-C591-307D-A088-4871B0406D0C
+  UUID: 5260BC28-9E56-3E37-B242-1C903E6F922E
   Functions: 373
   Symbols:   1289
   CStrings:  976
Functions:
~ -[INCExtensionRequest _scheduleContextTimer] : 272 -> 268
~ -[INCExtensionTransaction _updateCurrentUserActivityForType:intent:intentResponse:] : 1400 -> 1404
~ -[INCExtensionTransactionState description] : 280 -> 296
~ -[INCExtensionTransactionState initWithType:intent:intentResponse:userActivities:] -> _INCExtensionTransactionStateTypeGetName : 220 -> 32
~ _INCExtensionTransactionStateTypeGetName -> -[INCExtensionTransactionState initWithType:intent:intentResponse:userActivities:] : 32 -> 220
~ -[INCExtensionConnection listener:shouldAcceptNewConnection:] : 328 -> 324
~ -[INCExtensionConnection _startRequestTimerWithExtensionProxy:] : 716 -> 712
~ __54-[INCExtensionConnection resumeWithCompletionHandler:]_block_invoke.28 : 1136 -> 1128
~ -[INCAppProxy launchAppInBackground:restrictAppsToCarPlay:userActivityIdentifier:completionHandler:] : 356 -> 352
~ -[INCIntentDefaultValueProvider loadDefaultValuesWithAttributes:extensionProxy:completionHandler:] : 1348 -> 1340
~ -[INCIntentDefaultValueProvider loadDefaultValuesWithCompletionHandler:] : 948 -> 944
~ ___72-[INCIntentDefaultValueProvider loadDefaultValuesWithCompletionHandler:]_block_invoke : 304 -> 300
~ __72-[INCIntentDefaultValueProvider loadDefaultValuesWithCompletionHandler:]_block_invoke.8 : 212 -> 192
~ ___72-[INCIntentDefaultValueProvider loadDefaultValuesWithCompletionHandler:]_block_invoke_2 : 132 -> 124
~ ___56-[INCExtensionProxy confirmIntentWithCompletionHandler:]_block_invoke : 332 -> 344
~ __65-[INCExtensionProxy resolveIntentSlotKeyPaths:completionHandler:]_block_invoke.30 : 216 -> 220
~ -[INCAppLaunchRequest _retainsSiri] : 252 -> 248
~ -[INCAppLaunchRequest initWithURL:error:] : 1548 -> 1556
~ -[INCAppLaunchRequest initWithAudioCallIntentForCarousel:error:] : 760 -> 764
~ -[INCAppLaunchRequest initWithIntent:userActivity:inBackground:retainsSiri:error:] : 896 -> 908
~ -[INCAppLaunchRequest initWithInteraction:userActivity:inBackground:retainsSiri:error:] : 724 -> 728
~ _INCUnderlyingInteractionFromInteraction : 936 -> 932
~ -[INCWidgetIntentProvider _provideAppIntentWithOptions:completionHandler:] : 1436 -> 1404
~ _getWFLinkActionSerializedParametersForLNActionSymbolLoc : 204 -> 200
~ -[INCWidgetIntentProvider provideIntentWithOptions:completionHandler:] : 3000 -> 3012

```
