## TransparencyUI

> `/System/Library/PrivateFrameworks/TransparencyUI.framework/TransparencyUI`

```diff

-1033.82.1.0.0
-  __TEXT.__text: 0x33380
+1033.100.65.0.0
+  __TEXT.__text: 0x3417c
   __TEXT.__auth_stubs: 0x620
-  __TEXT.__objc_methlist: 0x27a4
-  __TEXT.__const: 0x28
-  __TEXT.__cstring: 0x4528
-  __TEXT.__oslogstring: 0x254c
-  __TEXT.__gcc_except_tab: 0x2dc
+  __TEXT.__objc_methlist: 0x281c
+  __TEXT.__const: 0x38
+  __TEXT.__cstring: 0x471e
+  __TEXT.__oslogstring: 0x251b
+  __TEXT.__gcc_except_tab: 0x29c
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0xe0c
+  __TEXT.__unwind_info: 0xe40
   __TEXT.__objc_classname: 0x723
-  __TEXT.__objc_methname: 0x7ce7
-  __TEXT.__objc_methtype: 0x18c0
-  __TEXT.__objc_stubs: 0x5d60
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0xac8
+  __TEXT.__objc_methname: 0x7e35
+  __TEXT.__objc_methtype: 0x18ce
+  __TEXT.__objc_stubs: 0x5ea0
+  __DATA_CONST.__got: 0x2a0
+  __DATA_CONST.__const: 0xb18
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa278
-  __DATA_CONST.__objc_selrefs: 0x1dc0
+  __DATA_CONST.__objc_const: 0xa2d8
+  __DATA_CONST.__objc_selrefs: 0x1e20
+  __DATA_CONST.__objc_classrefs: 0x470
+  __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__const: 0x2aa0
+  __AUTH_CONST.__const: 0x2b00
   __AUTH_CONST.__objc_const: 0xf78
-  __AUTH_CONST.__cfstring: 0x1b60
+  __AUTH_CONST.__cfstring: 0x1b40
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x320
   __AUTH.__objc_data: 0xeb0
-  __DATA.__objc_classrefs: 0x470
-  __DATA.__objc_superrefs: 0x150
-  __DATA.__objc_ivar: 0x328
+  __DATA.__objc_ivar: 0x330
   __DATA.__data: 0x880
   __DATA.__bss: 0x190
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/Transparency.framework/Transparency
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1476
-  Symbols:   5333
-  CStrings:  2179
+  Functions: 1501
+  Symbols:   5400
+  CStrings:  2200
 
Symbols:
+ +[TUIUtils isHSA2]
+ -[TUIKTPaneViewController _changeOptInState:requestedOptInChange:]
+ -[TUIKTPaneViewController _changeOptInState:requestedOptInChange:].cold.1
+ -[TUIKTPaneViewController _setupUIStateIDSDisabled:]
+ -[TUIKTPaneViewController _setupUIStateIDSDisabled:].cold.1
+ -[TUIKTPaneViewController _updateAppleIDHandleURL]
+ -[TUIKTPaneViewController _updateAppleIDHandleURL].cold.1
+ -[TUIKTPaneViewController dismissRemoteUIForViewController]
+ -[TUIKTPaneViewController dismissRemoteUIForViewController].cold.1
+ -[TUIKTPaneViewController handleURL]
+ -[TUIKTPaneViewController setHandleURL:]
+ -[TUIOptInFlowControllerImpl _showErrorAlertWithError:presentingViewController:]
+ -[TUIOptInFlowControllerImpl _showErrorAlertWithError:presentingViewController:].cold.1
+ -[TUIOptInFlowControllerImpl dismissRemoteUIForViewController:error:]
+ -[TUIOptInSpecifierProvider handleURL:]
+ -[TUIOptInSpecifierProvider handleURL:].cold.1
+ -[TUIOptInSpecifierProvider handleURL]
+ -[TUIOptInSpecifierProvider setHandleURL:]
+ GCC_except_table118
+ GCC_except_table173
+ GCC_except_table195
+ GCC_except_table203
+ GCC_except_table38
+ GCC_except_table57
+ GCC_except_table62
+ GCC_except_table64
+ GCC_except_table72
+ GCC_except_table80
+ GCC_except_table84
+ GCC_except_table90
+ GCC_except_table93
+ _OBJC_CLASS_$_AKAccountManager
+ _OBJC_IVAR_$_TUIKTPaneViewController._handleURL
+ _OBJC_IVAR_$_TUIOptInSpecifierProvider._handleURL
+ ___37-[TUIKTPaneViewController specifiers]_block_invoke.102
+ ___39-[TUIOptInSpecifierProvider handleURL:]_block_invoke
+ ___41-[TUIKTPaneViewController _updateAppleID]_block_invoke.189
+ ___41-[TUIKTPaneViewController _updateAppleID]_block_invoke.192
+ ___41-[TUIKTPaneViewController _updateAppleID]_block_invoke.195
+ ___41-[TUIKTPaneViewController _updateAppleID]_block_invoke_2.196
+ ___43-[TUIOptInSpecifierProvider _checkKTStatus]_block_invoke.35
+ ___43-[TUIOptInSpecifierProvider _checkKTStatus]_block_invoke.38
+ ___43-[TUIOptInSpecifierProvider _checkKTStatus]_block_invoke.42
+ ___43-[TUIOptInSpecifierProvider _checkKTStatus]_block_invoke_2.43
+ ___43-[TUIStaticIdentityManager _setupKTSession]_block_invoke.102
+ ___43-[TUIStaticIdentityManager _setupKTSession]_block_invoke.106
+ ___43-[TUIStaticIdentityManager _setupKTSession]_block_invoke_2.103
+ ___44-[TUIKTPaneViewController _grandSlamAccount]_block_invoke.521
+ ___47-[TUIKTPaneViewController _resetButtonPressed:]_block_invoke.238
+ ___47-[TUIKTPaneViewController _resetButtonPressed:]_block_invoke.241
+ ___47-[TUIKTPaneViewController _resetButtonPressed:]_block_invoke_2.242
+ ___48-[TUIKTPaneViewController _openMessagesSettings]_block_invoke.208
+ ___50-[TUIKTPaneViewController _updateAppleIDHandleURL]_block_invoke
+ ___50-[TUIKTPaneViewController _updateAppleIDHandleURL]_block_invoke.383
+ ___50-[TUIKTPaneViewController _updateAppleIDHandleURL]_block_invoke_2
+ ___52-[TUIKTPaneViewController _setupUIStateIDSDisabled:]_block_invoke
+ ___55-[TUIOptInFlowControllerImpl _verifyCDPWithCompletion:]_block_invoke.158
+ ___55-[TUIOptInFlowControllerImpl _verifyCDPWithCompletion:]_block_invoke_2.159
+ ___58-[TUIKTPaneViewController _updateTopGroupSpecifierFooter:]_block_invoke.527
+ ___58-[TUIKTPaneViewController optInFlowResultWithState:error:]_block_invoke.399
+ ___58-[TUIKTPaneViewController optInFlowResultWithState:error:]_block_invoke.402
+ ___58-[TUIOptInFlowControllerImpl _attemptToSetOptInWithState:]_block_invoke.165
+ ___58-[TUIOptInFlowControllerImpl _attemptToSetOptInWithState:]_block_invoke.165.cold.1
+ ___58-[TUIOptInFlowControllerImpl _attemptToSetOptInWithState:]_block_invoke.165.cold.2
+ ___58-[TUIOptInFlowControllerImpl _attemptToSetOptInWithState:]_block_invoke.175
+ ___58-[TUIOptInFlowControllerImpl _attemptToSetOptInWithState:]_block_invoke_2.176
+ ___59-[TUIKTPaneViewController dismissRemoteUIForViewController]_block_invoke
+ ___59-[TUIKTPaneViewController dismissRemoteUIForViewController]_block_invoke.177
+ ___59-[TUIKTPaneViewController dismissRemoteUIForViewController]_block_invoke.180
+ ___59-[TUIKTPaneViewController dismissRemoteUIForViewController]_block_invoke.180.cold.1
+ ___59-[TUIKTPaneViewController dismissRemoteUIForViewController]_block_invoke_2
+ ___59-[TUIKTPaneViewController dismissRemoteUIForViewController]_block_invoke_2.181
+ ___59-[TUIKTPaneViewController presentOptInNavigationController]_block_invoke.388
+ ___60-[TUIStaticIdentityManager localizedPeerAccountNameMessage:]_block_invoke.78
+ ___66-[TUIKTPaneViewController _changeOptInState:requestedOptInChange:]_block_invoke
+ ___66-[TUIKTPaneViewController _changeOptInState:requestedOptInChange:]_block_invoke.248
+ ___66-[TUIKTPaneViewController _changeOptInState:requestedOptInChange:]_block_invoke.251
+ ___66-[TUIKTPaneViewController _changeOptInState:requestedOptInChange:]_block_invoke.254
+ ___66-[TUIKTPaneViewController _changeOptInState:requestedOptInChange:]_block_invoke_2
+ ___66-[TUIKTPaneViewController _changeOptInState:requestedOptInChange:]_block_invoke_2.255
+ ___66-[TUIKTPaneViewController _getServerUILoadDelegateWithCompletion:]_block_invoke.512
+ ___66-[TUIKTPaneViewController _getServerUILoadDelegateWithCompletion:]_block_invoke.515
+ ___66-[TUIKTPaneViewController _getServerUILoadDelegateWithCompletion:]_block_invoke.515.cold.1
+ ___66-[TUIKTPaneViewController _getServerUILoadDelegateWithCompletion:]_block_invoke.518
+ ___66-[TUIOptInFlowControllerImpl _continueAttemptToSetOptInWithState:]_block_invoke.181.cold.1
+ ___66-[TUIOptInFlowControllerImpl _continueAttemptToSetOptInWithState:]_block_invoke.181.cold.2
+ ___69-[TUIKTPaneViewController _getDeviceVerificationEnabledForSpecifier:]_block_invoke.158
+ ___69-[TUIKTPaneViewController _getDeviceVerificationEnabledForSpecifier:]_block_invoke.161
+ ___69-[TUIKTPaneViewController _getDeviceVerificationEnabledForSpecifier:]_block_invoke.165
+ ___69-[TUIOptInFlowControllerImpl dismissRemoteUIForViewController:error:]_block_invoke
+ ___69-[TUIOptInFlowControllerImpl dismissRemoteUIForViewController:error:]_block_invoke.121
+ ___69-[TUIOptInFlowControllerImpl dismissRemoteUIForViewController:error:]_block_invoke.124
+ ___69-[TUIOptInFlowControllerImpl dismissRemoteUIForViewController:error:]_block_invoke.124.cold.1
+ ___69-[TUIOptInFlowControllerImpl dismissRemoteUIForViewController:error:]_block_invoke.128
+ ___69-[TUIOptInFlowControllerImpl dismissRemoteUIForViewController:error:]_block_invoke.128.cold.1
+ ___69-[TUIOptInFlowControllerImpl dismissRemoteUIForViewController:error:]_block_invoke.cold.1
+ ___69-[TUIOptInFlowControllerImpl dismissRemoteUIForViewController:error:]_block_invoke_2
+ ___69-[TUIOptInFlowControllerImpl dismissRemoteUIForViewController:error:]_block_invoke_2.125
+ ___69-[TUIOptInFlowControllerImpl dismissRemoteUIForViewController:error:]_block_invoke_2.129
+ ___71-[TUIKTPaneViewController _loadRemoteRequest:withIdentifier:specifier:]_block_invoke.415
+ ___78-[TUIKTPaneViewController _attemptUpdateAuthControllerWithActionableResponse:]_block_invoke.500
+ ___78-[TUIKTPaneViewController _attemptUpdateAuthControllerWithActionableResponse:]_block_invoke.504
+ ___78-[TUIKTPaneViewController _attemptUpdateAuthControllerWithActionableResponse:]_block_invoke.507
+ ___80-[TUIKTPaneViewController remoteUIController:didFinishLoadWithError:forRequest:]_block_invoke.452
+ ___80-[TUIKTPaneViewController remoteUIController:didFinishLoadWithError:forRequest:]_block_invoke.455
+ ___80-[TUIKTPaneViewController remoteUIController:didFinishLoadWithError:forRequest:]_block_invoke.458
+ ___80-[TUIKTPaneViewController remoteUIController:didFinishLoadWithError:forRequest:]_block_invoke.462
+ ___80-[TUIKTPaneViewController remoteUIController:didFinishLoadWithError:forRequest:]_block_invoke_2.459
+ ___80-[TUIOptInFlowControllerImpl _showErrorAlertWithError:presentingViewController:]_block_invoke
+ ___80-[TUIOptInFlowControllerImpl _showErrorAlertWithError:presentingViewController:]_block_invoke.256
+ ___80-[TUIOptInFlowControllerImpl _showErrorAlertWithError:presentingViewController:]_block_invoke.277
+ ___80-[TUIOptInFlowControllerImpl _showErrorAlertWithError:presentingViewController:]_block_invoke_2
+ ___80-[TUIOptInFlowControllerImpl _showErrorAlertWithError:presentingViewController:]_block_invoke_2.282
+ ___81-[TUIKTPaneViewController remoteUIController:didReceiveObjectModel:actionSignal:]_block_invoke.485
+ ___81-[TUIKTPaneViewController remoteUIController:shouldLoadRequest:redirectResponse:]_block_invoke.445
+ ___84-[TUIKTPaneViewController _loadRemoteRequest:withIdentifier:preparation:completion:]_block_invoke.421
+ ___84-[TUIKTPaneViewController _loadRemoteRequest:withIdentifier:preparation:completion:]_block_invoke.424
+ ___84-[TUIStaticIdentityManager postNotificationName:object:userInfo:deliverImmediately:]_block_invoke.112
+ ___85-[TUIKTPaneViewController _handleObjectModelChangeForController:objectModel:isModal:]_block_invoke.476
+ ___block_descriptor_48_e8_32r40w_e20_v20?0B8"NSError"12lw40l8r32l8
+ ___block_descriptor_64_e8_32s40bs48r56w_e20_v20?0B8"NSError"12lw56l8s40l8r48l8s32l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e17_v16?0"NSError"8ls56l8s32l8s40l8s48l8
+ ___block_literal_global.104
+ ___block_literal_global.105
+ ___block_literal_global.114
+ ___block_literal_global.123
+ ___block_literal_global.127
+ ___block_literal_global.131
+ ___block_literal_global.133
+ ___block_literal_global.153
+ ___block_literal_global.157
+ ___block_literal_global.161
+ ___block_literal_global.163
+ ___block_literal_global.174
+ ___block_literal_global.176
+ ___block_literal_global.178
+ ___block_literal_global.179
+ ___block_literal_global.185
+ ___block_literal_global.194
+ ___block_literal_global.207
+ ___block_literal_global.210
+ ___block_literal_global.237
+ ___block_literal_global.244
+ ___block_literal_global.257
+ ___block_literal_global.390
+ ___block_literal_global.392
+ ___block_literal_global.404
+ ___block_literal_global.406
+ ___block_literal_global.408
+ ___block_literal_global.410
+ ___block_literal_global.417
+ ___block_literal_global.419
+ ___block_literal_global.423
+ ___block_literal_global.430
+ ___block_literal_global.432
+ ___block_literal_global.434
+ ___block_literal_global.447
+ ___block_literal_global.451
+ ___block_literal_global.454
+ ___block_literal_global.457
+ ___block_literal_global.461
+ ___block_literal_global.467
+ ___block_literal_global.469
+ ___block_literal_global.478
+ ___block_literal_global.481
+ ___block_literal_global.487
+ ___block_literal_global.489
+ ___block_literal_global.496
+ ___block_literal_global.499
+ ___block_literal_global.502
+ ___block_literal_global.511
+ ___block_literal_global.514
+ ___block_literal_global.517
+ ___block_literal_global.520
+ ___block_literal_global.523
+ ___block_literal_global.529
+ ___block_literal_global.531
+ ___block_literal_global.83
+ ___block_literal_global.86
+ _kTUISetupFlowSheetHeightLowResolution
+ _kTransparencyErrorIDSRegistrationTimeout
+ _objc_msgSend$_changeOptInState:requestedOptInChange:
+ _objc_msgSend$_setupUIStateIDSDisabled:
+ _objc_msgSend$_showErrorAlertWithError:presentingViewController:
+ _objc_msgSend$_updateAppleIDHandleURL
+ _objc_msgSend$accountType
+ _objc_msgSend$authKitAccountWithAltDSID:
+ _objc_msgSend$bringSubviewToFront:
+ _objc_msgSend$dismissRemoteUIForViewController
+ _objc_msgSend$dismissRemoteUIForViewController:error:
+ _objc_msgSend$isHSA2
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$securityLevelForAccount:
+ _objc_msgSend$setHandleURL:
+ _objc_msgSend$waitForIDSRegistration:
- -[TUIOptInFlowControllerImpl _showErrorAlertWithError:]
- -[TUIOptInFlowControllerImpl _showErrorAlertWithError:].cold.1
- GCC_except_table112
- GCC_except_table163
- GCC_except_table183
- GCC_except_table185
- GCC_except_table26
- GCC_except_table41
- GCC_except_table49
- GCC_except_table51
- GCC_except_table54
- GCC_except_table61
- GCC_except_table69
- GCC_except_table75
- GCC_except_table77
- GCC_except_table86
- GCC_except_table91
- _OBJC_CLASS_$_KTIDStaticKeyStore
- ___37-[TUIKTPaneViewController specifiers]_block_invoke.100
- ___41-[TUIKTPaneViewController _updateAppleID]_block_invoke.175
- ___41-[TUIKTPaneViewController _updateAppleID]_block_invoke.175.cold.1
- ___41-[TUIKTPaneViewController _updateAppleID]_block_invoke.178
- ___41-[TUIKTPaneViewController _updateAppleID]_block_invoke.181
- ___41-[TUIKTPaneViewController _updateAppleID]_block_invoke.184
- ___41-[TUIKTPaneViewController _updateAppleID]_block_invoke.188
- ___41-[TUIKTPaneViewController _updateAppleID]_block_invoke.188.cold.1
- ___41-[TUIKTPaneViewController _updateAppleID]_block_invoke_2.185
- ___41-[TUIKTPaneViewController _updateAppleID]_block_invoke_2.189
- ___43-[TUIOptInSpecifierProvider _checkKTStatus]_block_invoke.33
- ___43-[TUIOptInSpecifierProvider _checkKTStatus]_block_invoke.36
- ___43-[TUIOptInSpecifierProvider _checkKTStatus]_block_invoke.40
- ___43-[TUIOptInSpecifierProvider _checkKTStatus]_block_invoke_2.41
- ___43-[TUIStaticIdentityManager _setupKTSession]_block_invoke.110
- ___43-[TUIStaticIdentityManager _setupKTSession]_block_invoke.114
- ___43-[TUIStaticIdentityManager _setupKTSession]_block_invoke_2.111
- ___44-[TUIKTPaneViewController _grandSlamAccount]_block_invoke.516
- ___46-[TUIStaticIdentityManager verifyConversation]_block_invoke.74
- ___46-[TUIStaticIdentityManager verifyConversation]_block_invoke.77
- ___46-[TUIStaticIdentityManager verifyConversation]_block_invoke_2
- ___47-[TUIKTPaneViewController _resetButtonPressed:]_block_invoke.230
- ___47-[TUIKTPaneViewController _resetButtonPressed:]_block_invoke.233
- ___47-[TUIKTPaneViewController _resetButtonPressed:]_block_invoke.233.cold.1
- ___47-[TUIKTPaneViewController _resetButtonPressed:]_block_invoke.237
- ___47-[TUIKTPaneViewController _resetButtonPressed:]_block_invoke.246
- ___47-[TUIKTPaneViewController _resetButtonPressed:]_block_invoke.250
- ___47-[TUIKTPaneViewController _resetButtonPressed:]_block_invoke.253
- ___47-[TUIKTPaneViewController _resetButtonPressed:]_block_invoke_2.234
- ___47-[TUIKTPaneViewController _resetButtonPressed:]_block_invoke_2.247
- ___47-[TUIKTPaneViewController _resetButtonPressed:]_block_invoke_2.254
- ___48-[TUIKTPaneViewController _openMessagesSettings]_block_invoke.200
- ___55-[TUIOptInFlowControllerImpl _showErrorAlertWithError:]_block_invoke
- ___55-[TUIOptInFlowControllerImpl _showErrorAlertWithError:]_block_invoke.256
- ___55-[TUIOptInFlowControllerImpl _showErrorAlertWithError:]_block_invoke.277
- ___55-[TUIOptInFlowControllerImpl _showErrorAlertWithError:]_block_invoke_2
- ___55-[TUIOptInFlowControllerImpl _showErrorAlertWithError:]_block_invoke_2.282
- ___55-[TUIOptInFlowControllerImpl _verifyCDPWithCompletion:]_block_invoke.134
- ___55-[TUIOptInFlowControllerImpl _verifyCDPWithCompletion:]_block_invoke.137
- ___55-[TUIOptInFlowControllerImpl _verifyCDPWithCompletion:]_block_invoke.144
- ___55-[TUIOptInFlowControllerImpl _verifyCDPWithCompletion:]_block_invoke.144.cold.1
- ___55-[TUIOptInFlowControllerImpl _verifyCDPWithCompletion:]_block_invoke.151.cold.1
- ___55-[TUIOptInFlowControllerImpl _verifyCDPWithCompletion:]_block_invoke.155
- ___55-[TUIOptInFlowControllerImpl _verifyCDPWithCompletion:]_block_invoke.155.cold.1
- ___55-[TUIOptInFlowControllerImpl _verifyCDPWithCompletion:]_block_invoke_2.145
- ___55-[TUIOptInFlowControllerImpl _verifyCDPWithCompletion:]_block_invoke_2.152
- ___55-[TUIOptInFlowControllerImpl _verifyCDPWithCompletion:]_block_invoke_2.156
- ___58-[TUIKTPaneViewController _updateTopGroupSpecifierFooter:]_block_invoke.522
- ___58-[TUIKTPaneViewController optInFlowResultWithState:error:]_block_invoke.394
- ___58-[TUIKTPaneViewController optInFlowResultWithState:error:]_block_invoke.397
- ___58-[TUIOptInFlowControllerImpl _attemptToSetOptInWithState:]_block_invoke.162
- ___58-[TUIOptInFlowControllerImpl _attemptToSetOptInWithState:]_block_invoke.162.cold.1
- ___58-[TUIOptInFlowControllerImpl _attemptToSetOptInWithState:]_block_invoke.162.cold.2
- ___58-[TUIOptInFlowControllerImpl _attemptToSetOptInWithState:]_block_invoke.166
- ___58-[TUIOptInFlowControllerImpl _attemptToSetOptInWithState:]_block_invoke_2.173
- ___59-[TUIKTPaneViewController presentOptInNavigationController]_block_invoke.383
- ___60-[TUIStaticIdentityManager localizedPeerAccountNameMessage:]_block_invoke.86
- ___66-[TUIKTPaneViewController _getServerUILoadDelegateWithCompletion:]_block_invoke.507
- ___66-[TUIKTPaneViewController _getServerUILoadDelegateWithCompletion:]_block_invoke.510
- ___66-[TUIKTPaneViewController _getServerUILoadDelegateWithCompletion:]_block_invoke.510.cold.1
- ___66-[TUIKTPaneViewController _getServerUILoadDelegateWithCompletion:]_block_invoke.513
- ___66-[TUIOptInFlowControllerImpl _continueAttemptToSetOptInWithState:]_block_invoke.178
- ___66-[TUIOptInFlowControllerImpl _continueAttemptToSetOptInWithState:]_block_invoke.178.cold.1
- ___66-[TUIOptInFlowControllerImpl _continueAttemptToSetOptInWithState:]_block_invoke.178.cold.2
- ___69-[TUIKTPaneViewController _getDeviceVerificationEnabledForSpecifier:]_block_invoke.153
- ___69-[TUIKTPaneViewController _getDeviceVerificationEnabledForSpecifier:]_block_invoke.156
- ___69-[TUIKTPaneViewController _getDeviceVerificationEnabledForSpecifier:]_block_invoke.160
- ___71-[TUIKTPaneViewController _loadRemoteRequest:withIdentifier:specifier:]_block_invoke.410
- ___78-[TUIKTPaneViewController _attemptUpdateAuthControllerWithActionableResponse:]_block_invoke.495
- ___78-[TUIKTPaneViewController _attemptUpdateAuthControllerWithActionableResponse:]_block_invoke.499
- ___78-[TUIKTPaneViewController _attemptUpdateAuthControllerWithActionableResponse:]_block_invoke.502
- ___80-[TUIKTPaneViewController remoteUIController:didFinishLoadWithError:forRequest:]_block_invoke.447
- ___80-[TUIKTPaneViewController remoteUIController:didFinishLoadWithError:forRequest:]_block_invoke.450
- ___80-[TUIKTPaneViewController remoteUIController:didFinishLoadWithError:forRequest:]_block_invoke.453
- ___80-[TUIKTPaneViewController remoteUIController:didFinishLoadWithError:forRequest:]_block_invoke.457
- ___80-[TUIKTPaneViewController remoteUIController:didFinishLoadWithError:forRequest:]_block_invoke_2.454
- ___81-[TUIKTPaneViewController remoteUIController:didReceiveObjectModel:actionSignal:]_block_invoke.480
- ___81-[TUIKTPaneViewController remoteUIController:shouldLoadRequest:redirectResponse:]_block_invoke.440
- ___84-[TUIKTPaneViewController _loadRemoteRequest:withIdentifier:preparation:completion:]_block_invoke.416
- ___84-[TUIKTPaneViewController _loadRemoteRequest:withIdentifier:preparation:completion:]_block_invoke.419
- ___84-[TUIStaticIdentityManager postNotificationName:object:userInfo:deliverImmediately:]_block_invoke.120
- ___85-[TUIKTPaneViewController _handleObjectModelChangeForController:objectModel:isModal:]_block_invoke.471
- ___block_descriptor_64_e8_32s40s48bs56w_e20_v20?0B8"NSError"12lw56l8s48l8s32l8s40l8
- ___block_literal_global.109
- ___block_literal_global.119
- ___block_literal_global.122
- ___block_literal_global.135
- ___block_literal_global.136
- ___block_literal_global.139
- ___block_literal_global.147
- ___block_literal_global.152
- ___block_literal_global.154
- ___block_literal_global.155
- ___block_literal_global.158
- ___block_literal_global.162
- ___block_literal_global.169
- ___block_literal_global.175
- ___block_literal_global.177
- ___block_literal_global.187
- ___block_literal_global.199
- ___block_literal_global.229
- ___block_literal_global.232
- ___block_literal_global.239
- ___block_literal_global.249
- ___block_literal_global.252
- ___block_literal_global.256
- ___block_literal_global.35
- ___block_literal_global.396
- ___block_literal_global.399
- ___block_literal_global.403
- ___block_literal_global.405
- ___block_literal_global.407
- ___block_literal_global.409
- ___block_literal_global.418
- ___block_literal_global.422
- ___block_literal_global.425
- ___block_literal_global.429
- ___block_literal_global.442
- ___block_literal_global.446
- ___block_literal_global.449
- ___block_literal_global.452
- ___block_literal_global.456
- ___block_literal_global.459
- ___block_literal_global.462
- ___block_literal_global.473
- ___block_literal_global.476
- ___block_literal_global.482
- ___block_literal_global.484
- ___block_literal_global.486
- ___block_literal_global.494
- ___block_literal_global.497
- ___block_literal_global.501
- ___block_literal_global.504
- ___block_literal_global.512
- ___block_literal_global.515
- ___block_literal_global.518
- ___block_literal_global.521
- ___block_literal_global.524
- ___block_literal_global.84
- _objc_msgSend$_showErrorAlertWithError:
- _objc_msgSend$findByContact:error:
- _objc_msgSend$ktCapable
- _objc_msgSend$updateStaticKeyDatabaseForContact:peerPublicAccountIdentity:complete:
CStrings:
+ "%s changeOptInState result = %d, loggableDatas = %{public}@, error = %{public}@ on %{public}@"
+ "%s handleURL = %d on %{public}@"
+ "%s requestedOptInChange = %{public}@ on %{public}@"
+ "%s user is not signed in to iMessage with AppleID on %{public}@"
+ "("
+ "-[TUIKTPaneViewController _changeOptInState:requestedOptInChange:]"
+ "-[TUIKTPaneViewController _changeOptInState:requestedOptInChange:]_block_invoke"
+ "-[TUIKTPaneViewController _changeOptInState:requestedOptInChange:]_block_invoke_2"
+ "-[TUIKTPaneViewController _setupUIStateIDSDisabled:]"
+ "-[TUIKTPaneViewController _updateAppleIDHandleURL]"
+ "-[TUIKTPaneViewController _updateAppleIDHandleURL]_block_invoke"
+ "-[TUIKTPaneViewController dismissRemoteUIForViewController]_block_invoke"
+ "-[TUIOptInFlowControllerImpl _showErrorAlertWithError:presentingViewController:]"
+ "-[TUIOptInFlowControllerImpl _showErrorAlertWithError:presentingViewController:]_block_invoke"
+ "-[TUIOptInFlowControllerImpl dismissRemoteUIForViewController:error:]_block_invoke"
+ "-[TUIOptInSpecifierProvider handleURL:]"
+ "IDS_KT_DISABLED_DETAIL"
+ "T@\"NSString\",?,C,N"
+ "T@\"NSString\",?,C,N,V_detailText"
+ "T@\"NSString\",?,C,N,V_helpLinkTitle"
+ "T@\"NSString\",?,C,N,V_helpLinkURL"
+ "T@\"NSString\",?,C,N,V_primaryButton"
+ "T@\"NSString\",?,C,N,V_secondaryButton"
+ "T@\"NSString\",?,C,N,V_symbolName"
+ "T@\"NSString\",?,C,N,V_title"
+ "T@\"NSString\",?,R,C"
+ "T@\"UIViewController\",?,C,N"
+ "T@\"UIViewController\",?,C,N,V_contentViewController"
+ "TB,N,V_handleURL"
+ "Tq,?,N"
+ "Tq,?,N,V_contentViewLayout"
+ "UPDATE_APPLE_ID_BUTTON"
+ "_changeOptInState:requestedOptInChange:"
+ "_handleURL"
+ "_setupUIStateIDSDisabled:"
+ "_showErrorAlertWithError:presentingViewController:"
+ "_updateAppleIDHandleURL"
+ "accountType"
+ "authKitAccountWithAltDSID:"
+ "bringSubviewToFront:"
+ "dismissRemoteUIForViewController"
+ "dismissRemoteUIForViewController:error:"
+ "handleURL"
+ "isHSA2"
+ "numberWithUnsignedInteger:"
+ "securityLevelForAccount:"
+ "setHandleURL:"
+ "v32@0:8@16Q24"
+ "waitForIDSRegistration error after verifying CDP %{public}@"
+ "waitForIDSRegistration:"
- "\x18"
- "%s KTOptInManager:changeOptInState result = %d, loggableDatas = %{public}@, error = %{public}@ on %{public}@"
- "%s calling KTOptInManager:changeOptInState with %@ on %{public}@"
- "%s user is not signed in to iMessage on %{public}@"
- "%{public}@ ktCapable == NO on deviceId %{public}@, failure = %{public}@"
- "-[TUIKTPaneViewController _resetButtonPressed:]_block_invoke_2"
- "-[TUIOptInFlowControllerImpl _showErrorAlertWithError:]"
- "-[TUIOptInFlowControllerImpl _showErrorAlertWithError:]_block_invoke"
- "-[TUIStaticIdentityManager verifyConversation]_block_invoke"
- "KTOptInChangeOptOut"
- "KTOptInChangeReset"
- "T@\"NSString\",C,N"
- "T@\"NSString\",C,N,V_detailText"
- "T@\"NSString\",C,N,V_helpLinkTitle"
- "T@\"NSString\",C,N,V_helpLinkURL"
- "T@\"NSString\",C,N,V_primaryButton"
- "T@\"NSString\",C,N,V_secondaryButton"
- "T@\"NSString\",C,N,V_symbolName"
- "T@\"NSString\",C,N,V_title"
- "T@\"UIViewController\",C,N"
- "T@\"UIViewController\",C,N,V_contentViewController"
- "Tq,N"
- "Tq,N,V_contentViewLayout"
- "Update Apple ID Settings"
- "_showErrorAlertWithError:"
- "findByContact:error:"
- "ktCapable"
- "no contact entry %{mask.hash}@, letting user confirm"
- "updateStaticKeyDatabaseForContact:peerPublicAccountIdentity:complete:"

```
