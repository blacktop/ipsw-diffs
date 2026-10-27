## MapKit

> `/System/iOSSupport/System/Library/Frameworks/MapKit.framework/Versions/A/MapKit`

```diff

-2552.20.6.12.13
-  __TEXT.__text: 0x25b1ec
-  __TEXT.__objc_methlist: 0x26984
-  __TEXT.__const: 0x69a0
+2552.21.6.17.18
+  __TEXT.__text: 0x25c95c
+  __TEXT.__objc_methlist: 0x26ab4
+  __TEXT.__const: 0x69c0
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__cstring: 0x10523
-  __TEXT.__swift5_typeref: 0x15f4
+  __TEXT.__cstring: 0x10539
+  __TEXT.__swift5_typeref: 0x15fc
   __TEXT.__swift5_reflstr: 0x1460
   __TEXT.__swift5_assocty: 0x1e8
   __TEXT.__swift5_fieldmd: 0x2124

   __TEXT.__swift5_protos: 0x70
   __TEXT.__swift5_proto: 0x208
   __TEXT.__swift5_types: 0x2d0
-  __TEXT.__oslogstring: 0x7753
+  __TEXT.__oslogstring: 0x785a
   __TEXT.__swift5_capture: 0x3a4
   __TEXT.__swift_as_entry: 0x13c
   __TEXT.__swift_as_ret: 0x134
   __TEXT.__swift_as_cont: 0x1cc
-  __TEXT.__gcc_except_tab: 0x6060
+  __TEXT.__gcc_except_tab: 0x61e4
   __TEXT.__ustring: 0x19c
-  __TEXT.__unwind_info: 0xa078
-  __TEXT.__eh_frame: 0x241c
+  __TEXT.__unwind_info: 0xa110
+  __TEXT.__eh_frame: 0x2424
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7a20
-  __DATA_CONST.__objc_classlist: 0x11e0
+  __DATA_CONST.__const: 0x7a70
+  __DATA_CONST.__objc_classlist: 0x11f0
   __DATA_CONST.__objc_catlist: 0x1f0
   __DATA_CONST.__objc_protolist: 0x648
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x147f0
+  __DATA_CONST.__objc_selrefs: 0x148a0
   __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0xd98
+  __DATA_CONST.__objc_superrefs: 0xda8
   __DATA_CONST.__objc_arraydata: 0x6a0
-  __DATA_CONST.__got: 0x2408
+  __DATA_CONST.__got: 0x2400
   __AUTH_CONST.__const: 0x6778
-  __AUTH_CONST.__cfstring: 0x10be0
-  __AUTH_CONST.__objc_const: 0x45bc8
+  __AUTH_CONST.__cfstring: 0x10c00
+  __AUTH_CONST.__objc_const: 0x45e28
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x240
   __AUTH_CONST.__objc_intobj: 0xf18
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x480
   __AUTH_CONST.__objc_floatobj: 0x70
-  __AUTH_CONST.__auth_got: 0x2050
-  __AUTH_CONST.__auth_ptr: 0x740
-  __AUTH.__objc_data: 0x67b8
+  __AUTH_CONST.__auth_got: 0x2060
+  __AUTH_CONST.__auth_ptr: 0x748
+  __AUTH.__objc_data: 0x6858
   __AUTH.__data: 0x2d48
-  __DATA.__objc_ivar: 0x327c
-  __DATA.__data: 0x54d8
+  __DATA.__objc_ivar: 0x3298
+  __DATA.__data: 0x54e0
   __DATA.__bss: 0x4220
   __DATA.__common: 0x70
   __DATA_DIRTY.__objc_data: 0x45b0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14908
-  Symbols:   33335
-  CStrings:  3131
+  Functions: 14935
+  Symbols:   33415
+  CStrings:  3136
 
Symbols:
+ +[MKCompassButton compassButtonWithMapView:backgroundDisabled:]
+ +[_MXExtensionManager(Ridesharing) _maps_migrateRideBookingExtensionsFromLegacyStorageIfNeeded]
+ -[MKAnnotationManager hasPendingVisibleAnnotationsUpdate]
+ -[MKAppImageManager _invokePendingCompletionHandlersForURLString:withImage:wasCached:completed:error:]
+ -[MKAppImageManager _removePendingCompletionHandlersForURLString:]
+ -[MKAppImageManager _startDownloadForURL:]
+ -[MKCompassButton initWithFrame:mapView:backgroundDisabled:]
+ -[MKCompassView_ios initWithFrame:backgroundDisabled:]
+ -[MKMapSnapshotOptions _setShowsRouteAnnotations:]
+ -[MKMapSnapshotOptions _showsRouteAnnotations]
+ -[MKPinchGestureRecognizer reset]
+ -[MKPinchGestureRecognizer timeSinceFirstLift]
+ -[MKPinchGestureRecognizer touchesBegan:withEvent:]
+ -[MKPinchGestureRecognizer touchesCancelled:withEvent:]
+ -[MKPinchGestureRecognizer touchesEnded:withEvent:]
+ -[MKPitchButton _updateEnabledState]
+ -[MKPitchButton _updateGlyph]
+ -[MKRotationGestureRecognizer reset]
+ -[MKRotationGestureRecognizer timeSinceFirstLift]
+ -[MKRotationGestureRecognizer touchesBegan:withEvent:]
+ -[MKRotationGestureRecognizer touchesCancelled:withEvent:]
+ -[MKRotationGestureRecognizer touchesEnded:withEvent:]
+ -[MKRouteContextBuilder _populateEtaDescriptionForRouteInfo:]
+ -[MKRouteContextBuilder buildRouteContextForRoutes:selectedRouteIndex:populateEtaDescriptions:]
+ -[_MKLocalizedHoursBuilder _findNextOperatingWeekday:timeZone:]
+ -[_MKLocalizedHoursBuilder stringForClosedTillDate:timeZone:]
+ -[_MKMapItemCustomFeature isSelected]
+ GCC_except_table10301
+ GCC_except_table10366
+ GCC_except_table10369
+ GCC_except_table10432
+ GCC_except_table10434
+ GCC_except_table10453
+ GCC_except_table10665
+ GCC_except_table10666
+ GCC_except_table10721
+ GCC_except_table10745
+ GCC_except_table10760
+ GCC_except_table10786
+ GCC_except_table10847
+ GCC_except_table10849
+ GCC_except_table10852
+ GCC_except_table10862
+ GCC_except_table10870
+ GCC_except_table10871
+ GCC_except_table10873
+ GCC_except_table10876
+ GCC_except_table10880
+ GCC_except_table10881
+ GCC_except_table10882
+ GCC_except_table10883
+ GCC_except_table10884
+ GCC_except_table10885
+ GCC_except_table10888
+ GCC_except_table10891
+ GCC_except_table10911
+ GCC_except_table10912
+ GCC_except_table11094
+ GCC_except_table11177
+ GCC_except_table11180
+ GCC_except_table11181
+ GCC_except_table11185
+ GCC_except_table11187
+ GCC_except_table11189
+ GCC_except_table11191
+ GCC_except_table11193
+ GCC_except_table11195
+ GCC_except_table11197
+ GCC_except_table11201
+ GCC_except_table11227
+ GCC_except_table11229
+ GCC_except_table1124
+ GCC_except_table11253
+ GCC_except_table11323
+ GCC_except_table11324
+ GCC_except_table11327
+ GCC_except_table11328
+ GCC_except_table11329
+ GCC_except_table11330
+ GCC_except_table11331
+ GCC_except_table11332
+ GCC_except_table11334
+ GCC_except_table11335
+ GCC_except_table11338
+ GCC_except_table11342
+ GCC_except_table11343
+ GCC_except_table11345
+ GCC_except_table11346
+ GCC_except_table11347
+ GCC_except_table11351
+ GCC_except_table11446
+ GCC_except_table11447
+ GCC_except_table11454
+ GCC_except_table1148
+ GCC_except_table11554
+ GCC_except_table11584
+ GCC_except_table11586
+ GCC_except_table11621
+ GCC_except_table11625
+ GCC_except_table11906
+ GCC_except_table11945
+ GCC_except_table11972
+ GCC_except_table12011
+ GCC_except_table12013
+ GCC_except_table12016
+ GCC_except_table12017
+ GCC_except_table12018
+ GCC_except_table12021
+ GCC_except_table12022
+ GCC_except_table12024
+ GCC_except_table12025
+ GCC_except_table12026
+ GCC_except_table12027
+ GCC_except_table12030
+ GCC_except_table12031
+ GCC_except_table12032
+ GCC_except_table12059
+ GCC_except_table12088
+ GCC_except_table12093
+ GCC_except_table12094
+ GCC_except_table12099
+ GCC_except_table12102
+ GCC_except_table12104
+ GCC_except_table12105
+ GCC_except_table12106
+ GCC_except_table12138
+ GCC_except_table12407
+ GCC_except_table12408
+ GCC_except_table12409
+ GCC_except_table12410
+ GCC_except_table12544
+ GCC_except_table12545
+ GCC_except_table12654
+ GCC_except_table12674
+ GCC_except_table12698
+ GCC_except_table12702
+ GCC_except_table12703
+ GCC_except_table12709
+ GCC_except_table12711
+ GCC_except_table12712
+ GCC_except_table12737
+ GCC_except_table12748
+ GCC_except_table12751
+ GCC_except_table1332
+ GCC_except_table1364
+ GCC_except_table1404
+ GCC_except_table1660
+ GCC_except_table168
+ GCC_except_table1711
+ GCC_except_table1744
+ GCC_except_table1747
+ GCC_except_table1763
+ GCC_except_table1766
+ GCC_except_table1800
+ GCC_except_table183
+ GCC_except_table1885
+ GCC_except_table1927
+ GCC_except_table1949
+ GCC_except_table195
+ GCC_except_table1953
+ GCC_except_table1978
+ GCC_except_table200
+ GCC_except_table2062
+ GCC_except_table2277
+ GCC_except_table2285
+ GCC_except_table2286
+ GCC_except_table2287
+ GCC_except_table2288
+ GCC_except_table2289
+ GCC_except_table2296
+ GCC_except_table2314
+ GCC_except_table253
+ GCC_except_table254
+ GCC_except_table2576
+ GCC_except_table2984
+ GCC_except_table2989
+ GCC_except_table2992
+ GCC_except_table3005
+ GCC_except_table3007
+ GCC_except_table3009
+ GCC_except_table3057
+ GCC_except_table3059
+ GCC_except_table3177
+ GCC_except_table3182
+ GCC_except_table3187
+ GCC_except_table3192
+ GCC_except_table3197
+ GCC_except_table322
+ GCC_except_table3306
+ GCC_except_table3310
+ GCC_except_table3318
+ GCC_except_table3338
+ GCC_except_table3343
+ GCC_except_table3402
+ GCC_except_table350
+ GCC_except_table356
+ GCC_except_table3707
+ GCC_except_table3756
+ GCC_except_table3758
+ GCC_except_table3759
+ GCC_except_table3761
+ GCC_except_table3767
+ GCC_except_table3808
+ GCC_except_table3809
+ GCC_except_table3811
+ GCC_except_table3814
+ GCC_except_table3855
+ GCC_except_table3856
+ GCC_except_table3857
+ GCC_except_table3858
+ GCC_except_table3859
+ GCC_except_table3860
+ GCC_except_table3872
+ GCC_except_table3875
+ GCC_except_table3876
+ GCC_except_table3878
+ GCC_except_table3879
+ GCC_except_table3881
+ GCC_except_table3903
+ GCC_except_table3907
+ GCC_except_table3913
+ GCC_except_table3916
+ GCC_except_table3917
+ GCC_except_table3918
+ GCC_except_table3967
+ GCC_except_table3968
+ GCC_except_table3973
+ GCC_except_table3974
+ GCC_except_table3984
+ GCC_except_table3985
+ GCC_except_table3986
+ GCC_except_table3987
+ GCC_except_table3989
+ GCC_except_table3990
+ GCC_except_table4010
+ GCC_except_table4012
+ GCC_except_table4021
+ GCC_except_table4027
+ GCC_except_table4030
+ GCC_except_table4032
+ GCC_except_table4033
+ GCC_except_table4034
+ GCC_except_table4037
+ GCC_except_table4058
+ GCC_except_table4059
+ GCC_except_table4061
+ GCC_except_table4062
+ GCC_except_table4068
+ GCC_except_table4069
+ GCC_except_table4070
+ GCC_except_table4072
+ GCC_except_table4073
+ GCC_except_table4107
+ GCC_except_table4121
+ GCC_except_table4124
+ GCC_except_table4405
+ GCC_except_table4437
+ GCC_except_table4461
+ GCC_except_table4588
+ GCC_except_table4589
+ GCC_except_table4590
+ GCC_except_table4596
+ GCC_except_table4665
+ GCC_except_table493
+ GCC_except_table496
+ GCC_except_table499
+ GCC_except_table515
+ GCC_except_table522
+ GCC_except_table5221
+ GCC_except_table536
+ GCC_except_table538
+ GCC_except_table540
+ GCC_except_table5410
+ GCC_except_table542
+ GCC_except_table5422
+ GCC_except_table549
+ GCC_except_table553
+ GCC_except_table5690
+ GCC_except_table574
+ GCC_except_table5755
+ GCC_except_table5759
+ GCC_except_table5761
+ GCC_except_table5762
+ GCC_except_table5763
+ GCC_except_table5764
+ GCC_except_table5765
+ GCC_except_table5766
+ GCC_except_table5767
+ GCC_except_table5768
+ GCC_except_table5769
+ GCC_except_table5770
+ GCC_except_table5772
+ GCC_except_table5773
+ GCC_except_table5776
+ GCC_except_table5777
+ GCC_except_table5873
+ GCC_except_table595
+ GCC_except_table5958
+ GCC_except_table5959
+ GCC_except_table6050
+ GCC_except_table608
+ GCC_except_table6086
+ GCC_except_table610
+ GCC_except_table6118
+ GCC_except_table612
+ GCC_except_table6122
+ GCC_except_table614
+ GCC_except_table6196
+ GCC_except_table622
+ GCC_except_table6250
+ GCC_except_table6253
+ GCC_except_table6255
+ GCC_except_table6284
+ GCC_except_table6299
+ GCC_except_table630
+ GCC_except_table6301
+ GCC_except_table6342
+ GCC_except_table636
+ GCC_except_table6516
+ GCC_except_table6593
+ GCC_except_table6609
+ GCC_except_table6662
+ GCC_except_table6663
+ GCC_except_table6664
+ GCC_except_table6665
+ GCC_except_table6667
+ GCC_except_table6668
+ GCC_except_table6679
+ GCC_except_table6680
+ GCC_except_table6703
+ GCC_except_table6778
+ GCC_except_table6821
+ GCC_except_table6877
+ GCC_except_table7094
+ GCC_except_table7097
+ GCC_except_table7106
+ GCC_except_table7107
+ GCC_except_table7292
+ GCC_except_table7299
+ GCC_except_table7328
+ GCC_except_table7331
+ GCC_except_table7442
+ GCC_except_table7483
+ GCC_except_table7484
+ GCC_except_table7485
+ GCC_except_table7486
+ GCC_except_table7487
+ GCC_except_table7488
+ GCC_except_table7489
+ GCC_except_table7490
+ GCC_except_table7499
+ GCC_except_table7500
+ GCC_except_table7501
+ GCC_except_table7502
+ GCC_except_table7503
+ GCC_except_table7685
+ GCC_except_table7739
+ GCC_except_table7756
+ GCC_except_table7760
+ GCC_except_table7766
+ GCC_except_table815
+ GCC_except_table8155
+ GCC_except_table8263
+ GCC_except_table8278
+ GCC_except_table8283
+ GCC_except_table8527
+ GCC_except_table8582
+ GCC_except_table8724
+ GCC_except_table8828
+ GCC_except_table8830
+ GCC_except_table8833
+ GCC_except_table8961
+ GCC_except_table9094
+ GCC_except_table9112
+ GCC_except_table9115
+ GCC_except_table9309
+ GCC_except_table9328
+ GCC_except_table9330
+ GCC_except_table9430
+ GCC_except_table9431
+ GCC_except_table9434
+ GCC_except_table9470
+ GCC_except_table9485
+ GCC_except_table953
+ GCC_except_table9538
+ GCC_except_table9646
+ GCC_except_table9671
+ GCC_except_table9673
+ GCC_except_table9675
+ GCC_except_table9676
+ GCC_except_table9748
+ GCC_except_table9853
+ GCC_except_table9854
+ GCC_except_table9855
+ GCC_except_table9857
+ GCC_except_table9858
+ GCC_except_table9859
+ GCC_except_table9861
+ GCC_except_table9865
+ GCC_except_table9868
+ GCC_except_table9869
+ GCC_except_table9872
+ GCC_except_table9873
+ GCC_except_table9894
+ GCC_except_table9895
+ GCC_except_table9898
+ GCC_except_table9920
+ GCC_except_table9933
+ GCC_except_table9956
+ GCC_except_table9962
+ OBJC_IVAR_$_MKAppImageManager._pendingCompletionHandlersByUrlString
+ OBJC_IVAR_$_MKCompassView_ios._backgroundDisabled
+ OBJC_IVAR_$_MKMapGestureController._pinchIsDirectTouch
+ OBJC_IVAR_$_MKMapSnapshotOptions._showsRouteAnnotations
+ OBJC_IVAR_$_MKPinchGestureRecognizer._firstLiftTimestamp
+ OBJC_IVAR_$_MKRotationGestureRecognizer._firstLiftTimestamp
+ OBJC_IVAR_$__MKMapItemCustomFeature._selected
+ OBJC_IVAR_$__MKStaticMapView._batchSuppressGrid
+ _GEOStringForDuration
+ _MapKitConfig__deprecated_RideBookingExtensionsAppBundleIdentifiers
+ _MapKitConfig__deprecated_RideBookingExtensionsAppBundleIdentifiers_Metadata
+ _MapKitConfig__deprecated_RideBookingExtensionsAppBundleIdentifiers_Metadata_block_invoke_13
+ _OBJC_CLASS_$_MKPinchGestureRecognizer
+ _OBJC_CLASS_$_MKRotationGestureRecognizer
+ _OBJC_METACLASS_$_MKPinchGestureRecognizer
+ _OBJC_METACLASS_$_MKRotationGestureRecognizer
+ _OBJC_METACLASS_$_UIPinchGestureRecognizer
+ _OBJC_METACLASS_$_UIRotationGestureRecognizer
+ __45-[MKAppImageManager cancelLoadAppImageAtURL:]_block_invoke_3
+ __GEOConfigRemoveValue
+ __OBJC_$_INSTANCE_METHODS_MKPinchGestureRecognizer
+ __OBJC_$_INSTANCE_METHODS_MKRotationGestureRecognizer
+ __OBJC_$_INSTANCE_VARIABLES_MKPinchGestureRecognizer
+ __OBJC_$_INSTANCE_VARIABLES_MKRotationGestureRecognizer
+ __OBJC_$_PROP_LIST_MKPinchGestureRecognizer
+ __OBJC_$_PROP_LIST_MKRotationGestureRecognizer
+ __OBJC_CLASS_RO_$_MKPinchGestureRecognizer
+ __OBJC_CLASS_RO_$_MKRotationGestureRecognizer
+ __OBJC_METACLASS_RO_$_MKPinchGestureRecognizer
+ __OBJC_METACLASS_RO_$_MKRotationGestureRecognizer
+ ___102-[MKAppImageManager _invokePendingCompletionHandlersForURLString:withImage:wasCached:completed:error:]_block_invoke
+ ___42-[MKAppImageManager _startDownloadForURL:]_block_invoke
+ ___42-[MKAppImageManager _startDownloadForURL:]_block_invoke_2
+ ___45-[MKAppImageManager cancelLoadAppImageAtURL:]_block_invoke_4
+ ___63-[_MKLocalizedHoursBuilder _findNextOperatingWeekday:timeZone:]_block_invoke
+ ___66-[MKAppImageManager _removePendingCompletionHandlersForURLString:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48s_e17_v16?0"UIImage"8ls32l8s40l8s48l8
+ ___block_descriptor_58_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0ls32l8s40l8r48l8r56l8
+ _findNextOperatingWeekday:timeZone:.oneTimeToken
+ _findNextOperatingWeekday:timeZone:.weekdays
+ _objc_msgSend$_activeEventOfType:
+ _objc_msgSend$_findNextOperatingWeekday:timeZone:
+ _objc_msgSend$_invokePendingCompletionHandlersForURLString:withImage:wasCached:completed:error:
+ _objc_msgSend$_populateEtaDescriptionForRouteInfo:
+ _objc_msgSend$_removePendingCompletionHandlersForURLString:
+ _objc_msgSend$_showsRouteAnnotations
+ _objc_msgSend$_startDownloadForURL:
+ _objc_msgSend$_updateEnabledState
+ _objc_msgSend$_updateGlyph
+ _objc_msgSend$arrayForKey:
+ _objc_msgSend$buildRouteContextForRoutes:selectedRouteIndex:populateEtaDescriptions:
+ _objc_msgSend$compassButtonWithMapView:backgroundDisabled:
+ _objc_msgSend$detailTextAction
+ _objc_msgSend$hasAnimation
+ _objc_msgSend$hasPendingVisibleAnnotationsUpdate
+ _objc_msgSend$initWithFrame:mapView:backgroundDisabled:
+ _objc_msgSend$isFamiliarRoute
+ _objc_msgSend$numberOfTouches
+ _objc_msgSend$routeLabelAction
+ _objc_msgSend$routeLabelArtwork
+ _objc_msgSend$routeLabelDescriptionString
+ _objc_msgSend$stringForClosedTillDate:timeZone:
+ _objc_msgSend$timeSinceFirstLift
+ _objc_msgSend$travelAndChargingDuration
+ _symbolic _____Sg 11GeoServices17DirectionsServiceC22FasterRoutePreferencesV
- -[MKPitchButton _updateButtonState]
- -[_MKAppImageManagerContainer completionHandler]
- -[_MKAppImageManagerContainer setCompletionHandler:]
- -[_MKLocalizedHoursBuilder _findNextOperatingWeekday:]
- GCC_except_table10276
- GCC_except_table10341
- GCC_except_table10344
- GCC_except_table10407
- GCC_except_table10409
- GCC_except_table10428
- GCC_except_table10640
- GCC_except_table10641
- GCC_except_table10696
- GCC_except_table10720
- GCC_except_table10735
- GCC_except_table10761
- GCC_except_table10820
- GCC_except_table10822
- GCC_except_table10824
- GCC_except_table10827
- GCC_except_table10837
- GCC_except_table10846
- GCC_except_table10848
- GCC_except_table10851
- GCC_except_table10855
- GCC_except_table10856
- GCC_except_table10857
- GCC_except_table10858
- GCC_except_table10859
- GCC_except_table10860
- GCC_except_table10861
- GCC_except_table10863
- GCC_except_table10866
- GCC_except_table10887
- GCC_except_table11069
- GCC_except_table11147
- GCC_except_table11152
- GCC_except_table11155
- GCC_except_table11156
- GCC_except_table11160
- GCC_except_table11162
- GCC_except_table11164
- GCC_except_table11166
- GCC_except_table11168
- GCC_except_table11170
- GCC_except_table11176
- GCC_except_table1119
- GCC_except_table11202
- GCC_except_table11204
- GCC_except_table11228
- GCC_except_table11297
- GCC_except_table11298
- GCC_except_table11299
- GCC_except_table11302
- GCC_except_table11303
- GCC_except_table11304
- GCC_except_table11305
- GCC_except_table11306
- GCC_except_table11307
- GCC_except_table11309
- GCC_except_table11310
- GCC_except_table11313
- GCC_except_table11317
- GCC_except_table11318
- GCC_except_table11320
- GCC_except_table11321
- GCC_except_table11326
- GCC_except_table11421
- GCC_except_table11422
- GCC_except_table11429
- GCC_except_table1143
- GCC_except_table11529
- GCC_except_table11559
- GCC_except_table11561
- GCC_except_table11596
- GCC_except_table11600
- GCC_except_table11881
- GCC_except_table11920
- GCC_except_table11947
- GCC_except_table11975
- GCC_except_table11976
- GCC_except_table11986
- GCC_except_table11988
- GCC_except_table11991
- GCC_except_table11992
- GCC_except_table11993
- GCC_except_table11996
- GCC_except_table11997
- GCC_except_table11999
- GCC_except_table12002
- GCC_except_table12005
- GCC_except_table12006
- GCC_except_table12007
- GCC_except_table12034
- GCC_except_table12063
- GCC_except_table12068
- GCC_except_table12069
- GCC_except_table12074
- GCC_except_table12077
- GCC_except_table12079
- GCC_except_table12080
- GCC_except_table12081
- GCC_except_table12113
- GCC_except_table12380
- GCC_except_table12381
- GCC_except_table12382
- GCC_except_table12383
- GCC_except_table12517
- GCC_except_table12518
- GCC_except_table12627
- GCC_except_table12647
- GCC_except_table12649
- GCC_except_table12671
- GCC_except_table12675
- GCC_except_table12682
- GCC_except_table12683
- GCC_except_table12684
- GCC_except_table12685
- GCC_except_table12721
- GCC_except_table12724
- GCC_except_table1327
- GCC_except_table1359
- GCC_except_table1399
- GCC_except_table1655
- GCC_except_table170
- GCC_except_table1706
- GCC_except_table1739
- GCC_except_table1742
- GCC_except_table1746
- GCC_except_table1748
- GCC_except_table1785
- GCC_except_table188
- GCC_except_table1880
- GCC_except_table1922
- GCC_except_table1944
- GCC_except_table1948
- GCC_except_table1973
- GCC_except_table2057
- GCC_except_table2271
- GCC_except_table2273
- GCC_except_table2276
- GCC_except_table2280
- GCC_except_table2281
- GCC_except_table2283
- GCC_except_table2284
- GCC_except_table2308
- GCC_except_table248
- GCC_except_table249
- GCC_except_table2570
- GCC_except_table2978
- GCC_except_table2983
- GCC_except_table2986
- GCC_except_table2987
- GCC_except_table2991
- GCC_except_table2995
- GCC_except_table3051
- GCC_except_table3053
- GCC_except_table312
- GCC_except_table3171
- GCC_except_table3176
- GCC_except_table3180
- GCC_except_table3181
- GCC_except_table3191
- GCC_except_table3300
- GCC_except_table3304
- GCC_except_table3312
- GCC_except_table3320
- GCC_except_table3337
- GCC_except_table3396
- GCC_except_table345
- GCC_except_table351
- GCC_except_table3701
- GCC_except_table3747
- GCC_except_table3751
- GCC_except_table3752
- GCC_except_table3754
- GCC_except_table3800
- GCC_except_table3801
- GCC_except_table3803
- GCC_except_table3806
- GCC_except_table3847
- GCC_except_table3848
- GCC_except_table3849
- GCC_except_table3850
- GCC_except_table3851
- GCC_except_table3852
- GCC_except_table3862
- GCC_except_table3863
- GCC_except_table3864
- GCC_except_table3867
- GCC_except_table3868
- GCC_except_table3873
- GCC_except_table3895
- GCC_except_table3899
- GCC_except_table3901
- GCC_except_table3905
- GCC_except_table3908
- GCC_except_table3910
- GCC_except_table3950
- GCC_except_table3951
- GCC_except_table3952
- GCC_except_table3953
- GCC_except_table3954
- GCC_except_table3955
- GCC_except_table3956
- GCC_except_table3957
- GCC_except_table3976
- GCC_except_table3981
- GCC_except_table3982
- GCC_except_table3983
- GCC_except_table3992
- GCC_except_table3993
- GCC_except_table3994
- GCC_except_table3995
- GCC_except_table3997
- GCC_except_table3998
- GCC_except_table4018
- GCC_except_table4029
- GCC_except_table4040
- GCC_except_table4050
- GCC_except_table4051
- GCC_except_table4057
- GCC_except_table4089
- GCC_except_table4103
- GCC_except_table4106
- GCC_except_table4387
- GCC_except_table4419
- GCC_except_table4443
- GCC_except_table4570
- GCC_except_table4571
- GCC_except_table4572
- GCC_except_table4578
- GCC_except_table4647
- GCC_except_table486
- GCC_except_table488
- GCC_except_table494
- GCC_except_table510
- GCC_except_table512
- GCC_except_table5202
- GCC_except_table531
- GCC_except_table533
- GCC_except_table535
- GCC_except_table537
- GCC_except_table5391
- GCC_except_table5403
- GCC_except_table544
- GCC_except_table548
- GCC_except_table5671
- GCC_except_table569
- GCC_except_table5726
- GCC_except_table5727
- GCC_except_table5728
- GCC_except_table5729
- GCC_except_table5730
- GCC_except_table5732
- GCC_except_table5734
- GCC_except_table5735
- GCC_except_table5736
- GCC_except_table5739
- GCC_except_table5740
- GCC_except_table5742
- GCC_except_table5743
- GCC_except_table5744
- GCC_except_table5750
- GCC_except_table5757
- GCC_except_table5854
- GCC_except_table590
- GCC_except_table5939
- GCC_except_table5940
- GCC_except_table603
- GCC_except_table6031
- GCC_except_table605
- GCC_except_table6067
- GCC_except_table607
- GCC_except_table609
- GCC_except_table6099
- GCC_except_table6103
- GCC_except_table617
- GCC_except_table6177
- GCC_except_table6231
- GCC_except_table6234
- GCC_except_table6236
- GCC_except_table625
- GCC_except_table6261
- GCC_except_table6265
- GCC_except_table6282
- GCC_except_table631
- GCC_except_table6323
- GCC_except_table6497
- GCC_except_table6574
- GCC_except_table6590
- GCC_except_table6623
- GCC_except_table6624
- GCC_except_table6626
- GCC_except_table6644
- GCC_except_table6646
- GCC_except_table6648
- GCC_except_table6649
- GCC_except_table6660
- GCC_except_table6684
- GCC_except_table6759
- GCC_except_table6802
- GCC_except_table6858
- GCC_except_table7073
- GCC_except_table7076
- GCC_except_table7085
- GCC_except_table7086
- GCC_except_table7271
- GCC_except_table7278
- GCC_except_table7307
- GCC_except_table7310
- GCC_except_table7421
- GCC_except_table7461
- GCC_except_table7462
- GCC_except_table7463
- GCC_except_table7464
- GCC_except_table7465
- GCC_except_table7466
- GCC_except_table7467
- GCC_except_table7468
- GCC_except_table7469
- GCC_except_table7478
- GCC_except_table7479
- GCC_except_table7480
- GCC_except_table7481
- GCC_except_table7663
- GCC_except_table7717
- GCC_except_table7734
- GCC_except_table7738
- GCC_except_table7744
- GCC_except_table810
- GCC_except_table8133
- GCC_except_table8241
- GCC_except_table8256
- GCC_except_table8261
- GCC_except_table8505
- GCC_except_table8560
- GCC_except_table8701
- GCC_except_table8805
- GCC_except_table8807
- GCC_except_table8810
- GCC_except_table8938
- GCC_except_table9071
- GCC_except_table9089
- GCC_except_table9092
- GCC_except_table9286
- GCC_except_table9305
- GCC_except_table9307
- GCC_except_table9407
- GCC_except_table9408
- GCC_except_table9411
- GCC_except_table9447
- GCC_except_table9462
- GCC_except_table948
- GCC_except_table9515
- GCC_except_table9623
- GCC_except_table9625
- GCC_except_table9627
- GCC_except_table9652
- GCC_except_table9653
- GCC_except_table9725
- GCC_except_table9829
- GCC_except_table9830
- GCC_except_table9831
- GCC_except_table9833
- GCC_except_table9834
- GCC_except_table9835
- GCC_except_table9837
- GCC_except_table9841
- GCC_except_table9844
- GCC_except_table9845
- GCC_except_table9846
- GCC_except_table9848
- GCC_except_table9849
- GCC_except_table9871
- GCC_except_table9874
- GCC_except_table9896
- GCC_except_table9909
- GCC_except_table9932
- GCC_except_table9938
- OBJC_IVAR_$__MKAppImageManagerContainer._completionHandler
- _GEOConfigSetArray
- _MapKitConfig_RideBookingExtensionsAppBundleIdentifiers
- _MapKitConfig_RideBookingExtensionsAppBundleIdentifiers_Metadata
- _MapKitConfig_RideBookingExtensionsAppBundleIdentifiers_Metadata_block_invoke_13
- __58-[MKAppImageManager URLSession:task:didCompleteWithError:]_block_invoke_3
- ___54-[_MKLocalizedHoursBuilder _findNextOperatingWeekday:]_block_invoke
- ___57-[MKAppImageManager loadAppImageAtURL:completionHandler:]_block_invoke_2
- ___58-[MKAppImageManager URLSession:task:didCompleteWithError:]_block_invoke_3
- ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"UIImage"8ls32l8s40l8s48l8s56l8
- _findNextOperatingWeekday:.oneTimeToken
- _findNextOperatingWeekday:.weekdays
- _objc_msgSend$_findNextOperatingWeekday:
- _objc_msgSend$_updateButtonState
- _objc_msgSend$completionHandler
- _objc_msgSend$reportDailyUsageCountType:
CStrings:
+ "MKGesturing"
+ "Updating MKStaticMapView snapshot: End updates (showGridFirst: %@)"
+ "[MK] Identical user location but puck animator is stopped; forwarding to (re)start it"
+ "[MK] Skipping identical user location; puck animator has a live animation"
+ "[↻]Joining in-flight request for url: %@"
+ "handlePinch began, directTouch=%{public}s"
+ "isAnimation=YES"
+ "showsRouteAnnotations"
- "Begin Gesturing"
- "End Gesturing"
- "Updating MKStaticMapView snapshot: End updates"
```
