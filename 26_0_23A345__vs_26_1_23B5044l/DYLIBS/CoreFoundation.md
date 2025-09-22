## CoreFoundation

> `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

```diff

-4040.1.0.0.0
-  __TEXT.__text: 0x1be564
-  __TEXT.__auth_stubs: 0x31e0
+4103.1.101.0.0
+  __TEXT.__text: 0x1b714c
+  __TEXT.__auth_stubs: 0x31c0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x7a5c
-  __TEXT.__const: 0x1a1728
-  __TEXT.__oslogstring: 0x58d8
-  __TEXT.__cstring: 0x14b327
-  __TEXT.__gcc_except_tab: 0x454c
+  __TEXT.__const: 0x1a1708
+  __TEXT.__oslogstring: 0x560c
+  __TEXT.__cstring: 0x149630
+  __TEXT.__gcc_except_tab: 0x44e4
   __TEXT.__ustring: 0x484
   __TEXT.__dof_CFRunLoop: 0x964
   __TEXT.__dof_Cocoa_Aut: 0x486
-  __TEXT.__unwind_info: 0x5ca0
-  __TEXT.__eh_frame: 0x588
+  __TEXT.__unwind_info: 0x5b38
+  __TEXT.__eh_frame: 0x478
   __TEXT.__objc_classname: 0xa9a
-  __TEXT.__objc_methname: 0x8370
-  __TEXT.__objc_methtype: 0xb399f
+  __TEXT.__objc_methname: 0x8374
+  __TEXT.__objc_methtype: 0xb39b7
   __TEXT.__objc_stubs: 0x60c0
   __DATA_CONST.__got: 0x490
-  __DATA_CONST.__const: 0x37d6c0
+  __DATA_CONST.__const: 0x37d130
   __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_nlclslist: 0x58
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_arraydata: 0x16e0
-  __AUTH_CONST.__auth_got: 0x1908
-  __AUTH_CONST.__const: 0x4d68
-  __AUTH_CONST.__cfstring: 0x1414c0
-  __AUTH_CONST.__objc_const: 0x9ad8
+  __AUTH_CONST.__auth_got: 0x18f8
+  __AUTH_CONST.__const: 0x4d48
+  __AUTH_CONST.__cfstring: 0x140920
+  __AUTH_CONST.__objc_const: 0x9af8
   __AUTH_CONST.__const_cfobj2: 0x40
   __AUTH_CONST.__objc_dictobj: 0x7f8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xa50
   __AUTH.__data: 0x58
-  __DATA.__objc_ivar: 0x51c
+  __DATA.__objc_ivar: 0x520
   __DATA.__data: 0x6f4
   __DATA.__cf_except_bt: 0x2000
   __DATA.__cf_except_pack: 0x410
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x9c8
+  __DATA.__bss: 0x980
   __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0x21c0
   __DATA_DIRTY.__data: 0x170
-  __DATA_DIRTY.__bss: 0xe80
+  __DATA_DIRTY.__bss: 0xe78
   __DATA_DIRTY.__common: 0x398
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 973E47E5-88F0-3367-B9D4-46D5CB999B75
-  Functions: 7998
-  Symbols:   20470
-  CStrings:  100977
+  UUID: 9E28C72B-0B77-336B-A472-0C4BA8581B62
+  Functions: 7874
+  Symbols:   20199
+  CStrings:  100565
 
