## WebInspector

> `/System/Library/PrivateFrameworks/WebInspector.framework/WebInspector`

```diff

-7616.2.9.10.13
-  __TEXT.__text: 0x73f20
-  __TEXT.__auth_stubs: 0xb50
+7617.1.17.10.9
+  __TEXT.__text: 0x669d8
+  __TEXT.__auth_stubs: 0xb60
   __TEXT.__objc_methlist: 0x3dac
-  __TEXT.__cstring: 0x3f12
+  __TEXT.__cstring: 0x401b
   __TEXT.__oslogstring: 0x130e
   __TEXT.__const: 0x8
-  __TEXT.__gcc_except_tab: 0x69e8
-  __TEXT.__unwind_info: 0x2f7c
+  __TEXT.__gcc_except_tab: 0x6774
+  __TEXT.__unwind_info: 0x2a9c
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0xc74
   __TEXT.__objc_methname: 0x79d4

   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x5c0
+  __AUTH_CONST.__auth_got: 0x5c8
   __AUTH.__objc_data: 0x1ea0
   __DATA.__objc_classrefs: 0x300
   __DATA.__objc_superrefs: 0x318

   - /usr/lib/libc++.1.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 168D132A-E1B7-3402-A628-5A111AAAD069
-  Functions: 2586
-  Symbols:   7484
-  CStrings:  2968
+  UUID: C67EDF5B-A7A1-3461-A1D5-C3ADA69C5817
+  Functions: 2416
+  Symbols:   7145
+  CStrings:  2970
 
Symbols:
+ __Z16WTFCrashWithInfoiPKcS0_i
+ __ZN3WTF8JSONImpl5ValuedlEPS1_St19destroying_delete_t
- -[RWIProtocolCSSDomainEventDispatcher nodeLayoutFlagsChangedWithNodeId:layoutFlags:].cold.3
- -[RWIProtocolCSSDomainEventDispatcher styleSheetAddedWithHeader:].cold.3
- -[RWIProtocolCSSFont setVariationAxes:].cold.1
- -[RWIProtocolCSSGrouping range].cold.2
- -[RWIProtocolCSSGrouping ruleId].cold.2
- -[RWIProtocolCSSInheritedStyleEntry inlineStyle].cold.2
- -[RWIProtocolCSSInheritedStyleEntry setMatchedCSSRules:].cold.1
- -[RWIProtocolCSSProperty range].cold.2
- -[RWIProtocolCSSPseudoIdMatches setMatches:].cold.1
- -[RWIProtocolCSSRule ruleId].cold.2
- -[RWIProtocolCSSRule selectorList].cold.2
- -[RWIProtocolCSSRule setGroupings:].cold.1
- -[RWIProtocolCSSRule style].cold.2
- -[RWIProtocolCSSRuleMatch rule].cold.2
- -[RWIProtocolCSSSelectorList range].cold.2
- -[RWIProtocolCSSSelectorList setSelectors:].cold.1
- -[RWIProtocolCSSStyle range].cold.2
- -[RWIProtocolCSSStyle setCssProperties:].cold.1
- -[RWIProtocolCSSStyle setShorthandEntries:].cold.1
- -[RWIProtocolCSSStyle styleId].cold.2
- -[RWIProtocolCSSStyleAttribute style].cold.2
- -[RWIProtocolCSSStyleSheetBody setRules:].cold.1
- -[RWIProtocolConsoleDomainEventDispatcher messageAddedWithMessage:].cold.3
- -[RWIProtocolConsoleMessage setParameters:].cold.1
- -[RWIProtocolConsoleMessage stackTrace].cold.2
- -[RWIProtocolConsoleStackTrace parentStackTrace].cold.2
- -[RWIProtocolConsoleStackTrace setCallFrames:].cold.1
- -[RWIProtocolDOMDomainEventDispatcher childNodeInsertedWithParentNodeId:previousNodeId:node:].cold.3
- -[RWIProtocolDOMDomainEventDispatcher didFireEventWithNodeId:eventName:timestamp:data:].cold.3
- -[RWIProtocolDOMDomainEventDispatcher inlineStyleInvalidatedWithNodeIds:].cold.3
- -[RWIProtocolDOMDomainEventDispatcher pseudoElementAddedWithParentId:pseudoElement:].cold.3
- -[RWIProtocolDOMDomainEventDispatcher setChildNodesWithParentId:nodes:].cold.3
- -[RWIProtocolDOMDomainEventDispatcher shadowRootPushedWithHostId:root:].cold.3
- -[RWIProtocolDOMEventListener location].cold.2
- -[RWIProtocolDOMFlexOverlayConfig flexColor].cold.2
- -[RWIProtocolDOMGridOverlayConfig gridColor].cold.2
- -[RWIProtocolDOMHighlightConfig borderColor].cold.2
- -[RWIProtocolDOMHighlightConfig contentColor].cold.2
- -[RWIProtocolDOMHighlightConfig marginColor].cold.2
- -[RWIProtocolDOMHighlightConfig paddingColor].cold.2
- -[RWIProtocolDOMNode contentDocument].cold.2
- -[RWIProtocolDOMNode setChildren:].cold.1
- -[RWIProtocolDOMNode setPseudoElements:].cold.1
- -[RWIProtocolDOMNode setShadowRoots:].cold.1
- -[RWIProtocolDOMNode templateContent].cold.2
- -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemAddedWithStorageId:key:newValue:].cold.3
- -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemRemovedWithStorageId:key:].cold.3
- -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemUpdatedWithStorageId:key:oldValue:newValue:].cold.3
- -[RWIProtocolDOMStorageDomainEventDispatcher domStorageItemsClearedWithStorageId:].cold.3
- -[RWIProtocolDebuggerBreakpointOptions setActions:].cold.1
- -[RWIProtocolDebuggerCallFrame location].cold.2
- -[RWIProtocolDebuggerCallFrame setScopeChain:].cold.1
- -[RWIProtocolDebuggerCallFrame thisObject].cold.2
- -[RWIProtocolDebuggerFunctionDetails location].cold.2
- -[RWIProtocolDebuggerFunctionDetails setScopeChain:].cold.1
- -[RWIProtocolDebuggerProbeSample payload].cold.2
- -[RWIProtocolDebuggerScope location].cold.2
- -[RWIProtocolDebuggerScope object].cold.2
- -[RWIProtocolJSONObject setObject:forKey:].cold.2
- -[RWIProtocolNetworkCachedResource response].cold.2
- -[RWIProtocolNetworkDomainEventDispatcher loadingFinishedWithRequestId:timestamp:sourceMapURL:metrics:].cold.3
- -[RWIProtocolNetworkDomainEventDispatcher requestInterceptedWithRequestId:request:].cold.3
- -[RWIProtocolNetworkDomainEventDispatcher requestServedFromMemoryCacheWithRequestId:frameId:loaderId:documentURL:timestamp:initiator:resource:].cold.4
- -[RWIProtocolNetworkDomainEventDispatcher requestServedFromMemoryCacheWithRequestId:frameId:loaderId:documentURL:timestamp:initiator:resource:].cold.5
- -[RWIProtocolNetworkDomainEventDispatcher requestWillBeSentWithRequestId:frameId:loaderId:documentURL:request:timestamp:walltime:initiator:redirectResponse:type:targetId:].cold.5
- -[RWIProtocolNetworkDomainEventDispatcher requestWillBeSentWithRequestId:frameId:loaderId:documentURL:request:timestamp:walltime:initiator:redirectResponse:type:targetId:].cold.6
- -[RWIProtocolNetworkDomainEventDispatcher requestWillBeSentWithRequestId:frameId:loaderId:documentURL:request:timestamp:walltime:initiator:redirectResponse:type:targetId:].cold.7
- -[RWIProtocolNetworkDomainEventDispatcher responseInterceptedWithRequestId:response:].cold.3
- -[RWIProtocolNetworkDomainEventDispatcher responseReceivedWithRequestId:frameId:loaderId:timestamp:type:response:].cold.3
- -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameReceivedWithRequestId:timestamp:response:].cold.3
- -[RWIProtocolNetworkDomainEventDispatcher webSocketFrameSentWithRequestId:timestamp:response:].cold.3
- -[RWIProtocolNetworkDomainEventDispatcher webSocketHandshakeResponseReceivedWithRequestId:timestamp:response:].cold.3
- -[RWIProtocolNetworkDomainEventDispatcher webSocketWillSendHandshakeRequestWithRequestId:timestamp:walltime:request:].cold.3
- -[RWIProtocolNetworkInitiator stackTrace].cold.2
- -[RWIProtocolNetworkMetrics requestHeaders].cold.2
- -[RWIProtocolNetworkMetrics securityConnection].cold.2
- -[RWIProtocolNetworkRequest headers].cold.2
- -[RWIProtocolNetworkResponse headers].cold.2
- -[RWIProtocolNetworkResponse requestHeaders].cold.2
- -[RWIProtocolNetworkResponse security].cold.2
- -[RWIProtocolNetworkResponse timing].cold.2
- -[RWIProtocolNetworkWebSocketRequest headers].cold.2
- -[RWIProtocolNetworkWebSocketResponse headers].cold.2
- -[RWIProtocolPageDomainEventDispatcher defaultUserPreferencesDidChangeWithPreferences:].cold.3
- -[RWIProtocolPageDomainEventDispatcher frameNavigatedWithFrame:].cold.3
- -[RWIProtocolPageFrameResourceTree frame].cold.2
- -[RWIProtocolPageFrameResourceTree setChildFrames:].cold.1
- -[RWIProtocolPageFrameResourceTree setResources:].cold.1
- -[RWIProtocolRuntimeCallArgument value].cold.2
- -[RWIProtocolRuntimeCollectionEntry key].cold.2
- -[RWIProtocolRuntimeCollectionEntry value].cold.2
- -[RWIProtocolRuntimeEntryPreview key].cold.2
- -[RWIProtocolRuntimeEntryPreview value].cold.2
- -[RWIProtocolRuntimeInternalPropertyDescriptor value].cold.2
- -[RWIProtocolRuntimeObjectPreview setEntries:].cold.1
- -[RWIProtocolRuntimeObjectPreview setProperties:].cold.1
- -[RWIProtocolRuntimePropertyDescriptor get].cold.2
- -[RWIProtocolRuntimePropertyDescriptor set].cold.2
- -[RWIProtocolRuntimePropertyDescriptor symbol].cold.2
- -[RWIProtocolRuntimePropertyDescriptor value].cold.2
- -[RWIProtocolRuntimePropertyPreview valuePreview].cold.2
- -[RWIProtocolRuntimeRemoteObject classPrototype].cold.2
- -[RWIProtocolRuntimeRemoteObject preview].cold.2
- -[RWIProtocolRuntimeRemoteObject value].cold.2
- -[RWIProtocolRuntimeStructureDescription prototypeStructure].cold.2
- -[RWIProtocolRuntimeTypeDescription setStructures:].cold.1
- -[RWIProtocolRuntimeTypeDescription typeSet].cold.2
- -[RWIProtocolSecurity certificate].cold.2
- -[RWIProtocolSecurity connection].cold.2
- __ZN9Inspector11toObjCArrayI18RWIProtocolCSSRuleEEP7NSArrayON3WTF6RefPtrINS4_8JSONImpl5ArrayENS4_12RawPtrTraitsIS7_EENS4_21DefaultRefDerefTraitsIS7_EEEE.cold.1
- __ZN9Inspector11toObjCArrayI18RWIProtocolDOMNodeEEP7NSArrayON3WTF6RefPtrINS4_8JSONImpl5ArrayENS4_12RawPtrTraitsIS7_EENS4_21DefaultRefDerefTraitsIS7_EEEE.cold.1
- __ZN9Inspector11toObjCArrayI22RWIProtocolCSSGroupingEEP7NSArrayON3WTF6RefPtrINS4_8JSONImpl5ArrayENS4_12RawPtrTraitsIS7_EENS4_21DefaultRefDerefTraitsIS7_EEEE.cold.1
- __ZN9Inspector11toObjCArrayI22RWIProtocolCSSPropertyEEP7NSArrayON3WTF6RefPtrINS4_8JSONImpl5ArrayENS4_12RawPtrTraitsIS7_EENS4_21DefaultRefDerefTraitsIS7_EEEE.cold.1
- __ZN9Inspector11toObjCArrayI22RWIProtocolCSSSelectorEEP7NSArrayON3WTF6RefPtrINS4_8JSONImpl5ArrayENS4_12RawPtrTraitsIS7_EENS4_21DefaultRefDerefTraitsIS7_EEEE.cold.1
- __ZN9Inspector11toObjCArrayI23RWIProtocolCSSRuleMatchEEP7NSArrayON3WTF6RefPtrINS4_8JSONImpl5ArrayENS4_12RawPtrTraitsIS7_EENS4_21DefaultRefDerefTraitsIS7_EEEE.cold.1
- __ZN9Inspector11toObjCArrayI24RWIProtocolDebuggerScopeEEP7NSArrayON3WTF6RefPtrINS4_8JSONImpl5ArrayENS4_12RawPtrTraitsIS7_EENS4_21DefaultRefDerefTraitsIS7_EEEE.cold.1
- __ZN9Inspector11toObjCArrayI27RWIProtocolConsoleCallFrameEEP7NSArrayON3WTF6RefPtrINS4_8JSONImpl5ArrayENS4_12RawPtrTraitsIS7_EENS4_21DefaultRefDerefTraitsIS7_EEEE.cold.1
- __ZN9Inspector11toObjCArrayI28RWIProtocolCSSShorthandEntryEEP7NSArrayON3WTF6RefPtrINS4_8JSONImpl5ArrayENS4_12RawPtrTraitsIS7_EENS4_21DefaultRefDerefTraitsIS7_EEEE.cold.1
- __ZN9Inspector11toObjCArrayI28RWIProtocolPageFrameResourceEEP7NSArrayON3WTF6RefPtrINS4_8JSONImpl5ArrayENS4_12RawPtrTraitsIS7_EENS4_21DefaultRefDerefTraitsIS7_EEEE.cold.1
- __ZN9Inspector11toObjCArrayI30RWIProtocolRuntimeEntryPreviewEEP7NSArrayON3WTF6RefPtrINS4_8JSONImpl5ArrayENS4_12RawPtrTraitsIS7_EENS4_21DefaultRefDerefTraitsIS7_EEEE.cold.1
- __ZN9Inspector11toObjCArrayI30RWIProtocolRuntimeRemoteObjectEEP7NSArrayON3WTF6RefPtrINS4_8JSONImpl5ArrayENS4_12RawPtrTraitsIS7_EENS4_21DefaultRefDerefTraitsIS7_EEEE.cold.1
- __ZN9Inspector11toObjCArrayI31RWIProtocolCSSFontVariationAxisEEP7NSArrayON3WTF6RefPtrINS4_8JSONImpl5ArrayENS4_12RawPtrTraitsIS7_EENS4_21DefaultRefDerefTraitsIS7_EEEE.cold.1
- __ZN9Inspector11toObjCArrayI32RWIProtocolPageFrameResourceTreeEEP7NSArrayON3WTF6RefPtrINS4_8JSONImpl5ArrayENS4_12RawPtrTraitsIS7_EENS4_21DefaultRefDerefTraitsIS7_EEEE.cold.1
- __ZN9Inspector11toObjCArrayI33RWIProtocolRuntimePropertyPreviewEEP7NSArrayON3WTF6RefPtrINS4_8JSONImpl5ArrayENS4_12RawPtrTraitsIS7_EENS4_21DefaultRefDerefTraitsIS7_EEEE.cold.1
- __ZN9Inspector11toObjCArrayI35RWIProtocolDebuggerBreakpointActionEEP7NSArrayON3WTF6RefPtrINS4_8JSONImpl5ArrayENS4_12RawPtrTraitsIS7_EENS4_21DefaultRefDerefTraitsIS7_EEEE.cold.1
- __ZN9Inspector11toObjCArrayI38RWIProtocolRuntimeStructureDescriptionEEP7NSArrayON3WTF6RefPtrINS4_8JSONImpl5ArrayENS4_12RawPtrTraitsIS7_EENS4_21DefaultRefDerefTraitsIS7_EEEE.cold.1
- __ZN9Inspector17toJSONObjectArrayEP7NSArray.cold.2
- __ZN9Inspector22toJSONStringArrayArrayEP7NSArray.cold.2
- ____ZN9Inspector33ObjCInspectorCSSBackendDispatcher12setStyleTextElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EEEERKNS1_6StringE_block_invoke_2.cold.2
- ____ZN9Inspector33ObjCInspectorCSSBackendDispatcher13getStyleSheetElRKN3WTF6StringE_block_invoke_2.cold.2
- ____ZN9Inspector33ObjCInspectorCSSBackendDispatcher15setRuleSelectorElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EEEERKNS1_6StringE_block_invoke_2.cold.2
- ____ZN9Inspector33ObjCInspectorCSSBackendDispatcher17getAllStyleSheetsEl_block_invoke_2.cold.2
- ____ZN9Inspector33ObjCInspectorCSSBackendDispatcher18getFontDataForNodeEli_block_invoke_2.cold.2
- ____ZN9Inspector33ObjCInspectorCSSBackendDispatcher21setGroupingHeaderTextElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EEEERKNS1_6StringE_block_invoke_2.cold.2
- ____ZN9Inspector33ObjCInspectorCSSBackendDispatcher22getInlineStylesForNodeEli_block_invoke_2.cold.3
- ____ZN9Inspector33ObjCInspectorCSSBackendDispatcher22getInlineStylesForNodeEli_block_invoke_2.cold.4
- ____ZN9Inspector33ObjCInspectorCSSBackendDispatcher23getComputedStyleForNodeEli_block_invoke_2.cold.2
- ____ZN9Inspector33ObjCInspectorCSSBackendDispatcher23getMatchedStylesForNodeEliONSt3__18optionalIbEES4__block_invoke_2.cold.4
- ____ZN9Inspector33ObjCInspectorCSSBackendDispatcher23getMatchedStylesForNodeEliONSt3__18optionalIbEES4__block_invoke_2.cold.5
- ____ZN9Inspector33ObjCInspectorCSSBackendDispatcher23getMatchedStylesForNodeEliONSt3__18optionalIbEES4__block_invoke_2.cold.6
- ____ZN9Inspector33ObjCInspectorCSSBackendDispatcher25getSupportedCSSPropertiesEl_block_invoke_2.cold.2
- ____ZN9Inspector33ObjCInspectorCSSBackendDispatcher33getSupportedSystemFontFamilyNamesEl_block_invoke_2.cold.2
- ____ZN9Inspector33ObjCInspectorCSSBackendDispatcher7addRuleElRKN3WTF6StringES4__block_invoke_2.cold.2
- ____ZN9Inspector33ObjCInspectorDOMBackendDispatcher11getDocumentEl_block_invoke_2.cold.2
- ____ZN9Inspector33ObjCInspectorDOMBackendDispatcher11resolveNodeEliRKN3WTF6StringE_block_invoke_2.cold.2
- ____ZN9Inspector33ObjCInspectorDOMBackendDispatcher13getAttributesEli_block_invoke_2.cold.2
- ____ZN9Inspector33ObjCInspectorDOMBackendDispatcher16getSearchResultsElRKN3WTF6StringEii_block_invoke_2.cold.2
- ____ZN9Inspector33ObjCInspectorDOMBackendDispatcher16querySelectorAllEliRKN3WTF6StringE_block_invoke_2.cold.2
- ____ZN9Inspector33ObjCInspectorDOMBackendDispatcher22getDataBindingsForNodeEli_block_invoke_2.cold.2
- ____ZN9Inspector33ObjCInspectorDOMBackendDispatcher22getSupportedEventNamesEl_block_invoke_2.cold.2
- ____ZN9Inspector33ObjCInspectorDOMBackendDispatcher24getEventListenersForNodeEliONSt3__18optionalIbEE_block_invoke_2.cold.2
- ____ZN9Inspector33ObjCInspectorDOMBackendDispatcher33getAccessibilityPropertiesForNodeEli_block_invoke_2.cold.2
- ____ZN9Inspector34ObjCInspectorPageBackendDispatcher10getCookiesEl_block_invoke_2.cold.2
- ____ZN9Inspector34ObjCInspectorPageBackendDispatcher15getResourceTreeEl_block_invoke_2.cold.2
- ____ZN9Inspector34ObjCInspectorPageBackendDispatcher16searchInResourceElRKN3WTF6StringES4_S4_ONSt3__18optionalIbEES8_S4__block_invoke_2.cold.2
- ____ZN9Inspector34ObjCInspectorPageBackendDispatcher17searchInResourcesElRKN3WTF6StringEONSt3__18optionalIbEES8__block_invoke_2.cold.2
- ____ZN9Inspector37ObjCInspectorNetworkBackendDispatcher16resolveWebSocketElRKN3WTF6StringES4__block_invoke_2.cold.2
- ____ZN9Inspector40ObjCInspectorDOMStorageBackendDispatcher18getDOMStorageItemsElON3WTF3RefINS1_8JSONImpl6ObjectENS1_12RawPtrTraitsIS4_EEEE_block_invoke_2.cold.2
CStrings:
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/include/c++/v1/optional"
+ "/AppleInternal/Library/BuildRoots/4f96e3a2-905b-11ee-9a19-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/local/include/wtf/JSONValues.h"
+ "RefPtr<Object> WTF::JSONImpl::Value::asObject()"
- "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/optional"

```
