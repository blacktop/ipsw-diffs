## ClockKit

> `/System/iOSSupport/System/Library/Frameworks/ClockKit.framework/Versions/A/ClockKit`

```diff

-2483.115.0.0.0
-  __TEXT.__text: 0x6d3b8
-  __TEXT.__auth_stubs: 0xfa0
-  __TEXT.__objc_methlist: 0x8f74
-  __TEXT.__const: 0xb1a
-  __TEXT.__cstring: 0x3ff2
-  __TEXT.__oslogstring: 0x252e
-  __TEXT.__gcc_except_tab: 0xf84
-  __TEXT.__dlopen_cstrs: 0x162
+2483.147.65.0.0
+  __TEXT.__text: 0x6c490
+  __TEXT.__auth_stubs: 0xf90
+  __TEXT.__objc_methlist: 0x93ec
+  __TEXT.__const: 0xb7a
+  __TEXT.__cstring: 0x3ec2
+  __TEXT.__oslogstring: 0x26f5
+  __TEXT.__gcc_except_tab: 0xee0
   __TEXT.__ustring: 0x7c
+  __TEXT.__dlopen_cstrs: 0xfe
   __TEXT.__constg_swiftt: 0x184
-  __TEXT.__swift5_typeref: 0x17f
+  __TEXT.__swift5_typeref: 0x180
   __TEXT.__swift5_reflstr: 0x95
   __TEXT.__swift5_fieldmd: 0x110
   __TEXT.__swift5_builtin: 0x3c

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x2438
-  __TEXT.__eh_frame: 0x118
+  __TEXT.__unwind_info: 0x23a0
+  __TEXT.__eh_frame: 0x1d0
   __TEXT.__objc_classname: 0x1e30
-  __TEXT.__objc_methname: 0xf0d5
+  __TEXT.__objc_methname: 0xf0fb
   __TEXT.__objc_methtype: 0x1b6f
-  __TEXT.__objc_stubs: 0x8c80
-  __DATA_CONST.__got: 0x710
-  __DATA_CONST.__const: 0x1bc8
+  __TEXT.__objc_stubs: 0x8c20
+  __DATA_CONST.__got: 0x730
+  __DATA_CONST.__const: 0x1b60
   __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3308
+  __DATA_CONST.__objc_selrefs: 0x3388
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x498
   __DATA_CONST.__objc_arraydata: 0x4f0
-  __AUTH_CONST.__auth_got: 0x7e0
+  __AUTH_CONST.__auth_got: 0x7d8
   __AUTH_CONST.__const: 0xff0
-  __AUTH_CONST.__cfstring: 0x5200
-  __AUTH_CONST.__objc_const: 0x12010
+  __AUTH_CONST.__cfstring: 0x51c0
+  __AUTH_CONST.__objc_const: 0x11860
   __AUTH_CONST.__objc_intobj: 0xb70
   __AUTH_CONST.__objc_doubleobj: 0x350
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x3950
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0xab0
+  __DATA.__objc_ivar: 0xab4
   __DATA.__data: 0x760
-  __DATA.__bss: 0xd40
+  __DATA.__bss: 0xcb0
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 9AA5FB66-61B6-36C9-98E2-914C05A49FC0
-  Functions: 3768
-  Symbols:   8285
+  UUID: 0603C0D3-A089-3519-891C-81E4EBD3BCD0
+  Functions: 3781
+  Symbols:   8309
   CStrings:  4435
 
Symbols:
+ +[CLKClockTimer sharedInstance].cold.1
+ +[CLKComplicationClientManager sharedClientManager].cold.1
+ +[CLKComplicationDescriptor allowedDictionaryClasses].cold.1
+ +[CLKComplicationTemplate(JSONSerialization) classesCompatibleWithJSONSerialization].cold.1
+ +[CLKCompoundTextProvider compoundTextProviderCurrentlyFormattingOnThisThread].cold.1
+ +[CLKDevice currentDevice].cold.1
+ +[CLKDevice resetCurrentDevice].cold.1
+ +[CLKFullColorImageProvider fullColorImageProviderWithJSONObjectRepresentation:bundle:].cold.1
+ +[CLKImageProvider imageProviderWithJSONObjectRepresentation:bundle:].cold.1
+ +[CLKRenderingContext sharedRenderingContext].cold.1
+ +[CLKTreatedImageCache sharedInstance].cold.1
+ +[CLKVideo(private) _videoNamed:device:bundle:modifier:].cold.1
+ +[CLKWorldClockTimeFormatter differenceForOffset:caps:suppressZero:size:].cold.1
+ +[_CLKTimeFormatData _timeFormatDataAccessLock].cold.1
+ -[CLKComplicationTemplate initWithCoder:].cold.1
+ -[CLKComplicationTemplateGraphicBezelCircularText _validEmbeddedTemplateClassNamesForKey:].cold.1
+ -[CLKCompoundTextProvider _processFormat:arguments:].cold.1
+ -[CLKCompoundTextProvider _processFormat:arguments:].cold.2
+ -[CLKCompoundTextProvider _processFormat:arguments:].cold.3
+ -[CLKDevice productTypeFromProductTypeString:].cold.1
+ -[CLKDevice setSupportsCharon:]
+ -[CLKDevice supportsCharon]
+ -[CLKDeviceMetrics _effectiveSizeClass].cold.1
+ -[CLKDeviceMetrics initWithDevice:identitySizeClass:].cold.1
+ -[CLKSensitiveUIMonitor _isVendorRelease].cold.1
+ -[NSString(CLKFormatter) _clkBlinkerRangeByBackwardsSearch].cold.1
+ -[NSString(CLKFormatter) _clkBlinkerRange].cold.1
+ CLKBuildVersion.cold.1
+ CLKBundle.cold.1
+ CLKCompanionDisplayDate.cold.1
+ CLKComplicationClientInterface.cold.1
+ CLKComplicationServerInterface.cold.1
+ CLKDatesHaveSameTimeDesignatorPeriod.cold.1
+ CLKDebugCompanionDisplayDateOverride.cold.1
+ CLKDesignatorRequiresWhitespace.cold.1
+ CLKDropLeftRedundantDesignator.cold.1
+ CLKForcedTime.cold.1
+ CLKInternalBuild.cold.1
+ CLKIsBridge.cold.1
+ CLKIsCLKCompanionWatchFaceLibraryServiceProcess.cold.1
+ CLKIsClockFaceApp.cold.1
+ CLKIsCreateWatchFace.cold.1
+ CLKIsCurrentLocaleCJK.cold.1
+ CLKIsCurrentLocaleNonLatin.cold.1
+ CLKIsFaceSnapshotService.cold.1
+ CLKIsGreenfieldTool.cold.1
+ CLKIsNTKCLITool.cold.1
+ CLKIsNTKDaemon.cold.1
+ CLKIsNTKXCTests.cold.1
+ CLKIsUVPreviewApp.cold.1
+ CLKLanguageIsTallScript.cold.1
+ CLKLayoutIsRTL.cold.1
+ CLKLocaleCurrentNumberSystem.cold.1
+ CLKLocaleNumberSystemPrefix.cold.1
+ CLKLoggingObjectForDomain.cold.1
+ CLKRemovesPunctuationFromWeekdayDay.cold.1
+ CLKRequestConcreteImplementation.cold.2
+ CLKRunningInProcess.cold.1
+ CLKRunningInProcess.cold.2
+ CLKRunningInProcess.cold.3
+ CLKRunningInProcess.cold.4
+ CLKRunningInProcess.cold.5
+ CLKRunningInProcess.cold.6
+ CLKRunningInProcess.cold.7
+ CLKRunningInProcess.cold.8
+ CLKSmallCapsAllowed.cold.1
+ CLKUsesFauxSmallCaps.cold.1
+ CLKWatchFaceLibraryServerInterface.cold.1
+ GCC_except_table1029
+ GCC_except_table109
+ GCC_except_table114
+ GCC_except_table115
+ GCC_except_table29
+ GCC_except_table50
+ GCC_except_table62
+ GCC_except_table63
+ GCC_except_table71
+ GCC_except_table75
+ OBJC_IVAR_$_CLKDevice._supportsCharon
+ _AlternatePunctuationAttributes.cold.1
+ _BoxedComplicationFamiliesByName.cold.1
+ __41-[CLKComplicationTemplate initWithCoder:]_block_invoke.114
+ __43-[CLKComplicationTemplate encodeWithCoder:]_block_invoke.106
+ ___block_descriptor_56_e8_32s40r_e79_v104?0"NSString"8B16B20{CGSize=dd}24{CGSize=dd}40d56{UIEdgeInsets=dddd}64^B96ls32l8r40l8
+ __block_literal_global.1358
+ __block_literal_global.1415
+ __block_literal_global.1624
+ __block_literal_global.343
+ __block_literal_global.369
+ __block_literal_global.388
+ __block_literal_global.427
+ __block_literal_global.468
+ __block_literal_global.518
+ __block_literal_global.542
+ __block_literal_global.583
+ __block_literal_global.660
+ __block_literal_global.694
+ __block_literal_global.776
+ __block_literal_global.788
+ __block_literal_global.809
+ __block_literal_global.834
+ __block_literal_global.868
+ __block_literal_global.918
+ __block_literal_global.936
+ __block_literal_global.948
+ __block_literal_global.973
+ __block_literal_global.993
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1147
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1178
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1209
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1231
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1246
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1266
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1312
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1345
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1366
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1386
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1401
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1460
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1481
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1497
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1516
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1530
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1550
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1593
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1613
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1632
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1650
+ _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1663
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1146
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1177
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1208
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1230
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1245
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1265
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1311
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1344
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1365
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1385
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1400
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1459
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1480
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1496
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1515
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1529
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1549
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1592
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1612
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1631
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1649
+ _enumerateFullColorImageProviderKeysWithBlock:.__lock.1662
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1148
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1179
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1210
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1232
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1247
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1267
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1313
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1346
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1367
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1387
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1402
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1461
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1482
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1498
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1517
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1531
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1551
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1594
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1614
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1633
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1651
+ _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1664
+ _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1144
+ _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1175
+ _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1206
+ _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1228
+ _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1243
+ _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1263
+ _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1309
+ _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1342
+ _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1383
+ _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1398
+ _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1478
+ _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1494
+ _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1513
+ _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1547
+ _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1590
+ _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1610
+ _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1647
+ _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1660
+ _enumerateFullColorImageProviderKeysWithBlock:._imageSize.1458
+ _enumerateFullColorImageProviderKeysWithBlock:._imageSize.1528
+ _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1145
+ _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1176
+ _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1207
+ _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1229
+ _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1244
+ _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1264
+ _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1310
+ _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1343
+ _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1384
+ _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1399
+ _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1479
+ _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1495
+ _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1514
+ _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1548
+ _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1591
+ _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1611
+ _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1648
+ _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1661
+ _imageSDKSize:deviceSize:forSDKVersion:.__cachedDevice.902
+ _imageSDKSize:deviceSize:forSDKVersion:.__lock.901
+ _imageSDKSize:deviceSize:forSDKVersion:.__previousCLKDeviceVersion.903
+ _imageSDKSize:deviceSize:forSDKVersion:._imageSize.900
- ComplicationDisplayLibraryCore.frameworkLibrary
- GCC_except_table1030
- GCC_except_table1055
- GCC_except_table112
- GCC_except_table1152
- GCC_except_table120
- GCC_except_table30
- GCC_except_table34
- GCC_except_table51
- GCC_except_table58
- GCC_except_table64
- GCC_except_table65
- GCC_except_table76
- _ComplicationDisplayLibrary
- _ComplicationDisplayLibraryCore
- __101-[CLKComplicationTemplateGraphicRectangularLargeImage _enumerateFullColorImageProviderKeysWithBlock:]_block_invoke_2.cold.1
- __101-[CLKComplicationTemplateGraphicRectangularLargeImage _enumerateFullColorImageProviderKeysWithBlock:]_block_invoke_2.cold.2
- __101-[CLKComplicationTemplateGraphicRectangularLargeImage _enumerateFullColorImageProviderKeysWithBlock:]_block_invoke_2.cold.3
- __103-[CLKComplicationTemplateGraphicExtraLargeCircularImage _enumerateFullColorImageProviderKeysWithBlock:]_block_invoke_2.cold.1
- __41-[CLKComplicationTemplate initWithCoder:]_block_invoke.122
- __43-[CLKComplicationTemplate encodeWithCoder:]_block_invoke.114
- __EnumerateCalendarUnitsBackwardWithBlock
- __EnumerateCalendarUnitsWithBlock
- ___101-[CLKComplicationTemplateGraphicRectangularLargeImage _enumerateFullColorImageProviderKeysWithBlock:]_block_invoke
- ___101-[CLKComplicationTemplateGraphicRectangularLargeImage _enumerateFullColorImageProviderKeysWithBlock:]_block_invoke_2
- ___103-[CLKComplicationTemplateGraphicExtraLargeCircularImage _enumerateFullColorImageProviderKeysWithBlock:]_block_invoke
- ___103-[CLKComplicationTemplateGraphicExtraLargeCircularImage _enumerateFullColorImageProviderKeysWithBlock:]_block_invoke_2
- ___45-[CLKComplicationTemplate validateWithError:]_block_invoke_10
- ___ComplicationDisplayLibraryCore_block_invoke
- ___block_descriptor_40_e8_32r_e11_v24?0d8d16lr32l8
- ___block_descriptor_48_e8_32s_e26_d16?0"CLKDeviceMetrics"8ls32l8
- ___block_descriptor_72_e8_32s40r48r56r_e79_v104?0"NSString"8B16B20{CGSize=dd}24{CGSize=dd}40d56{UIEdgeInsets=dddd}64^B96ls32l8r40l8r48l8r56l8
- ___getCDCircularMediumComplicationDiameterSymbolLoc_block_invoke
- ___getCDGraphicLargeRectangularComplicationInsetSymbolLoc_block_invoke
- ___getCDGraphicLargeRectangularComplicationLargeImageHeightSymbolLoc_block_invoke
- ___getCDGraphicLargeRectangularComplicationSizeSymbolLoc_block_invoke
- ___get_ClientRendererClass_block_invoke
- __block_literal_global.1001
- __block_literal_global.1366
- __block_literal_global.1423
- __block_literal_global.1647
- __block_literal_global.351
- __block_literal_global.377
- __block_literal_global.396
- __block_literal_global.435
- __block_literal_global.476
- __block_literal_global.526
- __block_literal_global.550
- __block_literal_global.578
- __block_literal_global.668
- __block_literal_global.702
- __block_literal_global.784
- __block_literal_global.804
- __block_literal_global.817
- __block_literal_global.850
- __block_literal_global.876
- __block_literal_global.926
- __block_literal_global.944
- __block_literal_global.972
- __block_literal_global.989
- __get_ClientRendererClass_block_invoke.cold.1
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_ClockKit
- _audit_stringComplicationDisplay
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1155
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1186
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1217
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1239
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1254
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1274
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1320
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1353
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1374
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1394
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1409
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1468
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1482
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1498
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1514
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1533
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1547
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1567
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1592
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1616
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1636
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1655
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1673
- _enumerateFullColorImageProviderKeysWithBlock:.__cachedDevice.1686
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1154
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1185
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1216
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1238
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1253
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1273
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1319
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1352
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1373
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1393
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1408
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1467
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1481
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1497
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1513
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1532
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1546
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1566
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1591
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1615
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1635
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1654
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1672
- _enumerateFullColorImageProviderKeysWithBlock:.__lock.1685
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1156
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1187
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1218
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1240
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1255
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1275
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1321
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1354
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1375
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1395
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1410
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1469
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1483
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1499
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1515
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1534
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1548
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1568
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1593
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1617
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1637
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1656
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1674
- _enumerateFullColorImageProviderKeysWithBlock:.__previousCLKDeviceVersion.1687
- _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1152
- _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1183
- _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1214
- _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1236
- _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1251
- _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1271
- _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1317
- _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1350
- _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1391
- _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1406
- _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1495
- _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1511
- _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1530
- _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1564
- _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1589
- _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1613
- _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1633
- _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1670
- _enumerateFullColorImageProviderKeysWithBlock:._imageDiameter.1683
- _enumerateFullColorImageProviderKeysWithBlock:._imageSize.1466
- _enumerateFullColorImageProviderKeysWithBlock:._imageSize.1480
- _enumerateFullColorImageProviderKeysWithBlock:._imageSize.1545
- _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1153
- _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1184
- _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1215
- _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1237
- _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1252
- _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1272
- _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1318
- _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1351
- _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1392
- _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1407
- _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1496
- _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1512
- _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1531
- _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1565
- _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1590
- _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1614
- _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1634
- _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1671
- _enumerateFullColorImageProviderKeysWithBlock:._pointSize.1684
- _imageSDKSize:deviceSize:forSDKVersion:.__cachedDevice.910
- _imageSDKSize:deviceSize:forSDKVersion:.__lock.909
- _imageSDKSize:deviceSize:forSDKVersion:.__previousCLKDeviceVersion.911
- _imageSDKSize:deviceSize:forSDKVersion:._imageSize.908
- _objc_msgSend$renderForPreviews
- _objc_msgSend$renderWithViewData:scale:handler:
- _objc_msgSend$viewDataForSwiftUIViewKey:
- _objc_release_x10
- getCDCircularMediumComplicationDiameterSymbolLoc.ptr
- getCDGraphicLargeRectangularComplicationInsetSymbolLoc.ptr
- getCDGraphicLargeRectangularComplicationLargeImageHeightSymbolLoc.ptr
- getCDGraphicLargeRectangularComplicationSizeSymbolLoc.ptr
- get_ClientRendererClass.softClass
CStrings:
+ "%@ - %s, _allHandlers.count = %lu"
+ "-[CLKClockTimer _updateIsPermittedToRun]"
+ "-[CLKClockTimer startUpdatesWithUpdateFrequency:withHandler:identificationLog:]"
+ "-[CLKClockTimer stopUpdatesForToken:]"
+ "CLKDevice supportsCharon: %u"
+ "Invalid SDK version %ld - resetting to jupiter or later"
+ "No update %@ - %s, _allHandlers.count = %lu, shouldPermitToRun = %d, _isForeground = %d, _backlightOn = %d, _ignoreScreenState = %d"
+ "Pausing %@ - %s, _allHandlers.count = %lu, shouldPermitToRun = %d, _isForeground = %d, _backlightOn = %d, _ignoreScreenState = %d"
+ "Resuming %@ - %s, _allHandlers.count = %lu, shouldPermitToRun = %d, _isForeground = %d, _backlightOn = %d, _ignoreScreenState = %d"
+ "TB,N,V_supportsCharon"
+ "_supportsCharon"
+ "setSupportsCharon:"
+ "supportsCharon"
- "CDCircularMediumComplicationDiameter"
- "CDGraphicLargeRectangularComplicationInset"
- "CDGraphicLargeRectangularComplicationLargeImageHeight"
- "CDGraphicLargeRectangularComplicationSize"
- "CLKComplicationTemplate: Complication took %gs to render"
- "The '%@' view on %@ took more than one frame to render which is too long when using an auto-updating view. This template will be removed from the timeline."
- "The '%@' view on %@ took more than two frames to render. This template will be removed from the timeline."
- "_ClientRenderer"
- "renderWithViewData:scale:handler:"
- "softlink:o:path:/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay"
- "v24@?0d8d16"

```
