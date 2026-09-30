## MapKit

> `/System/Library/Frameworks/MapKit.framework/MapKit`

```diff

-2504.32.10.2.3
-  __TEXT.__text: 0x22ca78
+2504.32.10.2.4
+  __TEXT.__text: 0x22d230
   __TEXT.__auth_stubs: 0x1e10
-  __TEXT.__objc_methlist: 0x26544
+  __TEXT.__objc_methlist: 0x265bc
   __TEXT.__const: 0x1be8
   __TEXT.__dlopen_cstrs: 0xbc
   __TEXT.__gcc_except_tab: 0x666c

   __TEXT.__cstring: 0x1701d
   __TEXT.__ustring: 0x19c
   __TEXT.__unwind_info: 0x8be0
-  __TEXT.__objc_classname: 0x530d
-  __TEXT.__objc_methname: 0x635e7
-  __TEXT.__objc_methtype: 0x1803c
-  __TEXT.__objc_stubs: 0x3faa0
+  __TEXT.__objc_classname: 0x530f
+  __TEXT.__objc_methname: 0x63af4
+  __TEXT.__objc_methtype: 0x1811b
+  __TEXT.__objc_stubs: 0x3fbe0
   __DATA_CONST.__got: 0x1c58
-  __DATA_CONST.__const: 0x79e8
+  __DATA_CONST.__const: 0x7a10
   __DATA_CONST.__objc_classlist: 0x10b0
   __DATA_CONST.__objc_catlist: 0x1f0
   __DATA_CONST.__objc_protolist: 0x650
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14808
+  __DATA_CONST.__objc_selrefs: 0x14858
   __DATA_CONST.__objc_protorefs: 0xe8
   __DATA_CONST.__objc_superrefs: 0xd98
   __DATA_CONST.__objc_arraydata: 0x6b0
   __AUTH_CONST.__auth_got: 0xf20
   __AUTH_CONST.__const: 0x2a20
   __AUTH_CONST.__cfstring: 0x1b6a0
-  __AUTH_CONST.__objc_const: 0x43340
+  __AUTH_CONST.__objc_const: 0x43660
   __AUTH_CONST.__objc_doubleobj: 0x220
   __AUTH_CONST.__objc_intobj: 0xf00
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_arrayobj: 0x480
   __AUTH_CONST.__objc_floatobj: 0x70
   __AUTH.__objc_data: 0x8b60
-  __DATA.__objc_ivar: 0x3148
+  __DATA.__objc_ivar: 0x3198
   __DATA.__data: 0x4c88
   __DATA.__bss: 0xd10
   __DATA.__common: 0x10

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 368F17A9-CBED-3632-A740-AA40D846D9A2
-  Functions: 12880
-  Symbols:   45496
-  CStrings:  25614
+  UUID: 3DBA56E4-3D54-31F7-BF5E-7E11788540C4
+  Functions: 12890
+  Symbols:   45547
+  CStrings:  25646
 
Symbols:
+ -[MKAutocompleteAnalyticsProvider updateStateWithQuery:queryTokens:visibleSuggestionEntries:responseStatus:modelVersion:rolloutId:rolloutDeploymentId:rolloutFactorpackId:rolloutRampId:experimentId:deploymentId:treatmentId:experimentDescription:]
+ -[MKAutocompleteAnalyticsState deploymentId]
+ -[MKAutocompleteAnalyticsState experimentDescription]
+ -[MKAutocompleteAnalyticsState experimentId]
+ -[MKAutocompleteAnalyticsState initWithQuery:queryTokens:suggestionEntries:responseStatus:modelVersion:rolloutId:rolloutDeploymentId:rolloutFactorpackId:rolloutRampId:experimentId:deploymentId:treatmentId:experimentDescription:]
+ -[MKAutocompleteAnalyticsState modelVersion]
+ -[MKAutocompleteAnalyticsState responseStatus]
+ -[MKAutocompleteAnalyticsState rolloutDeploymentId]
+ -[MKAutocompleteAnalyticsState rolloutFactorpackId]
+ -[MKAutocompleteAnalyticsState rolloutId]
+ -[MKAutocompleteAnalyticsState rolloutRampId]
+ -[MKAutocompleteAnalyticsState treatmentId]
+ -[MKLocalSearchKeypressMetrics initWithQuery:queryTokens:suggestionEntries:responseStatus:modelVersion:rolloutId:rolloutDeploymentId:rolloutFactorpackId:rolloutRampId:experimentId:deploymentId:treatmentId:experimentDescription:]
+ GCC_except_table11864
+ GCC_except_table11891
+ GCC_except_table11919
+ GCC_except_table11932
+ GCC_except_table11937
+ GCC_except_table11943
+ GCC_except_table11944
+ GCC_except_table11945
+ GCC_except_table11946
+ GCC_except_table11949
+ GCC_except_table11950
+ GCC_except_table11951
+ GCC_except_table11978
+ GCC_except_table12007
+ GCC_except_table12012
+ GCC_except_table12018
+ GCC_except_table12021
+ GCC_except_table12023
+ GCC_except_table12024
+ GCC_except_table12025
+ GCC_except_table12057
+ GCC_except_table12324
+ GCC_except_table12325
+ GCC_except_table12326
+ GCC_except_table12327
+ GCC_except_table12461
+ GCC_except_table12462
+ GCC_except_table12571
+ GCC_except_table12591
+ GCC_except_table12593
+ GCC_except_table12615
+ GCC_except_table12620
+ GCC_except_table12626
+ GCC_except_table12627
+ GCC_except_table12628
+ GCC_except_table12629
+ GCC_except_table12658
+ GCC_except_table12663
+ GCC_except_table12674
+ GCC_except_table12677
+ GCC_except_table12682
+ _OBJC_IVAR_$_MKAutocompleteAnalyticsState._deploymentId
+ _OBJC_IVAR_$_MKAutocompleteAnalyticsState._experimentDescription
+ _OBJC_IVAR_$_MKAutocompleteAnalyticsState._experimentId
+ _OBJC_IVAR_$_MKAutocompleteAnalyticsState._modelVersion
+ _OBJC_IVAR_$_MKAutocompleteAnalyticsState._responseStatus
+ _OBJC_IVAR_$_MKAutocompleteAnalyticsState._rolloutDeploymentId
+ _OBJC_IVAR_$_MKAutocompleteAnalyticsState._rolloutFactorpackId
+ _OBJC_IVAR_$_MKAutocompleteAnalyticsState._rolloutId
+ _OBJC_IVAR_$_MKAutocompleteAnalyticsState._rolloutRampId
+ _OBJC_IVAR_$_MKAutocompleteAnalyticsState._treatmentId
+ _OBJC_IVAR_$_MKLocalSearchKeypressMetrics._deploymentId
+ _OBJC_IVAR_$_MKLocalSearchKeypressMetrics._experimentDescription
+ _OBJC_IVAR_$_MKLocalSearchKeypressMetrics._experimentId
+ _OBJC_IVAR_$_MKLocalSearchKeypressMetrics._modelVersion
+ _OBJC_IVAR_$_MKLocalSearchKeypressMetrics._responseStatus
+ _OBJC_IVAR_$_MKLocalSearchKeypressMetrics._rolloutDeploymentId
+ _OBJC_IVAR_$_MKLocalSearchKeypressMetrics._rolloutFactorpackId
+ _OBJC_IVAR_$_MKLocalSearchKeypressMetrics._rolloutId
+ _OBJC_IVAR_$_MKLocalSearchKeypressMetrics._rolloutRampId
+ _OBJC_IVAR_$_MKLocalSearchKeypressMetrics._treatmentId
+ __MKMapViewShouldUseUnsafeDelegate.onceToken.44668
+ __MKMapViewShouldUseUnsafeDelegate.useUnsafeDelegate.44670
+ __ZL12fillTemplateP15NSMutableStringP8NSStringl.44465
+ ___245-[MKAutocompleteAnalyticsProvider updateStateWithQuery:queryTokens:visibleSuggestionEntries:responseStatus:modelVersion:rolloutId:rolloutDeploymentId:rolloutFactorpackId:rolloutRampId:experimentId:deploymentId:treatmentId:experimentDescription:]_block_invoke
+ ___Block_byref_object_copy_.46325
+ ___Block_byref_object_dispose_.46326
+ ____MKMapViewShouldUseUnsafeDelegate_block_invoke.44673
+ ___block_descriptor_140_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8
+ ___block_literal_global.16.46332
+ ___block_literal_global.20.44669
+ ___block_literal_global.43233
+ ___block_literal_global.43464
+ ___block_literal_global.43733
+ ___block_literal_global.44171
+ ___block_literal_global.44664
+ ___block_literal_global.45270
+ ___block_literal_global.45502
+ ___block_literal_global.45950
+ ___block_literal_global.46344
+ ___block_literal_global.46709
+ _objc_msgSend$captureClientACKeypressWithQuery:queryTokens:entries:keypressStatus:responseStatus:GEOModelMetadata_modelVersion:GEOModelMetadata_rolloutId:GEOModelMetadata_rolloutDeploymentId:GEOModelMetadata_rolloutFactorpackId:GEOModelMetadata_rolloutRampId:GEOExperimentMetadata_experimentId:GEOExperimentMetadata_deploymentId:GEOExperimentMetadata_treatmentId:GEOExperimentMetadata_experimentDescription:
+ _objc_msgSend$deploymentId
+ _objc_msgSend$experimentDescription
+ _objc_msgSend$experimentId
+ _objc_msgSend$initWithQuery:queryTokens:suggestionEntries:responseStatus:modelVersion:rolloutId:rolloutDeploymentId:rolloutFactorpackId:rolloutRampId:experimentId:deploymentId:treatmentId:experimentDescription:
+ _objc_msgSend$modelVersion
+ _objc_msgSend$responseStatus
+ _objc_msgSend$rolloutDeploymentId
+ _objc_msgSend$rolloutFactorpackId
+ _objc_msgSend$rolloutId
+ _objc_msgSend$rolloutRampId
+ _objc_msgSend$treatmentId
- -[MKAutocompleteAnalyticsProvider updateStateWithQuery:queryTokens:visibleSuggestionEntries:]
- -[MKAutocompleteAnalyticsState initWithQuery:queryTokens:suggestionEntries:]
- -[MKLocalSearchKeypressMetrics initWithQuery:queryTokens:suggestionEntries:]
- GCC_except_table11854
- GCC_except_table11881
- GCC_except_table11909
- GCC_except_table11910
- GCC_except_table11922
- GCC_except_table11925
- GCC_except_table11926
- GCC_except_table11927
- GCC_except_table11931
- GCC_except_table11933
- GCC_except_table11934
- GCC_except_table11939
- GCC_except_table11968
- GCC_except_table11997
- GCC_except_table12002
- GCC_except_table12003
- GCC_except_table12008
- GCC_except_table12011
- GCC_except_table12014
- GCC_except_table12015
- GCC_except_table12047
- GCC_except_table12314
- GCC_except_table12315
- GCC_except_table12316
- GCC_except_table12317
- GCC_except_table12451
- GCC_except_table12452
- GCC_except_table12561
- GCC_except_table12581
- GCC_except_table12583
- GCC_except_table12605
- GCC_except_table12609
- GCC_except_table12610
- GCC_except_table12616
- GCC_except_table12617
- GCC_except_table12618
- GCC_except_table12648
- GCC_except_table12653
- GCC_except_table12664
- GCC_except_table12667
- GCC_except_table12672
- __MKMapViewShouldUseUnsafeDelegate.onceToken.44613
- __MKMapViewShouldUseUnsafeDelegate.useUnsafeDelegate.44615
- __ZL12fillTemplateP15NSMutableStringP8NSStringl.44422
- ___93-[MKAutocompleteAnalyticsProvider updateStateWithQuery:queryTokens:visibleSuggestionEntries:]_block_invoke
- ___Block_byref_object_copy_.46270
- ___Block_byref_object_dispose_.46271
- ____MKMapViewShouldUseUnsafeDelegate_block_invoke.44618
- ___block_literal_global.16.46277
- ___block_literal_global.20.44614
- ___block_literal_global.43190
- ___block_literal_global.43421
- ___block_literal_global.43690
- ___block_literal_global.44128
- ___block_literal_global.44609
- ___block_literal_global.45215
- ___block_literal_global.45447
- ___block_literal_global.45895
- ___block_literal_global.46289
- ___block_literal_global.46654
- _objc_msgSend$captureClientACKeypressWithQuery:queryTokens:entries:keypressStatus:
- _objc_msgSend$initWithQuery:queryTokens:suggestionEntries:
CStrings:
+ "@116@0:8@16@24@32i40@44@52@60@68@76@84@92@100@108"
+ "T@\"NSNumber\",R,C,N,V_deploymentId"
+ "T@\"NSString\",R,C,N,V_experimentDescription"
+ "T@\"NSString\",R,C,N,V_experimentId"
+ "T@\"NSString\",R,C,N,V_modelVersion"
+ "T@\"NSString\",R,C,N,V_rolloutDeploymentId"
+ "T@\"NSString\",R,C,N,V_rolloutFactorpackId"
+ "T@\"NSString\",R,C,N,V_rolloutId"
+ "T@\"NSString\",R,C,N,V_rolloutRampId"
+ "T@\"NSString\",R,C,N,V_treatmentId"
+ "Ti,R,N,V_responseStatus"
+ "_deploymentId"
+ "_experimentDescription"
+ "_experimentId"
+ "_modelVersion"
+ "_responseStatus"
+ "_rolloutDeploymentId"
+ "_rolloutFactorpackId"
+ "_rolloutId"
+ "_rolloutRampId"
+ "_treatmentId"
+ "captureClientACKeypressWithQuery:queryTokens:entries:keypressStatus:responseStatus:GEOModelMetadata_modelVersion:GEOModelMetadata_rolloutId:GEOModelMetadata_rolloutDeploymentId:GEOModelMetadata_rolloutFactorpackId:GEOModelMetadata_rolloutRampId:GEOExperimentMetadata_experimentId:GEOExperimentMetadata_deploymentId:GEOExperimentMetadata_treatmentId:GEOExperimentMetadata_experimentDescription:"
+ "deploymentId"
+ "experimentDescription"
+ "experimentId"
+ "initWithQuery:queryTokens:suggestionEntries:responseStatus:modelVersion:rolloutId:rolloutDeploymentId:rolloutFactorpackId:rolloutRampId:experimentId:deploymentId:treatmentId:experimentDescription:"
+ "modelVersion"
+ "responseStatus"
+ "rolloutDeploymentId"
+ "rolloutFactorpackId"
+ "rolloutId"
+ "rolloutRampId"
+ "treatmentId"
+ "updateStateWithQuery:queryTokens:visibleSuggestionEntries:responseStatus:modelVersion:rolloutId:rolloutDeploymentId:rolloutFactorpackId:rolloutRampId:experimentId:deploymentId:treatmentId:experimentDescription:"
+ "v116@0:8@\"NSString\"16@\"NSArray\"24@\"NSArray\"32i40@\"NSString\"44@\"NSString\"52@\"NSString\"60@\"NSString\"68@\"NSString\"76@\"NSString\"84@\"NSNumber\"92@\"NSString\"100@\"NSString\"108"
+ "v116@0:8@16@24@32i40@44@52@60@68@76@84@92@100@108"
- "captureClientACKeypressWithQuery:queryTokens:entries:keypressStatus:"
- "initWithQuery:queryTokens:suggestionEntries:"
- "updateStateWithQuery:queryTokens:visibleSuggestionEntries:"
- "v40@0:8@\"NSString\"16@\"NSArray\"24@\"NSArray\"32"

```
