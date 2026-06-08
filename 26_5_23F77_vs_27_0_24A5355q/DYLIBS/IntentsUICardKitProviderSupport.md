## IntentsUICardKitProviderSupport

> `/System/Library/PrivateFrameworks/IntentsUICardKitProviderSupport.framework/IntentsUICardKitProviderSupport`

```diff

 3520.8.1.0.0
-  __TEXT.__text: 0x3fc4
-  __TEXT.__auth_stubs: 0x310
+  __TEXT.__text: 0x3c50
   __TEXT.__objc_methlist: 0x904
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__cstring: 0x14b
+  __TEXT.__gcc_except_tab: 0x58
+  __TEXT.__cstring: 0x15c
   __TEXT.__oslogstring: 0x46b
-  __TEXT.__unwind_info: 0x1d8
-  __TEXT.__objc_classname: 0x34f
-  __TEXT.__objc_methname: 0x17c4
-  __TEXT.__objc_methtype: 0x8f8
-  __TEXT.__objc_stubs: 0xf00
-  __DATA_CONST.__got: 0xd0
+  __TEXT.__unwind_info: 0x1b8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x208
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x30

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x198
+  __DATA_CONST.__got: 0xd0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x2598
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x58
   __DATA.__data: 0x6c0

   - /System/Library/PrivateFrameworks/TemplateKit.framework/TemplateKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4581F9A1-6B80-31C2-ACA6-ED2925F0EB6B
+  UUID: 0CB5CA07-0524-3CE3-ABE1-C67B2D53C02D
   Functions: 112
-  Symbols:   691
-  CStrings:  363
+  Symbols:   699
+  CStrings:  27
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x9
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
Functions:
~ +[INUICKPSynchronousRemoteViewController requestInstanceWithInfo:configuration:synchronousRemoteViewControllerDelegate:reply:] : 264 -> 288
~ ___126+[INUICKPSynchronousRemoteViewController requestInstanceWithInfo:configuration:synchronousRemoteViewControllerDelegate:reply:]_block_invoke : 272 -> 276
~ ___126+[INUICKPSynchronousRemoteViewController requestInstanceWithInfo:configuration:synchronousRemoteViewControllerDelegate:reply:]_block_invoke_2 : 308 -> 300
~ ___126+[INUICKPSynchronousRemoteViewController requestInstanceWithInfo:configuration:synchronousRemoteViewControllerDelegate:reply:]_block_invoke_4 : 112 -> 116
~ -[INUICKPSynchronousRemoteViewController setRemoteViewController:] : 260 -> 240
~ -[INUICKPSynchronousRemoteViewController cachedRepresentedParameters] : 112 -> 100
~ -[INUICKPSynchronousRemoteViewController _interaction] : 112 -> 100
~ -[INUICKPSynchronousRemoteViewController _minimumSizesBySystemVersion] : 288 -> 272
~ -[INUICKPSynchronousRemoteViewController maximumSizesBySystemVersionForRemoteViewController:] : 328 -> 308
~ -[INUICKPSynchronousRemoteViewController interfaceSectionsForRemoteViewController:] : 84 -> 76
~ -[INUICKPSynchronousRemoteViewController preferredContentSize] : 128 -> 120
~ -[INUICKPSynchronousRemoteViewController remoteViewController] : 16 -> 20
~ +[INUICKPInterfaceSectionConverter generateInterfaceSectionsFromCard:] : 500 -> 492
~ +[INUICKPInterfaceSectionConverter _interactionMatchingCardSection:inCard:] : 88 -> 80
~ +[INUICKPInterfaceSectionConverter _intrinsicInteractiveBehaviorForCardSection:] : 516 -> 500
~ -[INUICKPSynchronousRemoteView sizeThatFits:] : 84 -> 80
~ -[INUICKPCardSectionViewProvider providerIdentifier] : 64 -> 16
~ -[INUICKPCardSectionViewProvider vetoDisplayOfCardSection:] : 212 -> 208
~ ___59-[INUICKPCardSectionViewProvider vetoDisplayOfCardSection:]_block_invoke : 192 -> 180
~ +[INUICKPCardSectionViewProvider requestInstanceFromDefaultAllocatorWithCard:delegate:reply:] : 180 -> 188
~ +[INUICKPCardSectionViewProvider requestInstanceWithCard:delegate:allocator:reply:] : 720 -> 684
~ ___83+[INUICKPCardSectionViewProvider requestInstanceWithCard:delegate:allocator:reply:]_block_invoke : 152 -> 148
~ -[INUICKPCardSectionViewProvider boundingWidthForViewControllerAllocator:] : 136 -> 128
~ +[INUICKPCardSectionViewProvider _viewConfigurationsFromAllocator:] : 640 -> 620
~ -[INUICKPCardSectionViewProvider setAllocator:] : 64 -> 12
~ -[INUICKPExtensionCardSectionViewController desiresInteractivity:] : 100 -> 96
~ -[INUICKPExtensionCardSectionViewController remoteViewController:requestsHandlingOfIntent:] : 112 -> 108
~ -[INUICKPExtensionCardSectionViewController remoteViewControllerWillBeginEditing:] : 112 -> 108
~ -[INUICKPExtensionCardSectionViewController cardEventDidOccur:withIdentifier:userInfo:] : 700 -> 600
~ -[INUICKPEntryPoint providerIdentifier] : 64 -> 16
~ -[INParameter(CardKit) isSubParameterOf:] : 584 -> 556
~ -[INUICKPCardInterfaceSection isEqual:] : 276 -> 264
~ -[INUICKPCardInterfaceSection hash] : 92 -> 96
~ -[INUICKPCardInterfaceSection isWildCardSection] : 112 -> 104
~ -[INUICKPCardInterfaceSection parameters] : 16 -> 20
~ -[INUICKPCardInterfaceSection cardSection] : 16 -> 20
~ -[INUICKPCardInterfaceSection setCardSection:] : 80 -> 20
~ -[INUICKPSynchronousRemoteViewControllerAllocator performAllocationsFromInteraction:initialInterfaceSections:completion:] : 264 -> 276
~ -[INUICKPSynchronousRemoteViewControllerAllocator _recursivelyConnectForInterfaceSectionQueue:recursionDepth:completion:] : 1128 -> 1056
~ ___121-[INUICKPSynchronousRemoteViewControllerAllocator _recursivelyConnectForInterfaceSectionQueue:recursionDepth:completion:]_block_invoke_2 : 396 -> 384
~ ___121-[INUICKPSynchronousRemoteViewControllerAllocator _recursivelyConnectForInterfaceSectionQueue:recursionDepth:completion:]_block_invoke_3 : 580 -> 520
~ -[INUICKPSynchronousRemoteViewControllerAllocator _unhandledParametersForInterfaceSection:] : 528 -> 524
~ -[INUICKPSynchronousRemoteViewControllerAllocator boundingWidthForSynchronousRemoteViewController:] : 76 -> 72
~ -[INUICKPSynchronousRemoteViewControllerAllocator setInteraction:] : 64 -> 12
~ __INUICKPInteractionMatchingCardSectionInCard : 88 -> 80
~ __INUICKPIntrinsicInteractiveBehaviorForCardSection : 516 -> 500
~ _INUICKPInterfaceSectionsFromCard : 576 -> 568
~ +[NSObject(IntentsUICardKitProvider) inuickp_interactiveBehaviorPrecedenceOrder] : 84 -> 68
~ -[NSObject(IntentsUICardKitProvider) inuickp_intrinsicInteractiveBehavior] : 528 -> 516
~ -[INUICKPSynchronousRemoteViewController remoteViewControllerServiceDidTerminate:].cold.1 : 216 -> 164
~ ___121-[INUICKPSynchronousRemoteViewControllerAllocator _recursivelyConnectForInterfaceSectionQueue:recursionDepth:completion:]_block_invoke_3.cold.1 : 140 -> 96
CStrings:
- "#"
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"<CRCard>\""
- "@\"<CRCard>\"16@0:8"
- "@\"<CRCardSection>\""
- "@\"<CRKCardSectionViewControllingDelegate>\""
- "@\"<CRKCardSectionViewControllingDelegate>\"16@0:8"
- "@\"<CRKCardSectionViewProviderDelegate>\""
- "@\"<INUICKPInterfaceSectionOrganizing>\""
- "@\"<INUICKPSynchronousRemoteViewControllerDelegate>\""
- "@\"<INUICKPSynchronousRemoteViewDelegate>\""
- "@\"<INUICKPViewControllerAllocating>\""
- "@\"<INUICKPViewControllerAllocatingDelegate>\""
- "@\"<INUICKPViewControllerAllocatingDelegate>\"16@0:8"
- "@\"<SFCardSection>\"16@0:8"
- "@\"INInteraction\""
- "@\"INUIRemoteViewController\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSArray\"24@0:8@\"INUIRemoteViewController\"16"
- "@\"NSDictionary\"16@0:8"
- "@\"NSDictionary\"24@0:8@\"INUIRemoteViewController\"16"
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSSet\""
- "@\"NSSet\"16@0:8"
- "@\"NSSet\"24@0:8@\"INInteraction\"16"
- "@\"NSString\"16@0:8"
- "@\"UIViewController<CRKCardViewControlling>\"24@0:8@\"<CRCard>\"16"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8Q16@24"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"<CRCardSection>\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CRCardSection"
- "CRKCardSectionViewControlling"
- "CRKCardSectionViewProviding"
- "CRKCardViewControllerProviding"
- "CRKEventResponding"
- "CRKIdentifiedCardSectionViewProviding"
- "CRKIdentifiedProviding"
- "CRKProviderIdentifying"
- "CRKProviding"
- "CardKit"
- "CommandPlusIntentsUICardKitProvider"
- "INUICKPCardInterfaceSection"
- "INUICKPCardSectionViewProvider"
- "INUICKPEntryPoint"
- "INUICKPExtensionCardSectionViewController"
- "INUICKPInterfaceSectionConverter"
- "INUICKPInterfaceSectionModeling"
- "INUICKPInterfaceSectionOrganizing"
- "INUICKPSynchronousRemoteView"
- "INUICKPSynchronousRemoteViewController"
- "INUICKPSynchronousRemoteViewControllerAllocator"
- "INUICKPSynchronousRemoteViewControllerDelegate"
- "INUICKPSynchronousRemoteViewDelegate"
- "INUICKPViewControllerAllocating"
- "INUICKPViewControllerAllocatingDelegate"
- "INUIRemoteViewControllerDelegate"
- "IntentsUICardKitProvider"
- "NSCopying"
- "NSObject"
- "Q16@0:8"
- "Q24@0:8@\"<CRCard>\"16"
- "Q24@0:8@\"<CRCardSection>\"16"
- "Q24@0:8@16"
- "T#,R"
- "T@\"<CRCard>\",R,N"
- "T@\"<CRCard>\",R,N,V_card"
- "T@\"<CRCardSection>\",&,N,V_cardSection"
- "T@\"<CRKCardSectionViewControllingDelegate>\",W,N"
- "T@\"<CRKCardSectionViewControllingDelegate>\",W,N,V_cardSectionViewControllingDelegate"
- "T@\"<CRKCardSectionViewControllingDelegate>\",W,N,VcardSectionViewControllingDelegate"
- "T@\"<CRKCardSectionViewProviderDelegate>\",W,N,V_cardSectionViewProviderDelegate"
- "T@\"<INUICKPInterfaceSectionOrganizing>\",W,N,V_interfaceSectionOrganizer"
- "T@\"<INUICKPSynchronousRemoteViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<INUICKPSynchronousRemoteViewDelegate>\",W,N,V_delegate"
- "T@\"<INUICKPViewControllerAllocating>\",&,N,V_allocator"
- "T@\"<INUICKPViewControllerAllocatingDelegate>\",?,W,N"
- "T@\"<INUICKPViewControllerAllocatingDelegate>\",?,W,N,Vdelegate"
- "T@\"<SFCardSection>\",?,R,N"
- "T@\"INInteraction\",&,N,V_interaction"
- "T@\"INUIRemoteViewController\",&,N,V_remoteViewController"
- "T@\"NSArray\",?,R,N"
- "T@\"NSArray\",C,N,V_viewConfigurations"
- "T@\"NSArray\",R,C,N"
- "T@\"NSArray\",R,N"
- "T@\"NSDictionary\",R,C,N"
- "T@\"NSMutableArray\",R,N,V_finalInterfaceSections"
- "T@\"NSMutableArray\",R,N,V_mutableRedundantInterfaceSections"
- "T@\"NSMutableArray\",R,N,V_mutableSynchronousRemoteViewControllers"
- "T@\"NSMutableDictionary\",R,N,V_mutableSynchronousRemoteViewControllersByInitialInterfaceSection"
- "T@\"NSMutableSet\",R,N,V_handledParameters"
- "T@\"NSSet\",C,N"
- "T@\"NSSet\",C,N,V_cardSectionParameters"
- "T@\"NSSet\",R,C,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,N"
- "TB,?,R,N"
- "TB,N"
- "TB,N,V_requiresUserConsent"
- "TB,R,N"
- "TQ,R"
- "TQ,R,N"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_allocator"
- "_beginRecursivelyConnectingForInterfaceSectionQueue:completion:"
- "_canShowWhileLocked"
- "_cancelTouchesForCurrentEventInHostedContent"
- "_card"
- "_cardSection"
- "_cardSectionParameters"
- "_cardSectionViewControllingDelegate"
- "_cardSectionViewProviderDelegate"
- "_delegate"
- "_finalInterfaceSections"
- "_handledParameters"
- "_indexesForSubKeyPaths"
- "_interaction"
- "_interactionMatchingCardSection:inCard:"
- "_interfaceSectionOrganizer"
- "_intrinsicInteractiveBehaviorForCardSection:"
- "_minimumSizesBySystemVersion"
- "_mutableRedundantInterfaceSections"
- "_mutableSynchronousRemoteViewControllers"
- "_mutableSynchronousRemoteViewControllersByInitialInterfaceSection"
- "_recursivelyConnectForInterfaceSectionQueue:recursionDepth:completion:"
- "_remoteViewController"
- "_requiresUserConsent"
- "_synchronousRemoteViewControllerClass"
- "_touchDeliveryPolicyAssertion"
- "_unhandledParametersForInterfaceSection:"
- "_viewConfigurations"
- "_viewConfigurationsFromAllocator:"
- "actionCommands"
- "addChildViewController:"
- "addObject:"
- "addSubview:"
- "allKeys"
- "allKeysForObject:"
- "allocatedViewControllers"
- "allocator"
- "anyObject"
- "autorelease"
- "backingCardSection"
- "boundingWidthForProvider:"
- "boundingWidthForSynchronousRemoteViewController:"
- "boundingWidthForViewControllerAllocator:"
- "bounds"
- "cachedRepresentedParameters"
- "cachedSizeForSynchronousRemoteView:"
- "card"
- "cardEventDidOccur:withIdentifier:userInfo:"
- "cardSection"
- "cardSectionDisplayRequiresUserConsentForProvider:"
- "cardSectionIdentifier"
- "cardSectionViewControllingDelegate"
- "cardSectionViewProviderDelegate"
- "cardSections"
- "cardViewControllerForCard:"
- "class"
- "configuration"
- "conformsToProtocol:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d24@0:8@\"<INUICKPViewControllerAllocating>\"16"
- "d24@0:8@\"INUICKPSynchronousRemoteViewController\"16"
- "d24@0:8@16"
- "debugDescription"
- "delegate"
- "description"
- "desiresInteractivity:"
- "dictionaryWithObjects:forKeys:count:"
- "didMoveToParentViewController:"
- "disconnect"
- "displayPriorityForCard:"
- "displayPriorityForCardSection:"
- "finalInterfaceSections"
- "firstObject"
- "generateInterfaceSectionsFromCard:"
- "handledParameters"
- "hasNextCard"
- "hasPrefix:"
- "hash"
- "indexOfObject:"
- "indexOfObjectPassingTest:"
- "init"
- "initWithInteraction:"
- "initWithInteractiveBehavior:parameters:"
- "initWithParameters:interactiveBehavior:hostedViewContext:"
- "interaction"
- "interactions"
- "interactiveBehavior"
- "interfaceSectionOrganizer"
- "interfaceSectionsForRemoteViewController:"
- "inuickp_interactiveBehaviorPrecedenceOrder"
- "inuickp_intrinsicInteractiveBehavior"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSubParameterOf:"
- "isSubclassOfClass:"
- "isWildCardSection"
- "layoutSubviews"
- "length"
- "loadView"
- "mainScreen"
- "maximumSizesBySystemVersionForRemoteViewController:"
- "minimumSizesBySystemVersionForRemoteViewController:"
- "mutableCopy"
- "mutableRedundantInterfaceSections"
- "mutableSynchronousRemoteViewControllers"
- "mutableSynchronousRemoteViewControllersByInitialInterfaceSection"
- "numberWithBool:"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "organizedInterfaceSections"
- "parameterClass"
- "parameterKeyPath"
- "parameters"
- "parametersForInteraction:"
- "performAllocationsFromInteraction:initialInterfaceSections:completion:"
- "performCommand:forViewController:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "preferredContentSize"
- "presentation:didApplyCardSectionViewSource:toCardViewController:"
- "providerIdentifier"
- "redundantInterfaceSections"
- "release"
- "remoteViewController"
- "remoteViewController:requestsHandlingOfIntent:"
- "remoteViewControllerServiceDidTerminate:"
- "remoteViewControllerWillBeginEditing:"
- "removeAllObjects"
- "removeFromParentViewController"
- "removeFromSuperview"
- "removeObject:"
- "requestCancellation"
- "requestCardSectionViewProviderForCard:delegate:reply:"
- "requestIdentifiedCardSectionViewProviderForCard:delegate:reply:"
- "requestInfo"
- "requestInstanceFromDefaultAllocatorWithCard:delegate:reply:"
- "requestInstanceWithCard:delegate:allocator:reply:"
- "requestInstanceWithInfo:configuration:synchronousRemoteViewControllerDelegate:reply:"
- "requestRemoteViewControllerWithRequestInfo:reply:"
- "requiresUserConsent"
- "resolvedCardSections"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "set"
- "setAllocator:"
- "setCardSection:"
- "setCardSectionView:"
- "setCardSectionViewController:"
- "setCardSectionViewControllingDelegate:"
- "setCardSectionViewProviderDelegate:"
- "setDelegate:"
- "setDelegate:completion:"
- "setFrame:"
- "setIdealConfiguration:animated:completion:"
- "setInheritsSecurity:"
- "setInteraction:"
- "setInterfaceSectionOrganizer:"
- "setObject:forKey:"
- "setParameters:"
- "setRemoteViewController:"
- "setRequiresUserConsent:"
- "setServiceViewShouldShareTouchesWithHost:"
- "setSynchronousRemoteViewControllerClass:"
- "setView:"
- "setViewConfigurations:"
- "sizeThatFits:"
- "subviews"
- "superclass"
- "unionSet:"
- "unregisterCardViewController:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8#16"
- "v24@0:8@\"<CRKCardSectionViewControllingDelegate>\"16"
- "v24@0:8@\"<INUICKPViewControllerAllocatingDelegate>\"16"
- "v24@0:8@\"INUIRemoteViewController\"16"
- "v24@0:8@\"NSSet\"16"
- "v24@0:8@\"UIViewController<CRKCardViewControlling>\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B>16"
- "v32@0:8@\"INUIRemoteViewController\"16@\"INIntent\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@\"<CRCard>\"16@\"<CRKCardSectionViewProviderDelegate>\"24@?<v@?@\"NSError\"@\"<CRKCardSectionViewProviding>\">32"
- "v40@0:8@\"<CRCard>\"16@\"<CRKCardSectionViewProviderDelegate>\"24@?<v@?@\"NSError\"@\"<CRKIdentifiedCardSectionViewProviding>\">32"
- "v40@0:8@\"<CRKCardPresenting>\"16@\"<CRKCardSectionViewSourcing>\"24@\"UIViewController<CRKCardViewControlling>\"32"
- "v40@0:8@\"INInteraction\"16@\"NSArray\"24@?<v@?@\"NSError\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@?32"
- "v40@0:8Q16@\"NSString\"24@\"NSDictionary\"32"
- "v40@0:8Q16@24@32"
- "v48@0:8@16@24@32@?40"
- "valueWithCGSize:"
- "vetoDisplayOfCardSection:"
- "view"
- "viewConfigurations"
- "viewControllersByInitialInterfaceSection"
- "zone"
- "{CGSize=dd}16@0:8"
- "{CGSize=dd}24@0:8@\"INUICKPSynchronousRemoteView\"16"
- "{CGSize=dd}24@0:8@16"
- "{CGSize=dd}32@0:8{CGSize=dd}16"

```
