## CarPlaySetup

> `/System/Library/PrivateFrameworks/CarPlaySetup.framework/CarPlaySetup`

```diff

-807.4.1.0.0
-  __TEXT.__text: 0xb418
-  __TEXT.__objc_methlist: 0x984
+808.6.0.0.0
+  __TEXT.__text: 0xc6d0
+  __TEXT.__objc_methlist: 0xe90
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x113d
-  __TEXT.__gcc_except_tab: 0x2c4
-  __TEXT.__oslogstring: 0x4b2
-  __TEXT.__unwind_info: 0x388
+  __TEXT.__cstring: 0x1362
+  __TEXT.__gcc_except_tab: 0x2fc
+  __TEXT.__oslogstring: 0x57d
+  __TEXT.__unwind_info: 0x3d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x270
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__const: 0x298
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa60
+  __DATA_CONST.__objc_selrefs: 0xe98
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x48
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0xb0
-  __DATA_CONST.__got: 0x228
+  __DATA_CONST.__got: 0x258
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x1820
-  __AUTH_CONST.__objc_const: 0x12a8
+  __AUTH_CONST.__cfstring: 0x1a00
+  __AUTH_CONST.__objc_const: 0x1af0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x8c
-  __DATA.__data: 0x180
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0xa4
+  __DATA.__data: 0x2a0
   __DATA_DIRTY.__objc_data: 0x370
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit
+  - /System/Library/PrivateFrameworks/SiriAvailability.framework/SiriAvailability
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 217
-  Symbols:   522
-  CStrings:  237
+  Functions: 245
+  Symbols:   596
+  CStrings:  256
 
Symbols:
+ +[CARSetupVehicleMessageAIProcessingAlert alertWithResponseHandler:]
+ -[CARSetupAppIconProgressView _applySiriIconState]
+ -[CARSetupAppIconProgressView setStateController:]
+ -[CARSetupAppIconProgressView stateController]
+ -[CARSetupOnboardingViewController _proceedToMoreIntegrationOptions]
+ -[CARSetupOnboardingViewController showMoreIntegrationOptions]
+ -[CARSetupVehicleHandlesMessagingViewController .cxx_destruct]
+ -[CARSetupVehicleHandlesMessagingViewController _handleContinue:]
+ -[CARSetupVehicleHandlesMessagingViewController _messagesIconImage]
+ -[CARSetupVehicleHandlesMessagingViewController _selectedOption]
+ -[CARSetupVehicleHandlesMessagingViewController _vehicleMessagesIconImage]
+ -[CARSetupVehicleHandlesMessagingViewController initWithVehicleName:responseHandler:]
+ -[CARSetupVehicleHandlesMessagingViewController messagesAppName]
+ -[CARSetupVehicleHandlesMessagingViewController numberOfSectionsInTableView:]
+ -[CARSetupVehicleHandlesMessagingViewController responseHandler]
+ -[CARSetupVehicleHandlesMessagingViewController setMessagesAppName:]
+ -[CARSetupVehicleHandlesMessagingViewController setTableHeightConstraint:]
+ -[CARSetupVehicleHandlesMessagingViewController setUseVehicleForMessaging:]
+ -[CARSetupVehicleHandlesMessagingViewController tableHeightConstraint]
+ -[CARSetupVehicleHandlesMessagingViewController tableView:cellForRowAtIndexPath:]
+ -[CARSetupVehicleHandlesMessagingViewController tableView:didSelectRowAtIndexPath:]
+ -[CARSetupVehicleHandlesMessagingViewController tableView:numberOfRowsInSection:]
+ -[CARSetupVehicleHandlesMessagingViewController tableView:titleForFooterInSection:]
+ -[CARSetupVehicleHandlesMessagingViewController useVehicleForMessaging]
+ -[CARSetupVehicleHandlesMessagingViewController viewDidLayoutSubviews]
+ -[CARSetupVehicleHandlesMessagingViewController viewDidLoad]
+ GCC_except_table23
+ GCC_except_table4
+ _CGRectZero
+ _NSStringFromSOSiriOrchestrationMode
+ _OBJC_CLASS_$_CAPackage
+ _OBJC_CLASS_$_CARSetupVehicleHandlesMessagingViewController
+ _OBJC_CLASS_$_CARSetupVehicleMessageAIProcessingAlert
+ _OBJC_CLASS_$_CAStateController
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_OBTableWelcomeController
+ _OBJC_CLASS_$_UIAlertAction
+ _OBJC_CLASS_$_UIAlertController
+ _OBJC_CLASS_$_UIListContentConfiguration
+ _OBJC_CLASS_$_UITableView
+ _OBJC_CLASS_$_UITableViewCell
+ _OBJC_IVAR_$_CARSetupAppIconProgressView._stateController
+ _OBJC_IVAR_$_CARSetupOnboardingViewController._showMoreIntegrationOptions
+ _OBJC_IVAR_$_CARSetupVehicleHandlesMessagingViewController._messagesAppName
+ _OBJC_IVAR_$_CARSetupVehicleHandlesMessagingViewController._responseHandler
+ _OBJC_IVAR_$_CARSetupVehicleHandlesMessagingViewController._tableHeightConstraint
+ _OBJC_IVAR_$_CARSetupVehicleHandlesMessagingViewController._useVehicleForMessaging
+ _OBJC_METACLASS_$_CARSetupVehicleHandlesMessagingViewController
+ _OBJC_METACLASS_$_CARSetupVehicleMessageAIProcessingAlert
+ _OBJC_METACLASS_$_OBTableWelcomeController
+ _SOFetchSiriAvailability
+ _UIFontTextStyleHeadline
+ __OBJC_$_CLASS_METHODS_CARSetupVehicleMessageAIProcessingAlert
+ __OBJC_$_INSTANCE_METHODS_CARSetupVehicleHandlesMessagingViewController
+ __OBJC_$_INSTANCE_VARIABLES_CARSetupVehicleHandlesMessagingViewController
+ __OBJC_$_PROP_LIST_CARSetupVehicleHandlesMessagingViewController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIScrollViewDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UITableViewDataSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UITableViewDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UITableViewDataSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIScrollViewDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UITableViewDataSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UITableViewDelegate
+ __OBJC_$_PROTOCOL_REFS_UIScrollViewDelegate
+ __OBJC_$_PROTOCOL_REFS_UITableViewDataSource
+ __OBJC_$_PROTOCOL_REFS_UITableViewDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CARSetupVehicleHandlesMessagingViewController
+ __OBJC_CLASS_RO_$_CARSetupVehicleHandlesMessagingViewController
+ __OBJC_CLASS_RO_$_CARSetupVehicleMessageAIProcessingAlert
+ __OBJC_LABEL_PROTOCOL_$_UIScrollViewDelegate
+ __OBJC_LABEL_PROTOCOL_$_UITableViewDataSource
+ __OBJC_LABEL_PROTOCOL_$_UITableViewDelegate
+ __OBJC_METACLASS_RO_$_CARSetupVehicleHandlesMessagingViewController
+ __OBJC_METACLASS_RO_$_CARSetupVehicleMessageAIProcessingAlert
+ __OBJC_PROTOCOL_$_UIScrollViewDelegate
+ __OBJC_PROTOCOL_$_UITableViewDataSource
+ __OBJC_PROTOCOL_$_UITableViewDelegate
+ ___65-[CARSetupOnboardingViewController initWithFeatures:doneHandler:]_block_invoke_3
+ ___68+[CARSetupVehicleMessageAIProcessingAlert alertWithResponseHandler:]_block_invoke
+ ___68+[CARSetupVehicleMessageAIProcessingAlert alertWithResponseHandler:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e23_v16?0"UIAlertAction"8ls32l8
+ _kCAPackageTypeArchive
- +[CARMicaPlayer boolFromDictionary:key:defaultValue:]
- +[CARMicaPlayer rootDictForPath:]
- GCC_except_table25
- _AFDeviceSupportsSystemAssistantExperience
- _OBJC_CLASS_$_NSData
- _OBJC_CLASS_$_NSKeyedUnarchiver
- _OBJC_CLASS_$_NSNumber
- _OBJC_CLASS_$_NSSet
CStrings:
+ "CARSetupVehicleHandlesMessagingCell"
+ "CONTINUE_WITH_CARPLAY"
+ "CarPlayProgress"
+ "MORE_INTEGRATION_OPTIONS"
+ "Onboarding/welcome: proceed to more integration options"
+ "Siri orchestration mode for app icon progress animation: %{public}@"
+ "Unable to load Mica document with path: %@, error = %@"
+ "VEHICLE_MESSAGE_AI_PROCESSING_ALLOW"
+ "VEHICLE_MESSAGE_AI_PROCESSING_BODY"
+ "VEHICLE_MESSAGE_AI_PROCESSING_DONT_ALLOW"
+ "VEHICLE_MESSAGE_AI_PROCESSING_TITLE"
+ "VEHICLE_MESSAGING_CARD_BODY"
+ "VEHICLE_MESSAGING_CARD_TITLE_%@"
+ "VEHICLE_MESSAGING_CONTINUE"
+ "VEHICLE_MESSAGING_FOOTER"
+ "VEHICLE_MESSAGING_OPTION_MESSAGES_DETAIL"
+ "VEHICLE_MESSAGING_OPTION_MESSAGES_UNINSTALLED_TITLE"
+ "VEHICLE_MESSAGING_OPTION_VEHICLE_DETAIL"
+ "VEHICLE_MESSAGING_OPTION_VEHICLE_TITLE"
+ "bubble.left.and.text.bubble.right.fill"
+ "com.apple.MobileSMS"
+ "missing state %{public}@ in app icon progress animation"
+ "siri"
+ "siri.gen.1"
+ "siri.gen.2"
+ "v16@?0@\"UIAlertAction\"8"
+ "vehicle handles messaging prompt selection changed, use vehicle: %{public}@"
- "CarPlayProgressSAE"
- "CarPlayProgressSiri"
- "Unable to load Mica document with path: %@"
- "Unable to open Mica file: %@"
- "error = %@"
- "publishedObjects"
- "rootLayer"
- "show system experience CarPlay animation: %{public}@"
```
