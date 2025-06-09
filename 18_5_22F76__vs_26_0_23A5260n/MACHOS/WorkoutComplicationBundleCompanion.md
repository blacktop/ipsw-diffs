## WorkoutComplicationBundleCompanion

> `/System/Library/NanoTimeKit/ComplicationBundles/WorkoutComplicationBundleCompanion.bundle/WorkoutComplicationBundleCompanion`

```diff

-907.15.0.0.0
-  __TEXT.__text: 0x3e94
-  __TEXT.__auth_stubs: 0x3f0
-  __TEXT.__objc_stubs: 0x1200
-  __TEXT.__objc_methlist: 0x70c
-  __TEXT.__objc_methname: 0x171a
-  __TEXT.__cstring: 0x415
-  __TEXT.__objc_classname: 0x19e
-  __TEXT.__objc_methtype: 0x47c
-  __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0x5c
-  __TEXT.__oslogstring: 0x1a4
-  __TEXT.__unwind_info: 0x1a0
-  __DATA_CONST.__auth_got: 0x208
-  __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__const: 0x1e8
+1061.1.1.0.0
+  __TEXT.__text: 0x7a84
+  __TEXT.__auth_stubs: 0x280
+  __TEXT.__objc_stubs: 0x12a0
+  __TEXT.__objc_methlist: 0x734
+  __TEXT.__cstring: 0x39d
+  __TEXT.__objc_methname: 0x17e9
+  __TEXT.__const: 0xe8
+  __TEXT.__objc_classname: 0x1b9
+  __TEXT.__objc_methtype: 0x4a2
+  __TEXT.__gcc_except_tab: 0x88
+  __TEXT.__oslogstring: 0x272
+  __TEXT.__unwind_info: 0x148
+  __DATA_CONST.__auth_got: 0x150
+  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__const: 0x1a8
   __DATA_CONST.__cfstring: 0x500
   __DATA_CONST.__objc_classlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0xbe0
-  __DATA.__objc_selrefs: 0x6f8
+  __DATA.__objc_const: 0xc00
+  __DATA.__objc_selrefs: 0x720
   __DATA.__objc_ivar: 0x58
   __DATA.__objc_data: 0x280
-  __DATA.__data: 0x240
+  __DATA.__data: 0x2a0
   __DATA.__bss: 0x40
   - /System/Library/Frameworks/ClockKit.framework/ClockKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/NanoTimeKitCompanion.framework/NanoTimeKitCompanion
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D93EC69A-1E19-3472-B824-7DEE1406DF37
-  Functions: 115
-  Symbols:   160
-  CStrings:  442
+  UUID: 66C3E5C0-A371-3DD9-AC55-282650708A55
+  Functions: 114
+  Symbols:   1097
+  CStrings:  451
 
Symbols:
+ 
+ +[NLWorkoutComplicationDataSource _workoutTintColor]
+ +[NLWorkoutComplicationDataSource acceptsComplicationFamily:forDevice:]
+ +[NLWorkoutComplicationDataSource acceptsComplicationType:forDevice:]
+ +[NLWorkoutComplicationDataSource appIdentifier]
+ +[NLWorkoutComplicationDataSource hasMigratedToWidgetForFamily:device:]
+ +[NLWorkoutComplicationDataSource legacyNTKComplicationType]
+ +[NLWorkoutComplicationDataSource localizedAppName]
+ +[NLWorkoutComplicationImageProvider noWorkoutImageForComplicationFamily:]
+ -[NLWorkoutComplicationAnimatedWrapperView .cxx_destruct]
+ -[NLWorkoutComplicationAnimatedWrapperView _applyAnimationForPauseState:animated:]
+ -[NLWorkoutComplicationAnimatedWrapperView _updateState]
+ -[NLWorkoutComplicationAnimatedWrapperView _updateTint]
+ -[NLWorkoutComplicationAnimatedWrapperView color]
+ -[NLWorkoutComplicationAnimatedWrapperView imageProvider]
+ -[NLWorkoutComplicationAnimatedWrapperView initWithAnimationImages:]
+ -[NLWorkoutComplicationAnimatedWrapperView layoutSubviews]
+ -[NLWorkoutComplicationAnimatedWrapperView overrideColor]
+ -[NLWorkoutComplicationAnimatedWrapperView setColor:]
+ -[NLWorkoutComplicationAnimatedWrapperView setImageProvider:]
+ -[NLWorkoutComplicationAnimatedWrapperView setOverrideColor:]
+ -[NLWorkoutComplicationAnimatedWrapperView setUsesLegibility:]
+ -[NLWorkoutComplicationAnimatedWrapperView sizeThatFits:]
+ -[NLWorkoutComplicationAnimatedWrapperView usesLegibility]
+ -[NLWorkoutComplicationDataSource .cxx_destruct]
+ -[NLWorkoutComplicationDataSource _animationImages]
+ -[NLWorkoutComplicationDataSource _handleDeviceLockChange]
+ -[NLWorkoutComplicationDataSource _hasActiveWorkout]
+ -[NLWorkoutComplicationDataSource _hasPausedActiveWorkout]
+ -[NLWorkoutComplicationDataSource _invalidate]
+ -[NLWorkoutComplicationDataSource _makeAnimatedImageProvider]
+ -[NLWorkoutComplicationDataSource _noActiveWorkoutImageForComplicationFamily:]
+ -[NLWorkoutComplicationDataSource _noWorkoutsTemplate]
+ -[NLWorkoutComplicationDataSource _signatureTemplateWithFamily:hasActiveWorkout:hasPausedActiveWorkout:]
+ -[NLWorkoutComplicationDataSource _startObserving]
+ -[NLWorkoutComplicationDataSource _stopObservingSynchronously:]
+ -[NLWorkoutComplicationDataSource _templateForActiveWorkoutInSwitcher:]
+ -[NLWorkoutComplicationDataSource _templateForWorkout:family:]
+ -[NLWorkoutComplicationDataSource _unknownTemplateForFamily:]
+ -[NLWorkoutComplicationDataSource _updateActiveWorkoutState]
+ -[NLWorkoutComplicationDataSource activeWorkoutSnapshot]
+ -[NLWorkoutComplicationDataSource alwaysShowIdealizedTemplateInSwitcher]
+ -[NLWorkoutComplicationDataSource currentSwitcherTemplate]
+ -[NLWorkoutComplicationDataSource dealloc]
+ -[NLWorkoutComplicationDataSource didUpdateWorkoutSnapshot:]
+ -[NLWorkoutComplicationDataSource fetchWidgetMigrationForDescriptor:family:completion:]
+ -[NLWorkoutComplicationDataSource getCurrentTimelineEntryWithHandler:]
+ -[NLWorkoutComplicationDataSource getLaunchURLForTimelineEntryDate:timeTravelDate:withHandler:]
+ -[NLWorkoutComplicationDataSource hasKnownLastWorkoutState]
+ -[NLWorkoutComplicationDataSource healthStore]
+ -[NLWorkoutComplicationDataSource initWithComplication:family:forDevice:]
+ -[NLWorkoutComplicationDataSource isLoadingLastWorkout]
+ -[NLWorkoutComplicationDataSource lastWorkoutQuery]
+ -[NLWorkoutComplicationDataSource lastWorkout]
+ -[NLWorkoutComplicationDataSource lockedTemplate]
+ -[NLWorkoutComplicationDataSource resumeAnimations]
+ -[NLWorkoutComplicationDataSource sampleTemplate]
+ -[NLWorkoutComplicationDataSource setActiveWorkoutSnapshot:]
+ -[NLWorkoutComplicationDataSource setHasKnownLastWorkoutState:]
+ -[NLWorkoutComplicationDataSource setHealthStore:]
+ -[NLWorkoutComplicationDataSource setLastWorkout:]
+ -[NLWorkoutComplicationDataSource setLastWorkoutQuery:]
+ -[NLWorkoutComplicationDataSource setLoadingLastWorkout:]
+ -[NLWorkoutComplicationDataSource setWorkoutObservationQuery:]
+ -[NLWorkoutComplicationDataSource setWorkoutObserver:]
+ -[NLWorkoutComplicationDataSource workoutObservationQuery]
+ -[NLWorkoutComplicationDataSource workoutObserver]
+ -[NLWorkoutComplicationImageProvider copyWithZone:]
+ -[NLWorkoutComplicationImageProvider initWithPaused:]
+ -[NLWorkoutComplicationImageProvider isPaused]
+ -[NLWorkoutComplicationImageProvider setPaused:]
+ -[NLWorkoutImageView dealloc]
+ -[NLWorkoutImageView init]
+ -[NLWorkoutImageView observeValueForKeyPath:ofObject:change:context:]
+ -[NLWorkoutImageView startAnimating]
+ -[NLWorkoutRichComplicationBaseView .cxx_destruct]
+ -[NLWorkoutRichComplicationBaseView _filterStyle]
+ -[NLWorkoutRichComplicationBaseView _updateUI]
+ -[NLWorkoutRichComplicationBaseView configureWithImageProvider:reason:]
+ -[NLWorkoutRichComplicationBaseView filterProvider]
+ -[NLWorkoutRichComplicationBaseView initFullColorImageViewWithDevice:]
+ -[NLWorkoutRichComplicationBaseView initWithFrame:]
+ -[NLWorkoutRichComplicationBaseView layoutSubviews]
+ -[NLWorkoutRichComplicationBaseView noActiveWorkoutImageName]
+ -[NLWorkoutRichComplicationBaseView noActiveWorkoutImage]
+ -[NLWorkoutRichComplicationBaseView pauseLiveFullColorImageView]
+ -[NLWorkoutRichComplicationBaseView resumeLiveFullColorImageView]
+ -[NLWorkoutRichComplicationBaseView setFilterProvider:]
+ -[NLWorkoutRichComplicationBaseView transitionToMonochromeWithFraction:]
+ -[NLWorkoutRichComplicationBaseView updateMonochromeColor]
+ -[NLWorkoutRichComplicationCircularView noActiveWorkoutImageName]
+ -[NLWorkoutRichComplicationCircularView noActiveWorkoutImage]
+ -[NLWorkoutRichComplicationCornerView noActiveWorkoutImageName]
+ -[NLWorkoutRichComplicationCornerView noActiveWorkoutImage]
+ -[NLWorkoutRichComplicationExtraLargeView noActiveWorkoutImageName]
+ -[NLWorkoutRichComplicationExtraLargeView noActiveWorkoutImage]
+ /Library/Caches/com.apple.xbs/Binaries/SessionTrackerApp/install/TempContent/Objects/SessionTrackerApp.build/WorkoutComplicationBundleCompanion.build/Objects-normal/arm64e/NLWorkoutComplicationAnimatedWrapperView.o
+ /Library/Caches/com.apple.xbs/Binaries/SessionTrackerApp/install/TempContent/Objects/SessionTrackerApp.build/WorkoutComplicationBundleCompanion.build/Objects-normal/arm64e/NLWorkoutComplicationBundleUtilities.o
+ /Library/Caches/com.apple.xbs/Binaries/SessionTrackerApp/install/TempContent/Objects/SessionTrackerApp.build/WorkoutComplicationBundleCompanion.build/Objects-normal/arm64e/NLWorkoutComplicationDataSource.o
+ /Library/Caches/com.apple.xbs/Binaries/SessionTrackerApp/install/TempContent/Objects/SessionTrackerApp.build/WorkoutComplicationBundleCompanion.build/Objects-normal/arm64e/NLWorkoutComplicationImageProvider.o
+ /Library/Caches/com.apple.xbs/Binaries/SessionTrackerApp/install/TempContent/Objects/SessionTrackerApp.build/WorkoutComplicationBundleCompanion.build/Objects-normal/arm64e/NLWorkoutRichComplicationBaseView.o
+ /Library/Caches/com.apple.xbs/Binaries/SessionTrackerApp/install/TempContent/Objects/SessionTrackerApp.build/WorkoutComplicationBundleCompanion.build/Objects-normal/arm64e/NLWorkoutRichComplicationCircularView.o
+ /Library/Caches/com.apple.xbs/Binaries/SessionTrackerApp/install/TempContent/Objects/SessionTrackerApp.build/WorkoutComplicationBundleCompanion.build/Objects-normal/arm64e/NLWorkoutRichComplicationCornerView.o
+ /Library/Caches/com.apple.xbs/Binaries/SessionTrackerApp/install/TempContent/Objects/SessionTrackerApp.build/WorkoutComplicationBundleCompanion.build/Objects-normal/arm64e/NLWorkoutRichComplicationExtraLargeView.o
+ /Library/Caches/com.apple.xbs/Sources/SessionTrackerApp/WorkoutComplicationBundle/
+ /Library/Caches/com.apple.xbs/Sources/SessionTrackerApp/WorkoutComplicationBundle/Rich Complication/
+ GCC_except_table25
+ GCC_except_table35
+ NLWorkoutComplicationAnimatedWrapperView.m
+ NLWorkoutComplicationBundle.__bundle
+ NLWorkoutComplicationBundle.onceToken
+ NLWorkoutComplicationBundleUtilities.m
+ NLWorkoutComplicationDataSource.m
+ NLWorkoutComplicationImageProvider.m
+ NLWorkoutKeyNonGradientTextColor.__color
+ NLWorkoutKeyNonGradientTextColor.onceToken
+ NLWorkoutNoNonGradientTextColor.__color
+ NLWorkoutNoNonGradientTextColor.onceToken
+ NLWorkoutRichComplicationBaseView.m
+ NLWorkoutRichComplicationCircularView.m
+ NLWorkoutRichComplicationCornerView.m
+ NLWorkoutRichComplicationExtraLargeView.m
+ OBJC_IVAR_$_NLWorkoutComplicationAnimatedWrapperView._color
+ OBJC_IVAR_$_NLWorkoutComplicationAnimatedWrapperView._imageProvider
+ OBJC_IVAR_$_NLWorkoutComplicationAnimatedWrapperView._imageView
+ OBJC_IVAR_$_NLWorkoutComplicationAnimatedWrapperView._overrideColor
+ OBJC_IVAR_$_NLWorkoutComplicationAnimatedWrapperView._usesLegibility
+ OBJC_IVAR_$_NLWorkoutComplicationDataSource._activeWorkoutSnapshot
+ OBJC_IVAR_$_NLWorkoutComplicationDataSource._animationImages
+ OBJC_IVAR_$_NLWorkoutComplicationDataSource._deviceIsLocked
+ OBJC_IVAR_$_NLWorkoutComplicationDataSource._hasKnownLastWorkoutState
+ OBJC_IVAR_$_NLWorkoutComplicationDataSource._healthQueue
+ OBJC_IVAR_$_NLWorkoutComplicationDataSource._healthStore
+ OBJC_IVAR_$_NLWorkoutComplicationDataSource._inUVPreview
+ OBJC_IVAR_$_NLWorkoutComplicationDataSource._lastWorkout
+ OBJC_IVAR_$_NLWorkoutComplicationDataSource._lastWorkoutQuery
+ OBJC_IVAR_$_NLWorkoutComplicationDataSource._loadingLastWorkout
+ OBJC_IVAR_$_NLWorkoutComplicationDataSource._workoutObservationQuery
+ OBJC_IVAR_$_NLWorkoutComplicationDataSource._workoutObserver
+ OBJC_IVAR_$_NLWorkoutComplicationDataSource._workoutStateNotifyToken
+ OBJC_IVAR_$_NLWorkoutComplicationImageProvider._paused
+ OBJC_IVAR_$_NLWorkoutRichComplicationBaseView._filterProvider
+ OBJC_IVAR_$_NLWorkoutRichComplicationBaseView._state
+ OBJC_IVAR_$_NLWorkoutRichComplicationBaseView._staticImageView
+ _FIUIDeviceValueForLayoutMetric
+ _NLWorkoutComplicationBundle
+ __60-[NLWorkoutComplicationDataSource _updateActiveWorkoutState]_block_invoke.417
+ __OBJC_$_CLASS_METHODS_NLWorkoutComplicationDataSource
+ __OBJC_$_CLASS_METHODS_NLWorkoutComplicationImageProvider
+ __OBJC_$_INSTANCE_METHODS_NLWorkoutComplicationAnimatedWrapperView
+ __OBJC_$_INSTANCE_METHODS_NLWorkoutComplicationDataSource
+ __OBJC_$_INSTANCE_METHODS_NLWorkoutComplicationImageProvider
+ __OBJC_$_INSTANCE_METHODS_NLWorkoutImageView
+ __OBJC_$_INSTANCE_METHODS_NLWorkoutRichComplicationBaseView
+ __OBJC_$_INSTANCE_METHODS_NLWorkoutRichComplicationCircularView
+ __OBJC_$_INSTANCE_METHODS_NLWorkoutRichComplicationCornerView
+ __OBJC_$_INSTANCE_METHODS_NLWorkoutRichComplicationExtraLargeView
+ __OBJC_$_INSTANCE_VARIABLES_NLWorkoutComplicationAnimatedWrapperView
+ __OBJC_$_INSTANCE_VARIABLES_NLWorkoutComplicationDataSource
+ __OBJC_$_INSTANCE_VARIABLES_NLWorkoutComplicationImageProvider
+ __OBJC_$_INSTANCE_VARIABLES_NLWorkoutRichComplicationBaseView
+ __OBJC_$_PROP_LIST_CLKComplicationImageView
+ __OBJC_$_PROP_LIST_CLKFullColorImageView
+ __OBJC_$_PROP_LIST_CLKMonochromeComplicationView
+ __OBJC_$_PROP_LIST_CLKUIColoringView
+ __OBJC_$_PROP_LIST_NLWorkoutComplicationAnimatedWrapperView
+ __OBJC_$_PROP_LIST_NLWorkoutComplicationDataSource
+ __OBJC_$_PROP_LIST_NLWorkoutComplicationImageProvider
+ __OBJC_$_PROP_LIST_NLWorkoutRichComplicationBaseView
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CLKComplicationImageView
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CLKFullColorImageView
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CLKMonochromeComplicationView
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CLKUIColoringView
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CLKFullColorImageView
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CLKUIColoringView
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__HKWorkoutObserverDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CLKComplicationImageView
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CLKFullColorImageView
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CLKMonochromeComplicationView
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CLKUIColoringView
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES__HKWorkoutObserverDelegate
+ __OBJC_$_PROTOCOL_REFS_CDComplicationImageView
+ __OBJC_$_PROTOCOL_REFS_CLKFullColorImageView
+ __OBJC_$_PROTOCOL_REFS_CLKMonochromeComplicationView
+ __OBJC_$_PROTOCOL_REFS_CLKUIColoringView
+ __OBJC_CLASS_PROTOCOLS_$_NLWorkoutComplicationAnimatedWrapperView
+ __OBJC_CLASS_PROTOCOLS_$_NLWorkoutComplicationDataSource
+ __OBJC_CLASS_PROTOCOLS_$_NLWorkoutRichComplicationBaseView
+ __OBJC_CLASS_RO_$_NLWorkoutComplicationAnimatedWrapperView
+ __OBJC_CLASS_RO_$_NLWorkoutComplicationDataSource
+ __OBJC_CLASS_RO_$_NLWorkoutComplicationImageProvider
+ __OBJC_CLASS_RO_$_NLWorkoutImageView
+ __OBJC_CLASS_RO_$_NLWorkoutRichComplicationBaseView
+ __OBJC_CLASS_RO_$_NLWorkoutRichComplicationCircularView
+ __OBJC_CLASS_RO_$_NLWorkoutRichComplicationCornerView
+ __OBJC_CLASS_RO_$_NLWorkoutRichComplicationExtraLargeView
+ __OBJC_LABEL_PROTOCOL_$_CDComplicationImageView
+ __OBJC_LABEL_PROTOCOL_$_CLKComplicationImageView
+ __OBJC_LABEL_PROTOCOL_$_CLKFullColorImageView
+ __OBJC_LABEL_PROTOCOL_$_CLKMonochromeComplicationView
+ __OBJC_LABEL_PROTOCOL_$_CLKUIColoringView
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$__HKWorkoutObserverDelegate
+ __OBJC_METACLASS_RO_$_NLWorkoutComplicationAnimatedWrapperView
+ __OBJC_METACLASS_RO_$_NLWorkoutComplicationDataSource
+ __OBJC_METACLASS_RO_$_NLWorkoutComplicationImageProvider
+ __OBJC_METACLASS_RO_$_NLWorkoutImageView
+ __OBJC_METACLASS_RO_$_NLWorkoutRichComplicationBaseView
+ __OBJC_METACLASS_RO_$_NLWorkoutRichComplicationCircularView
+ __OBJC_METACLASS_RO_$_NLWorkoutRichComplicationCornerView
+ __OBJC_METACLASS_RO_$_NLWorkoutRichComplicationExtraLargeView
+ __OBJC_PROTOCOL_$_CDComplicationImageView
+ __OBJC_PROTOCOL_$_CLKComplicationImageView
+ __OBJC_PROTOCOL_$_CLKFullColorImageView
+ __OBJC_PROTOCOL_$_CLKMonochromeComplicationView
+ __OBJC_PROTOCOL_$_CLKUIColoringView
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$__HKWorkoutObserverDelegate
+ ___60-[NLWorkoutComplicationDataSource _updateActiveWorkoutState]_block_invoke
+ ___60-[NLWorkoutComplicationDataSource _updateActiveWorkoutState]_block_invoke_2
+ ___60-[NLWorkoutComplicationDataSource didUpdateWorkoutSnapshot:]_block_invoke
+ ___61-[NLWorkoutComplicationDataSource _makeAnimatedImageProvider]_block_invoke
+ ___62-[NLWorkoutComplicationDataSource _templateForWorkout:family:]_block_invoke
+ ___73-[NLWorkoutComplicationDataSource initWithComplication:family:forDevice:]_block_invoke
+ ___NLWorkoutComplicationBundle_block_invoke
+ ___NLWorkoutKeyNonGradientTextColor_block_invoke
+ ___NLWorkoutNoNonGradientTextColor_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32w_e47_v24?0"_HKCurrentWorkoutSnapshot"8"NSError"16lw32l8
+ ___block_descriptor_40_e8_32w_e51_"UIView<CDComplicationImageView>"24?0{CGSize=dd}8lw32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_literal_global
+ ___os_log_helper_16_0_0
+ ___os_log_helper_16_2_1_8_64
+ ___os_log_helper_16_2_2_8_64_8_64
+ __block_literal_global.7
+ __block_literal_global.9
+ __os_log_fault_impl
+ _kFontSizeCircular
+ _kFontSizeCorner
+ _kFontSizeLarge
+ _kNLWorkoutImageViewKVOContext
+ _memcpy
+ _objc_msgSend$CGColor
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$_animationImages
+ _objc_msgSend$_applyAnimationForPauseState:animated:
+ _objc_msgSend$_filterStyle
+ _objc_msgSend$_hasActiveWorkout
+ _objc_msgSend$_hasPausedActiveWorkout
+ _objc_msgSend$_invalidate
+ _objc_msgSend$_makeAnimatedImageProvider
+ _objc_msgSend$_noActiveWorkoutImageForComplicationFamily:
+ _objc_msgSend$_noWorkoutsTemplate
+ _objc_msgSend$_signatureTemplateWithFamily:hasActiveWorkout:hasPausedActiveWorkout:
+ _objc_msgSend$_startObserving
+ _objc_msgSend$_stopObservingSynchronously:
+ _objc_msgSend$_systemImageNamed:withConfiguration:
+ _objc_msgSend$_templateForActiveWorkoutInSwitcher:
+ _objc_msgSend$_templateForWorkout:family:
+ _objc_msgSend$_unknownTemplateForFamily:
+ _objc_msgSend$_updateActiveWorkoutState
+ _objc_msgSend$_updateState
+ _objc_msgSend$_updateTint
+ _objc_msgSend$_updateUI
+ _objc_msgSend$_workoutTintColor
+ _objc_msgSend$_workoutWithActivityType:startDate:endDate:workoutEvents:workoutActivities:duration:totalActiveEnergyBurned:totalBasalEnergyBurned:totalDistance:totalSwimmingStrokeCount:totalFlightsClimbed:goalType:goal:device:metadata:
+ _objc_msgSend$activityType
+ _objc_msgSend$addAnimation:forKey:
+ _objc_msgSend$addObject:
+ _objc_msgSend$addObserver:forKeyPath:options:context:
+ _objc_msgSend$addSubview:
+ _objc_msgSend$animationWithKeyPath:
+ _objc_msgSend$array
+ _objc_msgSend$begin
+ _objc_msgSend$boolValue
+ _objc_msgSend$bounds
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$calendarWithIdentifier:
+ _objc_msgSend$commit
+ _objc_msgSend$configuration
+ _objc_msgSend$configurationWithFont:
+ _objc_msgSend$count
+ _objc_msgSend$currentWorkoutSnapshotWithCompletion:
+ _objc_msgSend$date
+ _objc_msgSend$dateByAddingTimeInterval:
+ _objc_msgSend$dateFromComponents:
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$delegate
+ _objc_msgSend$device
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$elapsedTimeAtDate:
+ _objc_msgSend$endDate
+ _objc_msgSend$entryWithDate:complicationTemplate:
+ _objc_msgSend$family
+ _objc_msgSend$filterProvider
+ _objc_msgSend$filtersForView:style:
+ _objc_msgSend$filtersForView:style:fraction:
+ _objc_msgSend$fiui_sharedHealthStoreForCarousel
+ _objc_msgSend$fiui_swimmingLocationType
+ _objc_msgSend$fullColorImageProviderWithImageViewClass:
+ _objc_msgSend$functionWithName:
+ _objc_msgSend$healthStore
+ _objc_msgSend$image
+ _objc_msgSend$imageNamed:inBundle:compatibleWithTraitCollection:
+ _objc_msgSend$imageProviderWithImageViewCreationHandler:
+ _objc_msgSend$imageProviderWithOnePieceImage:
+ _objc_msgSend$imageWithRenderingMode:
+ _objc_msgSend$initWithAnimationImages:
+ _objc_msgSend$initWithExtensionBundleIdentifier:containerBundleIdentifier:kind:intent:
+ _objc_msgSend$initWithFrame:
+ _objc_msgSend$initWithHealthStore:
+ _objc_msgSend$initWithImage:
+ _objc_msgSend$initWithUnitManager:
+ _objc_msgSend$internalState
+ _objc_msgSend$invalidateEntries
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isFirstPartyWorkout
+ _objc_msgSend$isLocked
+ _objc_msgSend$isPaused
+ _objc_msgSend$keyColors
+ _objc_msgSend$kilocalorieUnit
+ _objc_msgSend$largeModularEmptyTextProvider
+ _objc_msgSend$layer
+ _objc_msgSend$localizedKeyMetricStringForWorkout:unitStyle:
+ _objc_msgSend$localizedLowercaseString
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$metadata
+ _objc_msgSend$mileUnit
+ _objc_msgSend$nextDateAfterDate:matchingComponents:options:
+ _objc_msgSend$noActiveWorkoutImage
+ _objc_msgSend$noMetricColors
+ _objc_msgSend$noWorkoutImageForComplicationFamily:
+ _objc_msgSend$nonGradientTextColor
+ _objc_msgSend$now
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$quantityWithUnit:doubleValue:
+ _objc_msgSend$removeAllAnimations
+ _objc_msgSend$removeAnimationForKey:
+ _objc_msgSend$removeObserver:forKeyPath:
+ _objc_msgSend$sampleTemplate
+ _objc_msgSend$sessionState
+ _objc_msgSend$setActiveWorkoutSnapshot:
+ _objc_msgSend$setAnimationDuration:
+ _objc_msgSend$setAnimationImages:
+ _objc_msgSend$setAutoreverses:
+ _objc_msgSend$setCenter:
+ _objc_msgSend$setContentsMultiplyColor:
+ _objc_msgSend$setDay:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setDisableActions:
+ _objc_msgSend$setDuration:
+ _objc_msgSend$setFilters:
+ _objc_msgSend$setFrame:
+ _objc_msgSend$setHidden:
+ _objc_msgSend$setHour:
+ _objc_msgSend$setImage:
+ _objc_msgSend$setMetadata:
+ _objc_msgSend$setMinute:
+ _objc_msgSend$setMonth:
+ _objc_msgSend$setPaused:
+ _objc_msgSend$setRelativeToDate:
+ _objc_msgSend$setRepeatCount:
+ _objc_msgSend$setTimeTravelUpdateFrequency:
+ _objc_msgSend$setTimingFunction:
+ _objc_msgSend$setTintColor:
+ _objc_msgSend$setToValue:
+ _objc_msgSend$setUseLowercaseSmallCaps:
+ _objc_msgSend$setYear:
+ _objc_msgSend$size
+ _objc_msgSend$snapshotDate
+ _objc_msgSend$startAnimating
+ _objc_msgSend$stopAnimating
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringWithValidatedFormat:validFormatSpecifiers:error:
+ _objc_msgSend$systemFontOfSize:
+ _objc_msgSend$templateWithCircularTemplate:
+ _objc_msgSend$templateWithHeaderTextProvider:body1TextProvider:
+ _objc_msgSend$templateWithHeaderTextProvider:body1TextProvider:body2TextProvider:
+ _objc_msgSend$templateWithHeaderTextProvider:bodyTextProvider:
+ _objc_msgSend$templateWithImageProvider:
+ _objc_msgSend$templateWithTextProvider:imageProvider:
+ _objc_msgSend$textProviderWithDate:style:units:
+ _objc_msgSend$textProviderWithDate:units:
+ _objc_msgSend$textProviderWithFormat:
+ _objc_msgSend$textProviderWithText:
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$tintColor
+ _objc_msgSend$workoutActivityType
+ _objc_msgSend$workoutObserver
+ _objc_retainAutoreleasedReturnValue
+ _templateForWorkout:family:.formattingManager
+ _templateForWorkout:family:.onceToken
- __NTKGenerateSimulatedCrash
- _kHKHealthDaemonActiveWorkoutServersDidUpdateNotification
- _notify_register_dispatch
- _objc_claimAutoreleasedReturnValue
- _objc_release_x1
- _objc_release_x19
- _objc_release_x20
- _objc_release_x21
- _objc_release_x22
- _objc_release_x23
- _objc_release_x24
- _objc_release_x25
- _objc_release_x26
- _objc_release_x27
- _objc_release_x28
- _objc_release_x8
- _objc_release_x9
- _objc_retain_x1
- _objc_retain_x19
- _objc_retain_x2
- _objc_retain_x20
- _objc_retain_x21
- _objc_retain_x22
- _objc_retain_x4
- _objc_retain_x8
- radr://5614542
CStrings:
+ "NO"
+ "WorkoutWidget"
+ "Yes"
+ "[NLWorkoutComplicationDataSource] currentWorkoutSnapshot: %@"
+ "[NLWorkoutComplicationDataSource] getCurrentTimelineEntryWithHandler called with workout is active: %@."
+ "_HKWorkoutObserverDelegate"
+ "_workoutWithActivityType:startDate:endDate:workoutEvents:workoutActivities:duration:totalActiveEnergyBurned:totalBasalEnergyBurned:totalDistance:totalSwimmingStrokeCount:totalFlightsClimbed:goalType:goal:device:metadata:"
+ "didUpdateWorkoutSnapshot:"
+ "now"
+ "setDelegate:"
+ "snapshotDate"
+ "timeIntervalSinceDate:"
+ "v24@0:8@\"_HKCurrentWorkoutSnapshot\"16"
- "Most probaly fiui_sharedHealthStoreForCarousel returned a nil store"
- "WorkoutWidgetExtension"
- "v12@?0i8"
- "workoutWithActivityType:startDate:endDate:duration:totalEnergyBurned:totalDistance:metadata:"

```
