## VoiceOverServices

> `/System/Library/PrivateFrameworks/VoiceOverServices.framework/VoiceOverServices`

```diff

-3148.15.26.0.0
-  __TEXT.__text: 0x31f38
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_methlist: 0x2d34
-  __TEXT.__cstring: 0x6b09
+3180.6.1.0.0
+  __TEXT.__text: 0x327a0
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_methlist: 0x2dc4
+  __TEXT.__cstring: 0x6cfe
   __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0x15c
   __TEXT.__oslogstring: 0x413
   __TEXT.__dlopen_cstrs: 0xf0
-  __TEXT.__unwind_info: 0x770
+  __TEXT.__unwind_info: 0x780
   __TEXT.__objc_classname: 0x2e8
-  __TEXT.__objc_methname: 0x63f9
+  __TEXT.__objc_methname: 0x658f
   __TEXT.__objc_methtype: 0x4ac
-  __TEXT.__objc_stubs: 0x7380
+  __TEXT.__objc_stubs: 0x74e0
   __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__const: 0x638
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2048
+  __DATA_CONST.__objc_selrefs: 0x20b0
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x140
-  __AUTH_CONST.__auth_got: 0x368
-  __AUTH_CONST.__const: 0x36e0
-  __AUTH_CONST.__cfstring: 0x8620
-  __AUTH_CONST.__objc_const: 0x4170
+  __AUTH_CONST.__auth_got: 0x378
+  __AUTH_CONST.__const: 0x37e0
+  __AUTH_CONST.__cfstring: 0x8820
+  __AUTH_CONST.__objc_const: 0x4220
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_intobj: 0x150
-  __DATA.__objc_ivar: 0x128
-  __DATA.__data: 0xd60
-  __DATA.__bss: 0x9b0
+  __DATA.__objc_ivar: 0x12c
+  __DATA.__data: 0xd98
+  __DATA.__bss: 0x940
   __DATA_DIRTY.__objc_data: 0x8c0
-  __DATA_DIRTY.__bss: 0x1098
+  __DATA_DIRTY.__bss: 0x1188
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A3F024AE-4D89-3BA8-82E3-4780B67CED57
-  Functions: 1829
-  Symbols:   6762
-  CStrings:  3487
+  UUID: 1A81A706-6E67-3DF5-BE57-A77D9E101E17
+  Functions: 1857
+  Symbols:   6858
+  CStrings:  3535
 
Symbols:
+ +[VOSCommand ActivateBrailleScreenInputPreferringSingleHand]
+ +[VOSCommand ActivateBrailleScreenInputPreferringSingleHand].cold.1
+ +[VOSCommand BrailleToggleBrailleUI]
+ +[VOSCommand BrailleToggleBrailleUI].cold.1
+ +[VOSCommand BrailleToggleKeyboardBrailleUI]
+ +[VOSCommand BrailleToggleKeyboardBrailleUI].cold.1
+ +[VOSCommand NextKeyboardLanguage]
+ +[VOSCommand NextKeyboardLanguage].cold.1
+ +[VOSCommand ReadAllPrefixes]
+ +[VOSCommand ReadAllPrefixes].cold.1
+ +[VOSCommand ReadFromTopPrefixes]
+ +[VOSCommand ReadFromTopPrefixes].cold.1
+ +[VOSCommand ToggleIgnoreTrackpad]
+ +[VOSCommand ToggleIgnoreTrackpad].cold.1
+ +[VOSSettingsItem BSIActivationGestures]
+ +[VOSSettingsItem BSIActivationGestures].cold.1
+ -[VOSCommand capability]
+ -[VOSCommand setCapability:]
+ -[VOSCommandProfile _checkCommandCapabilities:]
+ _AXDeviceIsPhone
+ _AXRuntimeCheck_SupportsVoiceOverReadPrefixes
+ _ActivateBrailleScreenInputPreferringSingleHand._Command
+ _ActivateBrailleScreenInputPreferringSingleHand.onceToken
+ _BSIActivationGestures._SettingsItem
+ _BSIActivationGestures.onceToken
+ _BrailleToggleBrailleUI._Command
+ _BrailleToggleBrailleUI.onceToken
+ _BrailleToggleKeyboardBrailleUI._Command
+ _BrailleToggleKeyboardBrailleUI.onceToken
+ _NextKeyboardLanguage._Command
+ _NextKeyboardLanguage.onceToken
+ _OBJC_IVAR_$_VOSCommand._capability
+ _ReadAllPrefixes._Command
+ _ReadAllPrefixes.onceToken
+ _ReadFromTopPrefixes._Command
+ _ReadFromTopPrefixes.onceToken
+ _ToggleIgnoreTrackpad._Command
+ _ToggleIgnoreTrackpad.onceToken
+ _VOSSingleHandBSIEnabled
+ ___29+[VOSCommand ReadAllPrefixes]_block_invoke
+ ___33+[VOSCommand ReadFromTopPrefixes]_block_invoke
+ ___34+[VOSCommand NextKeyboardLanguage]_block_invoke
+ ___34+[VOSCommand ToggleIgnoreTrackpad]_block_invoke
+ ___36+[VOSCommand BrailleToggleBrailleUI]_block_invoke
+ ___40+[VOSSettingsItem BSIActivationGestures]_block_invoke
+ ___44+[VOSCommand BrailleToggleKeyboardBrailleUI]_block_invoke
+ ___60+[VOSCommand ActivateBrailleScreenInputPreferringSingleHand]_block_invoke
+ ___block_literal_global.1002
+ ___block_literal_global.1007
+ ___block_literal_global.1012
+ ___block_literal_global.1017
+ ___block_literal_global.1022
+ ___block_literal_global.1027
+ ___block_literal_global.1032
+ ___block_literal_global.1037
+ ___block_literal_global.1042
+ ___block_literal_global.1047
+ ___block_literal_global.1052
+ ___block_literal_global.1057
+ ___block_literal_global.1062
+ ___block_literal_global.1067
+ ___block_literal_global.1072
+ ___block_literal_global.1077
+ ___block_literal_global.1082
+ ___block_literal_global.1087
+ ___block_literal_global.1092
+ ___block_literal_global.1097
+ ___block_literal_global.1102
+ ___block_literal_global.1107
+ ___block_literal_global.1112
+ ___block_literal_global.1117
+ ___block_literal_global.1122
+ ___block_literal_global.1127
+ ___block_literal_global.1132
+ ___block_literal_global.1137
+ ___block_literal_global.1142
+ ___block_literal_global.1147
+ ___block_literal_global.1152
+ ___block_literal_global.1157
+ ___block_literal_global.1162
+ ___block_literal_global.1167
+ ___block_literal_global.1172
+ ___block_literal_global.1177
+ ___block_literal_global.1182
+ ___block_literal_global.1187
+ ___block_literal_global.1192
+ ___block_literal_global.1197
+ ___block_literal_global.1202
+ ___block_literal_global.1207
+ ___block_literal_global.1212
+ ___block_literal_global.1217
+ ___block_literal_global.1222
+ ___block_literal_global.1227
+ ___block_literal_global.1232
+ ___block_literal_global.1237
+ ___block_literal_global.1242
+ ___block_literal_global.1247
+ ___block_literal_global.1252
+ ___block_literal_global.1257
+ ___block_literal_global.1262
+ ___block_literal_global.1267
+ ___block_literal_global.1272
+ ___block_literal_global.1277
+ ___block_literal_global.1282
+ ___block_literal_global.1287
+ ___block_literal_global.1292
+ ___block_literal_global.1297
+ ___block_literal_global.1302
+ ___block_literal_global.1307
+ ___block_literal_global.1312
+ ___block_literal_global.1317
+ ___block_literal_global.1322
+ ___block_literal_global.1327
+ ___block_literal_global.1332
+ ___block_literal_global.1337
+ ___block_literal_global.1342
+ ___block_literal_global.1347
+ ___block_literal_global.1352
+ ___block_literal_global.282
+ ___block_literal_global.287
+ ___block_literal_global.292
+ ___block_literal_global.297
+ ___block_literal_global.305
+ ___block_literal_global.307
+ ___block_literal_global.312
+ ___block_literal_global.317
+ ___block_literal_global.322
+ ___block_literal_global.327
+ ___block_literal_global.332
+ ___block_literal_global.337
+ ___block_literal_global.345
+ ___block_literal_global.347
+ ___block_literal_global.352
+ ___block_literal_global.357
+ ___block_literal_global.362
+ ___block_literal_global.367
+ ___block_literal_global.372
+ ___block_literal_global.377
+ ___block_literal_global.382
+ ___block_literal_global.387
+ ___block_literal_global.392
+ ___block_literal_global.397
+ ___block_literal_global.402
+ ___block_literal_global.407
+ ___block_literal_global.412
+ ___block_literal_global.417
+ ___block_literal_global.422
+ ___block_literal_global.427
+ ___block_literal_global.432
+ ___block_literal_global.437
+ ___block_literal_global.442
+ ___block_literal_global.453
+ ___block_literal_global.457
+ ___block_literal_global.460
+ ___block_literal_global.462
+ ___block_literal_global.467
+ ___block_literal_global.477
+ ___block_literal_global.478
+ ___block_literal_global.480
+ ___block_literal_global.482
+ ___block_literal_global.492
+ ___block_literal_global.493
+ ___block_literal_global.497
+ ___block_literal_global.502
+ ___block_literal_global.507
+ ___block_literal_global.512
+ ___block_literal_global.517
+ ___block_literal_global.522
+ ___block_literal_global.527
+ ___block_literal_global.530
+ ___block_literal_global.532
+ ___block_literal_global.537
+ ___block_literal_global.542
+ ___block_literal_global.547
+ ___block_literal_global.552
+ ___block_literal_global.557
+ ___block_literal_global.562
+ ___block_literal_global.567
+ ___block_literal_global.572
+ ___block_literal_global.577
+ ___block_literal_global.582
+ ___block_literal_global.585
+ ___block_literal_global.593
+ ___block_literal_global.595
+ ___block_literal_global.597
+ ___block_literal_global.601
+ ___block_literal_global.603
+ ___block_literal_global.605
+ ___block_literal_global.607
+ ___block_literal_global.611
+ ___block_literal_global.613
+ ___block_literal_global.615
+ ___block_literal_global.617
+ ___block_literal_global.622
+ ___block_literal_global.627
+ ___block_literal_global.632
+ ___block_literal_global.637
+ ___block_literal_global.642
+ ___block_literal_global.647
+ ___block_literal_global.652
+ ___block_literal_global.657
+ ___block_literal_global.662
+ ___block_literal_global.667
+ ___block_literal_global.672
+ ___block_literal_global.677
+ ___block_literal_global.682
+ ___block_literal_global.687
+ ___block_literal_global.692
+ ___block_literal_global.697
+ ___block_literal_global.702
+ ___block_literal_global.707
+ ___block_literal_global.712
+ ___block_literal_global.717
+ ___block_literal_global.722
+ ___block_literal_global.727
+ ___block_literal_global.732
+ ___block_literal_global.737
+ ___block_literal_global.742
+ ___block_literal_global.747
+ ___block_literal_global.752
+ ___block_literal_global.757
+ ___block_literal_global.762
+ ___block_literal_global.767
+ ___block_literal_global.772
+ ___block_literal_global.777
+ ___block_literal_global.782
+ ___block_literal_global.787
+ ___block_literal_global.792
+ ___block_literal_global.797
+ ___block_literal_global.802
+ ___block_literal_global.807
+ ___block_literal_global.812
+ ___block_literal_global.817
+ ___block_literal_global.822
+ ___block_literal_global.827
+ ___block_literal_global.832
+ ___block_literal_global.837
+ ___block_literal_global.842
+ ___block_literal_global.847
+ ___block_literal_global.852
+ ___block_literal_global.857
+ ___block_literal_global.862
+ ___block_literal_global.867
+ ___block_literal_global.872
+ ___block_literal_global.877
+ ___block_literal_global.882
+ ___block_literal_global.887
+ ___block_literal_global.892
+ ___block_literal_global.897
+ ___block_literal_global.902
+ ___block_literal_global.907
+ ___block_literal_global.912
+ ___block_literal_global.917
+ ___block_literal_global.922
+ ___block_literal_global.927
+ ___block_literal_global.932
+ ___block_literal_global.937
+ ___block_literal_global.942
+ ___block_literal_global.947
+ ___block_literal_global.952
+ ___block_literal_global.957
+ ___block_literal_global.962
+ ___block_literal_global.967
+ ___block_literal_global.972
+ ___block_literal_global.977
+ ___block_literal_global.982
+ ___block_literal_global.987
+ ___block_literal_global.992
+ ___block_literal_global.997
+ _kVOTEventCommandActivateBrailleScreenInputPreferringSingleHand
+ _kVOTEventCommandBrailleToggleZoomOut
+ _kVOTEventCommandOutputElementCVAnalysisSummary
+ _kVOTEventCommandReadAllPrefixes
+ _kVOTEventCommandReadFromTopPrefixes
+ _kVOTEventCommandToggleBrailleUI
+ _kVOTEventCommandToggleIgnoreTrackpad
+ _kVOTEventCommandToggleKeyboardBrailleUI
+ _objc_msgSend$ActivateBrailleScreenInputPreferringSingleHand
+ _objc_msgSend$BSIActivationGestures
+ _objc_msgSend$BrailleToggleBrailleUI
+ _objc_msgSend$BrailleToggleKeyboardBrailleUI
+ _objc_msgSend$NextKeyboardLanguage
+ _objc_msgSend$ReadAllPrefixes
+ _objc_msgSend$ReadFromTopPrefixes
+ _objc_msgSend$ToggleIgnoreTrackpad
+ _objc_msgSend$_checkCommandCapabilities:
+ _objc_msgSend$setVoiceOverTouchBrailleGesturesActivationGestureEnabled:
+ _objc_msgSend$voiceOverTouchBrailleGesturesActivationGestureEnabled
- ___block_literal_global.1004
- ___block_literal_global.1009
- ___block_literal_global.1014
- ___block_literal_global.1019
- ___block_literal_global.1024
- ___block_literal_global.1029
- ___block_literal_global.1034
- ___block_literal_global.1039
- ___block_literal_global.1044
- ___block_literal_global.1049
- ___block_literal_global.1054
- ___block_literal_global.1059
- ___block_literal_global.1064
- ___block_literal_global.1069
- ___block_literal_global.1074
- ___block_literal_global.1079
- ___block_literal_global.1084
- ___block_literal_global.1089
- ___block_literal_global.1094
- ___block_literal_global.1099
- ___block_literal_global.1104
- ___block_literal_global.1109
- ___block_literal_global.1114
- ___block_literal_global.1119
- ___block_literal_global.1124
- ___block_literal_global.1129
- ___block_literal_global.1134
- ___block_literal_global.1139
- ___block_literal_global.1144
- ___block_literal_global.1149
- ___block_literal_global.1154
- ___block_literal_global.1159
- ___block_literal_global.1164
- ___block_literal_global.1169
- ___block_literal_global.1174
- ___block_literal_global.1179
- ___block_literal_global.1184
- ___block_literal_global.1189
- ___block_literal_global.1194
- ___block_literal_global.1199
- ___block_literal_global.1204
- ___block_literal_global.1209
- ___block_literal_global.1214
- ___block_literal_global.1219
- ___block_literal_global.1224
- ___block_literal_global.1229
- ___block_literal_global.1234
- ___block_literal_global.1239
- ___block_literal_global.1244
- ___block_literal_global.1249
- ___block_literal_global.1254
- ___block_literal_global.1259
- ___block_literal_global.1264
- ___block_literal_global.1269
- ___block_literal_global.1274
- ___block_literal_global.1279
- ___block_literal_global.1284
- ___block_literal_global.1289
- ___block_literal_global.1294
- ___block_literal_global.1299
- ___block_literal_global.1304
- ___block_literal_global.1309
- ___block_literal_global.1314
- ___block_literal_global.279
- ___block_literal_global.283
- ___block_literal_global.284
- ___block_literal_global.288
- ___block_literal_global.293
- ___block_literal_global.298
- ___block_literal_global.303
- ___block_literal_global.308
- ___block_literal_global.313
- ___block_literal_global.318
- ___block_literal_global.323
- ___block_literal_global.333
- ___block_literal_global.338
- ___block_literal_global.343
- ___block_literal_global.348
- ___block_literal_global.353
- ___block_literal_global.358
- ___block_literal_global.363
- ___block_literal_global.368
- ___block_literal_global.373
- ___block_literal_global.378
- ___block_literal_global.383
- ___block_literal_global.388
- ___block_literal_global.393
- ___block_literal_global.398
- ___block_literal_global.403
- ___block_literal_global.408
- ___block_literal_global.413
- ___block_literal_global.418
- ___block_literal_global.423
- ___block_literal_global.428
- ___block_literal_global.433
- ___block_literal_global.438
- ___block_literal_global.443
- ___block_literal_global.448
- ___block_literal_global.450
- ___block_literal_global.461
- ___block_literal_global.466
- ___block_literal_global.471
- ___block_literal_global.476
- ___block_literal_global.481
- ___block_literal_global.485
- ___block_literal_global.486
- ___block_literal_global.496
- ___block_literal_global.498
- ___block_literal_global.500
- ___block_literal_global.501
- ___block_literal_global.511
- ___block_literal_global.513
- ___block_literal_global.516
- ___block_literal_global.521
- ___block_literal_global.526
- ___block_literal_global.531
- ___block_literal_global.536
- ___block_literal_global.541
- ___block_literal_global.543
- ___block_literal_global.545
- ___block_literal_global.546
- ___block_literal_global.553
- ___block_literal_global.555
- ___block_literal_global.556
- ___block_literal_global.566
- ___block_literal_global.568
- ___block_literal_global.571
- ___block_literal_global.576
- ___block_literal_global.581
- ___block_literal_global.586
- ___block_literal_global.591
- ___block_literal_global.599
- ___block_literal_global.604
- ___block_literal_global.606
- ___block_literal_global.608
- ___block_literal_global.610
- ___block_literal_global.614
- ___block_literal_global.619
- ___block_literal_global.624
- ___block_literal_global.629
- ___block_literal_global.634
- ___block_literal_global.639
- ___block_literal_global.644
- ___block_literal_global.649
- ___block_literal_global.654
- ___block_literal_global.659
- ___block_literal_global.664
- ___block_literal_global.669
- ___block_literal_global.674
- ___block_literal_global.679
- ___block_literal_global.684
- ___block_literal_global.689
- ___block_literal_global.694
- ___block_literal_global.699
- ___block_literal_global.704
- ___block_literal_global.709
- ___block_literal_global.714
- ___block_literal_global.719
- ___block_literal_global.724
- ___block_literal_global.729
- ___block_literal_global.734
- ___block_literal_global.739
- ___block_literal_global.744
- ___block_literal_global.749
- ___block_literal_global.754
- ___block_literal_global.759
- ___block_literal_global.764
- ___block_literal_global.769
- ___block_literal_global.774
- ___block_literal_global.779
- ___block_literal_global.784
- ___block_literal_global.789
- ___block_literal_global.794
- ___block_literal_global.799
- ___block_literal_global.804
- ___block_literal_global.809
- ___block_literal_global.814
- ___block_literal_global.819
- ___block_literal_global.824
- ___block_literal_global.829
- ___block_literal_global.834
- ___block_literal_global.839
- ___block_literal_global.844
- ___block_literal_global.849
- ___block_literal_global.854
- ___block_literal_global.859
- ___block_literal_global.864
- ___block_literal_global.869
- ___block_literal_global.874
- ___block_literal_global.879
- ___block_literal_global.884
- ___block_literal_global.889
- ___block_literal_global.894
- ___block_literal_global.899
- ___block_literal_global.904
- ___block_literal_global.909
- ___block_literal_global.914
- ___block_literal_global.919
- ___block_literal_global.924
- ___block_literal_global.929
- ___block_literal_global.934
- ___block_literal_global.939
- ___block_literal_global.944
- ___block_literal_global.949
- ___block_literal_global.954
- ___block_literal_global.959
- ___block_literal_global.964
- ___block_literal_global.969
- ___block_literal_global.974
- ___block_literal_global.979
- ___block_literal_global.984
- ___block_literal_global.989
- ___block_literal_global.994
- ___block_literal_global.999
- _kVOTEventCommandOutputElementComputerVisionAnalysisSummary
CStrings:
+ "ActivateBrailleScreenInputPreferringSingleHand"
+ "BSIActivationGestures"
+ "BSI_USE_ACTIVATION_GESTURES"
+ "BrailleToggleBrailleUI"
+ "BrailleToggleKeyboardBrailleUI"
+ "NextKeyboardLanguage"
+ "ReadAllPrefixes"
+ "ReadFromTopPrefixes"
+ "SingleHandBSI"
+ "T@\"NSString\",N,V_capability"
+ "ToggleIgnoreTrackpad"
+ "VOTEventCommandActivateBrailleScreenInputPreferringSingleHand"
+ "VOTEventCommandBrailleToggleZoomOut"
+ "VOTEventCommandOutputCVAnalysisSummary"
+ "VOTEventCommandReadAllPrefixes"
+ "VOTEventCommandReadFromTopPrefixes"
+ "VOTEventCommandToggleBrailleUI"
+ "VOTEventCommandToggleIgnoreTrackpad"
+ "VOTEventCommandToggleKeyboardBrailleUI"
+ "_capability"
+ "_checkCommandCapabilities:"
+ "capability"
+ "setCapability:"
+ "setVoiceOverTouchBrailleGesturesActivationGestureEnabled:"
+ "voiceOverTouchBrailleGesturesActivationGestureEnabled"
- "VOTEventCommandOutputComputerVisionAnalysisSummary"

```
