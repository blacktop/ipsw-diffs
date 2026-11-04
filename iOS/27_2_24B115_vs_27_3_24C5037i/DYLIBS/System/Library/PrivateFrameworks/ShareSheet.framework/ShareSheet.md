## ShareSheet

> `/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet`

```diff

-2131.21.31.2.5
-  __TEXT.__text: 0xc48f8
-  __TEXT.__objc_methlist: 0x11434
-  __TEXT.__const: 0x620
-  __TEXT.__gcc_except_tab: 0x20c4
-  __TEXT.__oslogstring: 0x72aa
-  __TEXT.__cstring: 0x72be
+2131.30.43.2.1
+  __TEXT.__text: 0xc5db8
+  __TEXT.__objc_methlist: 0x1154c
+  __TEXT.__const: 0x630
+  __TEXT.__gcc_except_tab: 0x2120
+  __TEXT.__oslogstring: 0x74ae
+  __TEXT.__cstring: 0x73fc
   __TEXT.__dlopen_cstrs: 0xb96
-  __TEXT.__ustring: 0x1f4
-  __TEXT.__unwind_info: 0x4158
+  __TEXT.__ustring: 0x20a
+  __TEXT.__unwind_info: 0x41b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2918
+  __DATA_CONST.__const: 0x2960
   __DATA_CONST.__objc_classlist: 0x638
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x3a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8d00
+  __DATA_CONST.__objc_selrefs: 0x8d80
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x678
-  __DATA_CONST.__got: 0xfe0
+  __DATA_CONST.__got: 0xfe8
   __AUTH_CONST.__const: 0x1120
-  __AUTH_CONST.__cfstring: 0x5a80
-  __AUTH_CONST.__objc_const: 0x2a558
+  __AUTH_CONST.__cfstring: 0x5b20
+  __AUTH_CONST.__objc_const: 0x2a658
   __AUTH_CONST.__objc_arrayobj: 0x510
   __AUTH_CONST.__objc_dictobj: 0x730
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x2dc8
   __AUTH.__data: 0x1a0
-  __DATA.__objc_ivar: 0x14b8
+  __DATA.__objc_ivar: 0x14c0
   __DATA.__data: 0x2be9
   __DATA_DIRTY.__objc_data: 0x1068
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5934
-  Symbols:   10308
-  CStrings:  1623
+  Functions: 5962
+  Symbols:   10337
+  CStrings:  1640
 
Symbols:
+ -[ObjectManipulationViewController preferredVerticalBarBehavior]
+ -[SHSheetInteractor showRequestAccessAlertForActivityType:shareSupportsRequestAccess:optionsIncludeAccessRequestsOption:requiresScreeningDisclosure:completionHandler:]
+ -[SHSheetPresenter _serviceActivityUUIDForActivity:]
+ -[SHSheetPresenter _stopPulsingActivity:]
+ -[SHSheetPresenter interactor:showRequestAccessAlertForActivityType:shareSupportsRequestAccess:optionsIncludeAccessRequestsOption:requiresScreeningDisclosure:completionHandler:]
+ -[SHSheetRemoteSceneViewController startPulsingActivityWithUUID:localizedTitle:]
+ -[SHSheetRemoteSceneViewController stopPulsingActivityWithUUID:]
+ -[SHSheetSceneViewController startPulsingActivityWithUUID:localizedTitle:]
+ -[SHSheetSceneViewController stopPulsingActivityWithUUID:]
+ -[UIActivityContentViewController _itemIdentifierForActivityUUID:]
+ -[UIActivityContentViewController _pulsingPeopleIdentifierForTileIdentifier:activityType:]
+ -[UIActivityContentViewController _startPulsingItemWithIdentifier:activityUUID:localizedTitle:]
+ -[UIActivityContentViewController _startPulsingPeopleCell:node:localizedTitle:]
+ -[UIActivityContentViewController preferredVerticalBarBehavior]
+ -[UIActivityContentViewController pulsingActivityUUID]
+ -[UIActivityContentViewController pulsingPeopleIdentifier]
+ -[UIActivityContentViewController setPulsingActivityUUID:]
+ -[UIActivityContentViewController setPulsingPeopleIdentifier:]
+ -[UIActivityContentViewController startPulsingActivityWithUUID:localizedTitle:]
+ -[UIActivityContentViewController stopPulsingActivityWithUUID:]
+ -[UIActivityViewController _preferredContentSizeForModalPresentationStyle:]
+ -[UIActivityViewController horizontalTraitChangeRegistration]
+ -[UIActivityViewController preferredVerticalBarBehavior]
+ -[UIActivityViewController setHorizontalTraitChangeRegistration:]
+ -[_UIActivityUserDefaultsViewController preferredVerticalBarBehavior]
+ GCC_except_table111
+ GCC_except_table126
+ GCC_except_table136
+ GCC_except_table139
+ GCC_except_table141
+ GCC_except_table77
+ GCC_except_table86
+ _OBJC_CLASS_$_UITraitHorizontalSizeClass
+ _OBJC_IVAR_$_UIActivityContentViewController._pulsingActivityUUID
+ _OBJC_IVAR_$_UIActivityContentViewController._pulsingPeopleIdentifier
+ _OBJC_IVAR_$_UIActivityViewController._horizontalTraitChangeRegistration
+ _SFDeviceIsIPhoneDuoDevice
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SHSheetContentView
+ ___177-[SHSheetPresenter interactor:showRequestAccessAlertForActivityType:shareSupportsRequestAccess:optionsIncludeAccessRequestsOption:requiresScreeningDisclosure:completionHandler:]_block_invoke
+ ___177-[SHSheetPresenter interactor:showRequestAccessAlertForActivityType:shareSupportsRequestAccess:optionsIncludeAccessRequestsOption:requiresScreeningDisclosure:completionHandler:]_block_invoke_2
+ ___177-[SHSheetPresenter interactor:showRequestAccessAlertForActivityType:shareSupportsRequestAccess:optionsIncludeAccessRequestsOption:requiresScreeningDisclosure:completionHandler:]_block_invoke_3
+ ___177-[SHSheetPresenter interactor:showRequestAccessAlertForActivityType:shareSupportsRequestAccess:optionsIncludeAccessRequestsOption:requiresScreeningDisclosure:completionHandler:]_block_invoke_4
+ ___177-[SHSheetPresenter interactor:showRequestAccessAlertForActivityType:shareSupportsRequestAccess:optionsIncludeAccessRequestsOption:requiresScreeningDisclosure:completionHandler:]_block_invoke_5
+ ___44-[UIActivityViewController viewIsAppearing:]_block_invoke
+ ___block_descriptor_34_e54_"NSString"32?0"NSString"8"NSString"16"NSString"24l
+ ___block_descriptor_40_e8_32w_e52_v24?0"<UITraitEnvironment>"8"UITraitCollection"16lw32l8
- -[SHSheetInteractor showRequestAccessAlertForActivityType:shareSupportsRequestAccess:optionsIncludeAccessRequestsOption:completionHandler:]
- -[SHSheetPresenter interactor:showRequestAccessAlertForActivityType:shareSupportsRequestAccess:optionsIncludeAccessRequestsOption:completionHandler:]
- -[UIActivityContentViewController pulsingActivity]
- -[UIActivityContentViewController setPulsingActivity:]
- GCC_except_table104
- GCC_except_table119
- GCC_except_table129
- GCC_except_table132
- GCC_except_table138
- GCC_except_table51
- GCC_except_table75
- GCC_except_table84
- _OBJC_IVAR_$_UIActivityContentViewController._pulsingActivity
- ___149-[SHSheetPresenter interactor:showRequestAccessAlertForActivityType:shareSupportsRequestAccess:optionsIncludeAccessRequestsOption:completionHandler:]_block_invoke
- ___149-[SHSheetPresenter interactor:showRequestAccessAlertForActivityType:shareSupportsRequestAccess:optionsIncludeAccessRequestsOption:completionHandler:]_block_invoke_2
- ___149-[SHSheetPresenter interactor:showRequestAccessAlertForActivityType:shareSupportsRequestAccess:optionsIncludeAccessRequestsOption:completionHandler:]_block_invoke_3
- ___149-[SHSheetPresenter interactor:showRequestAccessAlertForActivityType:shareSupportsRequestAccess:optionsIncludeAccessRequestsOption:completionHandler:]_block_invoke_4
CStrings:
+ "%@: no eligible file URL in resolved items, cannot show sharing UI"
+ "@\"NSString\"32@?0@\"NSString\"8@\"NSString\"16@\"NSString\"24"
+ "Ignoring AirDrop while performing activity:%@"
+ "Ignoring activity:%@ while creating collaboration for activity:%@"
+ "Item at index %{public}d has a copy representation; loading original URL inline"
+ "No item to pulse for activity UUID:%@"
+ "No item to pulse for activity:%@"
+ "Not pulsing slotted person item:%@"
+ "PREPARING_TEXT"
+ "Preparing…"
+ "Pulsing extension activity:%@ by service UUID:%@"
+ "Pulsing tapped person item:%@ instead of activity tile:%@"
+ "SHARE_LINK_ACCESS_REQUESTS_ALREADY_ON_MESSAGE_SCREENING_DISCLOSURE"
+ "SHARE_LINK_ACCESS_REQUESTS_OFF_MESSAGE_SCREENING_DISCLOSURE"
+ "SHARE_LINK_ACCESS_REQUESTS_UNSUPPORTED_MESSAGE_SCREENING_DISCLOSURE"
+ "start pulsing activity UUID:%@ item:%@"
+ "stop pulsing activity UUID:%@"
+ "v24@?0@\"<UITraitEnvironment>\"8@\"UITraitCollection\"16"
+ "\xf0\xf0cA"
- "stop pulsing activity:%@"
- "\xf0\xf0SA"
```
