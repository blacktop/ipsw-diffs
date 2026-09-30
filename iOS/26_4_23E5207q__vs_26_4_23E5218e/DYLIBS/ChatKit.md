## ChatKit

> `/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit`

```diff

-1450.500.178.2.5
-  __TEXT.__text: 0xba379c
-  __TEXT.__auth_stubs: 0xc1c0
+1450.500.206.0.0
+  __TEXT.__text: 0xbaaa18
+  __TEXT.__auth_stubs: 0xc1e0
   __TEXT.__delay_helper: 0xcd0
-  __TEXT.__objc_methlist: 0x70354
-  __TEXT.__const: 0x3bac4
-  __TEXT.__gcc_except_tab: 0x24040
-  __TEXT.__cstring: 0x3bf31
-  __TEXT.__oslogstring: 0x4d313
+  __TEXT.__objc_methlist: 0x7038c
+  __TEXT.__const: 0x3bc54
+  __TEXT.__gcc_except_tab: 0x24120
+  __TEXT.__cstring: 0x3c1f1
+  __TEXT.__oslogstring: 0x4d6a3
   __TEXT.__dlopen_cstrs: 0xb55
   __TEXT.__ustring: 0x1c4
-  __TEXT.__swift5_typeref: 0x3ff64
-  __TEXT.__constg_swiftt: 0x1bc2c
+  __TEXT.__swift5_typeref: 0x401b4
+  __TEXT.__constg_swiftt: 0x1bca4
   __TEXT.__swift5_builtin: 0x820
-  __TEXT.__swift5_reflstr: 0x10b21
-  __TEXT.__swift5_fieldmd: 0xf2f8
+  __TEXT.__swift5_reflstr: 0x10c61
+  __TEXT.__swift5_fieldmd: 0xf3c4
   __TEXT.__swift5_assocty: 0x42b0
-  __TEXT.__swift5_capture: 0x7948
+  __TEXT.__swift5_capture: 0x79cc
   __TEXT.__swift5_proto: 0x1860
-  __TEXT.__swift5_types: 0x129c
-  __TEXT.__swift_as_entry: 0x470
-  __TEXT.__swift_as_ret: 0x418
+  __TEXT.__swift5_types: 0x12a8
+  __TEXT.__swift_as_entry: 0x480
+  __TEXT.__swift_as_ret: 0x428
   __TEXT.__swift5_protos: 0xd8
   __TEXT.__swift5_mpenum: 0xe8
-  __TEXT.__unwind_info: 0x31cd0
-  __TEXT.__eh_frame: 0xdc0c
+  __TEXT.__unwind_info: 0x31e08
+  __TEXT.__eh_frame: 0xddd4
   __TEXT.__objc_classname: 0x12586
-  __TEXT.__objc_methname: 0x11754a
-  __TEXT.__objc_methtype: 0x25706
-  __TEXT.__objc_stubs: 0xad460
-  __DATA_CONST.__got: 0x72c8
-  __DATA_CONST.__const: 0xecc8
+  __TEXT.__objc_methname: 0x11759a
+  __TEXT.__objc_methtype: 0x256f6
+  __TEXT.__objc_stubs: 0xad520
+  __DATA_CONST.__got: 0x72d0
+  __DATA_CONST.__const: 0xecd8
   __DATA_CONST.__objc_classlist: 0x2ef0
   __DATA_CONST.__objc_catlist: 0x548
   __DATA_CONST.__objc_protolist: 0x1340
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35a90
+  __DATA_CONST.__objc_selrefs: 0x35ab8
   __DATA_CONST.__objc_protorefs: 0x510
   __DATA_CONST.__objc_superrefs: 0x19e0
   __DATA_CONST.__objc_arraydata: 0xef0
-  __AUTH_CONST.__auth_got: 0x60f0
-  __AUTH_CONST.__const: 0x39dc8
-  __AUTH_CONST.__cfstring: 0x23e80
-  __AUTH_CONST.__objc_const: 0x99908
+  __AUTH_CONST.__auth_got: 0x6100
+  __AUTH_CONST.__const: 0x39ff8
+  __AUTH_CONST.__cfstring: 0x23f80
+  __AUTH_CONST.__objc_const: 0x99910
   __AUTH_CONST.__objc_arrayobj: 0xe28
   __AUTH_CONST.__objc_intobj: 0x1008
   __AUTH_CONST.__objc_doubleobj: 0x880
   __AUTH_CONST.__objc_floatobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH.__objc_data: 0x287b0
-  __AUTH.__data: 0x13cc8
-  __DATA.__objc_ivar: 0x48f8
-  __DATA.__data: 0x1fa68
+  __AUTH.__data: 0x13d78
+  __DATA.__objc_ivar: 0x48fc
+  __DATA.__data: 0x1fb18
   __DATA.__objc_stublist: 0x38
-  __DATA.__bss: 0x3aa70
+  __DATA.__bss: 0x3aa80
   __DATA.__common: 0x1350
-  __DATA_DIRTY.__objc_data: 0x8780
+  __DATA_DIRTY.__objc_data: 0x8778
   __DATA_DIRTY.__data: 0x7a8
   __DATA_DIRTY.__bss: 0x16e0
   __DATA_DIRTY.__common: 0x50

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AA877CCC-71EF-3A2B-89E3-3DD5E13E644B
-  Functions: 70425
-  Symbols:   146507
-  CStrings:  59455
+  UUID: B489DD04-02D2-3BB0-9356-DE0BBCF7F19E
+  Functions: 70518
+  Symbols:   146570
+  CStrings:  59500
 
Symbols:
+ +[CKConversation conversationUpdaterLogHandle]
+ +[CKConversation conversationUpdaterLogHandle].cold.1
+ -[CKConversation _reloadTranscriptBackground]
+ -[CKConversation conversationUpdaterLogHandle]
+ -[CKConversation reasonTrackingUpdater:didBeginHoldingUpdatesWithInitialReason:]
+ -[CKConversation reasonTrackingUpdater:didEndHoldingUpdatesWithFinalReason:]
+ -[CKConversation reasonTrackingUpdater:needsUpdateForReasons:followingHoldForReason:]
+ -[CKCoreChatController customAcknowledgementDebouncer]
+ -[CKCoreChatController setCustomAcknowledgementDebouncer:]
+ -[CKCoreChatController transcriptCollectionViewController:balloonViewDidRequestSendCustomAcknowledgementPayload:forPlugin:error:].cold.1
+ -[CKCoreChatController transcriptCollectionViewController:balloonViewDidRequestSendCustomAcknowledgementPayload:forPlugin:error:].cold.2
+ -[CKCoreChatController transcriptCollectionViewController:balloonViewDidRequestSendCustomAcknowledgementPayload:forPlugin:error:].cold.3
+ -[CKCoreChatController transcriptCollectionViewController:balloonViewDidRequestSendCustomAcknowledgementPayload:forPlugin:error:].cold.4
+ -[CKCoreChatController transcriptCollectionViewController:balloonViewDidRequestSendCustomAcknowledgementPayload:forPlugin:error:].cold.5
+ -[CKCoreChatController transcriptCollectionViewController:balloonViewDidRequestSendCustomAcknowledgementPayload:forPlugin:error:].cold.6
+ -[CKMessageEntryView _updateLongPressAudioStopButtonHighlighted:]
+ -[CKMessageEntryView audioButtonLongPressed:].cold.1
+ -[CKMessageEntryView audioButtonTappedInEntryView:].cold.1
+ -[CKMessageEntryView dictationButtonTapped:].cold.1
+ -[CKMessageEntryView entryViewEmptyAction]
+ -[CKMessageEntryView entryViewEmptyAction].cold.1
+ -[CKMessageEntryView updateEntryView].cold.2
+ -[CKMessageEntryView updateEntryView].cold.3
+ GCC_except_table1000
+ GCC_except_table1006
+ GCC_except_table1010
+ GCC_except_table1017
+ GCC_except_table1023
+ GCC_except_table1027
+ GCC_except_table1050
+ GCC_except_table1053
+ GCC_except_table1060
+ GCC_except_table1067
+ GCC_except_table1098
+ GCC_except_table1100
+ GCC_except_table1123
+ GCC_except_table1128
+ GCC_except_table1130
+ GCC_except_table1175
+ GCC_except_table1177
+ GCC_except_table1179
+ GCC_except_table1181
+ GCC_except_table1184
+ GCC_except_table1189
+ GCC_except_table1191
+ GCC_except_table1194
+ GCC_except_table1196
+ GCC_except_table1204
+ GCC_except_table1222
+ GCC_except_table1233
+ GCC_except_table130
+ GCC_except_table1611
+ GCC_except_table1613
+ GCC_except_table1621
+ GCC_except_table1626
+ GCC_except_table1627
+ GCC_except_table1639
+ GCC_except_table194
+ GCC_except_table229
+ GCC_except_table233
+ GCC_except_table235
+ GCC_except_table243
+ GCC_except_table251
+ GCC_except_table268
+ GCC_except_table275
+ GCC_except_table279
+ GCC_except_table281
+ GCC_except_table287
+ GCC_except_table294
+ GCC_except_table343
+ GCC_except_table378
+ GCC_except_table390
+ GCC_except_table398
+ GCC_except_table401
+ GCC_except_table407
+ GCC_except_table410
+ GCC_except_table418
+ GCC_except_table439
+ GCC_except_table446
+ GCC_except_table454
+ GCC_except_table461
+ GCC_except_table465
+ GCC_except_table480
+ GCC_except_table496
+ GCC_except_table504
+ GCC_except_table521
+ GCC_except_table530
+ GCC_except_table556
+ GCC_except_table559
+ GCC_except_table578
+ GCC_except_table583
+ GCC_except_table587
+ GCC_except_table590
+ GCC_except_table620
+ GCC_except_table640
+ GCC_except_table655
+ GCC_except_table659
+ GCC_except_table661
+ GCC_except_table666
+ GCC_except_table670
+ GCC_except_table674
+ GCC_except_table679
+ GCC_except_table689
+ GCC_except_table694
+ GCC_except_table700
+ GCC_except_table703
+ GCC_except_table708
+ GCC_except_table722
+ GCC_except_table740
+ GCC_except_table745
+ GCC_except_table763
+ GCC_except_table768
+ GCC_except_table770
+ GCC_except_table775
+ GCC_except_table805
+ GCC_except_table807
+ GCC_except_table812
+ GCC_except_table833
+ GCC_except_table843
+ GCC_except_table849
+ GCC_except_table859
+ GCC_except_table870
+ GCC_except_table873
+ GCC_except_table875
+ GCC_except_table898
+ GCC_except_table901
+ GCC_except_table918
+ GCC_except_table921
+ GCC_except_table926
+ GCC_except_table934
+ GCC_except_table938
+ GCC_except_table947
+ GCC_except_table949
+ GCC_except_table953
+ GCC_except_table956
+ GCC_except_table961
+ GCC_except_table963
+ GCC_except_table966
+ GCC_except_table971
+ GCC_except_table975
+ GCC_except_table978
+ GCC_except_table981
+ GCC_except_table983
+ GCC_except_table988
+ GCC_except_table991
+ GCC_except_table994
+ _CKConversationTranscriptBackgroundHoldingUpdateReasonApplicationBackgrounded
+ _CKDefaultsKeyForceTranslationTipInNextConversation
+ _OBJC_IVAR_$_CKConversation._transcriptBackgroundUpdater
+ _OBJC_IVAR_$_CKCoreChatController._customAcknowledgementDebouncer
+ __CKEntryViewEmptyActionChangedNotification
+ __CKReadEntryViewEmptyActionFromPrefs
+ __OBJC_$_CLASS_METHODS_CKCoreChatController(Backgrounds|Background_Crossplatform|UserSafety|Nicknames|PinningInputViews|UltraConstrainedNetwork|CustomAcknowledgement|ChatKit|TapbackPicker|ChatKit1|ChatKit2)
+ __OBJC_$_INSTANCE_METHODS_CKChatController(MacToolbar|ClickyOrbConformance|CKChatController_Stickers|CKStickerDetailViewControllerDelegate|ChatItemSelection|Debug|ImpactEffectPicker|MenuBar|MessageHistoryViewController|MessageHistoryViewControllerDelegate|SendAnimation|QuickLook|CKNavBarUnifiedCallButton|Collaboration|GroupCollaboration|TipKit|SafetyMonitor|MediaInput|GlassThrowSendAnimation|PhotosSupport|Contacts|Wallet|Location|BackgroundContextMenu|BalloonEmphasis|NavigationBar|TapbackPicker|TapbackPicker_QuickLook|TapbackPicker_Orb|ChatKit|ChatKit1|TapbackPicker_ContextMenu|ChatKit2|ChatKit3|ChatKit4|ChatKit5|MenuBarKeyCommands|ChatKit6|ChatKit7|Translation|ChatKit8|ChatKit9|ChatKit10|ChatKit11)
+ __OBJC_$_INSTANCE_METHODS_CKCoreChatController(Backgrounds|Background_Crossplatform|UserSafety|Nicknames|PinningInputViews|UltraConstrainedNetwork|CustomAcknowledgement|ChatKit|TapbackPicker|ChatKit1|ChatKit2)
+ __OBJC_CLASS_PROTOCOLS_$_CKChatController(MacToolbar|ClickyOrbConformance|CKChatController_Stickers|CKStickerDetailViewControllerDelegate|ChatItemSelection|Debug|ImpactEffectPicker|MenuBar|MessageHistoryViewController|MessageHistoryViewControllerDelegate|SendAnimation|QuickLook|CKNavBarUnifiedCallButton|Collaboration|GroupCollaboration|TipKit|SafetyMonitor|MediaInput|GlassThrowSendAnimation|PhotosSupport|Contacts|Wallet|Location|BackgroundContextMenu|BalloonEmphasis|NavigationBar|TapbackPicker|TapbackPicker_QuickLook|TapbackPicker_Orb|ChatKit|ChatKit1|TapbackPicker_ContextMenu|ChatKit2|ChatKit3|ChatKit4|ChatKit5|MenuBarKeyCommands|ChatKit6|ChatKit7|Translation|ChatKit8|ChatKit9|ChatKit10|ChatKit11)
+ ___115-[CKChatController _presentCollabAddToMessagesGroupAlertIfNecessary:collaborationType:sendBlock:completionHandler:]_block_invoke.1406
+ ___145-[CKChatController _sendAutomaticallyPlacedSticker:stickerReactionSession:forChatItem:forParentChatItem:stickerFrame:animationCompletionHandler:]_block_invoke.1262
+ ___39-[CKChatController addToCollaboration:]_block_invoke.1631
+ ___39-[CKChatController addToCollaboration:]_block_invoke_2.1633
+ ___45-[CKChatController _handleChatItemDidChange:]_block_invoke.1608
+ ___46+[CKConversation conversationUpdaterLogHandle]_block_invoke
+ ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke.788
+ ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke.791
+ ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke_2.789
+ ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke_2.792
+ ___46-[CKMessageEntryView touchUpInsideSendButton:]_block_invoke
+ ___47-[CKChatController sendComposition:animations:]_block_invoke.881
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke.1537
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke.1541
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_2.1543
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_3.1547
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_4.1551
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_5.1552
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_6.1556
+ ___53-[CKChatController _showOrHideNicknameBannerIfNeeded]_block_invoke.1623
+ ___58-[CKChatController chatInputControllerDidSelectFunCamera:]_block_invoke.1258
+ ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke.1428
+ ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke.1431
+ ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke_2.1429
+ ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke_2.1433
+ ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1313
+ ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1314
+ ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1315
+ ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1315.cold.1
+ ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1316
+ ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1317
+ ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1318
+ ___67-[CKChatController _sendCompositionForNewCloudKitShare:completion:]_block_invoke.1377
+ ___68-[CKChatController verifyCompositionSendForFileProvider:completion:]_block_invoke.1308
+ ___68-[CKChatController verifyCompositionSendForFileProvider:completion:]_block_invoke.1310
+ ___69-[CKChatController nicknameBannerView:actionButtonTapped:forUpdates:]_block_invoke.1625
+ ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1387
+ ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1388
+ ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1389
+ ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1391
+ ___72-[CKChatController _verifyCompositionSendForNewFileProvider:completion:]_block_invoke.1343
+ ___72-[CKChatController _verifyCompositionSendForNewFileProvider:completion:]_block_invoke.1344
+ ___72-[CKChatController textPasteConfigurationSupporting:transformPasteItem:]_block_invoke.1672
+ ___73-[CKChatController _sendCompositionForFileProviderCloudDrive:completion:]_block_invoke.1346
+ ___73-[CKChatController _sendCompositionForFileProviderCloudDrive:completion:]_block_invoke.1347
+ ___76-[CKChatController _startSharingForURLForFileProviderCloudDrive:completion:]_block_invoke.1354
+ ___76-[CKChatController _startSharingForURLForFileProviderCloudDrive:completion:]_block_invoke.1355
+ ___77-[CKChatController selectedBalloonIntersectingRect:chatItemForRepositioning:]_block_invoke.1250
+ ___81-[CKChatController sendCompositionForCollaboration:collaborationType:completion:]_block_invoke.1394
+ ___81-[CKChatController sendCompositionForCollaboration:collaborationType:completion:]_block_invoke.1395
+ ___81-[CKChatController sendCompositionForCollaboration:collaborationType:completion:]_block_invoke_2.1396
+ ___86-[CKChatController _presentCollabAddToMessagesGroupAlert:sendBlock:completionHandler:]_block_invoke.1421
+ ___86-[CKChatController _presentCollabAddToMessagesGroupAlert:sendBlock:completionHandler:]_block_invoke.1422
+ ___87-[CKChatController _removeSubsharesAndSendFileProviderComposition:shareURL:completion:]_block_invoke.1368
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1362
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1362.cold.1
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1363
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1365
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1366
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke_2.1367
+ ___93-[CKChatController _sendCollaborationCompositionForFileProvider:sharingURL:share:completion:]_block_invoke.1330
+ ___93-[CKChatController _sendCollaborationCompositionForFileProvider:sharingURL:share:completion:]_block_invoke.1332
+ ___95-[CKChatController _updateAndSendCompositionForExistingCloudKitShare:share:attempt:completion:]_block_invoke.1385
+ ___Block_byref_object_copy_.1842
+ ___Block_byref_object_dispose_.1843
+ ____CKEntryViewEmptyActionChangedNotification_block_invoke
+ ____CKGetEntryViewEmptyActionPref_block_invoke
+ ___block_descriptor_64_e8_32s40s48s56w_e17_v16?0"NSTimer"8lw56l8s32l8s40l8s48l8
+ ___block_descriptor_73_e8_32s40s48s56s64r_e33_v36?0B8{CGSize=dd}12"NSError"28ls32l8r64l8s40l8s48l8s56l8
+ ___block_literal_global.1196
+ ___block_literal_global.1285
+ ___block_literal_global.1294
+ ___block_literal_global.1334
+ ___block_literal_global.1352
+ ___block_literal_global.1362
+ ___block_literal_global.1367
+ ___block_literal_global.1372
+ ___block_literal_global.1377
+ ___block_literal_global.1382
+ ___block_literal_global.1387
+ ___block_literal_global.1392
+ ___block_literal_global.1397
+ ___block_literal_global.1402
+ ___block_literal_global.1404
+ ___block_literal_global.1407
+ ___block_literal_global.1412
+ ___block_literal_global.1417
+ ___block_literal_global.1422
+ ___block_literal_global.1424
+ ___block_literal_global.1432
+ ___block_literal_global.1437
+ ___block_literal_global.1442
+ ___block_literal_global.1447
+ ___block_literal_global.1449
+ ___block_literal_global.1456
+ ___block_literal_global.1458
+ ___block_literal_global.1464
+ ___block_literal_global.1465
+ ___block_literal_global.1467
+ ___block_literal_global.1482
+ ___block_literal_global.1506
+ ___block_literal_global.1508
+ ___block_literal_global.1555
+ ___block_literal_global.1557
+ ___block_literal_global.1559
+ ___block_literal_global.1561
+ ___block_literal_global.1563
+ ___block_literal_global.1580
+ ___block_literal_global.1582
+ ___block_literal_global.1586
+ ___block_literal_global.1588
+ ___block_literal_global.1590
+ ___block_literal_global.1592
+ ___block_literal_global.1596
+ ___block_literal_global.1602
+ ___block_literal_global.1609
+ ___block_literal_global.1611
+ ___block_literal_global.1613
+ ___block_literal_global.1615
+ ___block_literal_global.1617
+ ___block_literal_global.1619
+ ___block_literal_global.1621
+ ___block_literal_global.1623
+ ___block_literal_global.1625
+ ___block_literal_global.1627
+ ___block_literal_global.1629
+ ___block_literal_global.1631
+ ___block_literal_global.1633
+ ___block_literal_global.1635
+ ___block_literal_global.1637
+ ___block_literal_global.1639
+ ___block_literal_global.1641
+ ___block_literal_global.1643
+ ___block_literal_global.1645
+ ___block_literal_global.1647
+ ___block_literal_global.1649
+ ___block_literal_global.1651
+ ___block_literal_global.1653
+ ___block_literal_global.1655
+ ___block_literal_global.1657
+ ___block_literal_global.1659
+ ___block_literal_global.1661
+ ___block_literal_global.1665
+ ___block_literal_global.1667
+ ___block_literal_global.1669
+ ___block_literal_global.1671
+ ___block_literal_global.1673
+ ___block_literal_global.1675
+ ___block_literal_global.1677
+ ___block_literal_global.1679
+ ___block_literal_global.1681
+ ___block_literal_global.1683
+ ___block_literal_global.1685
+ ___block_literal_global.1687
+ ___block_literal_global.1689
+ ___block_literal_global.1691
+ ___block_literal_global.1693
+ ___block_literal_global.1695
+ ___block_literal_global.1697
+ ___block_literal_global.1699
+ ___block_literal_global.1701
+ ___block_literal_global.1705
+ ___block_literal_global.1707
+ ___block_literal_global.1709
+ ___block_literal_global.1711
+ ___block_literal_global.1713
+ ___block_literal_global.1715
+ ___block_literal_global.1717
+ ___block_literal_global.1719
+ ___block_literal_global.1721
+ ___block_literal_global.1728
+ ___block_literal_global.1730
+ ___block_literal_global.1734
+ ___block_literal_global.1736
+ ___block_literal_global.1747
+ ___block_literal_global.1750
+ ___block_literal_global.1752
+ ___block_literal_global.1758
+ ___block_literal_global.1760
+ ___block_literal_global.1762
+ ___block_literal_global.1779
+ ___block_literal_global.1781
+ ___block_literal_global.1783
+ ___block_literal_global.1785
+ ___block_literal_global.1787
+ ___block_literal_global.1789
+ ___block_literal_global.1791
+ ___block_literal_global.1793
+ ___block_literal_global.1795
+ ___block_literal_global.1797
+ ___block_literal_global.1799
+ ___block_literal_global.1801
+ ___block_literal_global.1803
+ ___block_literal_global.1805
+ ___block_literal_global.1807
+ ___block_literal_global.1809
+ ___block_literal_global.1817
+ ___block_literal_global.1820
+ ___block_literal_global.1827
+ ___block_literal_global.1829
+ ___block_literal_global.1831
+ ___block_literal_global.1833
+ ___block_literal_global.1837
+ ___block_literal_global.1839
+ ___block_literal_global.1841
+ ___block_literal_global.1843
+ ___block_literal_global.1845
+ ___block_literal_global.1847
+ ___block_literal_global.1849
+ ___block_literal_global.1851
+ ___block_literal_global.1853
+ ___block_literal_global.1860
+ ___block_literal_global.1862
+ ___block_literal_global.1864
+ ___block_literal_global.1866
+ ___block_literal_global.1868
+ ___block_literal_global.1870
+ ___block_literal_global.1872
+ ___block_literal_global.1874
+ ___block_literal_global.1876
+ ___block_literal_global.1878
+ ___block_literal_global.1884
+ ___block_literal_global.1892
+ ___block_literal_global.1894
+ ___block_literal_global.1896
+ ___block_literal_global.1898
+ ___block_literal_global.1900
+ ___block_literal_global.1912
+ ___block_literal_global.1914
+ ___block_literal_global.1916
+ ___block_literal_global.1918
+ ___block_literal_global.1920
+ ___block_literal_global.1922
+ ___block_literal_global.1924
+ ___block_literal_global.1926
+ ___block_literal_global.1928
+ ___block_literal_global.1930
+ ___block_literal_global.1932
+ ___block_literal_global.1934
+ ___block_literal_global.1936
+ ___block_literal_global.1940
+ ___block_literal_global.1942
+ ___block_literal_global.1944
+ ___block_literal_global.1946
+ ___block_literal_global.1948
+ ___block_literal_global.1950
+ ___block_literal_global.1952
+ ___block_literal_global.1954
+ ___block_literal_global.1956
+ ___block_literal_global.1958
+ ___block_literal_global.1960
+ ___block_literal_global.1962
+ ___block_literal_global.1964
+ ___block_literal_global.1966
+ ___block_literal_global.1968
+ ___block_literal_global.1970
+ ___block_literal_global.1974
+ ___block_literal_global.1976
+ ___block_literal_global.1978
+ ___block_literal_global.1980
+ ___block_literal_global.1982
+ ___block_literal_global.1984
+ ___block_literal_global.1986
+ ___block_literal_global.1995
+ ___block_literal_global.1997
+ ___block_literal_global.1999
+ ___block_literal_global.2001
+ ___block_literal_global.2003
+ ___block_literal_global.2005
+ ___block_literal_global.2007
+ ___block_literal_global.2009
+ ___block_literal_global.2013
+ ___block_literal_global.2015
+ ___block_literal_global.2017
+ ___block_literal_global.2019
+ ___block_literal_global.2021
+ ___block_literal_global.2023
+ ___block_literal_global.2025
+ ___block_literal_global.2027
+ ___block_literal_global.2029
+ ___block_literal_global.2036
+ ___block_literal_global.2080
+ ___block_literal_global.2102
+ ___block_literal_global.2104
+ ___block_literal_global.2106
+ ___block_literal_global.2108
+ ___block_literal_global.2110
+ ___block_literal_global.2112
+ ___block_literal_global.2114
+ ___block_literal_global.2116
+ ___block_literal_global.2143
+ ___block_literal_global.2152
+ ___block_literal_global.2154
+ ___block_literal_global.2156
+ ___block_literal_global.2164
+ ___block_literal_global.2166
+ ___block_literal_global.2168
+ ___block_literal_global.2170
+ ___block_literal_global.2172
+ ___block_literal_global.2174
+ ___block_literal_global.2176
+ ___block_literal_global.2178
+ ___block_literal_global.2180
+ ___block_literal_global.2182
+ ___block_literal_global.2184
+ ___block_literal_global.2186
+ ___block_literal_global.2188
+ ___block_literal_global.2190
+ ___block_literal_global.2194
+ ___block_literal_global.2202
+ ___block_literal_global.2204
+ ___block_literal_global.2208
+ ___block_literal_global.2212
+ ___block_literal_global.2218
+ ___block_literal_global.2220
+ ___block_literal_global.2222
+ ___block_literal_global.2226
+ ___block_literal_global.2230
+ ___block_literal_global.2234
+ ___block_literal_global.2236
+ ___block_literal_global.2240
+ ___block_literal_global.2242
+ ___block_literal_global.2244
+ ___block_literal_global.2246
+ ___block_literal_global.2248
+ ___block_literal_global.2250
+ ___block_literal_global.2252
+ ___block_literal_global.2254
+ ___block_literal_global.2256
+ ___block_literal_global.2258
+ ___block_literal_global.2260
+ ___block_literal_global.2262
+ ___block_literal_global.2264
+ ___block_literal_global.2266
+ ___block_literal_global.2270
+ ___block_literal_global.2272
+ ___block_literal_global.2331
+ ___block_literal_global.2397
+ ___block_literal_global.2399
+ ___block_literal_global.2403
+ ___block_literal_global.2412
+ ___block_literal_global.2414
+ ___block_literal_global.2416
+ ___block_literal_global.2418
+ ___block_literal_global.2420
+ ___block_literal_global.2427
+ ___block_literal_global.2433
+ ___block_literal_global.2437
+ ___block_literal_global.2441
+ ___block_literal_global.2445
+ ___block_literal_global.2449
+ ___block_literal_global.2453
+ ___block_literal_global.2455
+ ___block_literal_global.2459
+ ___block_literal_global.2463
+ ___block_literal_global.2467
+ ___block_literal_global.2469
+ ___block_literal_global.2471
+ ___block_literal_global.2475
+ ___block_literal_global.2477
+ ___block_literal_global.2484
+ ___block_literal_global.2486
+ ___block_literal_global.2488
+ ___block_literal_global.2490
+ ___block_literal_global.2492
+ ___block_literal_global.2494
+ ___block_literal_global.2496
+ ___block_literal_global.2498
+ ___block_literal_global.2500
+ ___block_literal_global.2502
+ ___block_literal_global.2504
+ ___block_literal_global.2506
+ ___block_literal_global.2508
+ ___block_literal_global.2510
+ ___block_literal_global.2512
+ ___block_literal_global.2514
+ ___block_literal_global.2516
+ ___block_literal_global.2518
+ ___block_literal_global.2520
+ ___block_literal_global.2522
+ ___block_literal_global.2524
+ ___block_literal_global.2526
+ ___block_literal_global.2528
+ ___block_literal_global.2530
+ ___block_literal_global.2532
+ ___block_literal_global.2534
+ ___block_literal_global.2536
+ ___block_literal_global.2538
+ ___block_literal_global.2540
+ ___block_literal_global.2542
+ ___block_literal_global.2544
+ ___block_literal_global.2546
+ ___block_literal_global.2548
+ ___block_literal_global.2550
+ ___block_literal_global.2552
+ ___block_literal_global.2554
+ ___block_literal_global.2556
+ ___block_literal_global.2558
+ ___block_literal_global.2560
+ ___block_literal_global.2562
+ ___block_literal_global.2564
+ ___block_literal_global.2566
+ ___block_literal_global.2568
+ ___block_literal_global.2570
+ ___block_literal_global.2572
+ ___block_literal_global.2574
+ ___block_literal_global.2576
+ ___block_literal_global.2578
+ ___block_literal_global.2580
+ ___block_literal_global.2582
+ ___block_literal_global.2584
+ ___block_literal_global.2586
+ ___block_literal_global.2588
+ ___block_literal_global.2590
+ ___block_literal_global.2592
+ ___block_literal_global.2594
+ ___block_literal_global.2596
+ ___block_literal_global.2598
+ ___block_literal_global.2600
+ ___block_literal_global.2602
+ ___block_literal_global.2604
+ ___block_literal_global.2606
+ ___block_literal_global.2608
+ ___block_literal_global.2610
+ ___block_literal_global.2612
+ ___block_literal_global.2614
+ ___block_literal_global.2616
+ ___block_literal_global.2618
+ ___block_literal_global.2625
+ ___block_literal_global.2627
+ ___block_literal_global.2629
+ ___block_literal_global.2631
+ ___block_literal_global.2633
+ ___block_literal_global.2635
+ ___block_literal_global.2637
+ ___block_literal_global.2639
+ ___block_literal_global.2641
+ ___block_literal_global.2643
+ ___block_literal_global.2645
+ ___block_literal_global.2647
+ ___block_literal_global.2649
+ ___block_literal_global.2651
+ ___block_literal_global.2653
+ ___block_literal_global.2655
+ ___block_literal_global.2657
+ ___block_literal_global.2659
+ ___block_literal_global.2661
+ ___block_literal_global.2663
+ ___block_literal_global.4114
+ ___block_literal_global.4124
+ ___block_literal_global.4126
+ ___block_literal_global.423
+ ___block_literal_global.6166
+ ___block_literal_global.6168
+ ___block_literal_global.6180
+ ___block_literal_global.6188
+ ___block_literal_global.6192
+ ___block_literal_global.6196
+ ___block_literal_global.6200
+ ___block_literal_global.6204
+ ___block_literal_global.6208
+ ___block_literal_global.6212
+ ___block_literal_global.6216
+ ___block_literal_global.6220
+ ___block_literal_global.6224
+ ___block_literal_global.6228
+ ___block_literal_global.6234
+ ___block_literal_global.6238
+ ___block_literal_global.6242
+ ___block_literal_global.6248
+ ___block_literal_global.6256
+ ___block_literal_global.6260
+ ___block_literal_global.6263
+ ___block_literal_global.6267
+ ___block_literal_global.6271
+ ___block_literal_global.6275
+ ___block_literal_global.6279
+ ___block_literal_global.6283
+ ___block_literal_global.6287
+ ___block_literal_global.6291
+ ___block_literal_global.6295
+ ___block_literal_global.6299
+ ___block_literal_global.6303
+ ___block_literal_global.6307
+ ___block_literal_global.6311
+ ___block_literal_global.6315
+ ___block_literal_global.6319
+ ___block_literal_global.6323
+ ___block_literal_global.6325
+ ___block_literal_global.6329
+ ___block_literal_global.6333
+ ___block_literal_global.6337
+ ___block_literal_global.6351
+ ___block_literal_global.6353
+ ___block_literal_global.6355
+ ___block_literal_global.6359
+ ___block_literal_global.6363
+ ___block_literal_global.6377
+ ___block_literal_global.6385
+ ___block_literal_global.6399
+ ___block_literal_global.6403
+ ___block_literal_global.6407
+ ___block_literal_global.6411
+ ___block_literal_global.6423
+ ___block_literal_global.6428
+ ___block_literal_global.6436
+ ___block_literal_global.6444
+ ___block_literal_global.6448
+ ___block_literal_global.6452
+ ___block_literal_global.6456
+ ___block_literal_global.6462
+ ___block_literal_global.6464
+ ___block_literal_global.6466
+ ___block_literal_global.6468
+ ___block_literal_global.6470
+ ___block_literal_global.854
+ ___swift_memcpy20_8
+ __entryViewEmptyActionCached
+ __entryViewEmptyActionOnceToken
+ _areBannersSupported.once.6426
+ _areBannersSupported.once.6446
+ _attachmentBrowserDefaultSizeForSquare.once.6309
+ _attachmentBrowserDefaultSizeForSquare.sBehavior.6308.0
+ _attachmentBrowserDefaultSizeForSquare.sBehavior.6308.1
+ _attachmentBrowserGridInterItemSpacing.once.6313
+ _attachmentBrowserGridInterItemSpacing.sBehavior.6312
+ _canPresentOverKeyboard.once.6194
+ _canShowContactPhotosInConversationList.once.6230
+ _canShowContactPhotosInConversationList.sBehavior.6229
+ _contactPhotoTranscriptInsets.sBehavior.6261
+ _conversationListMinimumWidthForHiddenContactImage.once.6246
+ _conversationListMinimumWidthForHiddenContactImage.sBehavior.6245
+ _conversationListMultiSelectAccessoryUsesDefaultStyling.once.6240
+ _conversationListMultiSelectAccessoryUsesDefaultStyling.sBehavior.6239
+ _conversationListPrefersEditButtonOnTrailingEdge.once.6236
+ _conversationListPrefersEditButtonOnTrailingEdge.sBehavior.6235
+ _conversationUpdaterLogHandle.onceToken
+ _conversationUpdaterLogHandle.sLogHandle
+ _defaultAVPlayerViewContorllerControlsInsets.once.6269
+ _defaultAVPlayerViewContorllerControlsInsets.sBehavior.6268.0
+ _defaultAVPlayerViewContorllerControlsInsets.sBehavior.6268.1
+ _defaultAVPlayerViewContorllerControlsInsets.sBehavior.6268.2
+ _defaultAVPlayerViewContorllerControlsInsets.sBehavior.6268.3
+ _defaultConversationViewingMessageCount.once.6222
+ _defaultConversationViewingMessageCount.sBehavior.6221
+ _detonatedItemBalloonViewSize.once.6357
+ _detonatedItemBalloonViewSize.sBehavior.6356.0
+ _detonatedItemBalloonViewSize.sBehavior.6356.1
+ _detonatedItemDocumentIconSize.once.6361
+ _detonatedItemDocumentIconSize.sBehavior.6360.0
+ _detonatedItemDocumentIconSize.sBehavior.6360.1
+ _documentIconSize.once.6273
+ _documentIconSize.sBehavior.6272.0
+ _documentIconSize.sBehavior.6272.1
+ _entryFieldShouldUseBackdropView.once.6379
+ _entryFieldShouldUseBackdropView.once.6405
+ _entryViewAlwaysUsesConcentricPadding.once.6289
+ _entryViewAlwaysUsesConcentricPadding.sBehavior.6288
+ _entryViewConcentricPadding.once.6293
+ _entryViewConcentricPadding.sBehavior.6292
+ _entryViewHorizontalCoverInsets.once.6391
+ _entryViewHorizontalCoverInsets.once.6416
+ _entryViewHorizontalCoverInsets.sBehavior.6390.0
+ _entryViewHorizontalCoverInsets.sBehavior.6390.1
+ _entryViewHorizontalCoverInsets.sBehavior.6390.2
+ _entryViewHorizontalCoverInsets.sBehavior.6390.3
+ _entryViewHorizontalCoverInsets.sBehavior.6415.0
+ _entryViewHorizontalCoverInsets.sBehavior.6415.1
+ _entryViewHorizontalCoverInsets.sBehavior.6415.2
+ _entryViewHorizontalCoverInsets.sBehavior.6415.3
+ _entryViewMaxHandWritingPluginShelfHeight.once.6305
+ _entryViewMaxHandWritingPluginShelfHeight.sBehavior.6304
+ _entryViewVerticalCoverInsets.once.6387
+ _entryViewVerticalCoverInsets.once.6413
+ _entryViewVerticalCoverInsets.sBehavior.6386
+ _entryViewVerticalCoverInsets.sBehavior.6412
+ _get_witness_table 7SwiftUI4ViewRzlAA05TupleC0VyAaBPAAE5alert_11isPresented7actionsQrqd___AA7BindingVySbGqd_0_yXEtSyRd__AaBRd_0_r0_lFQOyAA5GroupVyADyAA19_ConditionalContentVyAA7SectionVyAA05EmptyC0VAA08ModifiedL0VyAeAE11toggleStyleyQrqd__AA06ToggleQ0Rd__lFQOyAA0R0VyAA4TextVG_AA06SwitchrQ0VQo_7ChatKit07Detailsc3RowQ0VGAUyAUyA4_019SharedWithYouFooterC0VAA21_TraitWritingModifierVyAA04ListX18BackgroundTraitKeyVGGAA14_PaddingLayoutVGGASG_AUyAQyAsDyA3_Sg_A21_A21_tGASGA6_GAA012SubscriptionC0VySo20NSNotificationCenterC10FoundationE9PublisherVAUyAQyAsDyA3__AOyAeAE06pickerQ0yQrqd__AA06PickerQ0Rd__lFQOyAA6PickerVyA_SSADyAA7ForEachVySayA29_6LocaleVGA39_AeAE3tag_15includeOptionalQrqd___SbtSHRd__lFQOyA__SSQo_G_A43_SgtGG_AA013DefaultPickerQ0VQo_AUyAA6ButtonVyA_GA6_GGSgtGASGA6_GGSgAUyAeAE18confirmationDialog_AG15titleVisibilityAHQrAA18LocalizedStringKeyV_AkA10VisibilityOqd__yXEtAaBRd__lFQOyAUyA53_AA32_EnvironmentKeyTransformModifierVySbGG_A53_Qo_A6_GSgAUyAeAEA62__AGA63_AHQrA65__AKA67_qd__yXEtAaBRd__lFQOyA53__A53_Qo_A6_GSgtGG_SSADyA53__A53_tGQo__AUyxA14_GSgtGAaBHPyHC.241
+ _get_witness_table 7SwiftUI7SectionVyAA9EmptyViewVAA05TupleE0VyAA0E0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaHRd__lFQOyAiAEAjklMQrAP_AQqd__yctAaHRd__lFQOyAiAE18confirmationDialog_AK15titleVisibility7actions7messageQrqd___ApA0Q0Oqd_0_yXEqd_1_yXEtSyRd__AaHRd_0_AaHRd_1_r1_lFQOyAiAE5alert_AktUQrqd___APqd_0_yXEqd_1_yXEtSyRd__AaHRd_0_AaHRd_1_r1_lFQOyAA15ModifiedContentVyAiAE11toggleStyleyQrqd__AA06ToggleX0Rd__lFQOyAA0Y0VyAA6VStackVyAGyAZyAA4TextVAA16_FlexFrameLayoutVG_AA012_ConditionalV0VyA11_yA11_yA9_A9_GAEGA11_yAEA9_GGtGGG_AA06SwitchyX0VQo_AA30_EnvironmentKeyWritingModifierVyAA5ColorVSgGG_SSAGyAA6ButtonVyA6_G_A31_tGA6_Qo__SSAGyA11_yA11_yAA7ForEachVySay10Foundation6LocaleVGSSA31_GAiAE16keyboardShortcutyQrAA16KeyboardShortcutVFQOyA31__Qo_GA31_GSg_A31_tGA6_Qo__7ChatKit019CKLanguageSelectionE0VQo__A52_Qo__A11_yA11_yAEA31_GAiAE06buttonX0yQrqd__AA015PrimitiveButtonX0Rd__lFQOyA30_yAA07LabeledV0VyA6_A6_GG_AA020NavigationLinkButtonX0Vys5NeverOGQo_GA11_yA11_yA2EGA67_GtGAEGAaHHPAeaHHPyHC_A71_AaHHPyHCAeaHHPyHCHC.99
+ _groupRecipientSelectionPresentationStyle.once.6335
+ _groupRecipientSelectionPresentationStyle.sBehavior.6334
+ _isAppStripInKeyboard.once.6297
+ _joystickUsesWindow.once.6375
+ _joystickUsesWindow.once.6401
+ _keyboardSizeDeterminesAppCardDetentHeight.once.6198
+ _lowClearanceInLandscape.once.6186
+ _minTranscriptMarginInsets.once.6265
+ _minTranscriptMarginInsets.sBehavior.6264.1
+ _minTranscriptMarginInsets.sBehavior.6264.3
+ _numberOfButtonsInPhotoPicker.once.6321
+ _numberOfButtonsInPhotoPicker.sBehavior.6320
+ _objc_msgSend$_reloadTranscriptBackground
+ _objc_msgSend$_updateLongPressAudioStopButtonHighlighted:
+ _objc_msgSend$buttonFor:
+ _objc_msgSend$collectionViewComputedInsets:
+ _objc_msgSend$conversationUpdaterLogHandle
+ _objc_msgSend$entryViewEmptyAction
+ _objc_msgSend$isEntryViewEmptyActionEnabled
+ _objc_msgSend$localizedStandardRangeOfString:
+ _photoPickerMaxPopoverPhotoHeight.once.6327
+ _photoPickerMaxPopoverPhotoHeight.sBehavior.6326
+ _photoPickerPopoverWidth.once.6317
+ _photoPickerPopoverWidth.sBehavior.6316
+ _presentForwardingUIModally.once.6206
+ _presentsAutocompleteInAPopover.once.6285
+ _presentsQuickLookController.once.6202
+ _presentsQuickLookController.sBehavior.6201
+ _previewMaxWidth.once.6250
+ _previewMaxWidth.sBehavior.6249
+ _resetsIdleTimer.once.6434
+ _resetsIdleTimer.once.6454
+ _searchLinksThumbnailWidth.once.6347
+ _searchLinksThumbnailWidth.sBehavior.6346
+ _searchPhotosThumbnailWidth.once.6345
+ _searchPhotosThumbnailWidth.sBehavior.6344
+ _shouldAlignRecipientGlyphsWithMargins.once.6331
+ _shouldAlignRecipientGlyphsWithMargins.sBehavior.6330
+ _shouldRefreshAlternateAddressesSheet.once.6281
+ _shouldRefreshAlternateAddressesSheet.sBehavior.6280
+ _shouldShowDisclosureChevronInRecipientAtoms.once.6277
+ _shouldSuppressRotationInNewCompose.once.6182
+ _shouldUnreadIndicatorChangeOnSelection.once.6244
+ _shouldUnreadIndicatorChangeOnSelection.sBehavior.6243
+ _shouldUseSimpleTimestampsInTranscript.once.6430
+ _shouldUseSimpleTimestampsInTranscript.once.6450
+ _shouldUseSimpleTimestampsInTranscript.sBehavior.6429
+ _shouldUseSimpleTimestampsInTranscript.sBehavior.6449
+ _showMMSSetup.once.6218
+ _showPendingInConversationList.once.6226
+ _showPendingInConversationList.sBehavior.6225
+ _showsConversationListCellChevronImage.once.6232
+ _showsConversationListCellChevronImage.sBehavior.6231
+ _suggestedAppStripLimit.once.6349
+ _suggestedAppStripLimit.sBehavior.6348
+ _supportedInterfaceOrientations.once.6214
+ _supportedInterfaceOrientations.sBehavior.6213
+ _supportsEntryViewPlusButtonLongPress.once.6301
+ _supportsEntryViewPlusButtonLongPress.sBehavior.6300
+ _symbolic _____ 7ChatKit25TranslationTipEligibilityV
+ _symbolic _____ 7ChatKit25TranslationTipEligibilityV22ConfusingLanguagePairsO
+ _symbolic _____ 7ChatKit37TranslationLanguageAlertConfigurationV
+ _symbolic _____6locale_SaySSG12messageGUIDst 10Foundation6LocaleV
+ _symbolic _____6locale_SaySSG12messageGUIDstSg 10Foundation6LocaleV
+ _symbolic _____Sg 16LinkPresentation0A8MetadataV
+ _symbolic _____yAAy_____ySay_____GSS_____y_____GG_____yAG_Qo_GAGG 7SwiftUI19_ConditionalContentV AA7ForEachV 10Foundation6LocaleV AA6ButtonV AA4TextV AA4ViewPAAE16keyboardShortcutyQrAA08KeyboardM0VFQO
+ _symbolic _____yAAy_____ySay_____GSS_____y_____GG_____yAG_Qo_GAGGSg 7SwiftUI19_ConditionalContentV AA7ForEachV 10Foundation6LocaleV AA6ButtonV AA4TextV AA4ViewPAAE16keyboardShortcutyQrAA08KeyboardM0VFQO
+ _symbolic _____yAAy_____ySay_____GSS_____y_____GG_____yAG_Qo_GAGGSg_AGt 7SwiftUI19_ConditionalContentV AA7ForEachV 10Foundation6LocaleV AA6ButtonV AA4TextV AA4ViewPAAE16keyboardShortcutyQrAA08KeyboardM0VFQO
+ _symbolic _____ySay_____GAB_____y______SSQo_G 7SwiftUI7ForEachV 10Foundation6LocaleV AA4ViewPAAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA4TextV
+ _symbolic _____ySay_____GAB_____y______SSQo_G_AESgt 7SwiftUI7ForEachV 10Foundation6LocaleV AA4ViewPAAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA4TextV
+ _symbolic _____ySay_____GSS_____y_____GG 7SwiftUI7ForEachV 10Foundation6LocaleV AA6ButtonV AA4TextV
+ _symbolic _____y_____SS_____y_____ySay_____GAE_____yAB_SSQo_G_AGSgtGG 7SwiftUI6PickerV AA4TextV AA9TupleViewV AA7ForEachV 10Foundation6LocaleV AA0F0PAAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO
+ _symbolic _____y______SaySSGtG s23_ContiguousArrayStorageC 10Foundation6LocaleV
+ _symbolic _____y__________y_____y__________y_____y_____y_____G______Qo_______y_____y_____yAHSSAFy_____ySay_____GAO_____yAH_SSQo_G_AQSgtGG______Qo_ACy_____yAHG_____GGSgtGAEGAZGG 7SwiftUI16SubscriptionViewV So20NSNotificationCenterC10FoundationE9PublisherV AA15ModifiedContentV AA7SectionV AA05EmptyD0V AA05TupleD0V AA0D0PAAE11toggleStyleyQrqd__AA06ToggleO0Rd__lFQO AA0P0V AA4TextV AA06SwitchpO0V AA012_ConditionalJ0V ArAE06pickerO0yQrqd__AA06PickerO0Rd__lFQO AA0U0V AA7ForEachV AF6LocaleV ArAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA07DefaultuO0V AA6ButtonV 7ChatKit07Detailsd3RowO0V
+ _symbolic _____y__________y_____y__________y_____y_____y_____G______Qo_______y_____y_____yAHSSAFy_____ySay_____GAO_____yAH_SSQo_G_AQSgtGG______Qo_ACy_____yAHG_____GGSgtGAEGAZGGSg 7SwiftUI16SubscriptionViewV So20NSNotificationCenterC10FoundationE9PublisherV AA15ModifiedContentV AA7SectionV AA05EmptyD0V AA05TupleD0V AA0D0PAAE11toggleStyleyQrqd__AA06ToggleO0Rd__lFQO AA0P0V AA4TextV AA06SwitchpO0V AA012_ConditionalJ0V ArAE06pickerO0yQrqd__AA06PickerO0Rd__lFQO AA0U0V AA7ForEachV AF6LocaleV ArAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA07DefaultuO0V AA6ButtonV 7ChatKit07Detailsd3RowO0V
+ _symbolic _____y__________y_____y_____y_____y_____y_____y_____y_____y_____yACyADy__________G______yAJyAJyA2IGABGAJyAbIGGtGGG______Qo______y_____SgGG_SSACy_____yAGG_AZtGAGQo__SSACyAJyAJy_____ySay_____GSSAZG_____yAZ_Qo_GAZGSg_AZtGAGQo_______Qo__A11_Qo__AJyAJyAbZG_____yAYy_____yA2GGG______y_____GQo_GAJyAJyA2BGA21_GtGABG 7SwiftUI7SectionV AA9EmptyViewV AA05TupleE0V AA0E0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaHRd__lFQO AiAEAjklMQrAP_AQqd__yctAaHRd__lFQO AiAE18confirmationDialog_AK15titleVisibility7actions7messageQrqd___ApA0Q0Oqd_0_yXEqd_1_yXEtSyRd__AaHRd_0_AaHRd_1_r1_lFQO AiAE5alert_AktUQrqd___APqd_0_yXEqd_1_yXEtSyRd__AaHRd_0_AaHRd_1_r1_lFQO AA15ModifiedContentV AiAE11toggleStyleyQrqd__AA06ToggleX0Rd__lFQO AA0Y0V AA6VStackV AA4TextV AA16_FlexFrameLayoutV AA012_ConditionalV0V AA06SwitchyX0V AA30_EnvironmentKeyWritingModifierV AA5ColorV AA6ButtonV AA7ForEachV 10Foundation6LocaleV AiAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO 7ChatKit019CKLanguageSelectionE0V AiAE06buttonX0yQrqd__AA015PrimitiveButtonX0Rd__lFQO AA07LabeledV0V AA020NavigationLinkButtonX0V s5NeverO
+ _symbolic _____y_____yABy_____ySay_____GSS_____y_____GG_____yAH_Qo_GAHGSg_AHtG 7SwiftUI9TupleViewV AA19_ConditionalContentV AA7ForEachV 10Foundation6LocaleV AA6ButtonV AA4TextV AA0D0PAAE16keyboardShortcutyQrAA08KeyboardN0VFQO
+ _symbolic _____y_____ySay_____GAC_____y______SSQo_G_AFSgtG 7SwiftUI9TupleViewV AA7ForEachV 10Foundation6LocaleV AA0D0PAAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA4TextV
+ _symbolic _____y_____ySay_____GSS_____y_____GG_____yAG_Qo_G 7SwiftUI19_ConditionalContentV AA7ForEachV 10Foundation6LocaleV AA6ButtonV AA4TextV AA4ViewPAAE16keyboardShortcutyQrAA08KeyboardM0VFQO
+ _symbolic _____y_____ySay_____GSS_____y_____GG_____yAG_Qo__G 7SwiftUI19_ConditionalContentV7StorageO AA7ForEachV 10Foundation6LocaleV AA6ButtonV AA4TextV AA4ViewPAAE16keyboardShortcutyQrAA08KeyboardN0VFQO
+ _symbolic _____y_____y_____G______Qo_______y_____y_____yABSS_____y_____ySay_____GAJ_____yAB_SSQo_G_ALSgtGG______Qo______y_____yABG_____GGSgt 7SwiftUI4ViewPAAE11toggleStyleyQrqd__AA06ToggleE0Rd__lFQO AA0F0V AA4TextV AA06SwitchfE0V AA19_ConditionalContentV AcAE06pickerE0yQrqd__AA06PickerE0Rd__lFQO AA0L0V AA05TupleC0V AA7ForEachV 10Foundation6LocaleV AcAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA07DefaultlE0V AA08ModifiedJ0V AA6ButtonV 7ChatKit07Detailsc3RowE0V
+ _symbolic _____y_____y_____SS_____y_____ySay_____GAE_____yAB_SSQo_G_AGSgtGG______Qo_ 7SwiftUI4ViewPAAE11pickerStyleyQrqd__AA06PickerE0Rd__lFQO AA0F0V AA4TextV AA05TupleC0V AA7ForEachV 10Foundation6LocaleV AcAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA07DefaultfE0V
+ _symbolic _____y_____y__________y_____y_____y_____G______Qo______GADyADy__________y_____GG_____GGACG_ADyAByAC_____yAISg_A2VtGACGAJG_____y_____ADyAByAcUyAI_AAy_____y_____yAFSSAUy_____ySay_____GA2______yAF_SSQo_G_A4_SgtGG______Qo_ADy_____yAFGAJGGSgtGACGAJGGSgADy_____yADyA12______ySbGG_A12_Qo_AJGSgADy_____yA12__A12_Qo_AJGSgt 7SwiftUI19_ConditionalContentV AA7SectionV AA9EmptyViewV AA08ModifiedD0V AA0G0PAAE11toggleStyleyQrqd__AA06ToggleJ0Rd__lFQO AA0K0V AA4TextV AA06SwitchkJ0V 7ChatKit07Detailsg3RowJ0V AT019SharedWithYouFooterG0V AA21_TraitWritingModifierV AA04Listq10BackgroundV3KeyV AA14_PaddingLayoutV AA05TupleG0V AA012SubscriptionG0V So20NSNotificationCenterC10FoundationE9PublisherV AkAE06pickerJ0yQrqd__AA06PickerJ0Rd__lFQO AA6PickerV AA7ForEachV A9_6LocaleV AkAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA013DefaultPickerJ0V AA6ButtonV AkAE18confirmationDialog_11isPresented15titleVisibility7actionsQrAA18LocalizedStringKeyV_AA7BindingVySbGAA10VisibilityOqd__yXEtAaJRd__lFQO AA024_EnvironmentKeyTransformX0V AkAEA26__A27_A28_A29_QrA31__A34_A36_qd__yXEtAaJRd__lFQO
+ _symbolic _____y_____y__________y_____y_____y_____G______Qo_______y_____y_____yAFSSADy_____ySay_____GAM_____yAF_SSQo_G_AOSgtGG______Qo_AAy_____yAFG_____GGSgtGACGAXG 7SwiftUI15ModifiedContentV AA7SectionV AA9EmptyViewV AA05TupleG0V AA0G0PAAE11toggleStyleyQrqd__AA06ToggleJ0Rd__lFQO AA0K0V AA4TextV AA06SwitchkJ0V AA012_ConditionalD0V AkAE06pickerJ0yQrqd__AA06PickerJ0Rd__lFQO AA0P0V AA7ForEachV 10Foundation6LocaleV AkAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA07DefaultpJ0V AA6ButtonV 7ChatKit07Detailsg3RowJ0V
+ _symbolic _____y_____y_____yAAy_____y_____y__________y_____y_____y_____G______Qo______GAFyAFy__________y_____GG_____GGAEG_AFyADyAeAyAKSg_A2WtGAEGALG_____y_____AFyADyAeAyAK_ACy_____y_____yAHSSAAy_____ySay_____GA3______yAH_SSQo_G_A5_SgtGG______Qo_AFy_____yAHGALGGSgtGAEGALGGSgAFy_____yAFyA13______ySbGG_A13_Qo_ALGSgAFy_____yA13__A13_Qo_ALGSgtGG_SSAAyA13__A13_tGQo__AFyxAQGSgtG 7SwiftUI9TupleViewV AA0D0PAAE5alert_11isPresented7actionsQrqd___AA7BindingVySbGqd_0_yXEtSyRd__AaDRd_0_r0_lFQO AA5GroupV AA19_ConditionalContentV AA7SectionV AA05EmptyD0V AA08ModifiedL0V AeAE11toggleStyleyQrqd__AA06ToggleQ0Rd__lFQO AA0R0V AA4TextV AA06SwitchrQ0V 7ChatKit07Detailsd3RowQ0V A2_019SharedWithYouFooterD0V AA21_TraitWritingModifierV AA04ListX18BackgroundTraitKeyV AA14_PaddingLayoutV AA012SubscriptionD0V So20NSNotificationCenterC10FoundationE9PublisherV AeAE06pickerQ0yQrqd__AA06PickerQ0Rd__lFQO AA6PickerV AA7ForEachV A17_6LocaleV AeAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA013DefaultPickerQ0V AA6ButtonV AeAE18confirmationDialog_AG15titleVisibilityAHQrAA18LocalizedStringKeyV_AkA10VisibilityOqd__yXEtAaDRd__lFQO AA32_EnvironmentKeyTransformModifierV AeAEA34__AGA35_AHQrA37__AKA39_qd__yXEtAaDRd__lFQO
+ _symbolic _____y_____y_____ySay_____GSS_____y_____GG_____yAH_Qo_GAH_G 7SwiftUI19_ConditionalContentV7StorageO AC AA7ForEachV 10Foundation6LocaleV AA6ButtonV AA4TextV AA4ViewPAAE16keyboardShortcutyQrAA08KeyboardN0VFQO
+ _symbolic _____y_____y_____y_____G______Qo_______y_____y_____yACSSAAy_____ySay_____GAJ_____yAC_SSQo_G_ALSgtGG______Qo______y_____yACG_____GGSgtG 7SwiftUI9TupleViewV AA0D0PAAE11toggleStyleyQrqd__AA06ToggleF0Rd__lFQO AA0G0V AA4TextV AA06SwitchgF0V AA19_ConditionalContentV AeAE06pickerF0yQrqd__AA06PickerF0Rd__lFQO AA0M0V AA7ForEachV 10Foundation6LocaleV AeAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA07DefaultmF0V AA08ModifiedK0V AA6ButtonV 7ChatKit07Detailsd3RowF0V
+ _symbolic _____y_____y_____y_____SS_____y_____ySay_____GAF_____yAC_SSQo_G_AHSgtGG______Qo______y_____yACG_____GG 7SwiftUI19_ConditionalContentV AA4ViewPAAE11pickerStyleyQrqd__AA06PickerG0Rd__lFQO AA0H0V AA4TextV AA05TupleE0V AA7ForEachV 10Foundation6LocaleV AeAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA07DefaulthG0V AA08ModifiedD0V AA6ButtonV 7ChatKit07Detailse3RowG0V
+ _symbolic _____y_____y_____y_____SS_____y_____ySay_____GAF_____yAC_SSQo_G_AHSgtGG______Qo______y_____yACG_____GGSg 7SwiftUI19_ConditionalContentV AA4ViewPAAE11pickerStyleyQrqd__AA06PickerG0Rd__lFQO AA0H0V AA4TextV AA05TupleE0V AA7ForEachV 10Foundation6LocaleV AeAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA07DefaulthG0V AA08ModifiedD0V AA6ButtonV 7ChatKit07Detailse3RowG0V
+ _symbolic _____y_____y_____y_____SS_____y_____ySay_____GAF_____yAC_SSQo_G_AHSgtGG______Qo______y_____yACG_____G_G 7SwiftUI19_ConditionalContentV7StorageO AA4ViewPAAE11pickerStyleyQrqd__AA06PickerH0Rd__lFQO AA0I0V AA4TextV AA05TupleF0V AA7ForEachV 10Foundation6LocaleV AgAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA07DefaultiH0V AA08ModifiedD0V AA6ButtonV 7ChatKit07Detailsf3RowH0V
+ _symbolic _____y_____y_____y__________y_____y_____y_____G______Qo______GAEyAEy__________y_____GG_____GGADG_AEyACyAdAyAJSg_A2VtGADGAKG_____y_____AEyACyAdAyAJ_ABy_____y_____yAGSSAAy_____ySay_____GA2______yAG_SSQo_G_A4_SgtGG______Qo_AEy_____yAGGAKGGSgtGADGAKGGSgAEy_____yAEyA12______ySbGG_A12_Qo_AKGSgAEy_____yA12__A12_Qo_AKGSgtG 7SwiftUI9TupleViewV AA19_ConditionalContentV AA7SectionV AA05EmptyD0V AA08ModifiedF0V AA0D0PAAE11toggleStyleyQrqd__AA06ToggleK0Rd__lFQO AA0L0V AA4TextV AA06SwitchlK0V 7ChatKit07Detailsd3RowK0V AV019SharedWithYouFooterD0V AA21_TraitWritingModifierV AA04Listr10BackgroundW3KeyV AA14_PaddingLayoutV AA012SubscriptionD0V So20NSNotificationCenterC10FoundationE9PublisherV AmAE06pickerK0yQrqd__AA06PickerK0Rd__lFQO AA6PickerV AA7ForEachV A9_6LocaleV AmAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA013DefaultPickerK0V AA6ButtonV AmAE18confirmationDialog_11isPresented15titleVisibility7actionsQrAA18LocalizedStringKeyV_AA7BindingVySbGAA10VisibilityOqd__yXEtAaLRd__lFQO AA024_EnvironmentKeyTransformY0V AmAEA26__A27_A28_A29_QrA31__A34_A36_qd__yXEtAaLRd__lFQO
+ _symbolic _____y_____y_____y_____y__________y_____y_____y_____G______Qo______GAFyAFy__________y_____GG_____GGAEG_AFyADyAeByAKSg_A2WtGAEGALG_____y_____AFyADyAeByAK_ACy_____y_____yAHSSABy_____ySay_____GA3______yAH_SSQo_G_A5_SgtGG______Qo_AFy_____yAHGALGGSgtGAEGALGGSgAFy_____yAFyA13______ySbGG_A13_Qo_ALGSgAFy_____yA13__A13_Qo_ALGSgtGG 7SwiftUI5GroupV AA9TupleViewV AA19_ConditionalContentV AA7SectionV AA05EmptyE0V AA08ModifiedG0V AA0E0PAAE11toggleStyleyQrqd__AA06ToggleL0Rd__lFQO AA0M0V AA4TextV AA06SwitchmL0V 7ChatKit07Detailse3RowL0V AX019SharedWithYouFooterE0V AA21_TraitWritingModifierV AA04Lists10BackgroundX3KeyV AA14_PaddingLayoutV AA012SubscriptionE0V So20NSNotificationCenterC10FoundationE9PublisherV AoAE06pickerL0yQrqd__AA06PickerL0Rd__lFQO AA6PickerV AA7ForEachV A11_6LocaleV AoAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA013DefaultPickerL0V AA6ButtonV AoAE18confirmationDialog_11isPresented15titleVisibility7actionsQrAA18LocalizedStringKeyV_AA7BindingVySbGAA10VisibilityOqd__yXEtAaNRd__lFQO AA024_EnvironmentKeyTransformZ0V AoAEA28__A29_A30_A31_QrA33__A36_A38_qd__yXEtAaNRd__lFQO
+ _symbolic _____y_____y_____y_____y_____y__________y_____y_____y_____G______Qo______GAFyAFy__________y_____GG_____GGAEG_AFyADyAeByAKSg_A2WtGAEGALG_____y_____AFyADyAeByAK_ACy_____y_____yAHSSABy_____ySay_____GA3______yAH_SSQo_G_A5_SgtGG______Qo_AFy_____yAHGALGGSgtGAEGALGGSgAFy_____yAFyA13______ySbGG_A13_Qo_ALGSgAFy_____yA13__A13_Qo_ALGSgtGG_SSAByA13__A13_tGQo_ 7SwiftUI4ViewPAAE5alert_11isPresented7actionsQrqd___AA7BindingVySbGqd_0_yXEtSyRd__AaBRd_0_r0_lFQO AA5GroupV AA05TupleC0V AA19_ConditionalContentV AA7SectionV AA05EmptyC0V AA08ModifiedL0V AcAE11toggleStyleyQrqd__AA06ToggleQ0Rd__lFQO AA0R0V AA4TextV AA06SwitchrQ0V 7ChatKit07Detailsc3RowQ0V A2_019SharedWithYouFooterC0V AA21_TraitWritingModifierV AA04ListX18BackgroundTraitKeyV AA14_PaddingLayoutV AA012SubscriptionC0V So20NSNotificationCenterC10FoundationE9PublisherV AcAE06pickerQ0yQrqd__AA06PickerQ0Rd__lFQO AA6PickerV AA7ForEachV A17_6LocaleV AcAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA013DefaultPickerQ0V AA6ButtonV AcAE18confirmationDialog_AE15titleVisibilityAFQrAA18LocalizedStringKeyV_AiA10VisibilityOqd__yXEtAaBRd__lFQO AA32_EnvironmentKeyTransformModifierV AcAEA34__AEA35_AFQrA37__AIA39_qd__yXEtAaBRd__lFQO
+ _symbolic _____y_____y_____y_____y_____y_____y_____yAAy__________G______yAHyAHyA2GG_____GAHyAjGGGtGGG______Qo______y_____SgGG_SSADy_____yAEG_AYtGAEQo__SSADyAHyAHy_____ySay_____GSSAYG_____yAY_Qo_GAYGSg_AYtGAEQo_ 7SwiftUI4ViewPAAE18confirmationDialog_11isPresented15titleVisibility7actions7messageQrqd___AA7BindingVySbGAA0I0Oqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AcAE5alert_AegHQrqd___AKqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AA15ModifiedContentV AcAE11toggleStyleyQrqd__AA06ToggleQ0Rd__lFQO AA0R0V AA6VStackV AA05TupleC0V AA4TextV AA16_FlexFrameLayoutV AA012_ConditionalO0V AA05EmptyC0V AA06SwitchrQ0V AA30_EnvironmentKeyWritingModifierV AA5ColorV AA6ButtonV AA7ForEachV 10Foundation6LocaleV AcAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO
+ _symbolic _____y_____y_____y_____y_____y_____y_____y_____yAAy__________G______yAHyAHyA2GG_____GAHyAjGGGtGGG______Qo______y_____SgGG_SSADy_____yAEG_AYtGAEQo__SSADyAHyAHy_____ySay_____GSSAYG_____yAY_Qo_GAYGSg_AYtGAEQo_______Qo_ 7SwiftUI4ViewPAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQO AcAE18confirmationDialog_AE15titleVisibility7actions7messageQrqd___AjA0N0Oqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AcAE5alert_AenOQrqd___AJqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AA15ModifiedContentV AcAE11toggleStyleyQrqd__AA06ToggleU0Rd__lFQO AA0V0V AA6VStackV AA05TupleC0V AA4TextV AA16_FlexFrameLayoutV AA012_ConditionalS0V AA05EmptyC0V AA06SwitchvU0V AA30_EnvironmentKeyWritingModifierV AA5ColorV AA6ButtonV AA7ForEachV 10Foundation6LocaleV AcAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO 7ChatKit019CKLanguageSelectionC0V
+ _symbolic _____y_____y_____y_____y_____y_____y_____y_____y_____yAAyABy__________G______yAHyAHyA2GG_____GAHyAjGGGtGGG______Qo______y_____SgGG_SSAAy_____yAEG_AYtGAEQo__SSAAyAHyAHy_____ySay_____GSSAYG_____yAY_Qo_GAYGSg_AYtGAEQo_______Qo__A10_Qo__AHyAHyAjYG_____yAXy_____yA2EGG______y_____GQo_GAHyAHyA2JGA20_GtG 7SwiftUI9TupleViewV AA0D0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaDRd__lFQO AeAEAfghIQrAL_AMqd__yctAaDRd__lFQO AeAE18confirmationDialog_AG15titleVisibility7actions7messageQrqd___AlA0O0Oqd_0_yXEqd_1_yXEtSyRd__AaDRd_0_AaDRd_1_r1_lFQO AeAE5alert_AgpQQrqd___ALqd_0_yXEqd_1_yXEtSyRd__AaDRd_0_AaDRd_1_r1_lFQO AA15ModifiedContentV AeAE11toggleStyleyQrqd__AA06ToggleV0Rd__lFQO AA0W0V AA6VStackV AA4TextV AA16_FlexFrameLayoutV AA012_ConditionalT0V AA05EmptyD0V AA06SwitchwV0V AA30_EnvironmentKeyWritingModifierV AA5ColorV AA6ButtonV AA7ForEachV 10Foundation6LocaleV AeAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO 7ChatKit019CKLanguageSelectionD0V AeAE06buttonV0yQrqd__AA015PrimitiveButtonV0Rd__lFQO AA07LabeledT0V AA020NavigationLinkButtonV0V s5NeverO
+ _symbolic _____y_____y_____y_____y_____y_____y_____y_____y_____yAAy__________G______yAHyAHyA2GG_____GAHyAjGGGtGGG______Qo______y_____SgGG_SSADy_____yAEG_AYtGAEQo__SSADyAHyAHy_____ySay_____GSSAYG_____yAY_Qo_GAYGSg_AYtGAEQo_______Qo__A10_Qo_ 7SwiftUI4ViewPAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQO AcAEAdefGQrAJ_AKqd__yctAaBRd__lFQO AcAE18confirmationDialog_AE15titleVisibility7actions7messageQrqd___AjA0N0Oqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AcAE5alert_AenOQrqd___AJqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AA15ModifiedContentV AcAE11toggleStyleyQrqd__AA06ToggleU0Rd__lFQO AA0V0V AA6VStackV AA05TupleC0V AA4TextV AA16_FlexFrameLayoutV AA012_ConditionalS0V AA05EmptyC0V AA06SwitchvU0V AA30_EnvironmentKeyWritingModifierV AA5ColorV AA6ButtonV AA7ForEachV 10Foundation6LocaleV AcAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO 7ChatKit019CKLanguageSelectionC0V
+ _symbolic _____y_____y_____y_____y_____y_____y_____y_____y_____yAAy__________G______yAHyAHyA2GG_____GAHyAjGGGtGGG______Qo______y_____SgGG_SSADy_____yAEG_AYtGAEQo__SSADyAHyAHy_____ySay_____GSSAYG_____yAY_Qo_GAYGSg_AYtGAEQo_______Qo__A10_Qo__AHyAHyAjYG_____yAXy_____yA2EGG______y_____GQo_GAHyAHyA2JGA20_Gt 7SwiftUI4ViewPAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQO AcAEAdefGQrAJ_AKqd__yctAaBRd__lFQO AcAE18confirmationDialog_AE15titleVisibility7actions7messageQrqd___AjA0N0Oqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AcAE5alert_AenOQrqd___AJqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AA15ModifiedContentV AcAE11toggleStyleyQrqd__AA06ToggleU0Rd__lFQO AA0V0V AA6VStackV AA05TupleC0V AA4TextV AA16_FlexFrameLayoutV AA012_ConditionalS0V AA05EmptyC0V AA06SwitchvU0V AA30_EnvironmentKeyWritingModifierV AA5ColorV AA6ButtonV AA7ForEachV 10Foundation6LocaleV AcAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO 7ChatKit019CKLanguageSelectionC0V AcAE06buttonU0yQrqd__AA015PrimitiveButtonU0Rd__lFQO AA07LabeledS0V AA020NavigationLinkButtonU0V s5NeverO
+ _theme.once.6173
+ _theme.once.6370
+ _theme.once.6397
+ _theme.once.6421
+ _theme.once.6442
+ _theme.sBehavior.6172
+ _theme.sBehavior.6369
+ _theme.sBehavior.6396
+ _theme.sBehavior.6420
+ _theme.sBehavior.6441
+ _transcriptContactImageDiameter.once.6254
+ _transcriptContactImageDiameter.sBehavior.6253
+ _transcriptGroupTypingContactImageDiameter.once.6258
+ _transcriptGroupTypingContactImageDiameter.sBehavior.6257
+ _transcriptHeaderViewMaxRows.once.6210
+ _transcriptHeaderViewMaxRows.sBehavior.6209
+ _type_layout_string 7ChatKit25TranslationTipEligibilityV
+ _usesActionMenu.once.6383
+ _usesActionMenu.once.6409
+ _usesPopovers.once.6190
+ _usesPopovers.sBehavior.6189
+ _usesUncollapsedSplitview.once.6178
+ _usesUncollapsedSplitview.sBehavior.6177
- -[CKChatController customAcknowledgementDebouncer]
- -[CKChatController setCustomAcknowledgementDebouncer:]
- -[CKChatController transcriptCollectionViewController:balloonViewDidRequestSendCustomAcknowledgementPayload:forPlugin:error:]
- -[CKChatController transcriptCollectionViewController:balloonViewDidRequestSendCustomAcknowledgementPayload:forPlugin:error:].cold.1
- -[CKChatController transcriptCollectionViewController:balloonViewDidRequestSendCustomAcknowledgementPayload:forPlugin:error:].cold.2
- -[CKChatController transcriptCollectionViewController:balloonViewDidRequestSendCustomAcknowledgementPayload:forPlugin:error:].cold.3
- -[CKChatController transcriptCollectionViewController:balloonViewDidRequestSendCustomAcknowledgementPayload:forPlugin:error:].cold.4
- -[CKChatController transcriptCollectionViewController:balloonViewDidRequestSendCustomAcknowledgementPayload:forPlugin:error:].cold.5
- -[CKChatController transcriptCollectionViewController:balloonViewDidRequestSendCustomAcknowledgementPayload:forPlugin:error:].cold.6
- -[CKUIBehavior audioRecordingViewLeadingButtonPadding]
- -[CKUIBehavior audioRecordingViewLeadingButtonPadding].cold.1
- -[CKUIBehavior audioRecordingViewWaveformSpacing]
- -[CKUIBehavior audioRecordingViewWaveformSpacing].cold.1
- GCC_except_table1001
- GCC_except_table1008
- GCC_except_table1013
- GCC_except_table1019
- GCC_except_table1024
- GCC_except_table1028
- GCC_except_table1051
- GCC_except_table1054
- GCC_except_table1061
- GCC_except_table1068
- GCC_except_table1099
- GCC_except_table1101
- GCC_except_table1124
- GCC_except_table1129
- GCC_except_table1131
- GCC_except_table1176
- GCC_except_table1178
- GCC_except_table1180
- GCC_except_table1182
- GCC_except_table1186
- GCC_except_table1190
- GCC_except_table1193
- GCC_except_table1195
- GCC_except_table1197
- GCC_except_table1205
- GCC_except_table1223
- GCC_except_table1234
- GCC_except_table133
- GCC_except_table1589
- GCC_except_table1620
- GCC_except_table1630
- GCC_except_table1631
- GCC_except_table1635
- GCC_except_table1636
- GCC_except_table1648
- GCC_except_table195
- GCC_except_table208
- GCC_except_table221
- GCC_except_table232
- GCC_except_table239
- GCC_except_table246
- GCC_except_table271
- GCC_except_table289
- GCC_except_table295
- GCC_except_table332
- GCC_except_table365
- GCC_except_table369
- GCC_except_table379
- GCC_except_table403
- GCC_except_table409
- GCC_except_table412
- GCC_except_table423
- GCC_except_table438
- GCC_except_table440
- GCC_except_table442
- GCC_except_table462
- GCC_except_table482
- GCC_except_table505
- GCC_except_table513
- GCC_except_table522
- GCC_except_table531
- GCC_except_table557
- GCC_except_table579
- GCC_except_table585
- GCC_except_table588
- GCC_except_table591
- GCC_except_table602
- GCC_except_table605
- GCC_except_table624
- GCC_except_table638
- GCC_except_table641
- GCC_except_table646
- GCC_except_table650
- GCC_except_table657
- GCC_except_table660
- GCC_except_table662
- GCC_except_table667
- GCC_except_table671
- GCC_except_table676
- GCC_except_table680
- GCC_except_table684
- GCC_except_table690
- GCC_except_table693
- GCC_except_table704
- GCC_except_table710
- GCC_except_table730
- GCC_except_table741
- GCC_except_table746
- GCC_except_table758
- GCC_except_table766
- GCC_except_table769
- GCC_except_table771
- GCC_except_table776
- GCC_except_table806
- GCC_except_table809
- GCC_except_table813
- GCC_except_table835
- GCC_except_table844
- GCC_except_table851
- GCC_except_table860
- GCC_except_table871
- GCC_except_table874
- GCC_except_table876
- GCC_except_table899
- GCC_except_table902
- GCC_except_table923
- GCC_except_table927
- GCC_except_table940
- GCC_except_table948
- GCC_except_table950
- GCC_except_table954
- GCC_except_table957
- GCC_except_table962
- GCC_except_table964
- GCC_except_table968
- GCC_except_table974
- GCC_except_table976
- GCC_except_table980
- GCC_except_table982
- GCC_except_table984
- GCC_except_table990
- GCC_except_table992
- GCC_except_table995
- _OBJC_IVAR_$_CKChatController._customAcknowledgementDebouncer
- _OUTLINED_FUNCTION_20
- _OUTLINED_FUNCTION_21
- _OUTLINED_FUNCTION_22
- __OBJC_$_CLASS_METHODS_CKCoreChatController(Backgrounds|Background_Crossplatform|UserSafety|Nicknames|PinningInputViews|UltraConstrainedNetwork|ChatKit|TapbackPicker|ChatKit1|ChatKit2)
- __OBJC_$_INSTANCE_METHODS_CKChatController(MacToolbar|ClickyOrbConformance|CKChatController_Stickers|CKStickerDetailViewControllerDelegate|ChatItemSelection|Debug|ImpactEffectPicker|MenuBar|MessageHistoryViewController|MessageHistoryViewControllerDelegate|SendAnimation|QuickLook|CKNavBarUnifiedCallButton|Collaboration|GroupCollaboration|TipKit|SafetyMonitor|MediaInput|GlassThrowSendAnimation|PhotosSupport|Contacts|Wallet|Location|BackgroundContextMenu|BalloonEmphasis|NavigationBar|TapbackPicker|TapbackPicker_QuickLook|TapbackPicker_Orb|ChatKit|ChatKit1|TapbackPicker_ContextMenu|ChatKit2|ChatKit3|ChatKit4|ChatKit5|CustomAcknowledgement|MenuBarKeyCommands|ChatKit6|ChatKit7|Translation|ChatKit8|ChatKit9|ChatKit10|ChatKit11)
- __OBJC_$_INSTANCE_METHODS_CKCoreChatController(Backgrounds|Background_Crossplatform|UserSafety|Nicknames|PinningInputViews|UltraConstrainedNetwork|ChatKit|TapbackPicker|ChatKit1|ChatKit2)
- __OBJC_CLASS_PROTOCOLS_$_CKChatController(MacToolbar|ClickyOrbConformance|CKChatController_Stickers|CKStickerDetailViewControllerDelegate|ChatItemSelection|Debug|ImpactEffectPicker|MenuBar|MessageHistoryViewController|MessageHistoryViewControllerDelegate|SendAnimation|QuickLook|CKNavBarUnifiedCallButton|Collaboration|GroupCollaboration|TipKit|SafetyMonitor|MediaInput|GlassThrowSendAnimation|PhotosSupport|Contacts|Wallet|Location|BackgroundContextMenu|BalloonEmphasis|NavigationBar|TapbackPicker|TapbackPicker_QuickLook|TapbackPicker_Orb|ChatKit|ChatKit1|TapbackPicker_ContextMenu|ChatKit2|ChatKit3|ChatKit4|ChatKit5|CustomAcknowledgement|MenuBarKeyCommands|ChatKit6|ChatKit7|Translation|ChatKit8|ChatKit9|ChatKit10|ChatKit11)
- ___115-[CKChatController _presentCollabAddToMessagesGroupAlertIfNecessary:collaborationType:sendBlock:completionHandler:]_block_invoke.1412
- ___145-[CKChatController _sendAutomaticallyPlacedSticker:stickerReactionSession:forChatItem:forParentChatItem:stickerFrame:animationCompletionHandler:]_block_invoke.1268
- ___39-[CKChatController addToCollaboration:]_block_invoke.1637
- ___39-[CKChatController addToCollaboration:]_block_invoke_2.1639
- ___45-[CKChatController _handleChatItemDidChange:]_block_invoke.1614
- ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke.789
- ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke.792
- ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke_2.790
- ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke_2.793
- ___47-[CKChatController sendComposition:animations:]_block_invoke.882
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke.1543
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke.1547
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_2.1549
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_3.1553
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_4.1557
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_5.1558
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_6.1562
- ___49-[CKUIBehavior audioRecordingViewWaveformSpacing]_block_invoke
- ___53-[CKChatController _showOrHideNicknameBannerIfNeeded]_block_invoke.1629
- ___54-[CKUIBehavior audioRecordingViewLeadingButtonPadding]_block_invoke
- ___58-[CKChatController chatInputControllerDidSelectFunCamera:]_block_invoke.1264
- ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke.1434
- ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke.1437
- ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke_2.1435
- ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke_2.1439
- ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1319
- ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1320
- ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1321
- ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1321.cold.1
- ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1322
- ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1323
- ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1324
- ___67-[CKChatController _sendCompositionForNewCloudKitShare:completion:]_block_invoke.1383
- ___68-[CKChatController verifyCompositionSendForFileProvider:completion:]_block_invoke.1314
- ___68-[CKChatController verifyCompositionSendForFileProvider:completion:]_block_invoke.1316
- ___69-[CKChatController nicknameBannerView:actionButtonTapped:forUpdates:]_block_invoke.1631
- ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1394
- ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1395
- ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1397
- ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1399
- ___72-[CKChatController _verifyCompositionSendForNewFileProvider:completion:]_block_invoke.1349
- ___72-[CKChatController _verifyCompositionSendForNewFileProvider:completion:]_block_invoke.1350
- ___72-[CKChatController textPasteConfigurationSupporting:transformPasteItem:]_block_invoke.1678
- ___73-[CKChatController _sendCompositionForFileProviderCloudDrive:completion:]_block_invoke.1352
- ___73-[CKChatController _sendCompositionForFileProviderCloudDrive:completion:]_block_invoke.1353
- ___76-[CKChatController _startSharingForURLForFileProviderCloudDrive:completion:]_block_invoke.1360
- ___76-[CKChatController _startSharingForURLForFileProviderCloudDrive:completion:]_block_invoke.1361
- ___77-[CKChatController selectedBalloonIntersectingRect:chatItemForRepositioning:]_block_invoke.1256
- ___81-[CKChatController sendCompositionForCollaboration:collaborationType:completion:]_block_invoke.1400
- ___81-[CKChatController sendCompositionForCollaboration:collaborationType:completion:]_block_invoke.1401
- ___81-[CKChatController sendCompositionForCollaboration:collaborationType:completion:]_block_invoke_2.1402
- ___86-[CKChatController _presentCollabAddToMessagesGroupAlert:sendBlock:completionHandler:]_block_invoke.1427
- ___86-[CKChatController _presentCollabAddToMessagesGroupAlert:sendBlock:completionHandler:]_block_invoke.1428
- ___87-[CKChatController _removeSubsharesAndSendFileProviderComposition:shareURL:completion:]_block_invoke.1374
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1368
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1368.cold.1
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1369
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1371
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1372
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke_2.1373
- ___93-[CKChatController _sendCollaborationCompositionForFileProvider:sharingURL:share:completion:]_block_invoke.1336
- ___93-[CKChatController _sendCollaborationCompositionForFileProvider:sharingURL:share:completion:]_block_invoke.1338
- ___95-[CKChatController _updateAndSendCompositionForExistingCloudKitShare:share:attempt:completion:]_block_invoke.1391
- ___Block_byref_object_copy_.1847
- ___Block_byref_object_dispose_.1848
- ___block_descriptor_56_e8_32s40s48w_e17_v16?0"NSTimer"8lw48l8s32l8s40l8
- ___block_descriptor_81_e8_32s40s48s56s64r72r_e33_v36?0B8{CGSize=dd}12"NSError"28lr64l8s32l8r72l8s40l8s48l8s56l8
- ___block_literal_global.1202
- ___block_literal_global.1236
- ___block_literal_global.1340
- ___block_literal_global.1356
- ___block_literal_global.1361
- ___block_literal_global.1366
- ___block_literal_global.1371
- ___block_literal_global.1376
- ___block_literal_global.1381
- ___block_literal_global.1386
- ___block_literal_global.1391
- ___block_literal_global.1396
- ___block_literal_global.1401
- ___block_literal_global.1406
- ___block_literal_global.1410
- ___block_literal_global.1411
- ___block_literal_global.1416
- ___block_literal_global.1421
- ___block_literal_global.1426
- ___block_literal_global.1430
- ___block_literal_global.1431
- ___block_literal_global.1436
- ___block_literal_global.1438
- ___block_literal_global.1441
- ___block_literal_global.1443
- ___block_literal_global.1445
- ___block_literal_global.1446
- ___block_literal_global.1453
- ___block_literal_global.1455
- ___block_literal_global.1470
- ___block_literal_global.1479
- ___block_literal_global.1481
- ___block_literal_global.1486
- ___block_literal_global.1503
- ___block_literal_global.1505
- ___block_literal_global.1554
- ___block_literal_global.1556
- ___block_literal_global.1560
- ___block_literal_global.1562
- ___block_literal_global.1564
- ___block_literal_global.1566
- ___block_literal_global.1583
- ___block_literal_global.1585
- ___block_literal_global.1587
- ___block_literal_global.1591
- ___block_literal_global.1593
- ___block_literal_global.1595
- ___block_literal_global.1597
- ___block_literal_global.1599
- ___block_literal_global.1601
- ___block_literal_global.1603
- ___block_literal_global.1610
- ___block_literal_global.1612
- ___block_literal_global.1614
- ___block_literal_global.1616
- ___block_literal_global.1618
- ___block_literal_global.1624
- ___block_literal_global.1626
- ___block_literal_global.1628
- ___block_literal_global.1634
- ___block_literal_global.1636
- ___block_literal_global.1638
- ___block_literal_global.1640
- ___block_literal_global.1642
- ___block_literal_global.1644
- ___block_literal_global.1646
- ___block_literal_global.1648
- ___block_literal_global.1650
- ___block_literal_global.1652
- ___block_literal_global.1654
- ___block_literal_global.1656
- ___block_literal_global.1658
- ___block_literal_global.1660
- ___block_literal_global.1662
- ___block_literal_global.1664
- ___block_literal_global.1666
- ___block_literal_global.1668
- ___block_literal_global.1670
- ___block_literal_global.1672
- ___block_literal_global.1674
- ___block_literal_global.1676
- ___block_literal_global.1678
- ___block_literal_global.1680
- ___block_literal_global.1682
- ___block_literal_global.1684
- ___block_literal_global.1686
- ___block_literal_global.1688
- ___block_literal_global.1690
- ___block_literal_global.1692
- ___block_literal_global.1694
- ___block_literal_global.1696
- ___block_literal_global.1698
- ___block_literal_global.1700
- ___block_literal_global.1702
- ___block_literal_global.1704
- ___block_literal_global.1706
- ___block_literal_global.1710
- ___block_literal_global.1712
- ___block_literal_global.1716
- ___block_literal_global.1718
- ___block_literal_global.1720
- ___block_literal_global.1722
- ___block_literal_global.1729
- ___block_literal_global.1731
- ___block_literal_global.1733
- ___block_literal_global.1735
- ___block_literal_global.1737
- ___block_literal_global.1740
- ___block_literal_global.1745
- ___block_literal_global.1753
- ___block_literal_global.1755
- ___block_literal_global.1756
- ___block_literal_global.1757
- ___block_literal_global.1770
- ___block_literal_global.1774
- ___block_literal_global.1778
- ___block_literal_global.1784
- ___block_literal_global.1786
- ___block_literal_global.1790
- ___block_literal_global.1792
- ___block_literal_global.1794
- ___block_literal_global.1796
- ___block_literal_global.1798
- ___block_literal_global.1800
- ___block_literal_global.1804
- ___block_literal_global.1806
- ___block_literal_global.1810
- ___block_literal_global.1812
- ___block_literal_global.1814
- ___block_literal_global.1822
- ___block_literal_global.1830
- ___block_literal_global.1832
- ___block_literal_global.1834
- ___block_literal_global.1836
- ___block_literal_global.1838
- ___block_literal_global.1840
- ___block_literal_global.1842
- ___block_literal_global.1844
- ___block_literal_global.1846
- ___block_literal_global.1848
- ___block_literal_global.1850
- ___block_literal_global.1852
- ___block_literal_global.1854
- ___block_literal_global.1856
- ___block_literal_global.1863
- ___block_literal_global.1865
- ___block_literal_global.1867
- ___block_literal_global.1869
- ___block_literal_global.1871
- ___block_literal_global.1873
- ___block_literal_global.1879
- ___block_literal_global.1881
- ___block_literal_global.1899
- ___block_literal_global.1901
- ___block_literal_global.1903
- ___block_literal_global.1915
- ___block_literal_global.1917
- ___block_literal_global.1919
- ___block_literal_global.1921
- ___block_literal_global.1923
- ___block_literal_global.1925
- ___block_literal_global.1927
- ___block_literal_global.1929
- ___block_literal_global.1931
- ___block_literal_global.1933
- ___block_literal_global.1935
- ___block_literal_global.1937
- ___block_literal_global.1939
- ___block_literal_global.1941
- ___block_literal_global.1943
- ___block_literal_global.1945
- ___block_literal_global.1947
- ___block_literal_global.1949
- ___block_literal_global.1951
- ___block_literal_global.1953
- ___block_literal_global.1955
- ___block_literal_global.1957
- ___block_literal_global.1959
- ___block_literal_global.1961
- ___block_literal_global.1963
- ___block_literal_global.1965
- ___block_literal_global.1969
- ___block_literal_global.1971
- ___block_literal_global.1973
- ___block_literal_global.1975
- ___block_literal_global.1979
- ___block_literal_global.1981
- ___block_literal_global.1983
- ___block_literal_global.1985
- ___block_literal_global.1987
- ___block_literal_global.1989
- ___block_literal_global.1991
- ___block_literal_global.1998
- ___block_literal_global.2000
- ___block_literal_global.2002
- ___block_literal_global.2004
- ___block_literal_global.2006
- ___block_literal_global.2008
- ___block_literal_global.2010
- ___block_literal_global.2012
- ___block_literal_global.2014
- ___block_literal_global.2016
- ___block_literal_global.2018
- ___block_literal_global.2020
- ___block_literal_global.2022
- ___block_literal_global.2024
- ___block_literal_global.2026
- ___block_literal_global.2028
- ___block_literal_global.2030
- ___block_literal_global.2032
- ___block_literal_global.2039
- ___block_literal_global.2071
- ___block_literal_global.2105
- ___block_literal_global.2107
- ___block_literal_global.2109
- ___block_literal_global.2111
- ___block_literal_global.2113
- ___block_literal_global.2115
- ___block_literal_global.2117
- ___block_literal_global.2119
- ___block_literal_global.2146
- ___block_literal_global.2148
- ___block_literal_global.2157
- ___block_literal_global.2159
- ___block_literal_global.2161
- ___block_literal_global.2169
- ___block_literal_global.2171
- ___block_literal_global.2173
- ___block_literal_global.2175
- ___block_literal_global.2177
- ___block_literal_global.2179
- ___block_literal_global.2181
- ___block_literal_global.2183
- ___block_literal_global.2185
- ___block_literal_global.2187
- ___block_literal_global.2189
- ___block_literal_global.2191
- ___block_literal_global.2193
- ___block_literal_global.2195
- ___block_literal_global.2197
- ___block_literal_global.2199
- ___block_literal_global.2201
- ___block_literal_global.2207
- ___block_literal_global.2209
- ___block_literal_global.2211
- ___block_literal_global.2213
- ___block_literal_global.2215
- ___block_literal_global.2217
- ___block_literal_global.2221
- ___block_literal_global.2223
- ___block_literal_global.2225
- ___block_literal_global.2227
- ___block_literal_global.2229
- ___block_literal_global.2231
- ___block_literal_global.2233
- ___block_literal_global.2235
- ___block_literal_global.2237
- ___block_literal_global.2239
- ___block_literal_global.2241
- ___block_literal_global.2243
- ___block_literal_global.2247
- ___block_literal_global.2251
- ___block_literal_global.2255
- ___block_literal_global.2259
- ___block_literal_global.2263
- ___block_literal_global.2265
- ___block_literal_global.2267
- ___block_literal_global.2269
- ___block_literal_global.2271
- ___block_literal_global.2275
- ___block_literal_global.2341
- ___block_literal_global.2400
- ___block_literal_global.2402
- ___block_literal_global.2404
- ___block_literal_global.2406
- ___block_literal_global.2408
- ___block_literal_global.2415
- ___block_literal_global.2417
- ___block_literal_global.2421
- ___block_literal_global.2423
- ___block_literal_global.2430
- ___block_literal_global.2432
- ___block_literal_global.2434
- ___block_literal_global.2436
- ___block_literal_global.2438
- ___block_literal_global.2440
- ___block_literal_global.2442
- ___block_literal_global.2444
- ___block_literal_global.2446
- ___block_literal_global.2448
- ___block_literal_global.2450
- ___block_literal_global.2452
- ___block_literal_global.2454
- ___block_literal_global.2456
- ___block_literal_global.2458
- ___block_literal_global.2460
- ___block_literal_global.2462
- ___block_literal_global.2464
- ___block_literal_global.2466
- ___block_literal_global.2468
- ___block_literal_global.2470
- ___block_literal_global.2472
- ___block_literal_global.2474
- ___block_literal_global.2476
- ___block_literal_global.2478
- ___block_literal_global.2480
- ___block_literal_global.2487
- ___block_literal_global.2489
- ___block_literal_global.2491
- ___block_literal_global.2493
- ___block_literal_global.2495
- ___block_literal_global.2497
- ___block_literal_global.2499
- ___block_literal_global.2501
- ___block_literal_global.2503
- ___block_literal_global.2505
- ___block_literal_global.2507
- ___block_literal_global.2509
- ___block_literal_global.2511
- ___block_literal_global.2513
- ___block_literal_global.2515
- ___block_literal_global.2517
- ___block_literal_global.2519
- ___block_literal_global.2521
- ___block_literal_global.2523
- ___block_literal_global.2525
- ___block_literal_global.2527
- ___block_literal_global.2529
- ___block_literal_global.2531
- ___block_literal_global.2533
- ___block_literal_global.2535
- ___block_literal_global.2537
- ___block_literal_global.2539
- ___block_literal_global.2541
- ___block_literal_global.2543
- ___block_literal_global.2545
- ___block_literal_global.2547
- ___block_literal_global.2549
- ___block_literal_global.2551
- ___block_literal_global.2553
- ___block_literal_global.2555
- ___block_literal_global.2557
- ___block_literal_global.2559
- ___block_literal_global.2561
- ___block_literal_global.2563
- ___block_literal_global.2565
- ___block_literal_global.2567
- ___block_literal_global.2569
- ___block_literal_global.2571
- ___block_literal_global.2573
- ___block_literal_global.2575
- ___block_literal_global.2577
- ___block_literal_global.2579
- ___block_literal_global.2581
- ___block_literal_global.2583
- ___block_literal_global.2585
- ___block_literal_global.2587
- ___block_literal_global.2589
- ___block_literal_global.2591
- ___block_literal_global.2593
- ___block_literal_global.2595
- ___block_literal_global.2597
- ___block_literal_global.2599
- ___block_literal_global.2601
- ___block_literal_global.2603
- ___block_literal_global.2605
- ___block_literal_global.2607
- ___block_literal_global.2609
- ___block_literal_global.2611
- ___block_literal_global.2613
- ___block_literal_global.2615
- ___block_literal_global.2617
- ___block_literal_global.2619
- ___block_literal_global.2626
- ___block_literal_global.2628
- ___block_literal_global.2630
- ___block_literal_global.2632
- ___block_literal_global.2634
- ___block_literal_global.2636
- ___block_literal_global.2638
- ___block_literal_global.2640
- ___block_literal_global.2642
- ___block_literal_global.2644
- ___block_literal_global.2646
- ___block_literal_global.2648
- ___block_literal_global.2650
- ___block_literal_global.2652
- ___block_literal_global.2654
- ___block_literal_global.2656
- ___block_literal_global.2658
- ___block_literal_global.2660
- ___block_literal_global.2662
- ___block_literal_global.2664
- ___block_literal_global.2666
- ___block_literal_global.2668
- ___block_literal_global.4127
- ___block_literal_global.4137
- ___block_literal_global.4139
- ___block_literal_global.530
- ___block_literal_global.579
- ___block_literal_global.6177
- ___block_literal_global.6189
- ___block_literal_global.6193
- ___block_literal_global.6197
- ___block_literal_global.6201
- ___block_literal_global.6205
- ___block_literal_global.6209
- ___block_literal_global.6213
- ___block_literal_global.6217
- ___block_literal_global.6221
- ___block_literal_global.6225
- ___block_literal_global.6229
- ___block_literal_global.6233
- ___block_literal_global.6237
- ___block_literal_global.6243
- ___block_literal_global.6247
- ___block_literal_global.6251
- ___block_literal_global.6257
- ___block_literal_global.6265
- ___block_literal_global.6269
- ___block_literal_global.6272
- ___block_literal_global.6276
- ___block_literal_global.6280
- ___block_literal_global.6284
- ___block_literal_global.6288
- ___block_literal_global.6292
- ___block_literal_global.6296
- ___block_literal_global.6300
- ___block_literal_global.6304
- ___block_literal_global.6308
- ___block_literal_global.6312
- ___block_literal_global.6316
- ___block_literal_global.6320
- ___block_literal_global.6324
- ___block_literal_global.6328
- ___block_literal_global.6332
- ___block_literal_global.6334
- ___block_literal_global.6338
- ___block_literal_global.6342
- ___block_literal_global.6346
- ___block_literal_global.6360
- ___block_literal_global.6362
- ___block_literal_global.6364
- ___block_literal_global.6368
- ___block_literal_global.6386
- ___block_literal_global.6390
- ___block_literal_global.6394
- ___block_literal_global.6408
- ___block_literal_global.6412
- ___block_literal_global.6416
- ___block_literal_global.6420
- ___block_literal_global.6437
- ___block_literal_global.6441
- ___block_literal_global.6445
- ___block_literal_global.6453
- ___block_literal_global.6457
- ___block_literal_global.6461
- ___block_literal_global.6465
- ___block_literal_global.6471
- ___block_literal_global.6473
- ___block_literal_global.6475
- ___block_literal_global.6477
- ___block_literal_global.6479
- ___block_literal_global.855
- ___block_literal_global.861
- _areBannersSupported.once.6435
- _areBannersSupported.once.6455
- _attachmentBrowserDefaultSizeForSquare.once.6318
- _attachmentBrowserDefaultSizeForSquare.sBehavior.6317.0
- _attachmentBrowserDefaultSizeForSquare.sBehavior.6317.1
- _attachmentBrowserGridInterItemSpacing.once.6322
- _attachmentBrowserGridInterItemSpacing.sBehavior.6321
- _audioRecordingViewLeadingButtonPadding.once
- _audioRecordingViewWaveformSpacing.once
- _canPresentOverKeyboard.once.6203
- _canShowContactPhotosInConversationList.once.6239
- _canShowContactPhotosInConversationList.sBehavior.6238
- _contactPhotoTranscriptInsets.sBehavior.6270
- _conversationListMinimumWidthForHiddenContactImage.once.6255
- _conversationListMinimumWidthForHiddenContactImage.sBehavior.6254
- _conversationListMultiSelectAccessoryUsesDefaultStyling.once.6249
- _conversationListMultiSelectAccessoryUsesDefaultStyling.sBehavior.6248
- _conversationListPrefersEditButtonOnTrailingEdge.once.6245
- _conversationListPrefersEditButtonOnTrailingEdge.sBehavior.6244
- _defaultAVPlayerViewContorllerControlsInsets.once.6278
- _defaultAVPlayerViewContorllerControlsInsets.sBehavior.6277.0
- _defaultAVPlayerViewContorllerControlsInsets.sBehavior.6277.1
- _defaultAVPlayerViewContorllerControlsInsets.sBehavior.6277.2
- _defaultAVPlayerViewContorllerControlsInsets.sBehavior.6277.3
- _defaultConversationViewingMessageCount.once.6231
- _defaultConversationViewingMessageCount.sBehavior.6230
- _detonatedItemBalloonViewSize.once.6366
- _detonatedItemBalloonViewSize.sBehavior.6365.0
- _detonatedItemBalloonViewSize.sBehavior.6365.1
- _detonatedItemDocumentIconSize.once.6370
- _detonatedItemDocumentIconSize.sBehavior.6369.0
- _detonatedItemDocumentIconSize.sBehavior.6369.1
- _documentIconSize.once.6282
- _documentIconSize.sBehavior.6281.0
- _documentIconSize.sBehavior.6281.1
- _entryFieldShouldUseBackdropView.once.6388
- _entryFieldShouldUseBackdropView.once.6414
- _entryViewAlwaysUsesConcentricPadding.once.6298
- _entryViewAlwaysUsesConcentricPadding.sBehavior.6297
- _entryViewConcentricPadding.once.6302
- _entryViewConcentricPadding.sBehavior.6301
- _entryViewHorizontalCoverInsets.once.6400
- _entryViewHorizontalCoverInsets.once.6425
- _entryViewHorizontalCoverInsets.sBehavior.6399.0
- _entryViewHorizontalCoverInsets.sBehavior.6399.1
- _entryViewHorizontalCoverInsets.sBehavior.6399.2
- _entryViewHorizontalCoverInsets.sBehavior.6399.3
- _entryViewHorizontalCoverInsets.sBehavior.6424.0
- _entryViewHorizontalCoverInsets.sBehavior.6424.1
- _entryViewHorizontalCoverInsets.sBehavior.6424.2
- _entryViewHorizontalCoverInsets.sBehavior.6424.3
- _entryViewMaxHandWritingPluginShelfHeight.once.6314
- _entryViewMaxHandWritingPluginShelfHeight.sBehavior.6313
- _entryViewVerticalCoverInsets.once.6396
- _entryViewVerticalCoverInsets.once.6422
- _entryViewVerticalCoverInsets.sBehavior.6395
- _entryViewVerticalCoverInsets.sBehavior.6421
- _get_witness_table 7SwiftUI4ViewRzlAA05TupleC0VyAaBPAAE5alert_11isPresented7actionsQrqd___AA7BindingVySbGqd_0_yXEtSyRd__AaBRd_0_r0_lFQOyAA5GroupVyADyAA19_ConditionalContentVyAA7SectionVyAA05EmptyC0VAA08ModifiedL0VyAeAE11toggleStyleyQrqd__AA06ToggleQ0Rd__lFQOyAA0R0VyAA4TextVG_AA06SwitchrQ0VQo_7ChatKit07Detailsc3RowQ0VGAUyAUyA4_019SharedWithYouFooterC0VAA21_TraitWritingModifierVyAA04ListX18BackgroundTraitKeyVGGAA14_PaddingLayoutVGGASG_AUyAQyAsDyA3_Sg_A21_A21_tGASGA6_GAA012SubscriptionC0VySo20NSNotificationCenterC10FoundationE9PublisherVAUyAQyAsDyA3__AOyAeAE06pickerQ0yQrqd__AA06PickerQ0Rd__lFQOyAA6PickerVyA_SSADyAA7ForEachVySaySSGSSAeAE3tag_15includeOptionalQrqd___SbtSHRd__lFQOyA__SSQo_G_A41_SgtGG_AA013DefaultPickerQ0VQo_AUyAA6ButtonVyA_GA6_GGSgtGASGA6_GGSgAUyAeAE18confirmationDialog_AG15titleVisibilityAHQrAA18LocalizedStringKeyV_AkA10VisibilityOqd__yXEtAaBRd__lFQOyAUyA51_AA32_EnvironmentKeyTransformModifierVySbGG_A51_Qo_A6_GSgAUyAeAEA60__AGA61_AHQrA63__AKA65_qd__yXEtAaBRd__lFQOyA51__A51_Qo_A6_GSgtGG_SSADyA51__A51_tGQo__AUyxA14_GSgtGAaBHPyHC.241
- _get_witness_table 7SwiftUI7SectionVyAA9EmptyViewVAA05TupleE0VyAA0E0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaHRd__lFQOyAiAEAjklMQrAP_AQqd__yctAaHRd__lFQOyAiAE18confirmationDialog_AK15titleVisibility7actions7messageQrqd___ApA0Q0Oqd_0_yXEqd_1_yXEtSyRd__AaHRd_0_AaHRd_1_r1_lFQOyAiAE5alert_AktUQrqd___APqd_0_yXEqd_1_yXEtSyRd__AaHRd_0_AaHRd_1_r1_lFQOyAA15ModifiedContentVyAiAE11toggleStyleyQrqd__AA06ToggleX0Rd__lFQOyAA0Y0VyAA6VStackVyAGyAZyAA4TextVAA16_FlexFrameLayoutVG_AA012_ConditionalV0VyA11_yA11_yA9_A9_GAEGA11_yAEA9_GGtGGG_AA06SwitchyX0VQo_AA30_EnvironmentKeyWritingModifierVyAA5ColorVSgGG_SSAGyAA6ButtonVyA6_G_A31_tGA6_Qo__SSAGyA11_yAiAE16keyboardShortcutyQrAA16KeyboardShortcutVFQOyA31__Qo_A31_GSg_A31_tGA6_Qo__7ChatKit019CKLanguageSelectionE0VQo__A44_Qo__A11_yA11_yAEA31_GAiAE06buttonX0yQrqd__AA015PrimitiveButtonX0Rd__lFQOyA30_yAA07LabeledV0VyA6_A6_GG_AA020NavigationLinkButtonX0Vys5NeverOGQo_GA11_yA11_yA2EGA59_GtGAEGAaHHPAeaHHPyHC_A63_AaHHPyHCAeaHHPyHCHC.88
- _groupRecipientSelectionPresentationStyle.once.6344
- _groupRecipientSelectionPresentationStyle.sBehavior.6343
- _isAppStripInKeyboard.once.6306
- _joystickUsesWindow.once.6384
- _joystickUsesWindow.once.6410
- _keyboardSizeDeterminesAppCardDetentHeight.once.6207
- _lowClearanceInLandscape.once.6195
- _minTranscriptMarginInsets.once.6274
- _minTranscriptMarginInsets.sBehavior.6273.1
- _minTranscriptMarginInsets.sBehavior.6273.3
- _numberOfButtonsInPhotoPicker.once.6330
- _numberOfButtonsInPhotoPicker.sBehavior.6329
- _objc_msgSend$buttonFor:with:
- _objc_msgSend$messageEntryViewSendButtonHitWhileDisabled:
- _photoPickerMaxPopoverPhotoHeight.once.6336
- _photoPickerMaxPopoverPhotoHeight.sBehavior.6335
- _photoPickerPopoverWidth.once.6326
- _photoPickerPopoverWidth.sBehavior.6325
- _presentForwardingUIModally.once.6215
- _presentsAutocompleteInAPopover.once.6294
- _presentsQuickLookController.once.6211
- _presentsQuickLookController.sBehavior.6210
- _previewMaxWidth.once.6259
- _previewMaxWidth.sBehavior.6258
- _resetsIdleTimer.once.6443
- _resetsIdleTimer.once.6463
- _searchLinksThumbnailWidth.once.6356
- _searchLinksThumbnailWidth.sBehavior.6355
- _searchPhotosThumbnailWidth.once.6354
- _searchPhotosThumbnailWidth.sBehavior.6353
- _shouldAlignRecipientGlyphsWithMargins.once.6340
- _shouldAlignRecipientGlyphsWithMargins.sBehavior.6339
- _shouldRefreshAlternateAddressesSheet.once.6290
- _shouldRefreshAlternateAddressesSheet.sBehavior.6289
- _shouldShowDisclosureChevronInRecipientAtoms.once.6286
- _shouldSuppressRotationInNewCompose.once.6191
- _shouldUnreadIndicatorChangeOnSelection.once.6253
- _shouldUnreadIndicatorChangeOnSelection.sBehavior.6252
- _shouldUseSimpleTimestampsInTranscript.once.6439
- _shouldUseSimpleTimestampsInTranscript.once.6459
- _shouldUseSimpleTimestampsInTranscript.sBehavior.6438
- _shouldUseSimpleTimestampsInTranscript.sBehavior.6458
- _showMMSSetup.once.6227
- _showPendingInConversationList.once.6235
- _showPendingInConversationList.sBehavior.6234
- _showsConversationListCellChevronImage.once.6241
- _showsConversationListCellChevronImage.sBehavior.6240
- _suggestedAppStripLimit.once.6358
- _suggestedAppStripLimit.sBehavior.6357
- _supportedInterfaceOrientations.once.6223
- _supportedInterfaceOrientations.sBehavior.6222
- _supportsEntryViewPlusButtonLongPress.once.6310
- _supportsEntryViewPlusButtonLongPress.sBehavior.6309
- _symbolic _____ 6TipKit4TipsO6ActionV
- _symbolic _____ySaySSGSS_____y______SSQo_G 7SwiftUI7ForEachV AA4ViewPAAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA4TextV
- _symbolic _____ySaySSGSS_____y______SSQo_G_ADSgt 7SwiftUI7ForEachV AA4ViewPAAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA4TextV
- _symbolic _____y_____SS_____y_____ySaySSGSS_____yAB_SSQo_G_AFSgtGG 7SwiftUI6PickerV AA4TextV AA9TupleViewV AA7ForEachV AA0F0PAAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO
- _symbolic _____y__________y_____y__________y_____y_____y_____G______Qo_______y_____y_____yAHSSAFy_____ySaySSGSS_____yAH_SSQo_G_APSgtGG______Qo_ACy_____yAHG_____GGSgtGAEGAYGG 7SwiftUI16SubscriptionViewV So20NSNotificationCenterC10FoundationE9PublisherV AA15ModifiedContentV AA7SectionV AA05EmptyD0V AA05TupleD0V AA0D0PAAE11toggleStyleyQrqd__AA06ToggleO0Rd__lFQO AA0P0V AA4TextV AA06SwitchpO0V AA012_ConditionalJ0V ArAE06pickerO0yQrqd__AA06PickerO0Rd__lFQO AA0U0V AA7ForEachV ArAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA07DefaultuO0V AA6ButtonV 7ChatKit07Detailsd3RowO0V
- _symbolic _____y__________y_____y__________y_____y_____y_____G______Qo_______y_____y_____yAHSSAFy_____ySaySSGSS_____yAH_SSQo_G_APSgtGG______Qo_ACy_____yAHG_____GGSgtGAEGAYGGSg 7SwiftUI16SubscriptionViewV So20NSNotificationCenterC10FoundationE9PublisherV AA15ModifiedContentV AA7SectionV AA05EmptyD0V AA05TupleD0V AA0D0PAAE11toggleStyleyQrqd__AA06ToggleO0Rd__lFQO AA0P0V AA4TextV AA06SwitchpO0V AA012_ConditionalJ0V ArAE06pickerO0yQrqd__AA06PickerO0Rd__lFQO AA0U0V AA7ForEachV ArAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA07DefaultuO0V AA6ButtonV 7ChatKit07Detailsd3RowO0V
- _symbolic _____y__________y_____y_____y_____y_____y_____y_____y_____y_____yACyADy__________G______yAJyAJyA2IGABGAJyAbIGGtGGG______Qo______y_____SgGG_SSACy_____yAGG_AZtGAGQo__SSACyAJy_____yAZ_Qo_AZGSg_AZtGAGQo_______Qo__A6_Qo__AJyAJyAbZG_____yAYy_____yA2GGG______y_____GQo_GAJyAJyA2BGA16_GtGABG 7SwiftUI7SectionV AA9EmptyViewV AA05TupleE0V AA0E0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaHRd__lFQO AiAEAjklMQrAP_AQqd__yctAaHRd__lFQO AiAE18confirmationDialog_AK15titleVisibility7actions7messageQrqd___ApA0Q0Oqd_0_yXEqd_1_yXEtSyRd__AaHRd_0_AaHRd_1_r1_lFQO AiAE5alert_AktUQrqd___APqd_0_yXEqd_1_yXEtSyRd__AaHRd_0_AaHRd_1_r1_lFQO AA15ModifiedContentV AiAE11toggleStyleyQrqd__AA06ToggleX0Rd__lFQO AA0Y0V AA6VStackV AA4TextV AA16_FlexFrameLayoutV AA012_ConditionalV0V AA06SwitchyX0V AA30_EnvironmentKeyWritingModifierV AA5ColorV AA6ButtonV AiAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO 7ChatKit019CKLanguageSelectionE0V AiAE06buttonX0yQrqd__AA015PrimitiveButtonX0Rd__lFQO AA07LabeledV0V AA020NavigationLinkButtonX0V s5NeverO
- _symbolic _____y_____ySaySSGSS_____y______SSQo_G_AESgtG 7SwiftUI9TupleViewV AA7ForEachV AA0D0PAAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA4TextV
- _symbolic _____y_____y_____G______Qo_______y_____y_____yABSS_____y_____ySaySSGSS_____yAB_SSQo_G_AKSgtGG______Qo______y_____yABG_____GGSgt 7SwiftUI4ViewPAAE11toggleStyleyQrqd__AA06ToggleE0Rd__lFQO AA0F0V AA4TextV AA06SwitchfE0V AA19_ConditionalContentV AcAE06pickerE0yQrqd__AA06PickerE0Rd__lFQO AA0L0V AA05TupleC0V AA7ForEachV AcAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA07DefaultlE0V AA08ModifiedJ0V AA6ButtonV 7ChatKit07Detailsc3RowE0V
- _symbolic _____y_____y_____SS_____y_____ySaySSGSS_____yAB_SSQo_G_AFSgtGG______Qo_ 7SwiftUI4ViewPAAE11pickerStyleyQrqd__AA06PickerE0Rd__lFQO AA0F0V AA4TextV AA05TupleC0V AA7ForEachV AcAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA07DefaultfE0V
- _symbolic _____y_____y__________y_____y_____y_____G______Qo______GADyADy__________y_____GG_____GGACG_ADyAByAC_____yAISg_A2VtGACGAJG_____y_____ADyAByAcUyAI_AAy_____y_____yAFSSAUy_____ySaySSGSS_____yAF_SSQo_G_A3_SgtGG______Qo_ADy_____yAFGAJGGSgtGACGAJGGSgADy_____yADyA11______ySbGG_A11_Qo_AJGSgADy_____yA11__A11_Qo_AJGSgt 7SwiftUI19_ConditionalContentV AA7SectionV AA9EmptyViewV AA08ModifiedD0V AA0G0PAAE11toggleStyleyQrqd__AA06ToggleJ0Rd__lFQO AA0K0V AA4TextV AA06SwitchkJ0V 7ChatKit07Detailsg3RowJ0V AT019SharedWithYouFooterG0V AA21_TraitWritingModifierV AA04Listq10BackgroundV3KeyV AA14_PaddingLayoutV AA05TupleG0V AA012SubscriptionG0V So20NSNotificationCenterC10FoundationE9PublisherV AkAE06pickerJ0yQrqd__AA06PickerJ0Rd__lFQO AA6PickerV AA7ForEachV AkAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA013DefaultPickerJ0V AA6ButtonV AkAE18confirmationDialog_11isPresented15titleVisibility7actionsQrAA18LocalizedStringKeyV_AA7BindingVySbGAA10VisibilityOqd__yXEtAaJRd__lFQO AA024_EnvironmentKeyTransformX0V AkAEA24__A25_A26_A27_QrA29__A32_A34_qd__yXEtAaJRd__lFQO
- _symbolic _____y_____y__________y_____y_____y_____G______Qo_______y_____y_____yAFSSADy_____ySaySSGSS_____yAF_SSQo_G_ANSgtGG______Qo_AAy_____yAFG_____GGSgtGACGAWG 7SwiftUI15ModifiedContentV AA7SectionV AA9EmptyViewV AA05TupleG0V AA0G0PAAE11toggleStyleyQrqd__AA06ToggleJ0Rd__lFQO AA0K0V AA4TextV AA06SwitchkJ0V AA012_ConditionalD0V AkAE06pickerJ0yQrqd__AA06PickerJ0Rd__lFQO AA0P0V AA7ForEachV AkAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA07DefaultpJ0V AA6ButtonV 7ChatKit07Detailsg3RowJ0V
- _symbolic _____y_____y_____yAAy_____y_____y__________y_____y_____y_____G______Qo______GAFyAFy__________y_____GG_____GGAEG_AFyADyAeAyAKSg_A2WtGAEGALG_____y_____AFyADyAeAyAK_ACy_____y_____yAHSSAAy_____ySaySSGSS_____yAH_SSQo_G_A4_SgtGG______Qo_AFy_____yAHGALGGSgtGAEGALGGSgAFy_____yAFyA12______ySbGG_A12_Qo_ALGSgAFy_____yA12__A12_Qo_ALGSgtGG_SSAAyA12__A12_tGQo__AFyxAQGSgtG 7SwiftUI9TupleViewV AA0D0PAAE5alert_11isPresented7actionsQrqd___AA7BindingVySbGqd_0_yXEtSyRd__AaDRd_0_r0_lFQO AA5GroupV AA19_ConditionalContentV AA7SectionV AA05EmptyD0V AA08ModifiedL0V AeAE11toggleStyleyQrqd__AA06ToggleQ0Rd__lFQO AA0R0V AA4TextV AA06SwitchrQ0V 7ChatKit07Detailsd3RowQ0V A2_019SharedWithYouFooterD0V AA21_TraitWritingModifierV AA04ListX18BackgroundTraitKeyV AA14_PaddingLayoutV AA012SubscriptionD0V So20NSNotificationCenterC10FoundationE9PublisherV AeAE06pickerQ0yQrqd__AA06PickerQ0Rd__lFQO AA6PickerV AA7ForEachV AeAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA013DefaultPickerQ0V AA6ButtonV AeAE18confirmationDialog_AG15titleVisibilityAHQrAA18LocalizedStringKeyV_AkA10VisibilityOqd__yXEtAaDRd__lFQO AA32_EnvironmentKeyTransformModifierV AeAEA32__AGA33_AHQrA35__AKA37_qd__yXEtAaDRd__lFQO
- _symbolic _____y_____y_____y_____G_Qo_ADG 7SwiftUI19_ConditionalContentV AA4ViewPAAE16keyboardShortcutyQrAA08KeyboardG0VFQO AA6ButtonV AA4TextV
- _symbolic _____y_____y_____y_____G_Qo_ADGSg 7SwiftUI19_ConditionalContentV AA4ViewPAAE16keyboardShortcutyQrAA08KeyboardG0VFQO AA6ButtonV AA4TextV
- _symbolic _____y_____y_____y_____G_Qo_ADGSg_ADt 7SwiftUI19_ConditionalContentV AA4ViewPAAE16keyboardShortcutyQrAA08KeyboardG0VFQO AA6ButtonV AA4TextV
- _symbolic _____y_____y_____y_____G_Qo_AD_G 7SwiftUI19_ConditionalContentV7StorageO AA4ViewPAAE16keyboardShortcutyQrAA08KeyboardH0VFQO AA6ButtonV AA4TextV
- _symbolic _____y_____y_____y_____G______Qo_______y_____y_____yACSSAAy_____ySaySSGSS_____yAC_SSQo_G_AKSgtGG______Qo______y_____yACG_____GGSgtG 7SwiftUI9TupleViewV AA0D0PAAE11toggleStyleyQrqd__AA06ToggleF0Rd__lFQO AA0G0V AA4TextV AA06SwitchgF0V AA19_ConditionalContentV AeAE06pickerF0yQrqd__AA06PickerF0Rd__lFQO AA0M0V AA7ForEachV AeAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA07DefaultmF0V AA08ModifiedK0V AA6ButtonV 7ChatKit07Detailsd3RowF0V
- _symbolic _____y_____y_____y_____SS_____y_____ySaySSGSS_____yAC_SSQo_G_AGSgtGG______Qo______y_____yACG_____GG 7SwiftUI19_ConditionalContentV AA4ViewPAAE11pickerStyleyQrqd__AA06PickerG0Rd__lFQO AA0H0V AA4TextV AA05TupleE0V AA7ForEachV AeAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA07DefaulthG0V AA08ModifiedD0V AA6ButtonV 7ChatKit07Detailse3RowG0V
- _symbolic _____y_____y_____y_____SS_____y_____ySaySSGSS_____yAC_SSQo_G_AGSgtGG______Qo______y_____yACG_____GGSg 7SwiftUI19_ConditionalContentV AA4ViewPAAE11pickerStyleyQrqd__AA06PickerG0Rd__lFQO AA0H0V AA4TextV AA05TupleE0V AA7ForEachV AeAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA07DefaulthG0V AA08ModifiedD0V AA6ButtonV 7ChatKit07Detailse3RowG0V
- _symbolic _____y_____y_____y_____SS_____y_____ySaySSGSS_____yAC_SSQo_G_AGSgtGG______Qo______y_____yACG_____G_G 7SwiftUI19_ConditionalContentV7StorageO AA4ViewPAAE11pickerStyleyQrqd__AA06PickerH0Rd__lFQO AA0I0V AA4TextV AA05TupleF0V AA7ForEachV AgAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA07DefaultiH0V AA08ModifiedD0V AA6ButtonV 7ChatKit07Detailsf3RowH0V
- _symbolic _____y_____y_____y__________y_____y_____y_____G______Qo______GAEyAEy__________y_____GG_____GGADG_AEyACyAdAyAJSg_A2VtGADGAKG_____y_____AEyACyAdAyAJ_ABy_____y_____yAGSSAAy_____ySaySSGSS_____yAG_SSQo_G_A3_SgtGG______Qo_AEy_____yAGGAKGGSgtGADGAKGGSgAEy_____yAEyA11______ySbGG_A11_Qo_AKGSgAEy_____yA11__A11_Qo_AKGSgtG 7SwiftUI9TupleViewV AA19_ConditionalContentV AA7SectionV AA05EmptyD0V AA08ModifiedF0V AA0D0PAAE11toggleStyleyQrqd__AA06ToggleK0Rd__lFQO AA0L0V AA4TextV AA06SwitchlK0V 7ChatKit07Detailsd3RowK0V AV019SharedWithYouFooterD0V AA21_TraitWritingModifierV AA04Listr10BackgroundW3KeyV AA14_PaddingLayoutV AA012SubscriptionD0V So20NSNotificationCenterC10FoundationE9PublisherV AmAE06pickerK0yQrqd__AA06PickerK0Rd__lFQO AA6PickerV AA7ForEachV AmAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA013DefaultPickerK0V AA6ButtonV AmAE18confirmationDialog_11isPresented15titleVisibility7actionsQrAA18LocalizedStringKeyV_AA7BindingVySbGAA10VisibilityOqd__yXEtAaLRd__lFQO AA024_EnvironmentKeyTransformY0V AmAEA24__A25_A26_A27_QrA29__A32_A34_qd__yXEtAaLRd__lFQO
- _symbolic _____y_____y_____y_____y_____G_Qo_AEGSg_AEtG 7SwiftUI9TupleViewV AA19_ConditionalContentV AA0D0PAAE16keyboardShortcutyQrAA08KeyboardH0VFQO AA6ButtonV AA4TextV
- _symbolic _____y_____y_____y_____y__________y_____y_____y_____G______Qo______GAFyAFy__________y_____GG_____GGAEG_AFyADyAeByAKSg_A2WtGAEGALG_____y_____AFyADyAeByAK_ACy_____y_____yAHSSABy_____ySaySSGSS_____yAH_SSQo_G_A4_SgtGG______Qo_AFy_____yAHGALGGSgtGAEGALGGSgAFy_____yAFyA12______ySbGG_A12_Qo_ALGSgAFy_____yA12__A12_Qo_ALGSgtGG 7SwiftUI5GroupV AA9TupleViewV AA19_ConditionalContentV AA7SectionV AA05EmptyE0V AA08ModifiedG0V AA0E0PAAE11toggleStyleyQrqd__AA06ToggleL0Rd__lFQO AA0M0V AA4TextV AA06SwitchmL0V 7ChatKit07Detailse3RowL0V AX019SharedWithYouFooterE0V AA21_TraitWritingModifierV AA04Lists10BackgroundX3KeyV AA14_PaddingLayoutV AA012SubscriptionE0V So20NSNotificationCenterC10FoundationE9PublisherV AoAE06pickerL0yQrqd__AA06PickerL0Rd__lFQO AA6PickerV AA7ForEachV AoAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA013DefaultPickerL0V AA6ButtonV AoAE18confirmationDialog_11isPresented15titleVisibility7actionsQrAA18LocalizedStringKeyV_AA7BindingVySbGAA10VisibilityOqd__yXEtAaNRd__lFQO AA024_EnvironmentKeyTransformZ0V AoAEA26__A27_A28_A29_QrA31__A34_A36_qd__yXEtAaNRd__lFQO
- _symbolic _____y_____y_____y_____y_____y__________y_____y_____y_____G______Qo______GAFyAFy__________y_____GG_____GGAEG_AFyADyAeByAKSg_A2WtGAEGALG_____y_____AFyADyAeByAK_ACy_____y_____yAHSSABy_____ySaySSGSS_____yAH_SSQo_G_A4_SgtGG______Qo_AFy_____yAHGALGGSgtGAEGALGGSgAFy_____yAFyA12______ySbGG_A12_Qo_ALGSgAFy_____yA12__A12_Qo_ALGSgtGG_SSAByA12__A12_tGQo_ 7SwiftUI4ViewPAAE5alert_11isPresented7actionsQrqd___AA7BindingVySbGqd_0_yXEtSyRd__AaBRd_0_r0_lFQO AA5GroupV AA05TupleC0V AA19_ConditionalContentV AA7SectionV AA05EmptyC0V AA08ModifiedL0V AcAE11toggleStyleyQrqd__AA06ToggleQ0Rd__lFQO AA0R0V AA4TextV AA06SwitchrQ0V 7ChatKit07Detailsc3RowQ0V A2_019SharedWithYouFooterC0V AA21_TraitWritingModifierV AA04ListX18BackgroundTraitKeyV AA14_PaddingLayoutV AA012SubscriptionC0V So20NSNotificationCenterC10FoundationE9PublisherV AcAE06pickerQ0yQrqd__AA06PickerQ0Rd__lFQO AA6PickerV AA7ForEachV AcAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA013DefaultPickerQ0V AA6ButtonV AcAE18confirmationDialog_AE15titleVisibilityAFQrAA18LocalizedStringKeyV_AiA10VisibilityOqd__yXEtAaBRd__lFQO AA32_EnvironmentKeyTransformModifierV AcAEA32__AEA33_AFQrA35__AIA37_qd__yXEtAaBRd__lFQO
- _symbolic _____y_____y_____y_____y_____y_____y_____yAAy__________G______yAHyAHyA2GG_____GAHyAjGGGtGGG______Qo______y_____SgGG_SSADy_____yAEG_AYtGAEQo__SSADyAHy_____yAY_Qo_AYGSg_AYtGAEQo_ 7SwiftUI4ViewPAAE18confirmationDialog_11isPresented15titleVisibility7actions7messageQrqd___AA7BindingVySbGAA0I0Oqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AcAE5alert_AegHQrqd___AKqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AA15ModifiedContentV AcAE11toggleStyleyQrqd__AA06ToggleQ0Rd__lFQO AA0R0V AA6VStackV AA05TupleC0V AA4TextV AA16_FlexFrameLayoutV AA012_ConditionalO0V AA05EmptyC0V AA06SwitchrQ0V AA30_EnvironmentKeyWritingModifierV AA5ColorV AA6ButtonV AcAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO
- _symbolic _____y_____y_____y_____y_____y_____y_____y_____yAAy__________G______yAHyAHyA2GG_____GAHyAjGGGtGGG______Qo______y_____SgGG_SSADy_____yAEG_AYtGAEQo__SSADyAHy_____yAY_Qo_AYGSg_AYtGAEQo_______Qo_ 7SwiftUI4ViewPAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQO AcAE18confirmationDialog_AE15titleVisibility7actions7messageQrqd___AjA0N0Oqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AcAE5alert_AenOQrqd___AJqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AA15ModifiedContentV AcAE11toggleStyleyQrqd__AA06ToggleU0Rd__lFQO AA0V0V AA6VStackV AA05TupleC0V AA4TextV AA16_FlexFrameLayoutV AA012_ConditionalS0V AA05EmptyC0V AA06SwitchvU0V AA30_EnvironmentKeyWritingModifierV AA5ColorV AA6ButtonV AcAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO 7ChatKit019CKLanguageSelectionC0V
- _symbolic _____y_____y_____y_____y_____y_____y_____y_____y_____yAAyABy__________G______yAHyAHyA2GG_____GAHyAjGGGtGGG______Qo______y_____SgGG_SSAAy_____yAEG_AYtGAEQo__SSAAyAHy_____yAY_Qo_AYGSg_AYtGAEQo_______Qo__A5_Qo__AHyAHyAjYG_____yAXy_____yA2EGG______y_____GQo_GAHyAHyA2JGA15_GtG 7SwiftUI9TupleViewV AA0D0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaDRd__lFQO AeAEAfghIQrAL_AMqd__yctAaDRd__lFQO AeAE18confirmationDialog_AG15titleVisibility7actions7messageQrqd___AlA0O0Oqd_0_yXEqd_1_yXEtSyRd__AaDRd_0_AaDRd_1_r1_lFQO AeAE5alert_AgpQQrqd___ALqd_0_yXEqd_1_yXEtSyRd__AaDRd_0_AaDRd_1_r1_lFQO AA15ModifiedContentV AeAE11toggleStyleyQrqd__AA06ToggleV0Rd__lFQO AA0W0V AA6VStackV AA4TextV AA16_FlexFrameLayoutV AA012_ConditionalT0V AA05EmptyD0V AA06SwitchwV0V AA30_EnvironmentKeyWritingModifierV AA5ColorV AA6ButtonV AeAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO 7ChatKit019CKLanguageSelectionD0V AeAE06buttonV0yQrqd__AA015PrimitiveButtonV0Rd__lFQO AA07LabeledT0V AA020NavigationLinkButtonV0V s5NeverO
- _symbolic _____y_____y_____y_____y_____y_____y_____y_____y_____yAAy__________G______yAHyAHyA2GG_____GAHyAjGGGtGGG______Qo______y_____SgGG_SSADy_____yAEG_AYtGAEQo__SSADyAHy_____yAY_Qo_AYGSg_AYtGAEQo_______Qo__A5_Qo_ 7SwiftUI4ViewPAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQO AcAEAdefGQrAJ_AKqd__yctAaBRd__lFQO AcAE18confirmationDialog_AE15titleVisibility7actions7messageQrqd___AjA0N0Oqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AcAE5alert_AenOQrqd___AJqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AA15ModifiedContentV AcAE11toggleStyleyQrqd__AA06ToggleU0Rd__lFQO AA0V0V AA6VStackV AA05TupleC0V AA4TextV AA16_FlexFrameLayoutV AA012_ConditionalS0V AA05EmptyC0V AA06SwitchvU0V AA30_EnvironmentKeyWritingModifierV AA5ColorV AA6ButtonV AcAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO 7ChatKit019CKLanguageSelectionC0V
- _symbolic _____y_____y_____y_____y_____y_____y_____y_____y_____yAAy__________G______yAHyAHyA2GG_____GAHyAjGGGtGGG______Qo______y_____SgGG_SSADy_____yAEG_AYtGAEQo__SSADyAHy_____yAY_Qo_AYGSg_AYtGAEQo_______Qo__A5_Qo__AHyAHyAjYG_____yAXy_____yA2EGG______y_____GQo_GAHyAHyA2JGA15_Gt 7SwiftUI4ViewPAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQO AcAEAdefGQrAJ_AKqd__yctAaBRd__lFQO AcAE18confirmationDialog_AE15titleVisibility7actions7messageQrqd___AjA0N0Oqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AcAE5alert_AenOQrqd___AJqd_0_yXEqd_1_yXEtSyRd__AaBRd_0_AaBRd_1_r1_lFQO AA15ModifiedContentV AcAE11toggleStyleyQrqd__AA06ToggleU0Rd__lFQO AA0V0V AA6VStackV AA05TupleC0V AA4TextV AA16_FlexFrameLayoutV AA012_ConditionalS0V AA05EmptyC0V AA06SwitchvU0V AA30_EnvironmentKeyWritingModifierV AA5ColorV AA6ButtonV AcAE16keyboardShortcutyQrAA16KeyboardShortcutVFQO 7ChatKit019CKLanguageSelectionC0V AcAE06buttonU0yQrqd__AA015PrimitiveButtonU0Rd__lFQO AA07LabeledS0V AA020NavigationLinkButtonU0V s5NeverO
- _theme.once.6182
- _theme.once.6379
- _theme.once.6406
- _theme.once.6430
- _theme.once.6451
- _theme.sBehavior.6181
- _theme.sBehavior.6378
- _theme.sBehavior.6405
- _theme.sBehavior.6429
- _theme.sBehavior.6450
- _transcriptContactImageDiameter.once.6263
- _transcriptContactImageDiameter.sBehavior.6262
- _transcriptGroupTypingContactImageDiameter.once.6267
- _transcriptGroupTypingContactImageDiameter.sBehavior.6266
- _transcriptHeaderViewMaxRows.once.6219
- _transcriptHeaderViewMaxRows.sBehavior.6218
- _usesActionMenu.once.6392
- _usesActionMenu.once.6418
- _usesPopovers.once.6199
- _usesPopovers.sBehavior.6198
- _usesUncollapsedSplitview.once.6187
- _usesUncollapsedSplitview.sBehavior.6186
CStrings:
+ "-[CKCoreChatController transcriptCollectionViewController:balloonViewDidRequestSendCustomAcknowledgementPayload:forPlugin:error:]"
+ "/Library/Caches/com.apple.xbs/0E4F2107-5684-4BF5-95D1-69FDE41A3E00/TemporaryDirectory.rFJkyZ/Sources/Messages/ChatKit/CKPluginExtensionStateObserver.m"
+ "/Library/Caches/com.apple.xbs/0E4F2107-5684-4BF5-95D1-69FDE41A3E00/TemporaryDirectory.rFJkyZ/Sources/Messages/ChatKit/CKStoragePluginDataModel.swift"
+ "/Library/Caches/com.apple.xbs/0E4F2107-5684-4BF5-95D1-69FDE41A3E00/TemporaryDirectory.rFJkyZ/Sources/Messages/ChatKit/CKTranscriptCollectionViewController.m"
+ "/Library/Caches/com.apple.xbs/0E4F2107-5684-4BF5-95D1-69FDE41A3E00/TemporaryDirectory.rFJkyZ/Sources/Messages/ChatKit/CKTranscriptPluginViewManager.m"
+ "/Library/Caches/com.apple.xbs/0E4F2107-5684-4BF5-95D1-69FDE41A3E00/TemporaryDirectory.rFJkyZ/Sources/Messages/ChatKit/CKTranscriptPrintPageRenderer.m"
+ "/Library/Caches/com.apple.xbs/0E4F2107-5684-4BF5-95D1-69FDE41A3E00/TemporaryDirectory.rFJkyZ/Sources/Messages/ChatKit/LegacyStoragePluginCounts.swift"
+ "/Library/Caches/com.apple.xbs/0E4F2107-5684-4BF5-95D1-69FDE41A3E00/TemporaryDirectory.rFJkyZ/Sources/Messages/ChatKit/StoragePluginCounts.swift"
+ "/Library/Caches/com.apple.xbs/0E4F2107-5684-4BF5-95D1-69FDE41A3E00/TemporaryDirectory.rFJkyZ/Sources/Messages/ChatKit/UITests/IMMockChat.m"
+ "Automatic translation already enabled"
+ "CKConversationTranscriptBackgroundHoldingUpdateReasonApplicationBackgrounded"
+ "CKConversationTranscriptBackgroundUpdateReasonNotificationReceived"
+ "CKConversationUpdater"
+ "CKCoreChatController_CustomAcknowledgements"
+ "CKEntryViewEmptyActionDebounceDuration"
+ "Cleaning up transcript background"
+ "Computing keyTransparencyFooterString Transparency status %lu"
+ "DETAILS_VIEW_ENCRYPTION_FOOTER_IMESSAGE_FORMAT"
+ "DETAILS_VIEW_ENCRYPTION_FOOTER_RCS"
+ "DETAILS_VIEW_ENCRYPTION_FOOTER_SMS"
+ "Force showing translation tip via debug menu"
+ "ForceTranslationTipInNextConversation"
+ "Hiding audio button - entryViewEmptyAction=%ld"
+ "Ignoring audio button long press - button is temporarily disabled after send"
+ "Ignoring audio button tap - button is temporarily disabled after send"
+ "Ignoring dictation button tap - button is temporarily disabled after send"
+ "KT_FOOTER_VIEW_TEXT_TURN_ON"
+ "No available top space"
+ "No chat controller"
+ "No foreign languages detected"
+ "Programmatically dismissing search."
+ "Showing audio button - entryViewEmptyAction=RecordAudioMessage"
+ "T@\"CKGlassSendButton\",N,&,VsendButton"
+ "Tip already consumed"
+ "Translation model not ready"
+ "Translation tip eligibility: %s"
+ "Translation tip not shown: %s"
+ "Translator not supported"
+ "_reloadTranscriptBackground"
+ "_transcriptBackgroundUpdater"
+ "_updateLongPressAudioStopButtonHighlighted:"
+ "buttonFor:"
+ "colorAppearanceChanged"
+ "com.apple.MobileSMS.EntryViewEmptyAction.changed"
+ "conversationUpdaterLogHandle"
+ "debug-forced-guid"
+ "disambiguationLocales"
+ "entryViewEmptyAction"
+ "isEntryViewEmptyActionEnabled"
+ "localizedStandardRangeOfString:"
+ "updateEntryView: entryViewEmptyAction=%ld, dictationButtonHidden=YES"
+ "updateEntryView: entryViewEmptyAction=CKEntryViewEmptyActionStartDictation, sendButtonHidden=%d, isDictationEnabled=%d"
+ "updateEntryView: entryViewEmptyAction=CKEntryViewEmptyActionStartDictation, sendButtonHidden=%d, isDictationEnabled=%d = dictationButtonHidden:%d"
- "-[CKChatController transcriptCollectionViewController:balloonViewDidRequestSendCustomAcknowledgementPayload:forPlugin:error:]"
- "/Library/Caches/com.apple.xbs/AFFFED38-BCA2-4062-ACA6-E67CC659B0EA/TemporaryDirectory.dSd3gS/Sources/Messages/ChatKit/CKPluginExtensionStateObserver.m"
- "/Library/Caches/com.apple.xbs/AFFFED38-BCA2-4062-ACA6-E67CC659B0EA/TemporaryDirectory.dSd3gS/Sources/Messages/ChatKit/CKStoragePluginDataModel.swift"
- "/Library/Caches/com.apple.xbs/AFFFED38-BCA2-4062-ACA6-E67CC659B0EA/TemporaryDirectory.dSd3gS/Sources/Messages/ChatKit/CKTranscriptCollectionViewController.m"
- "/Library/Caches/com.apple.xbs/AFFFED38-BCA2-4062-ACA6-E67CC659B0EA/TemporaryDirectory.dSd3gS/Sources/Messages/ChatKit/CKTranscriptPluginViewManager.m"
- "/Library/Caches/com.apple.xbs/AFFFED38-BCA2-4062-ACA6-E67CC659B0EA/TemporaryDirectory.dSd3gS/Sources/Messages/ChatKit/CKTranscriptPrintPageRenderer.m"
- "/Library/Caches/com.apple.xbs/AFFFED38-BCA2-4062-ACA6-E67CC659B0EA/TemporaryDirectory.dSd3gS/Sources/Messages/ChatKit/LegacyStoragePluginCounts.swift"
- "/Library/Caches/com.apple.xbs/AFFFED38-BCA2-4062-ACA6-E67CC659B0EA/TemporaryDirectory.dSd3gS/Sources/Messages/ChatKit/StoragePluginCounts.swift"
- "/Library/Caches/com.apple.xbs/AFFFED38-BCA2-4062-ACA6-E67CC659B0EA/TemporaryDirectory.dSd3gS/Sources/Messages/ChatKit/UITests/IMMockChat.m"
- "CKChatController_CustomAcknowledgements"
- "DETAILS_VIEW_ENCRYPTION_FOOTER_RCS_SMS"
- "KT_TURN_ON_FOOTER_TEXT"
- "T@\"UIButton\",N,&,VsendButton"
- "_\t"
- "audioRecordingViewLeadingButtonPadding"
- "audioRecordingViewWaveformSpacing"
- "buttonFor:with:"

```
