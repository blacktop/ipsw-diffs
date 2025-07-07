## TextInputUI

> `/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI`

```diff

-9075.1.102.0.0
-  __TEXT.__text: 0xc8f00
-  __TEXT.__auth_stubs: 0x28b0
-  __TEXT.__objc_methlist: 0xbbb4
-  __TEXT.__const: 0x1e40
+9079.2.102.0.0
+  __TEXT.__text: 0xc9f98
+  __TEXT.__auth_stubs: 0x28c0
+  __TEXT.__objc_methlist: 0xbbfc
+  __TEXT.__const: 0x1e50
   __TEXT.__dlopen_cstrs: 0x1c4
   __TEXT.__swift5_typeref: 0xe10
-  __TEXT.__oslogstring: 0x2522
-  __TEXT.__swift5_capture: 0x244
-  __TEXT.__cstring: 0x9b36
+  __TEXT.__oslogstring: 0x25e0
+  __TEXT.__swift5_capture: 0x254
+  __TEXT.__cstring: 0x9bc2
   __TEXT.__constg_swiftt: 0x98c
   __TEXT.__swift5_reflstr: 0x435
   __TEXT.__swift5_fieldmd: 0x450

   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__swift5_assocty: 0x158
   __TEXT.__ustring: 0x78
-  __TEXT.__unwind_info: 0x2b30
+  __TEXT.__unwind_info: 0x2bf0
   __TEXT.__eh_frame: 0x8e8
   __TEXT.__objc_classname: 0x14e2
-  __TEXT.__objc_methname: 0x2213f
-  __TEXT.__objc_methtype: 0x4d70
-  __TEXT.__objc_stubs: 0x1ac40
+  __TEXT.__objc_methname: 0x22201
+  __TEXT.__objc_methtype: 0x4d9c
+  __TEXT.__objc_stubs: 0x1ad60
   __DATA_CONST.__got: 0x1100
   __DATA_CONST.__const: 0x71c0
   __DATA_CONST.__objc_classlist: 0x500
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8158
+  __DATA_CONST.__objc_selrefs: 0x81a0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x348
-  __DATA_CONST.__objc_arraydata: 0x558
-  __AUTH_CONST.__auth_got: 0x1460
-  __AUTH_CONST.__const: 0x1410
-  __AUTH_CONST.__cfstring: 0xb200
-  __AUTH_CONST.__objc_const: 0x129d0
+  __DATA_CONST.__objc_arraydata: 0x560
+  __AUTH_CONST.__auth_got: 0x1468
+  __AUTH_CONST.__const: 0x1438
+  __AUTH_CONST.__cfstring: 0xb2a0
+  __AUTH_CONST.__objc_const: 0x129d8
   __AUTH_CONST.__objc_intobj: 0x318
-  __AUTH_CONST.__objc_arrayobj: 0x1e0
+  __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_doubleobj: 0x170
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_floatobj: 0xe0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 40809C33-3CF4-3B64-B989-BDE3232758C7
-  Functions: 4602
-  Symbols:   15549
-  CStrings:  9735
+  UUID: FFD8546E-17CD-3A19-B32B-F9ED0236D5A3
+  Functions: 4610
+  Symbols:   15572
+  CStrings:  9758
 
Symbols:
+ -[TUIKBKeyView resetPanAnimations]
+ -[TUIKeyboardState showsInputOrAssistantViews]
+ -[TUIKeyboardState showsInputViews]
+ -[TUIKeyboardTrackingCoordinator _filteredStartingSizeDiff:sizeUpdate:]
+ -[TUIKeyboardTrackingCoordinator incomingKeyboardFrame]
+ -[TUIKeyplane unduplicateTenKeySwitchKey:]
+ __TUIKeyboardTrackingLogger.8138
+ __TUIKeyboardTrackingLogger.log.8143
+ __TUIKeyboardTrackingLogger.onceToken.8141
+ ___90-[TUIKeyboardTrackingCoordinator updateClientsForState:finalFrame:animationInfo:forStart:]_block_invoke_5
+ ___90-[TUIKeyboardTrackingCoordinator updateClientsForState:finalFrame:animationInfo:forStart:]_block_invoke_6
+ ___Block_byref_object_copy_.12217
+ ___Block_byref_object_copy_.5130
+ ___Block_byref_object_copy_.5470
+ ___Block_byref_object_copy_.7889
+ ___Block_byref_object_dispose_.12218
+ ___Block_byref_object_dispose_.5131
+ ___Block_byref_object_dispose_.5471
+ ___Block_byref_object_dispose_.7890
+ ____TUIKeyboardTrackingLogger_block_invoke.8146
+ ___block_descriptor_97_8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_literal_global.10060
+ ___block_literal_global.10925
+ ___block_literal_global.11084
+ ___block_literal_global.11298
+ ___block_literal_global.12227
+ ___block_literal_global.12452
+ ___block_literal_global.12930
+ ___block_literal_global.144
+ ___block_literal_global.146
+ ___block_literal_global.217
+ ___block_literal_global.312.10955
+ ___block_literal_global.37.8722
+ ___block_literal_global.4.12475
+ ___block_literal_global.4113
+ ___block_literal_global.4308
+ ___block_literal_global.474.10155
+ ___block_literal_global.4980
+ ___block_literal_global.5162
+ ___block_literal_global.5609
+ ___block_literal_global.6303
+ ___block_literal_global.6422
+ ___block_literal_global.6684
+ ___block_literal_global.6955
+ ___block_literal_global.728
+ ___block_literal_global.732
+ ___block_literal_global.7483
+ ___block_literal_global.7944
+ ___block_literal_global.8142
+ ___block_literal_global.8335
+ ___block_literal_global.8725
+ _objc_msgSend$_filteredStartingSizeDiff:sizeUpdate:
+ _objc_msgSend$_isInAnimationBlock
+ _objc_msgSend$changeBackgroundToEnabled
+ _objc_msgSend$internalSharedClientWrapper
+ _objc_msgSend$layerForRenderFlags:
+ _objc_msgSend$previousKeyboardState
+ _objc_msgSend$resetPanAnimations
+ _objc_msgSend$showsInputOrAssistantViews
+ _objc_msgSend$showsInputViews
+ _objc_msgSend$unduplicateTenKeySwitchKey:
+ _sharedInstance.onceToken.6421
- -[TUIAssistantButtonBarView _uncollapseAllGroupsForNewSizeIfNecessary:]
- __TUIKeyboardTrackingLogger.8140
- __TUIKeyboardTrackingLogger.log.8145
- __TUIKeyboardTrackingLogger.onceToken.8143
- ___Block_byref_object_copy_.12213
- ___Block_byref_object_copy_.5146
- ___Block_byref_object_copy_.5479
- ___Block_byref_object_copy_.7891
- ___Block_byref_object_dispose_.12214
- ___Block_byref_object_dispose_.5147
- ___Block_byref_object_dispose_.5480
- ___Block_byref_object_dispose_.7892
- ____TUIKeyboardTrackingLogger_block_invoke.8148
- ___block_descriptor_97_8_32s40s48bs_e8_v12?0B8ls32l8s48l8s40l8
- ___block_literal_global.10062
- ___block_literal_global.10920
- ___block_literal_global.11079
- ___block_literal_global.11295
- ___block_literal_global.12223
- ___block_literal_global.12448
- ___block_literal_global.12922
- ___block_literal_global.138
- ___block_literal_global.140
- ___block_literal_global.214
- ___block_literal_global.311
- ___block_literal_global.37.8724
- ___block_literal_global.4.12471
- ___block_literal_global.4115
- ___block_literal_global.4339
- ___block_literal_global.460
- ___block_literal_global.4999
- ___block_literal_global.5178
- ___block_literal_global.5614
- ___block_literal_global.6306
- ___block_literal_global.6425
- ___block_literal_global.6688
- ___block_literal_global.6958
- ___block_literal_global.722
- ___block_literal_global.726
- ___block_literal_global.7485
- ___block_literal_global.7946
- ___block_literal_global.8144
- ___block_literal_global.8338
- ___block_literal_global.8727
- _objc_msgSend$_uncollapseAllGroupsForNewSizeIfNecessary:
- _sharedInstance.onceToken.6424
CStrings:
+ "%@; Update from coordinator for IAV bounds change"
+ "Arabic-With-QWERTY-Version2"
+ "QWERTY-Haitian-Creole"
+ "QWERTY-Maori"
+ "Successfully created poll candidate container (for autocorrection). Calling completion handler."
+ "Successfully created poll candidate container (for candidate selection). Calling completion handler."
+ "TUIKeyplaneKeySizingGuide"
+ "Tracking provider change to %@ complete."
+ "[Notifications] Transition from %@ to %@ will send only frame change"
+ "_filteredStartingSizeDiff:sizeUpdate:"
+ "_isInAnimationBlock"
+ "changeBackgroundToEnabled"
+ "extendsFromKeyplane"
+ "extra_multiscript_layouts_testfest"
+ "incomingKeyboardFrame"
+ "layerForRenderFlags:"
+ "pan opacity"
+ "resetPanAnimations"
+ "showsInputOrAssistantViews"
+ "showsInputViews"
+ "unduplicateTenKeySwitchKey:"
+ "{CGSize=dd}48@0:8{CGSize=dd}16{CGSize=dd}32"
- "Successfully created poll candidate container. Calling completion handler."
- "Tracking provider change to complete. State: %@"
- "Update from coordinator for IAV bounds change"
- "_uncollapseAllGroupsForNewSizeIfNecessary:"

```
