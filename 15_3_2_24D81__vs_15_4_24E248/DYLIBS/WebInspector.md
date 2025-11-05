## WebInspector

> `/System/Library/PrivateFrameworks/WebInspector.framework/Versions/A/WebInspector`

```diff

-7620.2.4.11.6
-  __TEXT.__text: 0x9234c
-  __TEXT.__auth_stubs: 0xb70
-  __TEXT.__objc_methlist: 0x5da4
+7621.1.15.11.10
+  __TEXT.__text: 0x8b8b8
+  __TEXT.__auth_stubs: 0xb80
+  __TEXT.__objc_methlist: 0x6760
   __TEXT.__const: 0x180
-  __TEXT.__cstring: 0x57f3
-  __TEXT.__oslogstring: 0x4849
-  __TEXT.__gcc_except_tab: 0xc47c
+  __TEXT.__cstring: 0x594e
+  __TEXT.__oslogstring: 0x4900
+  __TEXT.__gcc_except_tab: 0xc424
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x3d90
+  __TEXT.__unwind_info: 0x3e90
   __TEXT.__objc_classname: 0x1092
-  __TEXT.__objc_methname: 0xc38e
+  __TEXT.__objc_methname: 0xc45f
   __TEXT.__objc_methtype: 0x2024
-  __TEXT.__objc_stubs: 0x71c0
+  __TEXT.__objc_stubs: 0x7240
   __DATA_CONST.__got: 0x4a0
   __DATA_CONST.__const: 0x1d28
   __DATA_CONST.__objc_classlist: 0x438
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3268
+  __DATA_CONST.__objc_selrefs: 0x34d0
   __DATA_CONST.__objc_superrefs: 0x420
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__auth_got: 0x5d0
-  __AUTH_CONST.__const: 0x1058
-  __AUTH_CONST.__cfstring: 0x52c0
-  __AUTH_CONST.__objc_const: 0xb700
+  __AUTH_CONST.__auth_got: 0x5d8
+  __AUTH_CONST.__const: 0x1088
+  __AUTH_CONST.__cfstring: 0x5300
+  __AUTH_CONST.__objc_const: 0xa580
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x2a30
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x3d4
+  __DATA.__objc_ivar: 0x3d8
   __DATA.__data: 0x6d8
-  __DATA.__bss: 0x2e8
+  __DATA.__bss: 0x230
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Cocoa.framework/Versions/A/Cocoa
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxcselect.dylib
-  UUID: 27A6DE75-D670-34BE-8DEF-3B9809D3BE3E
-  Functions: 2757
-  Symbols:   7142
-  CStrings:  4581
+  UUID: 4052C5AD-555F-3699-8E64-50F8EB0D858B
+  Functions: 2832
+  Symbols:   7993
+  CStrings:  4600
 
Symbols:
+ +[RWIManager sharedManager].cold.3
+ +[RWISoftLinkingUtilities developerPath].cold.1
+ +[RWISoftLinkingUtilities simulatorAppURL].cold.1
+ +[RWISoftLinkingUtilities xcodeAppPath].cold.1
+ -[RWIDevice _copyRemoteInspectionEnabledValueFromDevice:]
+ -[RWIDevice _copyWirelessEnabledValueFromDevice:]
+ -[RWIDriver bidiPort]
+ -[RWIDriverConfiguration driverBidiPort]
+ -[RWIDriverConfiguration setDriverBidiPort:]
+ -[RWIProtocolCSSDomainEventDispatcher mediaQueryResultChanged].cold.1
+ -[RWIProtocolCSSDomainEventDispatcher mediaQueryResultChanged].cold.2
+ -[RWIProtocolCSSDomainEventDispatcher mediaQueryResultChanged].cold.3
+ -[RWIProtocolCSSDomainEventDispatcher nodeLayoutFlagsChangedWithNodeId:layoutFlags:].cold.3
+ -[RWIProtocolCSSDomainEventDispatcher nodeLayoutFlagsChangedWithNodeId:layoutFlags:].cold.4
+ -[RWIProtocolCSSDomainEventDispatcher nodeLayoutFlagsChangedWithNodeId:layoutFlags:].cold.5
+ -[RWIProtocolCSSDomainEventDispatcher nodeLayoutFlagsChangedWithNodeId:layoutFlags:].cold.6
+ -[RWIProtocolCSSDomainEventDispatcher nodeLayoutFlagsChangedWithNodeId:layoutFlags:].cold.7
+ -[RWIProtocolCSSDomainEventDispatcher nodeLayoutFlagsChangedWithNodeId:layoutFlags:].cold.8
+ -[RWIProtocolCSSDomainEventDispatcher styleSheetAddedWithHeader:].cold.3
+ -[RWIProtocolCSSDomainEventDispatcher styleSheetAddedWithHeader:].cold.4
+ -[RWIProtocolCSSDomainEventDispatcher styleSheetAddedWithHeader:].cold.5
+ -[RWIProtocolCSSDomainEventDispatcher styleSheetAddedWithHeader:].cold.6
+ -[RWIProtocolCSSDomainEventDispatcher styleSheetAddedWithHeader:].cold.7
+ -[RWIProtocolCSSDomainEventDispatcher styleSheetChangedWithStyleSheetId:].cold.2
+ -[RWIProtocolCSSDomainEventDispatcher styleSheetChangedWithStyleSheetId:].cold.3
+ -[RWIProtocolCSSDomainEventDispatcher styleSheetChangedWithStyleSheetId:].cold.4
+ -[RWIProtocolCSSDomainEventDispatcher styleSheetChangedWithStyleSheetId:].cold.5
+ -[RWIProtocolCSSDomainEventDispatcher styleSheetChangedWithStyleSheetId:].cold.6
+ -[RWIProtocolCSSDomainEventDispatcher styleSheetRemovedWithStyleSheetId:].cold.2
+ -[RWIProtocolCSSDomainEventDispatcher styleSheetRemovedWithStyleSheetId:].cold.3
+ -[RWIProtocolCSSDomainEventDispatcher styleSheetRemovedWithStyleSheetId:].cold.4
+ -[RWIProtocolCSSDomainEventDispatcher styleSheetRemovedWithStyleSheetId:].cold.5
+ -[RWIProtocolCSSDomainEventDispatcher styleSheetRemovedWithStyleSheetId:].cold.6
+ -[RWIProtocolCSSFont variationAxes].cold.2
+ -[RWIProtocolCSSGrouping setType:].cold.1
+ -[RWIProtocolCSSInheritedStyleEntry matchedCSSRules].cold.2
+ -[RWIProtocolCSSProperty setStatus:].cold.1
+ -[RWIProtocolCSSPropertyInfo aliases].cold.2
+ -[RWIProtocolCSSPropertyInfo longhands].cold.2
+ -[RWIProtocolCSSPropertyInfo values].cold.2
+ -[RWIProtocolCSSPseudoIdMatches matches].cold.2
+ -[RWIProtocolCSSPseudoIdMatches pseudoId].cold.2
+ -[RWIProtocolCSSPseudoIdMatches setPseudoId:].cold.1
+ -[RWIProtocolCSSRule groupings].cold.2
+ -[RWIProtocolCSSRule setOrigin:].cold.1
+ -[RWIProtocolCSSRuleMatch matchingSelectors].cold.2
+ -[RWIProtocolCSSSelector specificity].cold.2
+ -[RWIProtocolCSSSelectorList selectors].cold.2
+ -[RWIProtocolCSSStyle cssProperties].cold.2
+ -[RWIProtocolCSSStyle shorthandEntries].cold.2
+ -[RWIProtocolCSSStyleSheetBody rules].cold.2
+ -[RWIProtocolCSSStyleSheetHeader setOrigin:].cold.1
+ -[RWIProtocolConsoleChannel setLevel:].cold.1
+ -[RWIProtocolConsoleChannel setSource:].cold.1
+ -[RWIProtocolConsoleDomainEventDispatcher heapSnapshotWithTimestamp:snapshotData:title:].cold.2
+ -[RWIProtocolConsoleDomainEventDispatcher heapSnapshotWithTimestamp:snapshotData:title:].cold.3
+ -[RWIProtocolConsoleDomainEventDispatcher heapSnapshotWithTimestamp:snapshotData:title:].cold.4
+ -[RWIProtocolConsoleDomainEventDispatcher heapSnapshotWithTimestamp:snapshotData:title:].cold.5
+ -[RWIProtocolConsoleDomainEventDispatcher heapSnapshotWithTimestamp:snapshotData:title:].cold.6
+ -[RWIProtocolConsoleDomainEventDispatcher heapSnapshotWithTimestamp:snapshotData:title:].cold.7
+ -[RWIProtocolConsoleDomainEventDispatcher heapSnapshotWithTimestamp:snapshotData:title:].cold.8
+ -[RWIProtocolConsoleDomainEventDispatcher messageAddedWithMessage:].cold.3
+ -[RWIProtocolConsoleDomainEventDispatcher messageAddedWithMessage:].cold.4
+ -[RWIProtocolConsoleDomainEventDispatcher messageAddedWithMessage:].cold.5
+ -[RWIProtocolConsoleDomainEventDispatcher messageAddedWithMessage:].cold.6
+ -[RWIProtocolConsoleDomainEventDispatcher messageAddedWithMessage:].cold.7
+ -[RWIProtocolConsoleDomainEventDispatcher messageRepeatCountUpdatedWithCount:timestamp:].cold.2
+ -[RWIProtocolConsoleDomainEventDispatcher messageRepeatCountUpdatedWithCount:timestamp:].cold.3
+ -[RWIProtocolConsoleDomainEventDispatcher messageRepeatCountUpdatedWithCount:timestamp:].cold.4
+ -[RWIProtocolConsoleDomainEventDispatcher messageRepeatCountUpdatedWithCount:timestamp:].cold.5
+ -[RWIProtocolConsoleDomainEventDispatcher messageRepeatCountUpdatedWithCount:timestamp:].cold.6
+ -[RWIProtocolConsoleDomainEventDispatcher messageRepeatCountUpdatedWithCount:timestamp:].cold.7
+ -[RWIProtocolConsoleDomainEventDispatcher messagesClearedWithReason:].cold.2
+ -[RWIProtocolConsoleDomainEventDispatcher messagesClearedWithReason:].cold.3
+ -[RWIProtocolConsoleDomainEventDispatcher messagesClearedWithReason:].cold.4
+ -[RWIProtocolConsoleDomainEventDispatcher messagesClearedWithReason:].cold.5
+ -[RWIProtocolConsoleDomainEventDispatcher messagesClearedWithReason:].cold.6
+ -[RWIProtocolConsoleMessage parameters].cold.2
+ -[RWIProtocolConsoleMessage setLevel:].cold.1
+ -[RWIProtocolConsoleMessage setSource:].cold.1
+ -[RWIProtocolConsoleMessage setType:].cold.1
+ -[RWIProtocolConsoleStackTrace callFrames].cold.2
+ -[RWIProtocolDOMAccessibilityProperties childNodeIds].cold.2
+ -[RWIProtocolDOMAccessibilityProperties controlledNodeIds].cold.2
+ -[RWIProtocolDOMAccessibilityProperties flowedNodeIds].cold.2
+ -[RWIProtocolDOMAccessibilityProperties liveRegionRelevant].cold.2
+ -[RWIProtocolDOMAccessibilityProperties ownedNodeIds].cold.2
+ -[RWIProtocolDOMAccessibilityProperties selectedChildNodeIds].cold.2
+ -[RWIProtocolDOMAccessibilityProperties setChecked:].cold.1
+ -[RWIProtocolDOMAccessibilityProperties setCurrent:].cold.1
+ -[RWIProtocolDOMAccessibilityProperties setInvalid:].cold.1
+ -[RWIProtocolDOMAccessibilityProperties setLiveRegionStatus:].cold.1
+ -[RWIProtocolDOMDomainEventDispatcher attributeModifiedWithNodeId:name:value:].cold.2
+ -[RWIProtocolDOMDomainEventDispatcher attributeModifiedWithNodeId:name:value:].cold.3
+ -[RWIProtocolDOMDomainEventDispatcher attributeModifiedWithNodeId:name:value:].cold.4
+ -[RWIProtocolDOMDomainEventDispatcher attributeModifiedWithNodeId:name:value:].cold.5
+ -[RWIProtocolDOMDomainEventDispatcher attributeModifiedWithNodeId:name:value:].cold.6
+ -[RWIProtocolDOMDomainEventDispatcher attributeModifiedWithNodeId:name:value:].cold.7
+ -[RWIProtocolDOMDomainEventDispatcher attributeModifiedWithNodeId:name:value:].cold.8
+ -[RWIProtocolDOMDomainEventDispatcher attributeRemovedWithNodeId:name:].cold.2
+ -[RWIProtocolDOMDomainEventDispatcher attributeRemovedWithNodeId:name:].cold.3
+ -[RWIProtocolDOMDomainEventDispatcher attributeRemovedWithNodeId:name:].cold.4
+ -[RWIProtocolDOMDomainEventDispatcher attributeRemovedWithNodeId:name:].cold.5
+ -[RWIProtocolDOMDomainEventDispatcher attributeRemovedWithNodeId:name:].cold.6
+ -[RWIProtocolDOMDomainEventDispatcher attributeRemovedWithNodeId:name:].cold.7
+ -[RWIProtocolDOMDomainEventDispatcher characterDataModifiedWithNodeId:characterData:].cold.2
+ -[RWIProtocolDOMDomainEventDispatcher characterDataModifiedWithNodeId:characterData:].cold.3
+ -[RWIProtocolDOMDomainEventDispatcher characterDataModifiedWithNodeId:characterData:].cold.4
+ -[RWIProtocolDOMDomainEventDispatcher characterDataModifiedWithNodeId:characterData:].cold.5
+ -[RWIProtocolDOMDomainEventDispatcher characterDataModifiedWithNodeId:characterData:].cold.6
+ -[RWIProtocolDOMDomainEventDispatcher characterDataModifiedWithNodeId:characterData:].cold.7
+ -[RWIProtocolDOMDomainEventDispatcher childNodeCountUpdatedWithNodeId:childNodeCount:].cold.2
+ -[RWIProtocolDOMDomainEventDispatcher childNodeCountUpdatedWithNodeId:childNodeCount:].cold.3
+ -[RWIProtocolDOMDomainEventDispatcher childNodeCountUpdatedWithNodeId:childNodeCount:].cold.4
+ -[RWIProtocolDOMDomainEventDispatcher childNodeCountUpdatedWithNodeId:childNodeCount:].cold.5
+ -[RWIProtocolDOMDomainEventDispatcher childNodeCountUpdatedWithNodeId:childNodeCount:].cold.6
+ -[RWIProtocolDOMDomainEventDispatcher childNodeCountUpdatedWithNodeId:childNodeCount:].cold.7
+ -[RWIProtocolDOMDomainEventDispatcher childNodeInsertedWithParentNodeId:previousNodeId:node:].cold.3
+ -[RWIProtocolDOMDomainEventDispatcher childNodeInsertedWithParentNodeId:previousNodeId:node:].cold.4
+ -[RWIProtocolDOMDomainEventDispatcher childNodeInsertedWithParentNodeId:previousNodeId:node:].cold.5
+ -[RWIProtocolDOMDomainEventDispatcher childNodeInsertedWithParentNodeId:previousNodeId:node:].cold.6
+ -[RWIProtocolDOMDomainEventDispatcher childNodeInsertedWithParentNodeId:previousNodeId:node:].cold.7
+ -[RWIProtocolDOMDomainEventDispatcher childNodeInsertedWithParentNodeId:previousNodeId:node:].cold.8
+ -[RWIProtocolDOMDomainEventDispatcher childNodeInsertedWithParentNodeId:previousNodeId:node:].cold.9
+ -[RWIProtocolDOMDomainEventDispatcher childNodeRemovedWithParentNodeId:nodeId:].cold.2
+ -[RWIProtocolDOMDomainEventDispatcher childNodeRemovedWithParentNodeId:nodeId:].cold.3
+ -[RWIProtocolDOMDomainEventDispatcher childNodeRemovedWithParentNodeId:nodeId:].cold.4
+ -[RWIProtocolDOMDomainEventDispatcher childNodeRemovedWithParentNodeId:nodeId:].cold.5
+ -[RWIProtocolDOMDomainEventDispatcher childNodeRemovedWithParentNodeId:nodeId:].cold.6
+ -[RWIProtocolDOMDomainEventDispatcher childNodeRemovedWithParentNodeId:nodeId:].cold.7
+ -[RWIProtocolDOMDomainEventDispatcher customElementStateChangedWithNodeId:customElementState:].cold.2
+ -[RWIProtocolDOMDomainEventDispatcher customElementStateChangedWithNodeId:customElementState:].cold.3
+ -[RWIProtocolDOMDomainEventDispatcher customElementStateChangedWithNodeId:customElementState:].cold.4
+ -[RWIProtocolDOMDomainEventDispatcher customElementStateChangedWithNodeId:customElementState:].cold.5
+ -[RWIProtocolDOMDomainEventDispatcher customElementStateChangedWithNodeId:customElementState:].cold.6
+ -[RWIProtocolDOMDomainEventDispatcher customElementStateChangedWithNodeId:customElementState:].cold.7
+ -[RWIProtocolDOMDomainEventDispatcher didAddEventListenerWithNodeId:].cold.2
+ -[RWIProtocolDOMDomainEventDispatcher didAddEventListenerWithNodeId:].cold.3
+ -[RWIProtocolDOMDomainEventDispatcher didAddEventListenerWithNodeId:].cold.4
+ -[RWIProtocolDOMDomainEventDispatcher didAddEventListenerWithNodeId:].cold.5
+ -[RWIProtocolDOMDomainEventDispatcher didAddEventListenerWithNodeId:].cold.6
+ -[RWIProtocolDOMDomainEventDispatcher didFireEventWithNodeId:eventName:timestamp:data:].cold.10
+ -[RWIProtocolDOMDomainEventDispatcher didFireEventWithNodeId:eventName:timestamp:data:].cold.3
+ -[RWIProtocolDOMDomainEventDispatcher didFireEventWithNodeId:eventName:timestamp:data:].cold.4
+ -[RWIProtocolDOMDomainEventDispatcher didFireEventWithNodeId:eventName:timestamp:data:].cold.5
+ -[RWIProtocolDOMDomainEventDispatcher didFireEventWithNodeId:eventName:timestamp:data:].cold.6
+ -[RWIProtocolDOMDomainEventDispatcher didFireEventWithNodeId:eventName:timestamp:data:].cold.7
+ -[RWIProtocolDOMDomainEventDispatcher didFireEventWithNodeId:eventName:timestamp:data:].cold.8
+ -[RWIProtocolDOMDomainEventDispatcher didFireEventWithNodeId:eventName:timestamp:data:].cold.9
+ -[RWIProtocolDOMDomainEventDispatcher documentUpdated].cold.1
+ -[RWIProtocolDOMDomainEventDispatcher documentUpdated].cold.2
+ -[RWIProtocolDOMDomainEventDispatcher documentUpdated].cold.3
+ -[RWIProtocolDOMDomainEventDispatcher inlineStyleInvalidatedWithNodeIds:].cold.3
+ -[RWIProtocolDOMDomainEventDispatcher inlineStyleInvalidatedWithNodeIds:].cold.4
+ -[RWIProtocolDOMDomainEventDispatcher inlineStyleInvalidatedWithNodeIds:].cold.5
+ -[RWIProtocolDOMDomainEventDispatcher inlineStyleInvalidatedWithNodeIds:].cold.6
+ -[RWIProtocolDOMDomainEventDispatcher inlineStyleInvalidatedWithNodeIds:].cold.7
+ -[RWIProtocolDOMDomainEventDispatcher inspectWithNodeId:].cold.2
+ -[RWIProtocolDOMDomainEventDispatcher inspectWithNodeId:].cold.3
+ -[RWIProtocolDOMDomainEventDispatcher inspectWithNodeId:].cold.4
+ -[RWIProtocolDOMDomainEventDispatcher inspectWithNodeId:].cold.5
+ -[RWIProtocolDOMDomainEventDispatcher inspectWithNodeId:].cold.6
+ -[RWIProtocolDOMDomainEventDispatcher powerEfficientPlaybackStateChangedWithNodeId:timestamp:isPowerEfficient:].cold.2
+ -[RWIProtocolDOMDomainEventDispatcher powerEfficientPlaybackStateChangedWithNodeId:timestamp:isPowerEfficient:].cold.3
+ -[RWIProtocolDOMDomainEventDispatcher powerEfficientPlaybackStateChangedWithNodeId:timestamp:isPowerEfficient:].cold.4
+ -[RWIProtocolDOMDomainEventDispatcher powerEfficientPlaybackStateChangedWithNodeId:timestamp:isPowerEfficient:].cold.5
+ -[RWIProtocolDOMDomainEventDispatcher powerEfficientPlaybackStateChangedWithNodeId:timestamp:isPowerEfficient:].cold.6
+ -[RWIProtocolDOMDomainEventDispatcher powerEfficientPlaybackStateChangedWithNodeId:timestamp:isPowerEfficient:].cold.7
+ -[RWIProtocolDOMDomainEventDispatcher powerEfficientPlaybackStateChangedWithNodeId:timestamp:isPowerEfficient:].cold.8
+ -[RWIProtocolDOMDomainEventDispatcher pseudoElementAddedWithParentId:pseudoElement:].cold.3
+ -[RWIProtocolDOMDomainEventDispatcher pseudoElementAddedWithParentId:pseudoElement:].cold.4
+ -[RWIProtocolDOMDomainEventDispatcher pseudoElementAddedWithParentId:pseudoElement:].cold.5
+ -[RWIProtocolDOMDomainEventDispatcher pseudoElementAddedWithParentId:pseudoElement:].cold.6
+ -[RWIProtocolDOMDomainEventDispatcher pseudoElementAddedWithParentId:pseudoElement:].cold.7
+ -[RWIProtocolDOMDomainEventDispatcher pseudoElementAddedWithParentId:pseudoElement:].cold.8
+ -[RWIProtocolDOMDomainEventDispatcher pseudoElementRemovedWithParentId:pseudoElementId:].cold.2
+ -[RWIProtocolDOMDomainEventDispatcher pseudoElementRemovedWithParentId:pseudoElementId:].cold.3
+ -[RWIProtocolDOMDomainEventDispatcher pseudoElementRemovedWithParentId:pseudoElementId:].cold.4
+ -[RWIProtocolDOMDomainEventDispatcher pseudoElementRemovedWithParentId:pseudoElementId:].cold.5
+ -[RWIProtocolDOMDomainEventDispatcher pseudoElementRemovedWithParentId:pseudoElementId:].cold.6
+ -[RWIProtocolDOMDomainEventDispatcher pseudoElementRemovedWithParentId:pseudoElementId:].cold.7
+ -[RWIProtocolDOMDomainEventDispatcher setChildNodesWithParentId:nodes:].cold.3
+ -[RWIProtocolDOMDomainEventDispatcher setChildNodesWithParentId:nodes:].cold.4
+ -[RWIProtocolDOMDomainEventDispatcher setChildNodesWithParentId:nodes:].cold.5
+ -[RWIProtocolDOMDomainEventDispatcher setChildNodesWithParentId:nodes:].cold.6
+ -[RWIProtocolDOMDomainEventDispatcher setChildNodesWithParentId:nodes:].cold.7
+ -[RWIProtocolDOMDomainEventDispatcher setChildNodesWithParentId:nodes:].cold.8
+ -[RWIProtocolDOMDomainEventDispatcher shadowRootPoppedWithHostId:rootId:].cold.2
+ -[RWIProtocolDOMDomainEventDispatcher shadowRootPoppedWithHostId:rootId:].cold.3
+ -[RWIProtocolDOMDomainEventDispatcher shadowRootPoppedWithHostId:rootId:].cold.4
+ -[RWIProtocolDOMDomainEventDispatcher shadowRootPoppedWithHostId:rootId:].cold.5
+ -[RWIProtocolDOMDomainEventDispatcher shadowRootPoppedWithHostId:rootId:].cold.6
+ -[RWIProtocolDOMDomainEventDispatcher shadowRootPoppedWithHostId:rootId:].cold.7
+ -[RWIProtocolDOMDomainEventDispatcher shadowRootPushedWithHostId:root:].cold.3
+ -[RWIProtocolDOMDomainEventDispatcher shadowRootPushedWithHostId:root:].cold.4
+ -[RWIProtocolDOMDomainEventDispatcher shadowRootPushedWithHostId:root:].cold.5
+ -[RWIProtocolDOMDomainEventDispatcher shadowRootPushedWithHostId:root:].cold.6
+ -[RWIProtocolDOMDomainEventDispatcher shadowRootPushedWithHostId:root:].cold.7
+ -[RWIProtocolDOMDomainEventDispatcher shadowRootPushedWithHostId:root:].cold.8
+ -[RWIProtocolDOMDomainEventDispatcher willDestroyDOMNodeWithNodeId:].cold.2
+ -[RWIProtocolDOMDomainEventDispatcher willDestroyDOMNodeWithNodeId:].cold.3
+ -[RWIProtocolDOMDomainEventDispatcher willDestroyDOMNodeWithNodeId:].cold.4
+ -[RWIProtocolDOMDomainEventDispatcher willDestroyDOMNodeWithNodeId:].cold.5
+ -[RWIProtocolDOMDomainEventDispatcher willDestroyDOMNodeWithNodeId:].cold.6
+ -[RWIProtocolDOMDomainEventDispatcher willRemoveEventListenerWithNodeId:].cold.2
+ -[RWIProtocolDOMDomainEventDispatcher willRemoveEventListenerWithNodeId:].cold.3
+ -[RWIProtocolDOMDomainEventDispatcher willRemoveEventListenerWithNodeId:].cold.4
+ -[RWIProtocolDOMDomainEventDispatcher willRemoveEventListenerWithNodeId:].cold.5
+ -[RWIProtocolDOMDomainEventDispatcher willRemoveEventListenerWithNodeId:].cold.6
+ -[RWIProtocolDOMNode attributes].cold.2
+ -[RWIProtocolDOMNode children].cold.2
+ -[RWIProtocolDOMNode layoutFlags].cold.2
+ -[RWIProtocolDOMNode pseudoElements].cold.2
+ -[RWIProtocolDOMNode setCustomElementState:].cold.1
+ -[RWIProtocolDOMNode setShadowRootType:].cold.1
+ -[RWIProtocolDOMNode shadowRoots].cold.2
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemAddedWithStorageId:key:newValue:].cold.3
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemAddedWithStorageId:key:newValue:].cold.4
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemAddedWithStorageId:key:newValue:].cold.5
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemAddedWithStorageId:key:newValue:].cold.6
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemAddedWithStorageId:key:newValue:].cold.7
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemAddedWithStorageId:key:newValue:].cold.8
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemAddedWithStorageId:key:newValue:].cold.9
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemRemovedWithStorageId:key:].cold.3
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemRemovedWithStorageId:key:].cold.4
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemRemovedWithStorageId:key:].cold.5
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemRemovedWithStorageId:key:].cold.6
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemRemovedWithStorageId:key:].cold.7
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemRemovedWithStorageId:key:].cold.8
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemUpdatedWithStorageId:key:oldValue:newValue:].cold.10
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemUpdatedWithStorageId:key:oldValue:newValue:].cold.3
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemUpdatedWithStorageId:key:oldValue:newValue:].cold.4
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemUpdatedWithStorageId:key:oldValue:newValue:].cold.5
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemUpdatedWithStorageId:key:oldValue:newValue:].cold.6
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemUpdatedWithStorageId:key:oldValue:newValue:].cold.7
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemUpdatedWithStorageId:key:oldValue:newValue:].cold.8
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemUpdatedWithStorageId:key:oldValue:newValue:].cold.9
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemsClearedWithStorageId:].cold.3
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemsClearedWithStorageId:].cold.4
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemsClearedWithStorageId:].cold.5
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemsClearedWithStorageId:].cold.6
+ -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemsClearedWithStorageId:].cold.7
+ -[RWIProtocolDOMStyleable pseudoId].cold.2
+ -[RWIProtocolDOMStyleable setPseudoId:].cold.1
+ -[RWIProtocolDebuggerBreakpointAction setType:].cold.1
+ -[RWIProtocolDebuggerBreakpointOptions actions].cold.2
+ -[RWIProtocolDebuggerCallFrame scopeChain].cold.2
+ -[RWIProtocolDebuggerFunctionDetails scopeChain].cold.2
+ -[RWIProtocolDebuggerScope setType:].cold.1
+ -[RWIProtocolJSONObject JSONArrayForKey:].cold.2
+ -[RWIProtocolJSONObject boolForKey:].cold.2
+ -[RWIProtocolJSONObject init].cold.1
+ -[RWIProtocolJSONObject integerForKey:].cold.2
+ -[RWIProtocolJSONObject objectForKey:].cold.3
+ -[RWIProtocolJSONObject removeKey:].cold.2
+ -[RWIProtocolJSONObject setBool:forKey:].cold.2
+ -[RWIProtocolJSONObject setDouble:forKey:].cold.2
+ -[RWIProtocolJSONObject setInteger:forKey:].cold.2
+ -[RWIProtocolJSONObject setJSONArray:forKey:].cold.3
+ -[RWIProtocolJSONObject setObject:forKey:].cold.2
+ -[RWIProtocolJSONObject setString:forKey:].cold.1
+ -[RWIProtocolJSONObject stringForKey:].cold.2
+ -[RWIProtocolNetworkCachedResource setType:].cold.1
+ -[RWIProtocolNetworkDomainEventDispatcher dataReceivedWithRequestId:timestamp:dataLength:encodedDataLength:].cold.2
+ -[RWIProtocolNetworkDomainEventDispatcher dataReceivedWithRequestId:timestamp:dataLength:encodedDataLength:].cold.3
+ -[RWIProtocolNetworkDomainEventDispatcher dataReceivedWithRequestId:timestamp:dataLength:encodedDataLength:].cold.4
+ -[RWIProtocolNetworkDomainEventDispatcher dataReceivedWithRequestId:timestamp:dataLength:encodedDataLength:].cold.5
+ -[RWIProtocolNetworkDomainEventDispatcher dataReceivedWithRequestId:timestamp:dataLength:encodedDataLength:].cold.6
+ -[RWIProtocolNetworkDomainEventDispatcher dataReceivedWithRequestId:timestamp:dataLength:encodedDataLength:].cold.7
+ -[RWIProtocolNetworkDomainEventDispatcher dataReceivedWithRequestId:timestamp:dataLength:encodedDataLength:].cold.8
+ -[RWIProtocolNetworkDomainEventDispatcher dataReceivedWithRequestId:timestamp:dataLength:encodedDataLength:].cold.9
+ -[RWIProtocolNetworkDomainEventDispatcher loadingFailedWithRequestId:timestamp:errorText:canceled:].cold.2
+ -[RWIProtocolNetworkDomainEventDispatcher loadingFailedWithRequestId:timestamp:errorText:canceled:].cold.3
+ -[RWIProtocolNetworkDomainEventDispatcher loadingFailedWithRequestId:timestamp:errorText:canceled:].cold.4
+ -[RWIProtocolNetworkDomainEventDispatcher loadingFailedWithRequestId:timestamp:errorText:canceled:].cold.5
+ -[RWIProtocolNetworkDomainEventDispatcher loadingFailedWithRequestId:timestamp:errorText:canceled:].cold.6
+ -[RWIProtocolNetworkDomainEventDispatcher loadingFailedWithRequestId:timestamp:errorText:canceled:].cold.7
+ -[RWIProtocolNetworkDomainEventDispatcher loadingFailedWithRequestId:timestamp:errorText:canceled:].cold.8
+ -[RWIProtocolNetworkDomainEventDispatcher loadingFailedWithRequestId:timestamp:errorText:canceled:].cold.9
+ -[RWIProtocolNetworkDomainEventDispatcher loadingFinishedWithRequestId:timestamp:sourceMapURL:metrics:].cold.3
+ -[RWIProtocolNetworkDomainEventDispatcher loadingFinishedWithRequestId:timestamp:sourceMapURL:metrics:].cold.4
+ -[RWIProtocolNetworkDomainEventDispatcher loadingFinishedWithRequestId:timestamp:sourceMapURL:metrics:].cold.5
+ -[RWIProtocolNetworkDomainEventDispatcher loadingFinishedWithRequestId:timestamp:sourceMapURL:metrics:].cold.6
+ -[RWIProtocolNetworkDomainEventDispatcher loadingFinishedWithRequestId:timestamp:sourceMapURL:metrics:].cold.7
+ -[RWIProtocolNetworkDomainEventDispatcher loadingFinishedWithRequestId:timestamp:sourceMapURL:metrics:].cold.8
+ -[RWIProtocolNetworkDomainEventDispatcher loadingFinishedWithRequestId:timestamp:sourceMapURL:metrics:].cold.9
+ -[RWIProtocolNetworkDomainEventDispatcher requestInterceptedWithRequestId:request:].cold.3
+ -[RWIProtocolNetworkDomainEventDispatcher requestInterceptedWithRequestId:request:].cold.4
+ -[RWIProtocolNetworkDomainEventDispatcher requestInterceptedWithRequestId:request:].cold.5
+ -[RWIProtocolNetworkDomainEventDispatcher requestInterceptedWithRequestId:request:].cold.6
+ -[RWIProtocolNetworkDomainEventDispatcher requestInterceptedWithRequestId:request:].cold.7
+ -[RWIProtocolNetworkDomainEventDispatcher requestInterceptedWithRequestId:request:].cold.8
+ -[RWIProtocolNetworkDomainEventDispatcher requestServedFromMemoryCacheWithRequestId:frameId:loaderId:documentURL:timestamp:initiator:resource:].cold.10
+ -[RWIProtocolNetworkDomainEventDispatcher requestServedFromMemoryCacheWithRequestId:frameId:loaderId:documentURL:timestamp:initiator:resource:].cold.11
+ -[RWIProtocolNetworkDomainEventDispatcher requestServedFromMemoryCacheWithRequestId:frameId:loaderId:documentURL:timestamp:initiator:resource:].cold.12
+ -[RWIProtocolNetworkDomainEventDispatcher requestServedFromMemoryCacheWithRequestId:frameId:loaderId:documentURL:timestamp:initiator:resource:].cold.13
+ -[RWIProtocolNetworkDomainEventDispatcher requestServedFromMemoryCacheWithRequestId:frameId:loaderId:documentURL:timestamp:initiator:resource:].cold.14
+ -[RWIProtocolNetworkDomainEventDispatcher requestServedFromMemoryCacheWithRequestId:frameId:loaderId:documentURL:timestamp:initiator:resource:].cold.4
+ -[RWIProtocolNetworkDomainEventDispatcher requestServedFromMemoryCacheWithRequestId:frameId:loaderId:documentURL:timestamp:initiator:resource:].cold.5
+ -[RWIProtocolNetworkDomainEventDispatcher requestServedFromMemoryCacheWithRequestId:frameId:loaderId:documentURL:timestamp:initiator:resource:].cold.6
+ -[RWIProtocolNetworkDomainEventDispatcher requestServedFromMemoryCacheWithRequestId:frameId:loaderId:documentURL:timestamp:initiator:resource:].cold.7
+ -[RWIProtocolNetworkDomainEventDispatcher requestServedFromMemoryCacheWithRequestId:frameId:loaderId:documentURL:timestamp:initiator:resource:].cold.8
+ -[RWIProtocolNetworkDomainEventDispatcher requestServedFromMemoryCacheWithRequestId:frameId:loaderId:documentURL:timestamp:initiator:resource:].cold.9
+ -[RWIProtocolNetworkDomainEventDispatcher requestWillBeSentWithRequestId:frameId:loaderId:documentURL:request:timestamp:walltime:initiator:redirectResponse:type:targetId:].cold.10
+ -[RWIProtocolNetworkDomainEventDispatcher requestWillBeSentWithRequestId:frameId:loaderId:documentURL:request:timestamp:walltime:initiator:redirectResponse:type:targetId:].cold.11
+ -[RWIProtocolNetworkDomainEventDispatcher requestWillBeSentWithRequestId:frameId:loaderId:documentURL:request:timestamp:walltime:initiator:redirectResponse:type:targetId:].cold.12
+ -[RWIProtocolNetworkDomainEventDispatcher requestWillBeSentWithRequestId:frameId:loaderId:documentURL:request:timestamp:walltime:initiator:redirectResponse:type:targetId:].cold.13
+ -[RWIProtocolNetworkDomainEventDispatcher requestWillBeSentWithRequestId:frameId:loaderId:documentURL:request:timestamp:walltime:initiator:redirectResponse:type:targetId:].cold.14
+ -[RWIProtocolNetworkDomainEventDispatcher requestWillBeSentWithRequestId:frameId:loaderId:documentURL:request:timestamp:walltime:initiator:redirectResponse:type:targetId:].cold.15
+ -[RWIProtocolNetworkDomainEventDispatcher requestWillBeSentWithRequestId:frameId:loaderId:documentURL:request:timestamp:walltime:initiator:redirectResponse:type:targetId:].cold.16
+ -[RWIProtocolNetworkDomainEventDispatcher requestWillBeSentWithRequestId:frameId:loaderId:documentURL:request:timestamp:walltime:initiator:redirectResponse:type:targetId:].cold.17
+ -[RWIProtocolNetworkDomainEventDispatcher requestWillBeSentWithRequestId:frameId:loaderId:documentURL:request:timestamp:walltime:initiator:redirectResponse:type:targetId:].cold.18
+ -[RWIProtocolNetworkDomainEventDispatcher requestWillBeSentWithRequestId:frameId:loaderId:documentURL:request:timestamp:walltime:initiator:redirectResponse:type:targetId:].cold.19
+ -[RWIProtocolNetworkDomainEventDispatcher requestWillBeSentWithRequestId:frameId:loaderId:documentURL:request:timestamp:walltime:initiator:redirectResponse:type:targetId:].cold.5
+ -[RWIProtocolNetworkDomainEventDispatcher requestWillBeSentWithRequestId:frameId:loaderId:documentURL:request:timestamp:walltime:initiator:redirectResponse:type:targetId:].cold.6
+ -[RWIProtocolNetworkDomainEventDispatcher requestWillBeSentWithRequestId:frameId:loaderId:documentURL:request:timestamp:walltime:initiator:redirectResponse:type:targetId:].cold.7
+ -[RWIProtocolNetworkDomainEventDispatcher requestWillBeSentWithRequestId:frameId:loaderId:documentURL:request:timestamp:walltime:initiator:redirectResponse:type:targetId:].cold.8
+ -[RWIProtocolNetworkDomainEventDispatcher requestWillBeSentWithRequestId:frameId:loaderId:documentURL:request:timestamp:walltime:initiator:redirectResponse:type:targetId:].cold.9
+ -[RWIProtocolNetworkDomainEventDispatcher responseInterceptedWithRequestId:response:].cold.3
+ -[RWIProtocolNetworkDomainEventDispatcher responseInterceptedWithRequestId:response:].cold.4
+ -[RWIProtocolNetworkDomainEventDispatcher responseInterceptedWithRequestId:response:].cold.5
+ -[RWIProtocolNetworkDomainEventDispatcher responseInterceptedWithRequestId:response:].cold.6
+ -[RWIProtocolNetworkDomainEventDispatcher responseInterceptedWithRequestId:response:].cold.7
+ -[RWIProtocolNetworkDomainEventDispatcher responseInterceptedWithRequestId:response:].cold.8
+ -[RWIProtocolNetworkDomainEventDispatcher responseReceivedWithRequestId:frameId:loaderId:timestamp:type:response:].cold.10
+ -[RWIProtocolNetworkDomainEventDispatcher responseReceivedWithRequestId:frameId:loaderId:timestamp:type:response:].cold.11
+ -[RWIProtocolNetworkDomainEventDispatcher responseReceivedWithRequestId:frameId:loaderId:timestamp:type:response:].cold.12
+ -[RWIProtocolNetworkDomainEventDispatcher responseReceivedWithRequestId:frameId:loaderId:timestamp:type:response:].cold.3
+ -[RWIProtocolNetworkDomainEventDispatcher responseReceivedWithRequestId:frameId:loaderId:timestamp:type:response:].cold.4
+ -[RWIProtocolNetworkDomainEventDispatcher responseReceivedWithRequestId:frameId:loaderId:timestamp:type:response:].cold.5
+ -[RWIProtocolNetworkDomainEventDispatcher responseReceivedWithRequestId:frameId:loaderId:timestamp:type:response:].cold.6
+ -[RWIProtocolNetworkDomainEventDispatcher responseReceivedWithRequestId:frameId:loaderId:timestamp:type:response:].cold.7
+ -[RWIProtocolNetworkDomainEventDispatcher responseReceivedWithRequestId:frameId:loaderId:timestamp:type:response:].cold.8
+ -[RWIProtocolNetworkDomainEventDispatcher responseReceivedWithRequestId:frameId:loaderId:timestamp:type:response:].cold.9
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketClosedWithRequestId:timestamp:].cold.2
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketClosedWithRequestId:timestamp:].cold.3
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketClosedWithRequestId:timestamp:].cold.4
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketClosedWithRequestId:timestamp:].cold.5
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketClosedWithRequestId:timestamp:].cold.6
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketClosedWithRequestId:timestamp:].cold.7
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketCreatedWithRequestId:url:].cold.2
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketCreatedWithRequestId:url:].cold.3
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketCreatedWithRequestId:url:].cold.4
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketCreatedWithRequestId:url:].cold.5
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketCreatedWithRequestId:url:].cold.6
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketCreatedWithRequestId:url:].cold.7
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameErrorWithRequestId:timestamp:errorMessage:].cold.2
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameErrorWithRequestId:timestamp:errorMessage:].cold.3
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameErrorWithRequestId:timestamp:errorMessage:].cold.4
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameErrorWithRequestId:timestamp:errorMessage:].cold.5
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameErrorWithRequestId:timestamp:errorMessage:].cold.6
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameErrorWithRequestId:timestamp:errorMessage:].cold.7
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameErrorWithRequestId:timestamp:errorMessage:].cold.8
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameReceivedWithRequestId:timestamp:response:].cold.3
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameReceivedWithRequestId:timestamp:response:].cold.4
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameReceivedWithRequestId:timestamp:response:].cold.5
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameReceivedWithRequestId:timestamp:response:].cold.6
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameReceivedWithRequestId:timestamp:response:].cold.7
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameReceivedWithRequestId:timestamp:response:].cold.8
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameReceivedWithRequestId:timestamp:response:].cold.9
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameSentWithRequestId:timestamp:response:].cold.3
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameSentWithRequestId:timestamp:response:].cold.4
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameSentWithRequestId:timestamp:response:].cold.5
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameSentWithRequestId:timestamp:response:].cold.6
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameSentWithRequestId:timestamp:response:].cold.7
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameSentWithRequestId:timestamp:response:].cold.8
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameSentWithRequestId:timestamp:response:].cold.9
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketHandshakeResponseReceivedWithRequestId:timestamp:response:].cold.3
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketHandshakeResponseReceivedWithRequestId:timestamp:response:].cold.4
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketHandshakeResponseReceivedWithRequestId:timestamp:response:].cold.5
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketHandshakeResponseReceivedWithRequestId:timestamp:response:].cold.6
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketHandshakeResponseReceivedWithRequestId:timestamp:response:].cold.7
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketHandshakeResponseReceivedWithRequestId:timestamp:response:].cold.8
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketHandshakeResponseReceivedWithRequestId:timestamp:response:].cold.9
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketWillSendHandshakeRequestWithRequestId:timestamp:walltime:request:].cold.10
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketWillSendHandshakeRequestWithRequestId:timestamp:walltime:request:].cold.3
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketWillSendHandshakeRequestWithRequestId:timestamp:walltime:request:].cold.4
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketWillSendHandshakeRequestWithRequestId:timestamp:walltime:request:].cold.5
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketWillSendHandshakeRequestWithRequestId:timestamp:walltime:request:].cold.6
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketWillSendHandshakeRequestWithRequestId:timestamp:walltime:request:].cold.7
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketWillSendHandshakeRequestWithRequestId:timestamp:walltime:request:].cold.8
+ -[RWIProtocolNetworkDomainEventDispatcher webSocketWillSendHandshakeRequestWithRequestId:timestamp:walltime:request:].cold.9
+ -[RWIProtocolNetworkInitiator setType:].cold.1
+ -[RWIProtocolNetworkMetrics setPriority:].cold.1
+ -[RWIProtocolNetworkRequest setReferrerPolicy:].cold.1
+ -[RWIProtocolNetworkResponse setSource:].cold.1
+ -[RWIProtocolPageCookie partitionKey]
+ -[RWIProtocolPageCookie setPartitionKey:]
+ -[RWIProtocolPageCookie setSameSite:].cold.1
+ -[RWIProtocolPageDomainEventDispatcher defaultUserPreferencesDidChangeWithPreferences:].cold.3
+ -[RWIProtocolPageDomainEventDispatcher defaultUserPreferencesDidChangeWithPreferences:].cold.4
+ -[RWIProtocolPageDomainEventDispatcher defaultUserPreferencesDidChangeWithPreferences:].cold.5
+ -[RWIProtocolPageDomainEventDispatcher defaultUserPreferencesDidChangeWithPreferences:].cold.6
+ -[RWIProtocolPageDomainEventDispatcher defaultUserPreferencesDidChangeWithPreferences:].cold.7
+ -[RWIProtocolPageDomainEventDispatcher domContentEventFiredWithTimestamp:].cold.2
+ -[RWIProtocolPageDomainEventDispatcher domContentEventFiredWithTimestamp:].cold.3
+ -[RWIProtocolPageDomainEventDispatcher domContentEventFiredWithTimestamp:].cold.4
+ -[RWIProtocolPageDomainEventDispatcher domContentEventFiredWithTimestamp:].cold.5
+ -[RWIProtocolPageDomainEventDispatcher domContentEventFiredWithTimestamp:].cold.6
+ -[RWIProtocolPageDomainEventDispatcher frameClearedScheduledNavigationWithFrameId:].cold.2
+ -[RWIProtocolPageDomainEventDispatcher frameClearedScheduledNavigationWithFrameId:].cold.3
+ -[RWIProtocolPageDomainEventDispatcher frameClearedScheduledNavigationWithFrameId:].cold.4
+ -[RWIProtocolPageDomainEventDispatcher frameClearedScheduledNavigationWithFrameId:].cold.5
+ -[RWIProtocolPageDomainEventDispatcher frameClearedScheduledNavigationWithFrameId:].cold.6
+ -[RWIProtocolPageDomainEventDispatcher frameDetachedWithFrameId:].cold.2
+ -[RWIProtocolPageDomainEventDispatcher frameDetachedWithFrameId:].cold.3
+ -[RWIProtocolPageDomainEventDispatcher frameDetachedWithFrameId:].cold.4
+ -[RWIProtocolPageDomainEventDispatcher frameDetachedWithFrameId:].cold.5
+ -[RWIProtocolPageDomainEventDispatcher frameDetachedWithFrameId:].cold.6
+ -[RWIProtocolPageDomainEventDispatcher frameNavigatedWithFrame:].cold.3
+ -[RWIProtocolPageDomainEventDispatcher frameNavigatedWithFrame:].cold.4
+ -[RWIProtocolPageDomainEventDispatcher frameNavigatedWithFrame:].cold.5
+ -[RWIProtocolPageDomainEventDispatcher frameNavigatedWithFrame:].cold.6
+ -[RWIProtocolPageDomainEventDispatcher frameNavigatedWithFrame:].cold.7
+ -[RWIProtocolPageDomainEventDispatcher frameScheduledNavigationWithFrameId:delay:].cold.2
+ -[RWIProtocolPageDomainEventDispatcher frameScheduledNavigationWithFrameId:delay:].cold.3
+ -[RWIProtocolPageDomainEventDispatcher frameScheduledNavigationWithFrameId:delay:].cold.4
+ -[RWIProtocolPageDomainEventDispatcher frameScheduledNavigationWithFrameId:delay:].cold.5
+ -[RWIProtocolPageDomainEventDispatcher frameScheduledNavigationWithFrameId:delay:].cold.6
+ -[RWIProtocolPageDomainEventDispatcher frameScheduledNavigationWithFrameId:delay:].cold.7
+ -[RWIProtocolPageDomainEventDispatcher frameStartedLoadingWithFrameId:].cold.2
+ -[RWIProtocolPageDomainEventDispatcher frameStartedLoadingWithFrameId:].cold.3
+ -[RWIProtocolPageDomainEventDispatcher frameStartedLoadingWithFrameId:].cold.4
+ -[RWIProtocolPageDomainEventDispatcher frameStartedLoadingWithFrameId:].cold.5
+ -[RWIProtocolPageDomainEventDispatcher frameStartedLoadingWithFrameId:].cold.6
+ -[RWIProtocolPageDomainEventDispatcher frameStoppedLoadingWithFrameId:].cold.2
+ -[RWIProtocolPageDomainEventDispatcher frameStoppedLoadingWithFrameId:].cold.3
+ -[RWIProtocolPageDomainEventDispatcher frameStoppedLoadingWithFrameId:].cold.4
+ -[RWIProtocolPageDomainEventDispatcher frameStoppedLoadingWithFrameId:].cold.5
+ -[RWIProtocolPageDomainEventDispatcher frameStoppedLoadingWithFrameId:].cold.6
+ -[RWIProtocolPageDomainEventDispatcher loadEventFiredWithTimestamp:].cold.2
+ -[RWIProtocolPageDomainEventDispatcher loadEventFiredWithTimestamp:].cold.3
+ -[RWIProtocolPageDomainEventDispatcher loadEventFiredWithTimestamp:].cold.4
+ -[RWIProtocolPageDomainEventDispatcher loadEventFiredWithTimestamp:].cold.5
+ -[RWIProtocolPageDomainEventDispatcher loadEventFiredWithTimestamp:].cold.6
+ -[RWIProtocolPageFrameResource setType:].cold.1
+ -[RWIProtocolPageFrameResourceTree childFrames].cold.2
+ -[RWIProtocolPageFrameResourceTree resources].cold.2
+ -[RWIProtocolPageUserPreference setName:].cold.1
+ -[RWIProtocolPageUserPreference setValue:].cold.1
+ -[RWIProtocolRuntimeExecutionContextDescription setType:].cold.1
+ -[RWIProtocolRuntimeObjectPreview entries].cold.2
+ -[RWIProtocolRuntimeObjectPreview properties].cold.2
+ -[RWIProtocolRuntimeObjectPreview setSubtype:].cold.1
+ -[RWIProtocolRuntimeObjectPreview setType:].cold.1
+ -[RWIProtocolRuntimePropertyPreview setSubtype:].cold.1
+ -[RWIProtocolRuntimePropertyPreview setType:].cold.1
+ -[RWIProtocolRuntimeRemoteObject setSubtype:].cold.1
+ -[RWIProtocolRuntimeRemoteObject setType:].cold.1
+ -[RWIProtocolRuntimeStructureDescription fields].cold.2
+ -[RWIProtocolRuntimeStructureDescription optionalFields].cold.2
+ -[RWIProtocolRuntimeTypeDescription structures].cold.2
+ -[RWIProtocolSecurityCertificate dnsNames].cold.2
+ -[RWIProtocolSecurityCertificate ipAddresses].cold.2
+ AMDCopyErrorText.cold.1
+ AMDGetBundleVersion.cold.1
+ AMDSecureListenForNotificationsWithRetainedContext.cold.1
+ AMDSecureObserveNotification.cold.1
+ AMDSecureShutdownNotificationProxy.cold.1
+ AMDServiceConnectionGetSocket.cold.1
+ AMDServiceConnectionInvalidate.cold.1
+ AMDServiceConnectionReceive.cold.1
+ AMDServiceConnectionSend.cold.1
+ AMDeviceConnect.cold.1
+ AMDeviceCopyBonjourFullServiceName.cold.1
+ AMDeviceCopyDeviceIdentifier.cold.1
+ AMDeviceCopyValueWithError.cold.1
+ AMDeviceCopyWirelessDeviceValueWithError.cold.1
+ AMDeviceDeleteHostPairingRecordForUDID.cold.1
+ AMDeviceDisconnect.cold.1
+ AMDeviceGetInterfaceType.cold.1
+ AMDeviceIsValid.cold.1
+ AMDeviceIsWiFiPairableRef.cold.1
+ AMDeviceNotificationSubscribeWithOptions.cold.1
+ AMDeviceNotificationUnsubscribe.cold.1
+ AMDeviceRemoveValue.cold.1
+ AMDeviceSecureStartService.cold.1
+ AMDeviceSetValue.cold.1
+ AMDeviceStartSession.cold.1
+ AMDeviceStopSession.cold.1
+ AMDeviceUnpair.cold.1
+ AMDeviceValidatePairing.cold.1
+ AMDeviceWiFiPairableCopyRealUniqueDeviceID.cold.1
+ GCC_except_table782
+ GCC_except_table785
+ GCC_except_table788
+ GCC_except_table792
+ GCC_except_table803
+ GCC_except_table806
+ GCC_except_table809
+ GCC_except_table820
+ GCC_except_table821
+ GCC_except_table824
+ GCC_except_table829
+ GCC_except_table832
+ GCC_except_table836
+ GCC_except_table845
+ GCC_except_table850
+ GCC_except_table851
+ GCC_except_table855
+ GCC_except_table861
+ GCC_except_table871
+ GCC_except_table876
+ GCC_except_table882
+ GCC_except_table885
+ GCC_except_table888
+ GCC_except_table889
+ GCC_except_table894
+ GCC_except_table901
+ GCC_except_table902
+ GCC_except_table906
+ GCC_except_table909
+ GCC_except_table930
+ GCC_except_table938
+ GCC_except_table939
+ GCC_except_table942
+ GCC_except_table949
+ GCC_except_table970
+ GCC_except_table975
+ OBJC_IVAR_$_RWIDriverConfiguration._driverBidiPort
+ RWIDefaultLog.cold.1
+ RWIMessageDumpStateLog.cold.1
+ RWIMessageTraceLog.cold.1
+ RWIMobileDeviceDebugLog.cold.1
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _ZL13initSimDevicev.cold.1
+ _ZL21initSimServiceContextv.cold.1
+ _ZN3WTF16VectorDestructorILb1ENSt3__15tupleIJN9Inspector17BackendDispatcher15CommonErrorCodeENS_6StringEEEEE8destructEPS7_S9_.cold.1
+ _ZN3WTF9HashTableINS_6StringENS_12KeyValuePairIS1_NS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEEEENS_24KeyValuePairKeyExtractorISB_EENS_11DefaultHashIS1_EENS_7HashMapIS1_SA_SF_NS_10HashTraitsIS1_EENSH_ISA_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE18KeyValuePairTraitsESI_LSL_0EE6rehashEjPSB_.cold.1
+ _ZN3WTF9HashTableINS_6StringENS_12KeyValuePairIS1_PN9Inspector29SupplementalBackendDispatcherEEENS_24KeyValuePairKeyExtractorIS6_EENS_11DefaultHashIS1_EENS_7HashMapIS1_S5_SA_NS_10HashTraitsIS1_EENSC_IS5_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE18KeyValuePairTraitsESD_LSG_0EE15deallocateTableEPS6_.cold.1
+ _ZN9Inspector33ObjCInspectorCSSBackendDispatcher12setStyleTextElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEERKNS1_6StringE.cold.2
+ _ZN9Inspector33ObjCInspectorCSSBackendDispatcher13getStyleSheetElRKN3WTF6StringE.cold.2
+ _ZN9Inspector33ObjCInspectorCSSBackendDispatcher15setRuleSelectorElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEERKNS1_6StringE.cold.2
+ _ZN9Inspector33ObjCInspectorCSSBackendDispatcher16createStyleSheetElRKN3WTF6StringE.cold.2
+ _ZN9Inspector33ObjCInspectorCSSBackendDispatcher16forcePseudoStateEliON3WTF3RefINS1_8JSONImpl5ArrayENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE.cold.3
+ _ZN9Inspector33ObjCInspectorCSSBackendDispatcher17getAllStyleSheetsEl.cold.2
+ _ZN9Inspector33ObjCInspectorCSSBackendDispatcher17getStyleSheetTextElRKN3WTF6StringE.cold.2
+ _ZN9Inspector33ObjCInspectorCSSBackendDispatcher17setStyleSheetTextElRKN3WTF6StringES4_.cold.2
+ _ZN9Inspector33ObjCInspectorCSSBackendDispatcher18getFontDataForNodeEli.cold.2
+ _ZN9Inspector33ObjCInspectorCSSBackendDispatcher21setGroupingHeaderTextElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEERKNS1_6StringE.cold.2
+ _ZN9Inspector33ObjCInspectorCSSBackendDispatcher22getInlineStylesForNodeEli.cold.2
+ _ZN9Inspector33ObjCInspectorCSSBackendDispatcher23getComputedStyleForNodeEli.cold.2
+ _ZN9Inspector33ObjCInspectorCSSBackendDispatcher23getMatchedStylesForNodeEliONSt3__18optionalIbEES4_.cold.2
+ _ZN9Inspector33ObjCInspectorCSSBackendDispatcher25getSupportedCSSPropertiesEl.cold.2
+ _ZN9Inspector33ObjCInspectorCSSBackendDispatcher31setLayoutContextTypeChangedModeElRKN3WTF6StringE.cold.3
+ _ZN9Inspector33ObjCInspectorCSSBackendDispatcher31setLayoutContextTypeChangedModeElRKN3WTF6StringE.cold.4
+ _ZN9Inspector33ObjCInspectorCSSBackendDispatcher33getSupportedSystemFontFamilyNamesEl.cold.2
+ _ZN9Inspector33ObjCInspectorCSSBackendDispatcher6enableEl.cold.2
+ _ZN9Inspector33ObjCInspectorCSSBackendDispatcher7addRuleElRKN3WTF6StringES4_.cold.2
+ _ZN9Inspector33ObjCInspectorCSSBackendDispatcher7disableEl.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher10removeNodeEli.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher11getDocumentEl.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher11requestNodeElRKN3WTF6StringE.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher11resolveNodeEliRKN3WTF6StringE.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher11setNodeNameEliRKN3WTF6StringE.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher12getOuterHTMLEli.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher12setNodeValueEliRKN3WTF6StringE.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher12setOuterHTMLEliRKN3WTF6StringE.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher13getAttributesEli.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher13getMediaStatsEli.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher13hideHighlightEl.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher13highlightNodeElONSt3__18optionalIiEERKN3WTF6StringEONS5_3RefINS5_8JSONImpl6ObjectENS5_12RawPtrTraitsISB_EENS5_21DefaultRefDerefTraitsISB_EEEEONS5_6RefPtrISB_SD_SF_EESK_ONS2_IbEE.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher13highlightNodeElONSt3__18optionalIiEERKN3WTF6StringEONS5_3RefINS5_8JSONImpl6ObjectENS5_12RawPtrTraitsISB_EENS5_21DefaultRefDerefTraitsISB_EEEEONS5_6RefPtrISB_SD_SF_EESK_ONS2_IbEE.cold.3
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher13highlightNodeElONSt3__18optionalIiEERKN3WTF6StringEONS5_3RefINS5_8JSONImpl6ObjectENS5_12RawPtrTraitsISB_EENS5_21DefaultRefDerefTraitsISB_EEEEONS5_6RefPtrISB_SD_SF_EESK_ONS2_IbEE.cold.4
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher13highlightQuadElON3WTF3RefINS1_8JSONImpl5ArrayENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEEONS1_6RefPtrINS3_6ObjectENS5_ISC_EENS7_ISC_EEEESG_ONSt3__18optionalIbEE.cold.3
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher13highlightQuadElON3WTF3RefINS1_8JSONImpl5ArrayENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEEONS1_6RefPtrINS3_6ObjectENS5_ISC_EENS7_ISC_EEEESG_ONSt3__18optionalIbEE.cold.4
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher13highlightQuadElON3WTF3RefINS1_8JSONImpl5ArrayENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEEONS1_6RefPtrINS3_6ObjectENS5_ISC_EENS7_ISC_EEEESG_ONSt3__18optionalIbEE.cold.5
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher13highlightRectEliiiiON3WTF6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEESA_ONSt3__18optionalIbEE.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher13highlightRectEliiiiON3WTF6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEESA_ONSt3__18optionalIbEE.cold.3
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher13highlightRectEliiiiON3WTF6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEESA_ONSt3__18optionalIbEE.cold.4
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher13performSearchElRKN3WTF6StringEONS1_6RefPtrINS1_8JSONImpl5ArrayENS1_12RawPtrTraitsIS7_EENS1_21DefaultRefDerefTraitsIS7_EEEEONSt3__18optionalIbEE.cold.3
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher13performSearchElRKN3WTF6StringEONS1_6RefPtrINS1_8JSONImpl5ArrayENS1_12RawPtrTraitsIS7_EENS1_21DefaultRefDerefTraitsIS7_EEEEONSt3__18optionalIbEE.cold.4
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher13querySelectorEliRKN3WTF6StringE.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher14highlightFrameElRKN3WTF6StringEONS1_6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS7_EENS1_21DefaultRefDerefTraitsIS7_EEEESD_.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher14highlightFrameElRKN3WTF6StringEONS1_6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS7_EENS1_21DefaultRefDerefTraitsIS7_EEEESD_.cold.3
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher14highlightFrameElRKN3WTF6StringEONS1_6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS7_EENS1_21DefaultRefDerefTraitsIS7_EEEESD_.cold.4
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher15hideFlexOverlayElONSt3__18optionalIiEE.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher15hideGridOverlayElONSt3__18optionalIiEE.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher15removeAttributeEliRKN3WTF6StringE.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher15showFlexOverlayEliON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher15showGridOverlayEliON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher16getSearchResultsElRKN3WTF6StringEii.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher16querySelectorAllEliRKN3WTF6StringE.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher16setInspectedNodeEli.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher17highlightNodeListElON3WTF3RefINS1_8JSONImpl5ArrayENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEEONS2_INS3_6ObjectENS5_ISB_EENS7_ISB_EEEEONS1_6RefPtrISB_SC_SD_EESI_ONSt3__18optionalIbEE.cold.3
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher17highlightNodeListElON3WTF3RefINS1_8JSONImpl5ArrayENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEEONS2_INS3_6ObjectENS5_ISB_EENS7_ISB_EEEEONS1_6RefPtrISB_SC_SD_EESI_ONSt3__18optionalIbEE.cold.4
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher17highlightNodeListElON3WTF3RefINS1_8JSONImpl5ArrayENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEEONS2_INS3_6ObjectENS5_ISB_EENS7_ISB_EEEEONS1_6RefPtrISB_SC_SD_EESI_ONSt3__18optionalIbEE.cold.5
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher17highlightSelectorElRKN3WTF6StringES4_ONS1_3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS7_EENS1_21DefaultRefDerefTraitsIS7_EEEEONS1_6RefPtrIS7_S9_SB_EESG_ONSt3__18optionalIbEE.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher17highlightSelectorElRKN3WTF6StringES4_ONS1_3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS7_EENS1_21DefaultRefDerefTraitsIS7_EEEEONS1_6RefPtrIS7_S9_SB_EESG_ONSt3__18optionalIbEE.cold.3
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher17highlightSelectorElRKN3WTF6StringES4_ONS1_3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS7_EENS1_21DefaultRefDerefTraitsIS7_EEEEONS1_6RefPtrIS7_S9_SB_EESG_ONSt3__18optionalIbEE.cold.4
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher17markUndoableStateEl.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher17requestChildNodesEliONSt3__18optionalIiEE.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher17setAttributeValueEliRKN3WTF6StringES4_.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher18insertAdjacentHTMLEliRKN3WTF6StringES4_.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher19setAttributesAsTextEliRKN3WTF6StringES4_.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher20discardSearchResultsElRKN3WTF6StringE.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher21setInspectModeEnabledElbON3WTF6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEESA_SA_ONSt3__18optionalIbEE.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher21setInspectModeEnabledElbON3WTF6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEESA_SA_ONSt3__18optionalIbEE.cold.3
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher21setInspectModeEnabledElbON3WTF6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEESA_SA_ONSt3__18optionalIbEE.cold.4
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher21setInspectModeEnabledElbON3WTF6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEESA_SA_ONSt3__18optionalIbEE.cold.5
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher22getDataBindingsForNodeEli.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher22getSupportedEventNamesEl.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher24getAssociatedDataForNodeEli.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher24getEventListenersForNodeEliONSt3__18optionalIbEE.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher24pushNodeByPathToFrontendElRKN3WTF6StringE.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher24setEventListenerDisabledElib.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher29setBreakpointForEventListenerEliON3WTF6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher29setBreakpointForEventListenerEliON3WTF6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE.cold.3
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher32removeBreakpointForEventListenerEli.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher33getAccessibilityPropertiesForNodeEli.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher35setAllowEditingUserAgentShadowTreesElb.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher4redoEl.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher4undoEl.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher5focusEli.cold.2
+ _ZN9Inspector33ObjCInspectorDOMBackendDispatcher6moveToEliiONSt3__18optionalIiEE.cold.2
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher10getCookiesEl.cold.2
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher12deleteCookieElRKN3WTF6StringES4_.cold.2
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher12snapshotNodeEli.cold.2
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher12snapshotRectEliiiiRKN3WTF6StringE.cold.3
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher12snapshotRectEliiiiRKN3WTF6StringE.cold.4
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher13setShowRulersElb.cold.2
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher15getResourceTreeEl.cold.2
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher15overrideSettingElRKN3WTF6StringEONSt3__18optionalIbEE.cold.3
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher15overrideSettingElRKN3WTF6StringEONSt3__18optionalIbEE.cold.4
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher16searchInResourceElRKN3WTF6StringES4_S4_ONSt3__18optionalIbEES8_S4_.cold.2
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher16setEmulatedMediaElRKN3WTF6StringE.cold.2
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher17overrideUserAgentElRKN3WTF6StringE.cold.2
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher17searchInResourcesElRKN3WTF6StringEONSt3__18optionalIbEES8_.cold.2
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher17setShowPaintRectsElb.cold.2
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher18getResourceContentElRKN3WTF6StringES4_.cold.2
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher18setBootstrapScriptElRKN3WTF6StringE.cold.2
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher22overrideUserPreferenceElRKN3WTF6StringES4_.cold.3
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher22overrideUserPreferenceElRKN3WTF6StringES4_.cold.4
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher6enableEl.cold.2
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher6reloadElONSt3__18optionalIbEES4_.cold.2
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher7archiveEl.cold.2
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher7disableEl.cold.2
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher8navigateElRKN3WTF6StringE.cold.2
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher9setCookieElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEEONSt3__18optionalIbEE.cold.1
+ _ZN9Inspector34ObjCInspectorPageBackendDispatcher9setCookieElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEEONSt3__18optionalIbEE.cold.2
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher12loadResourceElRKN3WTF6StringES4_.cold.2
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher15addInterceptionElRKN3WTF6StringES4_ONSt3__18optionalIbEES8_.cold.3
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher15addInterceptionElRKN3WTF6StringES4_ONSt3__18optionalIbEES8_.cold.4
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher15getResponseBodyElRKN3WTF6StringE.cold.2
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher16resolveWebSocketElRKN3WTF6StringES4_.cold.2
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher17interceptContinueElRKN3WTF6StringES4_.cold.3
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher17interceptContinueElRKN3WTF6StringES4_.cold.4
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher18removeInterceptionElRKN3WTF6StringES4_ONSt3__18optionalIbEES8_.cold.3
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher18removeInterceptionElRKN3WTF6StringES4_ONSt3__18optionalIbEES8_.cold.4
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher19setExtraHTTPHeadersElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE.cold.2
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher20interceptWithRequestElRKN3WTF6StringES4_S4_ONS1_6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS7_EENS1_21DefaultRefDerefTraitsIS7_EEEES4_.cold.2
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher20interceptWithRequestElRKN3WTF6StringES4_S4_ONS1_6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS7_EENS1_21DefaultRefDerefTraitsIS7_EEEES4_.cold.3
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher21interceptWithResponseElRKN3WTF6StringES4_bS4_ONSt3__18optionalIiEES4_ONS1_6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsISB_EENS1_21DefaultRefDerefTraitsISB_EEEE.cold.2
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher21interceptWithResponseElRKN3WTF6StringES4_bS4_ONSt3__18optionalIiEES4_ONS1_6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsISB_EENS1_21DefaultRefDerefTraitsISB_EEEE.cold.3
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher22setInterceptionEnabledElb.cold.2
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher24getSerializedCertificateElRKN3WTF6StringE.cold.2
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher25interceptRequestWithErrorElRKN3WTF6StringES4_.cold.3
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher25interceptRequestWithErrorElRKN3WTF6StringES4_.cold.4
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher26setResourceCachingDisabledElb.cold.2
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher28interceptRequestWithResponseElRKN3WTF6StringES4_bS4_iS4_ONS1_3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS7_EENS1_21DefaultRefDerefTraitsIS7_EEEE.cold.2
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher6enableEl.cold.2
+ _ZN9Inspector37ObjCInspectorNetworkBackendDispatcher7disableEl.cold.2
+ _ZN9Inspector40ObjCInspectorDOMStorageBackendDispatcher17setDOMStorageItemElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEERKNS1_6StringESD_.cold.2
+ _ZN9Inspector40ObjCInspectorDOMStorageBackendDispatcher18getDOMStorageItemsElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE.cold.2
+ _ZN9Inspector40ObjCInspectorDOMStorageBackendDispatcher20clearDOMStorageItemsElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE.cold.2
+ _ZN9Inspector40ObjCInspectorDOMStorageBackendDispatcher20removeDOMStorageItemElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEERKNS1_6StringE.cold.2
+ _ZN9Inspector40ObjCInspectorDOMStorageBackendDispatcher6enableEl.cold.2
+ _ZN9Inspector40ObjCInspectorDOMStorageBackendDispatcher7disableEl.cold.2
+ _ZNK3WTF10RefCountedIN9Inspector14FrontendRouterEE5derefEv.cold.1
+ _ZNK3WTF10RefCountedIN9Inspector17BackendDispatcherEE5derefEv.cold.1
+ _ZNKSt3__114default_deleteIN9Inspector33ObjCInspectorCSSBackendDispatcherEEclB8sn190102EPS2_.cold.1
+ _ZNKSt3__114default_deleteIN9Inspector33ObjCInspectorDOMBackendDispatcherEEclB8sn190102EPS2_.cold.1
+ _ZNKSt3__114default_deleteIN9Inspector34ObjCInspectorPageBackendDispatcherEEclB8sn190102EPS2_.cold.1
+ _ZNKSt3__114default_deleteIN9Inspector37ObjCInspectorNetworkBackendDispatcherEEclB8sn190102EPS2_.cold.1
+ _ZNKSt3__114default_deleteIN9Inspector40ObjCInspectorDOMStorageBackendDispatcherEEclB8sn190102EPS2_.cold.1
+ _ZNSt3__111make_uniqueB8sn190102IN9Inspector26AlternateDispatchableAgentINS1_20CSSBackendDispatcherENS1_29AlternateCSSBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_33ObjCInspectorCSSBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_.cold.1
+ _ZNSt3__111make_uniqueB8sn190102IN9Inspector26AlternateDispatchableAgentINS1_20CSSBackendDispatcherENS1_29AlternateCSSBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_33ObjCInspectorCSSBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_.cold.2
+ _ZNSt3__111make_uniqueB8sn190102IN9Inspector26AlternateDispatchableAgentINS1_20DOMBackendDispatcherENS1_29AlternateDOMBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_33ObjCInspectorDOMBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_.cold.1
+ _ZNSt3__111make_uniqueB8sn190102IN9Inspector26AlternateDispatchableAgentINS1_20DOMBackendDispatcherENS1_29AlternateDOMBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_33ObjCInspectorDOMBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_.cold.2
+ _ZNSt3__111make_uniqueB8sn190102IN9Inspector26AlternateDispatchableAgentINS1_21PageBackendDispatcherENS1_30AlternatePageBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_34ObjCInspectorPageBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_.cold.1
+ _ZNSt3__111make_uniqueB8sn190102IN9Inspector26AlternateDispatchableAgentINS1_21PageBackendDispatcherENS1_30AlternatePageBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_34ObjCInspectorPageBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_.cold.2
+ _ZNSt3__111make_uniqueB8sn190102IN9Inspector26AlternateDispatchableAgentINS1_24NetworkBackendDispatcherENS1_33AlternateNetworkBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_37ObjCInspectorNetworkBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_.cold.1
+ _ZNSt3__111make_uniqueB8sn190102IN9Inspector26AlternateDispatchableAgentINS1_24NetworkBackendDispatcherENS1_33AlternateNetworkBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_37ObjCInspectorNetworkBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_.cold.2
+ _ZNSt3__111make_uniqueB8sn190102IN9Inspector26AlternateDispatchableAgentINS1_27DOMStorageBackendDispatcherENS1_36AlternateDOMStorageBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_40ObjCInspectorDOMStorageBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_.cold.1
+ _ZNSt3__111make_uniqueB8sn190102IN9Inspector26AlternateDispatchableAgentINS1_27DOMStorageBackendDispatcherENS1_36AlternateDOMStorageBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_40ObjCInspectorDOMStorageBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_.cold.2
+ __19-[RWIDevice unpair]_block_invoke.88
+ __39-[RWIDevice addMobileDeviceConnection:]_block_invoke.56
+ __39-[RWIDevice addMobileDeviceConnection:]_block_invoke.56.cold.1
+ __39-[RWIDevice addMobileDeviceConnection:]_block_invoke.56.cold.2
+ __39-[RWIDevice addMobileDeviceConnection:]_block_invoke.56.cold.3
+ __54-[RWIDevice _queueAttemptingPairWithProgressCallback:]_block_invoke.112
+ __54-[RWIDevice _queueAttemptingPairWithProgressCallback:]_block_invoke.116
+ __54-[RWIDevice _queueAttemptingPairWithProgressCallback:]_block_invoke_2.cold.1
+ __54-[RWIDevice _queueAttemptingPairWithProgressCallback:]_block_invoke_2.cold.2
+ __54-[RWIDevice _queueAttemptingPairWithProgressCallback:]_block_invoke_2.cold.3
+ __54-[RWIDevice _queueAttemptingPairWithProgressCallback:]_block_invoke_2.cold.4
+ __54-[RWIDevice _queueAttemptingPairWithProgressCallback:]_block_invoke_2.cold.5
+ __54-[RWIDevice _queueAttemptingPairWithProgressCallback:]_block_invoke_2.cold.6
+ __54-[RWIDevice _queueAttemptingPairWithProgressCallback:]_block_invoke_2.cold.7
+ __92-[RWIDevice _fetchDeviceInformationFromMobileDeviceConnection:shouldDelayServiceConnection:]_block_invoke.107
+ __92-[RWIDevice _fetchDeviceInformationFromMobileDeviceConnection:shouldDelayServiceConnection:]_block_invoke.110
+ __MergedGlobals
+ __ZN3WTF17HashMapTranslatorINS_7HashMapINS_6StringENS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEENS_11DefaultHashIS2_EENS_10HashTraitsIS2_EENSD_ISA_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE18KeyValuePairTraitsESC_E9translateIRKS2_NS_12KeyValuePairIS2_SA_EEZNSI_9inlineAddISN_NS3_INS4_10ObjectBaseENS6_ISR_EENS8_ISR_EEEEEENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS2_SP_NS_24KeyValuePairKeyExtractorISP_EESC_SJ_SE_LSH_0EEES2_SP_SZ_SC_SJ_SE_EEEEOT_OT0_EUlvE_EEvRS15_S14_RKT1_
+ __ZN3WTF17HashMapTranslatorINS_7HashMapINS_6StringENS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEENS_11DefaultHashIS2_EENS_10HashTraitsIS2_EENSD_ISA_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE18KeyValuePairTraitsESC_E9translateIRKS2_NS_12KeyValuePairIS2_SA_EEZNSI_9inlineAddISN_NS3_INS4_9ArrayBaseENS6_ISR_EENS8_ISR_EEEEEENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS2_SP_NS_24KeyValuePairKeyExtractorISP_EESC_SJ_SE_LSH_0EEES2_SP_SZ_SC_SJ_SE_EEEEOT_OT0_EUlvE_EEvRS15_S14_RKT1_
+ __ZN3WTF17HashMapTranslatorINS_7HashMapINS_6StringENS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEENS_11DefaultHashIS2_EENS_10HashTraitsIS2_EENSD_ISA_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE18KeyValuePairTraitsESC_E9translateIRKS2_NS_12KeyValuePairIS2_SA_EEZNSI_9inlineAddISN_SA_EENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS2_SP_NS_24KeyValuePairKeyExtractorISP_EESC_SJ_SE_LSH_0EEES2_SP_SV_SC_SJ_SE_EEEEOT_OT0_EUlvE_EEvRS11_S10_RKT1_
+ __ZN3WTF7HashMapINS_6StringENS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS4_EENS_21DefaultRefDerefTraitsIS4_EEEENS_11DefaultHashIS1_EENS_10HashTraitsIS1_EENSC_IS9_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE9inlineSetIRKS1_NS2_INS3_10ObjectBaseENS5_ISL_EENS7_ISL_EEEEEENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS1_NS_12KeyValuePairIS1_S9_EENS_24KeyValuePairKeyExtractorIST_EESB_NSH_18KeyValuePairTraitsESD_LSG_0EEES1_ST_SV_SB_SW_SD_EEEEOT_OT0_
+ __ZN3WTF7HashMapINS_6StringENS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS4_EENS_21DefaultRefDerefTraitsIS4_EEEENS_11DefaultHashIS1_EENS_10HashTraitsIS1_EENSC_IS9_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE9inlineSetIRKS1_NS2_INS3_9ArrayBaseENS5_ISL_EENS7_ISL_EEEEEENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS1_NS_12KeyValuePairIS1_S9_EENS_24KeyValuePairKeyExtractorIST_EESB_NSH_18KeyValuePairTraitsESD_LSG_0EEES1_ST_SV_SB_SW_SD_EEEEOT_OT0_
+ __ZN3WTF7HashMapINS_6StringENS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS4_EENS_21DefaultRefDerefTraitsIS4_EEEENS_11DefaultHashIS1_EENS_10HashTraitsIS1_EENSC_IS9_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE9inlineSetIRKS1_S9_EENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS1_NS_12KeyValuePairIS1_S9_EENS_24KeyValuePairKeyExtractorISP_EESB_NSH_18KeyValuePairTraitsESD_LSG_0EEES1_SP_SR_SB_SS_SD_EEEEOT_OT0_
+ __ZN3WTF9HashTableINS_6StringENS_12KeyValuePairIS1_NS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEEEENS_24KeyValuePairKeyExtractorISB_EENS_11DefaultHashIS1_EENS_7HashMapIS1_SA_SF_NS_10HashTraitsIS1_EENSH_ISA_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE18KeyValuePairTraitsESI_LSL_0EE17lookupForReinsertERKS1_
+ __ZN3WTF9HashTableINS_6StringENS_12KeyValuePairIS1_NS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEEEENS_24KeyValuePairKeyExtractorISB_EENS_11DefaultHashIS1_EENS_7HashMapIS1_SA_SF_NS_10HashTraitsIS1_EENSH_ISA_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE18KeyValuePairTraitsESI_LSL_0EE6expandEPSB_
+ __ZN3WTF9HashTableINS_6StringENS_12KeyValuePairIS1_NS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEEEENS_24KeyValuePairKeyExtractorISB_EENS_11DefaultHashIS1_EENS_7HashMapIS1_SA_SF_NS_10HashTraitsIS1_EENSH_ISA_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE18KeyValuePairTraitsESI_LSL_0EE6rehashEjPSB_
+ __ZN3WTF9HashTableINS_6StringENS_12KeyValuePairIS1_PN9Inspector29SupplementalBackendDispatcherEEENS_24KeyValuePairKeyExtractorIS6_EENS_11DefaultHashIS1_EENS_7HashMapIS1_S5_SA_NS_10HashTraitsIS1_EENSC_IS5_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE18KeyValuePairTraitsESD_LSG_0EE15deallocateTableEPS6_
+ __ZN9Inspector34ObjCInspectorPageBackendDispatcher9setCookieElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEEONSt3__18optionalIbEE
+ __ZNKSt3__114default_deleteIN9Inspector33ObjCInspectorCSSBackendDispatcherEEclB8sn190102EPS2_
+ __ZNKSt3__114default_deleteIN9Inspector33ObjCInspectorDOMBackendDispatcherEEclB8sn190102EPS2_
+ __ZNKSt3__114default_deleteIN9Inspector34ObjCInspectorPageBackendDispatcherEEclB8sn190102EPS2_
+ __ZNKSt3__114default_deleteIN9Inspector37ObjCInspectorNetworkBackendDispatcherEEclB8sn190102EPS2_
+ __ZNKSt3__114default_deleteIN9Inspector40ObjCInspectorDOMStorageBackendDispatcherEEclB8sn190102EPS2_
+ __ZNSt3__111make_uniqueB8sn190102IN9Inspector26AlternateDispatchableAgentINS1_20CSSBackendDispatcherENS1_29AlternateCSSBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_33ObjCInspectorCSSBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_
+ __ZNSt3__111make_uniqueB8sn190102IN9Inspector26AlternateDispatchableAgentINS1_20DOMBackendDispatcherENS1_29AlternateDOMBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_33ObjCInspectorDOMBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_
+ __ZNSt3__111make_uniqueB8sn190102IN9Inspector26AlternateDispatchableAgentINS1_21PageBackendDispatcherENS1_30AlternatePageBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_34ObjCInspectorPageBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_
+ __ZNSt3__111make_uniqueB8sn190102IN9Inspector26AlternateDispatchableAgentINS1_24NetworkBackendDispatcherENS1_33AlternateNetworkBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_37ObjCInspectorNetworkBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_
+ __ZNSt3__111make_uniqueB8sn190102IN9Inspector26AlternateDispatchableAgentINS1_27DOMStorageBackendDispatcherENS1_36AlternateDOMStorageBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_40ObjCInspectorDOMStorageBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_
+ __ZNSt3__122__libcpp_verbose_abortEPKcz
+ __ZNSt3__123__lower_bound_bisectingB8sn190102INS_17_ClassicAlgPolicyEPKNS_4pairIN3WTF28ComparableASCIISubsetLiteralILNS3_11ASCIISubsetE0EEE22RWIProtocolCSSPseudoIdEENS3_20ComparableStringViewENS_10__identityEZNKS3_14SortedArrayMapIA23_S8_E6tryGetINS3_6StringEEEPKS7_RKT_EUlRSK_RT0_E_EESO_SO_RKT1_NS_15iterator_traitsISO_E15difference_typeERT3_RT2_
+ __ZNSt3__127__throw_bad_optional_accessB8sn190102Ev
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8sn190102Em
+ __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B8sn190102Em
+ ___54-[RWIDevice _queueAttemptingPairWithProgressCallback:]_block_invoke_2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher12setStyleTextElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEERKNS1_6StringE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher12setStyleTextElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEERKNS1_6StringE_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher12setStyleTextElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEERKNS1_6StringE_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher12setStyleTextElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEERKNS1_6StringE_block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher13getStyleSheetElRKN3WTF6StringE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher13getStyleSheetElRKN3WTF6StringE_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher13getStyleSheetElRKN3WTF6StringE_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher13getStyleSheetElRKN3WTF6StringE_block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher15setRuleSelectorElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEERKNS1_6StringE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher15setRuleSelectorElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEERKNS1_6StringE_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher15setRuleSelectorElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEERKNS1_6StringE_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher15setRuleSelectorElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEERKNS1_6StringE_block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher16createStyleSheetElRKN3WTF6StringE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher16createStyleSheetElRKN3WTF6StringE_block_invoke_2.cold.1
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher16createStyleSheetElRKN3WTF6StringE_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher16createStyleSheetElRKN3WTF6StringE_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher16forcePseudoStateEliON3WTF3RefINS1_8JSONImpl5ArrayENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher17getAllStyleSheetsEl_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher17getAllStyleSheetsEl_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher17getAllStyleSheetsEl_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher17getAllStyleSheetsEl_block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher17getStyleSheetTextElRKN3WTF6StringE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher17getStyleSheetTextElRKN3WTF6StringE_block_invoke_2.cold.1
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher17getStyleSheetTextElRKN3WTF6StringE_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher17getStyleSheetTextElRKN3WTF6StringE_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher17setStyleSheetTextElRKN3WTF6StringES4__block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher18getFontDataForNodeEli_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher18getFontDataForNodeEli_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher18getFontDataForNodeEli_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher18getFontDataForNodeEli_block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher21setGroupingHeaderTextElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEERKNS1_6StringE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher21setGroupingHeaderTextElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEERKNS1_6StringE_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher21setGroupingHeaderTextElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEERKNS1_6StringE_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher21setGroupingHeaderTextElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEERKNS1_6StringE_block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher22getInlineStylesForNodeEli_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher22getInlineStylesForNodeEli_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher22getInlineStylesForNodeEli_block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher22getInlineStylesForNodeEli_block_invoke_2.cold.5
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher23getComputedStyleForNodeEli_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher23getComputedStyleForNodeEli_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher23getComputedStyleForNodeEli_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher23getComputedStyleForNodeEli_block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher23getMatchedStylesForNodeEliONSt3__18optionalIbEES4__block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher23getMatchedStylesForNodeEliONSt3__18optionalIbEES4__block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher23getMatchedStylesForNodeEliONSt3__18optionalIbEES4__block_invoke_2.cold.5
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher23getMatchedStylesForNodeEliONSt3__18optionalIbEES4__block_invoke_2.cold.6
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher23getMatchedStylesForNodeEliONSt3__18optionalIbEES4__block_invoke_2.cold.7
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher25getSupportedCSSPropertiesEl_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher25getSupportedCSSPropertiesEl_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher25getSupportedCSSPropertiesEl_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher25getSupportedCSSPropertiesEl_block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher31setLayoutContextTypeChangedModeElRKN3WTF6StringE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher33getSupportedSystemFontFamilyNamesEl_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher33getSupportedSystemFontFamilyNamesEl_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher33getSupportedSystemFontFamilyNamesEl_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher33getSupportedSystemFontFamilyNamesEl_block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher6enableEl_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher7addRuleElRKN3WTF6StringES4__block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher7addRuleElRKN3WTF6StringES4__block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher7addRuleElRKN3WTF6StringES4__block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher7addRuleElRKN3WTF6StringES4__block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorCSSBackendDispatcher7disableEl_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher10removeNodeEli_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher11getDocumentEl_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher11getDocumentEl_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher11getDocumentEl_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher11getDocumentEl_block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher11requestNodeElRKN3WTF6StringE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher11requestNodeElRKN3WTF6StringE_block_invoke_2.cold.1
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher11requestNodeElRKN3WTF6StringE_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher11requestNodeElRKN3WTF6StringE_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher11resolveNodeEliRKN3WTF6StringE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher11resolveNodeEliRKN3WTF6StringE_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher11resolveNodeEliRKN3WTF6StringE_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher11resolveNodeEliRKN3WTF6StringE_block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher11setNodeNameEliRKN3WTF6StringE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher11setNodeNameEliRKN3WTF6StringE_block_invoke_2.cold.1
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher11setNodeNameEliRKN3WTF6StringE_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher11setNodeNameEliRKN3WTF6StringE_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher12getOuterHTMLEli_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher12getOuterHTMLEli_block_invoke_2.cold.1
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher12getOuterHTMLEli_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher12getOuterHTMLEli_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher12setNodeValueEliRKN3WTF6StringE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher12setOuterHTMLEliRKN3WTF6StringE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher13getAttributesEli_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher13getAttributesEli_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher13getAttributesEli_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher13getAttributesEli_block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher13getMediaStatsEli_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher13getMediaStatsEli_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher13getMediaStatsEli_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher13getMediaStatsEli_block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher13hideHighlightEl_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher13highlightNodeElONSt3__18optionalIiEERKN3WTF6StringEONS5_3RefINS5_8JSONImpl6ObjectENS5_12RawPtrTraitsISB_EENS5_21DefaultRefDerefTraitsISB_EEEEONS5_6RefPtrISB_SD_SF_EESK_ONS2_IbEE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher13highlightQuadElON3WTF3RefINS1_8JSONImpl5ArrayENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEEONS1_6RefPtrINS3_6ObjectENS5_ISC_EENS7_ISC_EEEESG_ONSt3__18optionalIbEE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher13highlightRectEliiiiON3WTF6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEESA_ONSt3__18optionalIbEE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher13performSearchElRKN3WTF6StringEONS1_6RefPtrINS1_8JSONImpl5ArrayENS1_12RawPtrTraitsIS7_EENS1_21DefaultRefDerefTraitsIS7_EEEEONSt3__18optionalIbEE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher13performSearchElRKN3WTF6StringEONS1_6RefPtrINS1_8JSONImpl5ArrayENS1_12RawPtrTraitsIS7_EENS1_21DefaultRefDerefTraitsIS7_EEEEONSt3__18optionalIbEE_block_invoke_2.cold.1
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher13performSearchElRKN3WTF6StringEONS1_6RefPtrINS1_8JSONImpl5ArrayENS1_12RawPtrTraitsIS7_EENS1_21DefaultRefDerefTraitsIS7_EEEEONSt3__18optionalIbEE_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher13performSearchElRKN3WTF6StringEONS1_6RefPtrINS1_8JSONImpl5ArrayENS1_12RawPtrTraitsIS7_EENS1_21DefaultRefDerefTraitsIS7_EEEEONSt3__18optionalIbEE_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher13performSearchElRKN3WTF6StringEONS1_6RefPtrINS1_8JSONImpl5ArrayENS1_12RawPtrTraitsIS7_EENS1_21DefaultRefDerefTraitsIS7_EEEEONSt3__18optionalIbEE_block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher13querySelectorEliRKN3WTF6StringE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher13querySelectorEliRKN3WTF6StringE_block_invoke_2.cold.1
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher13querySelectorEliRKN3WTF6StringE_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher14highlightFrameElRKN3WTF6StringEONS1_6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS7_EENS1_21DefaultRefDerefTraitsIS7_EEEESD__block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher15hideFlexOverlayElONSt3__18optionalIiEE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher15hideGridOverlayElONSt3__18optionalIiEE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher15removeAttributeEliRKN3WTF6StringE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher15showFlexOverlayEliON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher15showGridOverlayEliON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher16getSearchResultsElRKN3WTF6StringEii_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher16getSearchResultsElRKN3WTF6StringEii_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher16getSearchResultsElRKN3WTF6StringEii_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher16getSearchResultsElRKN3WTF6StringEii_block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher16querySelectorAllEliRKN3WTF6StringE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher16querySelectorAllEliRKN3WTF6StringE_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher16querySelectorAllEliRKN3WTF6StringE_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher16querySelectorAllEliRKN3WTF6StringE_block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher16setInspectedNodeEli_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher17highlightNodeListElON3WTF3RefINS1_8JSONImpl5ArrayENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEEONS2_INS3_6ObjectENS5_ISB_EENS7_ISB_EEEEONS1_6RefPtrISB_SC_SD_EESI_ONSt3__18optionalIbEE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher17highlightSelectorElRKN3WTF6StringES4_ONS1_3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS7_EENS1_21DefaultRefDerefTraitsIS7_EEEEONS1_6RefPtrIS7_S9_SB_EESG_ONSt3__18optionalIbEE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher17markUndoableStateEl_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher17requestChildNodesEliONSt3__18optionalIiEE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher17setAttributeValueEliRKN3WTF6StringES4__block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher18insertAdjacentHTMLEliRKN3WTF6StringES4__block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher19setAttributesAsTextEliRKN3WTF6StringES4__block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher20discardSearchResultsElRKN3WTF6StringE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher21setInspectModeEnabledElbON3WTF6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEESA_SA_ONSt3__18optionalIbEE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher22getDataBindingsForNodeEli_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher22getDataBindingsForNodeEli_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher22getDataBindingsForNodeEli_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher22getDataBindingsForNodeEli_block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher22getSupportedEventNamesEl_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher22getSupportedEventNamesEl_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher22getSupportedEventNamesEl_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher22getSupportedEventNamesEl_block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher24getAssociatedDataForNodeEli_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher24getAssociatedDataForNodeEli_block_invoke_2.cold.1
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher24getAssociatedDataForNodeEli_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher24getEventListenersForNodeEliONSt3__18optionalIbEE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher24getEventListenersForNodeEliONSt3__18optionalIbEE_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher24getEventListenersForNodeEliONSt3__18optionalIbEE_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher24getEventListenersForNodeEliONSt3__18optionalIbEE_block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher24pushNodeByPathToFrontendElRKN3WTF6StringE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher24pushNodeByPathToFrontendElRKN3WTF6StringE_block_invoke_2.cold.1
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher24pushNodeByPathToFrontendElRKN3WTF6StringE_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher24pushNodeByPathToFrontendElRKN3WTF6StringE_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher24setEventListenerDisabledElib_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher29setBreakpointForEventListenerEliON3WTF6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher32removeBreakpointForEventListenerEli_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher33getAccessibilityPropertiesForNodeEli_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher33getAccessibilityPropertiesForNodeEli_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher33getAccessibilityPropertiesForNodeEli_block_invoke_2.cold.3
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher33getAccessibilityPropertiesForNodeEli_block_invoke_2.cold.4
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher35setAllowEditingUserAgentShadowTreesElb_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher4redoEl_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher4undoEl_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher5focusEli_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher6moveToEliiONSt3__18optionalIiEE_block_invoke.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher6moveToEliiONSt3__18optionalIiEE_block_invoke_2.cold.1
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher6moveToEliiONSt3__18optionalIiEE_block_invoke_2.cold.2
+ ___ZN9Inspector33ObjCInspectorDOMBackendDispatcher6moveToEliiONSt3__18optionalIiEE_block_invoke_2.cold.3
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher10getCookiesEl_block_invoke.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher10getCookiesEl_block_invoke_2.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher10getCookiesEl_block_invoke_2.cold.3
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher10getCookiesEl_block_invoke_2.cold.4
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher12deleteCookieElRKN3WTF6StringES4__block_invoke.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher12snapshotNodeEli_block_invoke.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher12snapshotNodeEli_block_invoke_2.cold.1
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher12snapshotNodeEli_block_invoke_2.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher12snapshotNodeEli_block_invoke_2.cold.3
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher12snapshotRectEliiiiRKN3WTF6StringE_block_invoke.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher12snapshotRectEliiiiRKN3WTF6StringE_block_invoke_2.cold.1
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher12snapshotRectEliiiiRKN3WTF6StringE_block_invoke_2.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher12snapshotRectEliiiiRKN3WTF6StringE_block_invoke_2.cold.3
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher13setShowRulersElb_block_invoke.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher15getResourceTreeEl_block_invoke.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher15getResourceTreeEl_block_invoke_2.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher15getResourceTreeEl_block_invoke_2.cold.3
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher15getResourceTreeEl_block_invoke_2.cold.4
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher15overrideSettingElRKN3WTF6StringEONSt3__18optionalIbEE_block_invoke.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher16searchInResourceElRKN3WTF6StringES4_S4_ONSt3__18optionalIbEES8_S4__block_invoke.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher16searchInResourceElRKN3WTF6StringES4_S4_ONSt3__18optionalIbEES8_S4__block_invoke_2.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher16searchInResourceElRKN3WTF6StringES4_S4_ONSt3__18optionalIbEES8_S4__block_invoke_2.cold.3
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher16searchInResourceElRKN3WTF6StringES4_S4_ONSt3__18optionalIbEES8_S4__block_invoke_2.cold.4
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher16setEmulatedMediaElRKN3WTF6StringE_block_invoke.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher17overrideUserAgentElRKN3WTF6StringE_block_invoke.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher17searchInResourcesElRKN3WTF6StringEONSt3__18optionalIbEES8__block_invoke.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher17searchInResourcesElRKN3WTF6StringEONSt3__18optionalIbEES8__block_invoke_2.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher17searchInResourcesElRKN3WTF6StringEONSt3__18optionalIbEES8__block_invoke_2.cold.3
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher17searchInResourcesElRKN3WTF6StringEONSt3__18optionalIbEES8__block_invoke_2.cold.4
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher17setShowPaintRectsElb_block_invoke.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher18getResourceContentElRKN3WTF6StringES4__block_invoke.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher18getResourceContentElRKN3WTF6StringES4__block_invoke_2.cold.1
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher18getResourceContentElRKN3WTF6StringES4__block_invoke_2.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher18getResourceContentElRKN3WTF6StringES4__block_invoke_2.cold.3
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher18getResourceContentElRKN3WTF6StringES4__block_invoke_2.cold.4
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher18setBootstrapScriptElRKN3WTF6StringE_block_invoke.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher22overrideUserPreferenceElRKN3WTF6StringES4__block_invoke.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher6enableEl_block_invoke.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher6reloadElONSt3__18optionalIbEES4__block_invoke.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher7archiveEl_block_invoke.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher7archiveEl_block_invoke_2.cold.1
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher7archiveEl_block_invoke_2.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher7archiveEl_block_invoke_2.cold.3
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher7disableEl_block_invoke.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher8navigateElRKN3WTF6StringE_block_invoke.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher9setCookieElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEEONSt3__18optionalIbEE_block_invoke.cold.1
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher9setCookieElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEEONSt3__18optionalIbEE_block_invoke.cold.2
+ ___ZN9Inspector34ObjCInspectorPageBackendDispatcher9setCookieElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEEONSt3__18optionalIbEE_block_invoke_2.cold.1
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher12loadResourceElRKN3WTF6StringES4__block_invoke.cold.2
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher12loadResourceElRKN3WTF6StringES4__block_invoke_2.cold.1
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher12loadResourceElRKN3WTF6StringES4__block_invoke_2.cold.2
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher12loadResourceElRKN3WTF6StringES4__block_invoke_2.cold.3
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher12loadResourceElRKN3WTF6StringES4__block_invoke_2.cold.4
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher12loadResourceElRKN3WTF6StringES4__block_invoke_2.cold.5
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher15addInterceptionElRKN3WTF6StringES4_ONSt3__18optionalIbEES8__block_invoke.cold.2
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher15getResponseBodyElRKN3WTF6StringE_block_invoke.cold.2
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher15getResponseBodyElRKN3WTF6StringE_block_invoke_2.cold.1
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher15getResponseBodyElRKN3WTF6StringE_block_invoke_2.cold.2
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher15getResponseBodyElRKN3WTF6StringE_block_invoke_2.cold.3
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher15getResponseBodyElRKN3WTF6StringE_block_invoke_2.cold.4
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher16resolveWebSocketElRKN3WTF6StringES4__block_invoke.cold.2
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher16resolveWebSocketElRKN3WTF6StringES4__block_invoke_2.cold.2
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher16resolveWebSocketElRKN3WTF6StringES4__block_invoke_2.cold.3
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher16resolveWebSocketElRKN3WTF6StringES4__block_invoke_2.cold.4
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher17interceptContinueElRKN3WTF6StringES4__block_invoke.cold.2
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher18removeInterceptionElRKN3WTF6StringES4_ONSt3__18optionalIbEES8__block_invoke.cold.2
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher19setExtraHTTPHeadersElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE_block_invoke.cold.2
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher20interceptWithRequestElRKN3WTF6StringES4_S4_ONS1_6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS7_EENS1_21DefaultRefDerefTraitsIS7_EEEES4__block_invoke.cold.2
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher21interceptWithResponseElRKN3WTF6StringES4_bS4_ONSt3__18optionalIiEES4_ONS1_6RefPtrINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsISB_EENS1_21DefaultRefDerefTraitsISB_EEEE_block_invoke.cold.2
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher22setInterceptionEnabledElb_block_invoke.cold.2
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher24getSerializedCertificateElRKN3WTF6StringE_block_invoke.cold.2
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher24getSerializedCertificateElRKN3WTF6StringE_block_invoke_2.cold.1
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher24getSerializedCertificateElRKN3WTF6StringE_block_invoke_2.cold.2
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher24getSerializedCertificateElRKN3WTF6StringE_block_invoke_2.cold.3
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher25interceptRequestWithErrorElRKN3WTF6StringES4__block_invoke.cold.2
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher26setResourceCachingDisabledElb_block_invoke.cold.2
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher28interceptRequestWithResponseElRKN3WTF6StringES4_bS4_iS4_ONS1_3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS7_EENS1_21DefaultRefDerefTraitsIS7_EEEE_block_invoke.cold.2
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher6enableEl_block_invoke.cold.2
+ ___ZN9Inspector37ObjCInspectorNetworkBackendDispatcher7disableEl_block_invoke.cold.2
+ ___ZN9Inspector40ObjCInspectorDOMStorageBackendDispatcher17setDOMStorageItemElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEERKNS1_6StringESD__block_invoke.cold.2
+ ___ZN9Inspector40ObjCInspectorDOMStorageBackendDispatcher18getDOMStorageItemsElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE_block_invoke.cold.2
+ ___ZN9Inspector40ObjCInspectorDOMStorageBackendDispatcher18getDOMStorageItemsElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE_block_invoke_2.cold.2
+ ___ZN9Inspector40ObjCInspectorDOMStorageBackendDispatcher18getDOMStorageItemsElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE_block_invoke_2.cold.3
+ ___ZN9Inspector40ObjCInspectorDOMStorageBackendDispatcher18getDOMStorageItemsElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE_block_invoke_2.cold.4
+ ___ZN9Inspector40ObjCInspectorDOMStorageBackendDispatcher20clearDOMStorageItemsElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE_block_invoke.cold.2
+ ___ZN9Inspector40ObjCInspectorDOMStorageBackendDispatcher20removeDOMStorageItemElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEERKNS1_6StringE_block_invoke.cold.2
+ ___ZN9Inspector40ObjCInspectorDOMStorageBackendDispatcher6enableEl_block_invoke.cold.2
+ ___ZN9Inspector40ObjCInspectorDOMStorageBackendDispatcher7disableEl_block_invoke.cold.2
+ ____ZN9Inspector34ObjCInspectorPageBackendDispatcher9setCookieElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEEONSt3__18optionalIbEE_block_invoke
+ ____ZN9Inspector34ObjCInspectorPageBackendDispatcher9setCookieElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEEONSt3__18optionalIbEE_block_invoke_2
+ ___block_descriptor_48_ea8_32s40s_e5_B8?0l
+ _objc_msgSend$_copyRemoteInspectionEnabledValueFromDevice:
+ _objc_msgSend$_copyWirelessEnabledValueFromDevice:
+ _objc_msgSend$driverBidiPort
+ _objc_msgSend$setCookieWithErrorCallback:successCallback:cookie:shouldPartition:
+ _objc_msgSend$setDriverBidiPort:
+ canLoadCoreSimulator.cold.1
+ canLoadMobileDevice.cold.1
+ iconForDevice.cold.1
+ isInternalInstall.cold.1
+ isSimulatingCustomerInstall.cold.1
- GCC_except_table780
- GCC_except_table781
- GCC_except_table784
- GCC_except_table790
- GCC_except_table798
- GCC_except_table801
- GCC_except_table805
- GCC_except_table814
- GCC_except_table815
- GCC_except_table822
- GCC_except_table825
- GCC_except_table828
- GCC_except_table834
- GCC_except_table839
- GCC_except_table844
- GCC_except_table849
- GCC_except_table853
- GCC_except_table857
- GCC_except_table869
- GCC_except_table874
- GCC_except_table878
- GCC_except_table883
- GCC_except_table886
- GCC_except_table887
- GCC_except_table892
- GCC_except_table897
- GCC_except_table898
- GCC_except_table904
- GCC_except_table907
- GCC_except_table928
- GCC_except_table934
- GCC_except_table935
- GCC_except_table940
- GCC_except_table947
- GCC_except_table966
- GCC_except_table967
- _ZN9Inspector34ObjCInspectorPageBackendDispatcher9setCookieElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE.cold.1
- _ZNSt3__111make_uniqueB8sn180100IN9Inspector26AlternateDispatchableAgentINS1_20CSSBackendDispatcherENS1_29AlternateCSSBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_33ObjCInspectorCSSBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_.cold.1
- _ZNSt3__111make_uniqueB8sn180100IN9Inspector26AlternateDispatchableAgentINS1_20DOMBackendDispatcherENS1_29AlternateDOMBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_33ObjCInspectorDOMBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_.cold.1
- _ZNSt3__111make_uniqueB8sn180100IN9Inspector26AlternateDispatchableAgentINS1_21PageBackendDispatcherENS1_30AlternatePageBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_34ObjCInspectorPageBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_.cold.1
- _ZNSt3__111make_uniqueB8sn180100IN9Inspector26AlternateDispatchableAgentINS1_24NetworkBackendDispatcherENS1_33AlternateNetworkBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_37ObjCInspectorNetworkBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_.cold.1
- _ZNSt3__111make_uniqueB8sn180100IN9Inspector26AlternateDispatchableAgentINS1_27DOMStorageBackendDispatcherENS1_36AlternateDOMStorageBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_40ObjCInspectorDOMStorageBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_.cold.1
- __19-[RWIDevice unpair]_block_invoke.84
- __54-[RWIDevice _queueAttemptingPairWithProgressCallback:]_block_invoke.107
- __54-[RWIDevice _queueAttemptingPairWithProgressCallback:]_block_invoke.109
- __54-[RWIDevice _queueAttemptingPairWithProgressCallback:]_block_invoke.109.cold.1
- __54-[RWIDevice _queueAttemptingPairWithProgressCallback:]_block_invoke.109.cold.2
- __54-[RWIDevice _queueAttemptingPairWithProgressCallback:]_block_invoke.109.cold.3
- __54-[RWIDevice _queueAttemptingPairWithProgressCallback:]_block_invoke.109.cold.4
- __54-[RWIDevice _queueAttemptingPairWithProgressCallback:]_block_invoke.109.cold.5
- __54-[RWIDevice _queueAttemptingPairWithProgressCallback:]_block_invoke.109.cold.6
- __54-[RWIDevice _queueAttemptingPairWithProgressCallback:]_block_invoke.109.cold.7
- __54-[RWIDevice _queueAttemptingPairWithProgressCallback:]_block_invoke.113
- __92-[RWIDevice _fetchDeviceInformationFromMobileDeviceConnection:shouldDelayServiceConnection:]_block_invoke.105
- __ZGVZ19canLoadMobileDeviceE6loaded
- __ZGVZ20canLoadCoreSimulatorE6loaded
- __ZGVZ21canLoadAMDeviceUnpairE6loaded
- __ZGVZ22canLoadAMDeviceConnectE6loaded
- __ZGVZ22canLoadAMDeviceIsValidE6loaded
- __ZGVZ23canLoadAMDCopyErrorTextE6loaded
- __ZGVZ23canLoadAMDeviceSetValueE6loaded
- __ZGVZ25canLoadAMDeviceDisconnectE6loaded
- __ZGVZ26canLoadAMDGetBundleVersionE6loaded
- __ZGVZ26canLoadAMDeviceRemoveValueE6loaded
- __ZGVZ26canLoadAMDeviceStopSessionE6loaded
- __ZGVZ27canLoadAMDeviceStartSessionE6loaded
- __ZGVZ30canLoadAMDeviceValidatePairingE6loaded
- __ZGVZ31canLoadAMDServiceConnectionSendE6loaded
- __ZGVZ31canLoadAMDeviceGetInterfaceTypeE6loaded
- __ZGVZ32canLoadAMDeviceIsWiFiPairableRefE6loaded
- __ZGVZ33canLoadAMDeviceCopyValueWithErrorE6loaded
- __ZGVZ33canLoadAMDeviceSecureStartServiceE6loaded
- __ZGVZ34canLoadAMDServiceConnectionReceiveE6loaded
- __ZGVZ35canLoadAMDSecureObserveNotificationE6loaded
- __ZGVZ35canLoadAMDeviceCopyDeviceIdentifierE6loaded
- __ZGVZ36canLoadAMDServiceConnectionGetSocketE6loaded
- __ZGVZ37canLoadAMDServiceConnectionInvalidateE6loaded
- __ZGVZ38canLoadAMDeviceNotificationUnsubscribeE6loaded
- __ZGVZ41canLoadAMDSecureShutdownNotificationProxyE6loaded
- __ZGVZ41canLoadAMDeviceCopyBonjourFullServiceNameE6loaded
- __ZGVZ45canLoadAMDeviceDeleteHostPairingRecordForUDIDE6loaded
- __ZGVZ47canLoadAMDeviceCopyWirelessDeviceValueWithErrorE6loaded
- __ZGVZ47canLoadAMDeviceNotificationSubscribeWithOptionsE6loaded
- __ZGVZ49canLoadAMDeviceWiFiPairableCopyRealUniqueDeviceIDE6loaded
- __ZGVZ57canLoadAMDSecureListenForNotificationsWithRetainedContextE6loaded
- __ZGVZL21MobileDeviceFrameworkvE7library
- __ZN3WTF17HashMapTranslatorINS_7HashMapINS_6StringENS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEENS_11DefaultHashIS2_EENS_10HashTraitsIS2_EENSD_ISA_EENS_15HashTableTraitsEE18KeyValuePairTraitsESC_E9translateIRKS2_NS_12KeyValuePairIS2_SA_EEZNSH_9inlineAddISM_NS3_INS4_10ObjectBaseENS6_ISQ_EENS8_ISQ_EEEEEENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS2_SO_NS_24KeyValuePairKeyExtractorISO_EESC_SI_SE_EES2_SO_SY_SC_SI_SE_EEEEOT_OT0_EUlvE_EEvRS14_S13_RKT1_
- __ZN3WTF17HashMapTranslatorINS_7HashMapINS_6StringENS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEENS_11DefaultHashIS2_EENS_10HashTraitsIS2_EENSD_ISA_EENS_15HashTableTraitsEE18KeyValuePairTraitsESC_E9translateIRKS2_NS_12KeyValuePairIS2_SA_EEZNSH_9inlineAddISM_NS3_INS4_9ArrayBaseENS6_ISQ_EENS8_ISQ_EEEEEENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS2_SO_NS_24KeyValuePairKeyExtractorISO_EESC_SI_SE_EES2_SO_SY_SC_SI_SE_EEEEOT_OT0_EUlvE_EEvRS14_S13_RKT1_
- __ZN3WTF17HashMapTranslatorINS_7HashMapINS_6StringENS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEENS_11DefaultHashIS2_EENS_10HashTraitsIS2_EENSD_ISA_EENS_15HashTableTraitsEE18KeyValuePairTraitsESC_E9translateIRKS2_NS_12KeyValuePairIS2_SA_EEZNSH_9inlineAddISM_SA_EENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS2_SO_NS_24KeyValuePairKeyExtractorISO_EESC_SI_SE_EES2_SO_SU_SC_SI_SE_EEEEOT_OT0_EUlvE_EEvRS10_SZ_RKT1_
- __ZN3WTF7HashMapINS_6StringENS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS4_EENS_21DefaultRefDerefTraitsIS4_EEEENS_11DefaultHashIS1_EENS_10HashTraitsIS1_EENSC_IS9_EENS_15HashTableTraitsEE9inlineSetIRKS1_NS2_INS3_10ObjectBaseENS5_ISK_EENS7_ISK_EEEEEENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS1_NS_12KeyValuePairIS1_S9_EENS_24KeyValuePairKeyExtractorISS_EESB_NSG_18KeyValuePairTraitsESD_EES1_SS_SU_SB_SV_SD_EEEEOT_OT0_
- __ZN3WTF7HashMapINS_6StringENS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS4_EENS_21DefaultRefDerefTraitsIS4_EEEENS_11DefaultHashIS1_EENS_10HashTraitsIS1_EENSC_IS9_EENS_15HashTableTraitsEE9inlineSetIRKS1_NS2_INS3_9ArrayBaseENS5_ISK_EENS7_ISK_EEEEEENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS1_NS_12KeyValuePairIS1_S9_EENS_24KeyValuePairKeyExtractorISS_EESB_NSG_18KeyValuePairTraitsESD_EES1_SS_SU_SB_SV_SD_EEEEOT_OT0_
- __ZN3WTF7HashMapINS_6StringENS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS4_EENS_21DefaultRefDerefTraitsIS4_EEEENS_11DefaultHashIS1_EENS_10HashTraitsIS1_EENSC_IS9_EENS_15HashTableTraitsEE9inlineSetIRKS1_S9_EENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS1_NS_12KeyValuePairIS1_S9_EENS_24KeyValuePairKeyExtractorISO_EESB_NSG_18KeyValuePairTraitsESD_EES1_SO_SQ_SB_SR_SD_EEEEOT_OT0_
- __ZN3WTF9HashTableINS_6StringENS_12KeyValuePairIS1_NS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEEEENS_24KeyValuePairKeyExtractorISB_EENS_11DefaultHashIS1_EENS_7HashMapIS1_SA_SF_NS_10HashTraitsIS1_EENSH_ISA_EENS_15HashTableTraitsEE18KeyValuePairTraitsESI_E17lookupForReinsertERKS1_
- __ZN3WTF9HashTableINS_6StringENS_12KeyValuePairIS1_NS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEEEENS_24KeyValuePairKeyExtractorISB_EENS_11DefaultHashIS1_EENS_7HashMapIS1_SA_SF_NS_10HashTraitsIS1_EENSH_ISA_EENS_15HashTableTraitsEE18KeyValuePairTraitsESI_E6expandEPSB_
- __ZN3WTF9HashTableINS_6StringENS_12KeyValuePairIS1_NS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEEEENS_24KeyValuePairKeyExtractorISB_EENS_11DefaultHashIS1_EENS_7HashMapIS1_SA_SF_NS_10HashTraitsIS1_EENSH_ISA_EENS_15HashTableTraitsEE18KeyValuePairTraitsESI_E6rehashEjPSB_
- __ZN3WTF9HashTableINS_6StringENS_12KeyValuePairIS1_PN9Inspector29SupplementalBackendDispatcherEEENS_24KeyValuePairKeyExtractorIS6_EENS_11DefaultHashIS1_EENS_7HashMapIS1_S5_SA_NS_10HashTraitsIS1_EENSC_IS5_EENS_15HashTableTraitsEE18KeyValuePairTraitsESD_E15deallocateTableEPS6_
- __ZN9Inspector34ObjCInspectorPageBackendDispatcher9setCookieElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE
- __ZNKSt3__114default_deleteIN9Inspector33ObjCInspectorCSSBackendDispatcherEEclB8sn180100EPS2_
- __ZNKSt3__114default_deleteIN9Inspector33ObjCInspectorDOMBackendDispatcherEEclB8sn180100EPS2_
- __ZNKSt3__114default_deleteIN9Inspector34ObjCInspectorPageBackendDispatcherEEclB8sn180100EPS2_
- __ZNKSt3__114default_deleteIN9Inspector37ObjCInspectorNetworkBackendDispatcherEEclB8sn180100EPS2_
- __ZNKSt3__114default_deleteIN9Inspector40ObjCInspectorDOMStorageBackendDispatcherEEclB8sn180100EPS2_
- __ZNSt3__111make_uniqueB8sn180100IN9Inspector26AlternateDispatchableAgentINS1_20CSSBackendDispatcherENS1_29AlternateCSSBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_33ObjCInspectorCSSBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_
- __ZNSt3__111make_uniqueB8sn180100IN9Inspector26AlternateDispatchableAgentINS1_20DOMBackendDispatcherENS1_29AlternateDOMBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_33ObjCInspectorDOMBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_
- __ZNSt3__111make_uniqueB8sn180100IN9Inspector26AlternateDispatchableAgentINS1_21PageBackendDispatcherENS1_30AlternatePageBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_34ObjCInspectorPageBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_
- __ZNSt3__111make_uniqueB8sn180100IN9Inspector26AlternateDispatchableAgentINS1_24NetworkBackendDispatcherENS1_33AlternateNetworkBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_37ObjCInspectorNetworkBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_
- __ZNSt3__111make_uniqueB8sn180100IN9Inspector26AlternateDispatchableAgentINS1_27DOMStorageBackendDispatcherENS1_36AlternateDOMStorageBackendDispatcherEEEJN3WTF12ASCIILiteralERNS1_30AugmentableInspectorControllerENS_10unique_ptrINS1_40ObjCInspectorDOMStorageBackendDispatcherENS_14default_deleteISB_EEEEEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_
- __ZNSt3__113__lower_boundB8sn180100INS_17_ClassicAlgPolicyEPKNS_4pairIN3WTF28ComparableASCIISubsetLiteralILNS3_11ASCIISubsetE0EEE22RWIProtocolCSSPseudoIdEESA_NS3_20ComparableStringViewENS_10__identityEZNKS3_14SortedArrayMapIA23_S8_E6tryGetINS3_6StringEEEPKS7_RKT_EUlRSK_RT0_E_EESO_SO_T1_RKT2_RT4_RT3_
- __ZNSt3__127__throw_bad_optional_accessB8sn180100Ev
- __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8sn180100Em
- __ZNSt3__16vectorIhNS_9allocatorIhEEEC2Em
- __ZZ19canLoadMobileDeviceE6loaded
- __ZZ20canLoadCoreSimulatorE6loaded
- __ZZ21canLoadAMDeviceUnpairE6loaded
- __ZZ22canLoadAMDeviceConnectE6loaded
- __ZZ22canLoadAMDeviceIsValidE6loaded
- __ZZ23canLoadAMDCopyErrorTextE6loaded
- __ZZ23canLoadAMDeviceSetValueE6loaded
- __ZZ25canLoadAMDeviceDisconnectE6loaded
- __ZZ26canLoadAMDGetBundleVersionE6loaded
- __ZZ26canLoadAMDeviceRemoveValueE6loaded
- __ZZ26canLoadAMDeviceStopSessionE6loaded
- __ZZ27canLoadAMDeviceStartSessionE6loaded
- __ZZ30canLoadAMDeviceValidatePairingE6loaded
- __ZZ31canLoadAMDServiceConnectionSendE6loaded
- __ZZ31canLoadAMDeviceGetInterfaceTypeE6loaded
- __ZZ32canLoadAMDeviceIsWiFiPairableRefE6loaded
- __ZZ33canLoadAMDeviceCopyValueWithErrorE6loaded
- __ZZ33canLoadAMDeviceSecureStartServiceE6loaded
- __ZZ34canLoadAMDServiceConnectionReceiveE6loaded
- __ZZ35canLoadAMDSecureObserveNotificationE6loaded
- __ZZ35canLoadAMDeviceCopyDeviceIdentifierE6loaded
- __ZZ36canLoadAMDServiceConnectionGetSocketE6loaded
- __ZZ37canLoadAMDServiceConnectionInvalidateE6loaded
- __ZZ38canLoadAMDeviceNotificationUnsubscribeE6loaded
- __ZZ41canLoadAMDSecureShutdownNotificationProxyE6loaded
- __ZZ41canLoadAMDeviceCopyBonjourFullServiceNameE6loaded
- __ZZ45canLoadAMDeviceDeleteHostPairingRecordForUDIDE6loaded
- __ZZ47canLoadAMDeviceCopyWirelessDeviceValueWithErrorE6loaded
- __ZZ47canLoadAMDeviceNotificationSubscribeWithOptionsE6loaded
- __ZZ49canLoadAMDeviceWiFiPairableCopyRealUniqueDeviceIDE6loaded
- __ZZ57canLoadAMDSecureListenForNotificationsWithRetainedContextE6loaded
- __ZZL21MobileDeviceFrameworkvE7library
- __ZZL22CoreSimulatorFrameworkvE4once
- __ZZL22CoreSimulatorFrameworkvE7library
- ___92-[RWIDevice _fetchDeviceInformationFromMobileDeviceConnection:shouldDelayServiceConnection:]_block_invoke_2
- ___ZN9Inspector34ObjCInspectorPageBackendDispatcher9setCookieElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE_block_invoke.cold.1
- ___ZN9Inspector34ObjCInspectorPageBackendDispatcher9setCookieElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE_block_invoke_2.cold.1
- ____ZN9Inspector34ObjCInspectorPageBackendDispatcher9setCookieElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE_block_invoke
- ____ZN9Inspector34ObjCInspectorPageBackendDispatcher9setCookieElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEE_block_invoke_2
- _objc_msgSend$setCookieWithErrorCallback:successCallback:cookie:
CStrings:
+ "%@ (%{public}@) creating service connection immediately to fetch device information"
+ "%@ (%{public}@) delaying creation of service connection: 'Allow Web Inspector' preference disabled"
+ "%@ (%{public}@) delaying creation of service connection: can cheaply read all basic information"
+ "%@ (%{public}@) will fetch device information; shouldDelayServiceConnection = %s"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/wtf/JSONValues.h"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/wtf/RefCounted.h"
+ "23A"
+ "23J"
+ "23M"
+ "23R"
+ "25A"
+ "B8@?0"
+ "Tq,N,V_driverBidiPort"
+ "WIRDriverBidiPortKey"
+ "WTF::RefCountedBase::~RefCountedBase()"
+ "_copyRemoteInspectionEnabledValueFromDevice:"
+ "_copyWirelessEnabledValueFromDevice:"
+ "_driverBidiPort"
+ "bad_optional_access was thrown in -fno-exceptions mode"
+ "bidiPort"
+ "driverBidiPort"
+ "partitionKey"
+ "setCookieWithErrorCallback:successCallback:cookie:shouldPartition:"
+ "setDriverBidiPort:"
+ "setPartitionKey:"
- "%@ (%{public}@) made it into the dispatch to fetch device info and will not delay service connection."
- "%@ (%{public}@) will fetch device information and delay service connection"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/wtf/JSONValues.h"
- "22E"
- "22L"
- "22O"
- "22T"
- "24E"
- "setCookieWithErrorCallback:successCallback:cookie:"

```
