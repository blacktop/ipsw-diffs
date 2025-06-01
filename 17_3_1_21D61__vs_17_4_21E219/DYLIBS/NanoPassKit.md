## NanoPassKit

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit`

```diff

-1161.3.0.0.0
-  __TEXT.__text: 0x21185c
+1163.8.0.0.0
+  __TEXT.__text: 0x2125b8
   __TEXT.__auth_stubs: 0x17e0
-  __TEXT.__objc_methlist: 0x2040c
+  __TEXT.__objc_methlist: 0x20464
   __TEXT.__const: 0x250
-  __TEXT.__cstring: 0x165e9
-  __TEXT.__oslogstring: 0x284e2
+  __TEXT.__cstring: 0x165f7
+  __TEXT.__oslogstring: 0x28649
   __TEXT.__gcc_except_tab: 0x3c80
   __TEXT.__dlopen_cstrs: 0x2eb
   __TEXT.__ustring: 0x160
-  __TEXT.__unwind_info: 0x7ea8
-  __TEXT.__objc_classname: 0x6450
-  __TEXT.__objc_methname: 0x3b804
-  __TEXT.__objc_methtype: 0x96d6
-  __TEXT.__objc_stubs: 0x20060
+  __TEXT.__unwind_info: 0x7ebc
+  __TEXT.__objc_classname: 0x6451
+  __TEXT.__objc_methname: 0x3b8b4
+  __TEXT.__objc_methtype: 0x96d9
+  __TEXT.__objc_stubs: 0x20180
   __DATA_CONST.__got: 0x7b0
-  __DATA_CONST.__const: 0x6418
+  __DATA_CONST.__const: 0x6490
   __DATA_CONST.__objc_classlist: 0x1098
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x39488
-  __DATA_CONST.__objc_selrefs: 0xb5a8
+  __DATA_CONST.__objc_const: 0x394e8
+  __DATA_CONST.__objc_selrefs: 0xb5e8
+  __DATA_CONST.__objc_protorefs: 0x90
+  __DATA_CONST.__objc_classrefs: 0x1438
+  __DATA_CONST.__objc_superrefs: 0xfd8
   __DATA_CONST.__objc_arraydata: 0x88
   __AUTH_CONST.__cfstring: 0xe160
   __AUTH_CONST.__objc_const: 0xc2d8

   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_got: 0xc00
   __AUTH.__objc_data: 0xa5a0
-  __DATA.__objc_protorefs: 0x90
-  __DATA.__objc_classrefs: 0x1438
-  __DATA.__objc_superrefs: 0xfd8
-  __DATA.__objc_ivar: 0x1a6c
+  __DATA.__objc_ivar: 0x1a74
   __DATA.__data: 0x1bd0
   __DATA.__bss: 0x360
   __DATA.__common: 0x8

   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 0D2D21DB-4845-315A-B850-8F781E820BCA
-  Functions: 13014
-  Symbols:   39003
-  CStrings:  16080
+  UUID: 14857387-A830-38AE-B6F7-48DA96FA67EA
+  Functions: 13029
+  Symbols:   39045
+  CStrings:  16097
 
