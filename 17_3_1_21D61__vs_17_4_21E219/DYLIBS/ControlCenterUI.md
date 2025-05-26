## ControlCenterUI

> `/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI`

```diff

-520.10.0.0.0
-  __TEXT.__text: 0x33030
-  __TEXT.__auth_stubs: 0x9d0
-  __TEXT.__objc_methlist: 0x3900
+520.107.0.0.0
+  __TEXT.__text: 0x33e08
+  __TEXT.__auth_stubs: 0x9e0
+  __TEXT.__objc_methlist: 0x3a50
   __TEXT.__const: 0x380
-  __TEXT.__cstring: 0x10d1
+  __TEXT.__cstring: 0x11d7
   __TEXT.__oslogstring: 0xef0
-  __TEXT.__gcc_except_tab: 0x378
-  __TEXT.__unwind_info: 0xfb8
-  __TEXT.__objc_classname: 0xbbf
-  __TEXT.__objc_methname: 0xcc0e
-  __TEXT.__objc_methtype: 0x2852
-  __TEXT.__objc_stubs: 0x8800
-  __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0xac0
-  __DATA_CONST.__objc_classlist: 0x1d0
+  __TEXT.__gcc_except_tab: 0x37c
+  __TEXT.__unwind_info: 0xffc
+  __TEXT.__objc_classname: 0xbf4
+  __TEXT.__objc_methname: 0xd0f4
+  __TEXT.__objc_methtype: 0x28b9
+  __TEXT.__objc_stubs: 0x8b20
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__const: 0xb80
+  __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x120
+  __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9c20
-  __DATA_CONST.__objc_selrefs: 0x2868
+  __DATA_CONST.__objc_const: 0x9e00
+  __DATA_CONST.__objc_selrefs: 0x2958
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x450
+  __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__cfstring: 0xe20
-  __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__objc_const: 0x1580
+  __AUTH_CONST.__cfstring: 0xf20
+  __AUTH_CONST.__const: 0x480
+  __AUTH_CONST.__objc_const: 0x15c8
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__auth_got: 0x4f8
-  __AUTH.__objc_data: 0x2d0
+  __AUTH_CONST.__auth_got: 0x500
+  __AUTH.__objc_data: 0x320
   __AUTH.__data: 0x28
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x440
-  __DATA.__objc_superrefs: 0x158
-  __DATA.__objc_ivar: 0x480
-  __DATA.__data: 0xd98
+  __DATA.__objc_ivar: 0x498
+  __DATA.__data: 0xdf8
   __DATA.__bss: 0x88
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xf50

   - /System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI
   - /System/Library/PrivateFrameworks/ControlCenterServices.framework/ControlCenterServices
   - /System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/MaterialKit.framework/MaterialKit

   - /System/Library/PrivateFrameworks/SystemStatusUI.framework/SystemStatusUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1428
-  Symbols:   5476
-  CStrings:  2475
+  Functions: 1460
+  Symbols:   5600
+  CStrings:  2534
 
Symbols:
+ -[CCUIAnalyticsEventsController .cxx_destruct]
+ -[CCUIAnalyticsEventsController addProvider:]
+ -[CCUIAnalyticsEventsController allProviders]
+ -[CCUIAnalyticsEventsController dealloc]
+ -[CCUIAnalyticsEventsController eventsControllerDomain]
+ -[CCUIAnalyticsEventsController initWithEventsControllerDomain:]
+ -[CCUIAnalyticsEventsController removeProvider:]
+ -[CCUIAnalyticsEventsController sendEventsForProvidersWhenSignificantTimeChanged]
+ -[CCUIAnalyticsEventsController setAllProviders:]
+ -[CCUIModularControlCenterOverlayViewController _analyticsLogCurrentModuleOrganization]
+ -[CCUIModularControlCenterOverlayViewController _beginSessionForAnalytics]
+ -[CCUIModularControlCenterOverlayViewController _endSessionForAnalytics]
+ -[CCUIModularControlCenterOverlayViewController analyticsEventsController]
+ -[CCUIModularControlCenterOverlayViewController currentSessionIdentifier]
+ -[CCUIModularControlCenterOverlayViewController dealloc]
+ -[CCUIModularControlCenterOverlayViewController moduleCollectionViewController:didExpandModuleWithIdentifier:]
+ -[CCUIModularControlCenterOverlayViewController sessionBeginTime]
+ -[CCUIModularControlCenterOverlayViewController setAnalyticsEventsController:]
+ -[CCUIModularControlCenterOverlayViewController setCurrentSessionIdentifier:]
+ -[CCUIModularControlCenterOverlayViewController setSessionBeginTime:]
+ -[CCUIModularControlCenterOverlayViewController setShouldSendModuleOrganizationToAnalytics:]
+ -[CCUIModularControlCenterOverlayViewController shouldSendModuleOrganizationToAnalytics]
+ -[CCUIModularControlCenterOverlayViewController significantTimeChanged]
+ -[CCUIModularControlCenterOverlayViewController viewDidAppear:]
+ -[CCUIModuleCollectionViewController _analyticsLogExpandedModuleWithIdentifier:]
+ -[CCUIModuleCollectionViewController _moduleIdentifierForModule:]
+ -[CCUIModuleCollectionViewController analyticsLogEnabledModuleOrdered]
+ GCC_except_table127
+ GCC_except_table163
+ _AnalyticsSendEventLazy
+ _CCUIAnalyticsControlCenterInvocation
+ _CCUIAnalyticsControlCenterInvocationActiveDuration
+ _CCUIAnalyticsControlCenterInvocationSessionIdentifier
+ _CCUIAnalyticsControlCenterModuleExpansion
+ _CCUIAnalyticsControlCenterModuleExpansionModuleIdentifier
+ _CCUIAnalyticsControlCenterModuleExpansionSessionID
+ _CCUIAnalyticsControlCenterModuleOrganization
+ _CCUIAnalyticsControlCenterModuleOrganizationModuleIdentifier
+ _CCUIAnalyticsControlCenterModuleOrganizationModuleRanking
+ _CCUIAnalyticsDomainControlCenter
+ _OBJC_CLASS_$_CCUIAnalyticsEventsController
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_IVAR_$_CCUIAnalyticsEventsController._allProviders
+ _OBJC_IVAR_$_CCUIAnalyticsEventsController._eventsControllerDomain
+ _OBJC_IVAR_$_CCUIModularControlCenterOverlayViewController._analyticsEventsController
+ _OBJC_IVAR_$_CCUIModularControlCenterOverlayViewController._currentSessionIdentifier
+ _OBJC_IVAR_$_CCUIModularControlCenterOverlayViewController._sessionBeginTime
+ _OBJC_IVAR_$_CCUIModularControlCenterOverlayViewController._shouldSendModuleOrganizationToAnalytics
+ _OBJC_METACLASS_$_CCUIAnalyticsEventsController
+ _UIApplicationSignificantTimeChangeNotification
+ __OBJC_$_INSTANCE_METHODS_CCUIAnalyticsEventsController
+ __OBJC_$_INSTANCE_VARIABLES_CCUIAnalyticsEventsController
+ __OBJC_$_PROP_LIST_CCUIAnalyticsEventsController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CCUIAnalyticsProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCUIAnalyticsProviding
+ __OBJC_$_PROTOCOL_REFS_CCUIAnalyticsProviding
+ __OBJC_CLASS_RO_$_CCUIAnalyticsEventsController
+ __OBJC_LABEL_PROTOCOL_$_CCUIAnalyticsProviding
+ __OBJC_METACLASS_RO_$_CCUIAnalyticsEventsController
+ __OBJC_PROTOCOL_$_CCUIAnalyticsProviding
+ ___110-[CCUIModularControlCenterOverlayViewController moduleCollectionViewController:didExpandModuleWithIdentifier:]_block_invoke
+ ___60-[CCUIModuleInstanceManager _instantiateModuleWithMetadata:]_block_invoke.73
+ ___70-[CCUIModuleCollectionViewController analyticsLogEnabledModuleOrdered]_block_invoke
+ ___70-[CCUIModuleCollectionViewController analyticsLogEnabledModuleOrdered]_block_invoke_2
+ ___71-[CCUIAnimationRunner additivelyRunAnimationBatch:withCompletionBlock:]_block_invoke.81
+ ___72-[CCUIModularControlCenterOverlayViewController _endSessionForAnalytics]_block_invoke
+ ___81-[CCUIAnalyticsEventsController sendEventsForProvidersWhenSignificantTimeChanged]_block_invoke
+ ___87-[CCUIModularControlCenterOverlayViewController dismissAnimated:withCompletionHandler:]_block_invoke.45
+ ___87-[CCUIModularControlCenterOverlayViewController dismissAnimated:withCompletionHandler:]_block_invoke.48
+ ___block_descriptor_32_e25_v32?0"NSString"8Q16^B24l
+ ___block_descriptor_48_e8_32s40s_e19_"NSDictionary"8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_literal_global.43
+ ___block_literal_global.69
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_analyticsLogCurrentModuleOrganization
+ _objc_msgSend$_analyticsLogExpandedModuleWithIdentifier:
+ _objc_msgSend$_beginSessionForAnalytics
+ _objc_msgSend$_endSessionForAnalytics
+ _objc_msgSend$_moduleIdentifierForModule:
+ _objc_msgSend$addObserver:selector:name:object:
+ _objc_msgSend$addProvider:
+ _objc_msgSend$allProviders
+ _objc_msgSend$analyticsLogEnabledModuleOrdered
+ _objc_msgSend$currentSessionIdentifier
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$initWithEventsControllerDomain:
+ _objc_msgSend$moduleCollectionViewController:didExpandModuleWithIdentifier:
+ _objc_msgSend$now
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$removeProvider:
+ _objc_msgSend$sessionBeginTime
+ _objc_msgSend$setCurrentSessionIdentifier:
+ _objc_msgSend$setSessionBeginTime:
+ _objc_msgSend$setShouldSendModuleOrganizationToAnalytics:
+ _objc_msgSend$shouldSendModuleOrganizationToAnalytics
+ _objc_msgSend$significantTimeChanged
+ _objc_msgSend$timeIntervalSinceNow
+ _objc_msgSend$weakObjectsHashTable
- GCC_except_table120
- GCC_except_table154
- ___60-[CCUIModuleInstanceManager _instantiateModuleWithMetadata:]_block_invoke.72
- ___71-[CCUIAnimationRunner additivelyRunAnimationBatch:withCompletionBlock:]_block_invoke.80
- ___87-[CCUIModularControlCenterOverlayViewController dismissAnimated:withCompletionHandler:]_block_invoke.41
- ___87-[CCUIModularControlCenterOverlayViewController dismissAnimated:withCompletionHandler:]_block_invoke.44
- ___block_literal_global.68
CStrings:
+ "\b\x1b\"5"
+ "%lu"
+ "@\"CCUIAnalyticsEventsController\""
+ "@\"NSDate\""
+ "@\"NSDictionary\"8@?0"
+ "CCUIAnalyticsDomainControlCenter"
+ "CCUIAnalyticsEventsController"
+ "CCUIAnalyticsProviding"
+ "T@\"<CCUIOverlayFlickGestureBehavior>\",?,R,C,N"
+ "T@\"CCUIAnalyticsEventsController\",&,N,V_analyticsEventsController"
+ "T@\"NSArray\",?,R,D,N"
+ "T@\"NSArray\",?,R,N"
+ "T@\"NSDate\",N,V_sessionBeginTime"
+ "T@\"NSHashTable\",&,N,V_allProviders"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,N,V_eventsControllerDomain"
+ "T@\"NSUUID\",&,N,V_currentSessionIdentifier"
+ "T@\"UITargetedPreview\",?,C,N"
+ "T@\"UIViewController<CCUIContentModuleBackgroundViewController>\",?,R,N"
+ "T@\"UIViewController<CCUIContentModuleContentViewController>\",?,R,N"
+ "T@\"UIViewPropertyAnimator\",?,R,N"
+ "TB,N,V_shouldSendModuleOrganizationToAnalytics"
+ "TQ,?,R,N"
+ "UUIDString"
+ "_allProviders"
+ "_analyticsEventsController"
+ "_analyticsLogCurrentModuleOrganization"
+ "_analyticsLogExpandedModuleWithIdentifier:"
+ "_beginSessionForAnalytics"
+ "_currentSessionIdentifier"
+ "_endSessionForAnalytics"
+ "_eventsControllerDomain"
+ "_moduleIdentifierForModule:"
+ "_sessionBeginTime"
+ "_shouldSendModuleOrganizationToAnalytics"
+ "activeDuration"
+ "addObserver:selector:name:object:"
+ "addProvider:"
+ "allProviders"
+ "analyticsEventsController"
+ "analyticsLogEnabledModuleOrdered"
+ "com.apple.springboardhome.controlcenter.invocation"
+ "com.apple.springboardhome.controlcenter.moduleexpansion"
+ "com.apple.springboardhome.controlcenter.moduleorganization"
+ "currentSessionIdentifier"
+ "dealloc"
+ "defaultCenter"
+ "eventsControllerDomain"
+ "initWithEventsControllerDomain:"
+ "moduleCollectionViewController:didExpandModuleWithIdentifier:"
+ "moduleRanking"
+ "now"
+ "removeProvider:"
+ "sendEventsForProvidersWhenSignificantTimeChanged"
+ "sessionBeginTime"
+ "sessionID"
+ "setAllProviders:"
+ "setAnalyticsEventsController:"
+ "setCurrentSessionIdentifier:"
+ "setSessionBeginTime:"
+ "setShouldSendModuleOrganizationToAnalytics:"
+ "shouldSendModuleOrganizationToAnalytics"
+ "significantTimeChanged"
+ "timeIntervalSinceNow"
+ "v32@0:8@\"CCUIModuleCollectionViewController\"16@\"NSString\"24"
+ "weakObjectsHashTable"
- "\b\x1b\"3"
- "T@\"<CCUIOverlayFlickGestureBehavior>\",R,C,N"
- "T@\"NSArray\",R,N"
- "T@\"UITargetedPreview\",C,N"
- "T@\"UIViewController<CCUIContentModuleBackgroundViewController>\",R,N"
- "T@\"UIViewController<CCUIContentModuleContentViewController>\",R,N"
- "T@\"UIViewPropertyAnimator\",R,N"

```
