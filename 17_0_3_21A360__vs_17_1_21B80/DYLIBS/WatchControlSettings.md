## WatchControlSettings

> `/System/Library/PrivateFrameworks/WatchControlSettings.framework/WatchControlSettings`

```diff

-137.0.0.0.0
-  __TEXT.__text: 0x9784
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_methlist: 0x6b0
+141.0.2.0.0
+  __TEXT.__text: 0x9d44
+  __TEXT.__auth_stubs: 0x530
+  __TEXT.__objc_methlist: 0x710
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x18b3
+  __TEXT.__cstring: 0x189a
   __TEXT.__gcc_except_tab: 0x3c
   __TEXT.__oslogstring: 0x606
   __TEXT.__dlopen_cstrs: 0xc6
-  __TEXT.__unwind_info: 0x32c
-  __TEXT.__objc_classname: 0x1cc
-  __TEXT.__objc_methname: 0x1913
-  __TEXT.__objc_methtype: 0x20b
-  __TEXT.__objc_stubs: 0x1320
-  __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0x3a8
+  __TEXT.__unwind_info: 0x368
+  __TEXT.__objc_classname: 0x1db
+  __TEXT.__objc_methname: 0x19a0
+  __TEXT.__objc_methtype: 0x219
+  __TEXT.__objc_stubs: 0x13e0
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__const: 0x2a0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x850
-  __DATA_CONST.__objc_selrefs: 0x748
+  __DATA_CONST.__objc_selrefs: 0x780
   __DATA_CONST.__objc_arraydata: 0x140
   __AUTH_CONST.__objc_const: 0x240
-  __AUTH_CONST.__cfstring: 0x2020
+  __AUTH_CONST.__cfstring: 0x2000
   __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x2b8
+  __AUTH_CONST.__auth_got: 0x2a8
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_classrefs: 0x108
   __DATA.__objc_superrefs: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 246
-  Symbols:   849
-  CStrings:  655
+  Functions: 258
+  Symbols:   873
+  CStrings:  663
 
Symbols:
+ -[WatchControlSettings accessibilityDomainBoolForKey:]
+ -[WatchControlSettings setAccessibilityDomainBool:forKey:]
+ -[WatchControlSettings setZoomDomainBool:forKey:]
+ -[WatchControlSettings zoomDomainAccessor]
+ -[WatchControlSettings zoomDomainBoolForKey:]
+ -[WatchControlSettings(GreySupportFeatures) enabledGreyFeatures]
+ -[WatchControlSettings(QuickActionsV2) quickActionsV2Enabled]
+ -[WatchControlSettings(QuickActionsV2) quickActionsV2State]
+ -[WatchControlSettings(QuickActionsV2) setQuickActionsV2State:]
+ _WCLocalizedStringElton
+ __OBJC_$_CLASS_METHODS_WatchControlSettings(GreySupportClients|GreySupportFeatures|InputSourceManaging|ActionMenuCustomization|GreyEventCustomization|GreyQuickActions|Onboarding|MotionPointer|DwellControl|Visuals|AutoScroll|FocusMovement|HapticFeedback|GreyInternal|Automation|LoggingModes|Experimental|QuickActionsV2)
+ __OBJC_$_INSTANCE_METHODS_WatchControlSettings(GreySupportClients|GreySupportFeatures|InputSourceManaging|ActionMenuCustomization|GreyEventCustomization|GreyQuickActions|Onboarding|MotionPointer|DwellControl|Visuals|AutoScroll|FocusMovement|HapticFeedback|GreyInternal|Automation|LoggingModes|Experimental|QuickActionsV2)
+ ___block_literal_global.456
+ __unnamed_array_storage.483
+ __unnamed_array_storage.510
+ __unnamed_array_storage.529
+ __unnamed_array_storage.534
+ __unnamed_array_storage.545
+ __unnamed_array_storage.578
+ __unnamed_array_storage.585
+ __unnamed_array_storage.592
+ _kAXSVoiceOverWatchHandGestures
+ _kAXSZoomPreferenceDomain
+ _kAXSZoomWatchHandGestures
+ _objc_msgSend$accessibilityDomainBoolForKey:
+ _objc_msgSend$intValue
+ _objc_msgSend$quickActionsV2Enabled
+ _objc_msgSend$quickActionsV2State
+ _objc_msgSend$setAccessibilityDomainBool:forKey:
+ _objc_msgSend$setZoomDomainBool:forKey:
+ _objc_msgSend$zoomDomainAccessor
+ _objc_msgSend$zoomDomainBoolForKey:
- -[WatchControlSettings(GreySupportFeatures) enabledGreyFeatureNames]
- __AXSWatchQuickActionsEnabled
- __AXSWatchQuickActionsSetState
- __OBJC_$_CLASS_METHODS_WatchControlSettings(GreySupportClients|GreySupportFeatures|InputSourceManaging|ActionMenuCustomization|GreyEventCustomization|GreyQuickActions|Onboarding|MotionPointer|DwellControl|Visuals|AutoScroll|FocusMovement|HapticFeedback|GreyInternal|Automation|LoggingModes|Experimental)
- __OBJC_$_INSTANCE_METHODS_WatchControlSettings(GreySupportClients|GreySupportFeatures|InputSourceManaging|ActionMenuCustomization|GreyEventCustomization|GreyQuickActions|Onboarding|MotionPointer|DwellControl|Visuals|AutoScroll|FocusMovement|HapticFeedback|GreyInternal|Automation|LoggingModes|Experimental)
- ___block_literal_global.467
- __unnamed_array_storage.489
- __unnamed_array_storage.516
- __unnamed_array_storage.535
- __unnamed_array_storage.540
- __unnamed_array_storage.551
- __unnamed_array_storage.584
- __unnamed_array_storage.591
- __unnamed_array_storage.598
- _objc_msgSend$setVoiceOverHandGesturesEnabled:
- _objc_msgSend$setZoomHandGesturesEnabled:
CStrings:
+ "0E581E21-36BA-4770-9408-0467585E8495"
+ "Localizable-elton"
+ "QuickActionsV2"
+ "accessibilityDomainBoolForKey:"
+ "applewatch.side.button.arrow.left"
+ "enabledGreyFeatures"
+ "intValue"
+ "quickActionsV2Enabled"
+ "quickActionsV2State"
+ "setAccessibilityDomainBool:forKey:"
+ "setQuickActionsV2State:"
+ "setZoomDomainBool:forKey:"
+ "v28@0:8B16@20"
+ "zoomDomainAccessor"
+ "zoomDomainBoolForKey:"
- "enabledGreyFeatureNames"
- "grey.feature.name.quick.actions"
- "grey.feature.name.voiceover"
- "grey.feature.name.watchcontrol"
- "grey.feature.name.zoom"
- "setVoiceOverHandGesturesEnabled:"
- "setZoomHandGesturesEnabled:"

```
