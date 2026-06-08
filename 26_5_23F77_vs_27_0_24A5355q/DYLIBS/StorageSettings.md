## StorageSettings

> `/System/Library/PrivateFrameworks/StorageSettings.framework/StorageSettings`

```diff

-156.0.0.0.0
-  __TEXT.__text: 0x83f8
-  __TEXT.__auth_stubs: 0x450
+157.0.0.0.0
+  __TEXT.__text: 0x80d0
   __TEXT.__objc_methlist: 0x790
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0xadb
+  __TEXT.__cstring: 0xaea
   __TEXT.__ustring: 0x4
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__unwind_info: 0x268
-  __TEXT.__objc_classname: 0xfa
-  __TEXT.__objc_methname: 0x18e6
-  __TEXT.__objc_methtype: 0x24b
-  __TEXT.__objc_stubs: 0x1960
-  __DATA_CONST.__got: 0x280
+  __TEXT.__unwind_info: 0x278
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x258
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x848
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x238
+  __DATA_CONST.__got: 0x280
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0xd60
   __AUTH_CONST.__objc_const: 0x1200
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0xfc
   __DATA.__data: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6F026F58-CB08-3F03-93D6-1E589E44FA72
+  UUID: D14ABB40-6019-3927-957A-8F99808C8FB6
   Functions: 196
   Symbols:   949
-  CStrings:  610
+  CStrings:  219
 
Symbols:
+ ___block_literal_global.42
+ ___block_literal_global.71
+ ___block_literal_global.89
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x4
- ___block_literal_global.2
- ___block_literal_global.29
- ___block_literal_global.47
- _objc_release_x28
- _objc_retain_x23
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x27
Functions:
~ -[STStorageProgressView updateColors] : 260 -> 220
~ -[STStorageProgressView initWithFrame:] : 124 -> 120
~ -[STStorageProgressView percent] : 16 -> 20
~ -[STStorageProgressView setPercent:] : 32 -> 36
~ _STStorageDeviceKey : 84 -> 68
~ -[STStorageTableCell initWithStyle:reuseIdentifier:specifier:] : 1888 -> 1880
~ -[STStorageTableCell setupTitleAndInfoConstraints] : 908 -> 888
~ -[STStorageTableCell createNormalFontConstraints] : 900 -> 872
~ -[STStorageTableCell createLargeFontConstraints] : 1024 -> 988
~ -[STStorageTableCell updateConstraints] : 908 -> 940
~ -[STStorageTableCell setIcon:] : 16 -> 20
~ -[STStorageTableCell icon] : 16 -> 20
~ -[STStorageTableCell title] : 16 -> 20
~ -[STStorageTableCell info] : 16 -> 20
~ -[STStorageTableCell infoHidden] : 16 -> 20
~ -[STStorageTableCell setInfoHidden:] : 68 -> 72
~ -[STStorageTableCell setSizeString:] : 332 -> 324
~ -[STStorageTableCell sizeString] : 100 -> 88
~ -[STStorageTableCell size] : 16 -> 20
~ -[STStorageTableCell setEnabled:] : 92 -> 96
~ -[STStorageTableCell cloudIconHidden] : 16 -> 20
~ -[STStoragePlugin setIdentifier:] : 64 -> 12
~ -[STStoragePlugin identifier] : 136 -> 132
~ -[STStoragePlugin setTips:] : 64 -> 12
~ -[STStoragePlugin tips] : 72 -> 24
~ -[STStoragePlugin notifyUsageChanged] : 80 -> 76
~ -[STStoragePlugin reloadTips] : 100 -> 96
~ -[STStoragePlugin reloadSpecifiersForApp:] : 192 -> 184
~ _STColorForCategoryKey : 148 -> 140
~ ___STColorForCategoryKey_block_invoke : 508 -> 472
~ _STColorForCategory : 84 -> 76
~ -[STStorageTip init] : 184 -> 180
~ -[STStorageTip propertyForKey:] : 112 -> 108
~ -[STStorageTip setSize:] : 108 -> 104
~ -[STStorageTip size] : 72 -> 68
~ -[STStorageTip _reload:] : 288 -> 272
~ -[STStorageOptionTip init] : 220 -> 216
~ -[STStorageOptionTip enableOption] : 124 -> 120
~ -[STStorageOptionTip setValue:specifier:] : 552 -> 508
~ -[STStorageOptionTip setActivationPercent:] : 156 -> 152
~ -[STStorageOptionTip activationPercent] : 80 -> 76
~ -[STStorageOptionTip immediateGain] : 100 -> 92
~ -[STStorageOptionTip setImmediateGain:] : 108 -> 104
~ -[STStorageOptionTip eventualGain] : 72 -> 68
~ -[STStorageOptionTip setEventualGain:] : 108 -> 104
~ -[STStorageOptionTip mayCauseDataLoss] : 20 -> 24
~ -[STStorageOptionTip setMayCauseDataLoss:] : 16 -> 20
~ +[STStorageAppCell specifierForStorageApp:] : 188 -> 184
~ +[STStorageAppCell specifierForChildApp:] : 272 -> 264
~ +[STStorageAppCell specifierForAppIdentifier:] : 132 -> 128
~ +[STStorageAppCell specifierForAppBundleURL:] : 136 -> 124
~ +[STStorageAppCell specifierForAppProxy:] : 104 -> 96
~ -[STStorageAppCell initWithStyle:reuseIdentifier:specifier:] : 248 -> 240
~ -[STStorageAppCell refreshCellContentsWithSpecifier:] : 804 -> 768
~ ___53-[STStorageAppCell refreshCellContentsWithSpecifier:]_block_invoke_2 : 244 -> 236
~ ___LastUsedFormatString_block_invoke : 68 -> 64
~ _STLoadHeaderIconForAppID : 104 -> 100
~ __STLoadHeaderIconForAppID : 364 -> 356
~ _AppIsClip : 112 -> 108
~ _STLoadHeaderIconForApp : 136 -> 132
~ _STLoadTableIconForAppID : 104 -> 100
~ __STLoadTableIconForAppID : 300 -> 296
~ _STLoadTableIconForApp : 136 -> 132
~ ____STLoadHeaderIconForAppID_block_invoke : 68 -> 64
~ __CachedIconForAppID : 160 -> 152
~ _getIconLoaderQueue : 84 -> 68
~ __LoadIconForAppID : 1196 -> 1156
~ ____STLoadHeaderIconForAppID_block_invoke_3 : 148 -> 144
~ ____STLoadTableIconForAppID_block_invoke : 68 -> 64
~ ____STLoadTableIconForAppID_block_invoke_3 : 148 -> 144
~ +[STStorageItemCell specifierForItemURL:] : 188 -> 184
~ -[STStorageItemCell refreshCellContentsWithSpecifier:] : 620 -> 600
~ ___54-[STStorageItemCell refreshCellContentsWithSpecifier:]_block_invoke : 192 -> 204
~ ___54-[STStorageItemCell refreshCellContentsWithSpecifier:]_block_invoke_2 : 120 -> 112
~ ___54-[STStorageItemCell refreshCellContentsWithSpecifier:]_block_invoke_3 : 444 -> 464
~ _STFrameworkLocStr : 116 -> 108
~ __FrameworkBundle : 84 -> 68
~ _STFrameworkImage : 124 -> 116
~ ____FrameworkBundle_block_invoke : 76 -> 72
~ +[STStorageAppHeaderCell specifierForStorageApp:] : 188 -> 184
~ +[STStorageAppHeaderCell specifierForAppIdentifier:] : 132 -> 128
~ +[STStorageAppHeaderCell specifierForAppProxy:] : 104 -> 96
~ +[STStorageAppHeaderCell specifierForAppBundleURL:] : 136 -> 124
~ -[STStorageAppHeaderCell refreshCellContentsWithSpecifier:] : 672 -> 648
~ -[STStorageAppHeaderCell setIcon:] : 16 -> 20
~ -[STStorageAppHeaderCell icon] : 16 -> 20
~ -[STStorageAppHeaderCell setTitle:] : 108 -> 104
~ -[STStorageAppHeaderCell title] : 100 -> 88
~ -[STStorageAppHeaderCell setVendor:] : 16 -> 20
~ -[STStorageAppHeaderCell vendor] : 100 -> 88
~ -[STStorageAppHeaderCell setInfo:] : 16 -> 20
~ -[STStorageAppHeaderCell info] : 100 -> 88
~ -[STStorageAppHeaderCell infoHidden] : 16 -> 20
~ -[STStorageAppHeaderCell setInfoHidden:] : 16 -> 20
~ -[PSSpecifier(STStorageAppHeaderCell) versionLabelEnabled] : 88 -> 84
~ -[STStorageActionTip init] : 216 -> 212
~ -[STStorageActionTip setDetailControllerClass:] : 84 -> 80
~ -[STStorageActionTip detailControllerClass] : 84 -> 76
~ -[STStorageTipCell initWithStyle:reuseIdentifier:specifier:] : 1536 -> 1528
~ -[STStorageTipCell updateConstraints] : 2256 -> 2252
~ -[STStorageTipCell refreshCellContentsWithSpecifier:] : 1384 -> 1392
~ ___53-[STStorageTipCell refreshCellContentsWithSpecifier:]_block_invoke : 24 -> 28
~ -[STStorageTipCell _activateOption] : 116 -> 108
~ -[STStorageTipInfoCell initWithStyle:reuseIdentifier:specifier:] : 472 -> 460
~ -[STStorageTipInfoCell updateConstraints] : 328 -> 320
~ -[STStorageTipInfoCell refreshCellContentsWithSpecifier:] : 520 -> 492
CStrings:
+ "HomeButtonType"
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSLayoutConstraint\""
- "@\"NSMutableArray\""
- "@\"NSObject<STStorageOptionTipDelegate>\""
- "@\"NSObject<STStorageTipUIDelegate>\""
- "@\"NSString\""
- "@\"PSSpecifier\""
- "@\"STStorageProgressView\""
- "@\"UIActivityIndicatorView\""
- "@\"UIButton\""
- "@\"UIColor\""
- "@\"UIImageView\""
- "@\"UILabel\""
- "@\"UIView\""
- "@16@0:8"
- "@24@0:8@16"
- "@40@0:8q16@24@32"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "B"
- "B16@0:8"
- "JwLB44/jEB8aFDpXQ16Tuw"
- "STStorageActionTip"
- "STStorageActionTipItem"
- "STStorageAppCell"
- "STStorageAppHeaderCell"
- "STStorageItemCell"
- "STStorageOptionTip"
- "STStoragePlugin"
- "STStorageProgressView"
- "STStorageTableCell"
- "STStorageTip"
- "STStorageTipCell"
- "STStorageTipInfoCell"
- "T#"
- "T@\"NSArray\",&"
- "T@\"NSArray\",C,V_significantItems"
- "T@\"NSDate\",&,V_createdDate"
- "T@\"NSDate\",&,V_lastUsedDate"
- "T@\"NSObject<STStorageOptionTipDelegate>\",W,V_delegate"
- "T@\"NSObject<STStorageTipUIDelegate>\",W,V_uiDelegate"
- "T@\"NSString\",&"
- "T@\"NSString\",&,V_additionalButtonTitle"
- "T@\"NSString\",&,V_confirmationButtonTitle"
- "T@\"NSString\",&,V_confirmationText"
- "T@\"NSString\",&,V_identifier"
- "T@\"PSSpecifier\",&,V_specifier"
- "T@\"PSSpecifier\",R,V_infoSpecifier"
- "T@\"UIActivityIndicatorView\",&,V_spinner"
- "T@\"UIImage\",&"
- "TB"
- "TB,GisRecoverable,V_recoverable"
- "TB,V_mayCauseDataLoss"
- "Td"
- "Tf"
- "Tq"
- "Tq,V_size"
- "UIImage"
- "URLByDeletingPathExtension"
- "_activateOption"
- "_additionalButtonTitle"
- "_appIconView"
- "_blueColor"
- "_checkIconView"
- "_cloudIconColor"
- "_cloudIconConstraint"
- "_cloudIconView"
- "_confirmationButtonTitle"
- "_confirmationText"
- "_constraints"
- "_createdDate"
- "_delegate"
- "_enableButton"
- "_enableWidth"
- "_grayColor"
- "_h2format"
- "_hformat"
- "_iconSizeConstraint"
- "_iconView"
- "_identifier"
- "_infoConstraints"
- "_infoHidden"
- "_infoSpecifier"
- "_isDemoted"
- "_isOption"
- "_largeFontConstraints"
- "_lastUsedDate"
- "_mayCauseDataLoss"
- "_minHeightConstraint"
- "_nativeSpinnerWidth"
- "_noCloudIconConstraint"
- "_normalFontConstraints"
- "_percent"
- "_prevPercent"
- "_progressLabel"
- "_progressView"
- "_progressWidth"
- "_recoverable"
- "_reload:"
- "_significantItems"
- "_size"
- "_sizeLabel"
- "_sizeRightConstraint"
- "_specLock"
- "_specifier"
- "_spinner"
- "_tips"
- "_titleInfoView"
- "_titleLabel"
- "_titleWidth"
- "_typeOfCurrentDevice"
- "_uiDelegate"
- "_vendorLabel"
- "accessoryType"
- "activateConstraints:"
- "activatingString"
- "activationPercent"
- "addObject:"
- "addObjectsFromArray:"
- "addOperationWithBlock:"
- "addSubview:"
- "addTarget:action:forControlEvents:"
- "additionalButtonTitle"
- "appClipMetadata"
- "appIdentifier"
- "appSize"
- "appSizeIfComputed"
- "array"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "ascender"
- "bezierPathWithArcCenter:radius:startAngle:endAngle:clockwise:"
- "bezierPathWithOvalInRect:"
- "boolValue"
- "bounds"
- "bundleForClass:"
- "bundleIdentifier"
- "bundleWithIdentifier:"
- "bundleWithURL:"
- "buttonWithType:"
- "cancelPreviousPerformRequestsWithTarget:selector:object:"
- "clearColor"
- "cloudIconHidden"
- "confirmationButtonTitle"
- "confirmationText"
- "constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:"
- "constraintsWithVisualFormat:options:metrics:views:"
- "contentView"
- "count"
- "createLargeFontConstraints"
- "createNormalFontConstraints"
- "createdDate"
- "currentDevice"
- "d"
- "d16@0:8"
- "deactivateConstraints:"
- "defaultCellHeight"
- "defaultCenter"
- "delegate"
- "descender"
- "detailControllerClass"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "documentAppIdentifiers"
- "documentSpecifiersForApp:"
- "drawRect:"
- "enableButtonTitle"
- "enableOption"
- "enableOptionForTip:"
- "eventualGain"
- "externDataSizeAppIdentifiers"
- "externDataSizeForApp:"
- "f"
- "f16@0:8"
- "floatValue"
- "frame"
- "generateBestRepresentationForRequest:completionHandler:"
- "genericApplicationIcon"
- "getCGImageForImageDescriptor:completion:"
- "getResourceValue:forKey:error:"
- "getValue:"
- "hasPrefix:"
- "icon"
- "identifier"
- "image"
- "imageForKey:"
- "imageNamed:inBundle:"
- "imageWithCGImage:"
- "immediateGain"
- "info"
- "infoHidden"
- "infoSpecifier"
- "infoText"
- "init"
- "initWithActivityIndicatorStyle:"
- "initWithBundleIdentifier:"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "initWithFileAtURL:size:scale:representationTypes:"
- "initWithFrame:"
- "initWithSize:scale:"
- "initWithString:attributes:"
- "initWithStyle:reuseIdentifier:specifier:"
- "intValue"
- "isAppClip"
- "isDemoted"
- "isEqualToString:"
- "isHidden"
- "isRecoverable"
- "lastPathComponent"
- "lastUsedDate"
- "length"
- "localizedStringForKey:value:table:"
- "longLongValue"
- "mayCauseDataLoss"
- "name"
- "notify:forBundleIDs:"
- "notifyUsageChanged"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithLongLong:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "percent"
- "performAdditionalAction"
- "performAdditionalAction:"
- "performSelector:withObject:afterDelay:"
- "performSetterWithValue:"
- "pointerValue"
- "postAppsStateChanged:"
- "postNotificationName:object:"
- "preferenceSpecifierNamed:target:set:get:detail:cell:edit:"
- "preferredContentSizeCategory"
- "preferredFontForTextStyle:"
- "propertyForKey:"
- "q"
- "q16@0:8"
- "q24@0:8@16"
- "recoverable"
- "redColor"
- "refreshCellContentsWithSpecifier:"
- "reload"
- "reloadSpecifiersForApp:"
- "reloadTips"
- "removePropertyForKey:"
- "representedApp"
- "secondaryLabelColor"
- "setAccessibilityElements:"
- "setAccessibilityIdentifier:"
- "setActivatingString:"
- "setActivationPercent:"
- "setActive:"
- "setAdditionalButtonTitle:"
- "setAdjustsFontForContentSizeCategory:"
- "setAllowsDefaultTighteningForTruncation:"
- "setAlternateButton:"
- "setAttributedTitle:forState:"
- "setBackgroundColor:"
- "setCancelButton:"
- "setCloudIconHidden:"
- "setConfirmationAction:"
- "setConfirmationAlternateAction:"
- "setConfirmationButtonTitle:"
- "setConfirmationText:"
- "setConstant:"
- "setContentCompressionResistancePriority:forAxis:"
- "setContentHuggingPriority:forAxis:"
- "setContentMode:"
- "setCreatedDate:"
- "setDelegate:"
- "setDetailControllerClass:"
- "setDrawBorder:"
- "setEnableButtonTitle:"
- "setEnabled:"
- "setEventualGain:"
- "setFont:"
- "setHidden:"
- "setHidesWhenStopped:"
- "setIcon:"
- "setIdentifier:"
- "setImage:"
- "setImmediateGain:"
- "setInfo:"
- "setInfoHidden:"
- "setInfoText:"
- "setLastUsedDate:"
- "setLineBreakMode:"
- "setLineWidth:"
- "setMaxConcurrentOperationCount:"
- "setMayCauseDataLoss:"
- "setNeedsDisplay"
- "setNeedsLayout"
- "setNeedsUpdateConstraints"
- "setNumberOfLines:"
- "setNumberStyle:"
- "setObject:forKey:"
- "setOkButton:"
- "setPercent:"
- "setPriority:"
- "setPrompt:"
- "setProperty:forKey:"
- "setQualityOfService:"
- "setRecoverable:"
- "setRepresentedApp:"
- "setSeparatorInset:"
- "setShape:"
- "setSignificantItems:"
- "setSize:"
- "setSizeString:"
- "setSpecifier:"
- "setSpinner:"
- "setStroke"
- "setText:"
- "setTextColor:"
- "setTintColor:"
- "setTips:"
- "setTitle:"
- "setTitleColor:forState:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setUiDelegate:"
- "setValue:specifier:"
- "setVendor:"
- "setVersionLabelEnabled:"
- "settingsIconCache"
- "setupTitleAndInfoConstraints"
- "sharedGenerator"
- "sharedNotifier"
- "showConfirmationViewForSpecifier:"
- "significantItems"
- "size"
- "sizeString"
- "sizeToFit"
- "specifier"
- "specifierForAppBundleURL:"
- "specifierForAppIdentifier:"
- "specifierForAppProxy:"
- "specifierForChildApp:"
- "specifierForItemURL:"
- "specifierForStorageApp:"
- "spinner"
- "startAnimating"
- "stopAnimating"
- "stringFromNumber:"
- "stringWithFormat:"
- "stroke"
- "symbolForTypeIdentifier:error:"
- "systemBlueColor"
- "systemDarkGrayColor"
- "systemDarkLightMidGrayColor"
- "systemDarkMidGrayColor"
- "systemGray2Color"
- "systemGrayColor"
- "systemGreenColor"
- "systemImageNamed:"
- "systemImageNamed:compatibleWithTraitCollection:"
- "systemLightMidGrayColor"
- "systemOrangeColor"
- "systemPinkColor"
- "systemPurpleColor"
- "systemTealColor"
- "systemYellowColor"
- "text"
- "timeIntervalSinceReferenceDate"
- "tipDidUpdate:"
- "tips"
- "title"
- "traitCollection"
- "traitCollectionDidChange:"
- "uiDelegate"
- "unsignedLongLongValue"
- "updateColors"
- "updateConstraints"
- "userInterfaceIdiom"
- "userInterfaceStyle"
- "userTotal"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8f16"
- "v24@0:8#16"
- "v24@0:8@16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v32@0:8@16@24"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "vendor"
- "vendorName"
- "versionLabelEnabled"
- "versionString"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
