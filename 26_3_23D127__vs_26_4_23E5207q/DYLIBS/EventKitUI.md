## EventKitUI

> `/System/Library/Frameworks/EventKitUI.framework/EventKitUI`

```diff

-1529.2.3.0.0
-  __TEXT.__text: 0x1dcc4c
-  __TEXT.__auth_stubs: 0x2250
-  __TEXT.__objc_methlist: 0x1f1ec
-  __TEXT.__const: 0x2894
-  __TEXT.__cstring: 0xdd81
-  __TEXT.__gcc_except_tab: 0x434c
-  __TEXT.__oslogstring: 0x793d
+1529.4.11.0.0
+  __TEXT.__text: 0x1f3c80
+  __TEXT.__auth_stubs: 0x2330
+  __TEXT.__objc_methlist: 0x1f2dc
+  __TEXT.__const: 0x2864
+  __TEXT.__cstring: 0xcbb6
+  __TEXT.__gcc_except_tab: 0x3ea4
+  __TEXT.__oslogstring: 0x79ad
   __TEXT.__ustring: 0x862
   __TEXT.__dlopen_cstrs: 0x322
-  __TEXT.__swift5_typeref: 0xd4e
-  __TEXT.__swift5_capture: 0x4a8
+  __TEXT.__swift5_typeref: 0xde0
+  __TEXT.__swift5_capture: 0x4b8
+  __TEXT.__constg_swiftt: 0x18f4
   __TEXT.__swift5_reflstr: 0x145d
   __TEXT.__swift5_assocty: 0x248
-  __TEXT.__constg_swiftt: 0x1870
   __TEXT.__swift5_fieldmd: 0xc58
   __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_proto: 0xe4
+  __TEXT.__swift5_proto: 0xe8
   __TEXT.__swift5_types: 0xf8
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0x77d8
-  __TEXT.__eh_frame: 0x5d0
-  __TEXT.__objc_classname: 0x427b
-  __TEXT.__objc_methname: 0x45935
-  __TEXT.__objc_methtype: 0xc36f
-  __TEXT.__objc_stubs: 0x320c0
-  __DATA_CONST.__got: 0x1970
-  __DATA_CONST.__const: 0x4778
-  __DATA_CONST.__objc_classlist: 0xc60
+  __TEXT.__unwind_info: 0x8100
+  __TEXT.__eh_frame: 0x5a4
+  __TEXT.__objc_classname: 0x47ca
+  __TEXT.__objc_methname: 0x468ab
+  __TEXT.__objc_methtype: 0xc50b
+  __TEXT.__objc_stubs: 0x328e0
+  __DATA_CONST.__got: 0x1990
+  __DATA_CONST.__const: 0x4780
+  __DATA_CONST.__objc_classlist: 0xc68
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x628
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf6d8
+  __DATA_CONST.__objc_selrefs: 0xf730
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x8b8
   __DATA_CONST.__objc_arraydata: 0x1c0
-  __AUTH_CONST.__auth_got: 0x1138
+  __AUTH_CONST.__auth_got: 0x11a8
   __AUTH_CONST.__const: 0x2808
-  __AUTH_CONST.__cfstring: 0xb3a0
-  __AUTH_CONST.__objc_const: 0x30790
+  __AUTH_CONST.__cfstring: 0xb3e0
+  __AUTH_CONST.__objc_const: 0x30920
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x7be8
-  __AUTH.__data: 0xbc0
-  __DATA.__objc_ivar: 0x2548
-  __DATA.__data: 0x4bc0
-  __DATA.__bss: 0x1640
+  __AUTH.__objc_data: 0x7c38
+  __AUTH.__data: 0xbb8
+  __DATA.__objc_ivar: 0x2558
+  __DATA.__data: 0x4bf8
+  __DATA.__bss: 0x16e8
   __DATA.__common: 0x218
   __DATA_DIRTY.__objc_data: 0x13b0
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D9E7D335-70D6-3D5E-9896-CBADD1259580
-  Functions: 11810
-  Symbols:   35031
-  CStrings:  16493
+  UUID: 01DBF7A3-B133-354C-B062-B75878064C7A
+  Functions: 11845
+  Symbols:   35198
+  CStrings:  16470
 
Symbols:
+ +[EKEventURLRichDetailItem titleForCell]
+ +[EKEventURLRichDetailItem titleForExtendedViewController]
+ +[EKEventURLTextDetailItem _SGSuggestionsServiceClass]
+ +[EKEventURLTextDetailItem titleForCell]
+ +[EKEventURLTextDetailItem titleForExtendedViewController]
+ -[EKEventDetailConferenceCell _normalizedEventURL]
+ -[EKEventDetailConferenceCell cachedNormalizedEventURL]
+ -[EKEventDetailConferenceCell setCachedNormalizedEventURL:]
+ -[EKEventURLAndNotesInlineEditItem _editItemForIndex:]
+ -[EKEventURLInlineEditItem numberOfSubitems]
+ -[EKEventURLRichDetailItem .cxx_destruct]
+ -[EKEventURLRichDetailItem _createEventDetailCell]
+ -[EKEventURLRichDetailItem cellForSubitemAtIndex:]
+ -[EKEventURLRichDetailItem conferenceCell:requestPresentShareSheetWithActivityItems:withPopoverSourceView:]
+ -[EKEventURLRichDetailItem conferenceCellShouldPresentShareSheet:]
+ -[EKEventURLRichDetailItem conferenceCellUpdated:]
+ -[EKEventURLRichDetailItem configureWithEvent:calendar:preview:]
+ -[EKEventURLRichDetailItem owningViewController]
+ -[EKEventURLRichDetailItem reset]
+ -[EKEventURLRichDetailItem section]
+ -[EKEventURLRichDetailItem textForCopyAction]
+ -[EKEventURLRichDetailItem textForExtendedViewController]
+ -[EKEventURLTextDetailItem .cxx_destruct]
+ -[EKEventURLTextDetailItem _createEventDetailCell]
+ -[EKEventURLTextDetailItem attributedTextFromEventBlock]
+ -[EKEventURLTextDetailItem configureWithEvent:calendar:preview:]
+ -[EKEventURLTextDetailItem linkWithLaunchInfo]
+ -[EKEventURLTextDetailItem linkWithURL]
+ -[EKEventURLTextDetailItem reset]
+ -[EKEventURLTextDetailItem textForCopyAction]
+ -[EKEventURLTextDetailItem textForExtendedViewController]
+ -[EKEventURLTextDetailItem textView:primaryActionForTextItem:defaultAction:]
+ _CUIKTruncateAttributedStringForAvailableSpace
+ _CUIKTruncateStringForAvailableSpace
+ _EKUIEventDetailsContext_AppIntentTriggered
+ _OBJC_CLASS_$_CUIKEventActionHandler
+ _OBJC_CLASS_$_EKEventURLRichDetailItem
+ _OBJC_CLASS_$_EKEventURLTextDetailItem
+ _OBJC_IVAR_$_EKEventDetailConferenceCell._cachedNormalizedEventURL
+ _OBJC_IVAR_$_EKEventDetailTextCell._forceTruncation
+ _OBJC_IVAR_$_EKEventURLRichDetailItem._cell
+ _OBJC_IVAR_$_EKEventURLRichDetailItem._normalizedURL
+ _OBJC_IVAR_$_EKEventURLTextDetailItem._cell
+ _OBJC_IVAR_$_EKEventURLTextDetailItem._launchInfo
+ _OBJC_IVAR_$_EKEventURLTextDetailItem._url
+ _OBJC_METACLASS_$_EKEventURLRichDetailItem
+ _OBJC_METACLASS_$_EKEventURLTextDetailItem
+ _OUTLINED_FUNCTION_2
+ __MergedGlobals
+ __OBJC_$_CLASS_METHODS_EKEventURLRichDetailItem
+ __OBJC_$_CLASS_METHODS_EKEventURLTextDetailItem
+ __OBJC_$_INSTANCE_METHODS_EKEventURLRichDetailItem
+ __OBJC_$_INSTANCE_METHODS_EKEventURLTextDetailItem
+ __OBJC_$_INSTANCE_VARIABLES_EKEventURLRichDetailItem
+ __OBJC_$_INSTANCE_VARIABLES_EKEventURLTextDetailItem
+ __OBJC_$_PROP_LIST_EKEventURLRichDetailItem
+ __OBJC_$_PROP_LIST_EKEventURLTextDetailItem
+ __OBJC_CLASS_PROTOCOLS_$_EKEventURLRichDetailItem
+ __OBJC_CLASS_PROTOCOLS_$_EKEventURLTextDetailItem
+ __OBJC_CLASS_RO_$_EKEventURLRichDetailItem
+ __OBJC_CLASS_RO_$_EKEventURLTextDetailItem
+ __OBJC_METACLASS_RO_$_EKEventURLRichDetailItem
+ __OBJC_METACLASS_RO_$_EKEventURLTextDetailItem
+ __PROTOCOLS__TtCV10EventKitUI26_AppExtensionEventHostView15HostCoordinator.83
+ __PROTOCOLS__TtCV10EventKitUI30_AppExtensionEventEditHostView15HostCoordinator.70
+ __PROTOCOLS__TtCV10EventKitUI36_AppExtensionCalendarChooserHostView15HostCoordinator.52
+ __PROTOCOLS__TtCV10EventKitUI39_AppExtensionEventGenericDetailHostView15HostCoordinator.67
+ ___35-[EKCalendarEditor _deleteCalendar]_block_invoke.62
+ ___37-[EKEventDetailConferenceCell update]_block_invoke_5
+ ___37-[EKEventDetailConferenceCell update]_block_invoke_6
+ ___41+[EKUIContextMenuActions _allActionInfos]_block_invoke.464
+ ___41+[EKUIContextMenuActions _allActionInfos]_block_invoke_2.467
+ ___41+[EKUIContextMenuActions _allActionInfos]_block_invoke_3.479
+ ___41+[EKUIContextMenuActions _allActionInfos]_block_invoke_4.481
+ ___56-[EKEventURLTextDetailItem attributedTextFromEventBlock]_block_invoke
+ ___64-[EKEventURLTextDetailItem configureWithEvent:calendar:preview:]_block_invoke
+ ___64-[EKEventURLTextDetailItem configureWithEvent:calendar:preview:]_block_invoke_2
+ ___76-[EKEventURLTextDetailItem textView:primaryActionForTextItem:defaultAction:]_block_invoke
+ ___76-[EKEventURLTextDetailItem textView:primaryActionForTextItem:defaultAction:]_block_invoke.43
+ ___76-[EKEventURLTextDetailItem textView:primaryActionForTextItem:defaultAction:]_block_invoke_2
+ ___76-[EKEventURLTextDetailItem textView:primaryActionForTextItem:defaultAction:]_block_invoke_2.45
+ ___block_literal_global.466
+ ___block_literal_global.469
+ ___block_literal_global.491
+ ___block_literal_global.535
+ ___isPlatformVersionAtLeast
+ ___isPlatformVersionAtLeast.cold.1
+ ___isPlatformVersionAtLeast.cold.2
+ __availability_version_check
+ __initializeAvailabilityCheck
+ _block_copy_helper.23
+ _block_copy_helper.29
+ _block_copy_helper.35
+ _block_copy_helper.38
+ _block_copy_helper.41
+ _block_copy_helper.44
+ _block_copy_helper.50
+ _block_copy_helper.53
+ _block_copy_helper.56
+ _block_copy_helper.59
+ _block_copy_helper.60
+ _block_copy_helper.66
+ _block_copy_helper.72
+ _block_copy_helper.80
+ _block_copy_helper.93
+ _block_descriptor.25
+ _block_descriptor.31
+ _block_descriptor.37
+ _block_descriptor.40
+ _block_descriptor.43
+ _block_descriptor.46
+ _block_descriptor.52
+ _block_descriptor.55
+ _block_descriptor.58
+ _block_descriptor.61
+ _block_descriptor.62
+ _block_descriptor.68
+ _block_descriptor.74
+ _block_descriptor.82
+ _block_descriptor.95
+ _block_destroy_helper.24
+ _block_destroy_helper.30
+ _block_destroy_helper.36
+ _block_destroy_helper.39
+ _block_destroy_helper.42
+ _block_destroy_helper.45
+ _block_destroy_helper.51
+ _block_destroy_helper.54
+ _block_destroy_helper.57
+ _block_destroy_helper.60
+ _block_destroy_helper.61
+ _block_destroy_helper.67
+ _block_destroy_helper.73
+ _block_destroy_helper.81
+ _block_destroy_helper.94
+ _compatibilityInitializeAvailabilityCheck
+ _dispatch_once_f
+ _dlsym
+ _fclose
+ _fopen
+ _fread
+ _fseek
+ _ftell
+ _get_underlying_type_ref 7SwiftUI4ViewPAAEAcAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOQr.14
+ _get_underlying_witness 7SwiftUI4ViewPAAEAcAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOqd__AaBHC.15
+ _get_witness_table 7SwiftUI19_ConditionalContentVyAA4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOyAA08ModifiedD0Vy08EventKitB0013_AppExtensionl4HostE0VAA30_SafeAreaRegionsIgnoringLayoutVG_Qo_AA6VStackVyAA4TextVGGAaDHPqd__AaDHD2_ATHO_AyaDHPyHCHC.85
+ _get_witness_table qd__7SwiftUI4ViewHD2_AaBPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOyAA15ModifiedContentVy08EventKitB0013_AppExtensionk8EditHostC0VAA30_SafeAreaRegionsIgnoringLayoutVG_Qo_HO.73
+ _get_witness_table qd__7SwiftUI4ViewHD2_AaBPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOyAA15ModifiedContentVy08EventKitB0032_AppExtensionCalendarChooserHostC0VAA30_SafeAreaRegionsIgnoringLayoutVG_Qo_HO.55
+ _get_witness_table qd__7SwiftUI4ViewHD2_AaBPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOyAA15ModifiedContentVyAKy08EventKitB0013_AppExtensionk17GenericDetailHostC0VAA24_BackgroundStyleModifierVyAA5ColorVGGAA30_SafeAreaRegionsIgnoringLayoutVG_Qo_HO.70
+ _initializeAvailabilityCheck
+ _objc_msgSend$CGSizeValue
+ _objc_msgSend$_normalizedEventURL
+ _objc_msgSend$cachedNormalizedEventURL
+ _objc_msgSend$calendarInEventStore:
+ _objc_msgSend$classesForSelector:argumentIndex:ofReply:
+ _objc_msgSend$connection
+ _objc_msgSend$deletedObjectIDs
+ _objc_msgSend$displayDetailsForURL:isEventURL:completionHandler:
+ _objc_msgSend$effectiveUserIdentifier
+ _objc_msgSend$ekui_affineTransform
+ _objc_msgSend$eventEditViewController:didCompleteWithAction:waitUntil:
+ _objc_msgSend$eventViewEventEditViewCompletedWithAction:eventID:waitUntilTimestamp:
+ _objc_msgSend$eventViewEventEditViewPresented:
+ _objc_msgSend$eventViewNavigationDoneButtonTapped
+ _objc_msgSend$genericViewBottomStatusButtonTapped:
+ _objc_msgSend$genericViewLeftBarButtonTapped:
+ _objc_msgSend$genericViewRightBarButtonTapped:
+ _objc_msgSend$handleCalendarDeletion:reportJunk:
+ _objc_msgSend$handleEventDeletion:span:
+ _objc_msgSend$handleEventUpdate:span:
+ _objc_msgSend$handleOpenCalendarEditor:
+ _objc_msgSend$handleOpenEventDetails:
+ _objc_msgSend$handleOpenEventEditor:
+ _objc_msgSend$initWithData:
+ _objc_msgSend$initWithTitle:viewID:leftBarButtonActions:rightBarButtonActions:
+ _objc_msgSend$initWithUnsignedInt:
+ _objc_msgSend$initializationOptions
+ _objc_msgSend$insertedObjectIDs
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$isLegacyEKUIClient
+ _objc_msgSend$isReadable
+ _objc_msgSend$isSubscribedCalendarJunk
+ _objc_msgSend$isTemporary
+ _objc_msgSend$largeDetent
+ _objc_msgSend$makeXPCConnectionWithError:
+ _objc_msgSend$management
+ _objc_msgSend$managementBundleIdentifier
+ _objc_msgSend$mimicSaveAndCommitEvent:oldToNewObjectIDMap:insertedObjectIDs:updatedObjectIDs:deletedObjectIDs:
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$redactedMimicSaveEvent:oldToNewObjectIDMap:serializedDictionary:objectIDToChangeSetDictionaryMap:objectIDToPersistentDictionaryMap:
+ _objc_msgSend$remoteCalendarChooserSelectionChanged:allSelected:
+ _objc_msgSend$remoteObjectProxy
+ _objc_msgSend$respondsToSelector:
+ _objc_msgSend$resume
+ _objc_msgSend$rightBarButtonActions
+ _objc_msgSend$setCachedNormalizedEventURL:
+ _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setDetents:
+ _objc_msgSend$setExportedInterface:
+ _objc_msgSend$setExportedObject:
+ _objc_msgSend$setInsetsLayoutMarginsFromSafeArea:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$setupEventEditViewWithSerializedEventDictionary:objectIDToChangeSetDictionaryMap:objectIDToPersistentDictionaryMap:eventOccurrenceDate:
+ _objc_msgSend$setupEventViewContextWithNavBarExistence:
+ _objc_msgSend$setupEventViewWithSerializedEventDictionary:objectIDToChangeSetDictionaryMap:objectIDToPersistentDictionaryMap:eventOccurrenceDate:
+ _objc_msgSend$setupGenericViewContextWithViewID:
+ _objc_msgSend$setupViewContextWithViewHierarchy:layoutDirection:sizeCategory:sourceAccountManagement:sourceBundleID:
+ _objc_msgSend$setupViewContextWithViewHierarchy:layoutDirection:sizeCategory:sourceAccountManagement:sourceBundleID:isLegacyClient:
+ _objc_msgSend$updateCalendarChooserViewWithChangedViewConfigurationDictionary:
+ _objc_msgSend$updateEventEditViewWithChangedViewConfigurationDictionary:
+ _objc_msgSend$updateEventViewWithChangedViewConfigurationDictionary:
+ _objc_msgSend$updatedObjectIDs
+ _objc_msgSend$waitUntilDatabaseUpdatedToTimestamp:completion:
+ _objectdestroy.45Tm
+ _rewind
+ _swift_unknownObjectRelease_n
+ _symbolic ScA_pSg
+ _symbolic _____yAAyAAy__________y_____GG_____G_____G 7SwiftUI15ModifiedContentV 08EventKitB0013_AppExtensionE21GenericDetailHostViewV AA24_BackgroundStyleModifierV AA5ColorV AA30_SafeAreaRegionsIgnoringLayoutV AA14_TaskModifier2V
+ _symbolic _____yAAy__________G_____G 7SwiftUI15ModifiedContentV 08EventKitB0013_AppExtensionE12EditHostViewV AA30_SafeAreaRegionsIgnoringLayoutV AA14_TaskModifier2V
+ _symbolic _____yAAy__________G_____G 7SwiftUI15ModifiedContentV 08EventKitB0013_AppExtensionE8HostViewV AA30_SafeAreaRegionsIgnoringLayoutV AA14_TaskModifier2V
+ _symbolic _____yAAy__________G_____G 7SwiftUI15ModifiedContentV 08EventKitB036_AppExtensionCalendarChooserHostViewV AA30_SafeAreaRegionsIgnoringLayoutV AA14_TaskModifier2V
+ _symbolic _____y_____yAAy__________y_____GG_____G_Qo_ 7SwiftUI4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AA15ModifiedContentV 08EventKitB0013_AppExtensionk17GenericDetailHostC0V AA24_BackgroundStyleModifierV AA5ColorV AA30_SafeAreaRegionsIgnoringLayoutV
+ _symbolic _____y_____y__________G_Qo_ 7SwiftUI4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AA15ModifiedContentV 08EventKitB0013_AppExtensionk4HostC0V AA30_SafeAreaRegionsIgnoringLayoutV
+ _symbolic _____y_____y__________G_Qo_ 7SwiftUI4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AA15ModifiedContentV 08EventKitB0013_AppExtensionk8EditHostC0V AA30_SafeAreaRegionsIgnoringLayoutV
+ _symbolic _____y_____y__________G_Qo_ 7SwiftUI4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AA15ModifiedContentV 08EventKitB0032_AppExtensionCalendarChooserHostC0V AA30_SafeAreaRegionsIgnoringLayoutV
+ _symbolic _____y_____y_____y__________G_Qo______y_____GG 7SwiftUI19_ConditionalContentV AA4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AA08ModifiedD0V 08EventKitB0013_AppExtensionl4HostE0V AA30_SafeAreaRegionsIgnoringLayoutV AA6VStackV AA4TextV
+ _symbolic _____y_____y_____y__________G_Qo______y_____G_G 7SwiftUI19_ConditionalContentV7StorageO AA4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AA08ModifiedD0V 08EventKitB0013_AppExtensionm4HostF0V AA30_SafeAreaRegionsIgnoringLayoutV AA6VStackV AA4TextV
+ _symbolic qd__
- +[EKEventURLDetailItem _SGSuggestionsServiceClass]
- +[EKEventURLDetailItem titleForCell]
- +[EKEventURLDetailItem titleForExtendedViewController]
- -[EKEventURLDetailItem .cxx_destruct]
- -[EKEventURLDetailItem _createEventDetailCell]
- -[EKEventURLDetailItem attributedTextFromEventBlock]
- -[EKEventURLDetailItem configureWithEvent:calendar:preview:]
- -[EKEventURLDetailItem linkWithLaunchInfo]
- -[EKEventURLDetailItem linkWithURL]
- -[EKEventURLDetailItem reset]
- -[EKEventURLDetailItem textForCopyAction]
- -[EKEventURLDetailItem textForExtendedViewController]
- -[EKEventURLDetailItem textView:primaryActionForTextItem:defaultAction:]
- _OBJC_CLASS_$_EKEventURLDetailItem
- _OBJC_IVAR_$_EKEventURLDetailItem._cell
- _OBJC_IVAR_$_EKEventURLDetailItem._launchInfo
- _OBJC_IVAR_$_EKEventURLDetailItem._url
- _OBJC_METACLASS_$_EKEventURLDetailItem
- __OBJC_$_CLASS_METHODS_EKEventURLDetailItem
- __OBJC_$_INSTANCE_METHODS_EKEventURLDetailItem
- __OBJC_$_INSTANCE_VARIABLES_EKEventURLDetailItem
- __OBJC_$_PROP_LIST_EKEventURLDetailItem
- __OBJC_CLASS_PROTOCOLS_$_EKEventURLDetailItem
- __OBJC_CLASS_RO_$_EKEventURLDetailItem
- __OBJC_METACLASS_RO_$_EKEventURLDetailItem
- __PROTOCOLS__TtCV10EventKitUI26_AppExtensionEventHostView15HostCoordinator.78
- __PROTOCOLS__TtCV10EventKitUI30_AppExtensionEventEditHostView15HostCoordinator.68
- __PROTOCOLS__TtCV10EventKitUI36_AppExtensionCalendarChooserHostView15HostCoordinator.50
- __PROTOCOLS__TtCV10EventKitUI39_AppExtensionEventGenericDetailHostView15HostCoordinator.65
- ___35-[EKCalendarEditor _deleteCalendar]_block_invoke.60
- ___41+[EKUIContextMenuActions _allActionInfos]_block_invoke.463
- ___41+[EKUIContextMenuActions _allActionInfos]_block_invoke_2.466
- ___41+[EKUIContextMenuActions _allActionInfos]_block_invoke_3.478
- ___41+[EKUIContextMenuActions _allActionInfos]_block_invoke_4.480
- ___52-[EKEventURLDetailItem attributedTextFromEventBlock]_block_invoke
- ___60-[EKEventURLDetailItem configureWithEvent:calendar:preview:]_block_invoke
- ___60-[EKEventURLDetailItem configureWithEvent:calendar:preview:]_block_invoke_2
- ___72-[EKEventURLDetailItem textView:primaryActionForTextItem:defaultAction:]_block_invoke
- ___72-[EKEventURLDetailItem textView:primaryActionForTextItem:defaultAction:]_block_invoke.43
- ___72-[EKEventURLDetailItem textView:primaryActionForTextItem:defaultAction:]_block_invoke_2
- ___72-[EKEventURLDetailItem textView:primaryActionForTextItem:defaultAction:]_block_invoke_2.45
- ___block_literal_global.468
- ___block_literal_global.490
- ___block_literal_global.534
- _block_copy_helper.21
- _block_copy_helper.27
- _block_copy_helper.33
- _block_copy_helper.36
- _block_copy_helper.39
- _block_copy_helper.42
- _block_copy_helper.48
- _block_copy_helper.51
- _block_copy_helper.54
- _block_copy_helper.55
- _block_copy_helper.57
- _block_copy_helper.61
- _block_copy_helper.67
- _block_copy_helper.77
- _block_copy_helper.88
- _block_descriptor.23
- _block_descriptor.29
- _block_descriptor.35
- _block_descriptor.38
- _block_descriptor.41
- _block_descriptor.44
- _block_descriptor.50
- _block_descriptor.53
- _block_descriptor.56
- _block_descriptor.57
- _block_descriptor.59
- _block_descriptor.63
- _block_descriptor.69
- _block_descriptor.79
- _block_descriptor.90
- _block_destroy_helper.22
- _block_destroy_helper.28
- _block_destroy_helper.34
- _block_destroy_helper.37
- _block_destroy_helper.40
- _block_destroy_helper.43
- _block_destroy_helper.49
- _block_destroy_helper.52
- _block_destroy_helper.55
- _block_destroy_helper.56
- _block_destroy_helper.58
- _block_destroy_helper.62
- _block_destroy_helper.68
- _block_destroy_helper.78
- _block_destroy_helper.89
- _get_witness_table 7SwiftUI15ModifiedContentVyACy08EventKitB0013_AppExtensionE12EditHostViewVAA30_SafeAreaRegionsIgnoringLayoutVGAA13_TaskModifierVGAA0K0HPAiaMHPAfaMHPyHC_AhA0kR0HPyHCHC_AkaNHPyHCHC.70
- _get_witness_table 7SwiftUI15ModifiedContentVyACy08EventKitB036_AppExtensionCalendarChooserHostViewVAA30_SafeAreaRegionsIgnoringLayoutVGAA13_TaskModifierVGAA0L0HPAiaMHPAfaMHPyHC_AhA0lS0HPyHCHC_AkaNHPyHCHC.52
- _get_witness_table 7SwiftUI15ModifiedContentVyACyACy08EventKitB0013_AppExtensionE21GenericDetailHostViewVAA24_BackgroundStyleModifierVyAA5ColorVGGAA30_SafeAreaRegionsIgnoringLayoutVGAA05_TaskO0VGAA0L0HPAoaSHPAlaSHPAfaSHPyHC_AkA0lO0HPyHCHC_AnaTHPyHCHC_AqaTHPyHCHC.67
- _get_witness_table 7SwiftUI19_ConditionalContentVyAA08ModifiedD0VyAEy08EventKitB0013_AppExtensionF8HostViewVAA30_SafeAreaRegionsIgnoringLayoutVGAA13_TaskModifierVGAA6VStackVyAA4TextVGGAA0K0HPAnaUHPAkaUHPAhaUHPyHC_AjA0kR0HPyHCHC_AmaVHPyHCHC_AsaUHPyHCHC.80
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x10
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objectdestroy.40Tm
- _symbolic _____yAAyAAy__________y_____GG_____G_____G 7SwiftUI15ModifiedContentV 08EventKitB0013_AppExtensionE21GenericDetailHostViewV AA24_BackgroundStyleModifierV AA5ColorV AA30_SafeAreaRegionsIgnoringLayoutV AA05_TaskO0V
- _symbolic _____yAAy__________G_____G 7SwiftUI15ModifiedContentV 08EventKitB0013_AppExtensionE12EditHostViewV AA30_SafeAreaRegionsIgnoringLayoutV AA13_TaskModifierV
- _symbolic _____yAAy__________G_____G 7SwiftUI15ModifiedContentV 08EventKitB0013_AppExtensionE8HostViewV AA30_SafeAreaRegionsIgnoringLayoutV AA13_TaskModifierV
- _symbolic _____yAAy__________G_____G 7SwiftUI15ModifiedContentV 08EventKitB036_AppExtensionCalendarChooserHostViewV AA30_SafeAreaRegionsIgnoringLayoutV AA13_TaskModifierV
- _symbolic _____y_____G s23_ContiguousArrayStorageC 7SwiftUI4EdgeO3SetV
- _symbolic _____y_____yABy__________G_____G_____y_____GG 7SwiftUI19_ConditionalContentV AA08ModifiedD0V 08EventKitB0013_AppExtensionF8HostViewV AA30_SafeAreaRegionsIgnoringLayoutV AA13_TaskModifierV AA6VStackV AA4TextV
- _symbolic _____y_____yABy__________G_____G_____y_____G_G 7SwiftUI19_ConditionalContentV7StorageO AA08ModifiedD0V 08EventKitB0013_AppExtensionG8HostViewV AA30_SafeAreaRegionsIgnoringLayoutV AA13_TaskModifierV AA6VStackV AA4TextV
CStrings:
+ "%d.%d.%d"
+ "/System/Library/CoreServices/SystemVersion.plist"
+ "CFDataCreateWithBytesNoCopy"
+ "CFDictionaryGetValue"
+ "CFGetTypeID"
+ "CFPropertyListCreateFromXMLData"
+ "CFPropertyListCreateWithData"
+ "CFRelease"
+ "CFStringCreateWithCStringNoCopy"
+ "CFStringGetCString"
+ "CFStringGetTypeID"
+ "EKEventURLRichDetailItem"
+ "EKEventURLTextDetailItem"
+ "EKUIEventDetailsContext_AppIntentTriggered"
+ "No URL available to share in conference cell. Virtual conference: %@, conference URL: %@, event URL: %@"
+ "ProductVersion"
+ "T@\"NSURL\",&,N,V_cachedNormalizedEventURL"
+ "View.task @ EventKitUI/EKCalendarChooserOOPHostView.swift:"
+ "View.task @ EventKitUI/EKEventEditOOPHostView.swift:"
+ "View.task @ EventKitUI/EKEventGenericDetailOOPHostView.swift:"
+ "View.task @ EventKitUI/EKEventOOPHostView.swift:"
+ "_cachedNormalizedEventURL"
+ "_forceTruncation"
+ "_normalizedEventURL"
+ "_normalizedURL"
+ "cachedNormalizedEventURL"
+ "displayDetailsForURL:isEventURL:completionHandler:"
+ "event-details-url-rich-cell"
+ "event-details-url-text-cell"
+ "handleCalendarDeletion:reportJunk:"
+ "handleEventDeletion:span:"
+ "handleEventUpdate:span:"
+ "handleOpenCalendarEditor:"
+ "handleOpenEventDetails:"
+ "handleOpenEventEditor:"
+ "isSubscribedCalendarJunk"
+ "kCFAllocatorNull"
+ "setCachedNormalizedEventURL:"
- "EKEventURLDetailItem"
- "event-details-url-cell"

```
