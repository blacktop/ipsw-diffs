## icloudCalendarSettings

> `/System/Library/PreferenceBundles/AccountSettings/icloudCalendarSettings.bundle/icloudCalendarSettings`

```diff

-2025.1.5.0.0
-  __TEXT.__text: 0x9c54
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_stubs: 0x1980
+2025.4.2.0.0
+  __TEXT.__text: 0xa844
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__objc_stubs: 0x1a60
   __TEXT.__objc_methlist: 0x94c
   __TEXT.__const: 0x314
   __TEXT.__objc_methname: 0x1d5e
-  __TEXT.__objc_classname: 0x1c3
-  __TEXT.__objc_methtype: 0x44d
-  __TEXT.__gcc_except_tab: 0x130
-  __TEXT.__cstring: 0x8f6
+  __TEXT.__objc_classname: 0x266
+  __TEXT.__objc_methtype: 0x471
+  __TEXT.__gcc_except_tab: 0x12c
+  __TEXT.__cstring: 0x824
   __TEXT.__oslogstring: 0x704
   __TEXT.__constg_swiftt: 0xb4
   __TEXT.__swift5_typeref: 0xce

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x2c8
-  __DATA_CONST.__auth_got: 0x330
+  __TEXT.__unwind_info: 0x318
+  __DATA_CONST.__auth_got: 0x308
   __DATA_CONST.__got: 0x268
   __DATA_CONST.__auth_ptr: 0x100
   __DATA_CONST.__const: 0x340

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 82D777A2-2AB7-35F9-AC56-EB47A0CACC2F
-  Functions: 232
-  Symbols:   231
-  CStrings:  650
+  UUID: FECE703E-52AB-36A6-BF36-990CC3AFC643
+  Functions: 245
+  Symbols:   2270
+  CStrings:  647
 
Symbols:
+ 
+ +[CalendarPopupButtonCell cellStyle]
+ +[CalendarReadSettingsRequest responseClass]
+ +[CalendarUpdateSettingsRequest responseClass]
+ +[CalendarUtil showErrorForPresenter:withError:callback:]
+ +[SharedCalendarEmailUpdateRequest responseClass]
+ -[CalBaseResponse .cxx_destruct]
+ -[CalBaseResponse calError]
+ -[CalBaseResponse initWithDictionary:]
+ -[CalBaseResponse setCalError:]
+ -[CalError .cxx_destruct]
+ -[CalError errorCode]
+ -[CalError errorMessage]
+ -[CalError errorTitle]
+ -[CalError initWithDictionary:]
+ -[CalError retryAfter]
+ -[CalError setErrorCode:]
+ -[CalError setErrorMessage:]
+ -[CalError setErrorTitle:]
+ -[CalError setRetryAfter:]
+ -[CalGetSettingsResponse .cxx_destruct]
+ -[CalGetSettingsResponse description]
+ -[CalGetSettingsResponse emails]
+ -[CalGetSettingsResponse initWithDictionary:]
+ -[CalGetSettingsResponse initWithHTTPResponse:data:]
+ -[CalGetSettingsResponse makoAccount]
+ -[CalGetSettingsResponse setEmails:]
+ -[CalGetSettingsResponse setMakoAccount:]
+ -[CalGetSettingsResponse setSharedCalendarEmail:]
+ -[CalGetSettingsResponse sharedCalendarEmail]
+ -[CalInviteEmail .cxx_destruct]
+ -[CalInviteEmail address]
+ -[CalInviteEmail description]
+ -[CalInviteEmail initWithDictionary:]
+ -[CalInviteEmail receive]
+ -[CalInviteEmail send]
+ -[CalInviteEmail setAddress:]
+ -[CalInviteEmail setReceive:]
+ -[CalInviteEmail setSend:]
+ -[CalInviteEmail toDictionary]
+ -[CalendarBaseRequest .cxx_destruct]
+ -[CalendarBaseRequest _errorDictionaryFromServerResponse:]
+ -[CalendarBaseRequest _performRequestWithHandler:renewToken:]
+ -[CalendarBaseRequest bodyDictionary]
+ -[CalendarBaseRequest iCloudAppleAccount]
+ -[CalendarBaseRequest initWithURLString:accountStore:appleAccount:httpRequestType:requestBody:httpHeader:]
+ -[CalendarBaseRequest performRequestWithHandler:]
+ -[CalendarBaseRequest requestBody]
+ -[CalendarBaseRequest setRequestBody:]
+ -[CalendarBaseRequest urlRequest]
+ -[CalendarBaseRequest urlRequest].cold.1
+ -[CalendarBaseRequest urlString]
+ -[CalendarPopupButtonCell .cxx_destruct]
+ -[CalendarPopupButtonCell _configureConstraints]
+ -[CalendarPopupButtonCell _configureViews:]
+ -[CalendarPopupButtonCell _setupViews]
+ -[CalendarPopupButtonCell initWithStyle:reuseIdentifier:]
+ -[CalendarPopupButtonCell popupButton]
+ -[CalendarPopupButtonCell popupMenu]
+ -[CalendarPopupButtonCell prepareForReuse]
+ -[CalendarPopupButtonCell refreshCellContentsWithSpecifier:]
+ -[CalendarPopupButtonCell rowLabel]
+ -[CalendarPopupButtonCell setPopupButton:]
+ -[CalendarPopupButtonCell setPopupMenu:]
+ -[CalendarPopupButtonCell setRowLabel:]
+ -[CalendarReadSettingsRequest initWithAccount:accountStore:]
+ -[CalendarReadSettingsRequest performRequestWithCallback:]
+ -[CalendarReadSettingsRequest urlString]
+ -[CalendarSendReceiveController .cxx_destruct]
+ -[CalendarSendReceiveController _didSelectEmailForSend:]
+ -[CalendarSendReceiveController _didSelectOptionForReceive:withOption:]
+ -[CalendarSendReceiveController _getEmail:]
+ -[CalendarSendReceiveController _receiveEmailSpecifiers]
+ -[CalendarSendReceiveController _sendEmailSpecifiers]
+ -[CalendarSendReceiveController _updateSettingsForEmail:]
+ -[CalendarSendReceiveController emailList]
+ -[CalendarSendReceiveController icloudAccount]
+ -[CalendarSendReceiveController initWithEmailData:userAccount:]
+ -[CalendarSendReceiveController selectedSendFromAddress]
+ -[CalendarSendReceiveController setEmailList:]
+ -[CalendarSendReceiveController setIcloudAccount:]
+ -[CalendarSendReceiveController setSelectedSendFromAddress:]
+ -[CalendarSendReceiveController specifiers]
+ -[CalendarSendReceiveController tableView:willDisplayCell:forRowAtIndexPath:]
+ -[CalendarSendReceiveController tableView:willDisplayCell:forRowAtIndexPath:].cold.1
+ -[CalendarSendReceiveController viewDidLoad]
+ -[CalendarSettingsController .cxx_destruct]
+ -[CalendarSettingsController _calendarCardViewSpecifier]
+ -[CalendarSettingsController _calendarSettingRefreshNotification:]
+ -[CalendarSettingsController _enableSharedCalendarUpdate:forSpecifier:]
+ -[CalendarSettingsController _enableSharedCalendarUpdate:forSpecifier:].cold.1
+ -[CalendarSettingsController _getSharedCalendarEmailStatus]
+ -[CalendarSettingsController _isSharedCalendarUpdateEnabled:]
+ -[CalendarSettingsController _loadCalendarSettingInfoSpecifier]
+ -[CalendarSettingsController _loadSendReceiveSpecifier]
+ -[CalendarSettingsController _loadSharedCalenderUpdateSpecifier]
+ -[CalendarSettingsController _sendReceiveSpecifierWasTapped:]
+ -[CalendarSettingsController _sendReceiveSpecifierWasTapped:].cold.1
+ -[CalendarSettingsController _showSendReceive]
+ -[CalendarSettingsController account]
+ -[CalendarSettingsController appleAccount]
+ -[CalendarSettingsController getSendReceiveState:]
+ -[CalendarSettingsController getSettingsResponse]
+ -[CalendarSettingsController handleURL:withCompletion:]
+ -[CalendarSettingsController handleURL:withCompletion:].cold.1
+ -[CalendarSettingsController handleURL:withCompletion:].cold.2
+ -[CalendarSettingsController handleURL:withCompletion:].cold.3
+ -[CalendarSettingsController setAppleAccount:]
+ -[CalendarSettingsController setGetSettingsResponse:]
+ -[CalendarSettingsController specifiers]
+ -[CalendarSettingsController specifiers].cold.1
+ -[CalendarSettingsController tableView:willDisplayCell:forRowAtIndexPath:]
+ -[CalendarSettingsController tableView:willDisplayCell:forRowAtIndexPath:].cold.1
+ -[CalendarSettingsController viewDidLoad]
+ -[CalendarSettingsController viewWillAppear:]
+ -[CalendarSettingsSpecifierProvider .cxx_destruct]
+ -[CalendarSettingsSpecifierProvider _dataclassState:]
+ -[CalendarSettingsSpecifierProvider accountForServiceType:primaryAltDSID:primaryDSID:]
+ -[CalendarSettingsSpecifierProvider account]
+ -[CalendarSettingsSpecifierProvider accountsForAccountManager:]
+ -[CalendarSettingsSpecifierProvider delegate]
+ -[CalendarSettingsSpecifierProvider initPresenter:]
+ -[CalendarSettingsSpecifierProvider initWithAccountManager:]
+ -[CalendarSettingsSpecifierProvider initWithAccountManager:presenter:]
+ -[CalendarSettingsSpecifierProvider initWithManager:presenter:]
+ -[CalendarSettingsSpecifierProvider onCalendarTapWithDeeplink:]
+ -[CalendarSettingsSpecifierProvider onCalendarTapWithDeeplink:].cold.1
+ -[CalendarSettingsSpecifierProvider onCalendarTap]
+ -[CalendarSettingsSpecifierProvider serviceOwnersManager]
+ -[CalendarSettingsSpecifierProvider setDelegate:]
+ -[CalendarSettingsSpecifierProvider setSpecifiers:]
+ -[CalendarSettingsSpecifierProvider specifiers]
+ -[CalendarSettingsSpecifierProvider specifiers].cold.1
+ -[CalendarSpinner .cxx_destruct]
+ -[CalendarSpinner initWithViewController:]
+ -[CalendarSpinner spinner]
+ -[CalendarSpinner startSpinner]
+ -[CalendarSpinner stopSpinner]
+ -[CalendarUpdateSettingsRequest .cxx_destruct]
+ -[CalendarUpdateSettingsRequest bodyDictionary]
+ -[CalendarUpdateSettingsRequest initWithAccount:accountStore:emailList:]
+ -[CalendarUpdateSettingsRequest inviteEmailArray]
+ -[CalendarUpdateSettingsRequest performRequestWithCallback:]
+ -[CalendarUpdateSettingsRequest setInviteEmailArray:]
+ -[CalendarUpdateSettingsRequest urlString]
+ -[PSSpecifier(Spinner) calendar_startSpinner]
+ -[PSSpecifier(Spinner) calendar_stopSpinner]
+ -[SharedCalendarEmailUpdateRequest bodyDictionary]
+ -[SharedCalendarEmailUpdateRequest initWithAccount:accountStore:sharedCalendarEmail:]
+ -[SharedCalendarEmailUpdateRequest performRequestWithCallback:]
+ -[SharedCalendarEmailUpdateRequest setSharedCalendarEmailUpdateFlag:]
+ -[SharedCalendarEmailUpdateRequest sharedCalendarEmailUpdateFlag]
+ -[SharedCalendarEmailUpdateRequest urlString]
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Binaries/icloudMCCKit/install/TempContent/Objects/icloudMCCKit.build/icloudCalendarSettings.build/DerivedSources/
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Binaries/icloudMCCKit/install/TempContent/Objects/icloudMCCKit.build/icloudCalendarSettings.build/Objects-normal/arm64e/CalBaseResponse.o
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Binaries/icloudMCCKit/install/TempContent/Objects/icloudMCCKit.build/icloudCalendarSettings.build/Objects-normal/arm64e/CalError.o
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Binaries/icloudMCCKit/install/TempContent/Objects/icloudMCCKit.build/icloudCalendarSettings.build/Objects-normal/arm64e/CalGetSettingsResponse.o
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Binaries/icloudMCCKit/install/TempContent/Objects/icloudMCCKit.build/icloudCalendarSettings.build/Objects-normal/arm64e/CalInviteEmail.o
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Binaries/icloudMCCKit/install/TempContent/Objects/icloudMCCKit.build/icloudCalendarSettings.build/Objects-normal/arm64e/CalendarBaseRequest.o
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Binaries/icloudMCCKit/install/TempContent/Objects/icloudMCCKit.build/icloudCalendarSettings.build/Objects-normal/arm64e/CalendarLogging.o
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Binaries/icloudMCCKit/install/TempContent/Objects/icloudMCCKit.build/icloudCalendarSettings.build/Objects-normal/arm64e/CalendarPlacardCell.o
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Binaries/icloudMCCKit/install/TempContent/Objects/icloudMCCKit.build/icloudCalendarSettings.build/Objects-normal/arm64e/CalendarPopupButtonCell.o
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Binaries/icloudMCCKit/install/TempContent/Objects/icloudMCCKit.build/icloudCalendarSettings.build/Objects-normal/arm64e/CalendarSendReceiveController.o
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Binaries/icloudMCCKit/install/TempContent/Objects/icloudMCCKit.build/icloudCalendarSettings.build/Objects-normal/arm64e/CalendarSettingsController.o
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Binaries/icloudMCCKit/install/TempContent/Objects/icloudMCCKit.build/icloudCalendarSettings.build/Objects-normal/arm64e/CalendarSettingsSpecifierProvider.o
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Binaries/icloudMCCKit/install/TempContent/Objects/icloudMCCKit.build/icloudCalendarSettings.build/Objects-normal/arm64e/CalendarSpinner.o
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Binaries/icloudMCCKit/install/TempContent/Objects/icloudMCCKit.build/icloudCalendarSettings.build/Objects-normal/arm64e/CalendarUtil.o
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Binaries/icloudMCCKit/install/TempContent/Objects/icloudMCCKit.build/icloudCalendarSettings.build/Objects-normal/arm64e/GeneratedAssetSymbols.o
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Binaries/icloudMCCKit/install/TempContent/Objects/icloudMCCKit.build/icloudCalendarSettings.build/Objects-normal/arm64e/PSSpecifier+Spinner.o
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Binaries/icloudMCCKit/install/TempContent/Objects/icloudMCCKit.build/icloudCalendarSettings.build/Objects-normal/arm64e/String+Extensions.o
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Binaries/icloudMCCKit/install/TempContent/Objects/icloudMCCKit.build/icloudCalendarSettings.build/Objects-normal/arm64e/icloudCalendarSettings.swiftmodule
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Binaries/icloudMCCKit/install/TempContent/Objects/icloudMCCKit.build/icloudCalendarSettings.build/Objects-normal/arm64e/icloudCalendarSettings_vers.o
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Sources/icloudMCCKit/CalendarSettings/Api/
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Sources/icloudMCCKit/CalendarSettings/Api/Response/
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Sources/icloudMCCKit/CalendarSettings/CustomCell/
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Sources/icloudMCCKit/CalendarSettings/Specifier/
+ /Library/Caches/com.apple.xbs/6EC83414-9AA2-46D4-9C17-916CB1E7813A/TemporaryDirectory.xj0g5s/Sources/icloudMCCKit/CalendarSettings/Utils/
+ CalBaseResponse.m
+ CalError.m
+ CalGetSettingsResponse.m
+ CalInviteEmail.m
+ CalendarBaseRequest.m
+ CalendarLogging.m
+ CalendarPlacardCell.swift
+ CalendarPopupButtonCell.m
+ CalendarSendReceiveController.m
+ CalendarSettingsController.m
+ CalendarSettingsSpecifierProvider.m
+ CalendarSpinner.m
+ CalendarUtil.m
+ GCC_except_table12
+ GCC_except_table2
+ GCC_except_table22
+ GCC_except_table6
+ GeneratedAssetSymbols.swift
+ OBJC_IVAR_$_CalBaseResponse._calError
+ OBJC_IVAR_$_CalError._errorCode
+ OBJC_IVAR_$_CalError._errorMessage
+ OBJC_IVAR_$_CalError._errorTitle
+ OBJC_IVAR_$_CalError._retryAfter
+ OBJC_IVAR_$_CalGetSettingsResponse._emails
+ OBJC_IVAR_$_CalGetSettingsResponse._makoAccount
+ OBJC_IVAR_$_CalGetSettingsResponse._sharedCalendarEmail
+ OBJC_IVAR_$_CalInviteEmail._address
+ OBJC_IVAR_$_CalInviteEmail._receive
+ OBJC_IVAR_$_CalInviteEmail._send
+ OBJC_IVAR_$_CalendarBaseRequest._iCloudAppleAccount
+ OBJC_IVAR_$_CalendarBaseRequest._requestBody
+ OBJC_IVAR_$_CalendarPopupButtonCell._popupButton
+ OBJC_IVAR_$_CalendarPopupButtonCell._popupMenu
+ OBJC_IVAR_$_CalendarPopupButtonCell._rowLabel
+ OBJC_IVAR_$_CalendarSendReceiveController._emailList
+ OBJC_IVAR_$_CalendarSendReceiveController._icloudAccount
+ OBJC_IVAR_$_CalendarSendReceiveController._selectedSendFromAddress
+ OBJC_IVAR_$_CalendarSendReceiveController._spinner
+ OBJC_IVAR_$_CalendarSettingsController._appleAccount
+ OBJC_IVAR_$_CalendarSettingsController._getSettingsResponse
+ OBJC_IVAR_$_CalendarSettingsController._userInfoDictionary
+ OBJC_IVAR_$_CalendarSettingsController.needsToNavigateToSendAndReceive
+ OBJC_IVAR_$_CalendarSettingsSpecifierProvider._accountManager
+ OBJC_IVAR_$_CalendarSettingsSpecifierProvider._delegate
+ OBJC_IVAR_$_CalendarSettingsSpecifierProvider._iCloudCalendarSettingSpecifier
+ OBJC_IVAR_$_CalendarSettingsSpecifierProvider._presenter
+ OBJC_IVAR_$_CalendarSettingsSpecifierProvider._serviceOwnersManager
+ OBJC_IVAR_$_CalendarSettingsSpecifierProvider._specifiers
+ OBJC_IVAR_$_CalendarSpinner._prevButtonItem
+ OBJC_IVAR_$_CalendarSpinner._spinner
+ OBJC_IVAR_$_CalendarSpinner._viewController
+ OBJC_IVAR_$_CalendarUpdateSettingsRequest._inviteEmailArray
+ OBJC_IVAR_$_SharedCalendarEmailUpdateRequest._sharedCalendarEmailUpdateFlag
+ PSSpecifier+Spinner.m
+ String+Extensions.swift
+ _$s10Foundation17NSLocalizedString_9tableName6bundle5value7commentS2S_SSSgSo8NSBundleCS2StF
+ _$s10Foundation3URLV19_bridgeToObjectiveCSo5NSURLCyF
+ _$s15_ObjectiveCTypes01_A11CBridgeablePTl
+ _$s21_IconServices_SwiftUI05AsyncA5ImageVMn
+ _$s22icloudCalendarSettings0B11PlacardCellC07refreshE8Contents4withySo11PSSpecifierCSg_tF
+ _$s22icloudCalendarSettings0B11PlacardCellC07refreshE8Contents4withySo11PSSpecifierCSg_tF0C00cD4ViewVy21_IconServices_SwiftUI05AsyncK5ImageVy0mN00P0VGGyXEfU_
+ _$s22icloudCalendarSettings0B11PlacardCellC07refreshE8Contents4withySo11PSSpecifierCSg_tF0C00cD4ViewVy21_IconServices_SwiftUI05AsyncK5ImageVy0mN00P0VGGyXEfU_y10Foundation3URLVcfU_
+ _$s22icloudCalendarSettings0B11PlacardCellC07refreshE8Contents4withySo11PSSpecifierCSg_tFTo
+ _$s22icloudCalendarSettings0B11PlacardCellC5coderACSgSo7NSCoderC_tcfC
+ _$s22icloudCalendarSettings0B11PlacardCellC5coderACSgSo7NSCoderC_tcfc
+ _$s22icloudCalendarSettings0B11PlacardCellC5coderACSgSo7NSCoderC_tcfcTo
+ _$s22icloudCalendarSettings0B11PlacardCellC5style15reuseIdentifier9specifierACSgSo011UITableViewE5StyleV_SSSgSo11PSSpecifierCSgtcfC
+ _$s22icloudCalendarSettings0B11PlacardCellC5style15reuseIdentifier9specifierACSgSo011UITableViewE5StyleV_SSSgSo11PSSpecifierCSgtcfc
+ _$s22icloudCalendarSettings0B11PlacardCellC5style15reuseIdentifier9specifierACSgSo011UITableViewE5StyleV_SSSgSo11PSSpecifierCSgtcfcTo
+ _$s22icloudCalendarSettings0B11PlacardCellC5style15reuseIdentifierACSo011UITableViewE5StyleV_SSSgtcfC
+ _$s22icloudCalendarSettings0B11PlacardCellC5style15reuseIdentifierACSo011UITableViewE5StyleV_SSSgtcfc
+ _$s22icloudCalendarSettings0B11PlacardCellC5style15reuseIdentifierACSo011UITableViewE5StyleV_SSSgtcfcTo
+ _$s22icloudCalendarSettings0B11PlacardCellCMF
+ _$s22icloudCalendarSettings0B11PlacardCellCMa
+ _$s22icloudCalendarSettings0B11PlacardCellCMf
+ _$s22icloudCalendarSettings0B11PlacardCellCMn
+ _$s22icloudCalendarSettings0B11PlacardCellCN
+ _$s22icloudCalendarSettings0B11PlacardCellCfD
+ _$s22icloudCalendarSettings19ResourceBundleClass33_AB55B1C9D62F009F4345535693AFCC67LLCMF
+ _$s22icloudCalendarSettings19ResourceBundleClass33_AB55B1C9D62F009F4345535693AFCC67LLCMXX
+ _$s22icloudCalendarSettings19ResourceBundleClass33_AB55B1C9D62F009F4345535693AFCC67LLCMa
+ _$s22icloudCalendarSettings19ResourceBundleClass33_AB55B1C9D62F009F4345535693AFCC67LLCMf
+ _$s22icloudCalendarSettings19ResourceBundleClass33_AB55B1C9D62F009F4345535693AFCC67LLCMm
+ _$s22icloudCalendarSettings19ResourceBundleClass33_AB55B1C9D62F009F4345535693AFCC67LLCMn
+ _$s22icloudCalendarSettings19ResourceBundleClass33_AB55B1C9D62F009F4345535693AFCC67LLCN
+ _$s22icloudCalendarSettings19ResourceBundleClass33_AB55B1C9D62F009F4345535693AFCC67LLCfD
+ _$s22icloudCalendarSettingsMXM
+ _$s7SwiftUI22UIHostingConfigurationV7marginsyACyxq_GAA4EdgeO3SetV_12CoreGraphics7CGFloatVtF
+ _$s7SwiftUI22UIHostingConfigurationVA2A9EmptyViewVRs_rlE7contentACyxAEGxyXE_tcfC
+ _$s7SwiftUI22UIHostingConfigurationVMn
+ _$s7SwiftUI22UIHostingConfigurationVy8Settings0E11PlacardViewVy014_IconServices_aB005AsyncH5ImageVyAA0K0VGGAA05EmptyG0VGACyxq_G5UIKit09UIContentD0AAWL
+ _$s7SwiftUI22UIHostingConfigurationVy8Settings0E11PlacardViewVy014_IconServices_aB005AsyncH5ImageVyAA0K0VGGAA05EmptyG0VGMR
+ _$s7SwiftUI22UIHostingConfigurationVy8Settings0E11PlacardViewVy014_IconServices_aB005AsyncH5ImageVyAA0K0VGGAA05EmptyG0VGMd
+ _$s7SwiftUI22UIHostingConfigurationVyxq_G5UIKit09UIContentD0AAMc
+ _$s7SwiftUI4EdgeO3SetV8verticalAEvgZ
+ _$s7SwiftUI5ImageVMn
+ _$s7SwiftUI9EmptyViewVMn
+ _$s8RawValueSYTl
+ _$s8Settings0A11PlacardViewVAA21_IconServices_SwiftUI05AsyncD5ImageVy0fG00I0VGRszrlE14localizedTitle0J8Subtitle27applicationBundleIdentifier10linkActionACyAJGSS_S2Sy10Foundation3URLVcSgtcfC
+ _$s8Settings0A11PlacardViewVMn
+ _$s8Settings0A11PlacardViewVy21_IconServices_SwiftUI05AsyncD5ImageVy0fG00I0VGGACyxGAG0C0AAWL
+ _$s8Settings0A11PlacardViewVy21_IconServices_SwiftUI05AsyncD5ImageVy0fG00I0VGGACyxGAG0C0AAWlTm
+ _$s8Settings0A11PlacardViewVy21_IconServices_SwiftUI05AsyncD5ImageVy0fG00I0VGGMR
+ _$s8Settings0A11PlacardViewVy21_IconServices_SwiftUI05AsyncD5ImageVy0fG00I0VGGMd
+ _$s8Settings0A11PlacardViewVyxG7SwiftUI0C0AAMc
+ _$s9UIKitCoreMXM
+ _$sBOWV
+ _$sBoWV
+ _$sS2Ss7CVarArg10FoundationWL
+ _$sS2Ss7CVarArg10FoundationWl
+ _$sSD10FoundationE19_bridgeToObjectiveCSo12NSDictionaryCyF
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo38UIApplicationOpenExternalURLOptionsKeya_ypTt0g5Tf4g_n
+ _$sSH13_rawHashValue4seedS2i_tFTq
+ _$sSH4hash4intoys6HasherVz_tFTq
+ _$sSH9hashValueSivgTq
+ _$sSHMp
+ _$sSHSQTb
+ _$sSQ2eeoiySbx_xtFZTq
+ _$sSQMp
+ _$sSS10FoundationE19_bridgeToObjectiveCSo8NSStringCyF
+ _$sSS10FoundationE26_forceBridgeFromObjectiveC_6resultySo8NSStringC_SSSgztFZ
+ _$sSS10FoundationE34_conditionallyBridgeFromObjectiveC_6resultSbSo8NSStringC_SSSgztFZ
+ _$sSS10FoundationE36_unconditionallyBridgeFromObjectiveCySSSo8NSStringCSgFZ
+ _$sSS10FoundationE6format_S2Sh_s7CVarArg_pdtcfC
+ _$sSS22icloudCalendarSettingsE9localizedSSvg
+ _$sSS22icloudCalendarSettingsE9localizedSSvpMV
+ _$sSS22icloudCalendarSettingsE9localizedySSs7CVarArg_pd_tF
+ _$sSS4hash4intoys6HasherVz_tF
+ _$sSS9hashValueSivg
+ _$sSSN
+ _$sSSSHsWP
+ _$sSSs7CVarArg10FoundationMc
+ _$sSY8rawValue03RawB0QzvgTq
+ _$sSY8rawValuexSg03RawB0Qz_tcfCTq
+ _$sSYMp
+ _$sScA15unownedExecutorScevgTj
+ _$sScM6sharedScMvgZ
+ _$sScMMa
+ _$sScMScAsWP
+ _$sSo15UITableViewCellC5UIKitE20contentConfigurationAC09UIContentF0_pSgvs
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaABSHSCWL
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaABSHSCWl
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaABSQSCWL
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaABSYSCWL
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaABSYSCWlTm
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaABs20_SwiftNewtypeWrapperSCWL
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaABs35_HasCustomAnyHashableRepresentationSCWL
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaMB
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaMF
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaML
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaMa
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaMf
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaMn
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaSHSCMc
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaSHSCMcMK
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaSHSCSH13_rawHashValue4seedS2i_tFTW
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaSHSCSH4hash4intoys6HasherVz_tFTW
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaSHSCSH9hashValueSivgTW
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaSHSCSQWb
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaSQSCMc
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaSQSCMcMK
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaSQSCSQ2eeoiySbx_xtFZTW
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaSYSCMA
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaSYSCMc
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaSYSCMcMK
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaSYSCSY8rawValue03RawG0QzvgTW
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyaSYSCSY8rawValuexSg03RawG0Qz_tcfCTW
+ _$sSo38UIApplicationOpenExternalURLOptionsKeya_yptMR
+ _$sSo38UIApplicationOpenExternalURLOptionsKeya_yptMd
+ _$sSo38UIApplicationOpenExternalURLOptionsKeya_yptWOc
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyas20_SwiftNewtypeWrapperSCMc
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyas20_SwiftNewtypeWrapperSCMcMK
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyas20_SwiftNewtypeWrapperSCSYWb
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentationPWb
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyas21_ObjectiveCBridgeableSCMA
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyas21_ObjectiveCBridgeableSCMc
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyas21_ObjectiveCBridgeableSCMcMK
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyas21_ObjectiveCBridgeableSCsACP016_forceBridgeFromF1C_6resulty01_F5CTypeQz_xSgztFZTW
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyas21_ObjectiveCBridgeableSCsACP024_conditionallyBridgeFromF1C_6resultSb01_F5CTypeQz_xSgztFZTW
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyas21_ObjectiveCBridgeableSCsACP026_unconditionallyBridgeFromF1Cyx01_F5CTypeQzSgFZTW
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyas21_ObjectiveCBridgeableSCsACP09_bridgeToF1C01_F5CTypeQzyFTW
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyas35_HasCustomAnyHashableRepresentationSCMc
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyas35_HasCustomAnyHashableRepresentationSCMcMK
+ _$sSo38UIApplicationOpenExternalURLOptionsKeyas35_HasCustomAnyHashableRepresentationSCsACP03_toghI0s0hI0VSgyFTW
+ _$sSoMXM
+ _$ss18_DictionaryStorageC8allocate8capacityAByxq_GSi_tFZ
+ _$ss18_DictionaryStorageCMn
+ _$ss18_DictionaryStorageCySo38UIApplicationOpenExternalURLOptionsKeyaypGMR
+ _$ss18_DictionaryStorageCySo38UIApplicationOpenExternalURLOptionsKeyaypGMd
+ _$ss20_SwiftNewtypeWrapperMp
+ _$ss20_SwiftNewtypeWrapperPSYTb
+ _$ss20_SwiftNewtypeWrapperPs35_HasCustomAnyHashableRepresentationTb
+ _$ss20_SwiftNewtypeWrapperPsSHRzSH8RawValueSYRpzrlE20_toCustomAnyHashables0hI0VSgyF
+ _$ss21_ObjectiveCBridgeableMp
+ _$ss21_ObjectiveCBridgeableP016_forceBridgeFromA1C_6resulty01_A5CTypeQz_xSgztFZTq
+ _$ss21_ObjectiveCBridgeableP024_conditionallyBridgeFromA1C_6resultSb01_A5CTypeQz_xSgztFZTq
+ _$ss21_ObjectiveCBridgeableP026_unconditionallyBridgeFromA1Cyx01_A5CTypeQzSgFZTq
+ _$ss21_ObjectiveCBridgeableP09_bridgeToA1C01_A5CTypeQzyFTq
+ _$ss22__RawDictionaryStorageC4find_9hashValues10_HashTableV6BucketV6bucket_Sb5foundtx_SitSHRzlFSo38UIApplicationOpenExternalURLOptionsKeya_Tg5
+ _$ss22__RawDictionaryStorageC4findys10_HashTableV6BucketV6bucket_Sb5foundtxSHRzlFSo38UIApplicationOpenExternalURLOptionsKeya_Tg5
+ _$ss23_ContiguousArrayStorageCMn
+ _$ss23_ContiguousArrayStorageCys7CVarArg_pGMR
+ _$ss23_ContiguousArrayStorageCys7CVarArg_pGMd
+ _$ss27_stringCompareWithSmolCheck__9expectingSbs11_StringGutsV_ADs01_G16ComparisonResultOtF
+ _$ss35_HasCustomAnyHashableRepresentationMp
+ _$ss35_HasCustomAnyHashableRepresentationP03_tobcD0s0cD0VSgyFTq
+ _$ss6HasherV5_seedABSi_tcfC
+ _$ss6HasherV9_finalizeSiyF
+ _$ss7CVarArgMp
+ _$sypN
+ _$sypWOb
+ _CalLogSystem.cold.1
+ _CalLogSystem.log
+ _CalLogSystem.onceToken
+ _OBJC_CLASS_$__TtC22icloudCalendarSettings19CalendarPlacardCell
+ _OBJC_METACLASS_$__TtC22icloudCalendarSettings19CalendarPlacardCell
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ __41-[CalendarSettingsController viewDidLoad]_block_invoke.93
+ __41-[CalendarSettingsController viewDidLoad]_block_invoke.cold.1
+ __41-[CalendarSettingsController viewDidLoad]_block_invoke.cold.2
+ __41-[CalendarSettingsController viewDidLoad]_block_invoke.cold.3
+ __57-[CalendarSendReceiveController _updateSettingsForEmail:]_block_invoke.138
+ __58-[CalendarReadSettingsRequest performRequestWithCallback:]_block_invoke.cold.1
+ __60-[CalendarUpdateSettingsRequest performRequestWithCallback:]_block_invoke.cold.1
+ __61-[CalendarBaseRequest _performRequestWithHandler:renewToken:]_block_invoke.99
+ __63-[SharedCalendarEmailUpdateRequest performRequestWithCallback:]_block_invoke.cold.1
+ __66-[CalendarSettingsController _calendarSettingRefreshNotification:]_block_invoke.192
+ __66-[CalendarSettingsController _calendarSettingRefreshNotification:]_block_invoke.cold.1
+ __66-[CalendarSettingsController _calendarSettingRefreshNotification:]_block_invoke.cold.2
+ __66-[CalendarSettingsController _calendarSettingRefreshNotification:]_block_invoke.cold.3
+ __71-[CalendarSettingsController _enableSharedCalendarUpdate:forSpecifier:]_block_invoke.184
+ __DATA__TtC22icloudCalendarSettings19CalendarPlacardCell
+ __DATA__TtC22icloudCalendarSettingsP33_AB55B1C9D62F009F4345535693AFCC6719ResourceBundleClass
+ __INSTANCE_METHODS__TtC22icloudCalendarSettings19CalendarPlacardCell
+ __METACLASS_DATA__TtC22icloudCalendarSettings19CalendarPlacardCell
+ __METACLASS_DATA__TtC22icloudCalendarSettingsP33_AB55B1C9D62F009F4345535693AFCC6719ResourceBundleClass
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_PSSpecifier_$_Spinner
+ __OBJC_$_CATEGORY_PSSpecifier_$_Spinner
+ __OBJC_$_CLASS_METHODS_CalendarPopupButtonCell
+ __OBJC_$_CLASS_METHODS_CalendarReadSettingsRequest
+ __OBJC_$_CLASS_METHODS_CalendarUpdateSettingsRequest
+ __OBJC_$_CLASS_METHODS_CalendarUtil
+ __OBJC_$_CLASS_METHODS_SharedCalendarEmailUpdateRequest
+ __OBJC_$_INSTANCE_METHODS_CalBaseResponse
+ __OBJC_$_INSTANCE_METHODS_CalError
+ __OBJC_$_INSTANCE_METHODS_CalGetSettingsResponse
+ __OBJC_$_INSTANCE_METHODS_CalInviteEmail
+ __OBJC_$_INSTANCE_METHODS_CalendarBaseRequest
+ __OBJC_$_INSTANCE_METHODS_CalendarPopupButtonCell
+ __OBJC_$_INSTANCE_METHODS_CalendarReadSettingsRequest
+ __OBJC_$_INSTANCE_METHODS_CalendarSendReceiveController
+ __OBJC_$_INSTANCE_METHODS_CalendarSettingsController
+ __OBJC_$_INSTANCE_METHODS_CalendarSettingsSpecifierProvider
+ __OBJC_$_INSTANCE_METHODS_CalendarSpinner
+ __OBJC_$_INSTANCE_METHODS_CalendarUpdateSettingsRequest
+ __OBJC_$_INSTANCE_METHODS_SharedCalendarEmailUpdateRequest
+ __OBJC_$_INSTANCE_VARIABLES_CalBaseResponse
+ __OBJC_$_INSTANCE_VARIABLES_CalError
+ __OBJC_$_INSTANCE_VARIABLES_CalGetSettingsResponse
+ __OBJC_$_INSTANCE_VARIABLES_CalInviteEmail
+ __OBJC_$_INSTANCE_VARIABLES_CalendarBaseRequest
+ __OBJC_$_INSTANCE_VARIABLES_CalendarPopupButtonCell
+ __OBJC_$_INSTANCE_VARIABLES_CalendarSendReceiveController
+ __OBJC_$_INSTANCE_VARIABLES_CalendarSettingsController
+ __OBJC_$_INSTANCE_VARIABLES_CalendarSettingsSpecifierProvider
+ __OBJC_$_INSTANCE_VARIABLES_CalendarSpinner
+ __OBJC_$_INSTANCE_VARIABLES_CalendarUpdateSettingsRequest
+ __OBJC_$_INSTANCE_VARIABLES_SharedCalendarEmailUpdateRequest
+ __OBJC_$_PROP_LIST_AAUISpecifierProvider
+ __OBJC_$_PROP_LIST_CalBaseResponse
+ __OBJC_$_PROP_LIST_CalError
+ __OBJC_$_PROP_LIST_CalGetSettingsResponse
+ __OBJC_$_PROP_LIST_CalInviteEmail
+ __OBJC_$_PROP_LIST_CalendarBaseRequest
+ __OBJC_$_PROP_LIST_CalendarPopupButtonCell
+ __OBJC_$_PROP_LIST_CalendarSendReceiveController
+ __OBJC_$_PROP_LIST_CalendarSettingsController
+ __OBJC_$_PROP_LIST_CalendarSettingsSpecifierProvider
+ __OBJC_$_PROP_LIST_CalendarSpinner
+ __OBJC_$_PROP_LIST_CalendarUpdateSettingsRequest
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST_SharedCalendarEmailUpdateRequest
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AAUISpecifierProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AIDAAccountManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AAUISpecifierProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_iCloudCalendarUnifiedSettingsProviderType
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AAUISpecifierProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AIDAAccountManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_iCloudCalendarUnifiedSettingsProviderType
+ __OBJC_$_PROTOCOL_REFS_AAUISpecifierProvider
+ __OBJC_$_PROTOCOL_REFS_AIDAAccountManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_iCloudCalendarUnifiedSettingsProviderType
+ __OBJC_CLASS_PROTOCOLS_$_CalendarSettingsSpecifierProvider
+ __OBJC_CLASS_RO_$_CalBaseResponse
+ __OBJC_CLASS_RO_$_CalError
+ __OBJC_CLASS_RO_$_CalGetSettingsResponse
+ __OBJC_CLASS_RO_$_CalInviteEmail
+ __OBJC_CLASS_RO_$_CalendarBaseRequest
+ __OBJC_CLASS_RO_$_CalendarPopupButtonCell
+ __OBJC_CLASS_RO_$_CalendarReadSettingsRequest
+ __OBJC_CLASS_RO_$_CalendarSendReceiveController
+ __OBJC_CLASS_RO_$_CalendarSettingsController
+ __OBJC_CLASS_RO_$_CalendarSettingsSpecifierProvider
+ __OBJC_CLASS_RO_$_CalendarSpinner
+ __OBJC_CLASS_RO_$_CalendarUpdateSettingsRequest
+ __OBJC_CLASS_RO_$_CalendarUtil
+ __OBJC_CLASS_RO_$_SharedCalendarEmailUpdateRequest
+ __OBJC_LABEL_PROTOCOL_$_AAUISpecifierProvider
+ __OBJC_LABEL_PROTOCOL_$_AIDAAccountManagerDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_iCloudCalendarUnifiedSettingsProviderType
+ __OBJC_METACLASS_RO_$_CalBaseResponse
+ __OBJC_METACLASS_RO_$_CalError
+ __OBJC_METACLASS_RO_$_CalGetSettingsResponse
+ __OBJC_METACLASS_RO_$_CalInviteEmail
+ __OBJC_METACLASS_RO_$_CalendarBaseRequest
+ __OBJC_METACLASS_RO_$_CalendarPopupButtonCell
+ __OBJC_METACLASS_RO_$_CalendarReadSettingsRequest
+ __OBJC_METACLASS_RO_$_CalendarSendReceiveController
+ __OBJC_METACLASS_RO_$_CalendarSettingsController
+ __OBJC_METACLASS_RO_$_CalendarSettingsSpecifierProvider
+ __OBJC_METACLASS_RO_$_CalendarSpinner
+ __OBJC_METACLASS_RO_$_CalendarUpdateSettingsRequest
+ __OBJC_METACLASS_RO_$_CalendarUtil
+ __OBJC_METACLASS_RO_$_SharedCalendarEmailUpdateRequest
+ __OBJC_PROTOCOL_$_AAUISpecifierProvider
+ __OBJC_PROTOCOL_$_AIDAAccountManagerDelegate
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_iCloudCalendarUnifiedSettingsProviderType
+ ___38-[CalendarPopupButtonCell _setupViews]_block_invoke
+ ___38-[CalendarPopupButtonCell _setupViews]_block_invoke_2
+ ___41-[CalendarSettingsController viewDidLoad]_block_invoke
+ ___57+[CalendarUtil showErrorForPresenter:withError:callback:]_block_invoke
+ ___57+[CalendarUtil showErrorForPresenter:withError:callback:]_block_invoke_2
+ ___57-[CalendarSendReceiveController _updateSettingsForEmail:]_block_invoke
+ ___57-[CalendarSendReceiveController _updateSettingsForEmail:]_block_invoke_2
+ ___57-[CalendarSendReceiveController _updateSettingsForEmail:]_block_invoke_3
+ ___57-[CalendarSendReceiveController _updateSettingsForEmail:]_block_invoke_4
+ ___58-[CalendarReadSettingsRequest performRequestWithCallback:]_block_invoke
+ ___60-[CalendarUpdateSettingsRequest performRequestWithCallback:]_block_invoke
+ ___61-[CalendarBaseRequest _performRequestWithHandler:renewToken:]_block_invoke
+ ___63-[SharedCalendarEmailUpdateRequest performRequestWithCallback:]_block_invoke
+ ___66-[CalendarSettingsController _calendarSettingRefreshNotification:]_block_invoke
+ ___71-[CalendarSettingsController _enableSharedCalendarUpdate:forSpecifier:]_block_invoke
+ ___71-[CalendarSettingsController _enableSharedCalendarUpdate:forSpecifier:]_block_invoke_2
+ ___71-[CalendarSettingsController _enableSharedCalendarUpdate:forSpecifier:]_block_invoke_3
+ ___71-[CalendarSettingsController _enableSharedCalendarUpdate:forSpecifier:]_block_invoke_4
+ ___77-[CalendarSendReceiveController tableView:willDisplayCell:forRowAtIndexPath:]_block_invoke
+ ___77-[CalendarSendReceiveController tableView:willDisplayCell:forRowAtIndexPath:]_block_invoke_2
+ ___77-[CalendarSendReceiveController tableView:willDisplayCell:forRowAtIndexPath:]_block_invoke_3
+ ____CalLogSystem_block_invoke
+ ___block_descriptor_32_e18_v16?0"UIAction"8l
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e23_v16?0"UIAlertAction"8ls32l8
+ ___block_descriptor_40_e8_32bs_e46_v32?0"AARequest"8"AAResponse"16"NSError"24ls32l8
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e18_v16?0"UIAction"8lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e44_v24?0"CalGetSettingsResponse"8"NSError"16lw40l8s32l8
+ ___block_descriptor_49_e8_32s40bs_e46_v32?0"AARequest"8"AAResponse"16"NSError"24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48w_e44_v24?0"CalGetSettingsResponse"8"NSError"16lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e20_v24?0q8"NSError"16ls56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56w_e44_v24?0"CalGetSettingsResponse"8"NSError"16lw56l8s32l8s40l8s48l8
+ ___block_literal_global
+ ___swift_allocate_boxed_opaque_existential_1
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_reflection_version
+ __block_literal_global.47
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_icloudCalendarSettings
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_icloudCalendarSettings
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_icloudCalendarSettings
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_icloudCalendarSettings
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_icloudCalendarSettings
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_icloudCalendarSettings
+ __swift_FORCE_LOAD_$_swiftCoreMedia_$_icloudCalendarSettings
+ __swift_FORCE_LOAD_$_swiftDispatch_$_icloudCalendarSettings
+ __swift_FORCE_LOAD_$_swiftFoundation_$_icloudCalendarSettings
+ __swift_FORCE_LOAD_$_swiftIntents_$_icloudCalendarSettings
+ __swift_FORCE_LOAD_$_swiftMetal_$_icloudCalendarSettings
+ __swift_FORCE_LOAD_$_swiftOSLog_$_icloudCalendarSettings
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_icloudCalendarSettings
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_icloudCalendarSettings
+ __swift_FORCE_LOAD_$_swiftSpatial_$_icloudCalendarSettings
+ __swift_FORCE_LOAD_$_swiftUIKit_$_icloudCalendarSettings
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_icloudCalendarSettings
+ __swift_FORCE_LOAD_$_swiftXPC_$_icloudCalendarSettings
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_icloudCalendarSettings
+ __swift_FORCE_LOAD_$_swiftos_$_icloudCalendarSettings
+ __swift_FORCE_LOAD_$_swiftsimd_$_icloudCalendarSettings
+ _associated conformance So38UIApplicationOpenExternalURLOptionsKeyaSHSCSQ
+ _associated conformance So38UIApplicationOpenExternalURLOptionsKeyas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So38UIApplicationOpenExternalURLOptionsKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _objc_allocWithZone
+ _objc_msgSend$DSIDForAccount:service:
+ _objc_msgSend$_calendarCardViewSpecifier
+ _objc_msgSend$_configureConstraints
+ _objc_msgSend$_configureViews:
+ _objc_msgSend$_didSelectEmailForSend:
+ _objc_msgSend$_didSelectOptionForReceive:withOption:
+ _objc_msgSend$_errorDictionaryFromServerResponse:
+ _objc_msgSend$_loadCalendarSettingInfoSpecifier
+ _objc_msgSend$_loadSendReceiveSpecifier
+ _objc_msgSend$_loadSharedCalenderUpdateSpecifier
+ _objc_msgSend$_performRequestWithHandler:renewToken:
+ _objc_msgSend$_receiveEmailSpecifiers
+ _objc_msgSend$_sendEmailSpecifiers
+ _objc_msgSend$_setupViews
+ _objc_msgSend$_showSendReceive
+ _objc_msgSend$_updateSettingsForEmail:
+ _objc_msgSend$aa_addBasicAuthorizationHeaderWithAccount:preferUsingPassword:
+ _objc_msgSend$aa_isManagedAppleID
+ _objc_msgSend$account
+ _objc_msgSend$accountForService:
+ _objc_msgSend$accountForServiceType:primaryAltDSID:primaryDSID:
+ _objc_msgSend$accountStore
+ _objc_msgSend$accountType
+ _objc_msgSend$accounts
+ _objc_msgSend$actionWithTitle:image:identifier:handler:
+ _objc_msgSend$actionWithTitle:style:handler:
+ _objc_msgSend$activateConstraints:
+ _objc_msgSend$acui_linkListCellSpecifierForDataclass:account:target:set:get:detail:
+ _objc_msgSend$addAction:
+ _objc_msgSend$addLayoutGuide:
+ _objc_msgSend$addObject:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$addObserver:selector:name:object:
+ _objc_msgSend$addSubview:
+ _objc_msgSend$addTarget:action:forControlEvents:
+ _objc_msgSend$address
+ _objc_msgSend$aida_accountForPrimaryiCloudAccount
+ _objc_msgSend$aida_accountForiCloudAccount:
+ _objc_msgSend$alertControllerWithTitle:message:preferredStyle:
+ _objc_msgSend$altDSIDForAccount:service:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$bodyDictionary
+ _objc_msgSend$boolValue
+ _objc_msgSend$bottomAnchor
+ _objc_msgSend$bounds
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$buttonAction
+ _objc_msgSend$buttonWithConfiguration:primaryAction:
+ _objc_msgSend$calError
+ _objc_msgSend$calendar_stopSpinner
+ _objc_msgSend$canOpenURL:
+ _objc_msgSend$cellReuseIdentifier
+ _objc_msgSend$centerYAnchor
+ _objc_msgSend$constraintEqualToAnchor:
+ _objc_msgSend$constraintEqualToAnchor:constant:
+ _objc_msgSend$constraintEqualToConstant:
+ _objc_msgSend$contentView
+ _objc_msgSend$copy
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$dataWithJSONObject:options:error:
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$defaultStore
+ _objc_msgSend$description
+ _objc_msgSend$deviceClass
+ _objc_msgSend$dictionaryWithContentsOfFile:
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$emails
+ _objc_msgSend$emptyGroupSpecifier
+ _objc_msgSend$errorMessage
+ _objc_msgSend$errorTitle
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$getSettingsResponse
+ _objc_msgSend$groupSpecifierWithID:name:
+ _objc_msgSend$groupSpecifierWithName:
+ _objc_msgSend$iCloudAppleAccount
+ _objc_msgSend$identifier
+ _objc_msgSend$infoDictionary
+ _objc_msgSend$initWithAccount:accountStore:
+ _objc_msgSend$initWithAccount:accountStore:emailList:
+ _objc_msgSend$initWithAccount:accountStore:sharedCalendarEmail:
+ _objc_msgSend$initWithAccountManager:presenter:
+ _objc_msgSend$initWithAccountStore:
+ _objc_msgSend$initWithAccountStore:grandSlamAccount:appTokenID:
+ _objc_msgSend$initWithActivityIndicatorStyle:
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithCoder:
+ _objc_msgSend$initWithCustomView:
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$initWithEmailData:userAccount:
+ _objc_msgSend$initWithStyle:reuseIdentifier:
+ _objc_msgSend$initWithStyle:reuseIdentifier:specifier:
+ _objc_msgSend$initWithViewController:
+ _objc_msgSend$isEditing
+ _objc_msgSend$isEnabledForDataclass:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isProvisionedForDataclass:
+ _objc_msgSend$item
+ _objc_msgSend$labelColor
+ _objc_msgSend$layoutIfNeeded
+ _objc_msgSend$leadingAnchor
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$mainBundle
+ _objc_msgSend$mainScreen
+ _objc_msgSend$makoAccount
+ _objc_msgSend$menuWithChildren:
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$navigationItem
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$onCalendarTapWithDeeplink:
+ _objc_msgSend$openURL:options:completionHandler:
+ _objc_msgSend$pe_isSettingsFeatureDescriptionCellSupported
+ _objc_msgSend$performRequestWithCallback:
+ _objc_msgSend$performRequestWithHandler:
+ _objc_msgSend$plainButtonConfiguration
+ _objc_msgSend$popupButton
+ _objc_msgSend$postNotificationName:object:userInfo:
+ _objc_msgSend$preferenceSpecifierNamed:target:set:get:detail:cell:edit:
+ _objc_msgSend$preferredFontForTextStyle:compatibleWithTraitCollection:
+ _objc_msgSend$presentViewController:animated:completion:
+ _objc_msgSend$propertiesForDataclass:
+ _objc_msgSend$propertyForKey:
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$receive
+ _objc_msgSend$registerClass:forCellReuseIdentifier:
+ _objc_msgSend$reloadSpecifierID:
+ _objc_msgSend$reloadSpecifiers
+ _objc_msgSend$reloadWithSpecifier:animated:
+ _objc_msgSend$removeObserver:name:object:
+ _objc_msgSend$removePropertyForKey:
+ _objc_msgSend$renewCredentialsForAccount:options:completion:
+ _objc_msgSend$rightBarButtonItem
+ _objc_msgSend$rowLabel
+ _objc_msgSend$secondaryLabelColor
+ _objc_msgSend$send
+ _objc_msgSend$serviceOwnersManager
+ _objc_msgSend$setAccessoryView:
+ _objc_msgSend$setBaseForegroundColor:
+ _objc_msgSend$setChangesSelectionAsPrimaryAction:
+ _objc_msgSend$setContentCompressionResistancePriority:forAxis:
+ _objc_msgSend$setContentHuggingPriority:forAxis:
+ _objc_msgSend$setControllerLoadAction:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setDetailControllerClass:
+ _objc_msgSend$setEditingAccessoryView:
+ _objc_msgSend$setEmailList:
+ _objc_msgSend$setFont:
+ _objc_msgSend$setHTTPBody:
+ _objc_msgSend$setHTTPMethod:
+ _objc_msgSend$setHidesBackButton:
+ _objc_msgSend$setIdentifier:
+ _objc_msgSend$setLineBreakMode:
+ _objc_msgSend$setMenu:
+ _objc_msgSend$setMessage:
+ _objc_msgSend$setName:
+ _objc_msgSend$setNumberOfLines:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setPopupButton:
+ _objc_msgSend$setPopupMenu:
+ _objc_msgSend$setPreferredMaxLayoutWidth:
+ _objc_msgSend$setProperty:forKey:
+ _objc_msgSend$setReceive:
+ _objc_msgSend$setRightBarButtonItem:animated:
+ _objc_msgSend$setRowLabel:
+ _objc_msgSend$setSelectionStyle:
+ _objc_msgSend$setSend:
+ _objc_msgSend$setSharedCalendarEmail:
+ _objc_msgSend$setShowsMenuAsPrimaryAction:
+ _objc_msgSend$setSpecifier:
+ _objc_msgSend$setState:
+ _objc_msgSend$setText:
+ _objc_msgSend$setTextColor:
+ _objc_msgSend$setTitle:
+ _objc_msgSend$setTitleLineBreakMode:
+ _objc_msgSend$setTranslatesAutoresizingMaskIntoConstraints:
+ _objc_msgSend$setUseAltDSID:
+ _objc_msgSend$setUserInfo:
+ _objc_msgSend$setValue:forHTTPHeaderField:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$sharedApplication
+ _objc_msgSend$sharedCalendarEmail
+ _objc_msgSend$showController:
+ _objc_msgSend$showErrorForPresenter:withError:callback:
+ _objc_msgSend$signURLRequest:isUserInitiated:
+ _objc_msgSend$sizeToFit
+ _objc_msgSend$specifierAtIndexPath:
+ _objc_msgSend$specifierForDataclass:
+ _objc_msgSend$specifierForID:
+ _objc_msgSend$specifiers
+ _objc_msgSend$startAnimating
+ _objc_msgSend$startSpinner
+ _objc_msgSend$statusCode
+ _objc_msgSend$stopAnimating
+ _objc_msgSend$stopSpinner
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$table
+ _objc_msgSend$target
+ _objc_msgSend$toDictionary
+ _objc_msgSend$topAnchor
+ _objc_msgSend$trailingAnchor
+ _objc_msgSend$traitCollection
+ _objc_msgSend$udid
+ _objc_msgSend$uppercaseString
+ _objc_msgSend$urlString
+ _objc_msgSend$userInfo
+ _objc_msgSend$widthAnchor
+ _swift_bridgeObjectRetain
+ _symbolic $sSY
+ _symbolic $ss21_ObjectiveCBridgeableP
+ _symbolic SS
+ _symbolic So11PSTableCellC
+ _symbolic So8NSStringC
+ _symbolic _____ 22icloudCalendarSettings0B11PlacardCellC
+ _symbolic _____ 22icloudCalendarSettings19ResourceBundleClass33_AB55B1C9D62F009F4345535693AFCC67LLC
+ _symbolic _____ So38UIApplicationOpenExternalURLOptionsKeya
+ _symbolic ______ypt So38UIApplicationOpenExternalURLOptionsKeya
+ _symbolic _____y______pG s23_ContiguousArrayStorageC s7CVarArgP
+ _symbolic _____y_____y_____GG 8Settings0A11PlacardViewV 21_IconServices_SwiftUI05AsyncD5ImageV 0fG00I0V
+ _symbolic _____y_____y_____y_____GG_____G 7SwiftUI22UIHostingConfigurationV 8Settings0E11PlacardViewV 014_IconServices_aB005AsyncH5ImageV AA0K0V AA05EmptyG0V
+ _symbolic _____y_____ypG s18_DictionaryStorageC So38UIApplicationOpenExternalURLOptionsKeya
+ _type_layout_string So38UIApplicationOpenExternalURLOptionsKeya
+ icloudCalendarSettings_vers.c
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x25
- _objc_retain_x28
- _objc_retain_x3
- radr://5614542

```