Symbols:
+ -[_CFXPreferencesHandle _canUseCachedPersonaInfo]
+ GCC_except_table102
+ GCC_except_table117
+ GCC_except_table122
+ GCC_except_table129
+ GCC_except_table133
+ GCC_except_table139
+ GCC_except_table157
+ GCC_except_table177
+ GCC_except_table179
+ GCC_except_table260
+ GCC_except_table264
+ GCC_except_table29
+ GCC_except_table44
+ GCC_except_table56
+ GCC_except_table76
+ _OBJC_IVAR_$__CFXPreferencesHandle.cachedUseLaunchPersona
+ _OBJC_IVAR_$__CFXPreferencesHandle.lastCheckedVoucher
+ __CFBundleInitPlugIn.cold.3
+ ___38-[_CFXPreferences flushManagedSources]_block_invoke.68
+ ___65-[_CFXPreferences _setupNewDaemonConnection:invalidationHandler:]_block_invoke.102
+ ___65-[_CFXPreferences _setupNewDaemonConnection:invalidationHandler:]_block_invoke.109
+ ___CFAppendFormattedValue
+ ___CFAppendFormattedValueWithStatisticalWritingDirections
+ ___CFShouldUseIsolatesForAppendingValue
+ ___CFShouldUseIsolatesForAppendingValueWithStatisticalWritingDirections
+ ___block_descriptor_tmp.118
+ ___block_descriptor_tmp.79
+ ___block_descriptor_tmp.82
+ ___block_literal_global.111
+ ___block_literal_global.197
+ ___block_literal_global.206
+ ___block_literal_global.245
+ ___block_literal_global.249
+ ___block_literal_global.257
+ ___block_literal_global.81
+ _voucher_release
- GCC_except_table101
- GCC_except_table116
- GCC_except_table118
- GCC_except_table121
- GCC_except_table123
- GCC_except_table128
- GCC_except_table138
- GCC_except_table146
- GCC_except_table156
- GCC_except_table158
- GCC_except_table176
- GCC_except_table178
- GCC_except_table259
- GCC_except_table263
- GCC_except_table46
- GCC_except_table93
- GCC_except_table97
- GCC_except_table99
- _OBJC_IVAR_$__CFXPreferencesHandle.checkedProcessCanHaveMultiplePersonas
- __CFICULog.cold.1
- ___38-[_CFXPreferences flushManagedSources]_block_invoke.66
- ___65-[_CFXPreferences _setupNewDaemonConnection:invalidationHandler:]_block_invoke.100
- ___65-[_CFXPreferences _setupNewDaemonConnection:invalidationHandler:]_block_invoke.107
- ___CFICULogLock
- ____CFICUCopyVariableNameForHeapPointer
- ____CFICUCreateArgumentForDouble
- ____CFICUCreateArgumentForParsePosition
- ____CFICUCreateArgumentForUCharInput
- ____CFICUCreateErrorStringWithComment
- ____CFICUCreateVariableName
- ____CFICUCreateVariableNameForHeapPointer
- ____CFICUCreateVariableNameForStackPointerLocked
- ____CFICUCreateVariableNameForStatus
- ____CFICUCreateVariableNameForStatusIfNeeded
- ____CFICUCreateVariableNameForUCharOutput
- ____CFICUCreateVariableNameLocked
- ____CFICUEmitPostamble
- ____CFICUGetEnumStringForUCalendarDateFields
- ____CFICUGetEnumStringForUCalendarDaysOfWeek
- ____CFICUGetEnumStringForUCalendarLimitType
- ____CFICUGetEnumStringForUDateFormatStyle
- ____CFICUGetEnumStringForUDateFormatSymbolType
- ____CFICUGetEnumStringForUNumberFormatAttribute
- ____CFICUGetEnumStringForUNumberFormatSymbol
- ____CFICUGetEnumStringForUNumberFormatTextAttribute
- ____CFICUGetEnumStringForURelativeDateTimeUnit
- ____CFICULogWithArguments
- ____CFICULoggingEnabled.loggingEnabled
- ____CFICULoggingEnabled.oncep
- ____CFICULoggingFD
- ____CFICULoggingFD_block_invoke.tempBufferCount
- ____CFICUSync.lock
- ______CFICUCopyVariableNameForHeapPointer_block_invoke
- ______CFICUCreateArgumentForUCharInput_block_invoke
- ______CFICUCreateVariableNameForHeapPointer_block_invoke
- ______CFICUCreateVariableNameForStackPointerIfNeeded_block_invoke
- ______CFICUCreateVariableNameForStackPointer_block_invoke
- ______CFICUCreateVariableName_block_invoke
- ______CFICULoggingEnabled_block_invoke
- ______CFICURemoveVariableNameForHeapPointer_block_invoke
- ___block_descriptor_tmp.119
- ___block_descriptor_tmp.181
- ___block_descriptor_tmp.239
- ___block_descriptor_tmp.244
- ___block_descriptor_tmp.263
- ___block_descriptor_tmp.271
- ___block_descriptor_tmp.275
- ___block_descriptor_tmp.276
- ___block_descriptor_tmp.376
- ___block_descriptor_tmp.80
- ___block_descriptor_tmp.83
- ___block_literal_global.109
- ___block_literal_global.121
- ___block_literal_global.183
- ___block_literal_global.189
- ___block_literal_global.193
- ___block_literal_global.205
- ___block_literal_global.243
- ___block_literal_global.247
- ___block_literal_global.255
- ___block_literal_global.82
- ___cficu_ucal_add.cold.2
- ___cficu_ucal_add.cold.3
- ___cficu_ucal_clear.cold.2
- ___cficu_ucal_clear.cold.3
- ___cficu_ucal_clear.cold.4
- ___cficu_ucal_clone.cold.2
- ___cficu_ucal_clone.cold.3
- ___cficu_ucal_close.cold.2
- ___cficu_ucal_close.cold.3
- ___cficu_ucal_close.cold.4
- ___cficu_ucal_close.cold.5
- ___cficu_ucal_get.cold.2
- ___cficu_ucal_get.cold.3
- ___cficu_ucal_getAttribute.cold.2
- ___cficu_ucal_getAttribute.cold.3
- ___cficu_ucal_getDayOfWeekType.cold.2
- ___cficu_ucal_getDayOfWeekType.cold.3
- ___cficu_ucal_getFieldDifference.cold.2
- ___cficu_ucal_getFieldDifference.cold.3
- ___cficu_ucal_getGregorianChange.cold.2
- ___cficu_ucal_getGregorianChange.cold.3
- ___cficu_ucal_getLimit.cold.2
- ___cficu_ucal_getLimit.cold.3
- ___cficu_ucal_getMillis.cold.2
- ___cficu_ucal_getMillis.cold.3
- ___cficu_ucal_getWeekendTransition.cold.2
- ___cficu_ucal_getWeekendTransition.cold.3
- ___cficu_ucal_isWeekend.cold.2
- ___cficu_ucal_isWeekend.cold.3
- ___cficu_ucal_open.cold.2
- ___cficu_ucal_open.cold.3
- ___cficu_ucal_roll.cold.2
- ___cficu_ucal_roll.cold.3
- ___cficu_ucal_set.cold.2
- ___cficu_ucal_set.cold.3
- ___cficu_ucal_setAttribute.cold.2
- ___cficu_ucal_setAttribute.cold.3
- ___cficu_ucal_setGregorianChange.cold.2
- ___cficu_ucal_setGregorianChange.cold.3
- ___cficu_ucal_setMillis.cold.2
- ___cficu_ucal_setMillis.cold.3
- ___cficu_ucal_setTimeZone.cold.2
- ___cficu_ucal_setTimeZone.cold.3
- ___cficu_ucurr_getDefaultFractionDigits.cold.1
- ___cficu_ucurr_getRoundingIncrement.cold.1
- ___cficu_udat_applyPattern.cold.1
- ___cficu_udat_applyPatternRelative.cold.1
- ___cficu_udat_clone.cold.1
- ___cficu_udat_close.cold.1
- ___cficu_udat_countSymbols.cold.1
- ___cficu_udat_format.cold.1
- ___cficu_udat_formatForFields.cold.1
- ___cficu_udat_get2DigitYearStart.cold.1
- ___cficu_udat_getCalendar.cold.1
- ___cficu_udat_getContext.cold.1
- ___cficu_udat_getSymbols.cold.1
- ___cficu_udat_isLenient.cold.1
- ___cficu_udat_open.cold.1
- ___cficu_udat_parseCalendar.cold.1
- ___cficu_udat_set2DigitYearStart.cold.1
- ___cficu_udat_setCalendar.cold.1
- ___cficu_udat_setContext.cold.1
- ___cficu_udat_setLenient.cold.1
- ___cficu_udat_setSymbols.cold.1
- ___cficu_udat_toPattern.cold.1
- ___cficu_udat_toPatternRelativeDate.cold.1
- ___cficu_udat_toPatternRelativeTime.cold.1
- ___cficu_udatpg_close.cold.1
- ___cficu_udatpg_getBestPattern.cold.1
- ___cficu_udatpg_getSkeleton.cold.1
- ___cficu_udatpg_open.cold.1
- ___cficu_ulistfmt_close.cold.1
- ___cficu_ulistfmt_format.cold.1
- ___cficu_ulistfmt_open.cold.1
- ___cficu_unum_applyPattern.cold.1
- ___cficu_unum_close.cold.1
- ___cficu_unum_formatDecimal.cold.1
- ___cficu_unum_formatDouble.cold.1
- ___cficu_unum_getAttribute.cold.1
- ___cficu_unum_getContext.cold.1
- ___cficu_unum_getDoubleAttribute.cold.1
- ___cficu_unum_getSymbol.cold.1
- ___cficu_unum_getTextAttribute.cold.1
- ___cficu_unum_open.cold.1
- ___cficu_unum_parse.cold.1
- ___cficu_unum_parseDecimal.cold.1
- ___cficu_unum_setAttribute.cold.1
- ___cficu_unum_setContext.cold.1
- ___cficu_unum_setDoubleAttribute.cold.1
- ___cficu_unum_setSymbol.cold.1
- ___cficu_unum_setTextAttribute.cold.1
- ___cficu_unum_toPattern.cold.1
- ___cficu_ureldatefmt_close.cold.1
- ___cficu_ureldatefmt_format.cold.1
- ___cficu_ureldatefmt_formatNumeric.cold.1
- ___cficu_ureldatefmt_open.cold.1
- _atexit
- _fputs
- _generationByPrefix
- _lastStackPointerVariableNamesByPrefix
- _stackPointersByPrefix
- _u_strlen
- _variableNamesByHeapPointer
CStrings:
+ "@\"NSObject<OS_voucher>\""
+ "LanguageAwareStringStatisticalLocalizedStringWithFormat"
+ "cachedUseLaunchPersona"
+ "lastCheckedVoucher"
- "\t%s\n"
- "#define TEMP_UCHAR%ld(str) u_uastrncpy(tempBuffer%ld, str, TEMP_BUFFER_SIZE)"
- "#include <float.h>"
- "#include <math.h>"
- "#include <stdio.h>"
- "#include <unicode/ucal.h>"
- "#include <unicode/ucurr.h>"
- "#include <unicode/udat.h>"
- "#include <unicode/udatpg.h>"
- "#include <unicode/unum.h>"
- "#include <unicode/ustdio.h>"
- "#include <unicode/ustring.h>"
- "#warning non-NULL UFieldPositionIterator ignored"
- "#warning non-NULL parseErr ignored"
- "#warning non-NULL parseError ignored"
- "#warning non-NULL pos ignored."
- "#warning non-NULL position ignored"
- "%@%ld"
- "%@,"
- "%d,"
- "%f"
- "&%@"
- "(ERROR: %s)"
- "-INFINITY"
- "// "
- "// ERROR: %s"
- "// cc %s -o test_program -licucore"
- "<unknown UCalendarAttribute>"
- "<unknown UCalendarDateFields>"
- "<unknown UCalendarDaysOfWeek>"
- "<unknown UCalendarLimitType>"
- "<unknown UCalendarType>"
- "<unknown UDateFormatStyle>"
- "<unknown UDateFormatSymbolType>"
- "<unknown UDateRelativeDateTimeFormatterStyle>"
- "<unknown UDisplayContext>"
- "<unknown UDisplayContextType>"
- "<unknown UNumberFormatAttribute>"
- "<unknown UNumberFormatStyle>"
- "<unknown UNumberFormatSymbol>"
- "<unknown UNumberFormatTextAttribute>"
- "<unknown URelativeDateTimeUnit>"
- "<unknown variable for %s>"
- "<unloggable message>\n"
- "CFICULogging"
- "CFICULogging: Logging to %s.\n"
- "CFICULogging: error: Failed to open %s.\n"
- "CFNETWORK_LIBRARY_PATH"
- "INFINITY"
- "NAN"
- "NULL"
- "TEMP_UCHAR%d(\"%@\")"
- "UCAL_ACTUAL_MAXIMUM"
- "UCAL_ACTUAL_MINIMUM"
- "UCAL_AM_PM"
- "UCAL_DAY_OF_MONTH"
- "UCAL_DAY_OF_WEEK"
- "UCAL_DAY_OF_WEEK_IN_MONTH"
- "UCAL_DAY_OF_YEAR"
- "UCAL_DOW_LOCAL"
- "UCAL_DST_OFFSET"
- "UCAL_ERA"
- "UCAL_EXTENDED_YEAR"
- "UCAL_FIELD_COUNT"
- "UCAL_FIRST_DAY_OF_WEEK"
- "UCAL_FRIDAY"
- "UCAL_GREATEST_MINIMUM"
- "UCAL_GREGORIAN"
- "UCAL_HOUR"
- "UCAL_HOUR_OF_DAY"
- "UCAL_IS_LEAP_MONTH"
- "UCAL_IS_REPEATED_DAY"
- "UCAL_JULIAN_DAY"
- "UCAL_LEAST_MAXIMUM"
- "UCAL_LENIENT"
- "UCAL_MAXIMUM"
- "UCAL_MILLISECOND"
- "UCAL_MILLISECONDS_IN_DAY"
- "UCAL_MINIMAL_DAYS_IN_FIRST_WEEK"
- "UCAL_MINIMUM"
- "UCAL_MINUTE"
- "UCAL_MONDAY"
- "UCAL_MONTH"
- "UCAL_REPEATED_WALL_TIME"
- "UCAL_SATURDAY"
- "UCAL_SECOND"
- "UCAL_SKIPPED_WALL_TIME"
- "UCAL_SUNDAY"
- "UCAL_THURSDAY"
- "UCAL_TRADITIONAL"
- "UCAL_TUESDAY"
- "UCAL_WEDNESDAY"
- "UCAL_WEEKDAY"
- "UCAL_WEEKEND"
- "UCAL_WEEKEND_CEASE"
- "UCAL_WEEKEND_ONSET"
- "UCAL_WEEK_OF_MONTH"
- "UCAL_WEEK_OF_YEAR"
- "UCAL_YEAR"
- "UCAL_YEAR_WOY"
- "UCAL_ZONE_OFFSET"
- "UCalendar *%@ = ucal_clone(%@, &%@); %@"
- "UCalendar *%@ = ucal_open(%@, %d, \"%s\", %s, &%@); %@"
- "UChar %@[%d];"
- "UChar tempBuffer%ld[TEMP_BUFFER_SIZE];"
- "UChar* const %@[%d] = {"
- "UDAT_AM_PMS"
- "UDAT_ERAS"
- "UDAT_ERA_NAMES"
- "UDAT_FULL"
- "UDAT_IGNORE"
- "UDAT_LOCALIZED_CHARS"
- "UDAT_LONG"
- "UDAT_LONG_RELATIVE"
- "UDAT_MEDIUM"
- "UDAT_MEDIUM_RELATIVE"
- "UDAT_MONTHS"
- "UDAT_NARROW_MONTHS"
- "UDAT_NARROW_WEEKDAYS"
- "UDAT_NONE"
- "UDAT_QUARTERS"
- "UDAT_RELATIVE"
- "UDAT_REL_UNIT_DAY"
- "UDAT_REL_UNIT_HOUR"
- "UDAT_REL_UNIT_MINUTE"
- "UDAT_REL_UNIT_MONTH"
- "UDAT_REL_UNIT_SECOND"
- "UDAT_REL_UNIT_WEEK"
- "UDAT_REL_UNIT_YEAR"
- "UDAT_SHORT"
- "UDAT_SHORTER_WEEKDAYS"
- "UDAT_SHORT_MONTHS"
- "UDAT_SHORT_QUARTERS"
- "UDAT_SHORT_RELATIVE"
- "UDAT_SHORT_WEEKDAYS"
- "UDAT_STANDALONE_MONTHS"
- "UDAT_STANDALONE_NARROW_MONTHS"
- "UDAT_STANDALONE_NARROW_WEEKDAYS"
- "UDAT_STANDALONE_QUARTERS"
- "UDAT_STANDALONE_SHORTER_WEEKDAYS"
- "UDAT_STANDALONE_SHORT_MONTHS"
- "UDAT_STANDALONE_SHORT_QUARTERS"
- "UDAT_STANDALONE_SHORT_WEEKDAYS"
- "UDAT_STANDALONE_WEEKDAYS"
- "UDAT_STYLE_LONG"
- "UDAT_STYLE_NARROW"
- "UDAT_STYLE_SHORT"
- "UDAT_WEEKDAYS"
- "UDISPCTX_CAPITALIZATION_FOR_BEGINNING_OF_SENTENCE"
- "UDISPCTX_CAPITALIZATION_FOR_MIDDLE_OF_SENTENCE"
- "UDISPCTX_CAPITALIZATION_FOR_STANDALONE"
- "UDISPCTX_CAPITALIZATION_FOR_UI_LIST_OR_MENU"
- "UDISPCTX_CAPITALIZATION_NONE"
- "UDISPCTX_TYPE_CAPITALIZATION"
- "UDISPCTX_TYPE_DIALECT_HANDLING"
- "UDateFormat *%@ = udat_clone(%@, &%@); %@"
- "UDateFormat *%@ = udat_open(%s, %s, \"%s\", %@, %d, %@, %d, &%@); %@"
- "UDateTimePatternGenerator *%@ = udatpg_open(\"%s\", &%@); %@"
- "UDisplayContext %@ = udat_getContext(%@, %s, %@); %@"
- "UErrorCode %@ = U_ZERO_ERROR;"
- "UListFormatter *%@ = ulistfmt_open(\"%s\", &%@); %@"
- "UNUM_CURRENCY"
- "UNUM_CURRENCY_CODE"
- "UNUM_CURRENCY_ISO"
- "UNUM_CURRENCY_PLURAL"
- "UNUM_CURRENCY_SYMBOL"
- "UNUM_DECIMAL"
- "UNUM_DECIMAL_ALWAYS_SHOWN"
- "UNUM_DECIMAL_SEPARATOR_SYMBOL"
- "UNUM_DEFAULT_RULESET"
- "UNUM_DIGIT_SYMBOL"
- "UNUM_DURATION"
- "UNUM_EIGHT_DIGIT_SYMBOL"
- "UNUM_EXPONENTIAL_SYMBOL"
- "UNUM_FIVE_DIGIT_SYMBOL"
- "UNUM_FORMAT_FAIL_IF_MORE_THAN_MAX_DIGITS"
- "UNUM_FORMAT_STYLE_COUNT"
- "UNUM_FORMAT_SYMBOL_COUNT"
- "UNUM_FORMAT_WIDTH"
- "UNUM_FOUR_DIGIT_SYMBOL"
- "UNUM_FRACTION_DIGITS"
- "UNUM_GROUPING_SEPARATOR_SYMBOL"
- "UNUM_GROUPING_SIZE"
- "UNUM_GROUPING_USED"
- "UNUM_INFINITY_SYMBOL"
- "UNUM_INTEGER_DIGITS"
- "UNUM_INTL_CURRENCY_SYMBOL"
- "UNUM_LENIENT_PARSE"
- "UNUM_LIMIT_BOOLEAN_ATTRIBUTE"
- "UNUM_MAX_FRACTION_DIGITS"
- "UNUM_MAX_INTEGER_DIGITS"
- "UNUM_MAX_NONBOOLEAN_ATTRIBUTE"
- "UNUM_MAX_SIGNIFICANT_DIGITS"
- "UNUM_MINUS_SIGN_SYMBOL"
- "UNUM_MIN_FRACTION_DIGITS"
- "UNUM_MIN_INTEGER_DIGITS"
- "UNUM_MIN_SIGNIFICANT_DIGITS"
- "UNUM_MONETARY_GROUPING_SEPARATOR_SYMBOL"
- "UNUM_MONETARY_SEPARATOR_SYMBOL"
- "UNUM_MULTIPLIER"
- "UNUM_NAN_SYMBOL"
- "UNUM_NEGATIVE_PREFIX"
- "UNUM_NEGATIVE_SUFFIX"
- "UNUM_NINE_DIGIT_SYMBOL"
- "UNUM_NUMBERING_SYSTEM"
- "UNUM_ONE_DIGIT_SYMBOL"
- "UNUM_ORDINAL"
- "UNUM_PADDING_CHARACTER"
- "UNUM_PADDING_POSITION"
- "UNUM_PAD_ESCAPE_SYMBOL"
- "UNUM_PARSE_ALL_INPUT"
- "UNUM_PARSE_INT_ONLY"
- "UNUM_PARSE_NO_EXPONENT"
- "UNUM_PATTERN_DECIMAL"
- "UNUM_PATTERN_RULEBASED"
- "UNUM_PATTERN_SEPARATOR_SYMBOL"
- "UNUM_PERCENT"
- "UNUM_PERCENT_SYMBOL"
- "UNUM_PERMILL_SYMBOL"
- "UNUM_PLUS_SIGN_SYMBOL"
- "UNUM_POSITIVE_PREFIX"
- "UNUM_POSITIVE_SUFFIX"
- "UNUM_PUBLIC_RULESETS"
- "UNUM_ROUNDING_INCREMENT"
- "UNUM_ROUNDING_MODE"
- "UNUM_SCIENTIFIC"
- "UNUM_SECONDARY_GROUPING_SIZE"
- "UNUM_SEVEN_DIGIT_SYMBOL"
- "UNUM_SIGNIFICANT_DIGITS_USED"
- "UNUM_SIGNIFICANT_DIGIT_SYMBOL"
- "UNUM_SIX_DIGIT_SYMBOL"
- "UNUM_SPELLOUT"
- "UNUM_THREE_DIGIT_SYMBOL"
- "UNUM_TWO_DIGIT_SYMBOL"
- "UNUM_ZERO_DIGIT_SYMBOL"
- "UNumberFormat *%@ = unum_open(%s, %@, %d, \"%s\", NULL, &%@); %@"
- "URelativeDateTimeFormatter *%@ = ureldatefmt_open(\"%s\", %@, %s, %s, &%@); %@"
- "cal"
- "char %@[%d];"
- "checkedProcessCanHaveMultiplePersonas"
- "const UCalendar *%@ = udat_getCalendar(%@);"
- "cxt"
- "dateFmt"
- "dtpg"
- "int TEMP_BUFFER_SIZE = 500;"
- "int main(int argc, char *argv[]) {"
- "int32_t %@ = %d;"
- "int32_t %@[%d] = {"
- "listFmt"
- "numFmt"
- "parsePos"
- "pattern"
- "relDateFmt"
- "result"
- "return 0;"
- "skeleton"
- "status"
- "stdout"
- "stringLengths"
- "temp"
- "u_printf(\"%@: '%%S'\\n\", %@);"
- "ucal_add(%@, %s, %d, &%@); %@"
- "ucal_clear(%@);"
- "ucal_close(%@);"
- "ucal_get(%@, %s, &%@); // %d %@"
- "ucal_getAttribute(%@, %s); // %d"
- "ucal_getDayOfWeekType(%@, %s, &%@); // %s %@"
- "ucal_getFieldDifference(%@, %@, %s, &%@); // %d %@"
- "ucal_getGregorianChange(%@, &%@); // %f %@"
- "ucal_getLimit(%@, %s, %s, &%@); // %d %@"
- "ucal_getMillis(%@, &%@); // %f %@"
- "ucal_getWeekendTransition(%@, %s, &%@); // %d %@"
- "ucal_isWeekend(%@, %@, &%@); // %d %@"
- "ucal_roll(%@, %s, %d, &%@); %@"
- "ucal_set(%@, %s, %d);"
- "ucal_setAttribute(%@, %s, %d);"
- "ucal_setGregorianChange(%@, %@, &%@); %@"
- "ucal_setMillis(%@, %@, &%@); %@"
- "ucal_setTimeZone(%@, %@, %d, &%@); %@"
- "ucurr_getDefaultFractionDigits(%@, &%@); // %d %@"
- "ucurr_getRoundingIncrement(%@, &%@); // %d %@"
- "udat_applyPattern(%@, %d, %@, %d);"
- "udat_applyPatternRelative(%@, %@, %d, %@, %d, &%@); %@"
- "udat_close(%@);"
- "udat_countSymbols(%@, %s); // %d"
- "udat_format(%@, %@, %@, %d, NULL, &%@); // %d %@ %@"
- "udat_get2DigitYearStart(%@, &%@); // %f %@"
- "udat_getSymbols(%@, %s, %d, %@, %d, &%@); // %d %@ %@"
- "udat_isLenient(%@); // %d"
- "udat_parseCalendar(%@, %@, %@, %d, %@, &%@); // %d %@"
- "udat_set2DigitYearStart(%@, %@, &%@); %@"
- "udat_setCalendar(%@, %@);"
- "udat_setContext(%@, %s, %@); %@"
- "udat_setLenient(%@, %d);"
- "udat_setSymbols(%@, %s, %d, %@, %d, &%@); %@"
- "udat_toPattern(%@, %d, %@, %d, &%@); // %d %@ %@"
- "udat_toPatternRelativeDate(%@,  %@, %d, &%@); // %d %@ %@"
- "udat_toPatternRelativeTime(%@,  %@, %d, &%@); // %d %@ %@"
- "udatpg_close(%@);"
- "udatpg_getBestPattern(%@, %@, %d, %@, %d, &%@); // %d %@ %@"
- "udatpg_getSkeleton(%@, %@, %d, %@, %d, &%@); // %d %@ %@"
- "ulistfmt_close(%@);"
- "ulistfmt_format(%@, %@, %@, %d, %@, %d, &%@); // %d %@  %@"
- "unum_applyPattern(%@, %d, %@, %d, NULL, &%@); %@"
- "unum_close(%@);"
- "unum_formatDecimal(%@, \"%@\", %d, %@, %d, NULL, &%@); %@"
- "unum_formatDouble(%@, %@, %@, %d, NULL, &%@); %@"
- "unum_getAttribute(%@, %s); // %d"
- "unum_getAttribute(%@, %s); // %f"
- "unum_getContext(%@, %d, &%@); // %d"
- "unum_getSymbol(%@, %s, %@, %d, &%@); // %d %@ %@"
- "unum_getTextAttribute(%@, %s, %@, %d, &%@); // %d %@ %@"
- "unum_parse(%@, %@, %d, %@, &%@); // %d %@"
- "unum_parseDecimal(%@, %@, %d, %@, %@, %d, &%@); // %d %@ %@"
- "unum_setAttribute(%@, %s, %d);"
- "unum_setContext(%@, %d, &%@);"
- "unum_setDoubleAttribute(%@, %s, %@);"
- "unum_setSymbol(%@, %s, %@, %d, &%@); %@"
- "unum_setTextAttribute(%@, %s, %@, %d, &%@); %@"
- "unum_toPattern(%@, %d, %@, %d, &%@); // %d %@ %@"
- "ureldatefmt_close(%@);"
- "ureldatefmt_formatNumeric(%@, %lf, %s, %@, %d, &%@); // %d, %@, %@"
- "};\n"

```
