## LocalAuthenticationUI

> `/System/Library/PrivateFrameworks/LocalAuthenticationUI.framework/Versions/A/LocalAuthenticationUI`

```diff

-1656.80.6.0.0
-  __TEXT.__text: 0x2560c
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x1f78
+1656.100.223.0.0
+  __TEXT.__text: 0x25e58
+  __TEXT.__auth_stubs: 0x6a0
+  __TEXT.__objc_methlist: 0x2c70
   __TEXT.__const: 0x9a8
-  __TEXT.__gcc_except_tab: 0xb70
+  __TEXT.__gcc_except_tab: 0xbfc
   __TEXT.__cstring: 0x17fa
-  __TEXT.__oslogstring: 0x130c
+  __TEXT.__oslogstring: 0x133a
   __TEXT.__dlopen_cstrs: 0x73
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0xb68
-  __TEXT.__objc_classname: 0x5c2
-  __TEXT.__objc_methname: 0x6720
-  __TEXT.__objc_methtype: 0x160e
-  __TEXT.__objc_stubs: 0x5d40
-  __DATA_CONST.__got: 0x408
+  __TEXT.__unwind_info: 0xbe0
+  __TEXT.__objc_classname: 0x5c3
+  __TEXT.__objc_methname: 0x6876
+  __TEXT.__objc_methtype: 0x161a
+  __TEXT.__objc_stubs: 0x5ec0
+  __DATA_CONST.__got: 0x448
   __DATA_CONST.__const: 0xd8
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c50
+  __DATA_CONST.__objc_selrefs: 0x1da8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x360
+  __AUTH_CONST.__auth_got: 0x368
   __AUTH_CONST.__const: 0xce0
   __AUTH_CONST.__cfstring: 0xee0
-  __AUTH_CONST.__objc_const: 0x7d68
-  __AUTH_CONST.__objc_intobj: 0x408
+  __AUTH_CONST.__objc_const: 0x6528
+  __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x360
+  __DATA.__objc_ivar: 0x370
   __DATA.__data: 0x840
   __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0x2d0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 63B9F29F-8C1E-3451-9756-957C9550B156
-  Functions: 935
-  Symbols:   2707
-  CStrings:  1974
+  UUID: 53B48119-4818-3D37-95C1-8B41E4B721AB
+  Functions: 952
+  Symbols:   2755
+  CStrings:  1990
 
Symbols:
+ +[LAUIAuthenticationSheetPasswordFieldBuilder sharedInstance].cold.1
+ +[LAUIPKGlyphWrapper _loadPKUI].cold.1
+ -[LAUIAuthenticationCore notificationNames].cold.1
+ -[LAUIAuthenticationSheetHelperAvailability isTouchIDAvailable:].cold.1
+ -[LAUIAuthenticationViewController _analyticsSessionStarting:]
+ -[LAUILockImageView _imageForLayer:].cold.2
+ GCC_except_table122
+ GCC_except_table123
+ GCC_except_table15
+ GCC_except_table216
+ GCC_except_table24
+ GCC_except_table28
+ GCC_except_table34
+ GCC_except_table36
+ GCC_except_table41
+ GCC_except_table44
+ GCC_except_table47
+ GCC_except_table52
+ GCC_except_table58
+ GCC_except_table77
+ LAUIAuthenticationSheetViewInit.cold.1
+ LA_LOG.cold.1
+ LA_LOG_LAUIAuthenticationCore.cold.1
+ LA_LOG_LAUIAuthenticationDialog.cold.1
+ LA_LOG_LAUIAuthenticationView.cold.1
+ LA_LOG_LAUIAuthenticationViewController.cold.1
+ LA_LOG_LAUIPKGlyphWrapper.cold.1
+ LA_LOG_LAUIPasswordField.cold.1
+ LA_LOG_RemotePasswordField.cold.1
+ OBJC_IVAR_$_LAUIAuthenticationCore._supportsConcurrentEvaluations
+ OBJC_IVAR_$_LAUIAuthenticationSheetController._occlusionTimer
+ OBJC_IVAR_$_LAUIAuthenticationSheetController._supportsConcurrentEvaluations
+ OBJC_IVAR_$_LAUIAuthenticationViewController._supportsConcurrentEvaluations
+ _LACBiomeDialogIDSheetController
+ _LACBiomeDialogIDViewController
+ _LACErrorCodeAuthenticationFailed
+ _LACErrorCodeSystemCancel
+ _LACErrorSubcodeInterruptedByAnotherEvaluation
+ _OBJC_CLASS_$_LACConcurrentEvaluationHelper
+ _OBJC_CLASS_$_LACError
+ _OBJC_CLASS_$_LACInstalledAppsCache
+ _OBJC_CLASS_$_LACTimer
+ __45-[LAUIAuthenticationViewController _setupUI:]_block_invoke.29
+ __49-[LAUIAuthenticationSheetController _configureUI]_block_invoke.22
+ __50-[LAUIAuthenticationSheetController _startTouchID]_block_invoke.183
+ __50-[LAUIAuthenticationSheetController _startTouchID]_block_invoke.186
+ __60-[LAUIAuthenticationSheetController event:eventHints:reply:]_block_invoke.208
+ __60-[LAUIAuthenticationSheetController event:eventHints:reply:]_block_invoke.208.cold.1
+ __60-[LAUIAuthenticationSheetController event:eventHints:reply:]_block_invoke.211
+ __60-[LAUIAuthenticationSheetController event:eventHints:reply:]_block_invoke.212
+ __60-[LAUIAuthenticationSheetController event:eventHints:reply:]_block_invoke.213
+ __60-[LAUIAuthenticationSheetController event:eventHints:reply:]_block_invoke.216
+ __63-[LAUIAuthenticationSheetController _beginSheetWithCompletion:]_block_invoke.50
+ __63-[LAUIAuthenticationSheetController _beginSheetWithCompletion:]_block_invoke.50.cold.1
+ __63-[LAUIAuthenticationSheetController _beginSheetWithCompletion:]_block_invoke.50.cold.2
+ __63-[LAUIAuthenticationSheetController _beginSheetWithCompletion:]_block_invoke.54
+ __72-[LAUIAuthenticationSheetController didSubmitUnverifiedData:completion:]_block_invoke.193
+ __75-[LAUIAuthenticationSheetController _setupUserPasswordFieldWithCompletion:]_block_invoke.74
+ __ZNKSt3__16vectorIN17LAUI_CA_utilities38animation_completion_handler_containerENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIU8__strongP12CAShapeLayerNS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIU8__strongU13block_pointerFvbENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__114__split_bufferIN17LAUI_CA_utilities38animation_completion_handler_containerERNS_9allocatorIS2_EEE17__destruct_at_endB8ne190102EPS2_
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN17LAUI_CA_utilities38animation_completion_handler_containerEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIU8__strongP12CAShapeLayerEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIU8__strongU13block_pointerFvbEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocator_destroyB8ne190102INS_9allocatorIN17LAUI_CA_utilities38animation_completion_handler_containerEEENS_16reverse_iteratorIPS3_EES7_EEvRT_T0_T1_
+ __ZNSt3__119__allocator_destroyB8ne190102INS_9allocatorIN17LAUI_CA_utilities38animation_completion_handler_containerEEEPS3_S5_EEvRT_T0_T1_
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorIN17LAUI_CA_utilities38animation_completion_handler_containerEEEPS4_EEED2B8ne190102Ev
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorIN17LAUI_CA_utilities38animation_completion_handler_containerEEES3_EEvRT_PT0_S8_S8_
+ __ZNSt3__16vectorIN17LAUI_CA_utilities38animation_completion_handler_containerENS_9allocatorIS2_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorIN17LAUI_CA_utilities38animation_completion_handler_containerENS_9allocatorIS2_EEE22__base_destruct_at_endB8ne190102EPS2_
+ __ZNSt3__16vectorIN17LAUI_CA_utilities38animation_completion_handler_containerENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRU8__strongU13block_pointerFvbEEEEPS2_DpOT_
+ __ZNSt3__16vectorIU8__strongP12CAShapeLayerNS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorIU8__strongU13block_pointerFvbENS_9allocatorIS3_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIU8__strongU13block_pointerFvbENS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorIU8__strongU13block_pointerFvbENS_9allocatorIS3_EEE16__init_with_sizeB8ne190102IPS3_S8_EEvT_T0_m
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___61-[LAUIAuthenticationSheetController windowDidBecomeOccluded:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48w_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48w_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_72_e8_32s40s48s56s64w_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64w
+ ___copy_helper_block_e8_32s40s48w
+ ___destroy_helper_block_e8_32s40s48s56s64w
+ __block_literal_global.180
+ __block_literal_global.403
+ __block_literal_global.50
+ __block_literal_global.60
+ __block_literal_global.619
+ _memcpy
+ _objc_msgSend$_analyticsSessionStarting:
+ _objc_msgSend$analyticsAction:dismissing:
+ _objc_msgSend$analyticsMechanism:result:
+ _objc_msgSend$analyticsMechanism:starting:
+ _objc_msgSend$analyticsSessionStarting:dialogID:bundleID:
+ _objc_msgSend$cancel
+ _objc_msgSend$dispatchAfter:inQueue:block:
+ _objc_msgSend$error:hasCode:subcode:
+ _objc_msgSend$errorWithCode:
+ _objc_msgSend$infoForPid:
+ _objc_msgSend$isConcurrentEvaluationEnabledForClientInfo:
+ _objc_msgSend$isRunning
- GCC_except_table120
- GCC_except_table121
- GCC_except_table214
- GCC_except_table25
- GCC_except_table26
- GCC_except_table31
- GCC_except_table37
- GCC_except_table39
- GCC_except_table45
- _OBJC_CLASS_$_InstalledAppsCache
- __45-[LAUIAuthenticationViewController _setupUI:]_block_invoke.27
- __49-[LAUIAuthenticationSheetController _configureUI]_block_invoke.20
- __50-[LAUIAuthenticationSheetController _startTouchID]_block_invoke.174
- __50-[LAUIAuthenticationSheetController _startTouchID]_block_invoke.177
- __60-[LAUIAuthenticationSheetController event:eventHints:reply:]_block_invoke.198
- __60-[LAUIAuthenticationSheetController event:eventHints:reply:]_block_invoke.198.cold.1
- __60-[LAUIAuthenticationSheetController event:eventHints:reply:]_block_invoke.201
- __60-[LAUIAuthenticationSheetController event:eventHints:reply:]_block_invoke.202
- __60-[LAUIAuthenticationSheetController event:eventHints:reply:]_block_invoke.203
- __60-[LAUIAuthenticationSheetController event:eventHints:reply:]_block_invoke.206
- __63-[LAUIAuthenticationSheetController _beginSheetWithCompletion:]_block_invoke.47
- __63-[LAUIAuthenticationSheetController _beginSheetWithCompletion:]_block_invoke.cold.1
- __63-[LAUIAuthenticationSheetController _beginSheetWithCompletion:]_block_invoke.cold.2
- __72-[LAUIAuthenticationSheetController didSubmitUnverifiedData:completion:]_block_invoke.184
- __75-[LAUIAuthenticationSheetController _setupUserPasswordFieldWithCompletion:]_block_invoke.67
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorIN17LAUI_CA_utilities38animation_completion_handler_containerEEENS_16reverse_iteratorIPS3_EEEclB8ne180100Ev
- __ZNKSt3__16vectorIN17LAUI_CA_utilities38animation_completion_handler_containerENS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIU8__strongP12CAShapeLayerNS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIU8__strongU13block_pointerFvbENS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__114__split_bufferIN17LAUI_CA_utilities38animation_completion_handler_containerERNS_9allocatorIS2_EEE17__destruct_at_endB8ne180100EPS2_
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN17LAUI_CA_utilities38animation_completion_handler_containerEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIU8__strongP12CAShapeLayerEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIU8__strongU13block_pointerFvbEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocator_destroyB8ne180100INS_9allocatorIN17LAUI_CA_utilities38animation_completion_handler_containerEEENS_16reverse_iteratorINS5_IPS3_EEEES8_EEvRT_T0_T1_
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorIN17LAUI_CA_utilities38animation_completion_handler_containerEEENS_16reverse_iteratorIPS4_EEEEED2B8ne180100Ev
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ne180100INS_9allocatorIN17LAUI_CA_utilities38animation_completion_handler_containerEEENS_16reverse_iteratorIPS3_EES7_S7_EET2_RT_T0_T1_S8_
- __ZNSt3__16vectorIN17LAUI_CA_utilities38animation_completion_handler_containerENS_9allocatorIS2_EEE12emplace_backIJRU8__strongU13block_pointerFvbEEEERS2_DpOT_
- __ZNSt3__16vectorIN17LAUI_CA_utilities38animation_completion_handler_containerENS_9allocatorIS2_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorIN17LAUI_CA_utilities38animation_completion_handler_containerENS_9allocatorIS2_EEE22__base_destruct_at_endB8ne180100EPS2_
- __ZNSt3__16vectorIN17LAUI_CA_utilities38animation_completion_handler_containerENS_9allocatorIS2_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS2_RS4_EE
- __ZNSt3__16vectorIU8__strongP12CAShapeLayerNS_9allocatorIS3_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorIU8__strongU13block_pointerFvbENS_9allocatorIS3_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIU8__strongU13block_pointerFvbENS_9allocatorIS3_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorIU8__strongU13block_pointerFvbENS_9allocatorIS3_EEE16__init_with_sizeB8ne180100IPS3_S8_EEvT_T0_m
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- ___block_descriptor_48_e8_32s40w_e34_v24?0"NSDictionary"8"NSError"16l
- ___block_descriptor_56_e8_32s40w_e34_v24?0"NSDictionary"8"NSError"16l
- ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56w
- __block_literal_global.178
- __block_literal_global.397
- __block_literal_global.49
- __block_literal_global.59
- __block_literal_global.606
CStrings:
+ "%{public}@ occlusion timer is already running"
+ "@\"LACTimer\""
+ "_analyticsSessionStarting:"
+ "_occlusionTimer"
+ "_supportsConcurrentEvaluations"
+ "analyticsAction:dismissing:"
+ "analyticsMechanism:result:"
+ "analyticsMechanism:starting:"
+ "analyticsSessionStarting:dialogID:bundleID:"
+ "cancel"
+ "dispatchAfter:inQueue:block:"
+ "error:hasCode:subcode:"
+ "errorWithCode:"
+ "infoForPid:"
+ "isConcurrentEvaluationEnabledForClientInfo:"
+ "isRunning"

```
