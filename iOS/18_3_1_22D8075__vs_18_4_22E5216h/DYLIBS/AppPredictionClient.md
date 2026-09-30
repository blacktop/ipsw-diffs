## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient`

```diff

-584.12.0.0.0
-  __TEXT.__text: 0x1762b8
+588.10.0.1.0
+  __TEXT.__text: 0x1781b0
   __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_methlist: 0x16068
+  __TEXT.__objc_methlist: 0x17584
   __TEXT.__const: 0x6f8
-  __TEXT.__cstring: 0x1a430
-  __TEXT.__oslogstring: 0x16598
-  __TEXT.__gcc_except_tab: 0x21f8
+  __TEXT.__cstring: 0x1a62c
+  __TEXT.__oslogstring: 0x16840
+  __TEXT.__gcc_except_tab: 0x21f0
   __TEXT.__dlopen_cstrs: 0x3d0
   __TEXT.__ustring: 0x18a
-  __TEXT.__unwind_info: 0x6070
+  __TEXT.__unwind_info: 0x60a0
   __TEXT.__objc_classname: 0x3825
-  __TEXT.__objc_methname: 0x31196
-  __TEXT.__objc_methtype: 0x64fa
-  __TEXT.__objc_stubs: 0x1b3c0
+  __TEXT.__objc_methname: 0x31351
+  __TEXT.__objc_methtype: 0x64fd
+  __TEXT.__objc_stubs: 0x1b4e0
   __DATA_CONST.__got: 0x1680
-  __DATA_CONST.__const: 0x5e78
+  __DATA_CONST.__const: 0x5e98
   __DATA_CONST.__objc_classlist: 0xd40
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x94d8
+  __DATA_CONST.__objc_selrefs: 0x9680
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0xb70
   __DATA_CONST.__objc_arraydata: 0xae8
   __AUTH_CONST.__auth_got: 0x770
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x26e0
-  __AUTH_CONST.__cfstring: 0x141c0
-  __AUTH_CONST.__objc_const: 0x44e30
+  __AUTH_CONST.__const: 0x2720
+  __AUTH_CONST.__cfstring: 0x14220
+  __AUTH_CONST.__objc_const: 0x42960
   __AUTH_CONST.__objc_intobj: 0xa08
   __AUTH_CONST.__objc_arrayobj: 0x6a8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x168
-  __AUTH.__objc_data: 0x2968
-  __DATA.__objc_ivar: 0x1b0c
+  __AUTH.__objc_data: 0x2738
+  __DATA.__objc_ivar: 0x1b14
   __DATA.__data: 0x1bb0
-  __DATA.__bss: 0x2f0
-  __DATA_DIRTY.__objc_data: 0x5b18
+  __DATA.__bss: 0x2f8
+  __DATA_DIRTY.__objc_data: 0x5d48
   __DATA_DIRTY.__data: 0x88
-  __DATA_DIRTY.__bss: 0x2b0
+  __DATA_DIRTY.__bss: 0x2b8
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 10003
-  Symbols:   12233
-  CStrings:  12687
+  Functions: 10133
+  Symbols:   12435
+  CStrings:  12718
 
Symbols:
+ _kATXCarPlayConfigDidUpdateNotification
+ _objc_retainAutoreleasedReturnValue
- _fmod
CStrings:
+ "%s: New first time CarPlay connection. Returning default OnBoarding suggestions"
+ "%s: No OnBoarding suggestions available, returning nil"
+ "%s: generated CarPlay smart stacks were nil"
+ "%s: generated CarPlay smart stacks. Stack1: %tu widgets, stack2: %tu widgets"
+ "%s: generating onboarding stacks for CarPlay. dayZero:%d, numDescriptors:%lu, descriptorCacheSize:%lu"
+ "-[ATXDefaultHomeScreenItemManager _generateSmartStackForCarPlayWithDescriptorCache]"
+ "-[ATXDefaultHomeScreenItemManager _generateSmartStacksForCarPlay]"
+ "-[ATXDefaultHomeScreenItemProducer carPlayOnboardingStacks]"
+ "-[ATXDefaultHomeScreenItemUpdater _updateCarPlayDefaultsOnQueueWithReason:appLaunchCounts:]"
+ "@84@0:8@16@24@32Q40B48B52B56@60@68B76B80"
+ "ATXCarPlayDefaultWidgetStacks"
+ "ATXDefaultHomeScreenItemUpdater: %s error fetching CarPlay config: %@"
+ "ATXDefaultHomeScreenItemUpdater: Error writing CarPlay defaults to file: %@"
+ "ATXDefaultHomeScreenItemUpdater: Finished updating CarPlay default stack and widget suggestions"
+ "ATXDefaultHomeScreenItemUpdater: updating defaults due to CarPlay config update"
+ "CarPlay config update"
+ "TB,R,N,V_isCarPlay"
+ "_carPlayOnboardingStacks"
+ "_carPlayPath"
+ "_generateSmartStackForCarPlayWithDescriptorCache"
+ "_generateSmartStacksForCarPlay"
+ "_isCarPlay"
+ "_readCarPlayUpdateFromFileWithCompletionHandler:"
+ "_updateCarPlayDefaultsOnQueueWithReason:appLaunchCounts:"
+ "carPlay"
+ "carPlayOnboardingStacks"
+ "com.apple.duetexpertd.ATXDefaultHomeScreenItemUpdater.updateCarPlayDefaults"
+ "com.apple.proactive.CarPlay.WidgetConfigurationManager.cacheDidUpdate"
+ "initWithCandidateWidgets:cachedWidgetPersonalityToAppScore:personalityToDescriptorDictionary:adblDrainClassification:isiPad:isDayZeroExperience:shouldIncludeContactsWidget:cachedHasiCloudFamily:appLaunchCounts:isAmbient:isCarPlay:"
+ "initWithHomeScreenPath:ambientPath:carPlayPath:"
+ "isCHSWidgetDescriptorAllowedForCarPlayOnboardingStacks:"
+ "isCarPlay"
+ "updateDefaultsDueToCarPlayConfigUpdate"
+ "writeCarPlayUpdate:completionHandler:"
- "@80@0:8@16@24@32Q40B48B52B56@60@68B76"
- "initWithCandidateWidgets:cachedWidgetPersonalityToAppScore:personalityToDescriptorDictionary:adblDrainClassification:isiPad:isDayZeroExperience:shouldIncludeContactsWidget:cachedHasiCloudFamily:appLaunchCounts:isAmbient:"
- "initWithHomeScreenPath:ambientPath:"

```
