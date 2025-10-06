## PosterKit

> `/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit`

```diff

-296.100.0.0.0
-  __TEXT.__text: 0x132764
+302.100.0.0.0
+  __TEXT.__text: 0x132120
   __TEXT.__auth_stubs: 0x2060
-  __TEXT.__objc_methlist: 0x1808c
+  __TEXT.__objc_methlist: 0x1804c
   __TEXT.__const: 0x1e94
-  __TEXT.__cstring: 0x9af8
-  __TEXT.__oslogstring: 0x5cf9
-  __TEXT.__gcc_except_tab: 0x28d8
+  __TEXT.__cstring: 0x9b28
+  __TEXT.__oslogstring: 0x5e69
+  __TEXT.__gcc_except_tab: 0x28a4
   __TEXT.__ustring: 0x1c
   __TEXT.__constg_swiftt: 0x844
   __TEXT.__swift5_typeref: 0x40ae

   __TEXT.__swift5_mpenum: 0x118
   __TEXT.__unwind_info: 0x4e88
   __TEXT.__eh_frame: 0x88
-  __TEXT.__objc_classname: 0x3b8f
-  __TEXT.__objc_methname: 0x3d421
-  __TEXT.__objc_methtype: 0xbad7
-  __TEXT.__objc_stubs: 0x20be0
-  __DATA_CONST.__got: 0x18a0
+  __TEXT.__objc_classname: 0x3b67
+  __TEXT.__objc_methname: 0x3d4dc
+  __TEXT.__objc_methtype: 0xbadb
+  __TEXT.__objc_stubs: 0x20c60
+  __DATA_CONST.__got: 0x18a8
   __DATA_CONST.__const: 0x34a8
-  __DATA_CONST.__objc_classlist: 0xa08
+  __DATA_CONST.__objc_classlist: 0x9f8
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x588
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb520
+  __DATA_CONST.__objc_selrefs: 0xb528
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0x830
+  __DATA_CONST.__objc_superrefs: 0x820
   __DATA_CONST.__objc_arraydata: 0x180
   __AUTH_CONST.__auth_got: 0x1040
   __AUTH_CONST.__const: 0x1db0
-  __AUTH_CONST.__cfstring: 0x9600
-  __AUTH_CONST.__objc_const: 0x4e188
+  __AUTH_CONST.__cfstring: 0x9620
+  __AUTH_CONST.__objc_const: 0x4e0d8
   __AUTH_CONST.__objc_intobj: 0x678
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x36d8
+  __AUTH.__objc_data: 0x3638
   __AUTH.__data: 0x408
-  __DATA.__objc_ivar: 0x1880
+  __DATA.__objc_ivar: 0x1874
   __DATA.__data: 0x4798
-  __DATA.__bss: 0x1370
+  __DATA.__bss: 0x1360
   __DATA.__common: 0x29
   __DATA_DIRTY.__objc_data: 0x2ef8
   __DATA_DIRTY.__data: 0x2b0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1F250320-09DF-37F5-9DFB-725E736A7592
-  Functions: 8424
-  Symbols:   28091
-  CStrings:  13045
+  UUID: 71CB4928-E37B-3CC8-A4E2-51C67F9C1AD8
+  Functions: 8414
+  Symbols:   28064
+  CStrings:  13053
 
Symbols:
+ -[FBSMutableSceneClientSettings(PRScene) pr_setDeviceMotionMode:]
+ -[FBSSceneClientSettings(PRScene) pr_deviceMotionMode]
+ -[FBSSceneClientSettingsDiff(PRScene) pr_deviceMotionModeDidChange]
+ -[PRImmutablePosterTitleStyleConfiguration initWithTimeFontConfiguration:preferredTitleAlignment:preferredTitleLayout:titleContentStyle:titleColor:timeNumberingSystem:userConfigured:preferredTimeMaxYPortrait:preferredTimeMaxYLandscape:contentsLuminance:alternateDateEnabled:groupName:adaptiveTimeHeightUserConfigured:version:]
+ -[PRImmutablePosterTitleStyleConfiguration isAdaptiveTimeHeightUserConfigured]
+ -[PRInlineComplicationGalleryItemCell _updateConstraintsForIconVisibility]
+ -[PRMutablePosterTitleStyleConfiguration initWithTimeFontConfiguration:preferredTitleAlignment:preferredTitleLayout:titleContentStyle:titleColor:timeNumberingSystem:userConfigured:preferredTimeMaxYPortrait:preferredTimeMaxYLandscape:contentsLuminance:alternateDateEnabled:groupName:adaptiveTimeHeightUserConfigured:version:]
+ -[PRMutablePosterTitleStyleConfiguration isAdaptiveTimeHeightUserConfigured]
+ -[PRMutablePosterTitleStyleConfiguration setAdaptiveTimeHeightUserConfigured:]
+ -[PRPosterPreferencesImpl applyToClientSettings:overridePreferredSalientRect:]
+ -[PRPosterPreferencesImpl deviceMotionMode]
+ -[PRPosterPreferencesImpl setDeviceMotionMode:]
+ -[PRPosterTitleStyleConfiguration initWithTimeFontConfiguration:preferredTitleAlignment:preferredTitleLayout:titleContentStyle:titleColor:timeNumberingSystem:userConfigured:preferredTimeMaxYPortrait:preferredTimeMaxYLandscape:contentsLuminance:alternateDateEnabled:groupName:adaptiveTimeHeightUserConfigured:version:]
+ -[PRRenderingServiceClient _sendAcknowledgment]
+ -[PRRenderingServiceClient _sendAcknowledgment].cold.1
+ -[PRRenderingServiceConnection _updateSendingStateBasedOnAcks]
+ -[PRRenderingServiceConnection acknowledgeMotionEvents]
+ -[PRRenderingServiceConnection acknowledgeMotionEvents].cold.1
+ -[PRRenderingServiceConnection sendMotionEvent:].cold.1
+ -[PRRenderingServiceServer acknowledgeMotionEvents]
+ -[PRWidgetGridViewController isEmpty]
+ -[UIWindowScene(PRScene) pr_updatePreferences:withTransition:configuredSalientRect:]
+ -[UIWindowScene(PRScene) pr_updatePreferences:withTransition:configuredSalientRect:].cold.1
+ GCC_except_table31
+ GCC_except_table65
+ GCC_except_table80
+ GCC_except_table89
+ GCC_except_table90
+ _OBJC_CLASS_$_PUIStyleFontWeightSlider
+ _OBJC_CLASS_$_UIListSeparatorConfiguration
+ _OBJC_IVAR_$_PRImmutablePosterTitleStyleConfiguration._adaptiveTimeHeightUserConfigured
+ _OBJC_IVAR_$_PRInlineComplicationGalleryItemCell._horizontalStackView
+ _OBJC_IVAR_$_PRInlineComplicationGalleryItemCell._stackViewConstraints
+ _OBJC_IVAR_$_PRMutablePosterTitleStyleConfiguration._adaptiveTimeHeightUserConfigured
+ _OBJC_IVAR_$_PRPosterPreferencesImpl._deviceMotionMode
+ _OBJC_IVAR_$_PRRenderingServiceClient._motionEventsReceivedSinceLastAck
+ _OBJC_IVAR_$_PRRenderingServiceConnection._lastAckTime
+ _OBJC_IVAR_$_PRRenderingServiceConnection._motionEventsSentSinceLastAck
+ _OBJC_IVAR_$_PRRenderingServiceConnection._shouldStopSending
+ _PRInlineComplicationGalleryItemExpandedVerticalInset
+ _PRInlineComplicationGalleryItemLeadingInset
+ _PRMPosterTitleStyleConfigurationKeyIsAdaptiveTimeHeightUserConfigured
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PRRenderingServiceClientToServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PRRenderingServiceClientToServerInterface
+ ___122-[PREditor _performActionsForUIScene:withUpdatedFBSScene:settingsDiff:fromSettings:transitionContext:lifecycleActionType:]_block_invoke.407
+ ___124-[PRRenderer _performActionsForUIScene:withUpdatedFBSScene:settingsDiff:fromSettings:transitionContext:lifecycleActionType:]_block_invoke.121
+ ___124-[PRRenderer _performActionsForUIScene:withUpdatedFBSScene:settingsDiff:fromSettings:transitionContext:lifecycleActionType:]_block_invoke_2.113
+ ___124-[PRRenderer _performActionsForUIScene:withUpdatedFBSScene:settingsDiff:fromSettings:transitionContext:lifecycleActionType:]_block_invoke_2.122
+ ___40-[PRRenderer _updateRenderingExtensions]_block_invoke.218
+ ___40-[PRRenderer _updateRenderingExtensions]_block_invoke.219
+ ___40-[PRRenderer _updateRenderingExtensions]_block_invoke.224
+ ___40-[PRRenderer _updateRenderingExtensions]_block_invoke.225
+ ___40-[PRRenderer _updateRenderingExtensions]_block_invoke.226
+ ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke.371
+ ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke.384
+ ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke.384.cold.1
+ ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke.389
+ ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke_2.383
+ ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke_2.383.cold.1
+ ___51-[PRRenderingServiceServer acknowledgeMotionEvents]_block_invoke
+ ___62-[PRRenderer _updateBacklightLuminanceFrom:to:animateChanges:]_block_invoke.130
+ ___70-[PRRenderingServiceServer listener:didReceiveConnection:withContext:]_block_invoke.80
+ ___71+[FBScene(PRScene) _pr_createPosterSceneWithRole:path:processIdentity:]_block_invoke.434
+ ___84-[UIWindowScene(PRScene) pr_updatePreferences:withTransition:configuredSalientRect:]_block_invoke
+ ___block_descriptor_32_e70_v24?0"<PRMutablePosterRenderingPreferences>"8"PRPosterTransition"16l
+ ___block_descriptor_96_e8_32s40s48s56s_e69_v24?0"FBSMutableSceneClientSettings"8"FBSSceneTransitionContext"16ls32l8s40l8s48l8s56l8
+ ___block_literal_global.112
+ ___block_literal_global.256
+ ___block_literal_global.316
+ ___block_literal_global.340
+ ___block_literal_global.367
+ ___block_literal_global.369
+ ___block_literal_global.374
+ ___block_literal_global.409
+ ___block_literal_global.418
+ ___block_literal_global.433
+ ___block_literal_global.437
+ ___block_literal_global.440
+ _objc_msgSend$_sendAcknowledgment
+ _objc_msgSend$_setLargeBackground:
+ _objc_msgSend$_setNonLargeBackground:
+ _objc_msgSend$_updateConstraintsForIconVisibility
+ _objc_msgSend$_updateSendingStateBasedOnAcks
+ _objc_msgSend$acknowledgeMotionEvents
+ _objc_msgSend$applyToClientSettings:overridePreferredSalientRect:
+ _objc_msgSend$currentContext
+ _objc_msgSend$initWithListAppearance:
+ _objc_msgSend$initWithTimeFontConfiguration:preferredTitleAlignment:preferredTitleLayout:titleContentStyle:titleColor:timeNumberingSystem:userConfigured:preferredTimeMaxYPortrait:preferredTimeMaxYLandscape:contentsLuminance:alternateDateEnabled:groupName:adaptiveTimeHeightUserConfigured:version:
+ _objc_msgSend$initWithVariant:size:
+ _objc_msgSend$listCellConfiguration
+ _objc_msgSend$pr_setDeviceMotionMode:
+ _objc_msgSend$pr_updatePreferences:withTransition:configuredSalientRect:
+ _objc_msgSend$pui_isAdaptiveTimeHeightUserConfigured
+ _objc_msgSend$pui_setAdaptiveTimeHeightUserConfigured:
+ _objc_msgSend$setClientMessagingExpectation:
+ _objc_msgSend$setSeparatorConfiguration:
+ _objc_msgSend$setSubvariant:
+ _objc_msgSend$setUserInterfaceStyle:
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$updatePreferences:
- -[PREditingFontAndColorPickerViewController _closeButtonTapped:]
- -[PREditingFontAndContentStylePickerViewController _closeButtonTapped:]
- -[PREditingFontAndContentStylePickerViewController closeButton]
- -[PREditingFontAndContentStylePickerViewController closeSystemBarButtonItem]
- -[PREditingFontAndContentStylePickerViewController setCloseButton:]
- -[PREditingFontAndContentStylePickerViewController setCloseSystemBarButtonItem:]
- -[PRFontWeightSlider .cxx_destruct]
- -[PRFontWeightSlider _createCustomThumbView]
- -[PRFontWeightSlider contentBackgroundColor]
- -[PRFontWeightSlider createThumbView]
- -[PRFontWeightSlider dealloc]
- -[PRFontWeightSlider init]
- -[PRFontWeightSlider layoutSubviews]
- -[PRFontWeightSlider setContentBackgroundColor:]
- -[PRFontWeightSlider setThumbBorderLayer:]
- -[PRFontWeightSlider setThumbClippingLayer:]
- -[PRFontWeightSlider setThumbContentLayer:]
- -[PRFontWeightSlider setThumbSoftShadowLayer:]
- -[PRFontWeightSlider setThumbView:]
- -[PRFontWeightSlider setUserInterfaceStyleTraitChangeRegistration:]
- -[PRFontWeightSlider thumbBorderLayer]
- -[PRFontWeightSlider thumbClippingLayer]
- -[PRFontWeightSlider thumbContentLayer]
- -[PRFontWeightSlider thumbRectForBounds:trackRect:value:]
- -[PRFontWeightSlider thumbSoftShadowLayer]
- -[PRFontWeightSlider thumbView]
- -[PRFontWeightSlider trackRectForBounds:]
- -[PRFontWeightSlider userInterfaceStyleTraitChangeRegistration]
- -[PRPosterPreferencesImpl applyToClientSettings:topComplicationsConfigured:]
- -[UIWindowScene(PRScene) pr_updatePreferences:withTransition:].cold.1
- -[_PRFontWeightSliderTrackView .cxx_destruct]
- -[_PRFontWeightSliderTrackView drawRect:]
- -[_PRFontWeightSliderTrackView initWithTrackBackgroundColor:]
- -[_PRFontWeightSliderTrackView trackBackgroundColor]
- GCC_except_table29
- GCC_except_table32
- GCC_except_table51
- GCC_except_table64
- GCC_except_table79
- GCC_except_table85
- GCC_except_table86
- GCC_except_table96
- _OBJC_CLASS_$_PRFontWeightSlider
- _OBJC_CLASS_$__PRFontWeightSliderTrackView
- _OBJC_IVAR_$_PREditingFontAndContentStylePickerViewController._closeButton
- _OBJC_IVAR_$_PREditingFontAndContentStylePickerViewController._closeSystemBarButtonItem
- _OBJC_IVAR_$_PRFontWeightSlider._contentBackgroundColor
- _OBJC_IVAR_$_PRFontWeightSlider._thumbBorderLayer
- _OBJC_IVAR_$_PRFontWeightSlider._thumbClippingLayer
- _OBJC_IVAR_$_PRFontWeightSlider._thumbContentLayer
- _OBJC_IVAR_$_PRFontWeightSlider._thumbSoftShadowLayer
- _OBJC_IVAR_$_PRFontWeightSlider._thumbView
- _OBJC_IVAR_$_PRFontWeightSlider._trackView
- _OBJC_IVAR_$_PRFontWeightSlider._userInterfaceStyleTraitChangeRegistration
- _OBJC_IVAR_$_PRInlineComplicationGalleryItemCell._leadingConstraint
- _OBJC_IVAR_$__PRFontWeightSliderTrackView._trackBackgroundColor
- _OBJC_METACLASS_$_PRFontWeightSlider
- _OBJC_METACLASS_$_UISlider
- _OBJC_METACLASS_$__PRFontWeightSliderTrackView
- _PRInlineComplicationGalleryItemExpandedHorizontalInset
- __OBJC_$_INSTANCE_METHODS_PRFontWeightSlider
- __OBJC_$_INSTANCE_METHODS__PRFontWeightSliderTrackView
- __OBJC_$_INSTANCE_VARIABLES_PRFontWeightSlider
- __OBJC_$_INSTANCE_VARIABLES__PRFontWeightSliderTrackView
- __OBJC_$_PROP_LIST_PRFontWeightSlider
- __OBJC_$_PROP_LIST__PRFontWeightSliderTrackView
- __OBJC_CLASS_RO_$_PRFontWeightSlider
- __OBJC_CLASS_RO_$__PRFontWeightSliderTrackView
- __OBJC_METACLASS_RO_$_PRFontWeightSlider
- __OBJC_METACLASS_RO_$__PRFontWeightSliderTrackView
- ___122-[PREditor _performActionsForUIScene:withUpdatedFBSScene:settingsDiff:fromSettings:transitionContext:lifecycleActionType:]_block_invoke.399
- ___124-[PRRenderer _performActionsForUIScene:withUpdatedFBSScene:settingsDiff:fromSettings:transitionContext:lifecycleActionType:]_block_invoke.117
- ___124-[PRRenderer _performActionsForUIScene:withUpdatedFBSScene:settingsDiff:fromSettings:transitionContext:lifecycleActionType:]_block_invoke_2.118
- ___26-[PRFontWeightSlider init]_block_invoke
- ___26-[PRFontWeightSlider init]_block_invoke_2
- ___40-[PRRenderer _updateRenderingExtensions]_block_invoke.214
- ___40-[PRRenderer _updateRenderingExtensions]_block_invoke.215
- ___40-[PRRenderer _updateRenderingExtensions]_block_invoke.220
- ___40-[PRRenderer _updateRenderingExtensions]_block_invoke.221
- ___40-[PRRenderer _updateRenderingExtensions]_block_invoke.222
- ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke.367
- ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke.380
- ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke.380.cold.1
- ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke.385
- ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke_2.379
- ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke_2.379.cold.1
- ___62-[PRRenderer _updateBacklightLuminanceFrom:to:animateChanges:]_block_invoke.126
- ___62-[UIWindowScene(PRScene) pr_updatePreferences:withTransition:]_block_invoke
- ___70-[PRRenderingServiceServer listener:didReceiveConnection:withContext:]_block_invoke.69
- ___71+[FBScene(PRScene) _pr_createPosterSceneWithRole:path:processIdentity:]_block_invoke.428
- ___block_descriptor_32_e36_"UIColor"16?0"UITraitCollection"8l
- ___block_descriptor_64_e8_32s40s48s56s_e69_v24?0"FBSMutableSceneClientSettings"8"FBSSceneTransitionContext"16ls32l8s40l8s48l8s56l8
- ___block_literal_global.252
- ___block_literal_global.312
- ___block_literal_global.336
- ___block_literal_global.363
- ___block_literal_global.365
- ___block_literal_global.370
- ___block_literal_global.382
- ___block_literal_global.405
- ___block_literal_global.414
- ___block_literal_global.429
- ___block_literal_global.456
- ___block_literal_global.459
- _objc_msgSend$_createCustomThumbView
- _objc_msgSend$addArcWithCenter:radius:startAngle:endAngle:clockwise:
- _objc_msgSend$addLineToPoint:
- _objc_msgSend$applyToClientSettings:topComplicationsConfigured:
- _objc_msgSend$contentBackgroundColor
- _objc_msgSend$fill
- _objc_msgSend$initWithDynamicProvider:
- _objc_msgSend$initWithTrackBackgroundColor:
- _objc_msgSend$listGroupedCellConfiguration
- _objc_msgSend$moveToPoint:
- _objc_msgSend$resolvedColorWithTraitCollection:
- _objc_msgSend$setMaximumTrackTintColor:
- _objc_msgSend$setMinimumTrackTintColor:
- _objc_msgSend$setPreferredCornerRadius:
- _objc_msgSend$systemGray4Color
- _objc_msgSend$thumbContentLayer
- _objc_msgSend$trackBackgroundColor
- _objc_msgSend$trackRectForBounds:
CStrings:
+ "@116@0:8@16Q24Q32@40@48@56B64d68d76d84B92@96B104Q108"
+ "Device motion active assertion is invalidated"
+ "PRRenderingServiceClient: Sent motion events ack, pid: %d"
+ "PRRenderingServiceConnection: connection <%p> pid: %i dropping motion event - no acks received"
+ "PRRenderingServiceConnection: connection <%p> pid: %i received ack"
+ "PRRenderingServiceConnection: connection <%p> pid: %i sent motion event (since last ack: %lu)"
+ "TB,R,D,N,GisAdaptiveTimeHeightUserConfigured"
+ "TQ,N,Spr_setDeviceMotionMode:"
+ "_deviceMotionMode"
+ "_horizontalStackView"
+ "_lastAckTime"
+ "_motionEventsReceivedSinceLastAck"
+ "_motionEventsSentSinceLastAck"
+ "_sendAcknowledgment"
+ "_setLargeBackground:"
+ "_setNonLargeBackground:"
+ "_shouldStopSending"
+ "_stackViewConstraints"
+ "_updateConstraintsForIconVisibility"
+ "_updateSendingStateBasedOnAcks"
+ "acknowledgeMotionEvents"
+ "applyToClientSettings:overridePreferredSalientRect:"
+ "currentContext"
+ "customizeSheet"
+ "deviceMotionMode"
+ "initWithListAppearance:"
+ "initWithTimeFontConfiguration:preferredTitleAlignment:preferredTitleLayout:titleContentStyle:titleColor:timeNumberingSystem:userConfigured:preferredTimeMaxYPortrait:preferredTimeMaxYLandscape:contentsLuminance:alternateDateEnabled:groupName:adaptiveTimeHeightUserConfigured:version:"
+ "initWithVariant:size:"
+ "listCellConfiguration"
+ "pr_deviceMotionMode"
+ "pr_deviceMotionModeDidChange"
+ "pr_setDeviceMotionMode:"
+ "pr_updatePreferences:withTransition:configuredSalientRect:"
+ "pui_isAdaptiveTimeHeightUserConfigured"
+ "pui_setAdaptiveTimeHeightUserConfigured:"
+ "setClientMessagingExpectation:"
+ "setDeviceMotionMode:"
+ "setSeparatorConfiguration:"
+ "setSubvariant:"
+ "setUserInterfaceStyle:"
+ "timeIntervalSinceDate:"
+ "v24@?0@\"<PRMutablePosterRenderingPreferences>\"8@\"PRPosterTransition\"16"
+ "v56@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24"
+ "v64@0:8@16@24{CGRect={CGPoint=dd}{CGSize=dd}}32"
- "@\"UIColor\"16@?0@\"UITraitCollection\"8"
- "@\"_PRFontWeightSliderTrackView\""
- "PRFontWeightSlider"
- "T@\"<UITraitChangeRegistration>\",&,N,V_userInterfaceStyleTraitChangeRegistration"
- "T@\"UIBarButtonItem\",&,N,V_closeSystemBarButtonItem"
- "T@\"UIColor\",&,N,V_contentBackgroundColor"
- "T@\"UIColor\",R,N,V_trackBackgroundColor"
- "T@\"UIImageView\",&,N,V_thumbView"
- "_PRFontWeightSliderTrackView"
- "_closeSystemBarButtonItem"
- "_contentBackgroundColor"
- "_createCustomThumbView"
- "_leadingConstraint"
- "_trackBackgroundColor"
- "addArcWithCenter:radius:startAngle:endAngle:clockwise:"
- "addLineToPoint:"
- "applyToClientSettings:topComplicationsConfigured:"
- "closeSystemBarButtonItem"
- "contentBackgroundColor"
- "drawRect:"
- "fill"
- "initWithDynamicProvider:"
- "initWithTrackBackgroundColor:"
- "listGroupedCellConfiguration"
- "moveToPoint:"
- "resolvedColorWithTraitCollection:"
- "setCloseSystemBarButtonItem:"
- "setContentBackgroundColor:"
- "setMaximumTrackTintColor:"
- "setMinimumTrackTintColor:"
- "setPreferredCornerRadius:"
- "setUserInterfaceStyleTraitChangeRegistration:"
- "systemGray4Color"
- "thumbRectForBounds:trackRect:value:"
- "trackBackgroundColor"
- "trackRectForBounds:"
- "userInterfaceStyleTraitChangeRegistration"
- "{CGRect={CGPoint=dd}{CGSize=dd}}84@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48f80"

```
