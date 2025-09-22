## FitnessApp

> `/System/Library/AccessibilityBundles/FitnessApp.axbundle/FitnessApp`

```diff

-1000.0.0.0.0
-  __TEXT.__text: 0xc31c
-  __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_stubs: 0x1860
-  __TEXT.__objc_methlist: 0x17b0
+1001.2.0.0.0
+  __TEXT.__text: 0xfbf0
+  __TEXT.__auth_stubs: 0x510
+  __TEXT.__objc_stubs: 0x1920
+  __TEXT.__objc_methlist: 0x1a00
   __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0x190
-  __TEXT.__objc_classname: 0x176d
-  __TEXT.__cstring: 0x268e
-  __TEXT.__objc_methname: 0x1838
-  __TEXT.__objc_methtype: 0x186
+  __TEXT.__gcc_except_tab: 0x270
+  __TEXT.__objc_classname: 0x1abf
+  __TEXT.__cstring: 0x2dd8
+  __TEXT.__objc_methname: 0x1bd1
+  __TEXT.__objc_methtype: 0x200
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x570
-  __DATA_CONST.__auth_got: 0x280
+  __TEXT.__unwind_info: 0x628
+  __DATA_CONST.__auth_got: 0x298
   __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x450
-  __DATA_CONST.__cfstring: 0x3060
-  __DATA_CONST.__objc_classlist: 0x430
+  __DATA_CONST.__const: 0x4e0
+  __DATA_CONST.__cfstring: 0x3560
+  __DATA_CONST.__objc_classlist: 0x4a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x188
-  __DATA.__objc_const: 0x4be8
-  __DATA.__objc_selrefs: 0x768
+  __DATA_CONST.__objc_superrefs: 0x1c0
+  __DATA.__objc_const: 0x53c8
+  __DATA.__objc_selrefs: 0x7e0
   __DATA.__objc_ivar: 0x8
-  __DATA.__objc_data: 0x29e0
+  __DATA.__objc_data: 0x2e40
   __DATA.__bss: 0x69
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AA780468-27BD-31C7-97FE-29301A539D18
-  Functions: 443
-  Symbols:   1507
-  CStrings:  1197
+  UUID: 555F7459-2D1B-34DC-8741-FA5412A8A5A1
+  Functions: 495
+  Symbols:   1647
+  CStrings:  1315
 
Symbols:
+ +[CHMindfulnessSessionListTableViewCellAccessibility _accessibilityPerformValidations:]
+ +[CHMindfulnessSessionListTableViewCellAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[CHMindfulnessSessionListTableViewCellAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[CHWorkoutDetailFourColumnDownhillRunTableViewCellAccessibility _accessibilityPerformValidations:]
+ +[CHWorkoutDetailFourColumnDownhillRunTableViewCellAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[CHWorkoutDetailFourColumnDownhillRunTableViewCellAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[CHWorkoutDetailFourColumnIntervalTableViewCellAccessibility _accessibilityPerformValidations:]
+ +[CHWorkoutDetailFourColumnIntervalTableViewCellAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[CHWorkoutDetailFourColumnIntervalTableViewCellAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[CHWorkoutDetailFourColumnSegmentTableViewCellAccessibility _accessibilityPerformValidations:]
+ +[CHWorkoutDetailFourColumnSegmentTableViewCellAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[CHWorkoutDetailFourColumnSegmentTableViewCellAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[CHWorkoutDetailFourColumnSwimmingSetTableViewCellAccessibility _accessibilityPerformValidations:]
+ +[CHWorkoutDetailFourColumnSwimmingSetTableViewCellAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[CHWorkoutDetailFourColumnSwimmingSetTableViewCellAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[CHWorkoutDetailFourColumnTrackLapTableViewCellAccessibility _accessibilityPerformValidations:]
+ +[CHWorkoutDetailFourColumnTrackLapTableViewCellAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[CHWorkoutDetailFourColumnTrackLapTableViewCellAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[CHWorkoutsListTableViewCellAccessibility _accessibilityPerformValidations:]
+ +[CHWorkoutsListTableViewCellAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[CHWorkoutsListTableViewCellAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[ActivityStandChartViewAccessibility reloadDataWithAnimated:]
+ -[CHASActivitySetupViewControllerAccessibility _accessibilityLoadAccessibilityInformation]
+ -[CHMindfulnessSessionListTableViewCellAccessibility _accessibilityLoadAccessibilityInformation]
+ -[CHMindfulnessSessionListTableViewCellAccessibility _isDateInLastWeek:]
+ -[CHMindfulnessSessionListTableViewCellAccessibility accessibilityPath]
+ -[CHMindfulnessSessionListTableViewCellAccessibility isAccessibilityElement]
+ -[CHWorkoutDetailFourColumnDownhillRunTableViewCellAccessibility configureWithDownhillRun:downhillRunIndex:activityType:isLastCell:formattingManager:]
+ -[CHWorkoutDetailFourColumnDownhillRunTableViewCellAccessibility configureWithDownhillRunsStats:activityType:formattingManager:]
+ -[CHWorkoutDetailFourColumnIntervalTableViewCellAccessibility configureWithInterval:index:workout:activityType:activityMoveMode:isLastCell:formattingManager:]
+ -[CHWorkoutDetailFourColumnSegmentTableViewCellAccessibility configureWithSegment:segmentIndex:workout:trackDistanceUnit:activityType:activityMoveMode:isLastCell:formattingManager:]
+ -[CHWorkoutDetailFourColumnSplitTableViewCellAccessibility configureWithSwimmingSplit:splitIndex:isLastCell:formattingManager:]
+ -[CHWorkoutDetailFourColumnSwimmingSetTableViewCellAccessibility configureWithSwimmingSet:index:isLastCell:formattingManager:]
+ -[CHWorkoutDetailFourColumnTrackLapTableViewCellAccessibility configureWithTrackLap:lapIndex:workout:distanceUnit:activityType:activityMoveMode:isLastCell:formattingManager:]
+ -[CHWorkoutFormattingManagerAccessibility _fetchIconForConnectedGymWorkout:context:completion:]
+ -[CHWorkoutFormattingManagerAccessibility _fetchIconForFirstPartyWorkout:context:completion:]
+ -[CHWorkoutFormattingManagerAccessibility _fetchIconForHiddenAppWorkout:context:completion:]
+ -[CHWorkoutFormattingManagerAccessibility _fetchIconForThirdPartyWorkout:context:completion:]
+ -[CHWorkoutsListTableViewCellAccessibility accessibilityLabel]
+ -[CHWorkoutsListTableViewCellAccessibility accessibilityPath]
+ -[CHWorkoutsListTableViewCellAccessibility isAccessibilityElement]
+ _AXAppNameForBundleId
+ _OBJC_CLASS_$_CHMindfulnessSessionListTableViewCellAccessibility
+ _OBJC_CLASS_$_CHWorkoutDetailFourColumnDownhillRunTableViewCellAccessibility
+ _OBJC_CLASS_$_CHWorkoutDetailFourColumnIntervalTableViewCellAccessibility
+ _OBJC_CLASS_$_CHWorkoutDetailFourColumnSegmentTableViewCellAccessibility
+ _OBJC_CLASS_$_CHWorkoutDetailFourColumnSwimmingSetTableViewCellAccessibility
+ _OBJC_CLASS_$_CHWorkoutDetailFourColumnTrackLapTableViewCellAccessibility
+ _OBJC_CLASS_$_CHWorkoutsListTableViewCellAccessibility
+ _OBJC_CLASS_$_FIUIFormattingManager
+ _OBJC_CLASS_$___CHMindfulnessSessionListTableViewCellAccessibility_super
+ _OBJC_CLASS_$___CHWorkoutDetailFourColumnDownhillRunTableViewCellAccessibility_super
+ _OBJC_CLASS_$___CHWorkoutDetailFourColumnIntervalTableViewCellAccessibility_super
+ _OBJC_CLASS_$___CHWorkoutDetailFourColumnSegmentTableViewCellAccessibility_super
+ _OBJC_CLASS_$___CHWorkoutDetailFourColumnSwimmingSetTableViewCellAccessibility_super
+ _OBJC_CLASS_$___CHWorkoutDetailFourColumnTrackLapTableViewCellAccessibility_super
+ _OBJC_CLASS_$___CHWorkoutsListTableViewCellAccessibility_super
+ _OBJC_METACLASS_$_CHMindfulnessSessionListTableViewCellAccessibility
+ _OBJC_METACLASS_$_CHWorkoutDetailFourColumnDownhillRunTableViewCellAccessibility
+ _OBJC_METACLASS_$_CHWorkoutDetailFourColumnIntervalTableViewCellAccessibility
+ _OBJC_METACLASS_$_CHWorkoutDetailFourColumnSegmentTableViewCellAccessibility
+ _OBJC_METACLASS_$_CHWorkoutDetailFourColumnSwimmingSetTableViewCellAccessibility
+ _OBJC_METACLASS_$_CHWorkoutDetailFourColumnTrackLapTableViewCellAccessibility
+ _OBJC_METACLASS_$_CHWorkoutsListTableViewCellAccessibility
+ _OBJC_METACLASS_$___CHMindfulnessSessionListTableViewCellAccessibility_super
+ _OBJC_METACLASS_$___CHWorkoutDetailFourColumnDownhillRunTableViewCellAccessibility_super
+ _OBJC_METACLASS_$___CHWorkoutDetailFourColumnIntervalTableViewCellAccessibility_super
+ _OBJC_METACLASS_$___CHWorkoutDetailFourColumnSegmentTableViewCellAccessibility_super
+ _OBJC_METACLASS_$___CHWorkoutDetailFourColumnSwimmingSetTableViewCellAccessibility_super
+ _OBJC_METACLASS_$___CHWorkoutDetailFourColumnTrackLapTableViewCellAccessibility_super
+ _OBJC_METACLASS_$___CHWorkoutsListTableViewCellAccessibility_super
+ __OBJC_$_CLASS_METHODS_CHMindfulnessSessionListTableViewCellAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_CHWorkoutDetailFourColumnDownhillRunTableViewCellAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_CHWorkoutDetailFourColumnIntervalTableViewCellAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_CHWorkoutDetailFourColumnSegmentTableViewCellAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_CHWorkoutDetailFourColumnSwimmingSetTableViewCellAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_CHWorkoutDetailFourColumnTrackLapTableViewCellAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_CHWorkoutsListTableViewCellAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_CHMindfulnessSessionListTableViewCellAccessibility
+ __OBJC_$_INSTANCE_METHODS_CHWorkoutDetailFourColumnDownhillRunTableViewCellAccessibility
+ __OBJC_$_INSTANCE_METHODS_CHWorkoutDetailFourColumnIntervalTableViewCellAccessibility
+ __OBJC_$_INSTANCE_METHODS_CHWorkoutDetailFourColumnSegmentTableViewCellAccessibility
+ __OBJC_$_INSTANCE_METHODS_CHWorkoutDetailFourColumnSwimmingSetTableViewCellAccessibility
+ __OBJC_$_INSTANCE_METHODS_CHWorkoutDetailFourColumnTrackLapTableViewCellAccessibility
+ __OBJC_$_INSTANCE_METHODS_CHWorkoutsListTableViewCellAccessibility
+ __OBJC_CLASS_RO_$_CHMindfulnessSessionListTableViewCellAccessibility
+ __OBJC_CLASS_RO_$_CHWorkoutDetailFourColumnDownhillRunTableViewCellAccessibility
+ __OBJC_CLASS_RO_$_CHWorkoutDetailFourColumnIntervalTableViewCellAccessibility
+ __OBJC_CLASS_RO_$_CHWorkoutDetailFourColumnSegmentTableViewCellAccessibility
+ __OBJC_CLASS_RO_$_CHWorkoutDetailFourColumnSwimmingSetTableViewCellAccessibility
+ __OBJC_CLASS_RO_$_CHWorkoutDetailFourColumnTrackLapTableViewCellAccessibility
+ __OBJC_CLASS_RO_$_CHWorkoutsListTableViewCellAccessibility
+ __OBJC_CLASS_RO_$___CHMindfulnessSessionListTableViewCellAccessibility_super
+ __OBJC_CLASS_RO_$___CHWorkoutDetailFourColumnDownhillRunTableViewCellAccessibility_super
+ __OBJC_CLASS_RO_$___CHWorkoutDetailFourColumnIntervalTableViewCellAccessibility_super
+ __OBJC_CLASS_RO_$___CHWorkoutDetailFourColumnSegmentTableViewCellAccessibility_super
+ __OBJC_CLASS_RO_$___CHWorkoutDetailFourColumnSwimmingSetTableViewCellAccessibility_super
+ __OBJC_CLASS_RO_$___CHWorkoutDetailFourColumnTrackLapTableViewCellAccessibility_super
+ __OBJC_CLASS_RO_$___CHWorkoutsListTableViewCellAccessibility_super
+ __OBJC_METACLASS_RO_$_CHMindfulnessSessionListTableViewCellAccessibility
+ __OBJC_METACLASS_RO_$_CHWorkoutDetailFourColumnDownhillRunTableViewCellAccessibility
+ __OBJC_METACLASS_RO_$_CHWorkoutDetailFourColumnIntervalTableViewCellAccessibility
+ __OBJC_METACLASS_RO_$_CHWorkoutDetailFourColumnSegmentTableViewCellAccessibility
+ __OBJC_METACLASS_RO_$_CHWorkoutDetailFourColumnSwimmingSetTableViewCellAccessibility
+ __OBJC_METACLASS_RO_$_CHWorkoutDetailFourColumnTrackLapTableViewCellAccessibility
+ __OBJC_METACLASS_RO_$_CHWorkoutsListTableViewCellAccessibility
+ __OBJC_METACLASS_RO_$___CHMindfulnessSessionListTableViewCellAccessibility_super
+ __OBJC_METACLASS_RO_$___CHWorkoutDetailFourColumnDownhillRunTableViewCellAccessibility_super
+ __OBJC_METACLASS_RO_$___CHWorkoutDetailFourColumnIntervalTableViewCellAccessibility_super
+ __OBJC_METACLASS_RO_$___CHWorkoutDetailFourColumnSegmentTableViewCellAccessibility_super
+ __OBJC_METACLASS_RO_$___CHWorkoutDetailFourColumnSwimmingSetTableViewCellAccessibility_super
+ __OBJC_METACLASS_RO_$___CHWorkoutDetailFourColumnTrackLapTableViewCellAccessibility_super
+ __OBJC_METACLASS_RO_$___CHWorkoutsListTableViewCellAccessibility_super
+ ___158-[CHWorkoutDetailFourColumnIntervalTableViewCellAccessibility configureWithInterval:index:workout:activityType:activityMoveMode:isLastCell:formattingManager:]_block_invoke
+ ___158-[CHWorkoutDetailFourColumnIntervalTableViewCellAccessibility configureWithInterval:index:workout:activityType:activityMoveMode:isLastCell:formattingManager:]_block_invoke_2
+ ___174-[CHWorkoutDetailFourColumnTrackLapTableViewCellAccessibility configureWithTrackLap:lapIndex:workout:distanceUnit:activityType:activityMoveMode:isLastCell:formattingManager:]_block_invoke
+ ___181-[CHWorkoutDetailFourColumnSegmentTableViewCellAccessibility configureWithSegment:segmentIndex:workout:trackDistanceUnit:activityType:activityMoveMode:isLastCell:formattingManager:]_block_invoke
+ ___181-[CHWorkoutDetailFourColumnSegmentTableViewCellAccessibility configureWithSegment:segmentIndex:workout:trackDistanceUnit:activityType:activityMoveMode:isLastCell:formattingManager:]_block_invoke_2
+ ___181-[CHWorkoutDetailFourColumnSegmentTableViewCellAccessibility configureWithSegment:segmentIndex:workout:trackDistanceUnit:activityType:activityMoveMode:isLastCell:formattingManager:]_block_invoke_3
+ ___82-[WorkoutsListContentViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke
+ ___86-[CHWorkoutCellImageLabelViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2
+ ___90-[CHASActivitySetupViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke
+ ___92-[CHWorkoutFormattingManagerAccessibility _fetchIconForHiddenAppWorkout:context:completion:]_block_invoke
+ ___93-[CHWorkoutFormattingManagerAccessibility _fetchIconForFirstPartyWorkout:context:completion:]_block_invoke
+ ___93-[CHWorkoutFormattingManagerAccessibility _fetchIconForThirdPartyWorkout:context:completion:]_block_invoke
+ ___95-[CHWorkoutFormattingManagerAccessibility _fetchIconForConnectedGymWorkout:context:completion:]_block_invoke
+ ___96-[CHMindfulnessSessionListTableViewCellAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke
+ ___block_descriptor_40_e8_32bs_e17_v16?0"UIImage"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"UIImage"8ls32l8s40l8
+ ___block_descriptor_48_e8_32w40w_e15_"NSString"8?0lw32l8w40l8
+ __block_literal_global.554
+ __block_literal_global.592
+ __block_literal_global.609
+ __block_literal_global.633
+ _accessibilityDescriptionForGoalType
+ _objc_msgSend$_accessibilitySetSortPriority:
+ _objc_msgSend$_goalType
+ _objc_msgSend$accessibilityPath
+ _objc_msgSend$device
+ _objc_msgSend$localizedLongActiveEnergyUnitString
+ _objc_msgSend$supportsDistanceForWorkout:workoutActivity:
+ _objc_msgSend$supportsPaceForWorkout:workoutActivity:
+ _objc_retain_x27
+ _objc_retain_x28
+ _objc_retain_x4
- -[CHASActivitySetupViewControllerAccessibility _updateAdvanceViewButton:]
- -[WorkoutsListContentViewAccessibility accessibilityLabel]
- -[WorkoutsListContentViewAccessibility configureWithCurrentWorkout]
- -[WorkoutsListContentViewAccessibility isAccessibilityElement]
- _OBJC_CLASS_$_UIImageView
- __block_literal_global.533
- __block_literal_global.571
- __block_literal_global.588
- __block_literal_global.600
- _objc_msgSend$safeUnsignedIntegerForKey:
- _objc_retain_x23
CStrings:
+ "@?"
+ "CHMindfulnessSessionListTableViewCell"
+ "CHMindfulnessSessionListTableViewCellAccessibility"
+ "CHWorkoutDetailFourColumnDownhillRunTableViewCell"
+ "CHWorkoutDetailFourColumnDownhillRunTableViewCellAccessibility"
+ "CHWorkoutDetailFourColumnIntervalTableViewCell"
+ "CHWorkoutDetailFourColumnIntervalTableViewCellAccessibility"
+ "CHWorkoutDetailFourColumnSegmentTableViewCell"
+ "CHWorkoutDetailFourColumnSegmentTableViewCellAccessibility"
+ "CHWorkoutDetailFourColumnSwimmingSetTableViewCell"
+ "CHWorkoutDetailFourColumnSwimmingSetTableViewCellAccessibility"
+ "CHWorkoutDetailFourColumnTrackLapTableViewCell"
+ "CHWorkoutDetailFourColumnTrackLapTableViewCellAccessibility"
+ "CHWorkoutsListTableViewCell"
+ "CHWorkoutsListTableViewCellAccessibility"
+ "Date"
+ "FitnessUI.MindfulnessSessionViewModel"
+ "Optional<MindfulnessSessionViewModel>"
+ "WorkoutsListContentView"
+ "__CHMindfulnessSessionListTableViewCellAccessibility_super"
+ "__CHWorkoutDetailFourColumnDownhillRunTableViewCellAccessibility_super"
+ "__CHWorkoutDetailFourColumnIntervalTableViewCellAccessibility_super"
+ "__CHWorkoutDetailFourColumnSegmentTableViewCellAccessibility_super"
+ "__CHWorkoutDetailFourColumnSwimmingSetTableViewCellAccessibility_super"
+ "__CHWorkoutDetailFourColumnTrackLapTableViewCellAccessibility_super"
+ "__CHWorkoutsListTableViewCellAccessibility_super"
+ "_accessibilitySetSortPriority:"
+ "_advancedButton"
+ "_fetchIconForConnectedGymWorkout:context:completion:"
+ "_fetchIconForFirstPartyWorkout:context:completion:"
+ "_fetchIconForHiddenAppWorkout:context:completion:"
+ "_fetchIconForThirdPartyWorkout:context:completion:"
+ "_goalType"
+ "com.apple.Health"
+ "configureWithDownhillRun:downhillRunIndex:activityType:isLastCell:formattingManager:"
+ "configureWithDownhillRunsStats:activityType:formattingManager:"
+ "configureWithInterval:index:workout:activityType:activityMoveMode:isLastCell:formattingManager:"
+ "configureWithSegment:segmentIndex:workout:trackDistanceUnit:activityType:activityMoveMode:isLastCell:formattingManager:"
+ "configureWithSwimmingSet:index:isLastCell:formattingManager:"
+ "configureWithSwimmingSplit:splitIndex:isLastCell:formattingManager:"
+ "configureWithTrackLap:lapIndex:workout:distanceUnit:activityType:activityMoveMode:isLastCell:formattingManager:"
+ "device"
+ "distance.goal"
+ "endDate"
+ "energy.goal"
+ "energy.value"
+ "fitnessUIFormattingManager"
+ "fiui_completionFactor"
+ "insetContentView"
+ "interval.number"
+ "labelStackView"
+ "lap.number"
+ "localizedLongActiveEnergyUnitString"
+ "mindfulnessSessionViewModel"
+ "open.goal"
+ "reloadDataWithAnimated:"
+ "run.number"
+ "segment.number"
+ "set.number"
+ "shouldUseCircularGradientImage"
+ "stroke.value"
+ "supportsDistanceForWorkout:workoutActivity:"
+ "supportsPaceForWorkout:workoutActivity:"
+ "time.goal"
+ "v16@?0@\"UIImage\"8"
+ "v40@0:8@16@24@?32"
+ "v44@0:8@16q24B32@36"
+ "v52@0:8@16q24@32B40@44"
+ "v68@0:8@16q24@32@40q48B56@60"
+ "v76@0:8@16q24@32Q40@48q56B64@68"
+ "vertical.value"
+ "workoutContentView"
- "FIUIWorkoutActivityType"
- "FIWorkoutActivityType"
- "FitnessApp.WorkoutCellImageLabelView"
- "HKSource"
- "UIImageView"
- "_isAppleWatch"
- "_updateAdvanceViewButton:"
- "award.earned"
- "configureWithCurrentWorkout"
- "identifier"
- "safeUnsignedIntegerForKey:"
- "workoutCellImageLabelView"
- "workoutIconView"

```
