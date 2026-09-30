## WebKit

> `/System/Library/Frameworks/WebKit.framework/WebKit`

```diff

-621.2.5.10.10
-  __TEXT.__text: 0xfadadc
-  __TEXT.__auth_stubs: 0x184f0
+621.3.6.10.1
+  __TEXT.__text: 0xfaec10
+  __TEXT.__auth_stubs: 0x184b0
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x19474
-  __TEXT.__const: 0x35f8
+  __TEXT.__objc_methlist: 0x19494
+  __TEXT.__const: 0x3628
   __TEXT.__swift5_typeref: 0x12e
   __TEXT.__swift5_capture: 0xd0
   __TEXT.__constg_swiftt: 0x28
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__cstring: 0x2fe958
+  __TEXT.__cstring: 0x2ff6cb
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__gcc_except_tab: 0x646cc
+  __TEXT.__gcc_except_tab: 0x648a4
   __TEXT.__oslogstring: 0x425e8
   __TEXT.__ustring: 0xd40
-  __TEXT.__unwind_info: 0x292c8
+  __TEXT.__unwind_info: 0x29310
   __TEXT.__eh_frame: 0x3c8
   __TEXT.__objc_classname: 0x32a2
-  __TEXT.__objc_methname: 0x47fa1
+  __TEXT.__objc_methname: 0x48050
   __TEXT.__objc_methtype: 0x36cee
-  __TEXT.__objc_stubs: 0x2a680
+  __TEXT.__objc_stubs: 0x2a6e0
   __DATA_CONST.__got: 0x1ec0
-  __DATA_CONST.__const: 0x1e130
+  __DATA_CONST.__const: 0x1e158
   __DATA_CONST.__objc_classlist: 0xbb8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x410
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x101b0
+  __DATA_CONST.__objc_selrefs: 0x101d0
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x990
-  __DATA_CONST.__objc_arraydata: 0x688
-  __AUTH_CONST.__auth_got: 0xc290
-  __AUTH_CONST.__const: 0x64a18
-  __AUTH_CONST.__cfstring: 0x136e0
-  __AUTH_CONST.__objc_const: 0x26f90
+  __DATA_CONST.__objc_arraydata: 0x630
+  __AUTH_CONST.__auth_got: 0xc270
+  __AUTH_CONST.__const: 0x64a48
+  __AUTH_CONST.__cfstring: 0x13760
+  __AUTH_CONST.__objc_const: 0x26fa0
   __AUTH_CONST.__objc_intobj: 0x6f0
-  __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH_CONST.__objc_dictobj: 0x208
+  __AUTH_CONST.__objc_dictobj: 0x1e0
+  __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x5320
   __AUTH.__data: 0x298
   __DATA.__objc_ivar: 0xf78
-  __DATA.__data: 0x3670
+  __DATA.__data: 0x3640
   __DATA.__bss: 0xd38
-  __DATA.__common: 0x1178
+  __DATA.__common: 0x1170
   __DATA_DIRTY.__objc_ivar: 0x510
   __DATA_DIRTY.__objc_data: 0x2210
   __DATA_DIRTY.__data: 0x5d88

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 4A095C3B-389A-32D5-A148-FECA0ACD1CC9
-  Functions: 69118
-  Symbols:   190115
-  CStrings:  31481
+  UUID: AF2C8490-026B-398D-9385-33A0FA97D21C
+  Functions: 69136
+  Symbols:   190146
+  CStrings:  31497
 
Symbols:
+ -[WKNavigationAction(WKPrivate) _isContentExtensionRedirect]
+ -[_WKWebExtensionDeclarativeNetRequestRule _allChromeResourceTypesForCondition:]
+ -[_WKWebExtensionDeclarativeNetRequestRule _combineRequestDomain:withURLFilter:]
+ -[_WKWebExtensionDeclarativeNetRequestRule _convertRulesWithModifiedCondition:webKitActionType:chromeActionType:]
+ -[_WKWebExtensionDeclarativeNetRequestRule _findLongestCommonSubstringWithString:andString:]
+ -[_WKWebExtensionDeclarativeNetRequestRule _webKitRuleWithWebKitActionType:chromeActionType:condition:]
+ GCC_except_table2907
+ GCC_except_table2912
+ GCC_except_table2915
+ GCC_except_table2920
+ GCC_except_table2927
+ GCC_except_table2932
+ GCC_except_table2934
+ GCC_except_table2937
+ GCC_except_table2943
+ GCC_except_table2948
+ GCC_except_table4689
+ GCC_except_table4704
+ GCC_except_table4726
+ GCC_except_table4734
+ GCC_except_table4744
+ GCC_except_table4768
+ GCC_except_table4776
+ GCC_except_table4781
+ GCC_except_table4793
+ GCC_except_table4801
+ GCC_except_table4836
+ GCC_except_table4850
+ GCC_except_table4860
+ GCC_except_table4900
+ GCC_except_table4909
+ GCC_except_table4928
+ GCC_except_table4936
+ GCC_except_table4941
+ GCC_except_table4948
+ GCC_except_table4952
+ GCC_except_table4969
+ GCC_except_table4974
+ GCC_except_table4990
+ GCC_except_table5002
+ GCC_except_table5006
+ GCC_except_table5016
+ GCC_except_table5026
+ GCC_except_table5040
+ GCC_except_table5062
+ GCC_except_table5065
+ GCC_except_table5070
+ GCC_except_table5075
+ GCC_except_table5078
+ GCC_except_table5087
+ GCC_except_table5096
+ GCC_except_table5105
+ GCC_except_table5121
+ GCC_except_table5148
+ GCC_except_table5152
+ GCC_except_table5158
+ GCC_except_table5161
+ GCC_except_table5166
+ GCC_except_table5178
+ GCC_except_table5185
+ GCC_except_table5197
+ GCC_except_table5203
+ GCC_except_table5207
+ GCC_except_table5210
+ GCC_except_table5224
+ GCC_except_table5233
+ GCC_except_table5235
+ GCC_except_table5242
+ GCC_except_table5247
+ GCC_except_table5253
+ GCC_except_table5258
+ GCC_except_table5262
+ GCC_except_table5264
+ GCC_except_table5271
+ GCC_except_table5282
+ GCC_except_table5287
+ GCC_except_table5290
+ GCC_except_table5304
+ GCC_except_table5317
+ GCC_except_table5332
+ GCC_except_table5351
+ GCC_except_table5361
+ GCC_except_table5389
+ GCC_except_table5395
+ GCC_except_table5400
+ GCC_except_table5408
+ GCC_except_table5412
+ GCC_except_table5429
+ GCC_except_table5431
+ GCC_except_table5438
+ GCC_except_table5450
+ GCC_except_table5453
+ GCC_except_table5459
+ GCC_except_table5482
+ GCC_except_table5486
+ GCC_except_table5500
+ GCC_except_table5503
+ GCC_except_table5506
+ GCC_except_table5513
+ GCC_except_table5519
+ GCC_except_table5522
+ GCC_except_table5526
+ GCC_except_table5536
+ GCC_except_table5557
+ GCC_except_table5577
+ GCC_except_table5585
+ GCC_except_table5598
+ GCC_except_table5628
+ GCC_except_table5636
+ GCC_except_table5644
+ GCC_except_table5659
+ GCC_except_table5674
+ GCC_except_table5697
+ GCC_except_table5717
+ GCC_except_table5739
+ GCC_except_table5760
+ GCC_except_table5789
+ GCC_except_table5799
+ GCC_except_table5801
+ GCC_except_table5831
+ __ZN3IPC13handleMessageIN8Messages20RemoteObjectRegistry14CallReplyBlockENS_10ConnectionEN6WebKit20RemoteObjectRegistryES6_FvRS4_yRKNS5_8UserDataEEEEvRT0_RNS_7DecoderEPT1_MT2_T3_
+ __ZN3WTF23EagerCallbackAggregatorIFvNSt12experimental15fundamentals_v38expectedINS_6StringES4_EEEEC2INS_17CompletionHandlerIFvOS5_EEEEEOT_S5_
+ __ZN3WTF23EagerCallbackAggregatorIFvNSt12experimental15fundamentals_v38expectedINS_6StringES4_EEEED2Ev
+ __ZN3WTF6Detail15CallableWrapperIZNK6WebKit15WebExtensionTab9processesENS2_29WebExtensionEventListenerTypeENS2_28WebExtensionContentWorldTypeEE3$_0vJRNS2_15WebProcessProxyENS_23ObjectIdentifierGenericIN7WebCore18PageIdentifierTypeENS_38ObjectIdentifierMainThreadAccessTraitsIyEEyEEEE4callES8_SE_
+ __ZN3WTF6Detail15CallableWrapperIZNK6WebKit15WebExtensionTab9processesENS2_29WebExtensionEventListenerTypeENS2_28WebExtensionContentWorldTypeEE3$_0vJRNS2_15WebProcessProxyENS_23ObjectIdentifierGenericIN7WebCore18PageIdentifierTypeENS_38ObjectIdentifierMainThreadAccessTraitsIyEEyEEEED0Ev
+ __ZN3WTF6Detail15CallableWrapperIZNK6WebKit15WebExtensionTab9processesENS2_29WebExtensionEventListenerTypeENS2_28WebExtensionContentWorldTypeEE3$_0vJRNS2_15WebProcessProxyENS_23ObjectIdentifierGenericIN7WebCore18PageIdentifierTypeENS_38ObjectIdentifierMainThreadAccessTraitsIyEEyEEEED1Ev
+ __ZN3WTF6Detail15CallableWrapperIZNK6WebKit15WebExtensionTab9processesENS2_29WebExtensionEventListenerTypeENS2_28WebExtensionContentWorldTypeEE3$_1bJRNS2_15WebProcessProxyERNS2_12WebPageProxyERNS2_13WebFrameProxyEEE4callES8_SA_SC_
+ __ZN3WTF6Detail15CallableWrapperIZNK6WebKit15WebExtensionTab9processesENS2_29WebExtensionEventListenerTypeENS2_28WebExtensionContentWorldTypeEE3$_1bJRNS2_15WebProcessProxyERNS2_12WebPageProxyERNS2_13WebFrameProxyEEED0Ev
+ __ZN3WTF6Detail15CallableWrapperIZNK6WebKit15WebExtensionTab9processesENS2_29WebExtensionEventListenerTypeENS2_28WebExtensionContentWorldTypeEE3$_1bJRNS2_15WebProcessProxyERNS2_12WebPageProxyERNS2_13WebFrameProxyEEED1Ev
+ __ZN3WTF9HashTableINS_3RefIN6WebKit15WebProcessProxyENS_12RawPtrTraitsIS3_EENS_21DefaultRefDerefTraitsIS3_EEEES8_NS_17IdentityExtractorENS_11DefaultHashIS8_EENS_10HashTraitsIS8_EESD_LNS_17ShouldValidateKeyE1EE3addEOS8_
+ __ZN6WebKit20RemoteObjectRegistry14callReplyBlockERN3IPC10ConnectionEyRKNS_8UserDataE
+ __ZN6WebKit23RemoteGraphicsContextGL11drawBuffersENSt3__14spanIKjLm18446744073709551615EEE
+ __ZN6WebKit23RemoteGraphicsContextGL14drawBuffersEXTENSt3__14spanIKjLm18446744073709551615EEE
+ __ZN6WebKit23RemoteGraphicsContextGL21invalidateFramebufferEjNSt3__14spanIKjLm18446744073709551615EEE
+ __ZN6WebKit23RemoteGraphicsContextGL24invalidateSubFramebufferEjNSt3__14spanIKjLm18446744073709551615EEEiiii
+ __ZN7WebCore5Style12BorderRadiusD2Ev
+ __ZNK3WTF8FunctionIFvNSt12experimental15fundamentals_v38expectedINS_6StringES4_EEEEclES5_
+ __ZNK6WebKit19WebExtensionContext9processesEON3WTF7HashSetINS_29WebExtensionEventListenerTypeENS1_11DefaultHashIS3_EENS1_10HashTraitsIS3_EENS1_15HashTableTraitsELNS1_17ShouldValidateKeyE1EEEONS2_INS_28WebExtensionContentWorldTypeENS4_ISC_EENS6_ISC_EES8_LS9_1EEEONS1_8FunctionIFbRNS_15WebProcessProxyERNS_12WebPageProxyERNS_13WebFrameProxyEEEE
+ __ZNK7WebCore26MediaRecorderPrivateWriter24shouldApplyVideoRotationEv
+ __ZNSt3__124__optional_destruct_baseIN7WebCore16FunctionNotationILNS1_10CSSValueIDE8ENS1_5Style5InsetEEELb0EED2B8sn190102Ev
+ __ZNSt3__124__optional_destruct_baseIN7WebCore5Style5InsetELb0EED2B8sn190102Ev
+ __ZTVN3WTF6Detail15CallableWrapperIZNK6WebKit15WebExtensionTab9processesENS2_29WebExtensionEventListenerTypeENS2_28WebExtensionContentWorldTypeEE3$_0vJRNS2_15WebProcessProxyENS_23ObjectIdentifierGenericIN7WebCore18PageIdentifierTypeENS_38ObjectIdentifierMainThreadAccessTraitsIyEEyEEEEE
+ __ZTVN3WTF6Detail15CallableWrapperIZNK6WebKit15WebExtensionTab9processesENS2_29WebExtensionEventListenerTypeENS2_28WebExtensionContentWorldTypeEE3$_1bJRNS2_15WebProcessProxyERNS2_12WebPageProxyERNS2_13WebFrameProxyEEEE
+ __ZZN6WebKit19WebExtensionContext11tabsConnectEN3WTF23ObjectIdentifierGenericINS_29WebExtensionTabIdentifierTypeENS1_38ObjectIdentifierMainThreadAccessTraitsIyEEyEENS2_INS_37WebExtensionPortChannelIdentifierTypeES5_yEENS1_6StringERKNS_35WebExtensionMessageTargetParametersERKNS_35WebExtensionMessageSenderParametersEONS1_17CompletionHandlerIFvONSt12experimental15fundamentals_v38expectedIvS9_EEEEEEN3$_0clEONS1_14HashCountedSetINS2_INS_26WebPageProxyIdentifierTypeES5_yEENS1_11DefaultHashISS_EENS1_10HashTraitsISS_EEEE
+ ___103-[_WKWebExtensionDeclarativeNetRequestRule _webKitRuleWithWebKitActionType:chromeActionType:condition:]_block_invoke
+ ___103-[_WKWebExtensionDeclarativeNetRequestRule _webKitRuleWithWebKitActionType:chromeActionType:condition:]_block_invoke_2
+ ___103-[_WKWebExtensionDeclarativeNetRequestRule _webKitRuleWithWebKitActionType:chromeActionType:condition:]_block_invoke_3
+ ___62-[_WKWebExtensionDeclarativeNetRequestRule ruleInWebKitFormat]_block_invoke
+ ____ZN6WebKitL22launchWithExtensionKitERNS_15ProcessLauncherENS_17ProcessLaunchTypeEPNS0_6ClientEON3WTF8FunctionIFvNS5_17ThreadSafeWeakPtrIS0_NS5_15NoTaggingTraitsIS0_EEEEONS_16ExtensionProcessENS5_12ASCIILiteralEP7NSErrorEEE_block_invoke
+ ____ZN6WebKitL22launchWithExtensionKitERNS_15ProcessLauncherENS_17ProcessLaunchTypeEPNS0_6ClientEON3WTF8FunctionIFvNS5_17ThreadSafeWeakPtrIS0_NS5_15NoTaggingTraitsIS0_EEEEONS_16ExtensionProcessENS5_12ASCIILiteralEP7NSErrorEEE_block_invoke_3
+ ___block_descriptor_40_ea8_32s_e32_"NSDictionary"16?0"NSString"8ls32l8
+ ___block_literal_global.346
+ ___block_literal_global.357
+ _objc_msgSend$_allChromeResourceTypesForCondition:
+ _objc_msgSend$_combineRequestDomain:withURLFilter:
+ _objc_msgSend$_convertRulesWithModifiedCondition:webKitActionType:chromeActionType:
+ _objc_msgSend$_findLongestCommonSubstringWithString:andString:
+ _objc_msgSend$_webKitRuleWithWebKitActionType:chromeActionType:condition:
+ _objc_msgSend$replaceObjectAtIndex:withObject:
+ _objc_msgSend$stringByReplacingCharactersInRange:withString:
- -[_WKWebExtensionDeclarativeNetRequestRule _allChromeResourceTypes]
- -[_WKWebExtensionDeclarativeNetRequestRule _chromeResourceTypeToWebKitLoadContext]
- -[_WKWebExtensionDeclarativeNetRequestRule _convertedRulesForWebKitActionType:chromeActionType:]
- -[_WKWebExtensionDeclarativeNetRequestRule _webKitRuleWithWebKitActionType:chromeActionType:chromeResourceTypes:]
- GCC_except_table2905
- GCC_except_table2914
- GCC_except_table2916
- GCC_except_table2923
- GCC_except_table2928
- GCC_except_table2933
- GCC_except_table2936
- GCC_except_table2939
- GCC_except_table2944
- GCC_except_table2950
- GCC_except_table4688
- GCC_except_table4703
- GCC_except_table4725
- GCC_except_table4733
- GCC_except_table4742
- GCC_except_table4767
- GCC_except_table4775
- GCC_except_table4780
- GCC_except_table4792
- GCC_except_table4800
- GCC_except_table4835
- GCC_except_table4849
- GCC_except_table4859
- GCC_except_table4899
- GCC_except_table4906
- GCC_except_table4926
- GCC_except_table4935
- GCC_except_table4940
- GCC_except_table4946
- GCC_except_table4950
- GCC_except_table4968
- GCC_except_table4973
- GCC_except_table4989
- GCC_except_table5001
- GCC_except_table5005
- GCC_except_table5015
- GCC_except_table5025
- GCC_except_table5039
- GCC_except_table5060
- GCC_except_table5064
- GCC_except_table5069
- GCC_except_table5073
- GCC_except_table5077
- GCC_except_table5086
- GCC_except_table5095
- GCC_except_table5104
- GCC_except_table5118
- GCC_except_table5144
- GCC_except_table5151
- GCC_except_table5157
- GCC_except_table5160
- GCC_except_table5165
- GCC_except_table5177
- GCC_except_table5184
- GCC_except_table5196
- GCC_except_table5202
- GCC_except_table5206
- GCC_except_table5209
- GCC_except_table5223
- GCC_except_table5232
- GCC_except_table5234
- GCC_except_table5241
- GCC_except_table5246
- GCC_except_table5252
- GCC_except_table5256
- GCC_except_table5260
- GCC_except_table5263
- GCC_except_table5270
- GCC_except_table5276
- GCC_except_table5286
- GCC_except_table5289
- GCC_except_table5303
- GCC_except_table5315
- GCC_except_table5331
- GCC_except_table5350
- GCC_except_table5360
- GCC_except_table5388
- GCC_except_table5393
- GCC_except_table5398
- GCC_except_table5406
- GCC_except_table5410
- GCC_except_table5428
- GCC_except_table5430
- GCC_except_table5437
- GCC_except_table5449
- GCC_except_table5452
- GCC_except_table5458
- GCC_except_table5481
- GCC_except_table5485
- GCC_except_table5499
- GCC_except_table5501
- GCC_except_table5505
- GCC_except_table5512
- GCC_except_table5517
- GCC_except_table5521
- GCC_except_table5524
- GCC_except_table5535
- GCC_except_table5556
- GCC_except_table5576
- GCC_except_table5584
- GCC_except_table5597
- GCC_except_table5627
- GCC_except_table5635
- GCC_except_table5643
- GCC_except_table5658
- GCC_except_table5672
- GCC_except_table5695
- GCC_except_table5716
- GCC_except_table5738
- GCC_except_table5759
- GCC_except_table5788
- GCC_except_table5798
- GCC_except_table5800
- GCC_except_table5830
- __ZN3IPC10Connection11cancelReplyIN8Messages24WebExtensionContextProxy27DispatchRuntimeMessageEventEZN6WebKit19WebExtensionContext15tabsSendMessageEN3WTF23ObjectIdentifierGenericINS5_29WebExtensionTabIdentifierTypeENS7_38ObjectIdentifierMainThreadAccessTraitsIyEEyEERKNS7_6StringERKNS5_35WebExtensionMessageTargetParametersERKNS5_35WebExtensionMessageSenderParametersEONS7_17CompletionHandlerIFvONSt12experimental15fundamentals_v38expectedISD_SD_EEEEEE3$_0EEvOT0_
- __ZN3IPC13handleMessageIN8Messages20RemoteObjectRegistry14CallReplyBlockENS_10ConnectionEN6WebKit20RemoteObjectRegistryES6_FvyRKNS5_8UserDataEEEEvRT0_RNS_7DecoderEPT1_MT2_T3_
- __ZN3WTF6Detail15CallableWrapperIZNK6WebKit15WebExtensionTab9processesENS2_29WebExtensionEventListenerTypeENS2_28WebExtensionContentWorldTypeEE3$_0bJRNS2_12WebPageProxyERNS2_13WebFrameProxyEEE4callES8_SA_
- __ZN3WTF6Detail15CallableWrapperIZNK6WebKit15WebExtensionTab9processesENS2_29WebExtensionEventListenerTypeENS2_28WebExtensionContentWorldTypeEE3$_0bJRNS2_12WebPageProxyERNS2_13WebFrameProxyEEED0Ev
- __ZN3WTF6Detail15CallableWrapperIZNK6WebKit15WebExtensionTab9processesENS2_29WebExtensionEventListenerTypeENS2_28WebExtensionContentWorldTypeEE3$_0bJRNS2_12WebPageProxyERNS2_13WebFrameProxyEEED1Ev
- __ZN3WTF9HashTableINS_3RefIN6WebKit15WebProcessProxyENS_12RawPtrTraitsIS3_EENS_21DefaultRefDerefTraitsIS3_EEEES8_NS_17IdentityExtractorENS_11DefaultHashIS8_EENS_10HashTraitsIS8_EESD_LNS_17ShouldValidateKeyE1EE6removeEPS8_
- __ZN6WebKit20RemoteObjectRegistry14callReplyBlockEyRKNS_8UserDataE
- __ZN6WebKit23RemoteGraphicsContextGL24invalidateSubFramebufferEjONSt3__14spanIKjLm18446744073709551615EEEiiii
- __ZN6WebKitL20screenRectOfContentsEPN7WebCore7ElementE
- __ZN7WebCore27PlatformMediaSessionManager28mediaCapabilityGrantsEnabledEv
- __ZN7WebCore27PlatformMediaSessionManager31setMediaCapabilityGrantsEnabledEb
- __ZN7WebCore5Style5InsetD2Ev
- __ZNK6WebKit19WebExtensionContext9processesEON3WTF7HashSetINS_29WebExtensionEventListenerTypeENS1_11DefaultHashIS3_EENS1_10HashTraitsIS3_EENS1_15HashTableTraitsELNS1_17ShouldValidateKeyE1EEEONS2_INS_28WebExtensionContentWorldTypeENS4_ISC_EENS6_ISC_EES8_LS9_1EEEONS1_8FunctionIFbRNS_12WebPageProxyERNS_13WebFrameProxyEEEE
- __ZNK7WebCore10ScrollView16contentsToScreenERKNS_7IntRectE
- __ZNK7WebCore18RenderLayerBacking16compositedBoundsEv
- __ZNSt3__124__optional_destruct_baseIN7WebCore5Style12BorderRadiusELb0EED2B8sn190102Ev
- __ZTVN3WTF6Detail15CallableWrapperIZNK6WebKit15WebExtensionTab9processesENS2_29WebExtensionEventListenerTypeENS2_28WebExtensionContentWorldTypeEE3$_0bJRNS2_12WebPageProxyERNS2_13WebFrameProxyEEEE
- ___113-[_WKWebExtensionDeclarativeNetRequestRule _webKitRuleWithWebKitActionType:chromeActionType:chromeResourceTypes:]_block_invoke
- ___113-[_WKWebExtensionDeclarativeNetRequestRule _webKitRuleWithWebKitActionType:chromeActionType:chromeResourceTypes:]_block_invoke_2
- ___113-[_WKWebExtensionDeclarativeNetRequestRule _webKitRuleWithWebKitActionType:chromeActionType:chromeResourceTypes:]_block_invoke_3
- ___113-[_WKWebExtensionDeclarativeNetRequestRule _webKitRuleWithWebKitActionType:chromeActionType:chromeResourceTypes:]_block_invoke_4
- ____ZN6WebKitL22launchWithExtensionKitERNS_15ProcessLauncherENS_17ProcessLaunchTypeEPNS0_6ClientEON3WTF8FunctionIFvNS5_17ThreadSafeWeakPtrIS0_NS5_15NoTaggingTraitsIS0_EEEEONS_16ExtensionProcessENS5_12ASCIILiteralEP7NSErrorEEE_block_invoke_4
- ____ZN6WebKitL22launchWithExtensionKitERNS_15ProcessLauncherENS_17ProcessLaunchTypeEPNS0_6ClientEON3WTF8FunctionIFvNS5_17ThreadSafeWeakPtrIS0_NS5_15NoTaggingTraitsIS0_EEEEONS_16ExtensionProcessENS5_12ASCIILiteralEP7NSErrorEEE_block_invoke_6
- ___block_literal_global.33
- ___block_literal_global.349
- ___block_literal_global.360
- _objc_msgSend$_allChromeResourceTypes
- _objc_msgSend$_chromeResourceTypeToWebKitLoadContext
- _objc_msgSend$_convertedRulesForWebKitActionType:chromeActionType:
- _objc_msgSend$_webKitRuleWithWebKitActionType:chromeActionType:chromeResourceTypes:
CStrings:
+ "%@: Expected reply block but received isReplyBlock false"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/GCGLSpan.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/ImageBufferPixelFormat.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/RealtimeMediaSourceCapabilities.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/SecurityOriginData.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/StorageNamespaceProvider.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/Frameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/Frameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/Frameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/WebKitAdditions/DownloadProgressAdditions.mm"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/WebKitAdditions/DyldCallbackAdditions.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/pal/spi/cocoa/NSAttributedStringSPI.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/CheckedPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/CompactVariantOperations.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/HashTable.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/JSONValues.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Markable.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Ref.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/RefCounted.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/RefPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/WeakRef.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/cocoa/TypeCastsCocoa.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "/AppleInternal/Library/BuildRoots/4~B2vIugBkO7rm7q8djI1MYzY2WHixnffR1BDlEP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/GPUProcess/graphics/RemoteGraphicsContextGL.cpp 497: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10393: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10401: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10493: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10496: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10522: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10525: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10558: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10604: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10722: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10738: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10754: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10770: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10798: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10814: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11870: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12089: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12309: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13082: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13964: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13966: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14036: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14107: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14108: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14122: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14123: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14141: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14149: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14165: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14166: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14167: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14196: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14199: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14244: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14245: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14259: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14260: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 15427: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5953: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5967: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5980: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5986: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6408: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6535: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6558: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6607: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6640: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6641: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6642: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6674: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6752: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6753: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6820: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6821: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6822: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6854: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6855: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6857: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7378: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7420: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7734: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8055: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8103: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8134: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8145: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8146: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8237: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8240: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8264: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8265: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8285: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8286: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8287: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8288: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8315: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8316: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8318: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8319: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8334: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8335: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8367: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8899: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8900: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8907: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9181: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9473: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9478: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9517: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9529: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9530: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9610: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9650: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9877: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebProcessProxy.cpp 2172: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebProcessProxy.cpp 2448: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebProcessProxy.cpp 2824: Invalid message dispatched %{public}s"
+ "@\"NSDictionary\"16@?0@\"NSString\"8"
+ "Rule with id %ld is invalid. The value in the `resourceTypes` array is invalid."
+ "Warning: Exception caught during handling of received message, marking message invalid .\nException: %@"
+ "_allChromeResourceTypesForCondition:"
+ "_combineRequestDomain:withURLFilter:"
+ "_convertRulesWithModifiedCondition:webKitActionType:chromeActionType:"
+ "_findLongestCommonSubstringWithString:andString:"
+ "_isContentExtensionRedirect"
+ "_webKitRuleWithWebKitActionType:chromeActionType:condition:"
+ "child-document"
+ "replaceObjectAtIndex:withObject:"
+ "static Storage WTF::CompactVariantOperations<WebCore::Style::Length<CSS::Range{0.000000e+00, INF, 0}>, WebCore::Style::Percentage<CSS::Range{0.000000e+00, INF, 0}, float>, WebCore::Style::UnevaluatedCalculation<WebCore::CSS::LengthPercentage<CSS::Range{0.000000e+00, INF, 0}>>>::encodedPayload(U &&) [Ts = <WebCore::Style::Length<CSS::Range{0.000000e+00, INF, 0}>, WebCore::Style::Percentage<CSS::Range{0.000000e+00, INF, 0}, float>, WebCore::Style::UnevaluatedCalculation<WebCore::CSS::LengthPercentage<CSS::Range{0.000000e+00, INF, 0}>>>, T = WebCore::Style::UnevaluatedCalculation<WebCore::CSS::LengthPercentage<CSS::Range{0.000000e+00, INF, 0}>>, U = WebCore::Style::UnevaluatedCalculation<WebCore::CSS::LengthPercentage<CSS::Range{0.000000e+00, INF, 0}>>]"
+ "static Storage WTF::CompactVariantOperations<WebCore::Style::Length<Range{-INF, INF, 0}>, WebCore::Style::Percentage<Range{-INF, INF, 0}, float>, WebCore::Style::UnevaluatedCalculation<WebCore::CSS::LengthPercentage<>>>::encodedPayload(U &&) [Ts = <WebCore::Style::Length<Range{-INF, INF, 0}>, WebCore::Style::Percentage<Range{-INF, INF, 0}, float>, WebCore::Style::UnevaluatedCalculation<WebCore::CSS::LengthPercentage<>>>, T = WebCore::Style::UnevaluatedCalculation<WebCore::CSS::LengthPercentage<>>, U = WebCore::Style::UnevaluatedCalculation<WebCore::CSS::LengthPercentage<>> &]"
+ "static Storage WTF::CompactVariantOperations<WebCore::Style::Length<Range{-INF, INF, 0}>, WebCore::Style::Percentage<Range{-INF, INF, 0}, float>, WebCore::Style::UnevaluatedCalculation<WebCore::CSS::LengthPercentage<>>>::encodedPayload(U &&) [Ts = <WebCore::Style::Length<Range{-INF, INF, 0}>, WebCore::Style::Percentage<Range{-INF, INF, 0}, float>, WebCore::Style::UnevaluatedCalculation<WebCore::CSS::LengthPercentage<>>>, T = WebCore::Style::UnevaluatedCalculation<WebCore::CSS::LengthPercentage<>>, U = WebCore::Style::UnevaluatedCalculation<WebCore::CSS::LengthPercentage<>>]"
+ "stringByReplacingCharactersInRange:withString:"
+ "top-document"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/GCGLSpan.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/ImageBufferPixelFormat.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/RealtimeMediaSourceCapabilities.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/SecurityOriginData.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/StorageNamespaceProvider.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/Frameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/Frameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/Frameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/WebKitAdditions/DownloadProgressAdditions.mm"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/WebKitAdditions/DyldCallbackAdditions.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/pal/spi/cocoa/NSAttributedStringSPI.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/CheckedPtr.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/HashTable.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/JSONValues.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/Markable.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/Ref.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/RefCounted.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/RefPtr.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/WeakRef.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/cocoa/TypeCastsCocoa.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/GPUProcess/graphics/RemoteGraphicsContextGL.cpp 462: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10384: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10392: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10484: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10487: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10513: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10516: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10549: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10595: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10713: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10729: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10745: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10761: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10789: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10805: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11861: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12080: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12300: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13073: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13937: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13939: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14018: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14098: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14099: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14113: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14114: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14131: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14132: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14156: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14157: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14158: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14187: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14190: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14235: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14236: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14250: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14251: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 15418: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5944: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5958: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5971: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5977: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6399: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6526: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6549: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6598: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6631: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6632: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6633: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6665: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6743: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6744: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6811: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6812: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6813: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6845: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6846: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6848: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7369: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7411: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7725: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8046: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8094: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8125: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8136: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8137: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8228: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8231: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8255: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8256: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8276: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8277: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8278: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8279: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8306: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8307: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8309: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8310: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8325: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8326: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8358: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8889: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8890: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8891: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9172: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9464: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9469: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9508: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9520: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9521: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9601: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9641: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9868: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebProcessProxy.cpp 2173: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebProcessProxy.cpp 2449: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebProcessProxy.cpp 2825: Invalid message dispatched %{public}s"
- "T &WTF::CheckedRef<WebCore::LocalFrameView>::get() const [T = WebCore::LocalFrameView, PtrTraits = WTF::RawPtrTraits<WebCore::LocalFrameView>]"
- "_allChromeResourceTypes"
- "_chromeResourceTypeToWebKitLoadContext"
- "_convertedRulesForWebKitActionType:chromeActionType:"
- "_webKitRuleWithWebKitActionType:chromeActionType:chromeResourceTypes:"
- "if-top-url"

```
