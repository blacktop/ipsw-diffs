## VoiceShortcutClient

> `/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient`

```diff

-2302.0.5.0.0
-  __TEXT.__text: 0xb7398
+2510.5.1.0.0
+  __TEXT.__text: 0xba080
   __TEXT.__auth_stubs: 0x26b0
-  __TEXT.__objc_methlist: 0x9434
-  __TEXT.__const: 0x2310
-  __TEXT.__cstring: 0x11db9
+  __TEXT.__objc_methlist: 0x9674
+  __TEXT.__const: 0x2340
+  __TEXT.__cstring: 0x12238
   __TEXT.__constg_swiftt: 0xbe0
   __TEXT.__swift5_typeref: 0xa22
   __TEXT.__swift5_reflstr: 0x448

   __TEXT.__swift5_mpenum: 0x1c
   __TEXT.__swift5_capture: 0x248
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__gcc_except_tab: 0x128c
-  __TEXT.__oslogstring: 0x2c62
+  __TEXT.__gcc_except_tab: 0x12f4
+  __TEXT.__oslogstring: 0x2d90
   __TEXT.__ustring: 0x172
-  __TEXT.__dlopen_cstrs: 0xc6b
-  __TEXT.__unwind_info: 0x4514
-  __TEXT.__eh_frame: 0x1e68
-  __TEXT.__objc_classname: 0x1bbc
-  __TEXT.__objc_methname: 0x1687f
-  __TEXT.__objc_methtype: 0x3d25
-  __TEXT.__objc_stubs: 0xe420
-  __DATA_CONST.__got: 0x528
-  __DATA_CONST.__const: 0x2d50
-  __DATA_CONST.__objc_classlist: 0x728
-  __DATA_CONST.__objc_catlist: 0xb0
+  __TEXT.__dlopen_cstrs: 0xd0e
+  __TEXT.__unwind_info: 0x45cc
+  __TEXT.__eh_frame: 0x1e58
+  __TEXT.__objc_classname: 0x1d3d
+  __TEXT.__objc_methname: 0x16ddd
+  __TEXT.__objc_methtype: 0x3db8
+  __TEXT.__objc_stubs: 0xe760
+  __DATA_CONST.__got: 0x538
+  __DATA_CONST.__const: 0x2e90
+  __DATA_CONST.__objc_classlist: 0x790
+  __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xea60
-  __DATA_CONST.__objc_selrefs: 0x4860
-  __DATA_CONST.__objc_arraydata: 0xff0
-  __AUTH_CONST.__const: 0x3a58
+  __DATA_CONST.__objc_const: 0xf0c8
+  __DATA_CONST.__objc_selrefs: 0x4948
+  __DATA_CONST.__objc_protorefs: 0x60
+  __DATA_CONST.__objc_classrefs: 0x868
+  __DATA_CONST.__objc_superrefs: 0x648
+  __DATA_CONST.__objc_arraydata: 0xfc0
+  __AUTH_CONST.__const: 0x3af8
   __AUTH_CONST.__auth_ptr: 0x48
-  __AUTH_CONST.__cfstring: 0x11d40
-  __AUTH_CONST.__objc_const: 0x69c8
-  __AUTH_CONST.__objc_intobj: 0x2c40
-  __AUTH_CONST.__objc_arrayobj: 0x1c8
+  __AUTH_CONST.__cfstring: 0x12060
+  __AUTH_CONST.__objc_const: 0x6cd8
+  __AUTH_CONST.__objc_intobj: 0x2c28
+  __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__auth_got: 0x1368
-  __AUTH.__objc_data: 0x2bc0
+  __AUTH.__objc_data: 0x2e40
   __AUTH.__data: 0x6e8
-  __DATA.__objc_protorefs: 0x60
-  __DATA.__objc_classrefs: 0x840
-  __DATA.__objc_superrefs: 0x620
-  __DATA.__objc_ivar: 0xa5c
-  __DATA.__data: 0x1650
-  __DATA.__bss: 0x2f90
-  __DATA_DIRTY.__objc_data: 0x19a0
-  __DATA_DIRTY.__data: 0x138
-  __DATA_DIRTY.__bss: 0x938
+  __DATA.__objc_ivar: 0xa68
+  __DATA.__data: 0x1e00
+  __DATA.__bss: 0x2800
+  __DATA_DIRTY.__objc_data: 0x1b30
+  __DATA_DIRTY.__data: 0x140
+  __DATA_DIRTY.__bss: 0x988
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5095
-  Symbols:   13885
-  CStrings:  7349
+  Functions: 5145
+  Symbols:   14154
+  CStrings:  7441
 
Symbols:
+ +[WFAutoShortcutContextualAction legacySpotlightDomainIdentifier]
+ +[WFCellularSettings defaultSettings]
+ +[WFColor(IconicSymbolUtilities) tintColorForBundleIdentifier:]
+ +[WFConfiguredSystemContextualAction supportsSecureCoding]
+ +[WFConfiguredSystemIntentAction supportsSecureCoding]
+ +[WFConfiguredSystemWorkflowAction supportsSecureCoding]
+ +[WFContextualAction(WFSpotlightResultRunnable) spotlightDomainIdentifierForBundleIdentifier:]
+ +[WFContextualActionIcon iconWithINImage:displayStyle:completion:]
+ +[WFExecutableAppShortcut supportsSecureCoding]
+ +[WFExecutableAppShortcut useNewDataSource]
+ +[WFStaccatoWorkflowRunnerClient defaultContextualActionContext]
+ +[WFSymbolIcon(IconicSymbolUtilities) symbolIconForActionIdentifier:bundleIdentifier:]
+ +[WFSystemActionRunnerClient defaultContextualActionContext]
+ +[WFToggleAccessibilityContextualAction spotlightDomainIdentifierForBundleIdentifier:]
+ +[WFToggleAlarmContextualAction spotlightDomainIdentifierForBundleIdentifier:]
+ +[WFToggleFocusModeContextualAction spotlightDomainIdentifierForBundleIdentifier:]
+ +[WFToggleSettingContextualAction spotlightDomainIdentifierForBundleIdentifier:]
+ -[INImage(Loading) retrieveImageDataWithCompletion:]
+ -[VCVoiceShortcutClient(Sync) coherenceEnabledWithCompletion:]
+ -[VCVoiceShortcutClient(Sync) coherenceMigrationEnabledWithCompletion:]
+ -[VCVoiceShortcutClient(Sync) setCoherenceMigrationStatus:completion:]
+ -[VCVoiceShortcutClient(Sync) toprakEngineEnabledWithCompletion:]
+ -[WFAppIcon(IconicSymbolUtilities) associatedLogo]
+ -[WFAutoShortcutContextualAction executableAppShortcut]
+ -[WFAutoShortcutContextualAction initWithAutoShortcut:identifier:parameterlessIdentifier:phrase:alternativePhrases:bundleIdentifier:actionIdentifier:orderOfShortcut:parentAction:prominentDisplayEligibility:executableAppShortcut:]
+ -[WFAutoShortcutContextualAction initWithExecutableAppShortcut:index:]
+ -[WFAutoShortcutContextualAction isTopHitEligible]
+ -[WFAutoShortcutContextualAction parameterlessIdentifier]
+ -[WFAutoShortcutContextualAction spotlightActionIdentifier]
+ -[WFCellularSettings cellularDataEnabledWithError:]
+ -[WFCellularSettings connection]
+ -[WFCellularSettings dealloc]
+ -[WFCellularSettings init]
+ -[WFCellularSettings isCellularDataCapableWithError:]
+ -[WFConfiguratorRunRequest initWithInputStrings:presentationMode:]
+ -[WFConfiguratorRunnerClient initWithWorkflowName:inputStrings:]
+ -[WFConfiguredStaccatoAction initWithIdentifier:associatedBundleIdentifier:name:previewIcon:shortcutsMetadata:]
+ -[WFConfiguredStaccatoAction setShortcutsMetadata:]
+ -[WFConfiguredStaccatoAction usesPreviewIconSymbolOverride]
+ -[WFConfiguredStaccatoAction(Staccato) initWithIdentifier:sectionIdentifier:associatedBundleIdentifier:name:systemImageName:shortcutsMetadata:]
+ -[WFConfiguredStaccatoAction(Staccato) isSystemStaccatoAction]
+ -[WFConfiguredStaccatoAction(Staccato) sectionIdentifier]
+ -[WFConfiguredStaccatoAction(Staccato) systemImageName]
+ -[WFConfiguredStaccatoAction(Staccato) tintColor]
+ -[WFConfiguredStaccatoIntentAction initWithIntent:named:previewIcon:appShortcutIdentifier:templateParameterValues:contextualParameters:shortcutsMetadata:]
+ -[WFConfiguredSystemContextualAction .cxx_destruct]
+ -[WFConfiguredSystemContextualAction appShortcutIdentifier]
+ -[WFConfiguredSystemContextualAction contextualAction]
+ -[WFConfiguredSystemContextualAction description]
+ -[WFConfiguredSystemContextualAction encodeWithCoder:]
+ -[WFConfiguredSystemContextualAction hash]
+ -[WFConfiguredSystemContextualAction initWithCoder:]
+ -[WFConfiguredSystemContextualAction initWithContextualAction:appShortcutIdentifier:shortcutsMetadata:]
+ -[WFConfiguredSystemContextualAction isEqual:]
+ -[WFConfiguredSystemIntentAction .cxx_destruct]
+ -[WFConfiguredSystemIntentAction appShortcutIdentifier]
+ -[WFConfiguredSystemIntentAction contextualParameters]
+ -[WFConfiguredSystemIntentAction description]
+ -[WFConfiguredSystemIntentAction encodeWithCoder:]
+ -[WFConfiguredSystemIntentAction hash]
+ -[WFConfiguredSystemIntentAction initWithCoder:]
+ -[WFConfiguredSystemIntentAction initWithIntent:named:previewIcon:appShortcutIdentifier:contextualParameters:shortcutsMetadata:]
+ -[WFConfiguredSystemIntentAction intent]
+ -[WFConfiguredSystemIntentAction isEqual:]
+ -[WFConfiguredSystemIntentAction setAppShortcutIdentifier:]
+ -[WFConfiguredSystemIntentAction setContextualParameters:]
+ -[WFConfiguredSystemIntentAction setIntent:]
+ -[WFConfiguredSystemNothingAction init]
+ -[WFConfiguredSystemWorkflowAction .cxx_destruct]
+ -[WFConfiguredSystemWorkflowAction description]
+ -[WFConfiguredSystemWorkflowAction encodeWithCoder:]
+ -[WFConfiguredSystemWorkflowAction hash]
+ -[WFConfiguredSystemWorkflowAction initWithCoder:]
+ -[WFConfiguredSystemWorkflowAction initWithName:workflowIdentifier:workflowIcon:associatedBundleIdentifier:shortcutsMetadata:]
+ -[WFConfiguredSystemWorkflowAction initWithWorkflow:shortcutsMetadata:]
+ -[WFConfiguredSystemWorkflowAction isEqual:]
+ -[WFConfiguredSystemWorkflowAction previewIcon]
+ -[WFConfiguredSystemWorkflowAction setWorkflowIcon:]
+ -[WFConfiguredSystemWorkflowAction setWorkflowIdentifier:]
+ -[WFConfiguredSystemWorkflowAction workflowIcon]
+ -[WFConfiguredSystemWorkflowAction workflowIdentifier]
+ -[WFContextualAction(Spotlight) spotlightActionIdentifier]
+ -[WFContextualActionIcon initWithLNPropertyIdentifier:displayStyle:]
+ -[WFContextualActionIcon lnPropertyIdentifier]
+ -[WFContextualActionIcon loadLNPropertyImageWithCompletion:]
+ -[WFExecutableAppShortcut .cxx_destruct]
+ -[WFExecutableAppShortcut alternatePhrases]
+ -[WFExecutableAppShortcut attributionBundleIdentifier]
+ -[WFExecutableAppShortcut base64ArchivedData]
+ -[WFExecutableAppShortcut bundleIdentifier]
+ -[WFExecutableAppShortcut chicletColor]
+ -[WFExecutableAppShortcut encodeWithCoder:]
+ -[WFExecutableAppShortcut entityInfo]
+ -[WFExecutableAppShortcut fullyQualifiedIdentifier]
+ -[WFExecutableAppShortcut id]
+ -[WFExecutableAppShortcut initWithAutoShortcut:phrase:alternatePhrases:entityInfo:]
+ -[WFExecutableAppShortcut initWithAutoShortcut:phrase:entityInfo:]
+ -[WFExecutableAppShortcut initWithCoder:]
+ -[WFExecutableAppShortcut isDeprecatedStyle]
+ -[WFExecutableAppShortcut namedQueryInfo]
+ -[WFExecutableAppShortcut phrase]
+ -[WFExecutableAppShortcut shortcutDescription]
+ -[WFExecutableAppShortcut triggerPhrase]
+ -[WFExecutableAppShortcut underlyingAutoShortcut]
+ -[WFSystemActionRunnerClient .cxx_destruct]
+ -[WFSystemActionRunnerClient actionContext]
+ -[WFSystemActionRunnerClient action]
+ -[WFSystemActionRunnerClient initWithSystemAction:]
+ -[WFSystemActionRunnerClient initWithSystemContextualAction:]
+ -[WFSystemActionRunnerClient initWithSystemIntentAction:]
+ -[WFSystemActionRunnerClient initWithSystemNothingAction:]
+ -[WFSystemActionRunnerClient initWithSystemWorkflowAction:]
+ -[WFSystemActionRunnerClient setAction:]
+ -[WFSystemActionRunnerClient setActionContext:]
+ -[WFSystemActionRunnerClient start]
+ -[WFToggleFocusModeContextualAction spotlightItem]
+ -[WFWorkflowDescriptor backgroundColor]
+ GCC_except_table1060
+ GCC_except_table1066
+ GCC_except_table1079
+ GCC_except_table1106
+ GCC_except_table1111
+ GCC_except_table1117
+ GCC_except_table1161
+ GCC_except_table1163
+ GCC_except_table1164
+ GCC_except_table1171
+ GCC_except_table1180
+ GCC_except_table1242
+ GCC_except_table1322
+ GCC_except_table1335
+ GCC_except_table1350
+ GCC_except_table1354
+ GCC_except_table1387
+ GCC_except_table1406
+ GCC_except_table1408
+ GCC_except_table1410
+ GCC_except_table1468
+ GCC_except_table1473
+ GCC_except_table1475
+ GCC_except_table1484
+ GCC_except_table1492
+ GCC_except_table1494
+ GCC_except_table1515
+ GCC_except_table1547
+ GCC_except_table1565
+ GCC_except_table1602
+ GCC_except_table1631
+ GCC_except_table1675
+ GCC_except_table1686
+ GCC_except_table1694
+ GCC_except_table170
+ GCC_except_table1710
+ GCC_except_table1715
+ GCC_except_table1718
+ GCC_except_table1778
+ GCC_except_table1835
+ GCC_except_table1843
+ GCC_except_table1850
+ GCC_except_table2102
+ GCC_except_table2152
+ GCC_except_table2156
+ GCC_except_table2161
+ GCC_except_table2192
+ GCC_except_table2267
+ GCC_except_table2270
+ GCC_except_table2294
+ GCC_except_table2300
+ GCC_except_table2305
+ GCC_except_table2324
+ GCC_except_table2333
+ GCC_except_table2472
+ GCC_except_table2555
+ GCC_except_table2558
+ GCC_except_table2631
+ GCC_except_table2637
+ GCC_except_table2638
+ GCC_except_table2644
+ GCC_except_table2646
+ GCC_except_table2658
+ GCC_except_table269
+ GCC_except_table2850
+ GCC_except_table290
+ GCC_except_table2910
+ GCC_except_table2939
+ GCC_except_table3003
+ GCC_except_table3032
+ GCC_except_table3033
+ GCC_except_table3034
+ GCC_except_table3205
+ GCC_except_table3207
+ GCC_except_table3214
+ GCC_except_table3311
+ GCC_except_table3315
+ GCC_except_table3328
+ GCC_except_table3439
+ GCC_except_table3497
+ GCC_except_table351
+ GCC_except_table3514
+ GCC_except_table3548
+ GCC_except_table3553
+ GCC_except_table3556
+ GCC_except_table3559
+ GCC_except_table356
+ GCC_except_table3562
+ GCC_except_table3565
+ GCC_except_table3570
+ GCC_except_table3574
+ GCC_except_table3577
+ GCC_except_table3579
+ GCC_except_table3582
+ GCC_except_table3585
+ GCC_except_table359
+ GCC_except_table3592
+ GCC_except_table3597
+ GCC_except_table3602
+ GCC_except_table3618
+ GCC_except_table3622
+ GCC_except_table3634
+ GCC_except_table366
+ GCC_except_table3666
+ GCC_except_table369
+ GCC_except_table523
+ GCC_except_table638
+ GCC_except_table677
+ GCC_except_table739
+ GCC_except_table860
+ GCC_except_table864
+ GCC_except_table887
+ GCC_except_table888
+ GCC_except_table897
+ GCC_except_table933
+ GCC_except_table964
+ _BiomeLibraryLibraryCore.frameworkLibrary.17190
+ _BiomeLibraryLibraryCore.frameworkLibrary.2932
+ _BiomeLibraryLibraryCore.frameworkLibrary.6774
+ _ContentKitLibrary.11048
+ _ContentKitLibrary.15748
+ _ContentKitLibrary.5666
+ _ContentKitLibraryCore.frameworkLibrary.11051
+ _ContentKitLibraryCore.frameworkLibrary.15758
+ _ContentKitLibraryCore.frameworkLibrary.5677
+ _CoreLocationLibraryCore.frameworkLibrary.7232
+ _CoreTelephonyLibrary
+ _CoreTelephonyLibraryCore.frameworkLibrary
+ _CoreTextLibraryCore.frameworkLibrary.10161
+ _FileProviderLibraryCore.frameworkLibrary.11033
+ _IconServicesLibrary.13970
+ _IconServicesLibraryCore.frameworkLibrary.13979
+ _ImageIOLibrary.4514
+ _ImageIOLibrary.7778
+ _ImageIOLibraryCore.frameworkLibrary.4532
+ _ImageIOLibraryCore.frameworkLibrary.7823
+ _LinkServicesLibrary.5461
+ _LinkServicesLibraryCore.frameworkLibrary.5466
+ _OBJC_CLASS_$_LNAutoShortcutsProvider
+ _OBJC_CLASS_$_WFCellularSettings
+ _OBJC_CLASS_$_WFConfiguratorRunRequest
+ _OBJC_CLASS_$_WFConfiguratorRunnerClient
+ _OBJC_CLASS_$_WFConfiguredActionButtonContextualAction
+ _OBJC_CLASS_$_WFConfiguredActionButtonIntentAction
+ _OBJC_CLASS_$_WFConfiguredActionButtonNothingAction
+ _OBJC_CLASS_$_WFConfiguredActionButtonWorkflowAction
+ _OBJC_CLASS_$_WFConfiguredSystemAction
+ _OBJC_CLASS_$_WFConfiguredSystemContextualAction
+ _OBJC_CLASS_$_WFConfiguredSystemIntentAction
+ _OBJC_CLASS_$_WFConfiguredSystemNothingAction
+ _OBJC_CLASS_$_WFConfiguredSystemWorkflowAction
+ _OBJC_CLASS_$_WFExecutableAppShortcut
+ _OBJC_CLASS_$_WFSystemActionRunnerClient
+ _OBJC_IVAR_$_WFAutoShortcutContextualAction._executableAppShortcut
+ _OBJC_IVAR_$_WFAutoShortcutContextualAction._parameterlessIdentifier
+ _OBJC_IVAR_$_WFCellularSettings._connection
+ _OBJC_IVAR_$_WFConfiguredSystemContextualAction._appShortcutIdentifier
+ _OBJC_IVAR_$_WFConfiguredSystemContextualAction._contextualAction
+ _OBJC_IVAR_$_WFConfiguredSystemIntentAction._appShortcutIdentifier
+ _OBJC_IVAR_$_WFConfiguredSystemIntentAction._contextualParameters
+ _OBJC_IVAR_$_WFConfiguredSystemIntentAction._intent
+ _OBJC_IVAR_$_WFConfiguredSystemWorkflowAction._workflowIcon
+ _OBJC_IVAR_$_WFConfiguredSystemWorkflowAction._workflowIdentifier
+ _OBJC_IVAR_$_WFContextualActionIcon._lnPropertyIdentifier
+ _OBJC_IVAR_$_WFExecutableAppShortcut._alternatePhrases
+ _OBJC_IVAR_$_WFExecutableAppShortcut._chicletColor
+ _OBJC_IVAR_$_WFExecutableAppShortcut._entityInfo
+ _OBJC_IVAR_$_WFExecutableAppShortcut._phrase
+ _OBJC_IVAR_$_WFExecutableAppShortcut._underlyingAutoShortcut
+ _OBJC_IVAR_$_WFSystemActionRunnerClient._action
+ _OBJC_IVAR_$_WFSystemActionRunnerClient._actionContext
+ _OBJC_METACLASS_$_WFCellularSettings
+ _OBJC_METACLASS_$_WFConfiguratorRunRequest
+ _OBJC_METACLASS_$_WFConfiguratorRunnerClient
+ _OBJC_METACLASS_$_WFConfiguredActionButtonContextualAction
+ _OBJC_METACLASS_$_WFConfiguredActionButtonIntentAction
+ _OBJC_METACLASS_$_WFConfiguredActionButtonNothingAction
+ _OBJC_METACLASS_$_WFConfiguredActionButtonWorkflowAction
+ _OBJC_METACLASS_$_WFConfiguredSystemAction
+ _OBJC_METACLASS_$_WFConfiguredSystemContextualAction
+ _OBJC_METACLASS_$_WFConfiguredSystemIntentAction
+ _OBJC_METACLASS_$_WFConfiguredSystemNothingAction
+ _OBJC_METACLASS_$_WFConfiguredSystemWorkflowAction
+ _OBJC_METACLASS_$_WFExecutableAppShortcut
+ _OBJC_METACLASS_$_WFSystemActionRunnerClient
+ _UIImageFunction.7813
+ _UIKitLibrary.16209
+ _UIKitLibrary.sLib.4096
+ _UIKitLibrary.sLib.7818
+ _UIKitLibrary.sLib.9964
+ _UIKitLibrary.sOnce.4091
+ _UIKitLibrary.sOnce.7808
+ _UIKitLibrary.sOnce.9957
+ _UIKitLibraryCore.frameworkLibrary.16219
+ _VCBundleIdentifierShortcutsSystemActionConfigurationExtension
+ _VCSpotlightDomainIdentifier
+ _VisionKitCoreLibraryCore.frameworkLibrary.12330
+ _WFBiomeLibrary.6770
+ _WFCellularSettingsErrorDomain
+ _WFContextualActionIconErrorDomain
+ _WFCoreTelephonyConnectionCallbackStub
+ _WFDeviceCapabilityActionButton
+ _WFEncodableErrorDictionary
+ _WFEncodableErrorObject
+ _WFEncodableErrorObject.encodableClasses
+ _WFEncodableErrorObject.onceToken
+ _WFLogCategoryAppShortcutInterpolation
+ _WFNSErrorFromCTError
+ _WFSpotlightResultRunnableLNPropertyIdentifier
+ _WFSpotlightResultRunnableTintColorNameIdentifier
+ _WFStaccatoActionIdentifierAccessibility
+ _WFStaccatoActionIdentifierCamera
+ _WFStaccatoActionIdentifierFlashlight
+ _WFStaccatoActionIdentifierFocus
+ _WFStaccatoActionIdentifierMagnifier
+ _WFStaccatoActionIdentifierShowFolder
+ _WFStaccatoActionIdentifierSilentMode
+ _WFStaccatoActionIdentifierTranslate
+ _WFStaccatoActionIdentifierVoiceMemos
+ _WFSystemActionTypeActionButton
+ _WFWorkflowRunSourceSystemAction
+ __OBJC_$_CATEGORY_INImage_$_Loading
+ __OBJC_$_CLASS_METHODS_VCVoiceShortcutClient(MenuBar|Sting|AppIntents|Sleep|TopHitContextual|VoiceShortcuts|Sync|AutoShortcuts|Accessibility|Staccato|Automations|ContextualActions|ShareSheet|Suggestions|Spotlight)
+ __OBJC_$_CLASS_METHODS_WFAppIcon(IconicSymbolUtilities)
+ __OBJC_$_CLASS_METHODS_WFCellularSettings
+ __OBJC_$_CLASS_METHODS_WFColor(Hexadecimal|WorkflowPalette|StandardColors|Convenience|Focus|IconicSymbolUtilities|Gradient)
+ __OBJC_$_CLASS_METHODS_WFConfiguredStaccatoAction(Staccato)
+ __OBJC_$_CLASS_METHODS_WFConfiguredSystemContextualAction
+ __OBJC_$_CLASS_METHODS_WFConfiguredSystemIntentAction
+ __OBJC_$_CLASS_METHODS_WFConfiguredSystemWorkflowAction
+ __OBJC_$_CLASS_METHODS_WFExecutableAppShortcut
+ __OBJC_$_CLASS_METHODS_WFIcon
+ __OBJC_$_CLASS_METHODS_WFStaccatoWorkflowRunnerClient
+ __OBJC_$_CLASS_METHODS_WFSymbolIcon(IconicSymbolUtilities)
+ __OBJC_$_CLASS_METHODS_WFSystemActionRunnerClient
+ __OBJC_$_CLASS_PROP_LIST_WFExecutableAppShortcut
+ __OBJC_$_INSTANCE_METHODS_INImage(Loading)
+ __OBJC_$_INSTANCE_METHODS_VCVoiceShortcutClient(MenuBar|Sting|AppIntents|Sleep|TopHitContextual|VoiceShortcuts|Sync|AutoShortcuts|Accessibility|Staccato|Automations|ContextualActions|ShareSheet|Suggestions|Spotlight)
+ __OBJC_$_INSTANCE_METHODS_WFAppIcon(IconicSymbolUtilities)
+ __OBJC_$_INSTANCE_METHODS_WFCellularSettings
+ __OBJC_$_INSTANCE_METHODS_WFColor(Hexadecimal|WorkflowPalette|StandardColors|Convenience|Focus|IconicSymbolUtilities|Gradient)
+ __OBJC_$_INSTANCE_METHODS_WFConfiguratorRunRequest
+ __OBJC_$_INSTANCE_METHODS_WFConfiguratorRunnerClient
+ __OBJC_$_INSTANCE_METHODS_WFConfiguredStaccatoAction(Staccato)
+ __OBJC_$_INSTANCE_METHODS_WFConfiguredSystemContextualAction
+ __OBJC_$_INSTANCE_METHODS_WFConfiguredSystemIntentAction
+ __OBJC_$_INSTANCE_METHODS_WFConfiguredSystemNothingAction
+ __OBJC_$_INSTANCE_METHODS_WFConfiguredSystemWorkflowAction
+ __OBJC_$_INSTANCE_METHODS_WFExecutableAppShortcut
+ __OBJC_$_INSTANCE_METHODS_WFIcon
+ __OBJC_$_INSTANCE_METHODS_WFSymbolIcon(IconicSymbolUtilities)
+ __OBJC_$_INSTANCE_METHODS_WFSystemActionRunnerClient
+ __OBJC_$_INSTANCE_VARIABLES_WFCellularSettings
+ __OBJC_$_INSTANCE_VARIABLES_WFConfiguredSystemContextualAction
+ __OBJC_$_INSTANCE_VARIABLES_WFConfiguredSystemIntentAction
+ __OBJC_$_INSTANCE_VARIABLES_WFConfiguredSystemWorkflowAction
+ __OBJC_$_INSTANCE_VARIABLES_WFExecutableAppShortcut
+ __OBJC_$_INSTANCE_VARIABLES_WFSystemActionRunnerClient
+ __OBJC_$_PROP_LIST_WFCellularSettings
+ __OBJC_$_PROP_LIST_WFConfiguredSystemContextualAction
+ __OBJC_$_PROP_LIST_WFConfiguredSystemIntentAction
+ __OBJC_$_PROP_LIST_WFConfiguredSystemWorkflowAction
+ __OBJC_$_PROP_LIST_WFExecutableAppShortcut
+ __OBJC_$_PROP_LIST_WFSystemActionRunnerClient
+ __OBJC_$_PROTOCOL_CLASS_METHODS_WFSpotlightResultRunnable
+ __OBJC_CLASS_PROTOCOLS_$_WFExecutableAppShortcut
+ __OBJC_CLASS_RO_$_WFCellularSettings
+ __OBJC_CLASS_RO_$_WFConfiguratorRunRequest
+ __OBJC_CLASS_RO_$_WFConfiguratorRunnerClient
+ __OBJC_CLASS_RO_$_WFConfiguredActionButtonContextualAction
+ __OBJC_CLASS_RO_$_WFConfiguredActionButtonIntentAction
+ __OBJC_CLASS_RO_$_WFConfiguredActionButtonNothingAction
+ __OBJC_CLASS_RO_$_WFConfiguredActionButtonWorkflowAction
+ __OBJC_CLASS_RO_$_WFConfiguredSystemAction
+ __OBJC_CLASS_RO_$_WFConfiguredSystemContextualAction
+ __OBJC_CLASS_RO_$_WFConfiguredSystemIntentAction
+ __OBJC_CLASS_RO_$_WFConfiguredSystemNothingAction
+ __OBJC_CLASS_RO_$_WFConfiguredSystemWorkflowAction
+ __OBJC_CLASS_RO_$_WFExecutableAppShortcut
+ __OBJC_CLASS_RO_$_WFSystemActionRunnerClient
+ __OBJC_METACLASS_RO_$_WFCellularSettings
+ __OBJC_METACLASS_RO_$_WFConfiguratorRunRequest
+ __OBJC_METACLASS_RO_$_WFConfiguratorRunnerClient
+ __OBJC_METACLASS_RO_$_WFConfiguredActionButtonContextualAction
+ __OBJC_METACLASS_RO_$_WFConfiguredActionButtonIntentAction
+ __OBJC_METACLASS_RO_$_WFConfiguredActionButtonNothingAction
+ __OBJC_METACLASS_RO_$_WFConfiguredActionButtonWorkflowAction
+ __OBJC_METACLASS_RO_$_WFConfiguredSystemAction
+ __OBJC_METACLASS_RO_$_WFConfiguredSystemContextualAction
+ __OBJC_METACLASS_RO_$_WFConfiguredSystemIntentAction
+ __OBJC_METACLASS_RO_$_WFConfiguredSystemNothingAction
+ __OBJC_METACLASS_RO_$_WFConfiguredSystemWorkflowAction
+ __OBJC_METACLASS_RO_$_WFExecutableAppShortcut
+ __OBJC_METACLASS_RO_$_WFSystemActionRunnerClient
+ ___104+[WFObservableResult drawGlyphsIntoWorkflowsIfNecessary:glyphSize:roundedIcon:synchronously:completion:]_block_invoke.191
+ ___104+[WFObservableResult drawGlyphsIntoWorkflowsIfNecessary:glyphSize:roundedIcon:synchronously:completion:]_block_invoke.200
+ ___104+[WFObservableResult drawGlyphsIntoWorkflowsIfNecessary:glyphSize:roundedIcon:synchronously:completion:]_block_invoke_2.197
+ ___104+[WFObservableResult drawGlyphsIntoWorkflowsIfNecessary:glyphSize:roundedIcon:synchronously:completion:]_block_invoke_2.201
+ ___37+[WFCellularSettings defaultSettings]_block_invoke
+ ___52-[INImage(Loading) retrieveImageDataWithCompletion:]_block_invoke
+ ___60-[WFContextualActionIcon loadLNPropertyImageWithCompletion:]_block_invoke
+ ___62-[VCVoiceShortcutClient(Sync) coherenceEnabledWithCompletion:]_block_invoke
+ ___62-[VCVoiceShortcutClient(Sync) coherenceEnabledWithCompletion:]_block_invoke_2
+ ___63+[WFColor(IconicSymbolUtilities) tintColorForBundleIdentifier:]_block_invoke
+ ___65-[VCVoiceShortcutClient(Sync) toprakEngineEnabledWithCompletion:]_block_invoke
+ ___65-[VCVoiceShortcutClient(Sync) toprakEngineEnabledWithCompletion:]_block_invoke_2
+ ___66+[WFContextualActionIcon iconWithINImage:displayStyle:completion:]_block_invoke
+ ___66-[WFConfiguratorRunRequest initWithInputStrings:presentationMode:]_block_invoke
+ ___70-[VCVoiceShortcutClient(Sync) setCoherenceMigrationStatus:completion:]_block_invoke
+ ___70-[VCVoiceShortcutClient(Sync) setCoherenceMigrationStatus:completion:]_block_invoke_2
+ ___71-[VCVoiceShortcutClient(Sync) coherenceMigrationEnabledWithCompletion:]_block_invoke
+ ___71-[VCVoiceShortcutClient(Sync) coherenceMigrationEnabledWithCompletion:]_block_invoke_2
+ ___86+[WFSymbolIcon(IconicSymbolUtilities) symbolIconForActionIdentifier:bundleIdentifier:]_block_invoke
+ ___BiomeLibraryLibraryCore_block_invoke.17191
+ ___BiomeLibraryLibraryCore_block_invoke.2933
+ ___BiomeLibraryLibraryCore_block_invoke.6775
+ ___Block_byref_object_copy_.1047
+ ___Block_byref_object_copy_.10882
+ ___Block_byref_object_copy_.12560
+ ___Block_byref_object_copy_.13626
+ ___Block_byref_object_copy_.15769
+ ___Block_byref_object_copy_.1624
+ ___Block_byref_object_copy_.17896
+ ___Block_byref_object_copy_.2449
+ ___Block_byref_object_copy_.4626
+ ___Block_byref_object_copy_.4875
+ ___Block_byref_object_copy_.8524
+ ___Block_byref_object_dispose_.1048
+ ___Block_byref_object_dispose_.10883
+ ___Block_byref_object_dispose_.12561
+ ___Block_byref_object_dispose_.13627
+ ___Block_byref_object_dispose_.15770
+ ___Block_byref_object_dispose_.1625
+ ___Block_byref_object_dispose_.17897
+ ___Block_byref_object_dispose_.2450
+ ___Block_byref_object_dispose_.4627
+ ___Block_byref_object_dispose_.4876
+ ___Block_byref_object_dispose_.8525
+ ___ContentKitLibraryCore_block_invoke.11052
+ ___ContentKitLibraryCore_block_invoke.15759
+ ___ContentKitLibraryCore_block_invoke.5678
+ ___CoreLocationLibraryCore_block_invoke.7233
+ ___CoreTelephonyLibraryCore_block_invoke
+ ___CoreTextLibraryCore_block_invoke.10162
+ ___FileProviderLibraryCore_block_invoke.11034
+ ___IconServicesLibraryCore_block_invoke.13980
+ ___ImageIOLibraryCore_block_invoke.4533
+ ___ImageIOLibraryCore_block_invoke.7824
+ ___LinkServicesLibraryCore_block_invoke.5467
+ ___UIKitLibraryCore_block_invoke.16220
+ ___UIKitLibrary_block_invoke.4094
+ ___UIKitLibrary_block_invoke.7816
+ ___UIKitLibrary_block_invoke.9962
+ ___VisionKitCoreLibraryCore_block_invoke.12331
+ ___WFEncodableErrorObject_block_invoke
+ ___block_descriptor_32_e36_"WFContentItem"24?0"NSString"8Q16l
+ ___block_descriptor_40_e8_32bs_e29_v24?0"INImage"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e44_v24?0"WFContextualActionIcon"8"NSError"16ls32l8
+ ___block_literal_global.101.12620
+ ___block_literal_global.10291
+ ___block_literal_global.105
+ ___block_literal_global.1073
+ ___block_literal_global.117
+ ___block_literal_global.12016
+ ___block_literal_global.12406
+ ___block_literal_global.12583
+ ___block_literal_global.12891
+ ___block_literal_global.13001
+ ___block_literal_global.13376
+ ___block_literal_global.136.12407
+ ___block_literal_global.13630
+ ___block_literal_global.141
+ ___block_literal_global.14549
+ ___block_literal_global.146.12398
+ ___block_literal_global.149
+ ___block_literal_global.15056
+ ___block_literal_global.15085
+ ___block_literal_global.151
+ ___block_literal_global.15746
+ ___block_literal_global.15787
+ ___block_literal_global.15798
+ ___block_literal_global.160
+ ___block_literal_global.1601
+ ___block_literal_global.16034
+ ___block_literal_global.16289
+ ___block_literal_global.165
+ ___block_literal_global.16895
+ ___block_literal_global.16905
+ ___block_literal_global.17.4888
+ ___block_literal_global.170
+ ___block_literal_global.17062
+ ___block_literal_global.180.17894
+ ___block_literal_global.18038
+ ___block_literal_global.181
+ ___block_literal_global.1818
+ ___block_literal_global.182.17892
+ ___block_literal_global.187.12375
+ ___block_literal_global.192
+ ___block_literal_global.194
+ ___block_literal_global.198
+ ___block_literal_global.204
+ ___block_literal_global.210
+ ___block_literal_global.219
+ ___block_literal_global.225
+ ___block_literal_global.231
+ ___block_literal_global.237
+ ___block_literal_global.243
+ ___block_literal_global.249.12326
+ ___block_literal_global.254
+ ___block_literal_global.2573
+ ___block_literal_global.260
+ ___block_literal_global.269
+ ___block_literal_global.275
+ ___block_literal_global.286
+ ___block_literal_global.291
+ ___block_literal_global.3086
+ ___block_literal_global.341
+ ___block_literal_global.346
+ ___block_literal_global.3678
+ ___block_literal_global.390
+ ___block_literal_global.4013
+ ___block_literal_global.4097
+ ___block_literal_global.4260
+ ___block_literal_global.430
+ ___block_literal_global.4553
+ ___block_literal_global.4669
+ ___block_literal_global.47.2581
+ ___block_literal_global.4795
+ ___block_literal_global.4882
+ ___block_literal_global.4904
+ ___block_literal_global.50.13631
+ ___block_literal_global.50.14766
+ ___block_literal_global.503
+ ___block_literal_global.5663
+ ___block_literal_global.5741
+ ___block_literal_global.60
+ ___block_literal_global.6987
+ ___block_literal_global.7809
+ ___block_literal_global.7876
+ ___block_literal_global.8044
+ ___block_literal_global.8355
+ ___block_literal_global.85
+ ___block_literal_global.8543
+ ___block_literal_global.87
+ ___block_literal_global.8906
+ ___block_literal_global.9626
+ ___block_literal_global.9958
+ ___getBiomeLibrarySymbolLoc_block_invoke.17181
+ ___getBiomeLibrarySymbolLoc_block_invoke.2929
+ ___getBiomeLibrarySymbolLoc_block_invoke.6772
+ ___getCGImageSourceCopyPropertiesAtIndexSymbolLoc_block_invoke.7796
+ ___getCGImageSourceCreateImageAtIndexSymbolLoc_block_invoke.7792
+ ___getCGImageSourceCreateWithDataSymbolLoc_block_invoke.7784
+ ___getCGImageSourceGetCountSymbolLoc_block_invoke.7788
+ ___getCLLocationClass_block_invoke.7231
+ ___getFPSandboxingURLWrapperClass_block_invoke.11029
+ ___getISImageDescriptorClass_block_invoke.13967
+ ___getVKCRemoveBackgroundRequestHandlerClass_block_invoke.12329
+ ___getWFAppShortcutInterpolationLogObject_block_invoke
+ ___getWFContentCollectionClass_block_invoke.5665
+ ___getWFContentItemClass_block_invoke.11027
+ ___getWFContentItemClass_block_invoke.15744
+ ___get_CTServerConnectionCreateWithIdentifierSymbolLoc_block_invoke
+ ___get_CTServerConnectionGetCellularDataIsEnabledSymbolLoc_block_invoke
+ ___get_CTServerConnectionGetCellularDataSettingsSymbolLoc_block_invoke
+ ___getkCGImagePropertyOrientationSymbolLoc_block_invoke.7802
+ ___getkISImageDescriptorHomeScreenSymbolLoc_block_invoke.13969
+ __unnamed_array_storage.12605
+ __unnamed_array_storage.14532
+ __unnamed_array_storage.15421
+ __unnamed_array_storage.15803
+ __unnamed_array_storage.2152
+ __unnamed_array_storage.2738
+ __unnamed_array_storage.3090
+ __unnamed_array_storage.3726
+ __unnamed_array_storage.4684
+ __unnamed_array_storage.6991
+ __unnamed_array_storage.8420
+ __unnamed_array_storage.8949
+ _audit_stringBiomeLibrary.17195
+ _audit_stringBiomeLibrary.2936
+ _audit_stringBiomeLibrary.6778
+ _audit_stringContentKit.11055
+ _audit_stringContentKit.15764
+ _audit_stringContentKit.5684
+ _audit_stringCoreLocation.7248
+ _audit_stringCoreTelephony
+ _audit_stringCoreText.10166
+ _audit_stringFileProvider.11047
+ _audit_stringIconServices.13983
+ _audit_stringImageIO.4536
+ _audit_stringImageIO.7827
+ _audit_stringLinkServices.5473
+ _audit_stringUIKit.16223
+ _audit_stringVisionKitCore.12334
+ _capabilities.cachedAnswer.202
+ _capabilities.cachedAnswer.208
+ _capabilities.cachedAnswer.217
+ _capabilities.cachedAnswer.223
+ _capabilities.cachedAnswer.229
+ _capabilities.cachedAnswer.235
+ _capabilities.cachedAnswer.241
+ _capabilities.cachedAnswer.247
+ _capabilities.cachedAnswer.258
+ _capabilities.cachedAnswer.267
+ _capabilities.cachedAnswer.273
+ _capabilities.onceTokenkMGQRingerButtonCapability
+ _classUIImage.7811
+ _defaultSettings.onceToken
+ _defaultSettings.settings
+ _getBiomeLibrarySymbolLoc.ptr.17180
+ _getBiomeLibrarySymbolLoc.ptr.2928
+ _getBiomeLibrarySymbolLoc.ptr.6771
+ _getCGImageSourceCopyPropertiesAtIndexSymbolLoc.ptr.7795
+ _getCGImageSourceCreateImageAtIndexSymbolLoc.ptr.7791
+ _getCGImageSourceCreateWithDataSymbolLoc.ptr.7783
+ _getCGImageSourceGetCountSymbolLoc.ptr.7787
+ _getCLLocationClass.softClass.7230
+ _getFPSandboxingURLWrapperClass.softClass.11028
+ _getISImageDescriptorClass.softClass.13966
+ _getUIImageClass.7805
+ _getVKCRemoveBackgroundRequestHandlerClass.softClass.12328
+ _getWFAppShortcutInterpolationLogObject
+ _getWFAppShortcutInterpolationLogObject.log
+ _getWFAppShortcutInterpolationLogObject.onceToken
+ _getWFContentCollectionClass.softClass.5664
+ _getWFContentItemClass.softClass.11026
+ _getWFContentItemClass.softClass.15743
+ _get_CTServerConnectionCreateWithIdentifierSymbolLoc.ptr
+ _get_CTServerConnectionGetCellularDataIsEnabledSymbolLoc.ptr
+ _get_CTServerConnectionGetCellularDataSettingsSymbolLoc.ptr
+ _getkCGImagePropertyOrientationSymbolLoc.ptr.7801
+ _getkISImageDescriptorHomeScreenSymbolLoc.ptr.13968
+ _initUIImage.7807
+ _objc_msgSend$WiFiAvailabilityStatus
+ _objc_msgSend$_isSystem
+ _objc_msgSend$_name
+ _objc_msgSend$_uri
+ _objc_msgSend$alternatePhrases
+ _objc_msgSend$basePhraseTemplates
+ _objc_msgSend$coherenceEnabledWithCompletion:
+ _objc_msgSend$coherenceMigrationEnabledWithCompletion:
+ _objc_msgSend$collectionWithItems:
+ _objc_msgSend$defaultContextualActionContext
+ _objc_msgSend$defaultSettings
+ _objc_msgSend$dictionaryWithObject:forKey:
+ _objc_msgSend$executableAppShortcut
+ _objc_msgSend$hexValue
+ _objc_msgSend$iconWithINImage:displayStyle:completion:
+ _objc_msgSend$iconWithImageURL:displayStyle:
+ _objc_msgSend$inImage
+ _objc_msgSend$initWithAutoShortcut:identifier:parameterlessIdentifier:phrase:alternativePhrases:bundleIdentifier:actionIdentifier:orderOfShortcut:parentAction:prominentDisplayEligibility:executableAppShortcut:
+ _objc_msgSend$initWithAutoShortcut:phrase:alternatePhrases:entityInfo:
+ _objc_msgSend$initWithIdentifier:associatedBundleIdentifier:name:previewIcon:shortcutsMetadata:
+ _objc_msgSend$initWithInputStrings:presentationMode:
+ _objc_msgSend$initWithIntent:named:previewIcon:appShortcutIdentifier:contextualParameters:shortcutsMetadata:
+ _objc_msgSend$initWithIntent:named:previewIcon:appShortcutIdentifier:templateParameterValues:contextualParameters:shortcutsMetadata:
+ _objc_msgSend$initWithLNPropertyIdentifier:displayStyle:
+ _objc_msgSend$initWithSystemContextualAction:
+ _objc_msgSend$initWithSystemIntentAction:
+ _objc_msgSend$initWithSystemNothingAction:
+ _objc_msgSend$initWithSystemWorkflowAction:
+ _objc_msgSend$isCellularDataCapableWithError:
+ _objc_msgSend$isTopHitEligible
+ _objc_msgSend$itemWithObject:
+ _objc_msgSend$lnPropertyIdentifier
+ _objc_msgSend$parameterlessIdentifier
+ _objc_msgSend$previewIcon
+ _objc_msgSend$propertiesForIdentifiers:error:
+ _objc_msgSend$retrieveImageDataWithCompletion:
+ _objc_msgSend$secondaryLabelColor
+ _objc_msgSend$secondarySystemFillColor
+ _objc_msgSend$setCoherenceMigrationStatus:completion:
+ _objc_msgSend$setSubtitle:
+ _objc_msgSend$setSurface:
+ _objc_msgSend$spotlightActionIdentifier
+ _objc_msgSend$symbolIconForActionIdentifier:bundleIdentifier:
+ _objc_msgSend$tertiarySystemBackgroundColor
+ _objc_msgSend$tintColorForBundleIdentifier:
+ _objc_msgSend$toprakEngineEnabledWithCompletion:
+ _objc_msgSend$useNewDataSource
+ _objc_msgSend$usesPreviewIconSymbolOverride
+ _objc_msgSend$wfIcon
+ _screenBounds.cachedAnswer.134
+ _sharedManager.onceToken.8542
+ _symbolIconForActionIdentifier:bundleIdentifier:.actionIdentifierMapping
+ _symbolIconForActionIdentifier:bundleIdentifier:.bundleIdentifierMapping
+ _symbolIconForActionIdentifier:bundleIdentifier:.onceToken
+ _systemName.cachedAnswer.185
+ _timestampDateFormatter.dateFormatter.13002
+ _timestampDateFormatter.onceToken.13000
+ _tintColorForBundleIdentifier:.bundleIdentifierMapping
+ _tintColorForBundleIdentifier:.onceToken
- +[WFAppIcon(AssociatedLogo) localAssetForBundleIdentifier:]
- +[WFAutoShortcutContextualAction spotlightDomainIdentifier]
- +[WFConfiguredStaccatoTopHitAction supportsSecureCoding]
- +[WFConfiguredStaccatoWorkflowAction supportsSecureCoding]
- +[WFContextualAction(Spotlight) spotlightDomainIdentifier]
- +[WFExecutableAutoShortcut supportsSecureCoding]
- +[WFIcon(IconicActionSymbol) apertureIconForActionIdentifier:]
- +[WFSymbolIcon(IconicApertureSymbols) alarm]
- +[WFSymbolIcon(IconicApertureSymbols) audiobook]
- +[WFSymbolIcon(IconicApertureSymbols) books]
- +[WFSymbolIcon(IconicApertureSymbols) codeScanner]
- +[WFSymbolIcon(IconicApertureSymbols) keynote]
- +[WFSymbolIcon(IconicApertureSymbols) numbers]
- +[WFSymbolIcon(IconicApertureSymbols) pages]
- +[WFSymbolIcon(IconicApertureSymbols) remote]
- +[WFSymbolIcon(IconicApertureSymbols) scanDocument]
- +[WFSymbolIcon(IconicApertureSymbols) timer]
- +[WFSymbolIcon(IconicApertureSymbols) voiceMemos]
- +[WFToggleAlarmContextualAction spotlightDomainIdentifier]
- +[WFToggleFocusModeContextualAction spotlightDomainIdentifier]
- +[WFToggleSettingContextualAction spotlightDomainIdentifier]
- -[WFAppIcon(AssociatedLogo) associatedLogo]
- -[WFAutoShortcutContextualAction initWithAutoShortcut:identifier:phrase:alternativePhrases:bundleIdentifier:actionIdentifier:orderOfShortcut:parentAction:prominentDisplayEligibility:]
- -[WFConfiguredStaccatoAction initWithIdentifier:sectionIdentifier:associatedBundleIdentifier:name:systemImageName:shortcutsMetadata:]
- -[WFConfiguredStaccatoAction isSystemStaccatoAction]
- -[WFConfiguredStaccatoAction sectionIdentifier]
- -[WFConfiguredStaccatoAction setSectionIdentifier:]
- -[WFConfiguredStaccatoAction setSystemImageName:]
- -[WFConfiguredStaccatoAction systemImageName]
- -[WFConfiguredStaccatoAction tintColor]
- -[WFConfiguredStaccatoIntentAction appShortcutIdentifier]
- -[WFConfiguredStaccatoIntentAction contextualParameters]
- -[WFConfiguredStaccatoIntentAction description]
- -[WFConfiguredStaccatoIntentAction initWithIntent:named:systemImageName:]
- -[WFConfiguredStaccatoIntentAction initWithIntent:sectionIdentifier:named:appShortcutIdentifier:systemImageName:templateParameterValues:contextualParameters:shortcutsMetadata:]
- -[WFConfiguredStaccatoIntentAction intent]
- -[WFConfiguredStaccatoTopHitAction .cxx_destruct]
- -[WFConfiguredStaccatoTopHitAction appShortcutIdentifier]
- -[WFConfiguredStaccatoTopHitAction contextualAction]
- -[WFConfiguredStaccatoTopHitAction description]
- -[WFConfiguredStaccatoTopHitAction encodeWithCoder:]
- -[WFConfiguredStaccatoTopHitAction hash]
- -[WFConfiguredStaccatoTopHitAction initWithCoder:]
- -[WFConfiguredStaccatoTopHitAction initWithContextualAction:appShortcutIdentifier:shortcutsMetadata:]
- -[WFConfiguredStaccatoTopHitAction isEqual:]
- -[WFConfiguredStaccatoWorkflowAction .cxx_destruct]
- -[WFConfiguredStaccatoWorkflowAction description]
- -[WFConfiguredStaccatoWorkflowAction encodeWithCoder:]
- -[WFConfiguredStaccatoWorkflowAction hash]
- -[WFConfiguredStaccatoWorkflowAction initWithCoder:]
- -[WFConfiguredStaccatoWorkflowAction initWithName:workflowIdentifier:workflowIcon:associatedBundleIdentifier:shortcutsMetadata:]
- -[WFConfiguredStaccatoWorkflowAction initWithWorkflow:shortcutsMetadata:]
- -[WFConfiguredStaccatoWorkflowAction isEqual:]
- -[WFConfiguredStaccatoWorkflowAction previewIcon]
- -[WFConfiguredStaccatoWorkflowAction setWorkflowIcon:]
- -[WFConfiguredStaccatoWorkflowAction workflowIcon]
- -[WFConfiguredStaccatoWorkflowAction workflowIdentifier]
- -[WFExecutableAutoShortcut .cxx_destruct]
- -[WFExecutableAutoShortcut base64ArchivedData]
- -[WFExecutableAutoShortcut chicletColor]
- -[WFExecutableAutoShortcut encodeWithCoder:]
- -[WFExecutableAutoShortcut entityInfo]
- -[WFExecutableAutoShortcut fullyQualifiedIdentifier]
- -[WFExecutableAutoShortcut id]
- -[WFExecutableAutoShortcut initWithAutoShortcut:phrase:entityInfo:]
- -[WFExecutableAutoShortcut initWithCoder:]
- -[WFExecutableAutoShortcut isDeprecatedStyle]
- -[WFExecutableAutoShortcut namedQueryInfo]
- -[WFExecutableAutoShortcut phrase]
- -[WFExecutableAutoShortcut shortcutDescription]
- -[WFExecutableAutoShortcut triggerPhrase]
- -[WFExecutableAutoShortcut underlyingAutoShortcut]
- -[WFStaccatoWorkflowRunnerClient .cxx_destruct]
- -[WFStaccatoWorkflowRunnerClient actionContext]
- -[WFStaccatoWorkflowRunnerClient action]
- -[WFStaccatoWorkflowRunnerClient initWithDescriptor:runRequest:]
- -[WFStaccatoWorkflowRunnerClient initWithLinkStaccatoAction:interactionType:preciseTimeStamp:]
- -[WFStaccatoWorkflowRunnerClient initWithTopHitStaccatoAction:]
- -[WFStaccatoWorkflowRunnerClient initWithWorkflowStaccatoAction:]
- -[WFStaccatoWorkflowRunnerClient setAction:]
- -[WFStaccatoWorkflowRunnerClient setActionContext:]
- GCC_except_table1072
- GCC_except_table1078
- GCC_except_table1091
- GCC_except_table1118
- GCC_except_table1123
- GCC_except_table1129
- GCC_except_table1173
- GCC_except_table1176
- GCC_except_table1183
- GCC_except_table1187
- GCC_except_table1192
- GCC_except_table1312
- GCC_except_table1392
- GCC_except_table1405
- GCC_except_table1451
- GCC_except_table1474
- GCC_except_table1532
- GCC_except_table1534
- GCC_except_table1536
- GCC_except_table1537
- GCC_except_table1539
- GCC_except_table1548
- GCC_except_table1556
- GCC_except_table1558
- GCC_except_table1578
- GCC_except_table1610
- GCC_except_table1627
- GCC_except_table1664
- GCC_except_table169
- GCC_except_table1693
- GCC_except_table1737
- GCC_except_table1748
- GCC_except_table1756
- GCC_except_table1826
- GCC_except_table1883
- GCC_except_table1891
- GCC_except_table1898
- GCC_except_table2091
- GCC_except_table2141
- GCC_except_table2145
- GCC_except_table2150
- GCC_except_table2181
- GCC_except_table2274
- GCC_except_table2277
- GCC_except_table2284
- GCC_except_table2290
- GCC_except_table2295
- GCC_except_table2314
- GCC_except_table2323
- GCC_except_table2462
- GCC_except_table2545
- GCC_except_table2548
- GCC_except_table2621
- GCC_except_table2627
- GCC_except_table2628
- GCC_except_table2634
- GCC_except_table2636
- GCC_except_table2648
- GCC_except_table268
- GCC_except_table2832
- GCC_except_table289
- GCC_except_table2892
- GCC_except_table2921
- GCC_except_table2985
- GCC_except_table3014
- GCC_except_table3015
- GCC_except_table3016
- GCC_except_table3183
- GCC_except_table3185
- GCC_except_table3192
- GCC_except_table3289
- GCC_except_table3293
- GCC_except_table3306
- GCC_except_table331
- GCC_except_table336
- GCC_except_table339
- GCC_except_table3410
- GCC_except_table3452
- GCC_except_table346
- GCC_except_table3481
- GCC_except_table3486
- GCC_except_table3489
- GCC_except_table349
- GCC_except_table3492
- GCC_except_table3495
- GCC_except_table3498
- GCC_except_table3503
- GCC_except_table3507
- GCC_except_table3510
- GCC_except_table3512
- GCC_except_table3515
- GCC_except_table3518
- GCC_except_table3525
- GCC_except_table3530
- GCC_except_table3535
- GCC_except_table3551
- GCC_except_table3555
- GCC_except_table3567
- GCC_except_table3599
- GCC_except_table376
- GCC_except_table518
- GCC_except_table633
- GCC_except_table672
- GCC_except_table734
- GCC_except_table858
- GCC_except_table862
- GCC_except_table884
- GCC_except_table885
- GCC_except_table895
- GCC_except_table950
- GCC_except_table979
- _BiomeLibraryLibraryCore.frameworkLibrary.16859
- _BiomeLibraryLibraryCore.frameworkLibrary.2807
- _BiomeLibraryLibraryCore.frameworkLibrary.6938
- _ContentKitLibrary.10938
- _ContentKitLibrary.15555
- _ContentKitLibraryCore.frameworkLibrary.10940
- _ContentKitLibraryCore.frameworkLibrary.15565
- _CoreLocationLibraryCore.frameworkLibrary.7401
- _CoreTextLibraryCore.frameworkLibrary.10051
- _FileProviderLibraryCore.frameworkLibrary.10922
- _IconServicesLibrary.13794
- _IconServicesLibraryCore.frameworkLibrary.13804
- _ImageIOLibrary.4429
- _ImageIOLibrary.7951
- _ImageIOLibraryCore.frameworkLibrary.4447
- _ImageIOLibraryCore.frameworkLibrary.7996
- _LinkServicesLibrary.5623
- _LinkServicesLibraryCore.frameworkLibrary.5626
- _OBJC_CLASS_$_WFExecutableAutoShortcut
- _OBJC_IVAR_$_WFConfiguredStaccatoAction._sectionIdentifier
- _OBJC_IVAR_$_WFConfiguredStaccatoAction._systemImageName
- _OBJC_IVAR_$_WFConfiguredStaccatoIntentAction._appShortcutIdentifier
- _OBJC_IVAR_$_WFConfiguredStaccatoIntentAction._contextualParameters
- _OBJC_IVAR_$_WFConfiguredStaccatoIntentAction._intent
- _OBJC_IVAR_$_WFConfiguredStaccatoTopHitAction._appShortcutIdentifier
- _OBJC_IVAR_$_WFConfiguredStaccatoTopHitAction._contextualAction
- _OBJC_IVAR_$_WFConfiguredStaccatoWorkflowAction._workflowIcon
- _OBJC_IVAR_$_WFConfiguredStaccatoWorkflowAction._workflowIdentifier
- _OBJC_IVAR_$_WFExecutableAutoShortcut._chicletColor
- _OBJC_IVAR_$_WFExecutableAutoShortcut._entityInfo
- _OBJC_IVAR_$_WFExecutableAutoShortcut._phrase
- _OBJC_IVAR_$_WFExecutableAutoShortcut._underlyingAutoShortcut
- _OBJC_IVAR_$_WFStaccatoWorkflowRunnerClient._action
- _OBJC_IVAR_$_WFStaccatoWorkflowRunnerClient._actionContext
- _OBJC_METACLASS_$_WFExecutableAutoShortcut
- _UIImageFunction.7986
- _UIKitLibrary.16016
- _UIKitLibrary.sLib.4026
- _UIKitLibrary.sLib.7991
- _UIKitLibrary.sLib.9855
- _UIKitLibrary.sOnce.4021
- _UIKitLibrary.sOnce.7981
- _UIKitLibrary.sOnce.9848
- _UIKitLibraryCore.frameworkLibrary.16026
- _VCBundleIdentifierShortcutsStaccatoConfigurationExtension
- _VisionKitCoreLibraryCore.frameworkLibrary.12191
- _WFBiomeLibrary.6933
- _WFVoiceMemosActionIdentifier
- __OBJC_$_CLASS_METHODS_VCVoiceShortcutClient(MenuBar|Sting|AppIntents|Sleep|TopHitContextual|VoiceShortcuts|AutoShortcuts|Accessibility|Staccato|Automations|ContextualActions|ShareSheet|Suggestions|Spotlight)
- __OBJC_$_CLASS_METHODS_WFAppIcon(AssociatedLogo)
- __OBJC_$_CLASS_METHODS_WFColor(Hexadecimal|WorkflowPalette|StandardColors|Convenience|Focus|Gradient)
- __OBJC_$_CLASS_METHODS_WFConfiguredStaccatoAction
- __OBJC_$_CLASS_METHODS_WFConfiguredStaccatoTopHitAction
- __OBJC_$_CLASS_METHODS_WFConfiguredStaccatoWorkflowAction
- __OBJC_$_CLASS_METHODS_WFExecutableAutoShortcut
- __OBJC_$_CLASS_METHODS_WFIcon(IconicActionSymbol)
- __OBJC_$_CLASS_METHODS_WFSymbolIcon(IconicApertureSymbols)
- __OBJC_$_CLASS_PROP_LIST_WFExecutableAutoShortcut
- __OBJC_$_INSTANCE_METHODS_VCVoiceShortcutClient(MenuBar|Sting|AppIntents|Sleep|TopHitContextual|VoiceShortcuts|AutoShortcuts|Accessibility|Staccato|Automations|ContextualActions|ShareSheet|Suggestions|Spotlight)
- __OBJC_$_INSTANCE_METHODS_WFAppIcon(AssociatedLogo)
- __OBJC_$_INSTANCE_METHODS_WFColor(Hexadecimal|WorkflowPalette|StandardColors|Convenience|Focus|Gradient)
- __OBJC_$_INSTANCE_METHODS_WFConfiguredStaccatoAction
- __OBJC_$_INSTANCE_METHODS_WFConfiguredStaccatoTopHitAction
- __OBJC_$_INSTANCE_METHODS_WFConfiguredStaccatoWorkflowAction
- __OBJC_$_INSTANCE_METHODS_WFExecutableAutoShortcut
- __OBJC_$_INSTANCE_METHODS_WFIcon(IconicActionSymbol)
- __OBJC_$_INSTANCE_METHODS_WFSymbolIcon(IconicApertureSymbols)
- __OBJC_$_INSTANCE_VARIABLES_WFConfiguredStaccatoTopHitAction
- __OBJC_$_INSTANCE_VARIABLES_WFConfiguredStaccatoWorkflowAction
- __OBJC_$_INSTANCE_VARIABLES_WFExecutableAutoShortcut
- __OBJC_$_PROP_LIST_WFConfiguredStaccatoAction
- __OBJC_$_PROP_LIST_WFConfiguredStaccatoTopHitAction
- __OBJC_$_PROP_LIST_WFConfiguredStaccatoWorkflowAction
- __OBJC_$_PROP_LIST_WFExecutableAutoShortcut
- __OBJC_CLASS_PROTOCOLS_$_WFExecutableAutoShortcut
- __OBJC_CLASS_RO_$_WFExecutableAutoShortcut
- __OBJC_METACLASS_RO_$_WFExecutableAutoShortcut
- ___104+[WFObservableResult drawGlyphsIntoWorkflowsIfNecessary:glyphSize:roundedIcon:synchronously:completion:]_block_invoke.190
- ___104+[WFObservableResult drawGlyphsIntoWorkflowsIfNecessary:glyphSize:roundedIcon:synchronously:completion:]_block_invoke.198
- ___104+[WFObservableResult drawGlyphsIntoWorkflowsIfNecessary:glyphSize:roundedIcon:synchronously:completion:]_block_invoke_2.196
- ___104+[WFObservableResult drawGlyphsIntoWorkflowsIfNecessary:glyphSize:roundedIcon:synchronously:completion:]_block_invoke_2.200
- ___62+[WFIcon(IconicActionSymbol) apertureIconForActionIdentifier:]_block_invoke
- ___BiomeLibraryLibraryCore_block_invoke.16860
- ___BiomeLibraryLibraryCore_block_invoke.2808
- ___BiomeLibraryLibraryCore_block_invoke.6939
- ___Block_byref_object_copy_.1025
- ___Block_byref_object_copy_.10774
- ___Block_byref_object_copy_.12426
- ___Block_byref_object_copy_.13450
- ___Block_byref_object_copy_.1490
- ___Block_byref_object_copy_.15576
- ___Block_byref_object_copy_.17371
- ___Block_byref_object_copy_.2323
- ___Block_byref_object_copy_.4541
- ___Block_byref_object_copy_.4806
- ___Block_byref_object_copy_.8643
- ___Block_byref_object_dispose_.1026
- ___Block_byref_object_dispose_.10775
- ___Block_byref_object_dispose_.12427
- ___Block_byref_object_dispose_.13451
- ___Block_byref_object_dispose_.1491
- ___Block_byref_object_dispose_.15577
- ___Block_byref_object_dispose_.17372
- ___Block_byref_object_dispose_.2324
- ___Block_byref_object_dispose_.4542
- ___Block_byref_object_dispose_.4807
- ___Block_byref_object_dispose_.8644
- ___ContentKitLibraryCore_block_invoke.10941
- ___ContentKitLibraryCore_block_invoke.15566
- ___CoreLocationLibraryCore_block_invoke.7402
- ___CoreTextLibraryCore_block_invoke.10052
- ___FileProviderLibraryCore_block_invoke.10923
- ___IconServicesLibraryCore_block_invoke.13805
- ___ImageIOLibraryCore_block_invoke.4448
- ___ImageIOLibraryCore_block_invoke.7997
- ___LinkServicesLibraryCore_block_invoke.5627
- ___UIKitLibraryCore_block_invoke.16027
- ___UIKitLibrary_block_invoke.4024
- ___UIKitLibrary_block_invoke.7989
- ___UIKitLibrary_block_invoke.9853
- ___VisionKitCoreLibraryCore_block_invoke.12192
- ___block_literal_global.101.12487
- ___block_literal_global.10181
- ___block_literal_global.1048
- ___block_literal_global.107.13159
- ___block_literal_global.11883
- ___block_literal_global.12272
- ___block_literal_global.12449
- ___block_literal_global.12758
- ___block_literal_global.12867
- ___block_literal_global.13214
- ___block_literal_global.133
- ___block_literal_global.13454
- ___block_literal_global.138
- ___block_literal_global.143.12264
- ___block_literal_global.14372
- ___block_literal_global.1467
- ___block_literal_global.148
- ___block_literal_global.14880
- ___block_literal_global.14909
- ___block_literal_global.15553
- ___block_literal_global.15594
- ___block_literal_global.15605
- ___block_literal_global.157
- ___block_literal_global.15841
- ___block_literal_global.16122
- ___block_literal_global.162
- ___block_literal_global.16563
- ___block_literal_global.16573
- ___block_literal_global.167
- ___block_literal_global.16730
- ___block_literal_global.17.4819
- ___block_literal_global.1729
- ___block_literal_global.17516
- ___block_literal_global.177
- ___block_literal_global.178
- ___block_literal_global.179
- ___block_literal_global.184.12235
- ___block_literal_global.189
- ___block_literal_global.193
- ___block_literal_global.195
- ___block_literal_global.201
- ___block_literal_global.207
- ___block_literal_global.216
- ___block_literal_global.222
- ___block_literal_global.228
- ___block_literal_global.234
- ___block_literal_global.240
- ___block_literal_global.2449
- ___block_literal_global.245
- ___block_literal_global.251
- ___block_literal_global.257
- ___block_literal_global.266
- ___block_literal_global.272
- ___block_literal_global.283
- ___block_literal_global.288
- ___block_literal_global.2929
- ___block_literal_global.338
- ___block_literal_global.343
- ___block_literal_global.3509
- ___block_literal_global.373
- ___block_literal_global.3943
- ___block_literal_global.4027
- ___block_literal_global.413
- ___block_literal_global.4191
- ___block_literal_global.4468
- ___block_literal_global.4581
- ___block_literal_global.47.2457
- ___block_literal_global.4722
- ___block_literal_global.4813
- ___block_literal_global.485
- ___block_literal_global.50.13455
- ___block_literal_global.50.14590
- ___block_literal_global.5862
- ___block_literal_global.59.8163
- ___block_literal_global.7155
- ___block_literal_global.7982
- ___block_literal_global.8165
- ___block_literal_global.84
- ___block_literal_global.8473
- ___block_literal_global.86.8199
- ___block_literal_global.8663
- ___block_literal_global.9026
- ___block_literal_global.9577
- ___block_literal_global.9849
- ___getBiomeLibrarySymbolLoc_block_invoke.16850
- ___getBiomeLibrarySymbolLoc_block_invoke.2805
- ___getBiomeLibrarySymbolLoc_block_invoke.6935
- ___getCGImageSourceCopyPropertiesAtIndexSymbolLoc_block_invoke.7969
- ___getCGImageSourceCreateImageAtIndexSymbolLoc_block_invoke.7965
- ___getCGImageSourceCreateWithDataSymbolLoc_block_invoke.7957
- ___getCGImageSourceGetCountSymbolLoc_block_invoke.7961
- ___getCLLocationClass_block_invoke.7400
- ___getFBSOpenApplicationOptionKeyLaunchIntentSymbolLoc_block_invoke
- ___getFPSandboxingURLWrapperClass_block_invoke.10918
- ___getISImageDescriptorClass_block_invoke.13791
- ___getVKCRemoveBackgroundRequestHandlerClass_block_invoke.12190
- ___getWFContentItemClass_block_invoke.15551
- ___getkCGImagePropertyOrientationSymbolLoc_block_invoke.7975
- ___getkISImageDescriptorHomeScreenSymbolLoc_block_invoke.13793
- __unnamed_array_storage.12472
- __unnamed_array_storage.14355
- __unnamed_array_storage.15338
- __unnamed_array_storage.15610
- __unnamed_array_storage.2024
- __unnamed_array_storage.2615
- __unnamed_array_storage.2933
- __unnamed_array_storage.3555
- __unnamed_array_storage.44
- __unnamed_array_storage.4596
- __unnamed_array_storage.50
- __unnamed_array_storage.56
- __unnamed_array_storage.62
- __unnamed_array_storage.68.12461
- __unnamed_array_storage.7159
- __unnamed_array_storage.8538
- __unnamed_array_storage.9069
- __unnamed_array_storage.9623
- _apertureIconForActionIdentifier:.actionIdentifierMapping
- _apertureIconForActionIdentifier:.bundleIdentifierMapping
- _apertureIconForActionIdentifier:.onceToken
- _audit_stringBiomeLibrary.16864
- _audit_stringBiomeLibrary.2811
- _audit_stringBiomeLibrary.6943
- _audit_stringContentKit.10944
- _audit_stringContentKit.15571
- _audit_stringCoreLocation.7417
- _audit_stringCoreText.10056
- _audit_stringFileProvider.10937
- _audit_stringIconServices.13808
- _audit_stringImageIO.4451
- _audit_stringImageIO.8000
- _audit_stringLinkServices.5630
- _audit_stringUIKit.16030
- _audit_stringVisionKitCore.12195
- _capabilities.cachedAnswer.199
- _capabilities.cachedAnswer.205
- _capabilities.cachedAnswer.214
- _capabilities.cachedAnswer.220
- _capabilities.cachedAnswer.226
- _capabilities.cachedAnswer.232
- _capabilities.cachedAnswer.238
- _capabilities.cachedAnswer.249
- _capabilities.cachedAnswer.255
- _capabilities.cachedAnswer.264
- _capabilities.cachedAnswer.270
- _capabilities.onceTokenkMGQInternalBuild
- _classUIImage.7984
- _getBiomeLibrarySymbolLoc.ptr.16849
- _getBiomeLibrarySymbolLoc.ptr.2804
- _getBiomeLibrarySymbolLoc.ptr.6934
- _getCGImageSourceCopyPropertiesAtIndexSymbolLoc.ptr.7968
- _getCGImageSourceCreateImageAtIndexSymbolLoc.ptr.7964
- _getCGImageSourceCreateWithDataSymbolLoc.ptr.7956
- _getCGImageSourceGetCountSymbolLoc.ptr.7960
- _getCLLocationClass.softClass.7399
- _getFBSOpenApplicationOptionKeyLaunchIntentSymbolLoc.ptr
- _getFPSandboxingURLWrapperClass.softClass.10917
- _getISImageDescriptorClass.softClass.13790
- _getUIImageClass.7978
- _getVKCRemoveBackgroundRequestHandlerClass.softClass.12189
- _getWFContentItemClass.softClass.15550
- _getkCGImagePropertyOrientationSymbolLoc.ptr.7974
- _getkISImageDescriptorHomeScreenSymbolLoc.ptr.13792
- _initUIImage.7980
- _objc_msgSend$WiFi
- _objc_msgSend$alarm
- _objc_msgSend$apertureIconForActionIdentifier:
- _objc_msgSend$audiobook
- _objc_msgSend$books
- _objc_msgSend$codeScanner
- _objc_msgSend$iconSymbolName
- _objc_msgSend$initWithAutoShortcut:identifier:phrase:alternativePhrases:bundleIdentifier:actionIdentifier:orderOfShortcut:parentAction:prominentDisplayEligibility:
- _objc_msgSend$initWithAutoShortcut:phrase:entityInfo:
- _objc_msgSend$initWithIdentifier:sectionIdentifier:associatedBundleIdentifier:name:systemImageName:shortcutsMetadata:
- _objc_msgSend$initWithIntent:sectionIdentifier:named:appShortcutIdentifier:systemImageName:templateParameterValues:contextualParameters:shortcutsMetadata:
- _objc_msgSend$initWithLinkStaccatoAction:interactionType:preciseTimeStamp:
- _objc_msgSend$initWithTopHitStaccatoAction:
- _objc_msgSend$initWithWorkflowStaccatoAction:
- _objc_msgSend$isEqualToDictionary:
- _objc_msgSend$keynote
- _objc_msgSend$localAssetForBundleIdentifier:
- _objc_msgSend$numbers
- _objc_msgSend$pages
- _objc_msgSend$remote
- _objc_msgSend$scanDocument
- _objc_msgSend$spotlightDomainIdentifier
- _objc_msgSend$voiceMemos
- _screenBounds.cachedAnswer.131
- _sharedManager.onceToken.8662
- _systemName.cachedAnswer.182
- _timestampDateFormatter.dateFormatter.12868
- _timestampDateFormatter.onceToken.12866
CStrings:
+ "\x02$"
+ "\x06\x13"
+ "%s Device is cellular data capable, indexing toggle"
+ "%s Device is not cellular data capable, not indexing toggle"
+ "%s Indexing App Shortcut with data backed image for %@, this should be investigated"
+ "%s Indexing large App Shortcut image of size %lu for app %@"
+ "%s Unable to get cellular data capability: %@"
+ "-[WFExecutableAppShortcut base64ArchivedData]"
+ "<%@ (%p): id: %@ name: %@, bundle: %@, action: %@, app shortcut identifier: %@>"
+ "<%@ (%p): id: %@ name: %@, bundle: %@, asi: %@, contextual parameters: %@ intent: %@>"
+ "<%@ (%p): id: %@ name: %@, bundle: %@, workflow: %@>"
+ "<%@ (%p): id: %@ name: %@, bundle: %@>"
+ "<%@: %p Error: %@>"
+ "@\"WFConfiguredSystemAction\""
+ "@\"WFContentItem\"24@?0@\"NSString\"8Q16"
+ "@\"WFExecutableAppShortcut\""
+ "@104@0:8@16@24@32@40@48@56@64Q72@80@88@96"
+ "@72@0:8@16@24@32@40@48@56@64"
+ "ActionButton"
+ "AppShortcutInterpolation"
+ "CTError"
+ "CTError WF_CTServerConnectionGetCellularDataIsEnabled(CTServerConnectionRef, Boolean *)"
+ "CTError WF_CTServerConnectionGetCellularDataSettings(CTServerConnectionRef, Boolean *, Boolean *, Boolean *)"
+ "CTErrorDomain"
+ "CTServerConnectionRef WF_CTServerConnectionCreateWithIdentifier(CFAllocatorRef, CFStringRef, CTServerConnectionCallback, _CTServerConnectionContext *)"
+ "Do Not Disturb"
+ "IconicSymbolUtilities"
+ "Loading"
+ "RingerButtonCapability"
+ "Sync"
+ "System Action"
+ "T@\"INAppIntent\",&,N,V_intent"
+ "T@\"NSArray\",&,N,V_contextualParameters"
+ "T@\"NSArray\",R,N,V_alternatePhrases"
+ "T@\"NSData\",C,N,V_shortcutsMetadata"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C,N,V_lnPropertyIdentifier"
+ "T@\"NSString\",R,N,V_parameterlessIdentifier"
+ "T@\"WFConfiguredSystemAction\",&,N,V_action"
+ "T@\"WFExecutableAppShortcut\",R,N,V_executableAppShortcut"
+ "T@\"WFExecutableAppShortcutIdentifier\",&,N,V_appShortcutIdentifier"
+ "T^{__CTServerConnection=},R,N,V_connection"
+ "WFCellularSettings"
+ "WFCellularSettings.m"
+ "WFCellularSettingsErrorDomain"
+ "WFConfiguratorRunRequest"
+ "WFConfiguratorRunRequest.m"
+ "WFConfiguratorRunnerClient"
+ "WFConfiguratorRunnerClient.m"
+ "WFConfiguredActionButtonContextualAction"
+ "WFConfiguredActionButtonIntentAction"
+ "WFConfiguredActionButtonNothingAction"
+ "WFConfiguredActionButtonWorkflowAction"
+ "WFConfiguredSystemAction"
+ "WFConfiguredSystemAction.m"
+ "WFConfiguredSystemContextualAction"
+ "WFConfiguredSystemContextualAction.m"
+ "WFConfiguredSystemIntentAction"
+ "WFConfiguredSystemIntentAction.m"
+ "WFConfiguredSystemNothingAction"
+ "WFConfiguredSystemWorkflowAction"
+ "WFConfiguredSystemWorkflowAction.m"
+ "WFContextualActionIconErrorDomain"
+ "WFExecutableAppShortcut"
+ "WFSystemActionRunnerClient"
+ "WFSystemActionRunnerClient.m"
+ "WFSystemColorTertiarySystemBackground"
+ "WFToggleSettingContextualActions"
+ "WiFiAvailabilityStatus"
+ "^{__CTServerConnection=}"
+ "^{__CTServerConnection=}16@0:8"
+ "_CTServerConnectionCreateWithIdentifier"
+ "_CTServerConnectionGetCellularDataIsEnabled"
+ "_CTServerConnectionGetCellularDataSettings"
+ "_alternatePhrases"
+ "_executableAppShortcut"
+ "_isSystem"
+ "_lnPropertyIdentifier"
+ "_parameterlessIdentifier"
+ "_uri"
+ "accessibility.fill"
+ "alternatePhrases"
+ "app_shortcuts_data_source_v2"
+ "basePhraseTemplates"
+ "cellularDataEnabledWithError:"
+ "coherenceEnabledWithCompletion:"
+ "coherenceMigrationEnabledWithCompletion:"
+ "collectionWithItems:"
+ "com.apple.VoiceShortcuts.library.indexed"
+ "com.apple.WorkflowUI.SystemActionConfigurationExtension"
+ "com_apple_shortcuts_runnable_lnproperty_identifier"
+ "com_apple_shortcuts_runnable_tint_color_name"
+ "defaultContextualActionContext"
+ "defaultSettings"
+ "dictionaryWithObject:forKey:"
+ "executableAppShortcut"
+ "iconWithINImage:displayStyle:completion:"
+ "inImage"
+ "initWithAutoShortcut:identifier:parameterlessIdentifier:phrase:alternativePhrases:bundleIdentifier:actionIdentifier:orderOfShortcut:parentAction:prominentDisplayEligibility:executableAppShortcut:"
+ "initWithAutoShortcut:phrase:alternatePhrases:entityInfo:"
+ "initWithExecutableAppShortcut:index:"
+ "initWithIdentifier:associatedBundleIdentifier:name:previewIcon:shortcutsMetadata:"
+ "initWithInputStrings:presentationMode:"
+ "initWithIntent:named:previewIcon:appShortcutIdentifier:contextualParameters:shortcutsMetadata:"
+ "initWithIntent:named:previewIcon:appShortcutIdentifier:templateParameterValues:contextualParameters:shortcutsMetadata:"
+ "initWithLNPropertyIdentifier:displayStyle:"
+ "initWithSystemAction:"
+ "initWithSystemContextualAction:"
+ "initWithSystemIntentAction:"
+ "initWithSystemNothingAction:"
+ "initWithSystemWorkflowAction:"
+ "initWithWorkflowName:inputStrings:"
+ "isCellularDataCapableWithError:"
+ "isTopHitEligible"
+ "itemWithObject:"
+ "legacySpotlightDomainIdentifier"
+ "lnPropertyIdentifier"
+ "loadLNPropertyImageWithCompletion:"
+ "parameterlessIdentifier"
+ "plus.magnifyingglass"
+ "propertiesForIdentifiers:error:"
+ "retrieveImageDataWithCompletion:"
+ "secondaryLabelColor"
+ "secondarySystemFillColor"
+ "setAppShortcutIdentifier:"
+ "setCoherenceMigrationStatus:completion:"
+ "setContextualParameters:"
+ "setShortcutsMetadata:"
+ "softlink:r:path:/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony"
+ "spotlightActionIdentifier"
+ "symbolIconForActionIdentifier:bundleIdentifier:"
+ "system-action"
+ "tertiarySystemBackgroundColor"
+ "tintColorForBundleIdentifier:"
+ "toprakEngineEnabledWithCompletion:"
+ "useNewDataSource"
+ "usesPreviewIconSymbolOverride"
+ "v24@?0@\"WFContextualActionIcon\"8@\"NSError\"16"
+ "v28@0:8B16@?<v@?@\"NSError\">20"
+ "void *CoreTelephonyLibrary(void)"
+ "workflowName"
- "\x02#"
- "\x06\x11"
- "\a"
- "-[WFExecutableAutoShortcut base64ArchivedData]"
- "<%@ (%p): id: %@ name: %@, bundle: %@, section: %@ action: %@, app shortcut identifier: %@>"
- "<%@ (%p): id: %@ name: %@, bundle: %@, section: %@ asi: %@ template parameters: %@, contextual parameters: %@ intent: %@>"
- "<%@ (%p): id: %@ name: %@, bundle: %@, section: %@ workflow: %@>"
- "<%@ (%p): id: %@ name: %@, bundle: %@, section: %@>"
- "<%@: %p Error: %@"
- "@\"WFConfiguredStaccatoAction\""
- "@88@0:8@16@24@32@40@48@56Q64@72@80"
- "AssociatedLogo"
- "FBSOpenApplicationOptionKeyLaunchIntent"
- "IconicActionSymbol"
- "IconicApertureSymbols"
- "InternalBuild"
- "NSString *getFBSOpenApplicationOptionKeyLaunchIntent(void)"
- "T@\"INAppIntent\",R,N,V_intent"
- "T@\"NSArray\",R,N,V_contextualParameters"
- "T@\"NSData\",R,C,N,V_shortcutsMetadata"
- "T@\"NSString\",C,N,V_sectionIdentifier"
- "T@\"NSString\",C,N,V_systemImageName"
- "T@\"NSString\",R,C,N,V_workflowIdentifier"
- "T@\"WFConfiguredStaccatoAction\",&,N,V_action"
- "WFConfiguredStaccatoAction.m"
- "WFExecutableAutoShortcut"
- "WiFi"
- "_systemImageName"
- "apertureIconForActionIdentifier:"
- "audiobook"
- "bonus_spi_v2"
- "books"
- "circle.slash"
- "codeScanner"
- "com.apple.WorkflowUI.StaccatoConfigurationExtension"
- "initWithAutoShortcut:identifier:phrase:alternativePhrases:bundleIdentifier:actionIdentifier:orderOfShortcut:parentAction:prominentDisplayEligibility:"
- "initWithIntent:named:systemImageName:"
- "initWithIntent:sectionIdentifier:named:appShortcutIdentifier:systemImageName:templateParameterValues:contextualParameters:shortcutsMetadata:"
- "initWithLinkStaccatoAction:interactionType:preciseTimeStamp:"
- "initWithTopHitStaccatoAction:"
- "initWithWorkflowStaccatoAction:"
- "isEqualToDictionary:"
- "keynote"
- "localAssetForBundleIdentifier:"
- "remote"
- "scanDocument"
- "setSectionIdentifier:"
- "setSystemImageName:"
- "spotlightDomainIdentifier"
- "voiceMemos"

```
