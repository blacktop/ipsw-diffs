## QuartzCore

> `/System/Library/Frameworks/QuartzCore.framework/QuartzCore`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__auth_got`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1223.0.8.2.0
-  __TEXT.__text: 0x3f61f0
-  __TEXT.__objc_methlist: 0xbb04
-  __TEXT.__const: 0x19c10
+1223.0.14.0.0
+  __TEXT.__text: 0x3fa604
+  __TEXT.__objc_methlist: 0xbbd4
+  __TEXT.__const: 0x19aa0
   __TEXT.__dlopen_cstrs: 0xe0
-  __TEXT.__cstring: 0x29c3a
-  __TEXT.__gcc_except_tab: 0x9f84
-  __TEXT.__oslogstring: 0x12f69
-  __TEXT.__unwind_info: 0x9448
+  __TEXT.__cstring: 0x29ea8
+  __TEXT.__gcc_except_tab: 0x9fac
+  __TEXT.__oslogstring: 0x13226
+  __TEXT.__unwind_info: 0x9498
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x11070
-  __DATA_CONST.__objc_classlist: 0x460
+  __DATA_CONST.__const: 0x110d0
+  __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5cd8
+  __DATA_CONST.__objc_selrefs: 0x5d10
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x4e0
+  __DATA_CONST.__objc_superrefs: 0x4e8
   __DATA_CONST.__objc_arraydata: 0x3ee0
-  __DATA_CONST.__got: 0xdc8
-  __AUTH_CONST.__const: 0x18560
-  __AUTH_CONST.__cfstring: 0x18e20
-  __AUTH_CONST.__objc_const: 0xec08
+  __DATA_CONST.__got: 0xdd0
+  __AUTH_CONST.__const: 0x18590
+  __AUTH_CONST.__cfstring: 0x18f00
+  __AUTH_CONST.__objc_const: 0xee20
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x150

   __AUTH_CONST.__objc_dictobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x2b78
-  __AUTH.__objc_data: 0x1400
+  __AUTH.__objc_data: 0x1450
   __AUTH.__data: 0x60
-  __DATA.__objc_ivar: 0x738
+  __DATA.__objc_ivar: 0x754
   __DATA.__data: 0x1450
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x46e0
+  __DATA.__bss: 0x46f0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x17c0
   __DATA_DIRTY.__data: 0x620
-  __DATA_DIRTY.__bss: 0x6a30
+  __DATA_DIRTY.__bss: 0x69c0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 12754
-  Symbols:   21746
-  CStrings:  8594
+  Functions: 12782
+  Symbols:   21794
+  CStrings:  8626
 
Symbols:
+ +[CADisplayLink(CAOverrideCreation) _displayLinkWithDisplay:target:selector:skipsOverrides:]
+ -[CADisplayFrameRateAssertion _ensureValid]
+ -[CADisplayFrameRateAssertion acquire]
+ -[CADisplayFrameRateAssertion cancel]
+ -[CADisplayFrameRateAssertion dealloc]
+ -[CADisplayFrameRateAssertion description]
+ -[CADisplayFrameRateAssertion identifier]
+ -[CADisplayFrameRateAssertion initializeClientPort]
+ -[CADisplayFrameRateAssertion invalidate]
+ -[CADisplayFrameRateAssertion isActive]
+ -[CADisplayFrameRateAssertion maximumFrameRate]
+ -[CADisplayFrameRateAssertion(Internal) _initWithDisplayId:maximumFrameRate:identifier:]
+ -[CADisplayStateControl createFrameRateAssertionWithMaximumFrameRate:identifier:]
+ -[CADisplayStateControl(CADebugAdditions) _copyAllFrameRateAssertionInfo]
+ -[CALayerHost hostedContextGravity]
+ -[CALayerHost setHostedContextGravity:]
+ GCC_except_table10006
+ GCC_except_table10008
+ GCC_except_table10027
+ GCC_except_table10029
+ GCC_except_table10173
+ GCC_except_table10212
+ GCC_except_table10368
+ GCC_except_table10537
+ GCC_except_table10584
+ GCC_except_table10623
+ GCC_except_table10789
+ GCC_except_table10792
+ GCC_except_table10793
+ GCC_except_table10797
+ GCC_except_table10861
+ GCC_except_table11113
+ GCC_except_table11115
+ GCC_except_table11117
+ GCC_except_table11134
+ GCC_except_table11393
+ GCC_except_table11427
+ GCC_except_table11432
+ GCC_except_table11581
+ GCC_except_table11583
+ GCC_except_table11586
+ GCC_except_table11607
+ GCC_except_table11997
+ GCC_except_table12047
+ GCC_except_table12280
+ GCC_except_table12302
+ GCC_except_table12329
+ GCC_except_table12341
+ GCC_except_table12342
+ GCC_except_table12379
+ GCC_except_table12409
+ GCC_except_table12411
+ GCC_except_table12417
+ GCC_except_table12423
+ GCC_except_table12427
+ GCC_except_table12430
+ GCC_except_table12488
+ GCC_except_table12540
+ GCC_except_table12541
+ GCC_except_table12577
+ GCC_except_table12582
+ GCC_except_table12595
+ GCC_except_table12760
+ GCC_except_table12766
+ GCC_except_table12770
+ GCC_except_table12777
+ GCC_except_table12779
+ GCC_except_table12823
+ GCC_except_table12869
+ GCC_except_table12959
+ GCC_except_table12960
+ GCC_except_table12964
+ GCC_except_table12968
+ GCC_except_table2254
+ GCC_except_table2292
+ GCC_except_table2293
+ GCC_except_table2357
+ GCC_except_table2471
+ GCC_except_table2474
+ GCC_except_table2476
+ GCC_except_table2481
+ GCC_except_table2486
+ GCC_except_table2490
+ GCC_except_table2494
+ GCC_except_table2533
+ GCC_except_table2539
+ GCC_except_table2541
+ GCC_except_table2544
+ GCC_except_table2577
+ GCC_except_table2599
+ GCC_except_table2610
+ GCC_except_table2625
+ GCC_except_table2630
+ GCC_except_table2643
+ GCC_except_table2645
+ GCC_except_table2665
+ GCC_except_table2670
+ GCC_except_table2682
+ GCC_except_table2684
+ GCC_except_table2695
+ GCC_except_table2706
+ GCC_except_table2726
+ GCC_except_table2731
+ GCC_except_table2743
+ GCC_except_table2745
+ GCC_except_table2755
+ GCC_except_table2761
+ GCC_except_table2780
+ GCC_except_table2785
+ GCC_except_table2797
+ GCC_except_table2799
+ GCC_except_table2810
+ GCC_except_table2829
+ GCC_except_table2834
+ GCC_except_table2846
+ GCC_except_table2849
+ GCC_except_table2908
+ GCC_except_table2962
+ GCC_except_table2971
+ GCC_except_table2974
+ GCC_except_table2978
+ GCC_except_table2999
+ GCC_except_table3002
+ GCC_except_table3017
+ GCC_except_table3020
+ GCC_except_table3029
+ GCC_except_table3033
+ GCC_except_table3036
+ GCC_except_table3043
+ GCC_except_table3046
+ GCC_except_table3054
+ GCC_except_table3057
+ GCC_except_table3067
+ GCC_except_table3070
+ GCC_except_table3097
+ GCC_except_table3100
+ GCC_except_table3113
+ GCC_except_table3116
+ GCC_except_table3120
+ GCC_except_table3143
+ GCC_except_table3594
+ GCC_except_table3599
+ GCC_except_table3658
+ GCC_except_table3663
+ GCC_except_table3678
+ GCC_except_table3952
+ GCC_except_table4087
+ GCC_except_table4111
+ GCC_except_table4112
+ GCC_except_table4251
+ GCC_except_table4254
+ GCC_except_table4335
+ GCC_except_table4350
+ GCC_except_table4354
+ GCC_except_table4355
+ GCC_except_table4358
+ GCC_except_table4359
+ GCC_except_table4363
+ GCC_except_table4368
+ GCC_except_table4492
+ GCC_except_table4752
+ GCC_except_table4894
+ GCC_except_table4902
+ GCC_except_table4903
+ GCC_except_table4911
+ GCC_except_table4921
+ GCC_except_table4931
+ GCC_except_table4936
+ GCC_except_table4942
+ GCC_except_table4943
+ GCC_except_table4951
+ GCC_except_table4959
+ GCC_except_table4962
+ GCC_except_table4967
+ GCC_except_table4970
+ GCC_except_table4977
+ GCC_except_table4978
+ GCC_except_table4984
+ GCC_except_table5144
+ GCC_except_table5147
+ GCC_except_table5167
+ GCC_except_table5174
+ GCC_except_table5175
+ GCC_except_table5570
+ GCC_except_table5571
+ GCC_except_table5582
+ GCC_except_table5597
+ GCC_except_table5602
+ GCC_except_table5605
+ GCC_except_table5618
+ GCC_except_table5619
+ GCC_except_table5623
+ GCC_except_table5628
+ GCC_except_table5651
+ GCC_except_table5658
+ GCC_except_table5659
+ GCC_except_table5663
+ GCC_except_table5674
+ GCC_except_table5678
+ GCC_except_table5695
+ GCC_except_table5696
+ GCC_except_table5707
+ GCC_except_table5708
+ GCC_except_table5774
+ GCC_except_table5831
+ GCC_except_table5832
+ GCC_except_table5835
+ GCC_except_table5838
+ GCC_except_table5845
+ GCC_except_table603
+ GCC_except_table607
+ GCC_except_table6083
+ GCC_except_table612
+ GCC_except_table614
+ GCC_except_table6149
+ GCC_except_table6159
+ GCC_except_table616
+ GCC_except_table6163
+ GCC_except_table6164
+ GCC_except_table6169
+ GCC_except_table6172
+ GCC_except_table6177
+ GCC_except_table6188
+ GCC_except_table6204
+ GCC_except_table6208
+ GCC_except_table6228
+ GCC_except_table6282
+ GCC_except_table6306
+ GCC_except_table6307
+ GCC_except_table6321
+ GCC_except_table6324
+ GCC_except_table6343
+ GCC_except_table6349
+ GCC_except_table6369
+ GCC_except_table6375
+ GCC_except_table6382
+ GCC_except_table6383
+ GCC_except_table6429
+ GCC_except_table6435
+ GCC_except_table6438
+ GCC_except_table6478
+ GCC_except_table6487
+ GCC_except_table6499
+ GCC_except_table652
+ GCC_except_table670
+ GCC_except_table673
+ GCC_except_table6812
+ GCC_except_table6817
+ GCC_except_table6846
+ GCC_except_table6850
+ GCC_except_table6851
+ GCC_except_table6857
+ GCC_except_table6876
+ GCC_except_table6883
+ GCC_except_table6884
+ GCC_except_table6891
+ GCC_except_table6955
+ GCC_except_table6956
+ GCC_except_table6960
+ GCC_except_table7106
+ GCC_except_table724
+ GCC_except_table729
+ GCC_except_table740
+ GCC_except_table745
+ GCC_except_table750
+ GCC_except_table753
+ GCC_except_table755
+ GCC_except_table7560
+ GCC_except_table7567
+ GCC_except_table7573
+ GCC_except_table7574
+ GCC_except_table7577
+ GCC_except_table7586
+ GCC_except_table7592
+ GCC_except_table7593
+ GCC_except_table7600
+ GCC_except_table7601
+ GCC_except_table7606
+ GCC_except_table7627
+ GCC_except_table763
+ GCC_except_table7634
+ GCC_except_table7639
+ GCC_except_table7644
+ GCC_except_table7649
+ GCC_except_table7652
+ GCC_except_table766
+ GCC_except_table7660
+ GCC_except_table7668
+ GCC_except_table7688
+ GCC_except_table7689
+ GCC_except_table770
+ GCC_except_table7874
+ GCC_except_table798
+ GCC_except_table803
+ GCC_except_table806
+ GCC_except_table808
+ GCC_except_table8096
+ GCC_except_table8101
+ GCC_except_table8102
+ GCC_except_table8121
+ GCC_except_table8122
+ GCC_except_table814
+ GCC_except_table819
+ GCC_except_table821
+ GCC_except_table823
+ GCC_except_table8235
+ GCC_except_table8237
+ GCC_except_table8241
+ GCC_except_table8245
+ GCC_except_table8283
+ GCC_except_table8286
+ GCC_except_table8287
+ GCC_except_table8290
+ GCC_except_table8292
+ GCC_except_table8300
+ GCC_except_table8309
+ GCC_except_table8311
+ GCC_except_table8312
+ GCC_except_table8313
+ GCC_except_table8314
+ GCC_except_table832
+ GCC_except_table8320
+ GCC_except_table8347
+ GCC_except_table8351
+ GCC_except_table8352
+ GCC_except_table8353
+ GCC_except_table841
+ GCC_except_table844
+ GCC_except_table8472
+ GCC_except_table8473
+ GCC_except_table8475
+ GCC_except_table8478
+ GCC_except_table8483
+ GCC_except_table8485
+ GCC_except_table8490
+ GCC_except_table8493
+ GCC_except_table850
+ GCC_except_table8500
+ GCC_except_table8503
+ GCC_except_table8512
+ GCC_except_table8513
+ GCC_except_table8515
+ GCC_except_table8525
+ GCC_except_table8527
+ GCC_except_table8530
+ GCC_except_table8537
+ GCC_except_table8538
+ GCC_except_table854
+ GCC_except_table8545
+ GCC_except_table8550
+ GCC_except_table8552
+ GCC_except_table8556
+ GCC_except_table8558
+ GCC_except_table8560
+ GCC_except_table8562
+ GCC_except_table8563
+ GCC_except_table8567
+ GCC_except_table8569
+ GCC_except_table8571
+ GCC_except_table8573
+ GCC_except_table8590
+ GCC_except_table8593
+ GCC_except_table8597
+ GCC_except_table8600
+ GCC_except_table8601
+ GCC_except_table8607
+ GCC_except_table8619
+ GCC_except_table8627
+ GCC_except_table863
+ GCC_except_table8633
+ GCC_except_table8634
+ GCC_except_table8644
+ GCC_except_table8646
+ GCC_except_table8648
+ GCC_except_table8652
+ GCC_except_table8654
+ GCC_except_table8655
+ GCC_except_table8656
+ GCC_except_table8657
+ GCC_except_table8659
+ GCC_except_table8674
+ GCC_except_table868
+ GCC_except_table8754
+ GCC_except_table8756
+ GCC_except_table8765
+ GCC_except_table8766
+ GCC_except_table8768
+ GCC_except_table8769
+ GCC_except_table8779
+ GCC_except_table8780
+ GCC_except_table8783
+ GCC_except_table8790
+ GCC_except_table8791
+ GCC_except_table8800
+ GCC_except_table8802
+ GCC_except_table8804
+ GCC_except_table8893
+ GCC_except_table8899
+ GCC_except_table8900
+ GCC_except_table8904
+ GCC_except_table8905
+ GCC_except_table8910
+ GCC_except_table8911
+ GCC_except_table8912
+ GCC_except_table8913
+ GCC_except_table8918
+ GCC_except_table8922
+ GCC_except_table8924
+ GCC_except_table8969
+ GCC_except_table8974
+ GCC_except_table8976
+ GCC_except_table8977
+ GCC_except_table910
+ GCC_except_table914
+ GCC_except_table917
+ GCC_except_table9304
+ GCC_except_table9313
+ GCC_except_table9316
+ GCC_except_table9317
+ GCC_except_table9318
+ GCC_except_table9319
+ GCC_except_table9320
+ GCC_except_table9324
+ GCC_except_table9325
+ GCC_except_table9328
+ GCC_except_table935
+ GCC_except_table9457
+ GCC_except_table9464
+ GCC_except_table9465
+ GCC_except_table9486
+ GCC_except_table9497
+ GCC_except_table9565
+ GCC_except_table9566
+ GCC_except_table9571
+ GCC_except_table9572
+ GCC_except_table9573
+ GCC_except_table9574
+ GCC_except_table958
+ GCC_except_table9601
+ GCC_except_table9627
+ GCC_except_table9642
+ GCC_except_table9646
+ GCC_except_table967
+ GCC_except_table9671
+ GCC_except_table9672
+ GCC_except_table9680
+ GCC_except_table9684
+ GCC_except_table9685
+ GCC_except_table9686
+ GCC_except_table969
+ GCC_except_table9690
+ GCC_except_table9693
+ GCC_except_table9696
+ GCC_except_table9721
+ GCC_except_table9723
+ GCC_except_table9724
+ GCC_except_table9726
+ GCC_except_table9727
+ GCC_except_table9745
+ GCC_except_table9790
+ GCC_except_table9812
+ GCC_except_table9813
+ GCC_except_table9815
+ GCC_except_table9817
+ GCC_except_table9895
+ _OBJC_CLASS_$_CADisplayFrameRateAssertion
+ _OBJC_IVAR_$_CADisplayFrameRateAssertion._active
+ _OBJC_IVAR_$_CADisplayFrameRateAssertion._client_port
+ _OBJC_IVAR_$_CADisplayFrameRateAssertion._display_id
+ _OBJC_IVAR_$_CADisplayFrameRateAssertion._identifier
+ _OBJC_IVAR_$_CADisplayFrameRateAssertion._invalidated
+ _OBJC_IVAR_$_CADisplayFrameRateAssertion._maximum_frame_rate
+ _OBJC_IVAR_$_CADisplayFrameRateAssertion._server_port
+ _OBJC_METACLASS_$_CADisplayFrameRateAssertion
+ _SILManagerSetParameter
+ __OBJC_$_CLASS_METHODS_CADisplayLink(CAOverrideCreation|CADisplayLinkPrivate|CADisplayLinkInternal)
+ __OBJC_$_INSTANCE_METHODS_CADisplayFrameRateAssertion(Internal)
+ __OBJC_$_INSTANCE_METHODS_CADisplayLink(CAOverrideCreation|CADisplayLinkPrivate|CADisplayLinkInternal)
+ __OBJC_$_INSTANCE_VARIABLES_CADisplayFrameRateAssertion
+ __OBJC_$_PROP_LIST_CADisplayFrameRateAssertion
+ __OBJC_CLASS_PROTOCOLS_$_CADisplayFrameRateAssertion
+ __OBJC_CLASS_RO_$_CADisplayFrameRateAssertion
+ __OBJC_METACLASS_RO_$_CADisplayFrameRateAssertion
+ __XCopyDisplayFrameRateAssertionInfo
+ __XCreateDisplayFrameRateAssertion
+ __XDestroyDisplayFrameRateAssertion
+ __ZN2CA12WindowServer12IOMFBDisplay27create_frame_rate_assertionEPNS_6Render6ObjectEPvS5_
+ __ZN2CA12WindowServer12IOMFBDisplay28destroy_frame_rate_assertionEPNS_6Render6ObjectEPvS5_
+ __ZN2CA12WindowServer12IOMFBDisplay30copy_frame_rate_assertion_infoEPNS_6Render6ObjectEPvS5_
+ __ZN2CA12WindowServer12IOMFBDisplay38update_frame_rate_assertion_cap_lockedEv
+ __ZN2CA12WindowServer6Server29on_secure_indicator_assertionEPNS_6Render6ObjectEPvS5_
+ __ZN2CA12WindowServerL37handle_frame_rate_assertion_dead_nameEj
+ __ZN2CA3OGL12_GLOBAL__N_124GradientContourRectState4map_ERKNS0_9RectStateEPNS_4Vec4IdEEPNS0_6VertexEm
+ __ZN2CA3OGLL34emit_sdf_key_fill_highlight_simpleERNS0_7ContextEfffNS_4Vec2IfEENS_4Vec4IfEEfffS4_S6_PNS0_7SurfaceEfPKNS0_5LayerEffb
+ __ZN2CA6Render14FlattenManager12delete_entryEPNS0_6HandleEPKNS0_6UpdateEPNS0_9LayerNodeEPKc
+ __ZN2CA6Render5Layer19string_from_gravityENS0_12LayerGravityE
+ __ZN2CA6Render7UpdaterL27frame_transform_to_ancestorEPKNS0_5LayerES4_RNS_4Mat4IdEE
+ __ZN2CA7Display15DisplayLinkItem31unregister_frame_interval_rangeEb
+ __ZN2CA7Display15DisplayLinkItemC2EPNS0_7DisplayEPKvP13objc_selectorb
+ __ZThn1568_N2CA12WindowServer11AccelServer10test_fenceEm
+ __ZThn1568_N2CA12WindowServer11AccelServer12delete_fenceEm
+ __ZThn1568_N2CA12WindowServer11AccelServer15supports_fencesEv
+ __ZThn1568_N2CA12WindowServer11AccelServer20flush_command_streamEv
+ __ZThn1568_N2CA12WindowServer11AccelServer9set_fenceEv
+ __ZZ46CADeviceSupportsImmediateRenderLatencyRecoveryE1b
+ __ZZ46CADeviceSupportsImmediateRenderLatencyRecoveryE4once
+ __ZZN2CA2CG12_GLOBAL__N_120RadialGradientDrawer4drawEvENK3$_0clEdPKfdS5_bb
+ __ZZZ20get_setters_for_typeIN2CA6Render9LayerHostEERKDavEUb_ENUlP11CALayerHostPKS2_PKNS1_5LayerERKNSt3__112basic_stringIcNSD_11char_traitsIcEENSD_9allocatorIcEEEER25ReverseSerializationStateE12_8__invokeES7_S9_SC_SL_SN_
+ ___CADeviceSupportsImmediateRenderLatencyRecovery_block_invoke
+ _objc_msgSend$_copyAllFrameRateAssertionInfo
+ _objc_msgSend$_displayLinkWithDisplay:target:selector:skipsOverrides:
+ _objc_msgSend$_initWithDisplayId:maximumFrameRate:identifier:
+ _objc_msgSend$hostedContextGravity
+ _objc_msgSend$setHostedContextGravity:
- GCC_except_table10010
- GCC_except_table10012
- GCC_except_table10156
- GCC_except_table10195
- GCC_except_table10350
- GCC_except_table10519
- GCC_except_table10566
- GCC_except_table10605
- GCC_except_table10769
- GCC_except_table10772
- GCC_except_table10773
- GCC_except_table10777
- GCC_except_table10841
- GCC_except_table11093
- GCC_except_table11094
- GCC_except_table11095
- GCC_except_table11097
- GCC_except_table11373
- GCC_except_table11407
- GCC_except_table11412
- GCC_except_table11561
- GCC_except_table11563
- GCC_except_table11566
- GCC_except_table11587
- GCC_except_table11976
- GCC_except_table12026
- GCC_except_table12255
- GCC_except_table12277
- GCC_except_table12279
- GCC_except_table12316
- GCC_except_table12317
- GCC_except_table12354
- GCC_except_table12384
- GCC_except_table12386
- GCC_except_table12392
- GCC_except_table12398
- GCC_except_table12402
- GCC_except_table12405
- GCC_except_table12463
- GCC_except_table12515
- GCC_except_table12516
- GCC_except_table12552
- GCC_except_table12557
- GCC_except_table12570
- GCC_except_table12735
- GCC_except_table12741
- GCC_except_table12745
- GCC_except_table12752
- GCC_except_table12754
- GCC_except_table12798
- GCC_except_table12841
- GCC_except_table12931
- GCC_except_table12932
- GCC_except_table12936
- GCC_except_table12940
- GCC_except_table2253
- GCC_except_table2291
- GCC_except_table2356
- GCC_except_table2470
- GCC_except_table2473
- GCC_except_table2475
- GCC_except_table2480
- GCC_except_table2485
- GCC_except_table2489
- GCC_except_table2493
- GCC_except_table2531
- GCC_except_table2535
- GCC_except_table2540
- GCC_except_table2543
- GCC_except_table2576
- GCC_except_table2598
- GCC_except_table2609
- GCC_except_table2624
- GCC_except_table2629
- GCC_except_table2642
- GCC_except_table2644
- GCC_except_table2664
- GCC_except_table2669
- GCC_except_table2681
- GCC_except_table2683
- GCC_except_table2694
- GCC_except_table2705
- GCC_except_table2725
- GCC_except_table2730
- GCC_except_table2742
- GCC_except_table2744
- GCC_except_table2754
- GCC_except_table2760
- GCC_except_table2779
- GCC_except_table2784
- GCC_except_table2796
- GCC_except_table2798
- GCC_except_table2809
- GCC_except_table2828
- GCC_except_table2833
- GCC_except_table2845
- GCC_except_table2848
- GCC_except_table2907
- GCC_except_table2961
- GCC_except_table2970
- GCC_except_table2973
- GCC_except_table2977
- GCC_except_table2998
- GCC_except_table3001
- GCC_except_table3015
- GCC_except_table3018
- GCC_except_table3027
- GCC_except_table3031
- GCC_except_table3034
- GCC_except_table3041
- GCC_except_table3044
- GCC_except_table3052
- GCC_except_table3055
- GCC_except_table3065
- GCC_except_table3068
- GCC_except_table3095
- GCC_except_table3098
- GCC_except_table3111
- GCC_except_table3114
- GCC_except_table3118
- GCC_except_table3141
- GCC_except_table3592
- GCC_except_table3597
- GCC_except_table3656
- GCC_except_table3661
- GCC_except_table3676
- GCC_except_table3950
- GCC_except_table4085
- GCC_except_table4109
- GCC_except_table4110
- GCC_except_table4249
- GCC_except_table4250
- GCC_except_table4333
- GCC_except_table4346
- GCC_except_table4352
- GCC_except_table4353
- GCC_except_table4356
- GCC_except_table4357
- GCC_except_table4361
- GCC_except_table4366
- GCC_except_table4490
- GCC_except_table4750
- GCC_except_table4890
- GCC_except_table4899
- GCC_except_table4900
- GCC_except_table4907
- GCC_except_table4919
- GCC_except_table4929
- GCC_except_table4934
- GCC_except_table4939
- GCC_except_table4940
- GCC_except_table4949
- GCC_except_table4955
- GCC_except_table4958
- GCC_except_table4963
- GCC_except_table4964
- GCC_except_table4975
- GCC_except_table4976
- GCC_except_table4980
- GCC_except_table5142
- GCC_except_table5145
- GCC_except_table5163
- GCC_except_table5172
- GCC_except_table5173
- GCC_except_table5565
- GCC_except_table5568
- GCC_except_table5580
- GCC_except_table5595
- GCC_except_table5598
- GCC_except_table5603
- GCC_except_table5616
- GCC_except_table5617
- GCC_except_table5621
- GCC_except_table5626
- GCC_except_table5647
- GCC_except_table5656
- GCC_except_table5657
- GCC_except_table5661
- GCC_except_table5670
- GCC_except_table5676
- GCC_except_table5692
- GCC_except_table5693
- GCC_except_table5699
- GCC_except_table5706
- GCC_except_table5770
- GCC_except_table5829
- GCC_except_table5830
- GCC_except_table5833
- GCC_except_table5834
- GCC_except_table5843
- GCC_except_table604
- GCC_except_table6081
- GCC_except_table610
- GCC_except_table613
- GCC_except_table6147
- GCC_except_table615
- GCC_except_table6157
- GCC_except_table6161
- GCC_except_table6162
- GCC_except_table6167
- GCC_except_table6170
- GCC_except_table6175
- GCC_except_table618
- GCC_except_table6186
- GCC_except_table6202
- GCC_except_table6206
- GCC_except_table6226
- GCC_except_table6280
- GCC_except_table6304
- GCC_except_table6305
- GCC_except_table6319
- GCC_except_table6322
- GCC_except_table6341
- GCC_except_table6347
- GCC_except_table6367
- GCC_except_table6373
- GCC_except_table6380
- GCC_except_table6381
- GCC_except_table6427
- GCC_except_table6433
- GCC_except_table6436
- GCC_except_table6476
- GCC_except_table6485
- GCC_except_table6497
- GCC_except_table653
- GCC_except_table671
- GCC_except_table674
- GCC_except_table6810
- GCC_except_table6813
- GCC_except_table6842
- GCC_except_table6848
- GCC_except_table6849
- GCC_except_table6853
- GCC_except_table6874
- GCC_except_table6881
- GCC_except_table6882
- GCC_except_table6889
- GCC_except_table6953
- GCC_except_table6954
- GCC_except_table6958
- GCC_except_table7104
- GCC_except_table725
- GCC_except_table733
- GCC_except_table742
- GCC_except_table746
- GCC_except_table751
- GCC_except_table754
- GCC_except_table7558
- GCC_except_table756
- GCC_except_table7565
- GCC_except_table7569
- GCC_except_table7570
- GCC_except_table7575
- GCC_except_table7584
- GCC_except_table7589
- GCC_except_table7590
- GCC_except_table7596
- GCC_except_table7599
- GCC_except_table7604
- GCC_except_table7625
- GCC_except_table7632
- GCC_except_table7633
- GCC_except_table764
- GCC_except_table7642
- GCC_except_table7646
- GCC_except_table7647
- GCC_except_table7658
- GCC_except_table7662
- GCC_except_table767
- GCC_except_table7686
- GCC_except_table7687
- GCC_except_table772
- GCC_except_table7870
- GCC_except_table799
- GCC_except_table804
- GCC_except_table807
- GCC_except_table8083
- GCC_except_table8088
- GCC_except_table8089
- GCC_except_table809
- GCC_except_table8094
- GCC_except_table8106
- GCC_except_table815
- GCC_except_table820
- GCC_except_table8219
- GCC_except_table822
- GCC_except_table8221
- GCC_except_table8225
- GCC_except_table8229
- GCC_except_table824
- GCC_except_table8267
- GCC_except_table8270
- GCC_except_table8271
- GCC_except_table8274
- GCC_except_table8276
- GCC_except_table8277
- GCC_except_table8279
- GCC_except_table8280
- GCC_except_table8281
- GCC_except_table8284
- GCC_except_table8298
- GCC_except_table8304
- GCC_except_table8331
- GCC_except_table8335
- GCC_except_table8336
- GCC_except_table8337
- GCC_except_table835
- GCC_except_table842
- GCC_except_table845
- GCC_except_table8456
- GCC_except_table8457
- GCC_except_table8458
- GCC_except_table8459
- GCC_except_table8461
- GCC_except_table8462
- GCC_except_table8467
- GCC_except_table8469
- GCC_except_table8471
- GCC_except_table8480
- GCC_except_table8481
- GCC_except_table8484
- GCC_except_table8494
- GCC_except_table8499
- GCC_except_table8505
- GCC_except_table8507
- GCC_except_table8509
- GCC_except_table851
- GCC_except_table8511
- GCC_except_table8514
- GCC_except_table8520
- GCC_except_table8522
- GCC_except_table8528
- GCC_except_table8529
- GCC_except_table8531
- GCC_except_table8534
- GCC_except_table8535
- GCC_except_table8540
- GCC_except_table8541
- GCC_except_table8546
- GCC_except_table855
- GCC_except_table8553
- GCC_except_table8574
- GCC_except_table8577
- GCC_except_table8581
- GCC_except_table8584
- GCC_except_table8585
- GCC_except_table8587
- GCC_except_table8591
- GCC_except_table8611
- GCC_except_table8612
- GCC_except_table8614
- GCC_except_table8617
- GCC_except_table8618
- GCC_except_table8620
- GCC_except_table8632
- GCC_except_table8638
- GCC_except_table8639
- GCC_except_table864
- GCC_except_table8640
- GCC_except_table8641
- GCC_except_table8643
- GCC_except_table8658
- GCC_except_table869
- GCC_except_table8738
- GCC_except_table8740
- GCC_except_table8747
- GCC_except_table8748
- GCC_except_table8749
- GCC_except_table8750
- GCC_except_table8751
- GCC_except_table8752
- GCC_except_table8753
- GCC_except_table8759
- GCC_except_table8772
- GCC_except_table8774
- GCC_except_table8784
- GCC_except_table8786
- GCC_except_table8877
- GCC_except_table8878
- GCC_except_table8879
- GCC_except_table8880
- GCC_except_table8883
- GCC_except_table8884
- GCC_except_table8888
- GCC_except_table8889
- GCC_except_table8897
- GCC_except_table8902
- GCC_except_table8906
- GCC_except_table8908
- GCC_except_table8953
- GCC_except_table8958
- GCC_except_table8960
- GCC_except_table8961
- GCC_except_table911
- GCC_except_table916
- GCC_except_table918
- GCC_except_table9287
- GCC_except_table9296
- GCC_except_table9299
- GCC_except_table9300
- GCC_except_table9301
- GCC_except_table9302
- GCC_except_table9303
- GCC_except_table9307
- GCC_except_table9308
- GCC_except_table9311
- GCC_except_table937
- GCC_except_table9440
- GCC_except_table9447
- GCC_except_table9448
- GCC_except_table9469
- GCC_except_table9480
- GCC_except_table9548
- GCC_except_table9549
- GCC_except_table9554
- GCC_except_table9555
- GCC_except_table9556
- GCC_except_table9557
- GCC_except_table9584
- GCC_except_table959
- GCC_except_table9610
- GCC_except_table9612
- GCC_except_table9625
- GCC_except_table9654
- GCC_except_table9655
- GCC_except_table9656
- GCC_except_table9658
- GCC_except_table9660
- GCC_except_table9662
- GCC_except_table9663
- GCC_except_table9667
- GCC_except_table9668
- GCC_except_table9669
- GCC_except_table9676
- GCC_except_table968
- GCC_except_table9704
- GCC_except_table9706
- GCC_except_table9707
- GCC_except_table9710
- GCC_except_table9773
- GCC_except_table9795
- GCC_except_table9796
- GCC_except_table9798
- GCC_except_table9800
- GCC_except_table984
- GCC_except_table9878
- GCC_except_table9989
- GCC_except_table9991
- __OBJC_$_CLASS_METHODS_CADisplayLink(CADisplayLinkPrivate|CADisplayLinkInternal)
- __OBJC_$_INSTANCE_METHODS_CADisplayLink(CADisplayLinkPrivate|CADisplayLinkInternal)
- __ZN2CA12WindowServer12IOMFBDisplay32emit_server_timing_update_lockedEv
- __ZN2CA3OGLL34emit_sdf_key_fill_highlight_simpleERNS0_7ContextEfffNS_4Vec2IfEENS_4Vec4IfEEfffS4_S6_PNS0_7SurfaceEfPKNS0_5LayerEff
- __ZN2CA6Render14FlattenManager12delete_entryEPNS0_6HandleEPKNS0_6UpdateEPKc
- __ZN2CA6Render28invoke_presentation_handlersERKNSt3__13setINS0_6Update11ContextInfoENS1_4lessIS4_EENS1_9allocatorIS4_EEEEjdyym
- __ZN2CA7Display15DisplayLinkItem31unregister_frame_interval_rangeEv
- __ZN2CA7Display15DisplayLinkItemC2EPNS0_7DisplayEPKvP13objc_selector
- __ZThn1544_N2CA12WindowServer11AccelServer10test_fenceEm
- __ZThn1544_N2CA12WindowServer11AccelServer12delete_fenceEm
- __ZThn1544_N2CA12WindowServer11AccelServer15supports_fencesEv
- __ZThn1544_N2CA12WindowServer11AccelServer20flush_command_streamEv
- __ZThn1544_N2CA12WindowServer11AccelServer9set_fenceEv
- __ZZN2CA7Display7Display6updateEvE14is_springboard
- __ZZN2CA7Display7Display6updateEvE19is_springboard_once
- ____ZN2CA7Display7Display6updateEv_block_invoke
- _getprogname
- _objc_msgSend$resizesHostedContext
CStrings:
+ "\t\t %g Hz from %s[%d] since %.0f seconds ago\n"
+ "\tframeRateAssertions:\n%s"
+ "   element[%u] mid=(%g,%g) half_size=(%g,%g) radius=%g inside_fill=%g maskable=%d"
+ "  compute disabled:%s%s%s%s%s%s%s%s\n"
+ " edge_clear_incremental"
+ "\"Duplicated Entry !!\" && map.map.find (\"resizesHostedContext\") == map.map.end ()"
+ "(hosted-context-gravity %s)"
+ "24A5401k"
+ "<no name>"
+ "Bounds H"
+ "Bounds W"
+ "Bounds X"
+ "Bounds Y"
+ "CADisplayFrameRateAssertion"
+ "CAFrameRateClient: pid %i register to server %u %u %u for display %u"
+ "CAFrameRateClient: register %u %u %u for display %u"
+ "CAFrameRateClient: unregister %u %u %u for display %u"
+ "CAFrameRateClient: update %u %u %u to %u %u %u for display %u"
+ "CAFrameRateServer: receiving registration %u %u %u%s from %d[%s] for display %u"
+ "CA_PRINT_GAIN_MAPS"
+ "Circular"
+ "Continuous"
+ "Creating frame rate assertion for display=%u pid=%i port=%u maximum_frame_rate=%g"
+ "DarkBoot: suppressing boot content on display %u"
+ "Destroying frame rate assertion for display=%u pid=%i port=%u maximum_frame_rate=%g"
+ "Display %u encoding %u element%s bounds=(%d,%d,%d,%d) RTR_strength=%g"
+ "Display %u layer[%u] '%s' mode=%s bounds=(%g,%g,%g,%g) radius=%g curve=%s disable_res_transition=%d res_transition_strength=%g maskable=%d intersects_contents=%d pinned=%d"
+ "Display %u no CAGainMapLayers in update"
+ "Display %u uuid length %zu"
+ "Display %u uuid set "
+ "Encoded Elements"
+ "Gain Map"
+ "ID0"
+ "ID1"
+ "No frame rate assertion found on display %u for port %u"
+ "PurpleGfxMem2"
+ "RTR Strength"
+ "The frame rate assertion (%@) is already active."
+ "The frame rate assertion (%@) is already invalidated."
+ "The frame rate assertion (%@) is deallocated without calling -invalidate first."
+ "The frame rate assertion (%@) is not active."
+ "Unable to get frame rate assertions 0x%x"
+ "active: %i, invalidated: %i, maximumFrameRate: %g, identifier: %@"
+ "hosted_context_gravity"
+ "kern.darkboot"
+ "resizesHostedContext"
- "  compute disabled:%s%s%s%s%s%s%s\n"
- "(resizes-hosted-context true)"
- "24A5389s"
- "CAFrameRateClient: pid %i register to server %u %u %u"
- "CAFrameRateClient: register %u %u %u"
- "CAFrameRateClient: unregister %u %u %u"
- "CAFrameRateClient: update %u %u %u to %u %u %u"
- "CAFrameRateServer: receiving registration %u %u %u%s from %d[%s]"
- "Display %u uuid changed to %{public}@"
- "Display %u uuid set to %{public}s"
- "Display %u uuid will change"
- "_intermediate_surf.iosurface"
- "get_intermediate_surface"
- "resizes_hosted_context"
```
