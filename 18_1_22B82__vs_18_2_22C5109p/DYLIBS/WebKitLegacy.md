## WebKitLegacy

> `/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy`

```diff

-619.2.8.10.7
-  __TEXT.__text: 0x13fdc8
-  __TEXT.__auth_stubs: 0x8a60
-  __TEXT.__objc_methlist: 0xea54
+620.1.11.10.8
+  __TEXT.__text: 0x13fdb4
+  __TEXT.__auth_stubs: 0x8a70
+  __TEXT.__objc_methlist: 0xea5c
   __TEXT.__const: 0x244
-  __TEXT.__gcc_except_tab: 0xf334
-  __TEXT.__cstring: 0xe892
+  __TEXT.__gcc_except_tab: 0xf3bc
+  __TEXT.__cstring: 0xf3a0
   __TEXT.__oslogstring: 0x141
-  __TEXT.__unwind_info: 0x82f8
+  __TEXT.__unwind_info: 0x82b0
   __TEXT.__objc_classname: 0x1be0
-  __TEXT.__objc_methname: 0x18937
-  __TEXT.__objc_methtype: 0x7d02
+  __TEXT.__objc_methname: 0x18956
+  __TEXT.__objc_methtype: 0x7e6a
   __TEXT.__objc_stubs: 0xb200
-  __DATA_CONST.__got: 0xf28
+  __DATA_CONST.__got: 0xf18
   __DATA_CONST.__const: 0x488
   __DATA_CONST.__objc_classlist: 0x6c8
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7da0
+  __DATA_CONST.__objc_selrefs: 0x7da8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x358
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x4548
+  __AUTH_CONST.__auth_got: 0x4550
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x5518
-  __AUTH_CONST.__cfstring: 0xd100
+  __AUTH_CONST.__const: 0x5498
+  __AUTH_CONST.__cfstring: 0xdae0
   __AUTH_CONST.__objc_const: 0x11298
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 7305
-  Symbols:   10447
-  CStrings:  7352
+  Functions: 7290
+  Symbols:   10433
+  CStrings:  7432
 
Symbols:
+ _WebThreadIsLockedOrDisabledInMainOrWebThread
+ __ZN7WebCore10LocalFrame14createSubframeERNS_4PageEON3WTF17CompletionHandlerIFNS3_9UniqueRefINS_22LocalFrameLoaderClientEEERS0_EEENS_16ProcessQualifiedINS3_23ObjectIdentifierGenericINS_19FrameIdentifierTypeENS3_38ObjectIdentifierMainThreadAccessTraitsIyEEyLNS3_33SupportsObjectIdentifierNullStateE1EEEEERNS_21HTMLFrameOwnerElementE
+ __ZN7WebCore10MouseEvent6createERKN3WTF10AtomStringENS_14EventCanBubbleENS_17EventIsCancelableENS_15EventIsComposedENS1_13MonotonicTimeEONS1_6RefPtrINS_11WindowProxyENS1_12RawPtrTraitsISA_EENS1_21DefaultRefDerefTraitsISA_EEEEiRKNS_8IntPointESJ_ddNS1_9OptionSetINS_21PlatformEventModifierEEENS_11MouseButtonEtPNS_11EventTargetEdNS_18SyntheticClickTypeERKNS1_6VectorINS1_3RefIS0_NSB_IS0_EENSD_IS0_EEEELm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEES10_NS_17MouseRelatedEvent11IsSimulatedENS_14EventIsTrustedE
+ __ZN7WebCore11HistoryItemC1ERNS_17HistoryItemClientERKN3WTF6StringES6_S6_NSt3__18optionalINS_16ProcessQualifiedINS3_23ObjectIdentifierGenericINS_29BackForwardItemIdentifierTypeENS3_38ObjectIdentifierMainThreadAccessTraitsIyEEyLNS3_33SupportsObjectIdentifierNullStateE1EEEEEEE
+ __ZN7WebCore14LoaderStrategy34responseFromResourceLoadIdentifierEN3WTF23ObjectIdentifierGenericINS_14ResourceLoaderENS1_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS1_33SupportsObjectIdentifierNullStateE1EEE
+ __ZN7WebCore14LoaderStrategy40networkMetricsFromResourceLoadIdentifierEN3WTF23ObjectIdentifierGenericINS_14ResourceLoaderENS1_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS1_33SupportsObjectIdentifierNullStateE1EEE
+ __ZN7WebCore14LoaderStrategy53intermediateLoadInformationFromResourceLoadIdentifierEN3WTF23ObjectIdentifierGenericINS_14ResourceLoaderENS1_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS1_33SupportsObjectIdentifierNullStateE1EEE
+ __ZN7WebCore14LocalFrameView17layoutUpdateCountEv
+ __ZN7WebCore14UserStyleSheetC1ERKN3WTF6StringERKNS1_3URLEONS1_6VectorIS2_Lm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEESC_NS_25UserContentInjectedFramesENS_14UserStyleLevelENSt3__18optionalINS1_23ObjectIdentifierGenericINS_18PageIdentifierTypeENS1_38ObjectIdentifierMainThreadAccessTraitsIyEEyLNS1_33SupportsObjectIdentifierNullStateE0EEEEE
+ __ZN7WebCore16BroadcastChannel17dispatchMessageToEN3WTF23ObjectIdentifierGenericINS_30BroadcastChannelIdentifierTypeENS1_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS1_33SupportsObjectIdentifierNullStateE1EEEONS1_3RefINS_21SerializedScriptValueENS1_12RawPtrTraitsIS9_EENS1_21DefaultRefDerefTraitsIS9_EEEEONS1_17CompletionHandlerIFvvEEE
+ __ZN7WebCore17PageConfigurationC1ENSt3__18optionalIN3WTF23ObjectIdentifierGenericINS_18PageIdentifierTypeENS3_38ObjectIdentifierMainThreadAccessTraitsIyEEyLNS3_33SupportsObjectIdentifierNullStateE0EEEEEN3PAL9SessionIDEONS3_9UniqueRefINS_12EditorClientEEEONS3_3RefINS_14SocketProviderENS3_12RawPtrTraitsISI_EENS3_21DefaultRefDerefTraitsISI_EEEEONSD_INS_14WebRTCProviderEEEONSH_INS_20CacheStorageProviderENSJ_ISS_EENSL_ISS_EEEEONSH_INS_19UserContentProviderENSJ_ISX_EENSL_ISX_EEEEONSH_INS_17BackForwardClientENSJ_IS12_EENSL_IS12_EEEEONSH_INS_9CookieJarENSJ_IS17_EENSL_IS17_EEEEONSD_INS_21ProgressTrackerClientEEEONS1_7variantIJNS3_17CompletionHandlerIFNSD_INS_22LocalFrameLoaderClientEEERNS_10LocalFrameEEEENS1G_IFNSD_INS_17RemoteFrameClientEEERNS_11RemoteFrameEEEEEEENS_16ProcessQualifiedINS4_INS_19FrameIdentifierTypeES7_yLS8_1EEEEEONS3_6RefPtrINS_5FrameENSJ_IS20_EENSL_IS20_EEEEONSD_INS_25SpeechRecognitionProviderEEEONSD_INS_21MediaRecorderProviderEEEONSH_INS_24BroadcastChannelRegistryENSJ_IS2B_EENSL_IS2B_EEEEONSD_INS_15StorageProviderEEEONSD_INS_19ModelPlayerProviderEEEONSH_INS_11BadgeClientENSJ_IS2M_EENSL_IS2M_EEEEONSH_INS_17HistoryItemClientENSJ_IS2R_EENSL_IS2R_EEEEONSD_INS_24PaymentCoordinatorClientEEEONSD_INS_12ChromeClientEEEONSD_INS_12CryptoClientEEE
+ __ZN7WebCore27AlternativeTextUIController18removeAlternativesEN3WTF23ObjectIdentifierGenericINS_20DictationContextTypeENS1_38ObjectIdentifierMainThreadAccessTraitsIyEEyLNS1_33SupportsObjectIdentifierNullStateE1EEE
+ __ZN7WebCore27AlternativeTextUIController22alternativesForContextEN3WTF23ObjectIdentifierGenericINS_20DictationContextTypeENS1_38ObjectIdentifierMainThreadAccessTraitsIyEEyLNS1_33SupportsObjectIdentifierNullStateE1EEE
+ __ZN7WebCore39LegacyWebSocketInspectorInstrumentation17didCloseWebSocketEPNS_8DocumentEN3WTF23ObjectIdentifierGenericINS_16WebSocketChannelENS3_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS3_33SupportsObjectIdentifierNullStateE1EEE
+ __ZN7WebCore39LegacyWebSocketInspectorInstrumentation18didCreateWebSocketEPNS_8DocumentEN3WTF23ObjectIdentifierGenericINS_16WebSocketChannelENS3_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS3_33SupportsObjectIdentifierNullStateE1EEERKNS3_3URLE
+ __ZN7WebCore39LegacyWebSocketInspectorInstrumentation21didSendWebSocketFrameEPNS_8DocumentEN3WTF23ObjectIdentifierGenericINS_16WebSocketChannelENS3_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS3_33SupportsObjectIdentifierNullStateE1EEERKNS_14WebSocketFrameE
+ __ZN7WebCore39LegacyWebSocketInspectorInstrumentation24didReceiveWebSocketFrameEPNS_8DocumentEN3WTF23ObjectIdentifierGenericINS_16WebSocketChannelENS3_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS3_33SupportsObjectIdentifierNullStateE1EEERKNS_14WebSocketFrameE
+ __ZN7WebCore39LegacyWebSocketInspectorInstrumentation29didReceiveWebSocketFrameErrorEPNS_8DocumentEN3WTF23ObjectIdentifierGenericINS_16WebSocketChannelENS3_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS3_33SupportsObjectIdentifierNullStateE1EEERKNS3_6StringE
+ __ZN7WebCore39LegacyWebSocketInspectorInstrumentation33willSendWebSocketHandshakeRequestEPNS_8DocumentEN3WTF23ObjectIdentifierGenericINS_16WebSocketChannelENS3_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS3_33SupportsObjectIdentifierNullStateE1EEERKNS_15ResourceRequestE
+ __ZN7WebCore39LegacyWebSocketInspectorInstrumentation36didReceiveWebSocketHandshakeResponseEPNS_8DocumentEN3WTF23ObjectIdentifierGenericINS_16WebSocketChannelENS3_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS3_33SupportsObjectIdentifierNullStateE1EEERKNS_16ResourceResponseE
+ __ZN7WebCore4Page18setTopContentInsetEf
+ __ZN7WebCore5Frame12disownOpenerEv
+ __ZN7WebCore5Frame24setOpenerForWebKitLegacyEPS0_
+ __ZN7WebCore8DragDataC1EPvRKNS_8IntPointES4_N3WTF9OptionSetINS_13DragOperationEEENS6_INS_20DragApplicationFlagsEEENS6_INS_21DragDestinationActionEEENSt3__18optionalINS5_23ObjectIdentifierGenericINS_18PageIdentifierTypeENS5_38ObjectIdentifierMainThreadAccessTraitsIyEEyLNS5_33SupportsObjectIdentifierNullStateE0EEEEE
+ __ZN7WebCore8Settings37setShouldUseModernAVContentKeySessionEb
+ __ZN7WebCore9IDBClient21IDBConnectionToServer18didCloseFromServerEN3WTF23ObjectIdentifierGenericINS_35IDBDatabaseConnectionIdentifierTypeENS2_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS2_33SupportsObjectIdentifierNullStateE1EEERKNS_8IDBErrorE
+ __ZN7WebCore9IDBClient21IDBConnectionToServer22fireVersionChangeEventEN3WTF23ObjectIdentifierGenericINS_35IDBDatabaseConnectionIdentifierTypeENS2_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS2_33SupportsObjectIdentifierNullStateE1EEERKNS_21IDBResourceIdentifierEy
+ __ZN7WebCore9IDBServer9IDBServer11deleteIndexERKNS_14IDBRequestDataEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS5_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS5_33SupportsObjectIdentifierNullStateE0EEERKNS5_6StringE
+ __ZN7WebCore9IDBServer9IDBServer11renameIndexERKNS_14IDBRequestDataEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS5_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS5_33SupportsObjectIdentifierNullStateE0EEEyRKNS5_6StringE
+ __ZN7WebCore9IDBServer9IDBServer16clearObjectStoreERKNS_14IDBRequestDataEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS5_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS5_33SupportsObjectIdentifierNullStateE0EEE
+ __ZN7WebCore9IDBServer9IDBServer17renameObjectStoreERKNS_14IDBRequestDataEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS5_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS5_33SupportsObjectIdentifierNullStateE0EEERKNS5_6StringE
+ __ZN7WebCore9IDBServer9IDBServer20establishTransactionEN3WTF23ObjectIdentifierGenericINS_35IDBDatabaseConnectionIdentifierTypeENS2_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS2_33SupportsObjectIdentifierNullStateE1EEERKNS_18IDBTransactionInfoE
+ __ZN7WebCore9IDBServer9IDBServer24databaseConnectionClosedEN3WTF23ObjectIdentifierGenericINS_35IDBDatabaseConnectionIdentifierTypeENS2_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS2_33SupportsObjectIdentifierNullStateE1EEE
+ __ZN7WebCore9IDBServer9IDBServer25abortOpenAndUpgradeNeededEN3WTF23ObjectIdentifierGenericINS_35IDBDatabaseConnectionIdentifierTypeENS2_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS2_33SupportsObjectIdentifierNullStateE1EEERKNSt3__18optionalINS_21IDBResourceIdentifierEEE
+ __ZN7WebCore9IDBServer9IDBServer25didFireVersionChangeEventEN3WTF23ObjectIdentifierGenericINS_35IDBDatabaseConnectionIdentifierTypeENS2_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS2_33SupportsObjectIdentifierNullStateE1EEERKNS_21IDBResourceIdentifierENS_9IndexedDB32ConnectionClosedOnBehalfOfServerE
+ __ZN7WebCore9IDBServer9IDBServer30databaseConnectionPendingCloseEN3WTF23ObjectIdentifierGenericINS_35IDBDatabaseConnectionIdentifierTypeENS2_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS2_33SupportsObjectIdentifierNullStateE1EEE
+ __ZN7WebCore9IDBServer9IDBServer30getAllDatabaseNamesAndVersionsEN3WTF23ObjectIdentifierGenericINS_21ProcessIdentifierTypeENS2_38ObjectIdentifierMainThreadAccessTraitsIyEEyLNS2_33SupportsObjectIdentifierNullStateE1EEERKNS_21IDBResourceIdentifierERKNS_12ClientOriginE
+ __ZN7WebCore9IDBServer9IDBServer41didFinishHandlingVersionChangeTransactionEN3WTF23ObjectIdentifierGenericINS_35IDBDatabaseConnectionIdentifierTypeENS2_38ObjectIdentifierThreadSafeAccessTraitsIyEEyLNS2_33SupportsObjectIdentifierNullStateE1EEERKNS_21IDBResourceIdentifierE
+ __ZNK7WebCore12ChromeClient26ensureScrollbarsControllerERNS_4PageERNS_14ScrollableAreaEb
- __ZN7WebCore10LocalFrame14createSubframeERNS_4PageEON3WTF17CompletionHandlerIFNS3_9UniqueRefINS_22LocalFrameLoaderClientEEERS0_EEENS_16ProcessQualifiedINS3_23ObjectIdentifierGenericINS_19FrameIdentifierTypeENS3_38ObjectIdentifierMainThreadAccessTraitsIyEEyEEEERNS_21HTMLFrameOwnerElementE
- __ZN7WebCore10MouseEvent6createERKN3WTF10AtomStringENS_14EventCanBubbleENS_17EventIsCancelableENS_15EventIsComposedENS1_13MonotonicTimeEONS1_6RefPtrINS_11WindowProxyENS1_12RawPtrTraitsISA_EENS1_21DefaultRefDerefTraitsISA_EEEEiRKNS_8IntPointESJ_ddNS1_9OptionSetINS_21PlatformEventModifierEEENS_11MouseButtonEtPNS_11EventTargetEdNS_18SyntheticClickTypeENS_17MouseRelatedEvent11IsSimulatedENS_14EventIsTrustedE
- __ZN7WebCore11HistoryItemC1ERNS_17HistoryItemClientERKN3WTF6StringES6_S6_NSt3__18optionalINS_16ProcessQualifiedINS3_23ObjectIdentifierGenericINS_29BackForwardItemIdentifierTypeENS3_38ObjectIdentifierMainThreadAccessTraitsIyEEyEEEEEE
- __ZN7WebCore13OverflowEvent17initOverflowEventEtbb
- __ZN7WebCore14LoaderStrategy34responseFromResourceLoadIdentifierEN3WTF23ObjectIdentifierGenericINS_14ResourceLoaderENS1_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEE
- __ZN7WebCore14LoaderStrategy40networkMetricsFromResourceLoadIdentifierEN3WTF23ObjectIdentifierGenericINS_14ResourceLoaderENS1_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEE
- __ZN7WebCore14LoaderStrategy53intermediateLoadInformationFromResourceLoadIdentifierEN3WTF23ObjectIdentifierGenericINS_14ResourceLoaderENS1_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEE
- __ZN7WebCore14UserStyleSheetC1ERKN3WTF6StringERKNS1_3URLEONS1_6VectorIS2_Lm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEESC_NS_25UserContentInjectedFramesENS_14UserStyleLevelENSt3__18optionalINS1_23ObjectIdentifierGenericINS_18PageIdentifierTypeENS1_38ObjectIdentifierMainThreadAccessTraitsIyEEyEEEE
- __ZN7WebCore16BroadcastChannel17dispatchMessageToEN3WTF23ObjectIdentifierGenericINS_30BroadcastChannelIdentifierTypeENS1_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEEONS1_3RefINS_21SerializedScriptValueENS1_12RawPtrTraitsIS8_EENS1_21DefaultRefDerefTraitsIS8_EEEEONS1_17CompletionHandlerIFvvEEE
- __ZN7WebCore17PageConfigurationC1ENSt3__18optionalIN3WTF23ObjectIdentifierGenericINS_18PageIdentifierTypeENS3_38ObjectIdentifierMainThreadAccessTraitsIyEEyEEEEN3PAL9SessionIDEONS3_9UniqueRefINS_12EditorClientEEEONS3_3RefINS_14SocketProviderENS3_12RawPtrTraitsISH_EENS3_21DefaultRefDerefTraitsISH_EEEEONSC_INS_14WebRTCProviderEEEONSG_INS_20CacheStorageProviderENSI_ISR_EENSK_ISR_EEEEONSG_INS_19UserContentProviderENSI_ISW_EENSK_ISW_EEEEONSG_INS_17BackForwardClientENSI_IS11_EENSK_IS11_EEEEONSG_INS_9CookieJarENSI_IS16_EENSK_IS16_EEEEONSC_INS_21ProgressTrackerClientEEEONS1_7variantIJNS3_17CompletionHandlerIFNSC_INS_22LocalFrameLoaderClientEEERNS_10LocalFrameEEEENS1F_IFNSC_INS_17RemoteFrameClientEEERNS_11RemoteFrameEEEEEEENS_16ProcessQualifiedINS4_INS_19FrameIdentifierTypeES7_yEEEEONS3_6RefPtrINS_5FrameENSI_IS1Z_EENSK_IS1Z_EEEEONSC_INS_25SpeechRecognitionProviderEEEONSC_INS_21MediaRecorderProviderEEEONSG_INS_24BroadcastChannelRegistryENSI_IS2A_EENSK_IS2A_EEEEONSC_INS_15StorageProviderEEEONSC_INS_19ModelPlayerProviderEEEONSG_INS_11BadgeClientENSI_IS2L_EENSK_IS2L_EEEEONSG_INS_17HistoryItemClientENSI_IS2Q_EENSK_IS2Q_EEEEONSC_INS_24PaymentCoordinatorClientEEEONSC_INS_12ChromeClientEEEONSC_INS_12CryptoClientEEE
- __ZN7WebCore27AlternativeTextUIController18removeAlternativesEN3WTF23ObjectIdentifierGenericINS_20DictationContextTypeENS1_38ObjectIdentifierMainThreadAccessTraitsIyEEyEE
- __ZN7WebCore27AlternativeTextUIController22alternativesForContextEN3WTF23ObjectIdentifierGenericINS_20DictationContextTypeENS1_38ObjectIdentifierMainThreadAccessTraitsIyEEyEE
- __ZN7WebCore39LegacyWebSocketInspectorInstrumentation17didCloseWebSocketEPNS_8DocumentEN3WTF23ObjectIdentifierGenericINS_16WebSocketChannelENS3_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEE
- __ZN7WebCore39LegacyWebSocketInspectorInstrumentation18didCreateWebSocketEPNS_8DocumentEN3WTF23ObjectIdentifierGenericINS_16WebSocketChannelENS3_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS3_3URLE
- __ZN7WebCore39LegacyWebSocketInspectorInstrumentation21didSendWebSocketFrameEPNS_8DocumentEN3WTF23ObjectIdentifierGenericINS_16WebSocketChannelENS3_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS_14WebSocketFrameE
- __ZN7WebCore39LegacyWebSocketInspectorInstrumentation24didReceiveWebSocketFrameEPNS_8DocumentEN3WTF23ObjectIdentifierGenericINS_16WebSocketChannelENS3_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS_14WebSocketFrameE
- __ZN7WebCore39LegacyWebSocketInspectorInstrumentation29didReceiveWebSocketFrameErrorEPNS_8DocumentEN3WTF23ObjectIdentifierGenericINS_16WebSocketChannelENS3_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS3_6StringE
- __ZN7WebCore39LegacyWebSocketInspectorInstrumentation33willSendWebSocketHandshakeRequestEPNS_8DocumentEN3WTF23ObjectIdentifierGenericINS_16WebSocketChannelENS3_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS_15ResourceRequestE
- __ZN7WebCore39LegacyWebSocketInspectorInstrumentation36didReceiveWebSocketHandshakeResponseEPNS_8DocumentEN3WTF23ObjectIdentifierGenericINS_16WebSocketChannelENS3_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS_16ResourceResponseE
- __ZN7WebCore5Frame9setOpenerEPS0_
- __ZN7WebCore8DragDataC1EPvRKNS_8IntPointES4_N3WTF9OptionSetINS_13DragOperationEEENS6_INS_20DragApplicationFlagsEEENS6_INS_21DragDestinationActionEEENSt3__18optionalINS5_23ObjectIdentifierGenericINS_18PageIdentifierTypeENS5_38ObjectIdentifierMainThreadAccessTraitsIyEEyEEEE
- __ZN7WebCore8SVGTests27hasFeatureForLegacyBindingsERKN3WTF6StringES4_
- __ZN7WebCore8Settings46setSampleBufferContentKeySessionSupportEnabledEb
- __ZN7WebCore9HTMLNames15incrementalAttrE
- __ZN7WebCore9IDBClient21IDBConnectionToServer18didCloseFromServerEN3WTF23ObjectIdentifierGenericINS_35IDBDatabaseConnectionIdentifierTypeENS2_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS_8IDBErrorE
- __ZN7WebCore9IDBClient21IDBConnectionToServer22fireVersionChangeEventEN3WTF23ObjectIdentifierGenericINS_35IDBDatabaseConnectionIdentifierTypeENS2_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS_21IDBResourceIdentifierEy
- __ZN7WebCore9IDBServer9IDBServer11deleteIndexERKNS_14IDBRequestDataEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS5_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS5_6StringE
- __ZN7WebCore9IDBServer9IDBServer11renameIndexERKNS_14IDBRequestDataEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS5_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEEyRKNS5_6StringE
- __ZN7WebCore9IDBServer9IDBServer16clearObjectStoreERKNS_14IDBRequestDataEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS5_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEE
- __ZN7WebCore9IDBServer9IDBServer17renameObjectStoreERKNS_14IDBRequestDataEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS5_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS5_6StringE
- __ZN7WebCore9IDBServer9IDBServer20establishTransactionEN3WTF23ObjectIdentifierGenericINS_35IDBDatabaseConnectionIdentifierTypeENS2_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS_18IDBTransactionInfoE
- __ZN7WebCore9IDBServer9IDBServer24databaseConnectionClosedEN3WTF23ObjectIdentifierGenericINS_35IDBDatabaseConnectionIdentifierTypeENS2_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEE
- __ZN7WebCore9IDBServer9IDBServer25abortOpenAndUpgradeNeededEN3WTF23ObjectIdentifierGenericINS_35IDBDatabaseConnectionIdentifierTypeENS2_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNSt3__18optionalINS_21IDBResourceIdentifierEEE
- __ZN7WebCore9IDBServer9IDBServer25didFireVersionChangeEventEN3WTF23ObjectIdentifierGenericINS_35IDBDatabaseConnectionIdentifierTypeENS2_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS_21IDBResourceIdentifierENS_9IndexedDB32ConnectionClosedOnBehalfOfServerE
- __ZN7WebCore9IDBServer9IDBServer30databaseConnectionPendingCloseEN3WTF23ObjectIdentifierGenericINS_35IDBDatabaseConnectionIdentifierTypeENS2_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEE
- __ZN7WebCore9IDBServer9IDBServer30getAllDatabaseNamesAndVersionsEN3WTF23ObjectIdentifierGenericINS_21ProcessIdentifierTypeENS2_38ObjectIdentifierMainThreadAccessTraitsIyEEyEERKNS_21IDBResourceIdentifierERKNS_12ClientOriginE
- __ZN7WebCore9IDBServer9IDBServer41didFinishHandlingVersionChangeTransactionEN3WTF23ObjectIdentifierGenericINS_35IDBDatabaseConnectionIdentifierTypeENS2_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS_21IDBResourceIdentifierE
- __ZNK7WebCore12ChromeClient26ensureScrollbarsControllerERNS_4PageERNS_14ScrollableAreaE
CStrings:
+ "/AppleInternal/Library/BuildRoots/e20a253b-8c72-11ef-890e-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
+ "/AppleInternal/Library/BuildRoots/e20a253b-8c72-11ef-890e-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/e20a253b-8c72-11ef-890e-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
+ "/AppleInternal/Library/BuildRoots/e20a253b-8c72-11ef-890e-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
+ "/AppleInternal/Library/BuildRoots/e20a253b-8c72-11ef-890e-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
+ "/AppleInternal/Library/BuildRoots/e20a253b-8c72-11ef-890e-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "::target-text pseudo-element"
+ "@page CSS at-rule margin descriptors"
+ "AltitudeAngleEnabled"
+ "AuxclickEventEnabled"
+ "AzimuthAngleEnabled"
+ "BlobFileAccessEnforcementEnabled"
+ "CSS appearance: base"
+ "CSS background-clip: border-area"
+ "CSS color-layers()"
+ "CSS line-clamp"
+ "CSS ruby-align property"
+ "CSS ruby-overhang property"
+ "CSS shape() function"
+ "CSS text-autospace property"
+ "CSSAppearanceBaseEnabled"
+ "CSSBackgroundClipBorderAreaEnabled"
+ "CSSColorLayersEnabled"
+ "CSSLineClampEnabled"
+ "CSSRubyAlignEnabled"
+ "CSSRubyOverhangEnabled"
+ "CSSShapeFunctionEnabled"
+ "CSSTextAutospaceEnabled"
+ "Cookie Store API CookieStoreManager"
+ "CookieStoreManagerEnabled"
+ "Cross document view-transitions"
+ "CrossDocumentViewTransitionsEnabled"
+ "Enable CSS line-clamp"
+ "Enable Cookie Store API CookieStoreManager which controls cookie change subscriptions for Service Workers"
+ "Enable HTML command & commandfor attribute support"
+ "Enable HTTPS-by-default (HTTPS-First)"
+ "Enable MediaSession capture related API"
+ "Enable `auxclick` event"
+ "Enable base value for CSS appearance"
+ "Enable ruby-align"
+ "Enable ruby-overhang"
+ "Enable support for @page margin descriptors"
+ "Enable support for CSS color-layers()"
+ "Enable support for view-transitions cross-document"
+ "Enable the ::target-text CSS pseudo-element"
+ "Enable the CSS shape() function"
+ "Enable the `altitudeAngle` property of the PointerEvents API"
+ "Enable the `auxclick` UI event"
+ "Enable the `azimuthAngle` property of the PointerEvents API"
+ "Enable the `getCoalescedEvents` function of the Pointer Events API"
+ "Enable the `getPredictedEvents` function of the Pointer Events API"
+ "Enable the border-area value for background-clip"
+ "Enable the property text-autospace, defined in CSS Text 4"
+ "Enforce blob backed file access valid for web process"
+ "GetCoalescedEventsEnabled"
+ "GetPredictedEventsEnabled"
+ "HTML command & commandfor attributes"
+ "HTTPS-by-default (HTTPS-First)"
+ "HTTPSByDefaultEnabled"
+ "Ignore iframe Embedding Protections"
+ "IgnoreIframeEmbeddingProtectionsEnabled"
+ "Ignores X-Frame-Options and CSP ancestors"
+ "LoginStatusAPIRequiresWebAuthnEnabled"
+ "MediaSession capture related API"
+ "MediaSessionCaptureToggleAPIEnabled"
+ "Modern AVContentKeySession"
+ "Observable API"
+ "ObservableEnabled"
+ "PageAtRuleMarginDescriptorsEnabled"
+ "Pointer Events getCoalescedEvents API"
+ "Pointer Events getPredictedEvents API"
+ "Require WebAuthn with the Login Status API"
+ "Require a recent WebAuthn authentication to set login status"
+ "ShouldUseModernAVContentKeySession"
+ "Support for the Observable API"
+ "Support specifying classes for view transitions"
+ "Support specifying types for view transitions"
+ "TargetTextPseudoElementEnabled"
+ "Use modern AVContentKeySession"
+ "Validate file backed blobs were created by the correct web process"
+ "View Transition Classes"
+ "View Transition Types"
+ "ViewTransitionClassesEnabled"
+ "ViewTransitionTypesEnabled"
+ "WebKitAllowPrivacySensitiveOperationsInNonPersistentDataStores"
+ "WebKitAltitudeAngleEnabled"
+ "WebKitAuxclickEventEnabled"
+ "WebKitAzimuthAngleEnabled"
+ "WebKitBlobFileAccessEnforcementEnabled"
+ "WebKitCSSAppearanceBaseEnabled"
+ "WebKitCSSBackgroundClipBorderAreaEnabled"
+ "WebKitCSSColorLayersEnabled"
+ "WebKitCSSLineClampEnabled"
+ "WebKitCSSRubyAlignEnabled"
+ "WebKitCSSRubyOverhangEnabled"
+ "WebKitCSSShapeFunctionEnabled"
+ "WebKitCSSTextAutospaceEnabled"
+ "WebKitCookieStoreManagerEnabled"
+ "WebKitCrossDocumentViewTransitionsEnabled"
+ "WebKitGetCoalescedEventsEnabled"
+ "WebKitGetPredictedEventsEnabled"
+ "WebKitHTTPSByDefaultEnabled"
+ "WebKitIgnoreIframeEmbeddingProtectionsEnabled"
+ "WebKitLegacyWebRTCOfferOptionsEnabled"
+ "WebKitLoginStatusAPIRequiresWebAuthnEnabled"
+ "WebKitMediaSessionCaptureToggleAPIEnabled"
+ "WebKitObservableEnabled"
+ "WebKitPageAtRuleMarginDescriptorsEnabled"
+ "WebKitShouldUseModernAVContentKeySession"
+ "WebKitTargetTextPseudoElementEnabled"
+ "WebKitViewTransitionClassesEnabled"
+ "WebKitViewTransitionTypesEnabled"
+ "WebKitWebXRWebGPUBindingsEnabled"
+ "_setTopContentInsetForTesting:"
+ "altitudeAngle PointerEvent Property"
+ "azimuthAngle PointerEvent Property"
+ "static ObjectIdentifierGeneric<type-parameter-0-0, type-parameter-0-1, type-parameter-0-2, > WTF::ObjectIdentifierGeneric<WebCore::FrameIdentifierType, WTF::ObjectIdentifierMainThreadAccessTraits<uint64_t>, unsigned long long, WTF::SupportsObjectIdentifierNullState::Yes>::generate() [T = WebCore::FrameIdentifierType, ThreadSafety = WTF::ObjectIdentifierMainThreadAccessTraits<uint64_t>, RawValue = unsigned long long, supportsNullState = WTF::SupportsObjectIdentifierNullState::Yes]"
+ "v24@0:8{ObjectIdentifierGeneric<WebCore::DictationContextType, WTF::ObjectIdentifierMainThreadAccessTraits<uint64_t>, unsigned long long, WTF::SupportsObjectIdentifierNullState::Yes>=Q}16"
+ "v32@0:8r^{FloatRect={FloatPoint=ff}{FloatSize=ff}}16{ObjectIdentifierGeneric<WebCore::DictationContextType, WTF::ObjectIdentifierMainThreadAccessTraits<uint64_t>, unsigned long long, WTF::SupportsObjectIdentifierNullState::Yes>=Q}24"
+ "{DragData={IntPoint=ii}{IntPoint=ii}^v{OptionSet<WebCore::DragOperation>=C}{OptionSet<WebCore::DragApplicationFlags>=C}{Vector<WTF::String, 0UL, WTF::CrashOnOverflow, 16UL, WTF::FastMalloc>=^{String}II}{OptionSet<WebCore::DragDestinationAction>=C}{optional<WTF::ObjectIdentifierGeneric<WebCore::PageIdentifierType, WTF::ObjectIdentifierMainThreadAccessTraits<uint64_t>, unsigned long long, WTF::SupportsObjectIdentifierNullState::No>>=(?=c{ObjectIdentifierGeneric<WebCore::PageIdentifierType, WTF::ObjectIdentifierMainThreadAccessTraits<uint64_t>, unsigned long long, WTF::SupportsObjectIdentifierNullState::No>=Q})B}{String={RefPtr<WTF::StringImpl, WTF::RawPtrTraits<WTF::StringImpl>, WTF::DefaultRefDerefTraits<WTF::StringImpl>>=^{StringImpl}}}B}64@0:8@16{CGPoint=dd}24{CGPoint=dd}40Q56"
+ "{Vector<WTF::String, 0UL, WTF::CrashOnOverflow, 16UL, WTF::FastMalloc>=^{String}II}24@0:8{ObjectIdentifierGeneric<WebCore::DictationContextType, WTF::ObjectIdentifierMainThreadAccessTraits<uint64_t>, unsigned long long, WTF::SupportsObjectIdentifierNullState::Yes>=Q}16"
+ "{optional<WebCore::NotificationData>=\"\"(?=\"__null_state_\"c\"__val_\"{NotificationData=\"defaultActionURL\"{URL=\"m_string\"{String=\"m_impl\"{RefPtr<WTF::StringImpl, WTF::RawPtrTraits<WTF::StringImpl>, WTF::DefaultRefDerefTraits<WTF::StringImpl>>=\"m_ptr\"^{StringImpl}}}\"m_isValid\"b1\"m_protocolIsInHTTPFamily\"b1\"m_hasOpaquePath\"b1\"m_portLength\"b3\"m_schemeEnd\"b26\"m_userStart\"I\"m_userEnd\"I\"m_passwordEnd\"I\"m_hostEnd\"I\"m_pathAfterLastSlash\"I\"m_pathEnd\"I\"m_queryEnd\"I}\"title\"{String=\"m_impl\"{RefPtr<WTF::StringImpl, WTF::RawPtrTraits<WTF::StringImpl>, WTF::DefaultRefDerefTraits<WTF::StringImpl>>=\"m_ptr\"^{StringImpl}}}\"body\"{String=\"m_impl\"{RefPtr<WTF::StringImpl, WTF::RawPtrTraits<WTF::StringImpl>, WTF::DefaultRefDerefTraits<WTF::StringImpl>>=\"m_ptr\"^{StringImpl}}}\"iconURL\"{String=\"m_impl\"{RefPtr<WTF::StringImpl, WTF::RawPtrTraits<WTF::StringImpl>, WTF::DefaultRefDerefTraits<WTF::StringImpl>>=\"m_ptr\"^{StringImpl}}}\"tag\"{String=\"m_impl\"{RefPtr<WTF::StringImpl, WTF::RawPtrTraits<WTF::StringImpl>, WTF::DefaultRefDerefTraits<WTF::StringImpl>>=\"m_ptr\"^{StringImpl}}}\"language\"{String=\"m_impl\"{RefPtr<WTF::StringImpl, WTF::RawPtrTraits<WTF::StringImpl>, WTF::DefaultRefDerefTraits<WTF::StringImpl>>=\"m_ptr\"^{StringImpl}}}\"direction\"C\"originString\"{String=\"m_impl\"{RefPtr<WTF::StringImpl, WTF::RawPtrTraits<WTF::StringImpl>, WTF::DefaultRefDerefTraits<WTF::StringImpl>>=\"m_ptr\"^{StringImpl}}}\"serviceWorkerRegistrationURL\"{URL=\"m_string\"{String=\"m_impl\"{RefPtr<WTF::StringImpl, WTF::RawPtrTraits<WTF::StringImpl>, WTF::DefaultRefDerefTraits<WTF::StringImpl>>=\"m_ptr\"^{StringImpl}}}\"m_isValid\"b1\"m_protocolIsInHTTPFamily\"b1\"m_hasOpaquePath\"b1\"m_portLength\"b3\"m_schemeEnd\"b26\"m_userStart\"I\"m_userEnd\"I\"m_passwordEnd\"I\"m_hostEnd\"I\"m_pathAfterLastSlash\"I\"m_pathEnd\"I\"m_queryEnd\"I}\"notificationID\"{UUID=\"m_data\"T}\"contextIdentifier\"{optional<WebCore::ProcessQualified<WTF::UUID>>=\"\"(?=\"__null_state_\"c\"__val_\"{ProcessQualified<WTF::UUID>=\"m_object\"{UUID=\"m_data\"T}\"m_processIdentifier\"{ObjectIdentifierGeneric<WebCore::ProcessIdentifierType, WTF::ObjectIdentifierMainThreadAccessTraits<uint64_t>, unsigned long long, WTF::SupportsObjectIdentifierNullState::Yes>=\"m_identifier\"Q}})\"__engaged_\"B}\"sourceSession\"{SessionID=\"m_identifier\"Q}\"creationTime\"{MonotonicTime=\"m_value\"d}\"data\"{Vector<unsigned char, 0UL, WTF::CrashOnOverflow, 16UL, WTF::FastMalloc>=\"m_buffer\"*\"m_capacity\"I\"m_size\"I}\"silent\"{optional<bool>=\"\"(?=\"__null_state_\"c\"__val_\"B)\"__engaged_\"B}})\"__engaged_\"B}"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
- "/AppleInternal/Library/BuildRoots/1b062e2c-8703-11ef-b6f2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
- "@page CSS at-rule support"
- "CSS color-contrast()"
- "CSSColorContrastEnabled"
- "ContentKeySession support for SampleBuffer Renderers"
- "ContentKeySession support for SampleBuffer Renderers Enabled"
- "Cookie Store API for Service Workers"
- "CookieStoreAPIServiceWorkerEnabled"
- "CryptoKitEnabled"
- "Enable @page support"
- "Enable Cookie Store API for Service Workers"
- "Enable CryptoKit for supported Algorithms."
- "Enable H264 LowLatency encoder"
- "Enable HTML invoketarget & invokeaction attribute support"
- "Enable support for CSS color-contrast() defined in CSS Color 5"
- "HTML invoketarget & invokeaction attributes"
- "PageAtRuleSupportEnabled"
- "SampleBufferContentKeySessionSupportEnabled"
- "Use the Metal backend for ANGLE"
- "WebGL via Metal"
- "WebGLUsingMetal"
- "WebKitCSSColorContrastEnabled"
- "WebKitCookieStoreAPIServiceWorkerEnabled"
- "WebKitCryptoKitEnabled"
- "WebKitPageAtRuleSupportEnabled"
- "WebKitSampleBufferContentKeySessionSupportEnabled"
- "WebKitSearchInputIncrementalAttributeAndSearchEventEnabled"
- "WebKitWebGLUsingMetal"
- "WebKitWebRTCH264LowLatencyEncoderEnabled"
- "WebRTC H264 LowLatency encoder"
- "WebRTCH264LowLatencyEncoderEnabled"
- "static ObjectIdentifierGeneric<type-parameter-0-0, type-parameter-0-1, type-parameter-0-2> WTF::ObjectIdentifierGeneric<WebCore::FrameIdentifierType, WTF::ObjectIdentifierMainThreadAccessTraits<uint64_t>, unsigned long long>::generate() [T = WebCore::FrameIdentifierType, ThreadSafety = WTF::ObjectIdentifierMainThreadAccessTraits<uint64_t>, RawValue = unsigned long long]"
- "v24@0:8{ObjectIdentifierGeneric<WebCore::DictationContextType, WTF::ObjectIdentifierMainThreadAccessTraits<uint64_t>, unsigned long long>=Q}16"
- "v32@0:8r^{FloatRect={FloatPoint=ff}{FloatSize=ff}}16{ObjectIdentifierGeneric<WebCore::DictationContextType, WTF::ObjectIdentifierMainThreadAccessTraits<uint64_t>, unsigned long long>=Q}24"
- "{DragData={IntPoint=ii}{IntPoint=ii}^v{OptionSet<WebCore::DragOperation>=C}{OptionSet<WebCore::DragApplicationFlags>=C}{Vector<WTF::String, 0UL, WTF::CrashOnOverflow, 16UL, WTF::FastMalloc>=^{String}II}{OptionSet<WebCore::DragDestinationAction>=C}{optional<WTF::ObjectIdentifierGeneric<WebCore::PageIdentifierType, WTF::ObjectIdentifierMainThreadAccessTraits<uint64_t>, unsigned long long>>=(?=c{ObjectIdentifierGeneric<WebCore::PageIdentifierType, WTF::ObjectIdentifierMainThreadAccessTraits<uint64_t>, unsigned long long>=Q})B}{String={RefPtr<WTF::StringImpl, WTF::RawPtrTraits<WTF::StringImpl>, WTF::DefaultRefDerefTraits<WTF::StringImpl>>=^{StringImpl}}}B}64@0:8@16{CGPoint=dd}24{CGPoint=dd}40Q56"
- "{Vector<WTF::String, 0UL, WTF::CrashOnOverflow, 16UL, WTF::FastMalloc>=^{String}II}24@0:8{ObjectIdentifierGeneric<WebCore::DictationContextType, WTF::ObjectIdentifierMainThreadAccessTraits<uint64_t>, unsigned long long>=Q}16"
- "{optional<WebCore::NotificationData>=\"\"(?=\"__null_state_\"c\"__val_\"{NotificationData=\"defaultActionURL\"{URL=\"m_string\"{String=\"m_impl\"{RefPtr<WTF::StringImpl, WTF::RawPtrTraits<WTF::StringImpl>, WTF::DefaultRefDerefTraits<WTF::StringImpl>>=\"m_ptr\"^{StringImpl}}}\"m_isValid\"b1\"m_protocolIsInHTTPFamily\"b1\"m_hasOpaquePath\"b1\"m_portLength\"b3\"m_schemeEnd\"b26\"m_userStart\"I\"m_userEnd\"I\"m_passwordEnd\"I\"m_hostEnd\"I\"m_pathAfterLastSlash\"I\"m_pathEnd\"I\"m_queryEnd\"I}\"title\"{String=\"m_impl\"{RefPtr<WTF::StringImpl, WTF::RawPtrTraits<WTF::StringImpl>, WTF::DefaultRefDerefTraits<WTF::StringImpl>>=\"m_ptr\"^{StringImpl}}}\"body\"{String=\"m_impl\"{RefPtr<WTF::StringImpl, WTF::RawPtrTraits<WTF::StringImpl>, WTF::DefaultRefDerefTraits<WTF::StringImpl>>=\"m_ptr\"^{StringImpl}}}\"iconURL\"{String=\"m_impl\"{RefPtr<WTF::StringImpl, WTF::RawPtrTraits<WTF::StringImpl>, WTF::DefaultRefDerefTraits<WTF::StringImpl>>=\"m_ptr\"^{StringImpl}}}\"tag\"{String=\"m_impl\"{RefPtr<WTF::StringImpl, WTF::RawPtrTraits<WTF::StringImpl>, WTF::DefaultRefDerefTraits<WTF::StringImpl>>=\"m_ptr\"^{StringImpl}}}\"language\"{String=\"m_impl\"{RefPtr<WTF::StringImpl, WTF::RawPtrTraits<WTF::StringImpl>, WTF::DefaultRefDerefTraits<WTF::StringImpl>>=\"m_ptr\"^{StringImpl}}}\"direction\"C\"originString\"{String=\"m_impl\"{RefPtr<WTF::StringImpl, WTF::RawPtrTraits<WTF::StringImpl>, WTF::DefaultRefDerefTraits<WTF::StringImpl>>=\"m_ptr\"^{StringImpl}}}\"serviceWorkerRegistrationURL\"{URL=\"m_string\"{String=\"m_impl\"{RefPtr<WTF::StringImpl, WTF::RawPtrTraits<WTF::StringImpl>, WTF::DefaultRefDerefTraits<WTF::StringImpl>>=\"m_ptr\"^{StringImpl}}}\"m_isValid\"b1\"m_protocolIsInHTTPFamily\"b1\"m_hasOpaquePath\"b1\"m_portLength\"b3\"m_schemeEnd\"b26\"m_userStart\"I\"m_userEnd\"I\"m_passwordEnd\"I\"m_hostEnd\"I\"m_pathAfterLastSlash\"I\"m_pathEnd\"I\"m_queryEnd\"I}\"notificationID\"{UUID=\"m_data\"T}\"contextIdentifier\"{ProcessQualified<WTF::UUID>=\"m_object\"{UUID=\"m_data\"T}\"m_processIdentifier\"{ObjectIdentifierGeneric<WebCore::ProcessIdentifierType, WTF::ObjectIdentifierMainThreadAccessTraits<uint64_t>, unsigned long long>=\"m_identifier\"Q}}\"sourceSession\"{SessionID=\"m_identifier\"Q}\"creationTime\"{MonotonicTime=\"m_value\"d}\"data\"{Vector<unsigned char, 0UL, WTF::CrashOnOverflow, 16UL, WTF::FastMalloc>=\"m_buffer\"*\"m_capacity\"I\"m_size\"I}\"silent\"{optional<bool>=\"\"(?=\"__null_state_\"c\"__val_\"B)\"__engaged_\"B}})\"__engaged_\"B}"

```
