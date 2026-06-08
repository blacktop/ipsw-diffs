## CertInfo

> `/System/Library/PrivateFrameworks/CertInfo.framework/CertInfo`

```diff

-2052.100.2.0.0
-  __TEXT.__text: 0x1053c
-  __TEXT.__auth_stubs: 0x4a0
+2054.0.0.0.0
+  __TEXT.__text: 0xf2c8
   __TEXT.__objc_methlist: 0x19f8
-  __TEXT.__cstring: 0x5e2
+  __TEXT.__cstring: 0x601
   __TEXT.__const: 0x138
-  __TEXT.__unwind_info: 0x600
-  __TEXT.__objc_classname: 0x40a
-  __TEXT.__objc_methname: 0x3de9
-  __TEXT.__objc_methtype: 0xfb0
-  __TEXT.__objc_stubs: 0x29a0
-  __DATA_CONST.__got: 0x238
+  __TEXT.__unwind_info: 0x4a8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xf78
   __DATA_CONST.__objc_superrefs: 0xe8
-  __AUTH_CONST.__auth_got: 0x258
+  __DATA_CONST.__got: 0x238
   __AUTH_CONST.__cfstring: 0x840
   __AUTH_CONST.__objc_const: 0x3148
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x780
   __DATA.__objc_ivar: 0x1b0
   __DATA.__data: 0x1e8

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BDC58FA8-2F2C-375F-A339-177306909539
+  UUID: A867D2EF-60A5-39BD-94B7-48C584AEAAB9
   Functions: 424
-  Symbols:   1694
-  CStrings:  964
+  Symbols:   1702
+  CStrings:  140
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x1
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x27
+ _objc_retain_x4
+ _objc_retain_x6
+ _objc_retain_x7
+ _objc_retain_x8
Functions:
~ -[CertificateViewController init] : 176 -> 180
~ -[CertificateViewController initWithTrust:action:] : 192 -> 188
~ -[CertificateViewController dealloc] : 104 -> 100
~ -[CertificateViewController viewWillAppear:] : 96 -> 92
~ -[CertificateViewController viewDidDisappear:] : 108 -> 104
~ -[CertificateViewController setCertificateTitle:issuer:purpose:expiration:properties:isRoot:action:] : 252 -> 260
~ -[CertificateViewController setShowCertificateButton:localizedTitle:localizedDescription:destructive:handler:] : 244 -> 248
~ -[CertificateViewController tableView:titleForFooterInSection:] : 88 -> 84
~ -[CertificateViewController tableView:cellForRowAtIndexPath:] : 1004 -> 928
~ -[CertificateViewController tableView:didSelectRowAtIndexPath:] : 336 -> 328
~ -[CertificateViewController tableView:shouldHighlightRowAtIndexPath:] : 112 -> 108
~ -[CertificateViewController preferredContentSizeChanged:] : 68 -> 64
~ -[CertificateViewController certificateTrust] : 16 -> 20
~ -[CertificateViewController setCertificateTrust:] : 80 -> 20
~ -[CertificateViewController certUIAction] : 16 -> 20
~ -[CertificateViewController setCertUIAction:] : 16 -> 20
~ -[CertificateViewController certificateTitle] : 16 -> 20
~ -[CertificateViewController setCertificateTitle:] : 80 -> 20
~ -[CertificateViewController certificateIssuer] : 16 -> 20
~ -[CertificateViewController setCertificateIssuer:] : 80 -> 20
~ -[CertificateViewController certificatePurpose] : 16 -> 20
~ -[CertificateViewController setCertificatePurpose:] : 80 -> 20
~ -[CertificateViewController certificateExpiration] : 16 -> 20
~ -[CertificateViewController setCertificateExpiration:] : 80 -> 20
~ -[CertificateViewController certificateProperties] : 16 -> 20
~ -[CertificateViewController setCertificateProperties:] : 80 -> 20
~ -[CertificateViewController certificateIsRoot] : 16 -> 20
~ -[CertificateViewController setCertificateIsRoot:] : 16 -> 20
~ -[CertificateViewController showCertificateButton] : 16 -> 20
~ -[CertificateViewController setShowCertificateButton:] : 16 -> 20
~ -[CertificateViewController certificateButtonTitle] : 16 -> 20
~ -[CertificateViewController setCertificateButtonTitle:] : 80 -> 20
~ -[CertificateViewController certificateButtonDescription] : 16 -> 20
~ -[CertificateViewController setCertificateButtonDescription:] : 80 -> 20
~ -[CertificateViewController certificateButtonIsDestructiveAction] : 16 -> 20
~ -[CertificateViewController setCertificateButtonIsDestructiveAction:] : 16 -> 20
~ -[CertificateViewController certificateButtonActionHandler] : 16 -> 20
~ -[CertInfoTrustDetailsViewController loadView] : 152 -> 148
~ -[CertInfoTrustDetailsViewController _setupNavItem] : 164 -> 152
~ -[CertInfoTrustDetailsViewController trustProperties] : 16 -> 20
~ -[CertInfoTrustDetailsViewController setTrustProperties:] : 80 -> 20
~ -[CertInfoTrustDetailsView _appendRemainingCertificates] : 276 -> 288
~ -[CertInfoTrustDetailsView initWithFrame:trustProperties:] : 584 -> 580
~ -[CertInfoTrustDetailsView layoutSubviews] : 64 -> 68
~ -[CertUIKeyValueCell _setup] : 568 -> 556
~ -[CertUIKeyValueCell setValue:forKey:] : 460 -> 432
~ -[CertUIKeyValueCell sizeThatFits:] : 316 -> 296
~ -[CertUIKeyValueCell _setupConstraints] : 976 -> 916
~ -[CertUIKeyValueCell keyLabel] : 16 -> 20
~ -[CertUIKeyValueCell setKeyLabel:] : 80 -> 20
~ -[CertUIKeyValueCell valueLabel] : 16 -> 20
~ -[CertUIKeyValueCell setValueLabel:] : 80 -> 20
~ -[CertUIKeyValueCell constraints] : 16 -> 20
~ -[CertUIKeyValueCell setConstraints:] : 80 -> 20
~ +[CertUIKeyValueView defaultPreferredValueLabelOriginX] : 176 -> 168
~ -[CertUIKeyValueView layoutSubviews] : 1260 -> 1168
~ -[CertUIKeyValueView _createVerifiedComponentsIfNeeded] : 372 -> 360
~ -[CertUIKeyValueView sizeThatFits:] : 592 -> 568
~ -[CertUIKeyValueView setItemDetail:] : 340 -> 304
~ -[CertUIKeyValueView setKey:value:] : 148 -> 144
~ -[CertUIKeyValueView setHighlightTextColor:] : 148 -> 140
~ -[CertUIKeyValueView setCheckmarkLabelText:checkmarkLabelColor:showCheckmark:] : 340 -> 320
~ -[CertUIKeyValueView setPreferredValueLabelOriginX:] : 36 -> 40
~ -[CertUIKeyValueView titleFont] : 144 -> 132
~ -[CertUIKeyValueView detailFont] : 120 -> 112
~ -[CertUIKeyValueView verifiedFont] : 148 -> 132
~ -[CertUIKeyValueView preferredValueLabelOriginX] : 16 -> 20
~ -[CertUIKeyValueView keyLabel] : 16 -> 20
~ -[CertUIKeyValueView setKeyLabel:] : 80 -> 20
~ -[CertUIKeyValueView valueLabel] : 16 -> 20
~ -[CertUIKeyValueView setValueLabel:] : 80 -> 20
~ -[CertUIKeyValueView verifiedImageView] : 16 -> 20
~ -[CertUIKeyValueView setVerifiedImageView:] : 80 -> 20
~ -[CertUIKeyValueView verifiedLabel] : 16 -> 20
~ -[CertUIKeyValueView setVerifiedLabel:] : 80 -> 20
~ -[CertificateDetailsViewController initWithCertificate:] : 216 -> 208
~ -[CertificateDetailsViewController initWithCertificateProperties:] : 236 -> 220
~ -[CertificateDetailsViewController initWithTrust:] : 240 -> 228
~ -[CertificateDetailsViewController dealloc] : 104 -> 100
~ -[CertificateDetailsViewController _setup] : 376 -> 348
~ -[CertificateDetailsViewController setCertificateProperties:] : 232 -> 216
~ -[CertificateDetailsViewController numberOfSectionsInTableView:] : 60 -> 56
~ -[CertificateDetailsViewController tableView:numberOfRowsInSection:] : 160 -> 148
~ -[CertificateDetailsViewController tableView:titleForHeaderInSection:] : 152 -> 140
~ -[CertificateDetailsViewController tableView:cellForRowAtIndexPath:] : 344 -> 328
~ -[CertificateDetailsViewController preferredContentSizeChanged:] : 68 -> 64
~ -[CertificateDetailsViewController certificateTrust] : 16 -> 20
~ -[CertificateDetailsViewController setCertificateTrust:] : 80 -> 20
~ -[CertificateDetailsViewController keyValueSections] : 16 -> 20
~ -[CertificateDetailsViewController setKeyValueSections:] : 80 -> 20
~ -[CertificateDetailsViewController keyValueSectionTitles] : 16 -> 20
~ -[CertificateDetailsViewController setKeyValueSectionTitles:] : 80 -> 20
~ -[CertInfoSheetViewController _setupNavItem] : 320 -> 304
~ -[CertInfoSheetViewController _pushDetailsView] : 160 -> 152
~ -[CertInfoSheetViewController loadView] : 328 -> 312
~ -[CertInfoSheetViewController viewWillAppear:] : 176 -> 164
~ -[CertInfoSheetViewController viewDidDisappear:] : 108 -> 104
~ -[CertInfoSheetViewController serviceName] : 16 -> 20
~ -[CertInfoSheetViewController setServiceName:] : 80 -> 20
~ -[CertInfoSheetViewController trustTitle] : 16 -> 20
~ -[CertInfoSheetViewController setTrustTitle:] : 80 -> 20
~ -[CertInfoSheetViewController trustSubtitle] : 16 -> 20
~ -[CertInfoSheetViewController setTrustSubtitle:] : 80 -> 20
~ -[CertInfoSheetViewController trustPurpose] : 16 -> 20
~ -[CertInfoSheetViewController setTrustPurpose:] : 80 -> 20
~ -[CertInfoSheetViewController trustExpiration] : 16 -> 20
~ -[CertInfoSheetViewController setTrustExpiration:] : 80 -> 20
~ -[CertInfoSheetViewController trustProperties] : 16 -> 20
~ -[CertInfoSheetViewController setTrustProperties:] : 80 -> 20
~ -[CertUIItemSummaryCell _setupCell] : 648 -> 640
~ -[CertUIItemSummaryCell _profileImageAppropriateForDevice] : 220 -> 204
~ -[CertUIItemSummaryCell _setupConstraints] : 2424 -> 2152
~ -[CertUIItemSummaryCell cellHeight] : 160 -> 148
~ -[CertUIItemSummaryCell itemImageView] : 16 -> 20
~ -[CertUIItemSummaryCell setItemImageView:] : 80 -> 20
~ -[CertUIItemSummaryCell itemTitleView] : 16 -> 20
~ -[CertUIItemSummaryCell setItemTitleView:] : 80 -> 20
~ -[CertUIItemSummaryCell itemTitleLabel] : 16 -> 20
~ -[CertUIItemSummaryCell setItemTitleLabel:] : 80 -> 20
~ -[CertUIItemSummaryCell itemSubtitleLabel] : 16 -> 20
~ -[CertUIItemSummaryCell setItemSubtitleLabel:] : 80 -> 20
~ -[NSData(CertInfoAdditions) CertUIHexString] : 208 -> 204
~ ___44-[NSData(CertInfoAdditions) CertUIHexString]_block_invoke : 140 -> 144
~ -[CertInfoCertificateSummaryView initWithFrame:] : 244 -> 248
~ -[CertInfoCertificateSummaryView setMoreDetailsSelectedBlock:] : 136 -> 132
~ -[CertInfoCertificateSummaryView _cellForReuseIdentifier:] : 444 -> 440
~ -[CertInfoCertificateSummaryView _configureCell:] : 636 -> 584
~ -[CertInfoCertificateSummaryView tableView:cellForRowAtIndexPath:] : 232 -> 228
~ -[CertInfoCertificateSummaryView tableView:didSelectRowAtIndexPath:] : 176 -> 172
~ -[CertInfoCertificateSummaryView tableView] : 16 -> 20
~ -[CertInfoCertificateSummaryView trustTitle] : 16 -> 20
~ -[CertInfoCertificateSummaryView setTrustTitle:] : 80 -> 20
~ -[CertInfoCertificateSummaryView trustSubtitle] : 16 -> 20
~ -[CertInfoCertificateSummaryView setTrustSubtitle:] : 80 -> 20
~ -[CertInfoCertificateSummaryView purpose] : 16 -> 20
~ -[CertInfoCertificateSummaryView setPurpose:] : 80 -> 20
~ -[CertInfoCertificateSummaryView expirationDate] : 16 -> 20
~ -[CertInfoCertificateSummaryView setExpirationDate:] : 80 -> 20
~ -[CertInfoCertificateSummaryView headerCell] : 16 -> 20
~ -[CertInfoCertificateSummaryView setHeaderCell:] : 80 -> 20
~ -[CertInfoCertificateSummaryView descriptionCell] : 16 -> 20
~ -[CertInfoCertificateSummaryView setDescriptionCell:] : 80 -> 20
~ -[CertInfoGradientLabel dealloc] : 88 -> 92
~ -[CertInfoGradientLabel font] : 100 -> 84
~ -[CertInfoGradientLabel setGradient:] : 372 -> 380
~ -[CertInfoGradientLabel _patternColor] : 16 -> 20
~ -[CertInfoGradientLabel drawRect:] : 292 -> 284
~ -[CertInfoGradientLabel text] : 16 -> 20
~ -[CertInfoGradientLabel setText:] : 80 -> 20
~ -[CertInfoGradientLabel setFont:] : 80 -> 20
~ -[CertInfoGradientLabel gradient] : 16 -> 20
~ -[CertInfoCertificateHeaderCell initWithStyle:reuseIdentifier:] : 308 -> 284
~ -[CertInfoCertificateHeaderCell _certificateImage] : 252 -> 232
~ -[CertInfoCertificateHeaderCell _titleLabel] : 244 -> 232
~ -[CertInfoCertificateHeaderCell _subtitleLabel] : 288 -> 272
~ -[CertInfoCertificateHeaderCell _notTrustedGradient] : 128 -> 120
~ -[CertInfoCertificateHeaderCell _trustedLabel] : 272 -> 256
~ -[CertInfoCertificateHeaderCell setTrustTitle:] : 108 -> 104
~ -[CertInfoCertificateHeaderCell setTrustSubtitle:] : 108 -> 104
~ -[CertInfoCertificateHeaderCell setExpired:] : 136 -> 124
~ -[CertInfoCertificateHeaderCell rowHeight] : 80 -> 76
~ -[CertInfoCertificateHeaderCell layoutSubviews] : 748 -> 704
~ -[CertInfoCertificateDetailsView appendInfoFromCertView:] : 176 -> 172
~ -[CertInfoCertificateDetailsView _cellInfosForSection:] : 624 -> 596
~ -[CertInfoCertificateDetailsView _sectionInfoForCertSection:title:] : 168 -> 160
~ -[CertInfoCertificateDetailsView _sectionsFromProperties:] : 580 -> 556
~ -[CertInfoCertificateDetailsView initWithFrame:certificateProperties:] : 292 -> 296
~ -[CertInfoCertificateDetailsView layoutSubviews] : 64 -> 68
~ -[CertInfoCertificateDetailsView tableView:numberOfRowsInSection:] : 144 -> 140
~ -[CertInfoCertificateDetailsView _titleForIndexPath:] : 212 -> 196
~ -[CertInfoCertificateDetailsView _detailForIndexPath:] : 212 -> 196
~ -[CertInfoCertificateDetailsView tableView:cellForRowAtIndexPath:] : 328 -> 312
~ -[CertInfoCertificateDetailsView numberOfSectionsInTableView:] : 16 -> 20
~ -[CertInfoCertificateDetailsView tableView:titleForHeaderInSection:] : 148 -> 144
~ -[CertUIKeyDataCell _setup] : 568 -> 556
~ -[CertUIKeyDataCell setValue:forKey:] : 372 -> 344
~ -[CertUIKeyDataCell _setupConstraints] : 896 -> 836
~ -[CertUIKeyDataCell keyLabel] : 16 -> 20
~ -[CertUIKeyDataCell setKeyLabel:] : 80 -> 20
~ -[CertUIKeyDataCell valueLabel] : 16 -> 20
~ -[CertUIKeyDataCell setValueLabel:] : 80 -> 20
~ -[CertUIKeyDataCell constraints] : 16 -> 20
~ -[CertUIKeyDataCell setConstraints:] : 80 -> 20
~ -[CertificateSummaryTableViewCell updateWithCertificateTrust:] : 204 -> 196
~ -[CertificateSummaryTableViewCell setCertificateName:issuer:isRoot:] : 320 -> 300
~ -[CertInfoCertificateDetailsController initWithCertificateProperties:] : 288 -> 284
~ -[CertInfoCertificateDetailsController _sectionsForProperties:currentSectionDictionary:] : 852 -> 816
~ -[CertInfoCertificateDetailsController setShowsDoneButton:] : 244 -> 240
~ -[CertInfoCertificateDetailsController showsDoneButton] : 20 -> 24
~ -[CertInfoCertificateDetailsController _doneButtonPressed:] : 156 -> 148
~ -[CertInfoCertificateDetailsController numberOfSectionsInTableView:] : 16 -> 20
~ -[CertInfoCertificateDetailsController tableView:numberOfRowsInSection:] : 112 -> 108
~ -[CertInfoCertificateDetailsController tableView:titleForHeaderInSection:] : 108 -> 104
~ -[CertInfoCertificateDetailsController tableView:cellForRowAtIndexPath:] : 296 -> 272
~ __stringValueForPropertyDictionary : 564 -> 552
~ -[CertInfoCertificateDetailsController tableView:performAction:forRowAtIndexPath:withSender:] : 236 -> 232
~ -[CertInfoCertificateDetailsController _propertiesForIndexPath:] : 180 -> 168
~ -[CertUIItemDetailsSummaryCell initWithStyle:reuseIdentifier:] : 104 -> 108
~ -[CertUIItemDetailsSummaryCell layoutSubviews] : 428 -> 424
~ -[CertUIItemDetailsSummaryCell setDetailLabelOriginX:] : 296 -> 300
~ -[CertUIItemDetailsSummaryCell createViewWithDescriptors:] : 572 -> 564
~ -[CertUIItemDetailsSummaryCell createViewWithItemDetailArray:] : 604 -> 608
~ -[CertUIItemDetailsSummaryCell detailViews] : 16 -> 20
~ -[CertUIItemDetailsSummaryCell setDetailViews:] : 80 -> 20
~ -[CertUIItemDetailsSummaryCell detailLabelOriginX] : 16 -> 20
~ -[CertUICertificatePropertiesInfo initWithCertificate:] : 184 -> 180
~ -[CertUICertificatePropertiesInfo initWithCertificateProperties:] : 168 -> 160
~ -[CertUICertificatePropertiesInfo initWithSendableCertificateProperties:] : 140 -> 136
~ -[CertUICertificatePropertiesInfo initWithTrust:] : 176 -> 164
~ -[CertUICertificatePropertiesInfo _setup:] : 752 -> 732
~ -[CertUICertificatePropertiesInfo _cellInfosForSection:] : 668 -> 640
~ -[CertUICertificatePropertiesInfo _sectionInfoForCertSection:title:] : 168 -> 160
~ -[CertUICertificatePropertiesInfo _sectionsFromProperties:] : 580 -> 556
~ -[CertUICertificatePropertiesInfo _sendablePropertyFromProperty:] : 368 -> 340
~ -[CertUICertificatePropertiesInfo _sendablePropertiesFromProperties:] : 348 -> 340
~ -[CertUICertificatePropertiesInfo _sendablePropertiesFromTrust:] : 344 -> 340
~ -[CertUICertificatePropertiesInfo setSections:] : 64 -> 12
~ -[CertUICertificatePropertiesInfo setSectionTitles:] : 64 -> 12
~ -[CertInfoDescriptionCellContentView dealloc] : 88 -> 92
~ -[CertInfoDescriptionCellContentView _recalculateIdealHeight] : 516 -> 524
~ -[CertInfoDescriptionCellContentView setLabelsAndValues:] : 136 -> 124
~ -[CertInfoDescriptionCellContentView rowHeight] : 16 -> 20
~ -[CertInfoDescriptionCellContentView drawRect:] : 552 -> 544
~ -[CertInfoCertificateSummaryDescriptionCell setLabelsAndValues:] : 16 -> 20
~ -[CertInfoCertificateSummaryDescriptionCell rowHeight] : 16 -> 20
~ +[CertUIItemDetail itemDetailWithDetailTitle:detail:] : 140 -> 144
~ +[CertUIItemDetail itemDetailWithDetailTitle:detail:detailHighlightColor:] : 152 -> 160
~ +[CertUIItemDetail itemDetailWithDetailTitle:detail:detailHighlightColor:showCheckmarkView:checkmarkText:checkmarkHighlightColor:showCheckmark:] : 200 -> 216
~ -[CertUIItemDetail initWithDetailTitle:detail:detailHighlightColor:showCheckmarkView:checkmarkText:checkmarkHighlightColor:showCheckmark:] : 260 -> 292
~ -[CertUIItemDetail setDetailTitle:] : 64 -> 12
~ -[CertUIItemDetail setDetail:] : 64 -> 12
~ -[CertUIItemDetail setDetailHighlightColor:] : 64 -> 12
~ -[CertUIItemDetail setCheckmarkText:] : 64 -> 12
~ -[CertUIItemDetail setCheckmarkHighlightColor:] : 64 -> 12
~ -[CertInfoTrustSummaryController initWithTrustDescription:] : 272 -> 260
~ -[CertInfoTrustSummaryController setShowsDoneButton:] : 328 -> 324
~ -[CertInfoTrustSummaryController showsDoneButton] : 20 -> 24
~ -[CertInfoTrustSummaryController setActionButtonTitle:destructive:animated:] : 132 -> 128
~ -[CertInfoTrustSummaryController _doneButtonPressed:] : 156 -> 148
~ -[CertInfoTrustSummaryController _actionButtonPressed:] : 156 -> 148
~ -[CertInfoTrustSummaryController viewDidAppear:] : 140 -> 128
~ -[CertInfoTrustSummaryController tableView:cellForRowAtIndexPath:] : 200 -> 196
~ -[CertInfoTrustSummaryController tableView:didSelectRowAtIndexPath:] : 316 -> 304
~ -[CertInfoTrustSummaryController tableView:heightForRowAtIndexPath:] : 228 -> 220
~ -[CertInfoTrustSummaryController _cellForReuseIdentifier:] : 344 -> 320
~ -[CertInfoTrustSummaryController _headerCell] : 304 -> 292
~ -[CertInfoTrustSummaryController _descriptionCell] : 184 -> 180
~ -[_CertInfoTrustSummaryHeaderCell initWithStyle:reuseIdentifier:] : 312 -> 292
~ -[_CertInfoTrustSummaryHeaderCell actionButton] : 164 -> 156
~ -[_CertInfoTrustSummaryHeaderCell setTrustTitle:] : 108 -> 104
~ -[_CertInfoTrustSummaryHeaderCell trustTitle] : 84 -> 76
~ -[_CertInfoTrustSummaryHeaderCell setTrustSubtitle:] : 108 -> 104
~ -[_CertInfoTrustSummaryHeaderCell trustSubtitle] : 84 -> 76
~ -[_CertInfoTrustSummaryHeaderCell setExpired:] : 136 -> 124
~ -[_CertInfoTrustSummaryHeaderCell rowHeight] : 80 -> 76
~ -[_CertInfoTrustSummaryHeaderCell setActionButtonTitle:destructive:animated:] : 416 -> 412
~ -[_CertInfoTrustSummaryHeaderCell layoutSubviews] : 112 -> 108
~ -[_CertInfoTrustSummaryHeaderCell _layoutSubviewsWithActionButtonSize:] : 1236 -> 1196
~ -[_CertInfoTrustSummaryHeaderCell _titleLabel] : 244 -> 232
~ -[_CertInfoTrustSummaryHeaderCell _subtitleLabel] : 288 -> 272
~ -[_CertInfoTrustSummaryHeaderCell _trustedLabel] : 164 -> 160
~ -[_CertInfoTrustSummaryHeaderCell isTrusted] : 16 -> 20
~ -[_CertInfoTrustSummaryHeaderCell setTrusted:] : 16 -> 20
~ -[_CertInfoGradientLabel initWithTrusted:] : 684 -> 676
~ -[_CertInfoGradientLabel dealloc] : 88 -> 92
~ -[_CertInfoGradientLabel sizeThatFits:] : 132 -> 144
~ -[_CertInfoGradientLabel drawRect:] : 344 -> 360
~ -[_CertInfoActionButton initWithTitle:isDestructive:] : 464 -> 456
~ ___53-[_CertInfoActionButton initWithTitle:isDestructive:]_block_invoke : 388 -> 352
~ -[CertInfoCertificateListController initWithTrustDescription:] : 220 -> 212
~ -[CertInfoCertificateListController numberOfSectionsInTableView:] : 16 -> 20
~ -[CertInfoCertificateListController tableView:didSelectRowAtIndexPath:] : 168 -> 164
~ -[CertInfoCertificateListCellContentView initWithFrame:] : 312 -> 324
~ -[CertInfoCertificateListCellContentView setTitle:] : 20 -> 24
~ -[CertInfoCertificateListCellContentView setSubtitle:] : 264 -> 248
~ -[CertInfoCertificateListCellContentView setExpiration:] : 332 -> 312
~ -[CertInfoCertificateListCellContentView _setupLabel:isSubtitle:] : 256 -> 236
~ -[CertInfoCertificateListCellContentView _setText:forLabel:withRedColor:] : 184 -> 180
~ -[CertInfoCertificateListCellContentView layoutSubviews] : 796 -> 784
~ ___70-[CertInfoCertificateListTableViewCell initWithStyle:reuseIdentifier:]_block_invoke : 144 -> 136
~ -[CertInfoCertificateListTableViewCell updateWithTrustDescription:certificateIndex:] : 228 -> 212
~ -[CertInfoCertificateListTableViewCell layoutSubviews] : 400 -> 392
~ -[TrustCertificateViewController _setupNavItem] : 412 -> 392
~ -[TrustCertificateViewController setCertificateInfo:issuer:purpose:expiration:isRoot:properties:action:] : 204 -> 216
~ -[TrustCertificateViewController setShowCertificateButton:localizedTitle:localizedDescription:destructive:handler:] : 164 -> 168
~ -[TrustCertificateViewController allowCertificateTrust] : 16 -> 20
~ -[TrustCertificateViewController setAllowCertificateTrust:] : 16 -> 20
~ -[TrustCertificateViewController certificateViewController] : 16 -> 20
~ -[TrustCertificateViewController setCertificateViewController:] : 80 -> 20
~ -[CertificateDetailsSummaryCell setDetails:] : 140 -> 136
~ -[CertificateDetailsSummaryCell setDetailsWithCertificateTrust:certificateExpiration:certificateIsTrusted:] : 920 -> 872
~ -[CertificateDetailsSummaryCell details] : 16 -> 20
~ -[CertInfoBasicTrustDescription summaryDescriptionItems] : 304 -> 284
~ -[CertInfoCertificateDetailsController initWithTrust:certificateIndex:].cold.1 : 100 -> 96
~ -[CertInfoCertificateDetailsController initWithTrust:certificateIndex:].cold.2 : 100 -> 96
~ -[CertInfoCertificateDetailsController tableView:performAction:forRowAtIndexPath:withSender:].cold.1 : 100 -> 96
~ -[CertInfoTrustSummaryController initWithTrustDescription:].cold.1 : 120 -> 116
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"<CertInfoCertificateDetailsControllerDelegate>\""
- "@\"<CertInfoSheetViewControllerDelegate>\""
- "@\"<CertInfoTrustDescription>\""
- "@\"<CertInfoTrustSummaryControllerDelegate>\""
- "@\"<TrustCertificateViewControllerDelegate>\""
- "@\"CertInfoCertificateDetailsView\""
- "@\"CertInfoCertificateHeaderCell\""
- "@\"CertInfoCertificateListCellContentView\""
- "@\"CertInfoCertificateSummaryDescriptionCell\""
- "@\"CertInfoDescriptionCellContentView\""
- "@\"CertInfoGradientLabel\""
- "@\"CertificateViewController\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSArray\"24@0:8@\"UITableView\"16"
- "@\"NSArray\"24@0:8Q16"
- "@\"NSArray\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSDate\""
- "@\"NSDate\"24@0:8Q16"
- "@\"NSIndexPath\"24@0:8@\"UITableView\"16"
- "@\"NSIndexPath\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSIndexPath\"40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "@\"NSMutableArray\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8Q16"
- "@\"NSString\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSString\"32@0:8@\"UITableView\"16q24"
- "@\"UIBarButtonItem\""
- "@\"UIColor\""
- "@\"UIContextMenuConfiguration\"48@0:8@\"UITableView\"16@\"NSIndexPath\"24{CGPoint=dd}32"
- "@\"UIFont\""
- "@\"UIImage\""
- "@\"UIImageView\""
- "@\"UILabel\""
- "@\"UISwipeActionsConfiguration\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"UITableView\""
- "@\"UITableViewCell\""
- "@\"UITableViewCell\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"UITargetedPreview\"32@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24"
- "@\"UIView\""
- "@\"UIView\"24@0:8@\"UIScrollView\"16"
- "@\"UIView\"32@0:8@\"UITableView\"16q24"
- "@\"_CertInfoActionButton\""
- "@\"_CertInfoGradientLabel\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{__SecCertificate=}16"
- "@24@0:8^{__SecTrust=}16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@28@0:8^{__SecTrust=}16i24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16q24"
- "@32@0:8^{__SecTrust=}16q24"
- "@32@0:8q16@24"
- "@36@0:8^{__SecTrust=}16i24@28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8^{__SecTrust=}16i24@28B36"
- "@48@0:8@16@24{CGPoint=dd}32"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48"
- "@64@0:8@16@24@32B40@44@52B60"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"UIScrollView\"16"
- "B24@0:8@16"
- "B24@0:8q16"
- "B32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "B32@0:8@\"UITableView\"16@\"UITableViewFocusUpdateContext\"24"
- "B32@0:8@16@24"
- "B40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"<UISpringLoadedInteractionContext>\"32"
- "B40@0:8@16@24@32"
- "B48@0:8@\"UITableView\"16:24@\"NSIndexPath\"32@40"
- "B48@0:8@16:24@32@40"
- "CGImage"
- "CertInfoAdditions"
- "CertInfoBasicTrustDescription"
- "CertInfoCertificateDetailsController"
- "CertInfoCertificateDetailsView"
- "CertInfoCertificateHeaderCell"
- "CertInfoCertificateListCellContentView"
- "CertInfoCertificateListController"
- "CertInfoCertificateListTableViewCell"
- "CertInfoCertificateSummaryDescriptionCell"
- "CertInfoCertificateSummaryView"
- "CertInfoDescriptionCellContentView"
- "CertInfoGradientLabel"
- "CertInfoSheetViewController"
- "CertInfoTrustDescription"
- "CertInfoTrustDetailsView"
- "CertInfoTrustDetailsViewController"
- "CertInfoTrustSummaryController"
- "CertUIAdditions"
- "CertUICertificatePropertiesInfo"
- "CertUIHexString"
- "CertUIItemDetail"
- "CertUIItemDetailsSummaryCell"
- "CertUIItemSummaryCell"
- "CertUIKeyDataCell"
- "CertUIKeyValueCell"
- "CertUIKeyValueView"
- "CertUIVerifiedColor"
- "CertificateDetailsSummaryCell"
- "CertificateDetailsViewController"
- "CertificateSummaryTableViewCell"
- "CertificateViewController"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<CertInfoCertificateDetailsControllerDelegate>\",W,N,V_delegate"
- "T@\"<CertInfoSheetViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<CertInfoTrustSummaryControllerDelegate>\",W,N,V_delegate"
- "T@\"<TrustCertificateViewControllerDelegate>\",W,N,V_trustCertificateDelegate"
- "T@\"CertInfoCertificateHeaderCell\",&,N,V_headerCell"
- "T@\"CertInfoCertificateSummaryDescriptionCell\",&,N,V_descriptionCell"
- "T@\"CertificateViewController\",&,N,V_certificateViewController"
- "T@\"NSArray\",&,N,V_certificateProperties"
- "T@\"NSArray\",&,N,V_constraints"
- "T@\"NSArray\",&,N,V_detailViews"
- "T@\"NSArray\",&,N,V_details"
- "T@\"NSArray\",&,N,V_keyValueSectionTitles"
- "T@\"NSArray\",&,N,V_keyValueSections"
- "T@\"NSArray\",&,N,V_sectionTitles"
- "T@\"NSArray\",&,N,V_sections"
- "T@\"NSArray\",&,N,V_trustProperties"
- "T@\"NSDate\",&,N,V_certificateExpiration"
- "T@\"NSDate\",&,N,V_expirationDate"
- "T@\"NSDate\",&,N,V_trustExpiration"
- "T@\"NSString\",&,N,V_certificateButtonDescription"
- "T@\"NSString\",&,N,V_certificateButtonTitle"
- "T@\"NSString\",&,N,V_certificateIssuer"
- "T@\"NSString\",&,N,V_certificatePurpose"
- "T@\"NSString\",&,N,V_certificateTitle"
- "T@\"NSString\",&,N,V_checkmarkText"
- "T@\"NSString\",&,N,V_detail"
- "T@\"NSString\",&,N,V_detailTitle"
- "T@\"NSString\",&,N,V_purpose"
- "T@\"NSString\",&,N,V_serviceName"
- "T@\"NSString\",&,N,V_text"
- "T@\"NSString\",&,N,V_trustPurpose"
- "T@\"NSString\",&,N,V_trustSubtitle"
- "T@\"NSString\",&,N,V_trustTitle"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N"
- "T@\"NSString\",R,C"
- "T@\"UIColor\",&,N,V_checkmarkHighlightColor"
- "T@\"UIColor\",&,N,V_detailHighlightColor"
- "T@\"UIFont\",&,N,V_font"
- "T@\"UIImage\",&,N,V_gradient"
- "T@\"UIImageView\",&,N,V_itemImageView"
- "T@\"UIImageView\",&,N,V_verifiedImageView"
- "T@\"UILabel\",&,N,V_itemSubtitleLabel"
- "T@\"UILabel\",&,N,V_itemTitleLabel"
- "T@\"UILabel\",&,N,V_keyLabel"
- "T@\"UILabel\",&,N,V_valueLabel"
- "T@\"UILabel\",&,N,V_verifiedLabel"
- "T@\"UITableView\",R,N,V_tableView"
- "T@\"UIView\",&,N,V_itemTitleView"
- "T@\"_CertInfoActionButton\",R,W,N"
- "T@,&,N,V_certificateTrust"
- "T@?,C,N,V_certificateButtonActionHandler"
- "TB,D,N"
- "TB,N"
- "TB,N,GisTrusted,V_trusted"
- "TB,N,V_allowCertificateTrust"
- "TB,N,V_certificateButtonIsDestructiveAction"
- "TB,N,V_certificateIsRoot"
- "TB,N,V_showCertificateButton"
- "TB,N,V_showCheckmark"
- "TB,N,V_showCheckmarkView"
- "TQ,R"
- "Td,N,V_detailLabelOriginX"
- "Td,N,V_preferredValueLabelOriginX"
- "Td,R,N"
- "Ti,N,V_certUIAction"
- "TrustCertificateViewController"
- "UIScrollViewDelegate"
- "UITableViewDataSource"
- "UITableViewDelegate"
- "Vv16@0:8"
- "^{CGColor=}"
- "^{CGColor=}16@0:8"
- "^{CGSize=dd}"
- "^{_NSZone=}16@0:8"
- "^{__SecTrust=}"
- "_CertInfoActionButton"
- "_CertInfoGradientLabel"
- "_CertInfoTrustSummaryHeaderCell"
- "_accept"
- "_action"
- "_actionButton"
- "_actionButtonPressed:"
- "_allowCertificateTrust"
- "_appendRemainingCertificates"
- "_applicationIconImageForFormat:precomposed:scale:"
- "_cancel"
- "_cellForReuseIdentifier:"
- "_cellInfosForSection:"
- "_certUIAction"
- "_certificateButtonActionHandler"
- "_certificateButtonDescription"
- "_certificateButtonIsDestructiveAction"
- "_certificateButtonTitle"
- "_certificateContentView"
- "_certificateExpiration"
- "_certificateImage"
- "_certificateIsRoot"
- "_certificateIssuer"
- "_certificateProperties"
- "_certificatePurpose"
- "_certificateTitle"
- "_certificateTrust"
- "_certificateViewController"
- "_certificateViews"
- "_checkImage"
- "_checkmarkHighlightColor"
- "_checkmarkText"
- "_configureCell:"
- "_constraints"
- "_copyPropertiesFromTrust:"
- "_createVerifiedComponentsIfNeeded"
- "_currentCertView"
- "_customContentView"
- "_delegate"
- "_description"
- "_descriptionCell"
- "_detail"
- "_detailForIndexPath:"
- "_detailHighlightColor"
- "_detailLabelOriginX"
- "_detailTitle"
- "_detailViews"
- "_details"
- "_dismissWithResult:"
- "_doneButton"
- "_doneButtonPressed:"
- "_expirationDate"
- "_expirationLabel"
- "_firstLineBaselineFrameOriginY"
- "_firstLineBaselineOffsetFromBoundsTop"
- "_font"
- "_gradient"
- "_headerCell"
- "_idealHeight"
- "_itemImageView"
- "_itemSubtitleLabel"
- "_itemTitleLabel"
- "_itemTitleView"
- "_keyLabel"
- "_keyValueSectionTitles"
- "_keyValueSections"
- "_labelFont"
- "_labelsAndValues"
- "_layoutSubviewsWithActionButtonSize:"
- "_legacy_drawAtPoint:withFont:"
- "_legacy_drawInRect:withFont:lineBreakMode:"
- "_legacy_sizeWithFont:"
- "_legacy_sizeWithFont:constrainedToSize:"
- "_legacy_sizeWithFont:constrainedToSize:lineBreakMode:"
- "_legacy_sizeWithFont:forWidth:lineBreakMode:"
- "_moreDetailsSelectedBlock"
- "_notTrustedGradient"
- "_patternColor"
- "_preferredValueLabelOriginX"
- "_profileImageAppropriateForDevice"
- "_propertiesForIndexPath:"
- "_purpose"
- "_pushDetailsView"
- "_recalculateIdealHeight"
- "_sectionDictionaries"
- "_sectionInfoForCertSection:title:"
- "_sectionTitles"
- "_sections"
- "_sectionsForProperties:"
- "_sectionsForProperties:currentSectionDictionary:"
- "_sectionsFromProperties:"
- "_sendablePropertiesFromProperties:"
- "_sendablePropertiesFromTrust:"
- "_sendablePropertyFromProperty:"
- "_serviceName"
- "_setText:forLabel:withRedColor:"
- "_setup"
- "_setup:"
- "_setupCell"
- "_setupConstraints"
- "_setupLabel:isSubtitle:"
- "_setupNavItem"
- "_showCertificateButton"
- "_showCheckmark"
- "_showCheckmarkView"
- "_showsDoneButton"
- "_sizes"
- "_sizesCount"
- "_subtitleLabel"
- "_tableSections"
- "_tableView"
- "_text"
- "_titleForIndexPath:"
- "_titleLabel"
- "_trust"
- "_trustCertificateDelegate"
- "_trustExpiration"
- "_trustProperties"
- "_trustPurpose"
- "_trustSubtitle"
- "_trustTitle"
- "_trusted"
- "_trustedLabel"
- "_valueFont"
- "_valueLabel"
- "_verifiedImageView"
- "_verifiedLabel"
- "absoluteString"
- "actionButton"
- "addConstraint:"
- "addConstraints:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:selector:name:object:"
- "addSubview:"
- "addTarget:action:forControlEvents:"
- "allowCertificateTrust"
- "animateWithDuration:animations:completion:"
- "appendFormat:"
- "appendInfoFromCertView:"
- "appendString:"
- "array"
- "arrayWithCapacity:"
- "autorelease"
- "b1"
- "boldSystemFontOfSize:"
- "bounds"
- "bundleForClass:"
- "bundleWithIdentifier:"
- "bytes"
- "cellHeight"
- "certUIAction"
- "certificateButtonActionHandler"
- "certificateButtonDescription"
- "certificateButtonIsDestructiveAction"
- "certificateButtonTitle"
- "certificateCount"
- "certificateDetailsControllerDidFinish:"
- "certificateExpiration"
- "certificateExpirationDateAtIndex:"
- "certificateIsRoot"
- "certificateIssuer"
- "certificateIssuerSummaryAtIndex:"
- "certificateProperties"
- "certificatePropertiesAtIndex:"
- "certificatePurpose"
- "certificateSubjectSummaryAtIndex:"
- "certificateTitle"
- "certificateTrust"
- "certificateViewController"
- "checkmarkHighlightColor"
- "checkmarkText"
- "class"
- "colorWithRed:green:blue:alpha:"
- "componentsJoinedByString:"
- "conformsToProtocol:"
- "constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:"
- "constraints"
- "contentView"
- "copy"
- "copy:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createViewWithDescriptors:"
- "createViewWithItemDetailArray:"
- "currentDevice"
- "currentHandler"
- "currentLocale"
- "d"
- "d16@0:8"
- "d32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "d32@0:8@\"UITableView\"16q24"
- "d32@0:8@16@24"
- "d32@0:8@16q24"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "defaultPreferredValueLabelOriginX"
- "delegate"
- "dequeueReusableCellWithIdentifier:"
- "dequeueReusableCellWithIdentifier:forIndexPath:"
- "description"
- "descriptionCell"
- "deselectRowAtIndexPath:animated:"
- "detail"
- "detailFont"
- "detailHighlightColor"
- "detailLabelOriginX"
- "detailTextLabel"
- "detailTitle"
- "detailViews"
- "details"
- "dictionary"
- "dictionaryWithDictionary:"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjectsAndKeys:"
- "didReceiveMemoryWarning"
- "drawAtPoint:"
- "drawRect:"
- "enumerateByteRangesUsingBlock:"
- "expirationDate"
- "firstObject"
- "font"
- "fontDescriptor"
- "fontDescriptorWithSymbolicTraits:"
- "fontWithDescriptor:size:"
- "frame"
- "generalPasteboard"
- "gradient"
- "grayColor"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hash"
- "headerCell"
- "i"
- "i16@0:8"
- "image"
- "imageNamed:inBundle:"
- "imageView"
- "imageWithRenderingMode:"
- "indexPathForPreferredFocusedViewInTableView:"
- "indexPathForSelectedRow"
- "init"
- "initWithBarButtonSystemItem:target:action:"
- "initWithCapacity:"
- "initWithCertificate:"
- "initWithCertificateProperties:"
- "initWithDetailTitle:detail:detailHighlightColor:showCheckmarkView:checkmarkText:checkmarkHighlightColor:showCheckmark:"
- "initWithFrame:"
- "initWithFrame:certificateProperties:"
- "initWithFrame:style:"
- "initWithFrame:trustProperties:"
- "initWithImage:"
- "initWithNibName:bundle:"
- "initWithObjectsAndKeys:"
- "initWithRootViewController:"
- "initWithSendableCertificateProperties:"
- "initWithStyle:"
- "initWithStyle:reuseIdentifier:"
- "initWithTitle:isDestructive:"
- "initWithTitle:style:target:action:"
- "initWithTrust:"
- "initWithTrust:action:"
- "initWithTrust:action:delegate:"
- "initWithTrust:action:delegate:allowTrust:"
- "initWithTrust:certificateIndex:"
- "initWithTrustCertificateDelegate:"
- "initWithTrustCertificateDelegate:allowTrust:"
- "initWithTrustDescription:"
- "initWithTrusted:"
- "isEqual:"
- "isEqualToString:"
- "isHidden"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isRootCertificate"
- "isTrusted"
- "itemDetailWithDetailTitle:detail:"
- "itemDetailWithDetailTitle:detail:detailHighlightColor:"
- "itemDetailWithDetailTitle:detail:detailHighlightColor:showCheckmarkView:checkmarkText:checkmarkHighlightColor:showCheckmark:"
- "itemImageView"
- "itemSubtitleLabel"
- "itemTitleLabel"
- "itemTitleView"
- "keyLabel"
- "keyValueSectionTitles"
- "keyValueSections"
- "layoutSubviews"
- "length"
- "lineBreakMode"
- "loadView"
- "localizedStringForKey:value:table:"
- "localizedStringFromDate:dateStyle:timeStyle:"
- "mainScreen"
- "mutableCopy"
- "navigationController"
- "navigationItem"
- "numberOfSectionsInTableView:"
- "objectAtIndex:"
- "objectForKey:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "postNotificationName:object:"
- "preferredContentSizeChanged:"
- "preferredFontDescriptorWithTextStyle:"
- "preferredFontForTextStyle:"
- "preferredValueLabelOriginX"
- "purpose"
- "pushViewController:animated:"
- "q24@0:8@\"UITableView\"16"
- "q24@0:8@16"
- "q32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "q32@0:8@\"UITableView\"16q24"
- "q32@0:8@16@24"
- "q32@0:8@16q24"
- "q40@0:8@\"UITableView\"16@\"NSString\"24q32"
- "q40@0:8@16@24q32"
- "redColor"
- "registerClass:forCellReuseIdentifier:"
- "release"
- "reloadData"
- "removeConstraints:"
- "removeFromSuperview"
- "removeObserver:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "reuseIdentifier"
- "rightBarButtonItem"
- "row"
- "rowHeight"
- "scale"
- "scrollViewDidChangeAdjustedContentInset:"
- "scrollViewDidEndDecelerating:"
- "scrollViewDidEndDragging:willDecelerate:"
- "scrollViewDidEndScrollingAnimation:"
- "scrollViewDidEndZooming:withView:atScale:"
- "scrollViewDidScroll:"
- "scrollViewDidScrollToTop:"
- "scrollViewDidZoom:"
- "scrollViewShouldScrollToTop:"
- "scrollViewWillBeginDecelerating:"
- "scrollViewWillBeginDragging:"
- "scrollViewWillBeginZooming:withView:"
- "scrollViewWillEndDragging:withVelocity:targetContentOffset:"
- "sectionIndexTitlesForTableView:"
- "sectionTitles"
- "sections"
- "self"
- "serviceName"
- "setAccessoryType:"
- "setActionButtonTitle:destructive:animated:"
- "setAllowCertificateTrust:"
- "setAllowsSelection:"
- "setAutoresizesSubviews:"
- "setAutoresizingMask:"
- "setBackgroundColor:"
- "setBackgroundImage:forState:"
- "setCellLayoutMarginsFollowReadableWidth:"
- "setCertUIAction:"
- "setCertificateButtonActionHandler:"
- "setCertificateButtonDescription:"
- "setCertificateButtonIsDestructiveAction:"
- "setCertificateButtonTitle:"
- "setCertificateExpiration:"
- "setCertificateInfo:issuer:purpose:expiration:isRoot:properties:action:"
- "setCertificateIsRoot:"
- "setCertificateIssuer:"
- "setCertificateName:issuer:isRoot:"
- "setCertificateProperties:"
- "setCertificatePurpose:"
- "setCertificateTitle:"
- "setCertificateTitle:issuer:purpose:expiration:properties:isRoot:action:"
- "setCertificateTrust:"
- "setCertificateTrust:certificateExpiration:certificateIsTrusted:"
- "setCertificateViewController:"
- "setCheckmarkHighlightColor:"
- "setCheckmarkLabelText:checkmarkLabelColor:showCheckmark:"
- "setCheckmarkText:"
- "setClipsToBounds:"
- "setConstraints:"
- "setContentCompressionResistancePriority:forAxis:"
- "setContentEdgeInsets:"
- "setContentHuggingPriority:forAxis:"
- "setDataSource:"
- "setDateStyle:"
- "setDelegate:"
- "setDescriptionCell:"
- "setDetail:"
- "setDetailHighlightColor:"
- "setDetailLabelOriginX:"
- "setDetailTitle:"
- "setDetailViews:"
- "setDetails:"
- "setDetailsWithCertificateTrust:certificateExpiration:certificateIsTrusted:"
- "setExpiration:"
- "setExpirationDate:"
- "setExpired:"
- "setFont:"
- "setFrame:"
- "setGradient:"
- "setHeaderCell:"
- "setHidden:"
- "setHighlightTextColor:"
- "setHighlightedTextColor:"
- "setImage:"
- "setItemDetail:"
- "setItemImageView:"
- "setItemSubtitleLabel:"
- "setItemTitleLabel:"
- "setItemTitleView:"
- "setKey:value:"
- "setKeyLabel:"
- "setKeyValueSectionTitles:"
- "setKeyValueSections:"
- "setLabelsAndValues:"
- "setLeftBarButtonItem:"
- "setLocale:"
- "setMoreDetailsSelectedBlock:"
- "setNeedsDisplay"
- "setNeedsLayout"
- "setNumberOfLines:"
- "setObject:forKey:"
- "setOpaque:"
- "setPreferredValueLabelOriginX:"
- "setPriority:"
- "setPurpose:"
- "setRightBarButtonItem:"
- "setSectionTitles:"
- "setSections:"
- "setSelected:animated:"
- "setSelectionStyle:"
- "setSeparatorInset:"
- "setServiceName:"
- "setShadowColor:"
- "setShadowOffset:"
- "setShowCertificateButton:"
- "setShowCertificateButton:localizedTitle:localizedDescription:destructive:handler:"
- "setShowCheckmark:"
- "setShowCheckmarkView:"
- "setShowsDoneButton:"
- "setString:"
- "setSubtitle:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setTimeStyle:"
- "setTintColor:"
- "setTitle:"
- "setTitle:destructive:"
- "setTitle:forState:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setTrustCertificateDelegate:"
- "setTrustExpiration:"
- "setTrustProperties:"
- "setTrustPurpose:"
- "setTrustSubtitle:"
- "setTrustTitle:"
- "setTrusted:"
- "setUserInteractionEnabled:"
- "setValue:forKey:"
- "setValueLabel:"
- "setVerifiedImageView:"
- "setVerifiedLabel:"
- "setView:"
- "sheetViewController:finishedWithReturnCode:"
- "shouldAutorotateToInterfaceOrientation:"
- "showCertificateButton"
- "showCheckmark"
- "showCheckmarkView"
- "showsDoneButton"
- "size"
- "sizeThatFits:"
- "sizeToFit"
- "stretchableImageWithLeftCapWidth:topCapHeight:"
- "stringFromDate:"
- "stringWithCapacity:"
- "stringWithFormat:"
- "summaryDescriptionItems"
- "summarySubtitle"
- "summaryTitle"
- "superclass"
- "superview"
- "systemBlueColor"
- "systemFontOfSize:"
- "systemGrayColor"
- "systemRedColor"
- "tableView"
- "tableView:accessoryButtonTappedForRowWithIndexPath:"
- "tableView:accessoryTypeForRowWithIndexPath:"
- "tableView:canEditRowAtIndexPath:"
- "tableView:canFocusRowAtIndexPath:"
- "tableView:canMoveRowAtIndexPath:"
- "tableView:canPerformAction:forRowAtIndexPath:withSender:"
- "tableView:canPerformPrimaryActionForRowAtIndexPath:"
- "tableView:cellForRowAtIndexPath:"
- "tableView:commitEditingStyle:forRowAtIndexPath:"
- "tableView:contextMenuConfigurationForRowAtIndexPath:point:"
- "tableView:didBeginMultipleSelectionInteractionAtIndexPath:"
- "tableView:didDeselectRowAtIndexPath:"
- "tableView:didEndDisplayingCell:forRowAtIndexPath:"
- "tableView:didEndDisplayingFooterView:forSection:"
- "tableView:didEndDisplayingHeaderView:forSection:"
- "tableView:didEndEditingRowAtIndexPath:"
- "tableView:didHighlightRowAtIndexPath:"
- "tableView:didSelectRowAtIndexPath:"
- "tableView:didUnhighlightRowAtIndexPath:"
- "tableView:didUpdateFocusInContext:withAnimationCoordinator:"
- "tableView:editActionsForRowAtIndexPath:"
- "tableView:editingStyleForRowAtIndexPath:"
- "tableView:estimatedHeightForFooterInSection:"
- "tableView:estimatedHeightForHeaderInSection:"
- "tableView:estimatedHeightForRowAtIndexPath:"
- "tableView:heightForFooterInSection:"
- "tableView:heightForHeaderInSection:"
- "tableView:heightForRowAtIndexPath:"
- "tableView:indentationLevelForRowAtIndexPath:"
- "tableView:leadingSwipeActionsConfigurationForRowAtIndexPath:"
- "tableView:moveRowAtIndexPath:toIndexPath:"
- "tableView:numberOfRowsInSection:"
- "tableView:performAction:forRowAtIndexPath:withSender:"
- "tableView:performPrimaryActionForRowAtIndexPath:"
- "tableView:previewForDismissingContextMenuWithConfiguration:"
- "tableView:previewForHighlightingContextMenuWithConfiguration:"
- "tableView:sectionForSectionIndexTitle:atIndex:"
- "tableView:selectionFollowsFocusForRowAtIndexPath:"
- "tableView:shouldBeginMultipleSelectionInteractionAtIndexPath:"
- "tableView:shouldHighlightRowAtIndexPath:"
- "tableView:shouldIndentWhileEditingRowAtIndexPath:"
- "tableView:shouldShowMenuForRowAtIndexPath:"
- "tableView:shouldSpringLoadRowAtIndexPath:withContext:"
- "tableView:shouldUpdateFocusInContext:"
- "tableView:targetIndexPathForMoveFromRowAtIndexPath:toProposedIndexPath:"
- "tableView:titleForDeleteConfirmationButtonForRowAtIndexPath:"
- "tableView:titleForFooterInSection:"
- "tableView:titleForHeaderInSection:"
- "tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:"
- "tableView:viewForFooterInSection:"
- "tableView:viewForHeaderInSection:"
- "tableView:willBeginEditingRowAtIndexPath:"
- "tableView:willDeselectRowAtIndexPath:"
- "tableView:willDisplayCell:forRowAtIndexPath:"
- "tableView:willDisplayContextMenuWithConfiguration:animator:"
- "tableView:willDisplayFooterView:forSection:"
- "tableView:willDisplayHeaderView:forSection:"
- "tableView:willEndContextMenuInteractionWithConfiguration:animator:"
- "tableView:willPerformPreviewActionForMenuWithConfiguration:animator:"
- "tableView:willSelectRowAtIndexPath:"
- "tableViewDidEndMultipleSelectionInteraction:"
- "text"
- "textLabel"
- "timeIntervalSinceNow"
- "titleFont"
- "titleLabel"
- "titleOriginX"
- "trustCertificateDelegate"
- "trustCertificateViewController:finishedWithReturnCode:"
- "trustExpiration"
- "trustProperties"
- "trustPurpose"
- "trustSubtitle"
- "trustSummaryControllerDidFinish:"
- "trustSummaryControllerPerformAction:"
- "trustTitle"
- "trusted"
- "updateConstraintsIfNeeded"
- "updateWithCertificateTrust:"
- "updateWithTrustDescription:certificateIndex:"
- "userInterfaceIdiom"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"UIScrollView\"16"
- "v24@0:8@\"UITableView\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8B16B20"
- "v24@0:8^{__SecTrust=}16"
- "v24@0:8d16"
- "v28@0:8@\"UIScrollView\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"UIScrollView\"16@\"UIView\"24"
- "v32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "v32@0:8@16@24"
- "v32@0:8@16B24B28"
- "v32@0:8@16Q24"
- "v32@0:8{CGSize=dd}16"
- "v36@0:8@16@24B32"
- "v36@0:8^{__SecTrust=}16@24B32"
- "v40@0:8@\"UIScrollView\"16@\"UIView\"24d32"
- "v40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionAnimating>\"32"
- "v40@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionCommitAnimating>\"32"
- "v40@0:8@\"UITableView\"16@\"UITableViewCell\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UITableView\"16@\"UITableViewFocusUpdateContext\"24@\"UIFocusAnimationCoordinator\"32"
- "v40@0:8@\"UITableView\"16@\"UIView\"24q32"
- "v40@0:8@\"UITableView\"16q24@\"NSIndexPath\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24d32"
- "v40@0:8@16@24q32"
- "v40@0:8@16q24@32"
- "v48@0:8@\"UIScrollView\"16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8@\"UITableView\"16:24@\"NSIndexPath\"32@40"
- "v48@0:8@16:24@32@40"
- "v48@0:8@16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8B16@20@28B36@?40"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v64@0:8@16@24@32@40@48B56i60"
- "v64@0:8@16@24@32@40B48@52i60"
- "valueLabel"
- "verifiedColor"
- "verifiedFont"
- "verifiedImageView"
- "verifiedLabel"
- "view"
- "viewDidAppear:"
- "viewDidDisappear:"
- "viewDidLoad"
- "viewForZoomingInScrollView:"
- "viewWillAppear:"
- "whiteColor"
- "zone"
- "{CGSize=dd}32@0:8{CGSize=dd}16"

```
