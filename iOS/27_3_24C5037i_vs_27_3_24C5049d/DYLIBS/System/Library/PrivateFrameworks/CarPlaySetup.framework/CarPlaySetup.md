## CarPlaySetup

> `/System/Library/PrivateFrameworks/CarPlaySetup.framework/CarPlaySetup`

```diff

-808.6.0.0.0
-  __TEXT.__text: 0xc6d0
-  __TEXT.__objc_methlist: 0xe90
-  __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x1362
-  __TEXT.__gcc_except_tab: 0x2fc
-  __TEXT.__oslogstring: 0x57d
-  __TEXT.__unwind_info: 0x3d0
+808.9.1.0.0
+  __TEXT.__text: 0xd318
+  __TEXT.__objc_methlist: 0xf30
+  __TEXT.__const: 0xb8
+  __TEXT.__cstring: 0x13bb
+  __TEXT.__gcc_except_tab: 0x340
+  __TEXT.__oslogstring: 0x5e4
+  __TEXT.__unwind_info: 0x408
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x298
+  __DATA_CONST.__const: 0x2c0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe98
+  __DATA_CONST.__objc_selrefs: 0xf40
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0xb0
-  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__got: 0x268
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x1a00
-  __AUTH_CONST.__objc_const: 0x1af0
+  __AUTH_CONST.__cfstring: 0x1a40
+  __AUTH_CONST.__objc_const: 0x1bc0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xa4
+  __DATA.__objc_ivar: 0xb4
   __DATA.__data: 0x2a0
   __DATA_DIRTY.__objc_data: 0x370
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SiriAvailability.framework/SiriAvailability
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 245
-  Symbols:   596
-  CStrings:  256
+  Functions: 259
+  Symbols:   624
+  CStrings:  261
 
Symbols:
+ -[CARSetupMessageProcessingViewController .cxx_destruct]
+ -[CARSetupMessageProcessingViewController _handleAllow:]
+ -[CARSetupMessageProcessingViewController _handleDecline:]
+ -[CARSetupMessageProcessingViewController _messagesPrivacyIcon]
+ -[CARSetupMessageProcessingViewController initWithVehicleBrand:responseHandler:]
+ -[CARSetupMessageProcessingViewController responseHandler]
+ -[CARSetupMessageProcessingViewController viewDidLoad]
+ -[CARSetupVehicleHandlesMessagingViewController _presentAIConsentAlert]
+ -[CARSetupVehicleHandlesMessagingViewController _respondWithAccepted:]
+ -[CARSetupVehicleHandlesMessagingViewController _setUseVehicleForMessaging:]
+ -[CARSetupVehicleHandlesMessagingViewController hasResponded]
+ -[CARSetupVehicleHandlesMessagingViewController initWithVehicleBrand:needsAIConsent:responseHandler:]
+ -[CARSetupVehicleHandlesMessagingViewController needsAIConsent]
+ -[CARSetupVehicleHandlesMessagingViewController setHasResponded:]
+ -[CARSetupVehicleHandlesMessagingViewController vehicleBrand]
+ _CGRectGetMaxX
+ _CGRectGetMaxY
+ _CGRectGetMidX
+ _CGRectGetMidY
+ _CGRectGetMinX
+ _CGRectGetMinY
+ _OBJC_CLASS_$_CARSetupMessageProcessingViewController
+ _OBJC_CLASS_$_UIGraphicsImageRenderer
+ _OBJC_CLASS_$_UIGraphicsImageRendererFormat
+ _OBJC_IVAR_$_CARSetupMessageProcessingViewController._responseHandler
+ _OBJC_IVAR_$_CARSetupVehicleHandlesMessagingViewController._hasResponded
+ _OBJC_IVAR_$_CARSetupVehicleHandlesMessagingViewController._needsAIConsent
+ _OBJC_IVAR_$_CARSetupVehicleHandlesMessagingViewController._vehicleBrand
+ _OBJC_METACLASS_$_CARSetupMessageProcessingViewController
+ __OBJC_$_INSTANCE_METHODS_CARSetupMessageProcessingViewController
+ __OBJC_$_INSTANCE_VARIABLES_CARSetupMessageProcessingViewController
+ __OBJC_$_PROP_LIST_CARSetupMessageProcessingViewController
+ __OBJC_CLASS_RO_$_CARSetupMessageProcessingViewController
+ __OBJC_METACLASS_RO_$_CARSetupMessageProcessingViewController
+ ___63-[CARSetupMessageProcessingViewController _messagesPrivacyIcon]_block_invoke
+ ___71-[CARSetupVehicleHandlesMessagingViewController _presentAIConsentAlert]_block_invoke
+ ___block_descriptor_112_e8_32s40s_e40_v16?0"UIGraphicsImageRendererContext"8ls32l8s40l8
+ ___block_descriptor_40_e8_32w_e23_v16?0"UIAlertAction"8lw32l8
- +[CARSetupVehicleMessageAIProcessingAlert alertWithResponseHandler:]
- -[CARSetupVehicleHandlesMessagingViewController initWithVehicleName:responseHandler:]
- _OBJC_CLASS_$_CARSetupVehicleMessageAIProcessingAlert
- _OBJC_METACLASS_$_CARSetupVehicleMessageAIProcessingAlert
- __OBJC_$_CLASS_METHODS_CARSetupVehicleMessageAIProcessingAlert
- __OBJC_CLASS_RO_$_CARSetupVehicleMessageAIProcessingAlert
- __OBJC_METACLASS_RO_$_CARSetupVehicleMessageAIProcessingAlert
- ___68+[CARSetupVehicleMessageAIProcessingAlert alertWithResponseHandler:]_block_invoke
- ___68+[CARSetupVehicleMessageAIProcessingAlert alertWithResponseHandler:]_block_invoke_2
- ___block_descriptor_40_e8_32bs_e23_v16?0"UIAlertAction"8ls32l8
CStrings:
+ "VEHICLE_MESSAGE_PROCESSING_ALLOW"
+ "VEHICLE_MESSAGE_PROCESSING_CARD_BODY_%@"
+ "VEHICLE_MESSAGE_PROCESSING_CARD_TITLE_%@"
+ "VEHICLE_MESSAGE_PROCESSING_DONT_ALLOW"
+ "VEHICLE_MESSAGING_AUTOMAKER"
+ "VEHICLE_MESSAGING_CARD_TITLE"
+ "VEHICLE_MESSAGING_OPTION_VEHICLE_TITLE_%@"
+ "bubble.left.and.text.bubble.right"
+ "hand.raised.app.fill"
+ "v16@?0@\"UIGraphicsImageRendererContext\"8"
+ "vehicle handles messaging AI consent alert allowed"
+ "vehicle handles messaging AI consent alert declined"
- "VEHICLE_MESSAGE_AI_PROCESSING_ALLOW"
- "VEHICLE_MESSAGE_AI_PROCESSING_BODY"
- "VEHICLE_MESSAGE_AI_PROCESSING_DONT_ALLOW"
- "VEHICLE_MESSAGE_AI_PROCESSING_TITLE"
- "VEHICLE_MESSAGING_CARD_TITLE_%@"
- "VEHICLE_MESSAGING_OPTION_VEHICLE_TITLE"
- "bubble.left.and.text.bubble.right.fill"
```
