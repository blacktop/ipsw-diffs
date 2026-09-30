## NanoWeatherComplicationsCompanion

> `/System/Library/PrivateFrameworks/NanoWeatherComplicationsCompanion.framework/NanoWeatherComplicationsCompanion`

```diff

-1135.2.9.0.0
-  __TEXT.__text: 0x8f04
-  __TEXT.__auth_stubs: 0x360
+1135.5.10.0.0
+  __TEXT.__text: 0x9b5c
+  __TEXT.__auth_stubs: 0x2e0
   __TEXT.__delay_helper: 0xdc
   __TEXT.__objc_methlist: 0xc14
   __TEXT.__const: 0x1c0
   __TEXT.__cstring: 0x3c7
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x2f0
+  __TEXT.__unwind_info: 0x338
   __TEXT.__objc_classname: 0x445
   __TEXT.__objc_methname: 0x1c2d
   __TEXT.__objc_methtype: 0x443

   __DATA_CONST.__objc_selrefs: 0x8b8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x1b8
+  __AUTH_CONST.__auth_got: 0x178
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__cfstring: 0x460
   __AUTH_CONST.__objc_const: 0x2090

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A74B9FEB-B3A0-33CF-8064-9F01C12D3211
+  UUID: 7F0714CD-206D-36CF-8E48-EA16E7A49BB1
   Functions: 243
-  Symbols:   1220
+  Symbols:   1212
   CStrings:  517
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x24
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
Functions:
~ ___35+[NWCHourlyForecastView initialize]_block_invoke : 232 -> 240
~ -[NWCHourlyForecastView initWithDevice:] : 920 -> 944
~ -[NWCHourlyForecastView applySimpleEntryModel:] : 184 -> 208
~ -[NWCHourlyForecastView _applyDate:timeZone:] : 720 -> 776
~ ___45-[NWCHourlyForecastView _applyDate:timeZone:]_block_invoke : 120 -> 124
~ -[NWCHourlyForecastView applyNonAccentFilters:] : 112 -> 120
~ -[NWCHourlyForecastView _applyConstraintsWithConstants:] : 1804 -> 2060
~ ____LayoutConstants_block_invoke_3 : 340 -> 348
~ +[NWCColor conditionsBackgroundColor] : 68 -> 84
~ ___37+[NWCColor conditionsBackgroundColor]_block_invoke : 100 -> 108
~ +[NWCColor conditionsBlueTintColor] : 68 -> 84
~ ___35+[NWCColor conditionsBlueTintColor]_block_invoke : 92 -> 96
~ +[NWCColor conditionsYellowTintColor] : 68 -> 84
~ ___37+[NWCColor conditionsYellowTintColor]_block_invoke : 92 -> 96
~ +[NWCColor conditionsNoDataColor] : 68 -> 84
~ ___33+[NWCColor conditionsNoDataColor]_block_invoke : 72 -> 76
~ +[NWCColor titleNoDataColor] : 68 -> 84
~ ___28+[NWCColor titleNoDataColor]_block_invoke : 84 -> 88
~ -[NWCSevenDayForecastView _addDailyForecastViewsToStackView:] : 780 -> 856
~ -[NWCSevenDayForecastView _applyConstraints] : 532 -> 600
~ -[NWCSevenDayForecastView configureWithImageProvider:reason:] : 120 -> 128
~ -[NWCSevenDayForecastView transitionToMonochromeWithFraction:] : 872 -> 932
~ ___62-[NWCSevenDayForecastView transitionToMonochromeWithFraction:]_block_invoke : 128 -> 136
~ -[NWCSevenDayForecastView updateMonochromeColor] : 804 -> 860
~ ___48-[NWCSevenDayForecastView updateMonochromeColor]_block_invoke : 116 -> 124
~ -[NWCSevenDayForecastView _setupViewBuilderForDevice:] : 136 -> 144
~ -[NWCSevenDayForecastView viewBuilder] : 124 -> 136
~ -[NWCSevenDayForecastView setDailyForecastRangeView:] : 20 -> 80
~ -[NWCSevenDayForecastView setDailyForecastViews:] : 20 -> 80
~ -[NWCSevenDayForecastView setViewBuilder:] : 20 -> 80
~ -[NWCSevenDayForecastView setSeparatorViews:] : 20 -> 80
~ -[NWCSevenDayForecastView setHorizontalStackView:] : 20 -> 80
~ -[NWCHourlyForecastWindView applySimpleEntryModel:] : 400 -> 440
~ -[NWCHourlyForecastWindView applyStyle] : 292 -> 312
~ -[NWCHourlyForecastWindView applyAccentFilters:] : 140 -> 148
~ -[NWCHourlyForecastWindView applyNonAccentFilters:] : 184 -> 200
~ ____LayoutConstants_block_invoke_3 : 176 -> 180
~ +[NWMUltravioletIndexColorIndex allIndices] : 160 -> 176
~ ___43+[NWMUltravioletIndexColorIndex allIndices]_block_invoke : 1160 -> 1260
~ _NWCComplicationFamilyDescription : 88 -> 92
~ _NWCHourlyDateEnumeration : 348 -> 352
~ _NWCMinuteByMinuteDateEnumeration : 348 -> 352
~ _NWCIsCurrentLocaleNonLatin : 128 -> 136
~ ___NWCIsCurrentLocaleNonLatin_block_invoke : 132 -> 136
~ _NWCLocalizationBundle : 68 -> 84
~ ___NWCLocalizationBundle_block_invoke : 92 -> 96
~ _NWCLocalizedImageNamed : 168 -> 184
~ _NWCLocalizedString : 116 -> 124
~ _NWCGlyphPrefixedTextProvider : 232 -> 240
~ ___NWCGlyphPrefixedTextProvider_block_invoke : 276 -> 284
~ _NWCExtraLargeScalingFactor : 224 -> 228
~ ___NWCExtraLargeScalingFactor_block_invoke_3 : 92 -> 96
~ _NWMConditionsLocalizedString : 128 -> 136
~ -[NWCHourlyForecastConditionGlyphView applySimpleEntryModel:] : 504 -> 568
~ -[NWCHourlyForecastConditionGlyphView applyStyle] : 292 -> 312
~ -[NWCHourlyForecastConditionGlyphView applyAccentFilters:] : 140 -> 148
~ -[NWCHourlyForecastConditionGlyphView applyNonAccentFilters:] : 184 -> 200
~ ____LayoutConstants_block_invoke_3 : 176 -> 180
~ -[NWCHourlyForecastTemperatureViewBuilder initWithDevice:] : 116 -> 108
~ -[NWCHourlyForecastTemperatureViewBuilder createHourlyForecastView] : 104 -> 108
~ -[NWCHourlyForecastPrecipitationViewBuilder initWithDevice:] : 116 -> 108
~ -[NWCHourlyForecastPrecipitationViewBuilder createHourlyForecastView] : 104 -> 108
~ -[NWCDailyForecastRangeView initWithFrame:] : 260 -> 264
~ -[NWCDailyForecastRangeView _applyConstraints:] : 808 -> 916
~ -[NWCDailyForecastRangeView _rangeLabelWithFontSize:] : 240 -> 248
~ ____LayoutConstants_block_invoke_3 : 436 -> 448
~ +[NWCCBundle bundle] : 68 -> 84
~ ___20+[NWCCBundle bundle]_block_invoke : 92 -> 96
~ ___38+[NWCForecastSeparatorView initialize]_block_invoke : 72 -> 76
~ +[NWCForecastSeparatorView defaultColor] : 12 -> 60
~ -[NWCSimpleHourEntryModel initWithTopString:middleString:bottomString:isDay:timeZone:] : 232 -> 216
~ -[NWCSimpleHourEntryModel initWithCoder:] : 424 -> 460
~ -[NWCSimpleHourEntryModel encodeWithCoder:] : 376 -> 412
~ -[NWCSimpleEntryModel initWithEntries:] : 116 -> 108
~ -[NWCSimpleEntryModel initWithCoder:] : 156 -> 164
~ -[NWCSimpleEntryModel encodeWithCoder:] : 128 -> 136
~ -[NWCHourlyForecastWindViewBuilder initWithDevice:] : 116 -> 108
~ -[NWCHourlyForecastWindViewBuilder createHourlyForecastView] : 104 -> 108
~ -[NWCDailyForecastUltravioletIndexViewBuilder initWithDevice:] : 116 -> 108
~ -[NWCDailyForecastUltravioletIndexViewBuilder createDailyForecastView] : 104 -> 108
~ +[NWMUltravioletIndexCategoryColor spectrum] : 144 -> 164
~ +[NWMUltravioletIndexCategoryColor colorForNumber:] : 96 -> 104
~ -[NWCDailyForecastUltravioletIndexView initWithDevice:] : 136 -> 144
~ -[NWCWindObservationsBaseView _applyConstraintsWithLayoutConstants:] : 1204 -> 1376
~ -[NWCWindObservationsBaseView _processWindSpeed:unit:directionAbbreviation:] : 384 -> 400
~ -[NWCWindObservationsBaseView initFullColorImageViewWithDevice:] : 856 -> 880
~ -[NWCWindObservationsBaseView configureWithImageProvider:reason:] : 256 -> 280
~ -[NWCWindObservationsBaseView transitionToMonochromeWithFraction:] : 292 -> 328
~ -[NWCWindObservationsBaseView updateMonochromeColor] : 288 -> 328
~ -[NWCWindObservationsBaseView setDevice:] : 20 -> 80
~ -[NWCWindObservationsBaseView setWindDirectionAbbreviationLabel:] : 20 -> 80
~ -[NWCWindObservationsBaseView setWindSpeedLabel:] : 20 -> 80
~ -[NWCWindObservationsBaseView setWindUnitLabel:] : 20 -> 80
~ ____LayoutConstants_block_invoke_3 : 436 -> 444
~ ____LinearGaugeLayoutConstants_block_invoke_3 : 308 -> 316
~ -[NWCDailyForecastView initWithDevice:] : 564 -> 572
~ -[NWCDailyForecastView layoutSubviews] : 216 -> 228
~ -[NWCDailyForecastView applyAccentFilters:fraction:] : 148 -> 156
~ -[NWCDailyForecastView applyNonAccentFilters:fraction:] : 204 -> 224
~ -[NWCDailyForecastView updateWithHighlightColor:fraction:] : 112 -> 116
~ -[NWCDailyForecastView _applyLayoutConstraints:] : 348 -> 384
~ ____LayoutConstants_block_invoke_3 : 460 -> 476
~ -[NWCSevenDayForecastUltravioletIndexView processSimpleEntryModel:] : 532 -> 584
~ ___67-[NWCSevenDayForecastUltravioletIndexView processSimpleEntryModel:]_block_invoke : 336 -> 352
~ ___67-[NWCSevenDayForecastUltravioletIndexView processSimpleEntryModel:]_block_invoke.14 : 836 -> 936
~ -[NWCFiveHourForecastView processSimpleEntryModel:] : 140 -> 144
~ ___51-[NWCFiveHourForecastView processSimpleEntryModel:]_block_invoke : 188 -> 200
~ -[NWCFiveHourForecastView _addHourlyForecastViewsToStackView:] : 584 -> 632
~ -[NWCFiveHourForecastView _applyConstraints] : 532 -> 600
~ -[NWCFiveHourForecastView configureWithImageProvider:reason:] : 120 -> 128
~ -[NWCFiveHourForecastView transitionToMonochromeWithFraction:] : 592 -> 640
~ -[NWCFiveHourForecastView updateMonochromeColor] : 520 -> 560
~ -[NWCFiveHourForecastView _setupViewBuilderForDevice:] : 136 -> 144
~ -[NWCFiveHourForecastView viewBuilder] : 124 -> 136
~ -[NWCFiveHourForecastView setHourlyForecastViews:] : 20 -> 80
~ -[NWCFiveHourForecastView setViewBuilder:] : 20 -> 80
~ -[NWCFiveHourForecastView setSeparatorViews:] : 20 -> 80
~ -[NWCFiveHourForecastView setHorizontalStackView:] : 20 -> 80
~ +[NWCLocationDisplayName attributedDisplayNameWithLocationGlyph:inFont:] : 268 -> 276
~ +[NWCLocationDisplayName attributedDisplayNameWithLocationGlyph:withTextStyle:] : 180 -> 192
~ +[NWCLocationDisplayName _attributedDisplayName:prefixedWithLocationGlyph:] : 292 -> 304
CStrings:
+ "FE1BCD7B-332F-481C-B7DE-7E80973B07BF"
- "FE1BCD7B-63A2-4EB3-9EF5-D6A9E506101E"

```