Symbols:
+ -[NPKAuthIntentListener _handleButtonEvent:]
+ -[NPKAuthIntentListener _initializeHIDClient]
+ -[NPKAuthIntentListener dealloc]
+ -[NPKAuthIntentListener hidSystemClient]
+ -[NPKAuthIntentListener init]
+ -[NPKAuthIntentListener setHidSystemClient:]
+ -[NPKContactlessPaymentSessionManager _handleSessionTimerFired]
+ -[NPKContactlessPaymentSessionManager _startSessionTimerWithReason:]
+ -[NPKContactlessPaymentSessionManager _stopSessionTimer]
+ -[NPKContactlessPaymentSessionManager sessionTimer]
+ -[NPKContactlessPaymentSessionManager setSessionTimer:]
+ -[NPKDoublePressDelegationAssertion handleDelegatedDoublePressEventWithSource:]
+ -[NPKPaymentProvisioningFlowController _checkSpaceAvailableForAppletTypes:triedCleanup:completion:]
+ -[NPKPaymentProvisioningFlowController _handleEligibiltySuccessWithContext:]
+ -[NPKPaymentProvisioningFlowController _performSEStorageCheck:]
+ -[NPKProtoAcceptSubcredentialInvitationResponse hasPending]
+ -[NPKProtoAcceptSubcredentialInvitationResponse pending]
+ -[NPKProtoAcceptSubcredentialInvitationResponse setHasPending:]
+ -[NPKProtoAcceptSubcredentialInvitationResponse setPending:]
+ -[NPKQuickPaymentSessionSource _handleAuthIntentEventFromSource:]
+ -[NPKRemoteButtonListener doublePressDelegationAssertionDidReceiveDelegatedDoublePressEvent:authIntentSource:]
+ -[NPKTransientAssertion handleDelegatedDoublePressEventWithSource:]
+ -[PKExpressPassInformation(NanoPassKit) npk_expressAppletIdentifiers]
+ GCC_except_table154
+ GCC_except_table164
+ GCC_except_table174
+ GCC_except_table181
+ _NPKIsAssistiveTouchEnabled
+ _NSStringFromNPKContactlessPaymentSessionTimerReason
+ _OBJC_CLASS_$_NPKAuthIntentListener
+ _OBJC_CLASS_$_PKProvisioningSEStorageManager
+ _OBJC_IVAR_$_NPKAuthIntentListener._hidSystemClient
+ _OBJC_IVAR_$_NPKContactlessPaymentSessionManager._sessionTimer
+ _OBJC_IVAR_$_NPKProtoAcceptSubcredentialInvitationResponse._has
+ _OBJC_IVAR_$_NPKProtoAcceptSubcredentialInvitationResponse._pending
+ _OBJC_METACLASS_$_NPKAuthIntentListener
+ _PKDynamicSEAllocationFakeFullSE
+ _PKEnableDynamicSEAllocation
+ __OBJC_$_INSTANCE_METHODS_NPKAuthIntentListener
+ __OBJC_$_INSTANCE_VARIABLES_NPKAuthIntentListener
+ __OBJC_$_PROP_LIST_NPKAuthIntentListener
+ __OBJC_$_PROP_LIST_NPKBalanceField.147
+ __OBJC_$_PROP_LIST_NPKCommutePlanField.198
+ __OBJC_$_PROP_LIST_NPKDateRange.71
+ __OBJC_CLASS_RO_$_NPKAuthIntentListener
+ __OBJC_METACLASS_RO_$_NPKAuthIntentListener
+ ___111-[NPKContactlessPaymentSessionManager _handleRKEActionRequestedForPass:action:function:withSession:completion:]_block_invoke.542
+ ___122-[NPKPaymentWebServiceCompanionTargetDevice _trackOutstandingRequestWithMessageIdentifier:completionHandler:errorHandler:]_block_invoke.894
+ ___152-[NPKContactlessPaymentSessionManagerTransactionContext updateWithConcreteTransactions:ephemeralTransaction:updatedPassTransitItems:paymentApplication:]_block_invoke.362
+ ___152-[NPKContactlessPaymentSessionManagerTransactionContext updateWithConcreteTransactions:ephemeralTransaction:updatedPassTransitItems:paymentApplication:]_block_invoke.380
+ ___35-[NPKRemoteInterfacePresenter init]_block_invoke.77
+ ___39-[NPKTransientAssertion initWithQueue:]_block_invoke.104
+ ___45-[NPKAuthIntentListener _initializeHIDClient]_block_invoke
+ ___65-[NPKQuickPaymentSessionSource _handleAuthIntentEventFromSource:]_block_invoke
+ ___65-[NPKQuickPaymentSessionSource _handleAuthIntentEventFromSource:]_block_invoke.73
+ ___65-[NPKQuickPaymentSessionSource _handleAuthIntentEventFromSource:]_block_invoke.74
+ ___65-[NPKQuickPaymentSessionSource _handleAuthIntentEventFromSource:]_block_invoke.76
+ ___65-[NPKQuickPaymentSessionSource _handleAuthIntentEventFromSource:]_block_invoke.77
+ ___69-[PKExpressPassInformation(NanoPassKit) npk_expressAppletIdentifiers]_block_invoke
+ ___76-[NPKPaymentProvisioningFlowController _handleEligibiltySuccessWithContext:]_block_invoke
+ ___76-[NPKPaymentProvisioningFlowController _handleEligibiltySuccessWithContext:]_block_invoke_2
+ ___83-[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:withStates:]_block_invoke.517
+ ___83-[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:withStates:]_block_invoke.519
+ ___83-[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:withStates:]_block_invoke.520
+ ___91-[NPKPaymentWebServiceCompanionTargetDevice hasActiveExternallySharedPassesWithCompletion:]_block_invoke.891
+ ___93-[NPKPaymentWebServiceCompanionTargetDevice paymentSetupFeaturesForConfiguration:completion:]_block_invoke.874
+ ___99-[NPKPaymentProvisioningFlowController _checkSpaceAvailableForAppletTypes:triedCleanup:completion:]_block_invoke
+ ___99-[NPKPaymentProvisioningFlowController _checkSpaceAvailableForAppletTypes:triedCleanup:completion:]_block_invoke.114
+ ___block_descriptor_40_e8_32s_e31_v32?0"NSArray"8"NSSet"16^B24ls32l8
+ ___block_descriptor_40_e8_32w_e8_v16?0Q8lw32l8
+ ___block_descriptor_57_e8_32s40s48bs_e41_v16?0"PKProvisioningSEStorageSnapshot"8ls32l8s40l8s48l8
+ ___block_literal_global.139
+ ___block_literal_global.511
+ ___block_literal_global.516
+ ___block_literal_global.868
+ ___block_literal_global.87
+ _objc_msgSend$_checkSpaceAvailableForAppletTypes:triedCleanup:completion:
+ _objc_msgSend$_handleAuthIntentEventFromSource:
+ _objc_msgSend$_handleEligibiltySuccessWithContext:
+ _objc_msgSend$_handleSessionTimerFired
+ _objc_msgSend$_performSEStorageCheck:
+ _objc_msgSend$_startSessionTimerWithReason:
+ _objc_msgSend$_stopSessionTimer
+ _objc_msgSend$appletTypeIdentifier
+ _objc_msgSend$canFitAppletTypes:
+ _objc_msgSend$debugPerformSECleanup:
+ _objc_msgSend$descriptionText
+ _objc_msgSend$doublePressDelegationAssertionDidReceiveDelegatedDoublePressEvent:authIntentSource:
+ _objc_msgSend$extractApplicationIdentifier:subcredentialIdentifier:fromIdentifiers:
+ _objc_msgSend$getCurrentSnapshot:
+ _objc_msgSend$handleEndSessionRequestedForReason:
+ _objc_msgSend$initWithWebService:
+ _objc_msgSend$npk_expressAppletIdentifiers
+ _objc_msgSend$paymentSessionSource:receivedDelegatedButtonEventAtDate:authIntentSource:
+ _objc_msgSend$paymentSessionSource:startedPaymentSession:dueToButtonEventAtDate:authIntentSource:
+ _objc_msgSend$paymentSessionSourceRequestsAssistiveTouchAlertPresentation:
+ _objc_msgSend$pk_safelyAddObject:
+ _objc_msgSend$setAssociatedPlan:
+ _objc_msgSend$setDescriptionText:
+ _timeIntervalWithNPKContactlessPaymentSessionTimerReason
- -[NPKContactlessPaymentSessionManager _handleContactlessInterfaceVisibilityTimeoutTimer]
- -[NPKContactlessPaymentSessionManager _startContactlessInterfaceVisibilityTimeoutTimer]
- -[NPKContactlessPaymentSessionManager _stopContactlessInterfaceVisibilityTimeoutTimer]
- -[NPKContactlessPaymentSessionManager contactlessInterfaceVisibilityTimeoutTimer]
- -[NPKContactlessPaymentSessionManager setContactlessInterfaceVisibilityTimeoutTimer:]
- -[NPKDoublePressDelegationAssertion handleDelegatedDoublePressEvent]
- -[NPKPMUButtonListener _handleButtonEvent:]
- -[NPKPMUButtonListener _initializeHIDClient]
- -[NPKPMUButtonListener dealloc]
- -[NPKPMUButtonListener hidSystemClient]
- -[NPKPMUButtonListener init]
- -[NPKPMUButtonListener setHidSystemClient:]
- -[NPKQuickPaymentSessionSource _handlePMUButtonEvent]
- -[NPKRemoteButtonListener doublePressDelegationAssertionDidReceiveDelegatedDoublePressEvent:]
- -[NPKTransientAssertion handleDelegatedDoublePressEvent]
- -[PKExpressPassInformation(NanoPassKit) npk_getAppletIdentifiers:appletsToKeys:includeKeyContainerAsApplet:]
- GCC_except_table152
- GCC_except_table162
- GCC_except_table172
- _NPKIsDoubleClickToConfirmDisabled
- _NSSelectorFromString
- _OBJC_CLASS_$_NPKPMUButtonListener
- _OBJC_CLASS_$_NSInvocation
- _OBJC_IVAR_$_NPKContactlessPaymentSessionManager._contactlessInterfaceVisibilityTimeoutTimer
- _OBJC_IVAR_$_NPKPMUButtonListener._hidSystemClient
- _OBJC_METACLASS_$_NPKPMUButtonListener
- _PKEnableDynamicSEAllocationIsWatch
- __OBJC_$_INSTANCE_METHODS_NPKPMUButtonListener
- __OBJC_$_INSTANCE_VARIABLES_NPKPMUButtonListener
- __OBJC_$_PROP_LIST_NPKBalanceField.146
- __OBJC_$_PROP_LIST_NPKCommutePlanField.197
- __OBJC_$_PROP_LIST_NPKDateRange.70
- __OBJC_$_PROP_LIST_NPKPMUButtonListener
- __OBJC_CLASS_RO_$_NPKPMUButtonListener
- __OBJC_METACLASS_RO_$_NPKPMUButtonListener
- ___111-[NPKContactlessPaymentSessionManager _handleRKEActionRequestedForPass:action:function:withSession:completion:]_block_invoke.528
- ___122-[NPKPaymentWebServiceCompanionTargetDevice _trackOutstandingRequestWithMessageIdentifier:completionHandler:errorHandler:]_block_invoke.893
- ___152-[NPKContactlessPaymentSessionManagerTransactionContext updateWithConcreteTransactions:ephemeralTransaction:updatedPassTransitItems:paymentApplication:]_block_invoke.355
- ___152-[NPKContactlessPaymentSessionManagerTransactionContext updateWithConcreteTransactions:ephemeralTransaction:updatedPassTransitItems:paymentApplication:]_block_invoke.373
- ___35-[NPKRemoteInterfacePresenter init]_block_invoke.75
- ___39-[NPKTransientAssertion initWithQueue:]_block_invoke.102
- ___44-[NPKPMUButtonListener _initializeHIDClient]_block_invoke
- ___53-[NPKQuickPaymentSessionSource _handlePMUButtonEvent]_block_invoke
- ___53-[NPKQuickPaymentSessionSource _handlePMUButtonEvent]_block_invoke.72
- ___53-[NPKQuickPaymentSessionSource _handlePMUButtonEvent]_block_invoke.74
- ___53-[NPKQuickPaymentSessionSource _handlePMUButtonEvent]_block_invoke.75
- ___83-[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:withStates:]_block_invoke.510
- ___83-[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:withStates:]_block_invoke.512
- ___83-[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:withStates:]_block_invoke.513
- ___91-[NPKPaymentWebServiceCompanionTargetDevice hasActiveExternallySharedPassesWithCompletion:]_block_invoke.890
- ___93-[NPKPaymentWebServiceCompanionTargetDevice paymentSetupFeaturesForConfiguration:completion:]_block_invoke.873
- ___block_literal_global.134
- ___block_literal_global.509
- ___block_literal_global.82
- ___block_literal_global.84
- ___block_literal_global.86
- ___block_literal_global.867
- _objc_msgSend$_handleContactlessInterfaceVisibilityTimeoutTimer
- _objc_msgSend$_handlePMUButtonEvent
- _objc_msgSend$_startContactlessInterfaceVisibilityTimeoutTimer
- _objc_msgSend$_stopContactlessInterfaceVisibilityTimeoutTimer
- _objc_msgSend$doublePressDelegationAssertionDidReceiveDelegatedDoublePressEvent:
- _objc_msgSend$invocationWithMethodSignature:
- _objc_msgSend$invoke
- _objc_msgSend$methodSignatureForSelector:
- _objc_msgSend$npk_getAppletIdentifiers:appletsToKeys:includeKeyContainerAsApplet:
- _objc_msgSend$paymentSessionSource:receivedDelegatedButtonEventAtDate:
- _objc_msgSend$paymentSessionSource:startedPaymentSession:dueToButtonEventAtDate:
- _objc_msgSend$setArgument:atIndex:
- _objc_msgSend$setSelector:
- _objc_msgSend$setTarget:
CStrings:
+ "-[NPKTransientAssertion handleDelegatedDoublePressEventWithSource:]"
+ "NPKAuthIntentListener"
+ "Notice: Error converting encrypted payload to JSON string: %@"
+ "Notice: Overriding canFit to NO b/c fake full se"
+ "Notice: Performing SE storage check."
+ "Notice: Received encrypted payload %@"
+ "Notice: SE storage check returned can fit applets on SE: %@ from snapshot %@"
+ "Notice: Session source is NOT delegating auth intent event"
+ "Notice: Session source is delegating auth intent event"
+ "Notice: Session source received an assistive touch gesture event"
+ "Notice: Starting contactless session timer for reason: %@"
+ "Notice: Stopping contactless session timer"
+ "Notice: contactless session timer fired with visibility %d"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_sessionTimer"
+ "T@\"NSString\",?,R,C"
+ "Warning: Do not call NPKMaxPaymentCards with dynamic SE enabled."
+ "Warning: Received unexpected auth intent source: %lu, is double click disabled: %i"
+ "_checkSpaceAvailableForAppletTypes:triedCleanup:completion:"
+ "_handleAuthIntentEventFromSource:"
+ "_handleEligibiltySuccessWithContext:"
+ "_handleSessionTimerFired"
+ "_performSEStorageCheck:"
+ "_sessionTimer"
+ "_startSessionTimerWithReason:"
+ "_stopSessionTimer"
+ "appletTypeIdentifier"
+ "authTokenInUse"
+ "canFitAppletTypes:"
+ "debugPerformSECleanup:"
+ "descriptionText"
+ "doublePressDelegationAssertionDidReceiveDelegatedDoublePressEvent:authIntentSource:"
+ "extractApplicationIdentifier:subcredentialIdentifier:fromIdentifiers:"
+ "getCurrentSnapshot:"
+ "handleDelegatedDoublePressEventWithSource:"
+ "initWithWebService:"
+ "npk_expressAppletIdentifiers"
+ "paymentSessionSource:receivedDelegatedButtonEventAtDate:authIntentSource:"
+ "paymentSessionSource:startedPaymentSession:dueToButtonEventAtDate:authIntentSource:"
+ "paymentSessionSourceRequestsAssistiveTouchAlertPresentation:"
+ "pk_safelyAddObject:"
+ "sessionCreated"
+ "sessionTimer"
+ "setAssociatedPlan:"
+ "setDescriptionText:"
+ "setSessionTimer:"
+ "v16@?0@\"PKProvisioningSEStorageSnapshot\"8"
+ "v32@0:8@\"NPKDoublePressDelegationAssertion\"16Q24"
- "-[NPKTransientAssertion handleDelegatedDoublePressEvent]"
- "NPKPMUButtonListener"
- "Notice: Contactless interface visibility timer fired with visibility %d"
- "Notice: Session source is NOT delegating button event"
- "Notice: Session source is delegating button event"
- "Notice: Setting contactless interface visibility timer"
- "Notice: Stopping contactless interface visibility timer"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_contactlessInterfaceVisibilityTimeoutTimer"
- "Warning: Unable to perform selector for getAppletIdentifiers:appletsToKeys:includeKeyContainerAsApplet:"
- "_contactlessInterfaceVisibilityTimeoutTimer"
- "_handleContactlessInterfaceVisibilityTimeoutTimer"
- "_handlePMUButtonEvent"
- "_startContactlessInterfaceVisibilityTimeoutTimer"
- "_stopContactlessInterfaceVisibilityTimeoutTimer"
- "contactlessInterfaceVisibilityTimeoutTimer"
- "doublePressDelegationAssertionDidReceiveDelegatedDoublePressEvent:"
- "getAppletIdentifiers:appletsToKeys:includeKeyContainerAsApplet:"
- "handleDelegatedDoublePressEvent"
- "invocationWithMethodSignature:"
- "invoke"
- "methodSignatureForSelector:"
- "npk_getAppletIdentifiers:appletsToKeys:includeKeyContainerAsApplet:"
- "paymentSessionSource:receivedDelegatedButtonEventAtDate:"
- "paymentSessionSource:startedPaymentSession:dueToButtonEventAtDate:"
- "setArgument:atIndex:"
- "setContactlessInterfaceVisibilityTimeoutTimer:"
- "setSelector:"
- "setTarget:"
- "true"
- "v24@0:8@\"NPKDoublePressDelegationAssertion\"16"

```
