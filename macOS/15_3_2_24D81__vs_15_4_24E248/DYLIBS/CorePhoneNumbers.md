## CorePhoneNumbers

> `/System/Library/PrivateFrameworks/CorePhoneNumbers.framework/Versions/A/CorePhoneNumbers`

```diff

-525.300.111.0.0
-  __TEXT.__text: 0x7dac
+525.500.101.0.0
+  __TEXT.__text: 0x7e10
   __TEXT.__auth_stubs: 0x640
   __TEXT.__const: 0xca
-  __TEXT.__cstring: 0x30c
+  __TEXT.__cstring: 0x306
   __TEXT.__ustring: 0xa
   __TEXT.__oslogstring: 0x4a
-  __TEXT.__unwind_info: 0x1d0
+  __TEXT.__unwind_info: 0x1c8
   __TEXT.__objc_classname: 0x1
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0xc0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8AA44960-3147-359E-81F1-E6F0DE19D2B3
-  Functions: 120
-  Symbols:   289
-  CStrings:  94
+  UUID: 7812C5CD-7D63-313F-94A5-DEE800F35059
+  Functions: 124
+  Symbols:   297
+  CStrings:  92
 
Symbols:
+ CFPhoneNumberCreate.cold.1
+ CFPhoneNumberCreateCopy.cold.1
+ CFPhoneNumberGetTypeID.cold.1
+ PNGetFormatFileHeader.cold.1
+ _PNCopySampleNumberForCountry.cold.1
+ _PNCopyStrippedNumberWithoutPauses.cold.1
+ _PNSetSampleNumberForCountry.cold.1
+ cpn_default_log.cold.1
Functions:
~ _CFPhoneNumberCreate : 528 -> 512
~ _PNCopyBestGuessCountryCodeForNumber : 168 -> 164
~ _PNGetFormatFileHeader : 80 -> 72
~ __GetCountryOffsetFromDialingCode : 704 -> 688
~ _UIPhoneFormatCountryGetInfoIndex : 480 -> 476
~ __PNCopyStrippedNumberWithoutPauses : 360 -> 344
~ __PNCopyFullyQualifiedNumberForCountryInternal : 1320 -> 1348
~ __DecomposePhoneNumberWithCountryIndex : 896 -> 880
~ __NumberRangeWithoutVerticalServiceCode : 1216 -> 1212
~ _InlineBufferHasPatternAtOffset : 492 -> 508
~ __FormatEntryAndNationalPrefixForDigitsInCountry : 308 -> 312
~ __FindFormatEntryForDigitsInCountry : 1640 -> 1644
~ __CreateFormattedNumberForDigitsWithCountryIndex : 2400 -> 2420
~ __CreateFormattedStringForDigitsInRange : 2352 -> 2484
~ __PNCreateLocalizedStringWithString : 516 -> 512
~ ___CFPhoneNumberNormalize : 104 -> 112
~ _decomposedPhoneNumbersEqual : 320 -> 312
~ _cpn_default_log : 68 -> 56
~ __PNCopyIndexStringsForAddressBookSearch : 1028 -> 1040
~ __PNSetSampleNumberForCountry : 308 -> 292
~ __PNCopySampleNumberForCountry : 440 -> 424
~ _UIPhoneFormatFileGetCountryLength : 192 -> 184
~ _shouldEnableStrictEquality : 48 -> 56
~ ___InternationalPrefixForDigitsInCountry : 852 -> 828
- sub_1920c8720
~ _CFPhoneNumberGetTypeID : 68 -> 56
~ _CFPhoneNumberCreateCopy : 216 -> 200
~ _CFPhoneNumberCopyNumberForLocalAssist : 568 -> 576
CStrings:
- "00"
- "86"

```
