## NanoWeatherComplicationsCompanion

> `/System/Library/PrivateFrameworks/NanoWeatherComplicationsCompanion.framework/NanoWeatherComplicationsCompanion`

```diff

-1135.5.12.0.0
-  __TEXT.__text: 0x9b5c
-  __TEXT.__auth_stubs: 0x2e0
+1160.0.0.0.0
+  __TEXT.__text: 0x8f90
   __TEXT.__delay_helper: 0xdc
   __TEXT.__objc_methlist: 0xc14
   __TEXT.__const: 0x1c0
-  __TEXT.__cstring: 0x3c7
+  __TEXT.__cstring: 0x3d5
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x338
-  __TEXT.__objc_classname: 0x445
-  __TEXT.__objc_methname: 0x1c2d
-  __TEXT.__objc_methtype: 0x443
-  __TEXT.__objc_stubs: 0x1b20
-  __DATA_CONST.__got: 0x190
+  __TEXT.__unwind_info: 0x2f0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x188
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_selrefs: 0x8b8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0x190
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__cfstring: 0x460
   __AUTH_CONST.__objc_const: 0x2090
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x50
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x960
   __DATA.__objc_ivar: 0x98
   __DATA.__data: 0x304

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EB5BDA9D-EE96-3E36-8C82-B5AC2B669046
+  UUID: 16A0DF7A-0C21-3634-9ECF-ABA58FBCE1F1
   Functions: 243
-  Symbols:   1212
-  CStrings:  517
+  Symbols:   1220
+  CStrings:  75
 
Symbols:
+ _OBJC_CLASS_$_NTKOverrideTextProvider$loadHelper_x8
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _gotLoadHelper_x8$_OBJC_CLASS_$_NTKOverrideTextProvider
- _objc_retainAutoreleasedReturnValue
Functions:
~ ___35+[NWCHourlyForecastView initialize]_block_invoke : 240 -> 232
~ -[NWCHourlyForecastView initWithDevice:] : 944 -> 936
~ -[NWCHourlyForecastView applySimpleEntryModel:] : 208 -> 184
~ -[NWCHourlyForecastView _applyDate:timeZone:] : 776 -> 720
~ ___45-[NWCHourlyForecastView _applyDate:timeZone:]_block_invoke : 124 -> 120
~ -[NWCHourlyForecastView applyNonAccentFilters:] : 120 -> 112
~ -[NWCHourlyForecastView _applyConstraintsWithConstants:] : 2060 -> 1804
~ -[NWCHourlyForecastView device] : 16 -> 20
~ -[NWCHourlyForecastView topLabel] : 16 -> 20
~ -[NWCHourlyForecastView middleImageView] : 16 -> 20
~ -[NWCHourlyForecastView middleLabel] : 16 -> 20
~ -[NWCHourlyForecastView timeLabel] : 16 -> 20
~ ____LayoutConstants_block_invoke_3 : 348 -> 340
~ +[NWCColor conditionsBackgroundColor] : 84 -> 68
~ ___37+[NWCColor conditionsBackgroundColor]_block_invoke : 108 -> 100
~ +[NWCColor conditionsBlueTintColor] : 84 -> 68
~ ___35+[NWCColor conditionsBlueTintColor]_block_invoke : 96 -> 92
~ +[NWCColor conditionsYellowTintColor] : 84 -> 68
~ ___37+[NWCColor conditionsYellowTintColor]_block_invoke : 96 -> 92
~ +[NWCColor conditionsNoDataColor] : 84 -> 68
~ ___33+[NWCColor conditionsNoDataColor]_block_invoke : 76 -> 72
~ +[NWCColor titleNoDataColor] : 84 -> 68
~ ___28+[NWCColor titleNoDataColor]_block_invoke : 88 -> 84
~ -[NWCSevenDayForecastView _addDailyForecastViewsToStackView:] : 856 -> 780
~ -[NWCSevenDayForecastView _applyConstraints] : 600 -> 532
~ -[NWCSevenDayForecastView initFullColorImageViewWithDevice:] : 212 -> 216
~ -[NWCSevenDayForecastView configureWithImageProvider:reason:] : 128 -> 120
~ -[NWCSevenDayForecastView transitionToMonochromeWithFraction:] : 932 -> 872
~ ___62-[NWCSevenDayForecastView transitionToMonochromeWithFraction:]_block_invoke : 136 -> 128
~ -[NWCSevenDayForecastView updateMonochromeColor] : 860 -> 804
~ ___48-[NWCSevenDayForecastView updateMonochromeColor]_block_invoke : 124 -> 116
~ -[NWCSevenDayForecastView _setupViewBuilderForDevice:] : 144 -> 136
~ -[NWCSevenDayForecastView viewBuilder] : 136 -> 128
~ -[NWCSevenDayForecastView device] : 16 -> 20
~ -[NWCSevenDayForecastView dailyForecastRangeView] : 16 -> 20
~ -[NWCSevenDayForecastView setDailyForecastRangeView:] : 80 -> 20
~ -[NWCSevenDayForecastView dailyForecastViews] : 16 -> 20
~ -[NWCSevenDayForecastView setDailyForecastViews:] : 80 -> 20
~ -[NWCSevenDayForecastView setViewBuilder:] : 80 -> 20
~ -[NWCSevenDayForecastView separatorViews] : 16 -> 20
~ -[NWCSevenDayForecastView setSeparatorViews:] : 80 -> 20
~ -[NWCSevenDayForecastView horizontalStackView] : 16 -> 20
~ -[NWCSevenDayForecastView setHorizontalStackView:] : 80 -> 20
~ -[NWCHourlyForecastWindView applySimpleEntryModel:] : 440 -> 396
~ -[NWCHourlyForecastWindView applyStyle] : 312 -> 292
~ -[NWCHourlyForecastWindView applyAccentFilters:] : 148 -> 140
~ -[NWCHourlyForecastWindView applyNonAccentFilters:] : 200 -> 184
~ ____LayoutConstants_block_invoke_3 : 180 -> 176
~ +[NWMUltravioletIndexColorIndex allIndices] : 176 -> 160
~ ___43+[NWMUltravioletIndexColorIndex allIndices]_block_invoke : 1260 -> 1160
~ _NWCComplicationFamilyDescription : 92 -> 88
~ _NWCHourlyDateEnumeration : 352 -> 344
~ _NWCMinuteByMinuteDateEnumeration : 352 -> 344
~ _NWCIsCurrentLocaleNonLatin : 136 -> 128
~ ___NWCIsCurrentLocaleNonLatin_block_invoke : 136 -> 132
~ _NWCLocalizationBundle : 84 -> 68
~ ___NWCLocalizationBundle_block_invoke : 96 -> 92
~ _NWCLocalizedImageNamed : 184 -> 168
~ _NWCLocalizedString : 124 -> 116
~ _NWCGlyphPrefixedTextProvider : 240 -> 232
~ ___NWCGlyphPrefixedTextProvider_block_invoke : 284 -> 276
~ _NWCExtraLargeScalingFactor : 228 -> 224
~ ___NWCExtraLargeScalingFactor_block_invoke_3 : 96 -> 92
~ _NWMConditionsLocalizedString : 136 -> 128
~ -[NWCHourlyForecastConditionGlyphView applySimpleEntryModel:] : 568 -> 504
~ -[NWCHourlyForecastConditionGlyphView applyStyle] : 312 -> 292
~ -[NWCHourlyForecastConditionGlyphView applyAccentFilters:] : 148 -> 140
~ -[NWCHourlyForecastConditionGlyphView applyNonAccentFilters:] : 200 -> 184
~ ____LayoutConstants_block_invoke_3 : 180 -> 176
~ -[NWCHourlyForecastTemperatureViewBuilder initWithDevice:] : 108 -> 116
~ -[NWCHourlyForecastTemperatureViewBuilder createHourlyForecastView] : 108 -> 104
~ -[NWCHourlyForecastPrecipitationViewBuilder initWithDevice:] : 108 -> 116
~ -[NWCHourlyForecastPrecipitationViewBuilder createHourlyForecastView] : 108 -> 104
~ -[NWCDailyForecastRangeView initWithFrame:] : 264 -> 260
~ -[NWCDailyForecastRangeView _applyConstraints:] : 916 -> 808
~ -[NWCDailyForecastRangeView _rangeLabelWithFontSize:] : 248 -> 240
~ -[NWCDailyForecastRangeView highLabel] : 16 -> 20
~ -[NWCDailyForecastRangeView lowLabel] : 16 -> 20
~ ____LayoutConstants_block_invoke_3 : 448 -> 436
~ +[NWCCBundle bundle] : 84 -> 68
~ ___20+[NWCCBundle bundle]_block_invoke : 96 -> 92
~ ___38+[NWCForecastSeparatorView initialize]_block_invoke : 76 -> 72
~ +[NWCForecastSeparatorView defaultColor] : 60 -> 12
~ -[NWCSimpleHourEntryModel initWithTopString:middleString:bottomString:isDay:timeZone:] : 216 -> 232
~ -[NWCSimpleHourEntryModel initWithCoder:] : 460 -> 424
~ -[NWCSimpleHourEntryModel encodeWithCoder:] : 412 -> 376
~ -[NWCSimpleEntryModel initWithEntries:] : 108 -> 116
~ -[NWCSimpleEntryModel initWithCoder:] : 164 -> 156
~ -[NWCSimpleEntryModel encodeWithCoder:] : 136 -> 128
~ -[NWCHourlyForecastWindViewBuilder initWithDevice:] : 108 -> 116
~ -[NWCHourlyForecastWindViewBuilder createHourlyForecastView] : 108 -> 104
~ -[NWCDailyForecastUltravioletIndexViewBuilder initWithDevice:] : 108 -> 116
~ -[NWCDailyForecastUltravioletIndexViewBuilder createDailyForecastView] : 108 -> 104
~ +[NWMUltravioletIndexCategoryColor spectrum] : 164 -> 144
~ +[NWMUltravioletIndexCategoryColor colorForNumber:] : 104 -> 96
~ -[NWCDailyForecastUltravioletIndexView initWithDevice:] : 144 -> 136
~ -[NWCWindObservationsBaseView _applyConstraintsWithLayoutConstants:] : 1376 -> 1204
~ -[NWCWindObservationsBaseView _processWindSpeed:unit:directionAbbreviation:] : 400 -> 384
~ -[NWCWindObservationsBaseView initFullColorImageViewWithDevice:] : 880 -> 868
~ -[NWCWindObservationsBaseView configureWithImageProvider:reason:] : 280 -> 256
~ -[NWCWindObservationsBaseView transitionToMonochromeWithFraction:] : 328 -> 292
~ -[NWCWindObservationsBaseView updateMonochromeColor] : 328 -> 288
~ -[NWCWindObservationsBaseView device] : 16 -> 20
~ -[NWCWindObservationsBaseView setDevice:] : 80 -> 20
~ -[NWCWindObservationsBaseView windDirectionAbbreviationLabel] : 16 -> 20
~ -[NWCWindObservationsBaseView setWindDirectionAbbreviationLabel:] : 80 -> 20
~ -[NWCWindObservationsBaseView windSpeedLabel] : 16 -> 20
~ -[NWCWindObservationsBaseView setWindSpeedLabel:] : 80 -> 20
~ -[NWCWindObservationsBaseView windUnitLabel] : 16 -> 20
~ -[NWCWindObservationsBaseView setWindUnitLabel:] : 80 -> 20
~ ____LayoutConstants_block_invoke_3 : 444 -> 436
~ ____LinearGaugeLayoutConstants_block_invoke_3 : 316 -> 308
~ -[NWCDailyForecastView layoutSubviews] : 228 -> 216
~ -[NWCDailyForecastView applyAccentFilters:fraction:] : 156 -> 148
~ -[NWCDailyForecastView applyNonAccentFilters:fraction:] : 224 -> 204
~ -[NWCDailyForecastView updateWithHighlightColor:fraction:] : 116 -> 112
~ -[NWCDailyForecastView _applyLayoutConstraints:] : 384 -> 348
~ -[NWCDailyForecastView device] : 16 -> 20
~ -[NWCDailyForecastView linearGaugeView] : 16 -> 20
~ -[NWCDailyForecastView weekdayLabel] : 16 -> 20
~ ____LayoutConstants_block_invoke_3 : 476 -> 460
~ -[NWCSevenDayForecastUltravioletIndexView processSimpleEntryModel:] : 584 -> 532
~ ___67-[NWCSevenDayForecastUltravioletIndexView processSimpleEntryModel:]_block_invoke : 352 -> 336
~ ___67-[NWCSevenDayForecastUltravioletIndexView processSimpleEntryModel:]_block_invoke.14 : 936 -> 836
~ -[NWCFiveHourForecastView processSimpleEntryModel:] : 144 -> 140
~ ___51-[NWCFiveHourForecastView processSimpleEntryModel:]_block_invoke : 200 -> 188
~ -[NWCFiveHourForecastView _addHourlyForecastViewsToStackView:] : 632 -> 584
~ -[NWCFiveHourForecastView _applyConstraints] : 600 -> 532
~ -[NWCFiveHourForecastView initFullColorImageViewWithDevice:] : 212 -> 216
~ -[NWCFiveHourForecastView configureWithImageProvider:reason:] : 128 -> 120
~ -[NWCFiveHourForecastView transitionToMonochromeWithFraction:] : 640 -> 596
~ -[NWCFiveHourForecastView updateMonochromeColor] : 560 -> 524
~ -[NWCFiveHourForecastView _setupViewBuilderForDevice:] : 144 -> 136
~ -[NWCFiveHourForecastView viewBuilder] : 136 -> 128
~ -[NWCFiveHourForecastView device] : 16 -> 20
~ -[NWCFiveHourForecastView hourlyForecastViews] : 16 -> 20
~ -[NWCFiveHourForecastView setHourlyForecastViews:] : 80 -> 20
~ -[NWCFiveHourForecastView setViewBuilder:] : 80 -> 20
~ -[NWCFiveHourForecastView separatorViews] : 16 -> 20
~ -[NWCFiveHourForecastView setSeparatorViews:] : 80 -> 20
~ -[NWCFiveHourForecastView horizontalStackView] : 16 -> 20
~ -[NWCFiveHourForecastView setHorizontalStackView:] : 80 -> 20
~ +[NWCLocationDisplayName attributedDisplayNameWithLocationGlyph:inFont:] : 276 -> 268
~ +[NWCLocationDisplayName attributedDisplayNameWithLocationGlyph:withTextStyle:] : 192 -> 180
~ +[NWCLocationDisplayName _attributedDisplayName:prefixedWithLocationGlyph:] : 304 -> 292
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<CLKMonochromeFilterProvider>\""
- "@\"<CLKMonochromeFilterProvider>\"16@0:8"
- "@\"<NWCDailyForecastViewBuildable>\""
- "@\"<NWCHourlyForecastViewBuildable>\""
- "@\"CLKDevice\""
- "@\"CLKDevice\"16@0:8"
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSTimeZone\""
- "@\"NWCDailyForecastRangeView\""
- "@\"NWCDailyForecastView\"16@0:8"
- "@\"NWCHourlyForecastView\"16@0:8"
- "@\"NWKUILinearGaugeView\""
- "@\"UIFontDescriptor\"16@0:8"
- "@\"UIImageView\""
- "@\"UILabel\""
- "@\"UIStackView\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"CLKDevice\"16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8d16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8d16@24"
- "@40@0:8:16@24@32"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@52@0:8@16@24@32B40@44"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CLKFullColorImageView"
- "CLKMonochromeComplicationView"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "NWCCBundle"
- "NWCColor"
- "NWCDailyForecastRangeView"
- "NWCDailyForecastUltravioletIndexView"
- "NWCDailyForecastUltravioletIndexViewBuilder"
- "NWCDailyForecastView"
- "NWCDailyForecastViewBuildable"
- "NWCFiveHourForecastConditionGlyphView"
- "NWCFiveHourForecastPrecipitationView"
- "NWCFiveHourForecastTemperatureView"
- "NWCFiveHourForecastView"
- "NWCFiveHourForecastWindView"
- "NWCForecastSeparatorView"
- "NWCHourlyForecastConditionGlyphView"
- "NWCHourlyForecastPrecipitationView"
- "NWCHourlyForecastPrecipitationViewBuilder"
- "NWCHourlyForecastTemperatureView"
- "NWCHourlyForecastTemperatureViewBuilder"
- "NWCHourlyForecastView"
- "NWCHourlyForecastViewBuildable"
- "NWCHourlyForecastWindView"
- "NWCHourlyForecastWindViewBuilder"
- "NWCLocationDisplayName"
- "NWCSevenDayForecastUltravioletIndexView"
- "NWCSevenDayForecastView"
- "NWCSimpleEntryModel"
- "NWCSimpleHourEntryModel"
- "NWCWindObservationsBaseView"
- "NWCWindObservationsGraphicCircularView"
- "NWCWindObservationsGraphicExtraLargeCircularView"
- "NWKUIColorIndexable"
- "NWMUltravioletIndexCategoryColor"
- "NWMUltravioletIndexColorIndex"
- "Q16@0:8"
- "T#,R"
- "T@\"<CLKMonochromeFilterProvider>\",W,N"
- "T@\"<CLKMonochromeFilterProvider>\",W,N,V_filterProvider"
- "T@\"<NWCDailyForecastViewBuildable>\",&,N,V_viewBuilder"
- "T@\"<NWCHourlyForecastViewBuildable>\",&,N,V_viewBuilder"
- "T@\"CLKDevice\",&,N,V_device"
- "T@\"CLKDevice\",R,N"
- "T@\"CLKDevice\",R,N,V_device"
- "T@\"NSArray\",&,N,V_dailyForecastViews"
- "T@\"NSArray\",&,N,V_hourlyForecastViews"
- "T@\"NSArray\",&,N,V_separatorViews"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,V_hourlyEntryModels"
- "T@\"NSBundle\",R,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,V_bottomString"
- "T@\"NSString\",R,V_middleString"
- "T@\"NSString\",R,V_topString"
- "T@\"NSTimeZone\",R,V_timeZone"
- "T@\"NWCDailyForecastRangeView\",&,N,V_dailyForecastRangeView"
- "T@\"NWKUILinearGaugeView\",R,N,V_linearGaugeView"
- "T@\"UIColor\",R"
- "T@\"UIColor\",R,N"
- "T@\"UIFontDescriptor\",?,C,N"
- "T@\"UIImageView\",R,N,V_middleImageView"
- "T@\"UILabel\",&,N,V_windDirectionAbbreviationLabel"
- "T@\"UILabel\",&,N,V_windSpeedLabel"
- "T@\"UILabel\",&,N,V_windUnitLabel"
- "T@\"UILabel\",R,N,V_highLabel"
- "T@\"UILabel\",R,N,V_lowLabel"
- "T@\"UILabel\",R,N,V_middleLabel"
- "T@\"UILabel\",R,N,V_timeLabel"
- "T@\"UILabel\",R,N,V_topLabel"
- "T@\"UILabel\",R,N,V_weekdayLabel"
- "T@\"UIStackView\",&,N,V_horizontalStackView"
- "TB,R"
- "TB,R,V_isDay"
- "TQ,R"
- "Td,?,N"
- "Td,R,N"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_addDailyForecastViewsToStackView:"
- "_addHourlyForecastViewsToStackView:"
- "_applyConstraints"
- "_applyConstraints:"
- "_applyConstraintsWithConstants:"
- "_applyConstraintsWithLayoutConstants:"
- "_applyDate:timeZone:"
- "_applyLayoutConstraints:"
- "_attributedDisplayName:prefixedWithLocationGlyph:"
- "_bottomString"
- "_dailyForecastRangeView"
- "_dailyForecastViews"
- "_device"
- "_filterProvider"
- "_highLabel"
- "_horizontalStackView"
- "_hourlyEntryModels"
- "_hourlyForecastViews"
- "_isDay"
- "_linearGaugeView"
- "_lowLabel"
- "_middleImageView"
- "_middleLabel"
- "_middleString"
- "_processWindSpeed:unit:directionAbbreviation:"
- "_rangeLabelWithFontSize:"
- "_separatorViews"
- "_setupViewBuilderForDevice:"
- "_timeLabel"
- "_timeZone"
- "_topLabel"
- "_topString"
- "_viewBuilder"
- "_weekdayLabel"
- "_windDirectionAbbreviationLabel"
- "_windSpeedLabel"
- "_windUnitLabel"
- "activateConstraints:"
- "addArrangedSubview:"
- "addAttribute:value:range:"
- "addAttributes:range:"
- "addObject:"
- "addSubview:"
- "allIndices"
- "applyAccentFilters:"
- "applyAccentFilters:fraction:"
- "applyBackgroundGaugeFilters:fraction:"
- "applyEntryModel:date:timeZone:"
- "applyForegroundGaugeFilters:"
- "applyIndicatorFillColor:"
- "applyNonAccentFilters:"
- "applyNonAccentFilters:fraction:"
- "applySimpleEntryModel:"
- "applyStyle"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "attributedDisplayNameWithLocationGlyph:inFont:"
- "attributedDisplayNameWithLocationGlyph:withTextStyle:"
- "attributedStringWithAttachment:"
- "autorelease"
- "autoupdatingCurrentLocale"
- "bottomAnchor"
- "bottomString"
- "bounds"
- "bundle"
- "bundleForClass:"
- "centerXAnchor"
- "centerYAnchor"
- "class"
- "color"
- "colorForNumber:"
- "colorForValue:"
- "colorForView:accented:"
- "colorWithAlphaComponent:"
- "colorWithRed:green:blue:alpha:"
- "colorWithWhite:alpha:"
- "compare:"
- "components:fromDate:"
- "conditionsBackgroundColor"
- "conditionsBlueTintColor"
- "conditionsNoDataColor"
- "conditionsYellowTintColor"
- "configurationWithFont:scale:"
- "configurationWithScale:"
- "configurationWithTextStyle:scale:"
- "configureWithImageProvider:reason:"
- "conformsToProtocol:"
- "constantValue:withOverrides:"
- "constraintEqualToAnchor:"
- "constraintEqualToAnchor:constant:"
- "constraintEqualToAnchor:multiplier:"
- "constraintGreaterThanOrEqualToAnchor:constant:"
- "containsObject:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDailyForecastView"
- "createHourlyForecastView"
- "currentCalendar"
- "currentDevice"
- "currentLocale"
- "d16@0:8"
- "dailyForecastRangeView"
- "dailyForecastViews"
- "dateFormatFromTemplate:options:locale:"
- "dateFromComponents:"
- "dateFromString:"
- "debugDescription"
- "decodeArrayOfObjectsOfClass:forKey:"
- "decodeBoolForKey:"
- "decodeObjectOfClass:forKey:"
- "defaultColor"
- "description"
- "device"
- "dictionaryWithObjects:forKeys:count:"
- "doubleValue"
- "encodeBool:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateObjectsUsingBlock:"
- "extreme"
- "filterProvider"
- "filtersForView:style:"
- "filtersForView:style:fraction:"
- "firstBaselineAnchor"
- "firstObject"
- "font"
- "fontDescriptor"
- "fontSizeFactor"
- "frame"
- "hash"
- "high"
- "highLabel"
- "horizontalStackView"
- "hour"
- "hourlyEntryModels"
- "hourlyForecastViews"
- "imageNamed:inBundle:compatibleWithTraitCollection:"
- "imageWithRenderingMode:"
- "indexForValue:"
- "indexOfObject:"
- "indexWithUltravioletIndexValue:color:"
- "init"
- "initFullColorImageViewWithDevice:"
- "initWithCoder:"
- "initWithDevice:"
- "initWithEntries:"
- "initWithFrame:"
- "initWithLayoutConstants:"
- "initWithString:"
- "initWithTopString:middleString:bottomString:isDay:timeZone:"
- "initWithUUIDString:"
- "initWithUltravioletIndexValue:color:"
- "initWithValue:color:"
- "initialize"
- "insertAttributedString:atIndex:"
- "interpolateIndicatorWithColor:fraction:"
- "intrinsicContentSize"
- "isDay"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "languageCode"
- "lastValue"
- "layer"
- "layoutSubviews"
- "leadingAnchor"
- "length"
- "linearGaugeView"
- "localeWithLocaleIdentifier:"
- "localizedStringForKey:value:table:"
- "low"
- "lowLabel"
- "mainScreen"
- "makeObjectsPerformSelector:withObject:"
- "maximumDailyConditionCount"
- "maximumHourlyConditionCount"
- "metadata"
- "metricsWithDevice:identitySizeClass:"
- "middleImageView"
- "middleLabel"
- "middleString"
- "minute"
- "moderate"
- "mutableCopy"
- "numberFromString:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "otherAttributes"
- "pauseLiveFullColorImageView"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "processSimpleEntryModel:"
- "q16@0:8"
- "raise:format:"
- "release"
- "renderSynchronouslyWithImageQueueDiscard:inGroup:"
- "respondsToSelector:"
- "resumeLiveFullColorImageView"
- "retain"
- "retainCount"
- "scaledValue:"
- "scaledValue:withOverrides:"
- "screenScale"
- "self"
- "separatorViews"
- "setAdjustsFontSizeToFitWidth:"
- "setAxis:"
- "setBackgroundColor:"
- "setBackgroundColorIndices:"
- "setBaselineAdjustment:"
- "setColorIndices:"
- "setContentCompressionResistancePriority:forAxis:"
- "setContentHuggingPriority:forAxis:"
- "setContentMode:"
- "setDailyForecastRangeView:"
- "setDailyForecastViews:"
- "setDateFormat:"
- "setDevice:"
- "setDistribution:"
- "setFilterProvider:"
- "setFilters:"
- "setFont:"
- "setFontDescriptor:"
- "setFontSizeFactor:"
- "setFrame:"
- "setHighValue:"
- "setHorizontalStackView:"
- "setHour:"
- "setHourlyForecastViews:"
- "setImage:"
- "setLocale:"
- "setMaximumFractionDigits:"
- "setMinimumIntegerDigits:"
- "setMinimumScaleFactor:"
- "setMinute:"
- "setNumberOfLines:"
- "setObject:forKeyedSubscript:"
- "setPriority:"
- "setRenderValueAsPercentage:"
- "setRoundingBehavior:"
- "setSeparatorViews:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setTimeZone:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setValue:"
- "setViewBuilder:"
- "setWindDirectionAbbreviationLabel:"
- "setWindSpeedLabel:"
- "setWindUnitLabel:"
- "setWithObject:"
- "setWithObjects:"
- "spectrum"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringFromDate:"
- "stringFromNumber:"
- "stringWithFormat:"
- "subarrayWithRange:"
- "superclass"
- "supportedComplicationFamily"
- "supportsCapability:"
- "supportsSecureCoding"
- "systemCyanColor"
- "systemFontOfSize:weight:design:"
- "systemGrayTextColor"
- "systemGreenColor"
- "systemImageNamed:withConfiguration:"
- "systemOrangeColor"
- "systemPinkColor"
- "systemPurpleColor"
- "systemRedColor"
- "systemYellowColor"
- "textProviderWithText:"
- "textProviderWithText:overrideBlock:"
- "timeLabel"
- "timeZone"
- "timeZoneForSecondsFromGMT:"
- "tintColor"
- "titleNoDataColor"
- "topAnchor"
- "topLabel"
- "topString"
- "trailingAnchor"
- "traitCollection"
- "transitionToMonochromeWithFraction:"
- "unknown"
- "updateMonochromeColor"
- "updateWithHighlightColor:fraction:"
- "uppercaseStringWithLocale:"
- "v16@0:8"
- "v24@0:8@\"<CLKMonochromeFilterProvider>\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"UIFontDescriptor\"16"
- "v24@0:8@16"
- "v24@0:8d16"
- "v28@0:8B16@\"NSObject<OS_dispatch_group>\"20"
- "v28@0:8B16@20"
- "v32@0:8@\"CLKFullColorImageProvider\"16q24"
- "v32@0:8@16@24"
- "v32@0:8@16d24"
- "v32@0:8@16q24"
- "v40@0:8@16@24@32"
- "v48@0:8{?=dddd}16"
- "v56@0:8{?=ddddd}16"
- "valueForKeyPath:"
- "version"
- "veryHigh"
- "viewBuilder"
- "weekdayLabel"
- "whiteColor"
- "widthAnchor"
- "windDirectionAbbreviationLabel"
- "windSpeedLabel"
- "windUnitLabel"
- "zone"
- "{CGSize=dd}16@0:8"

```
