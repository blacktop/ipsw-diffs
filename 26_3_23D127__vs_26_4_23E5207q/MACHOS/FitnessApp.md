## FitnessApp

> `/System/Library/AccessibilityBundles/FitnessApp.axbundle/FitnessApp`

```diff

-1001.4.8.0.0
-  __TEXT.__text: 0xfb6c
-  __TEXT.__auth_stubs: 0x510
+1001.12.0.0.0
+  __TEXT.__text: 0x106e8
+  __TEXT.__auth_stubs: 0x4d0
   __TEXT.__objc_stubs: 0x1920
   __TEXT.__objc_methlist: 0x19b8
   __TEXT.__const: 0x58

   __TEXT.__objc_methtype: 0x200
   __TEXT.__ustring: 0xa
   __TEXT.__unwind_info: 0x618
-  __DATA_CONST.__auth_got: 0x298
+  __DATA_CONST.__auth_got: 0x278
   __DATA_CONST.__got: 0x180
   __DATA_CONST.__const: 0x4e0
   __DATA_CONST.__cfstring: 0x3560

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DBD26A5F-1F44-30E9-AAF8-2CFE9C26B3C4
+  UUID: BE38F22C-A67A-386D-9BF7-44433BB04364
   Functions: 491
-  Symbols:   1633
+  Symbols:   1629
   CStrings:  1313
 
Symbols:
+ _objc_retain_x23
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
Functions:
~ +[CHWorkoutDetailFourColumnSplitTableViewCellAccessibility _accessibilityPerformValidations:] : 432 -> 440
~ -[CHWorkoutDetailFourColumnSplitTableViewCellAccessibility configureWithWorkout:workoutActivity:unit:split:splitIndex:splitDistance:includeHeartRate:isLastCell:dataCalculator:formattingManager:] : 1488 -> 1552
~ ___194-[CHWorkoutDetailFourColumnSplitTableViewCellAccessibility configureWithWorkout:workoutActivity:unit:split:splitIndex:splitDistance:includeHeartRate:isLastCell:dataCalculator:formattingManager:]_block_invoke_2 : 220 -> 240
~ -[CHWorkoutDetailFourColumnSplitTableViewCellAccessibility configureWithSwimmingSplit:splitIndex:isLastCell:formattingManager:] : 692 -> 748
~ -[AddToYourRingTableViewCellAccessibility accessibilityElements] : 300 -> 320
~ +[AX_FitnessNSStringAccessibility attrStringWithValue:unit:] : 256 -> 268
~ +[MonthDayCellLayerAccessibility _accessibilityPerformValidations:] : 300 -> 312
~ -[MonthDayCellLayerAccessibility accessibilityLabel] : 320 -> 344
~ -[MonthDayCellLayerAccessibility accessibilityValue] : 372 -> 408
~ -[MonthDayCellLayerAccessibility accessibilityFrame] : 172 -> 176
~ +[ActivityMoveAndExerciseChartViewAccessibility _accessibilityPerformValidations:] : 192 -> 204
~ -[ActivityMoveAndExerciseChartViewAccessibility accessibilityElements] : 1016 -> 1104
~ +[ActivitySharingTabViewHostingControllerAccessibility _accessibilityPerformValidations:] : 196 -> 204
~ -[ActivitySharingTabViewHostingControllerAccessibility viewIsAppearing:] : 204 -> 220
~ +[CHAchievementDetailViewControllerAccessibility _accessibilityPerformValidations:] : 252 -> 260
~ -[CHAchievementDetailViewControllerAccessibility _axAnnotateAchievementView] : 740 -> 780
~ ___76-[CHAchievementDetailViewControllerAccessibility _axAnnotateAchievementView]_block_invoke : 116 -> 124
~ -[ActivityTileSectionHeaderAccessibility _accessibilityLoadAccessibilityInformation] : 124 -> 128
~ +[AppStoreAppRecommendationCollectionViewCellAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[AppStoreAppRecommendationCollectionViewCellAccessibility accessibilityLabel] : 148 -> 160
~ +[FitnessUITransitionViewAccessibility _accessibilityPerformValidations:] : 84 -> 92
~ -[FitnessUITransitionViewAccessibility accessibilityViewIsModal] : 180 -> 188
~ ___64-[FitnessUITransitionViewAccessibility accessibilityViewIsModal]_block_invoke : 152 -> 164
~ -[CHAchievementCollectionViewCellAccessibility accessibilityLabel] : 84 -> 92
~ +[CHWorkoutDetailFourColumnIntervalTableViewCellAccessibility _accessibilityPerformValidations:] : 372 -> 380
~ -[CHWorkoutDetailFourColumnIntervalTableViewCellAccessibility configureWithInterval:index:workout:activityType:activityMoveMode:isLastCell:formattingManager:] : 1680 -> 1760
~ +[_CHWorkoutSummaryTabbedLabelContainerAccessibility _accessibilityPerformValidations:] : 148 -> 156
~ -[_CHWorkoutSummaryTabbedLabelContainerAccessibility accessibilityLabel] : 624 -> 664
~ +[TrendDetailChartViewAccessibility _accessibilityPerformValidations:] : 292 -> 300
~ -[TrendDetailChartViewAccessibility accessibilityElements] : 1500 -> 1548
~ ___58-[TrendDetailChartViewAccessibility accessibilityElements]_block_invoke : 80 -> 84
~ ___58-[TrendDetailChartViewAccessibility accessibilityElements]_block_invoke_2 : 80 -> 84
~ +[CHWorkoutFormattingManagerAccessibility _accessibilityPerformValidations:] : 332 -> 340
~ -[CHWorkoutFormattingManagerAccessibility formattedDurationForWorkout:workoutActivity:context:] : 416 -> 424
~ -[CHWorkoutFormattingManagerAccessibility _fetchIconForConnectedGymWorkout:context:completion:] : 224 -> 216
~ ___95-[CHWorkoutFormattingManagerAccessibility _fetchIconForConnectedGymWorkout:context:completion:]_block_invoke : 148 -> 160
~ ___92-[CHWorkoutFormattingManagerAccessibility _fetchIconForHiddenAppWorkout:context:completion:]_block_invoke : 128 -> 136
~ -[CHWorkoutFormattingManagerAccessibility _fetchIconForFirstPartyWorkout:context:completion:] : 224 -> 216
~ ___93-[CHWorkoutFormattingManagerAccessibility _fetchIconForFirstPartyWorkout:context:completion:]_block_invoke : 252 -> 264
~ -[CHWorkoutFormattingManagerAccessibility _fetchIconForThirdPartyWorkout:context:completion:] : 224 -> 216
~ ___93-[CHWorkoutFormattingManagerAccessibility _fetchIconForThirdPartyWorkout:context:completion:]_block_invoke : 164 -> 180
~ +[CHFriendListViewControllerAccessibility _accessibilityPerformValidations:] : 128 -> 136
~ -[CHFriendListViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 344 -> 352
~ ___85-[CHFriendListViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 76 -> 80
~ +[ActivityStandChartViewAccessibility _accessibilityPerformValidations:] : 140 -> 148
~ -[ActivityStandChartViewAccessibility accessibilityElements] : 816 -> 868
~ +[CHFriendDetailGoalCellAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[CHFriendDetailGoalCellAccessibility accessibilityLabel] : 84 -> 92
~ -[CHFriendDetailGoalCellAccessibility accessibilityValue] : 84 -> 92
~ +[CHWorkoutDetailHeartRateChartViewAccessibility _accessibilityPerformValidations:] : 268 -> 276
~ -[CHWorkoutDetailHeartRateChartViewAccessibility accessibilityElements] : 140 -> 152
~ -[CHWorkoutDetailHeartRateChartViewAccessibility _accessibilityQuantityForSliceAtIndex:] : 912 -> 976
~ -[CHWorkoutDetailHeartRateChartViewAccessibility _accessibilityTimeIntervalPerSlice] : 84 -> 88
~ -[CHWorkoutDetailHeartRateChartViewAccessibility _accessibilityHoursPerSlice] : 96 -> 100
~ -[CHWorkoutDetailHeartRateChartViewAccessibility _axDateInterval] : 160 -> 168
~ -[CHWorkoutDetailHeartRateChartViewAccessibility _decimalForDate:] : 180 -> 188
~ +[CHFriendDetailCollectionViewControllerAccessibility _accessibilityPerformValidations:] : 188 -> 196
~ -[CHFriendDetailCollectionViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 492 -> 512
~ +[CHWorkoutCellImageLabelViewAccessibility _accessibilityPerformValidations:] : 184 -> 192
~ -[CHWorkoutCellImageLabelViewAccessibility _accessibilityLoadAccessibilityInformation] : 504 -> 520
~ ___86-[CHWorkoutCellImageLabelViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 148 -> 160
~ ___86-[CHWorkoutCellImageLabelViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 148 -> 156
~ +[WeekPaletteTappableDayAccessibility _accessibilityPerformValidations:] : 116 -> 124
~ -[WeekPaletteTappableDayAccessibility accessibilityTraits] : 152 -> 156
~ +[CHAchievementsCellContentViewAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[CHAchievementsCellContentViewAccessibility accessibilityLabel] : 324 -> 356
~ -[CHAchievementsCellContentViewAccessibility accessibilityValue] : 188 -> 208
~ +[DayViewMoveAndExerciseChartTableViewCellAccessibility _accessibilityPerformValidations:] : 172 -> 184
~ -[DayViewMoveAndExerciseChartTableViewCellAccessibility accessibilityElements] : 324 -> 352
~ -[TrophyCaseSectionCellAccessibility _accessibilityLoadAccessibilityInformation] : 252 -> 256
~ ___80-[TrophyCaseSectionCellAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 76 -> 80
~ -[TrophyCaseSectionCellAccessibility _axLabelForAchievementLabel] : 264 -> 292
~ +[CHWorkoutDetailSummaryTableViewCellAccessibility _accessibilityPerformValidations:] : 200 -> 208
~ -[CHWorkoutDetailSummaryTableViewCellAccessibility accessibilityTraits] : 420 -> 428
~ -[_FitnessMonthTitleLabelAccessibility accessibilityLabel] : 264 -> 288
~ -[TrophyCaseSectionHeaderViewAccessibility _accessibilityLoadAccessibilityInformation] : 112 -> 116
~ +[TrophyCaseAwardDetailBadgeCellAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[TrophyCaseAwardDetailBadgeCellAccessibility _accessibilityLoadAccessibilityInformation] : 308 -> 328
~ +[CHASActivitySetupGoalViewAccessibility _accessibilityPerformValidations:] : 252 -> 260
~ -[CHASActivitySetupGoalViewAccessibility accessibilityValue] : 376 -> 408
~ -[CHASActivitySetupGoalViewAccessibility _accessibilityPerformButtonActionForButton:] : 304 -> 316
~ +[CHWorkoutDetailPaceTableViewCellAccessibility _accessibilityPerformValidations:] : 168 -> 176
~ -[CHWorkoutDetailPaceTableViewCellAccessibility _accessibilityLoadAccessibilityInformation] : 220 -> 240
~ +[CHWorkoutDetailFourColumnSegmentTableViewCellAccessibility _accessibilityPerformValidations:] : 416 -> 424
~ -[CHWorkoutDetailFourColumnSegmentTableViewCellAccessibility configureWithSegment:segmentIndex:workout:trackDistanceUnit:activityType:activityMoveMode:isLastCell:formattingManager:] : 1864 -> 1928
~ +[CHMindfulnessSessionListTableViewCellAccessibility _accessibilityPerformValidations:] : 176 -> 184
~ -[CHMindfulnessSessionListTableViewCellAccessibility _accessibilityLoadAccessibilityInformation] : 384 -> 392
~ ___96-[CHMindfulnessSessionListTableViewCellAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 300 -> 320
~ -[CHMindfulnessSessionListTableViewCellAccessibility accessibilityPath] : 156 -> 172
~ -[CHMindfulnessSessionListTableViewCellAccessibility _isDateInLastWeek:] : 220 -> 244
~ +[CHASActivitySetupViewControllerAccessibility _accessibilityPerformValidations:] : 364 -> 372
~ -[CHASActivitySetupViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 252 -> 256
~ ___90-[CHASActivitySetupViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 132 -> 140
~ -[CHASActivitySetupViewControllerAccessibility _accessibilityUpdateCurrentPresentedView] : 224 -> 240
~ +[TrendListMetricViewAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[TrendListMetricViewAccessibility accessibilityLabel] : 204 -> 224
~ +[PaletteViewControllerAccessibility _accessibilityPerformValidations:] : 328 -> 336
~ -[PaletteViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 1324 -> 1396
~ ___80-[PaletteViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 88 -> 92
~ -[AXGroupedTitleValueView initWithAccessibilityContainer:titleView:valueView:] : 208 -> 204
~ -[AXGroupedTitleValueView isAccessibilityElement] : 128 -> 136
~ ___46+[AXFitnessGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___46+[AXFitnessGlue accessibilityInitializeBundle]_block_invoke_2 : 164 -> 168
~ ___46+[AXFitnessGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ ___46+[AXFitnessGlue accessibilityInitializeBundle]_block_invoke_4 : 1460 -> 1468
~ _CHCacheIndexForDate : 108 -> 112
~ ___CHCacheIndexForDate_block_invoke : 76 -> 80
~ -[NSObject(AXFitnessPriv) _fitnessUIAccessibilityDescriptionForPercentages:exercisingPercentage:standingPercentage:arePercentagesCapped:] : 268 -> 264
~ ___137-[NSObject(AXFitnessPriv) _fitnessUIAccessibilityDescriptionForPercentages:exercisingPercentage:standingPercentage:arePercentagesCapped:]_block_invoke : 88 -> 92
~ _accessibilityHKUnitForTrendType : 408 -> 456
~ ___accessibilityFitnessStringForDate_block_invoke : 136 -> 144
~ _accessibilityLocalizedString : 160 -> 168
~ _accessibilityDescriptionForPercentages : 472 -> 524
~ _accessibilityLocalizedStringForAchievement : 144 -> 148
~ ___accessibilityLocalizedStringForAchievement_block_invoke : 112 -> 116
~ _accessibilityAttributedStringForPaceContainingString : 696 -> 728
~ ___accessibilityAttributedStringForPaceContainingString_block_invoke : 80 -> 84
~ _accessibilityDescriptionForGoalType : 80 -> 84
~ __userIsWheelchairUserWithVoiceOverOn : 336 -> 340
~ ____userIsWheelchairUserWithVoiceOverOn_block_invoke : 112 -> 116
~ -[CHFriendDetailActionCellAccessibility accessibilityLabel] : 84 -> 92
~ +[CHWorkoutsListTableViewCellAccessibility _accessibilityPerformValidations:] : 108 -> 116
~ -[CHWorkoutsListTableViewCellAccessibility accessibilityPath] : 180 -> 200
~ -[WeekViewAccessibility accessibilityElements] : 288 -> 296
~ +[CHFriendListCompetitionTableViewCellAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[WorkoutAppRecommendationCollectionViewCellAccessibility accessibilityLabel] : 84 -> 92
~ +[CHListTableHeaderViewAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[CHListTableHeaderViewAccessibility accessibilityLabel] : 188 -> 208
~ +[TrendDetailDailyAverageViewAccessibility _accessibilityPerformValidations:] : 292 -> 300
~ -[TrendDetailDailyAverageViewAccessibility accessibilityElements] : 644 -> 680
~ -[TrendDetailDailyAverageViewAccessibility _axLabelForIndex:withFormatter:] : 1200 -> 1256
~ ___75-[TrendDetailDailyAverageViewAccessibility _axLabelForIndex:withFormatter:]_block_invoke : 80 -> 84
~ ___75-[TrendDetailDailyAverageViewAccessibility _axLabelForIndex:withFormatter:]_block_invoke_2 : 80 -> 84
~ -[TrendDetailDailyAverageViewAccessibility _axDayStringForIndex:withFormatter:] : 388 -> 392
~ ___79-[TrendDetailDailyAverageViewAccessibility _axDayStringForIndex:withFormatter:]_block_invoke : 80 -> 84
~ +[PaletteWeekdayHeaderViewAccessibility _accessibilityPerformValidations:] : 128 -> 136
~ -[PaletteWeekdayHeaderViewAccessibility _accessibilityLoadAccessibilityInformation] : 320 -> 328
~ ___83-[PaletteWeekdayHeaderViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 344 -> 352
~ -[PaletteWeekdayHeaderViewAccessibility _accessibilityHitTest:withEvent:] : 144 -> 152
~ -[PaletteWeekdayHeaderViewAccessibility accessibilityElements] : 132 -> 140
~ +[CHWorkoutDetailFourColumnDownhillRunTableViewCellAccessibility _accessibilityPerformValidations:] : 336 -> 344
~ -[CHWorkoutDetailFourColumnDownhillRunTableViewCellAccessibility configureWithDownhillRunsStats:activityType:formattingManager:] : 704 -> 752
~ -[CHWorkoutDetailFourColumnDownhillRunTableViewCellAccessibility configureWithDownhillRun:downhillRunIndex:activityType:isLastCell:formattingManager:] : 904 -> 976
~ +[CHWorkoutDetailFourColumnSwimmingSetTableViewCellAccessibility _accessibilityPerformValidations:] : 296 -> 308
~ -[CHWorkoutDetailFourColumnSwimmingSetTableViewCellAccessibility configureWithSwimmingSet:index:isLastCell:formattingManager:] : 884 -> 960
~ -[TrendPairTableViewCellAccessibility _accessibilityLoadAccessibilityInformation] : 284 -> 288
~ +[DayViewStandChartTableViewCellAccessibility _accessibilityPerformValidations:] : 144 -> 156
~ -[DayViewStandChartTableViewCellAccessibility accessibilityElements] : 272 -> 296
~ +[MonthWeekViewAccessibility _accessibilityPerformValidations:] : 116 -> 128
~ -[MonthWeekViewAccessibility accessibilityElements] : 484 -> 508
~ +[DayViewActivityRingsTableViewCellAccessibility _accessibilityPerformValidations:] : 168 -> 176
~ -[DayViewActivityRingsTableViewCellAccessibility accessibilityLabel] : 204 -> 224
~ -[DayViewActivityRingsTableViewCellAccessibility accessibilityFrame] : 104 -> 108
~ -[DayViewActivityRingsTableViewCellAccessibility accessibilityPath] : 84 -> 92
~ +[CHWorkoutDetailFourColumnTrackLapTableViewCellAccessibility _accessibilityPerformValidations:] : 384 -> 392
~ -[CHWorkoutDetailFourColumnTrackLapTableViewCellAccessibility configureWithTrackLap:lapIndex:workout:distanceUnit:activityType:activityMoveMode:isLastCell:formattingManager:] : 1508 -> 1608
~ +[MonthScrollViewControllerAccessibility _accessibilityPerformValidations:] : 124 -> 136
~ -[MonthScrollViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 120 -> 124
~ +[CHNoHeartRateDataViewControllerAccessibility _accessibilityPerformValidations:] : 188 -> 200
~ -[CHNoHeartRateDataViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 352 -> 364
~ ___90-[CHNoHeartRateDataViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 108 -> 116
~ +[CHFriendListTableViewCellAccessibility _accessibilityPerformValidations:] : 228 -> 236
~ -[CHFriendListTableViewCellAccessibility _accessibilityLoadAccessibilityInformation] : 524 -> 556
~ ___84-[CHFriendListTableViewCellAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 116 -> 124
~ +[CHWorkoutDetailExpandingHeaderViewAccessibility _accessibilityPerformValidations:] : 152 -> 160
~ -[CHWorkoutDetailExpandingHeaderViewAccessibility accessibilityActivationPoint] : 80 -> 84
~ +[CHListSummaryTableViewCellAccessibility _accessibilityPerformValidations:] : 220 -> 228
~ -[CHListSummaryTableViewCellAccessibility accessibilityElements] : 280 -> 308
~ +[WorkoutsListContentViewAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[WorkoutsListContentViewAccessibility _accessibilityLoadAccessibilityInformation] : 384 -> 392
~ ___82-[WorkoutsListContentViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 296 -> 316
~ -[WorkoutsListContentViewAccessibility _isDateInLastWeek:] : 220 -> 244
~ +[TodayActivityTileAccessibility _accessibilityPerformValidations:] : 224 -> 232
~ -[TodayActivityTileAccessibility accessibilityElements] : 332 -> 360
~ +[FitDayCellLayerAccessibility _accessibilityPerformValidations:] : 212 -> 220
~ +[FitDayCellLayerAccessibility activityCellImageWithDiameter:thickness:calories:briskMinutes:hourlyBreak:fadeInnerRings:fadeAll:] : 136 -> 144
~ -[FitDayCellLayerAccessibility accessibilityLabel] : 320 -> 344
~ -[FitDayCellLayerAccessibility accessibilityValue] : 176 -> 192
~ +[CHWorkoutDetailTwoValueTableViewCellAccessibility _accessibilityPerformValidations:] : 260 -> 268
~ -[CHWorkoutDetailTwoValueTableViewCellAccessibility accessibilityElements] : 400 -> 428
~ -[CHWorkoutDetailTwoValueTableViewCellAccessibility configureWithTitle1:value1:] : 168 -> 176
~ -[CHWorkoutDetailTwoValueTableViewCellAccessibility configureWithTitle2:value2:] : 168 -> 176
~ -[CHWorkoutDetailTwoValueTableViewCellAccessibility _axStringForValue:] : 208 -> 232
~ +[TrendingDownTableViewCellAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[TrendingDownTableViewCellAccessibility accessibilityLabel] : 164 -> 180
~ +[CHFriendInboxBarButtonViewAccessibility _accessibilityPerformValidations:] : 120 -> 128
~ -[CHFriendInboxBarButtonViewAccessibility accessibilityValue] : 244 -> 264

```
