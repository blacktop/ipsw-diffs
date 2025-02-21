## RunningBoard

> `/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard`

```diff

-945.80.1.0.1
-  __TEXT.__text: 0x7b308
-  __TEXT.__auth_stubs: 0x1410
-  __TEXT.__objc_methlist: 0x4f30
-  __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x6bb9
-  __TEXT.__oslogstring: 0xb1e7
-  __TEXT.__gcc_except_tab: 0xcb0
-  __TEXT.__unwind_info: 0x1ae0
+961.100.15.502.1
+  __TEXT.__text: 0x7a928
+  __TEXT.__auth_stubs: 0x1450
+  __TEXT.__objc_methlist: 0x5efc
+  __TEXT.__const: 0x1e8
+  __TEXT.__cstring: 0x7a05
+  __TEXT.__oslogstring: 0xb44b
+  __TEXT.__gcc_except_tab: 0xca4
+  __TEXT.__unwind_info: 0x1be8
   __TEXT.__objc_classname: 0xf1d
-  __TEXT.__objc_methname: 0xcce1
-  __TEXT.__objc_methtype: 0x2b92
-  __TEXT.__objc_stubs: 0x9b80
-  __DATA_CONST.__got: 0x788
-  __DATA_CONST.__const: 0x1648
+  __TEXT.__objc_methname: 0xceb2
+  __TEXT.__objc_methtype: 0x2bfc
+  __TEXT.__objc_stubs: 0x9cc0
+  __DATA_CONST.__got: 0x750
+  __DATA_CONST.__const: 0x1708
   __DATA_CONST.__objc_classlist: 0x360
-  __DATA_CONST.__objc_catlist: 0x168
+  __DATA_CONST.__objc_catlist: 0x170
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b18
+  __DATA_CONST.__objc_selrefs: 0x2cb8
   __DATA_CONST.__objc_superrefs: 0x290
   __DATA_CONST.__objc_arraydata: 0x6b8
-  __AUTH_CONST.__auth_got: 0xa18
+  __AUTH_CONST.__auth_got: 0xa38
+  __AUTH_CONST.__auth_ptr: 0x40
   __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x5880
-  __AUTH_CONST.__objc_const: 0xeb38
+  __AUTH_CONST.__cfstring: 0x6740
+  __AUTH_CONST.__objc_const: 0xd160
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x9d8
+  __DATA.__objc_ivar: 0x9ec
   __DATA.__data: 0x1320
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0x1fe0
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x24c
+  __DATA_DIRTY.__bss: 0x23c
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 2539
-  Symbols:   3307
-  CStrings:  4369
+  Functions: 2659
+  Symbols:   3433
+  CStrings:  4511
 
Symbols:
+ _RBSAppViewServiceMachServiceName
+ _RBSAppViewServiceSessionVendingEntitlement
+ _bzero
+ _objc_retainAutoreleasedReturnValue
+ _xpc_array_create_empty
- _RBViewServicesEntitlement
CStrings:
+ "\v3"
+ "\x14\x12!\"'\x14"
+ "%{public}@ ignoring unsupported LaunchRequestEndpointIdentifiers value for launchIdentifier %{public}@: value=%{public}@"
+ "%{public}@ ignoring unsupported MANAGEDBY_SERVICES value for launchIdentifier %{public}@: value=%{public}@"
+ "@\"RBAssertion\"24@0:8@\"RBSAssertionIdentifier\"16"
+ "B32@0:8@\"RBSProcessIdentity\"16@\"RBSAssertionIdentifier\"24"
+ "BUG IN %@: RunningBoard terminated %@ because it was suspended while holding a shared file lock:\n%@\nFile locks MUST be held in one of the following directories:\n%@"
+ "Invalidating %{public}lu assertions synchronously"
+ "Process: %@ with pid: %d; launch assertion: %@"
+ "Skipping assertion: %@ for invalidation as this doesn't belong to the terminating process: %@ with pid: %d"
+ "Specified target process %@ does not exist"
+ "T@\"RBSAssertionIdentifier\",&,N,V_launchAssertionIdentifier"
+ "TB,N,GisLaunchAssertion,V_launchAssertion"
+ "TB,N,V_launchAssertion"
+ "Unknown ViewService App: ViewService Apps are deprecated and you should not be adding new ones - if you need an exception please file a radar to RunningBoard|All to be added to the allowlist."
+ "_ManagedBy_Services"
+ "_launchAssertion"
+ "_launchAssertionIdentifier"
+ "_mutateContextIfNeeded bundleType %{public}@ refusing SBMachServices %{public}@"
+ "assertion failure: \"lassProps != ((void*)0)\" -> %llu"
+ "boolForKey:"
+ "com.apple.AAUIViewService"
+ "com.apple.AMSEngagementViewService"
+ "com.apple.AMSUIPaymentViewService"
+ "com.apple.APSUIApp"
+ "com.apple.AXRemoteViewService"
+ "com.apple.AXUIViewService"
+ "com.apple.AppSSOUIService"
+ "com.apple.AppleIDSetupUIService"
+ "com.apple.AskPermissionUI"
+ "com.apple.AuthKitUIService"
+ "com.apple.AuthenticationServicesUI"
+ "com.apple.BusinessChatViewService"
+ "com.apple.CBRemoteSetup"
+ "com.apple.CSViewService"
+ "com.apple.CTCarrierSpaceAuth"
+ "com.apple.CTNotifyUIService"
+ "com.apple.CarPlaySetupApp"
+ "com.apple.CarPlaySplashScreen"
+ "com.apple.ClipViewService"
+ "com.apple.CompanionSetup"
+ "com.apple.CompanionViewService"
+ "com.apple.CompassCalibrationViewService"
+ "com.apple.ContactsUI.Carousel"
+ "com.apple.CoreAuthUI"
+ "com.apple.CredentialSharingService"
+ "com.apple.Diagnostics"
+ "com.apple.DiagnosticsReporter"
+ "com.apple.EventViewService"
+ "com.apple.EyeReliefUI"
+ "com.apple.FCAuthenticationUI"
+ "com.apple.FMDMagSafeSetupRemoteUI"
+ "com.apple.FinanceUIService"
+ "com.apple.FontInstallViewService"
+ "com.apple.GameCenterRemoteAlert"
+ "com.apple.HDSViewService"
+ "com.apple.HeadphoneProxService"
+ "com.apple.HealthENBuddy"
+ "com.apple.HealthPrivacyService"
+ "com.apple.Home.HomeControlService"
+ "com.apple.Home.HomeUIService"
+ "com.apple.HomeCaptiveViewService"
+ "com.apple.InCallService"
+ "com.apple.MailCompositionService"
+ "com.apple.MusicUIService"
+ "com.apple.NanoMailComposeService"
+ "com.apple.NanoMessageUIViewService"
+ "com.apple.NanoNowPlayingViewService"
+ "com.apple.NanoSettingsViewService"
+ "com.apple.NanoTextSizeViewService"
+ "com.apple.PASViewService"
+ "com.apple.PCViewService"
+ "com.apple.PDUIApp"
+ "com.apple.PassbookSecureUIService"
+ "com.apple.PassbookUIService"
+ "com.apple.Photos.PhotosUIService"
+ "com.apple.ProximityReaderUIService"
+ "com.apple.PublicHealthRemoteUI"
+ "com.apple.QuickboardViewService"
+ "com.apple.RecoverDeviceUI"
+ "com.apple.RemotePassUIService"
+ "com.apple.RemoteiCloudQuotaUI"
+ "com.apple.SIMSetupUIService"
+ "com.apple.SOSBuddy"
+ "com.apple.ScreenSharingViewService"
+ "com.apple.ScreenTimeUnlock"
+ "com.apple.ScreenshotServicesService"
+ "com.apple.SharedWebCredentialViewService"
+ "com.apple.SharingViewService"
+ "com.apple.SharingViewServiceTV"
+ "com.apple.SleepLockScreen"
+ "com.apple.SpringBoardEducation"
+ "com.apple.StoreDemoViewService"
+ "com.apple.SubcredentialUIService"
+ "com.apple.SysViewService"
+ "com.apple.SystemPaperViewService"
+ "com.apple.TDGSharingViewService"
+ "com.apple.TVAccessViewService"
+ "com.apple.TVAirPlay"
+ "com.apple.TVCRDService"
+ "com.apple.TVDisplayAssistant"
+ "com.apple.TVHomeSharing"
+ "com.apple.TVMusic"
+ "com.apple.TVNowPlayingService"
+ "com.apple.TVPhotos"
+ "com.apple.TVProfileMappingService"
+ "com.apple.TVRemoteUIService"
+ "com.apple.TVRestrictionPINService"
+ "com.apple.TVScreenSaver"
+ "com.apple.TVSetupUIService"
+ "com.apple.TVSystemBulletinService"
+ "com.apple.TVSystemMenuService"
+ "com.apple.TVUserProfileService"
+ "com.apple.TVWhatsNew"
+ "com.apple.TrustMe"
+ "com.apple.VSViewService"
+ "com.apple.VoiceMemos"
+ "com.apple.WebContentFilter.remoteUI.WebContentAnalysisUI"
+ "com.apple.WebSheet"
+ "com.apple.WiFiViewService"
+ "com.apple.WorkoutRemoteViewService"
+ "com.apple.coreidv.ui-service"
+ "com.apple.ctkui"
+ "com.apple.datadetectors.DDActionsService"
+ "com.apple.dockkit.pairinguiservice"
+ "com.apple.facetime"
+ "com.apple.family"
+ "com.apple.feedback.remote"
+ "com.apple.findmy.remoteuiservice"
+ "com.apple.frontboard.workspace-service"
+ "com.apple.gamecenter.GameCenterUIService"
+ "com.apple.iMessageAppsViewService"
+ "com.apple.internal.suiaviewservice"
+ "com.apple.ios.StoreKitUIService"
+ "com.apple.mobilephone"
+ "com.apple.mobilesms.compose"
+ "com.apple.perftest.PerfTestService"
+ "com.apple.podcasts"
+ "com.apple.runningboard.test.limeVS"
+ "com.apple.shortcuts.runtime"
+ "com.apple.susuiservice"
+ "entitlementValuesForKeys:"
+ "hasAssertionWithIdentifierForTarget:identifier:"
+ "isLaunchAssertion"
+ "launchAssertion"
+ "launchAssertionIdentifier"
+ "launchRequestIdentifierToMachNameMap"
+ "rb_hasEntitlement:"
+ "rb_hasEntitlementDomain:"
+ "setLaunchAssertion:"
+ "setLaunchAssertionIdentifier:"
+ "setLaunchRequestIdentifierToMachNameMap:"
+ "setWithCapacity:"
- "\v#"
- "\x14\x12!!'\x13"
- "%@ was suspended with locked system files:\n%@\nnot in allowed directories:\n%@"
- "Executing launch request for %{public}@ (%{public}@)"
- "Invalidating assertions synchronously"
- "Specified target process does not exist"
- "The running process did not match the expected."
- "assertion failure: \"lassProps != ((void *)0)\" -> %lld"
- "com.apple.UIKit.vends-view-services"
- "com.apple.chrono.WidgetRenderer-Default"
- "hasEntitlement:"
- "hasEntitlementDomain:"

```
