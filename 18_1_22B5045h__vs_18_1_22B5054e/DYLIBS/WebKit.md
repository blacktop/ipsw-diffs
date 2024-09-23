## WebKit

> `/System/Library/Frameworks/WebKit.framework/WebKit`

```diff

-619.2.3.1.0
-  __TEXT.__text: 0xe4db60
-  __TEXT.__auth_stubs: 0x16da0
+619.2.5.10.3
+  __TEXT.__text: 0xe523dc
+  __TEXT.__auth_stubs: 0x16d80
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x1423c
+  __TEXT.__objc_methlist: 0x14244
   __TEXT.__const: 0x3820
-  __TEXT.__gcc_except_tab: 0x5b62c
-  __TEXT.__cstring: 0x792d7
-  __TEXT.__oslogstring: 0x3851f
+  __TEXT.__gcc_except_tab: 0x5b838
+  __TEXT.__cstring: 0x79709
+  __TEXT.__oslogstring: 0x3884a
   __TEXT.__ustring: 0xc9c
-  __TEXT.__unwind_info: 0x272d0
+  __TEXT.__unwind_info: 0x277e0
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x2fa5
-  __TEXT.__objc_methname: 0x441e7
-  __TEXT.__objc_methtype: 0x2def2
-  __TEXT.__objc_stubs: 0x28780
+  __TEXT.__objc_methname: 0x441d9
+  __TEXT.__objc_methtype: 0x2df40
+  __TEXT.__objc_stubs: 0x28760
   __DATA_CONST.__got: 0x1a90
-  __DATA_CONST.__const: 0x193d8
+  __DATA_CONST.__const: 0x193f0
   __DATA_CONST.__objc_classlist: 0xad8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x3e8

   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x960
   __DATA_CONST.__objc_arraydata: 0x688
-  __AUTH_CONST.__auth_got: 0xb6e8
+  __AUTH_CONST.__auth_got: 0xb6d8
   __AUTH_CONST.__auth_ptr: 0x70
-  __AUTH_CONST.__const: 0x5b570
+  __AUTH_CONST.__const: 0x5b780
   __AUTH_CONST.__cfstring: 0x12de0
-  __AUTH_CONST.__objc_const: 0x2cdc0
+  __AUTH_CONST.__objc_const: 0x2ce00
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x208
   __AUTH_CONST.__objc_intobj: 0x5e8
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x4b00
-  __AUTH.__data: 0x2c0
-  __DATA.__objc_ivar: 0xec8
+  __AUTH.__objc_data: 0x4ab0
+  __AUTH.__data: 0x2a0
+  __DATA.__objc_ivar: 0xecc
   __DATA.__data: 0x3298
-  __DATA.__bss: 0x770
-  __DATA.__common: 0x658
+  __DATA.__bss: 0x6c0
+  __DATA.__common: 0x640
   __DATA_DIRTY.__objc_ivar: 0x50c
-  __DATA_DIRTY.__objc_data: 0x2170
-  __DATA_DIRTY.__data: 0x5730
-  __DATA_DIRTY.__bss: 0x19b8
-  __DATA_DIRTY.__common: 0x2949
+  __DATA_DIRTY.__objc_data: 0x21c0
+  __DATA_DIRTY.__data: 0x5750
+  __DATA_DIRTY.__bss: 0x1a70
+  __DATA_DIRTY.__common: 0x2951
   - /System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 63639
-  Symbols:   76666
-  CStrings:  25667
+  Functions: 63687
+  Symbols:   76720
+  CStrings:  25683
 
Symbols:
+ __ZN7WebCore9IDBServer28UniqueIDBDatabaseTransaction11deleteIndexERKNS_14IDBRequestDataEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS5_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS5_6StringE
+ __ZN7WebCore14IDBRequestDataC1EN3WTF23ObjectIdentifierGenericINS_21ProcessIdentifierTypeENS1_38ObjectIdentifierMainThreadAccessTraitsIyEEyEENS_21IDBResourceIdentifierES7_ONSt3__18optionalIS7_EENS9_INS2_INS_28IDBObjectStoreIdentifierTypeENS1_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEEEEyNS_9IndexedDB15IndexRecordTypeEyNSH_11RequestTypeE
+ __ZN7WebCore18IDBObjectStoreInfoC1EN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS1_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS1_6StringEONSt3__18optionalINSA_7variantIJS7_NS1_6VectorIS7_Lm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEEEEEEEbONS1_7HashMapIyNS_12IDBIndexInfoENS1_11DefaultHashIyEENS1_10HashTraitsIyEENSO_ISL_EENS1_15HashTableTraitsEEE
+ __ZN7WebCore9IDBServer28UniqueIDBDatabaseTransaction17renameObjectStoreERKNS_14IDBRequestDataEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS5_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS5_6StringE
+ __ZN7WebCore13IDBCursorInfoC1ERKNS_21IDBResourceIdentifierES3_N3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS4_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEEyRKNS_15IDBKeyRangeDataENS_9IndexedDB12CursorSourceENSD_15CursorDirectionENSD_10CursorTypeE
+ __ZN7WebCore9IDBServer28UniqueIDBDatabaseTransaction11renameIndexERKNS_14IDBRequestDataEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS5_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEEyRKNS5_6StringE
+ __ZN7WebCore9IDBServer28UniqueIDBDatabaseTransaction16clearObjectStoreERKNS_14IDBRequestDataEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS5_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEE
+ __ZN7WebCore22EmptyFrameLoaderClient39dispatchDecidePolicyForNavigationActionERKNS_16NavigationActionERKNS_15ResourceRequestERKNS_16ResourceResponseEPNS_9FormStateERKN3WTF6StringENSC_23ObjectIdentifierGenericINS_24NavigationIdentifierTypeENSC_38ObjectIdentifierMainThreadAccessTraitsIyEEyEEONSt3__18optionalINS_13HitTestResultEEEbiNS_18PolicyDecisionModeEONSC_17CompletionHandlerIFvNS_12PolicyActionEEEE
+ __ZN7WebCore4Page37intelligenceTextAnimationsDidCompleteEv
+ __ZN7WebCore15IDBDatabaseInfoC1ERKN3WTF6StringEyyONS1_7HashMapINS1_23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS1_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEENS_18IDBObjectStoreInfoENS1_11DefaultHashISA_EENS1_10HashTraitsISA_EENSE_ISB_EENS1_15HashTableTraitsEEE
+ __ZN7WebCore12IDBIndexInfoC1EyN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS1_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS1_6StringEONSt3__17variantIJS7_NS1_6VectorIS7_Lm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEEEEEbb
+ __ZN7WebCore14DocumentLoader15setNavigationIDEN3WTF23ObjectIdentifierGenericINS_24NavigationIdentifierTypeENS1_38ObjectIdentifierMainThreadAccessTraitsIyEEyEE
- __ZN7WebCore9IDBServer28UniqueIDBDatabaseTransaction17renameObjectStoreERKNS_14IDBRequestDataEyRKN3WTF6StringE
- __ZN7WebCore9IDBServer28UniqueIDBDatabaseTransaction11renameIndexERKNS_14IDBRequestDataEyyRKN3WTF6StringE
- __ZN7WebCore9IDBServer28UniqueIDBDatabaseTransaction16clearObjectStoreERKNS_14IDBRequestDataEy
- __ZN7WebCore12IDBIndexInfoC1EyyRKN3WTF6StringEONSt3__17variantIJS2_NS1_6VectorIS2_Lm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEEEEEbb
- __ZN7WebCore13IDBCursorInfoC1ERKNS_21IDBResourceIdentifierES3_yyRKNS_15IDBKeyRangeDataENS_9IndexedDB12CursorSourceENS7_15CursorDirectionENS7_10CursorTypeE
- __ZN7WebCore9IDBServer28UniqueIDBDatabaseTransaction11deleteIndexERKNS_14IDBRequestDataEyRKN3WTF6StringE
- __ZN7WebCore14IDBRequestDataC1EN3WTF23ObjectIdentifierGenericINS_21ProcessIdentifierTypeENS1_38ObjectIdentifierMainThreadAccessTraitsIyEEyEENS_21IDBResourceIdentifierES7_ONSt3__18optionalIS7_EEyyNS_9IndexedDB15IndexRecordTypeEyNSC_11RequestTypeE
- __ZN7WebCore22EmptyFrameLoaderClient39dispatchDecidePolicyForNavigationActionERKNS_16NavigationActionERKNS_15ResourceRequestERKNS_16ResourceResponseEPNS_9FormStateERKN3WTF6StringEyONSt3__18optionalINS_13HitTestResultEEEbiNS_18PolicyDecisionModeEONSC_17CompletionHandlerIFvNS_12PolicyActionEEEE
- __ZN7WebCore18IDBObjectStoreInfoC1Ev
- __ZN7WebCore12IDBIndexInfoC1Ev
- __ZNK7WebCore4Page41showSelectionForActiveWritingToolsSessionEv
- __ZN7WebCore18IDBObjectStoreInfoC1EyRKN3WTF6StringEONSt3__18optionalINS5_7variantIJS2_NS1_6VectorIS2_Lm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEEEEEEEbONS1_7HashMapIyNS_12IDBIndexInfoENS1_11DefaultHashIyEENS1_10HashTraitsIyEENSJ_ISG_EENS1_15HashTableTraitsEEE
- __ZN7WebCore14DocumentLoader15setNavigationIDEy
- __ZN7WebCore15IDBDatabaseInfoC1ERKN3WTF6StringEyyyONS1_7HashMapIyNS_18IDBObjectStoreInfoENS1_11DefaultHashIyEENS1_10HashTraitsIyEENS9_IS6_EENS1_15HashTableTraitsEEE
CStrings:
+ "callCompletionHandlerForAnimationID:completionHandler:"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6118: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9773: Invalid message dispatched %!s(MISSING)"
+ "void WebKit::WebPageProxy::didSameDocumentNavigationForFrame(IPC::Connection &, FrameIdentifier, std::optional<WebCore::NavigationIdentifier>, SameDocumentNavigationType, URL &&, const UserData &)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5519: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7447: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6685: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12777: Invalid message dispatched %!s(MISSING)"
+ "_databaseSchemaVersion"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/StorageNamespaceProvider.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5951: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7529: Invalid message dispatched %!s(MISSING)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8143: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12806: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7446: Invalid message dispatched %!s(MISSING)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "sendFrameToDecode"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12865: Invalid message dispatched %!s(MISSING)"
+ "%!p(MISSING) - [pageProxyID=%!l(MISSING)lu, webPageID=%!l(MISSING)lu, PID=%!i(MISSING)] WebPageProxy::updateThrottleState: taking a web process background assertion for muted media capture"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9729: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/WebPageProxyCocoa.mm 1338: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6225: Invalid message dispatched %!s(MISSING)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7610: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10973: Invalid message dispatched %!s(MISSING)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/RealtimeMediaSourceCapabilities.h"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7582: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12751: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7658: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6775: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6394: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/VideoPresentationManagerProxy.mm 1061: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8127: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6622: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8037: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9713: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8126: Invalid message dispatched %!s(MISSING)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/WebKitAdditions/DyldCallbackAdditions.h"
+ "Muted capture assertion is invalidated"
+ "Cleared queued message(s) for port channel %!{(MISSING)public}llu in %!{(MISSING)public}@ world"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6089: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6258: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12589: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7057: Invalid message dispatched %!s(MISSING)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/SecurityOriginData.h"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12775: Invalid message dispatched %!s(MISSING)"
+ "WebKit::NetworkResourceLoadParameters::NetworkResourceLoadParameters(NetworkLoadParameters &&, WebCore::ResourceLoaderIdentifier, RefPtr<WebCore::FormData> &&, std::optional<Vector<SandboxExtension::Handle>> &&, std::optional<SandboxExtension::Handle> &&, Seconds, WebCore::FetchOptions &&, std::optional<WebCore::ContentSecurityPolicyResponseHeaders> &&, URL &&, URL &&, WebCore::CrossOriginEmbedderPolicy, WebCore::CrossOriginEmbedderPolicy, WebCore::HTTPHeaderMap &&, bool, WebCore::PreflightPolicy, bool, Vector<Ref<WebCore::SecurityOrigin>> &&, bool, std::optional<WebCore::FrameIdentifier>, bool, URL &&, bool, bool, bool, WebCore::SandboxFlags, URL &&, WebCore::CrossOriginOpenerPolicy &&, std::optional<WebCore::NavigationIdentifier>, std::optional<WebCore::NavigationRequester> &&, WebCore::ServiceWorkersMode, std::optional<WebCore::ServiceWorkerRegistrationIdentifier>, OptionSet<WebCore::HTTPHeadersToKeepFromCleaning>, std::optional<WebCore::FetchIdentifier>, URL &&, std::optional<UserContentControllerIdentifier>, bool, bool, bool)"
+ "void WebKit::WebPageProxy::didReceiveServerRedirectForProvisionalLoadForFrameShared(Ref<WebProcessProxy> &&, FrameIdentifier, std::optional<WebCore::NavigationIdentifier>, ResourceRequest &&, const UserData &)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebNavigationState.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6193: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8621: Invalid message dispatched %!s(MISSING)"
+ "void WebKit::WebPageProxy::didFinishLoadForFrame(IPC::Connection &, FrameIdentifier, FrameInfoData &&, ResourceRequest &&, std::optional<WebCore::NavigationIdentifier>, const UserData &)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5507: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9478: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10812: Invalid message dispatched %!s(MISSING)"
+ "{RetainPtr<NSMutableDictionary<NSUUID *,NSUUID *>>=\"m_ptr\"^v}"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7532: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12573: Invalid message dispatched %!s(MISSING)"
+ "WebPage_IntelligenceTextAnimationsDidComplete"
+ "void WebKit::WebPageProxy::didCommitLoadForFrame(IPC::Connection &, FrameIdentifier, FrameInfoData &&, ResourceRequest &&, std::optional<WebCore::NavigationIdentifier>, const String &, bool, FrameLoadType, const CertificateInfo &, bool, bool, bool, HasInsecureContent, MouseEventPolicy, const UserData &)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11028: Invalid message dispatched %!s(MISSING)"
+ "void WebKit::WebPageProxy::didStartProvisionalLoadForFrameShared(Ref<WebProcessProxy> &&, FrameIdentifier, FrameInfoData &&, ResourceRequest &&, std::optional<WebCore::NavigationIdentifier>, URL &&, URL &&, const UserData &)"
+ "v32@0:8@16r^{TextAnimationData=CC{UUID=T}{UUID=T}{UUID=T}}24"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10810: Invalid message dispatched %!s(MISSING)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/pal/spi/cocoa/NSAttributedStringSPI.h"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12864: Invalid message dispatched %!s(MISSING)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6257: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6289: Invalid message dispatched %!s(MISSING)"
+ "void WebKit::WebPageProxy::decidePolicyForResponseShared(Ref<WebProcessProxy> &&, PageIdentifier, FrameInfoData &&, std::optional<WebCore::NavigationIdentifier>, const ResourceResponse &, const ResourceRequest &, bool, const String &, bool, WebCore::CrossOriginOpenerPolicyValue, CompletionHandler<void (PolicyDecision &&)> &&)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7559: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6774: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6735: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7898: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8616: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7581: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8747: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/VideoPresentationManagerProxy.mm 1054: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6256: Invalid message dispatched %!s(MISSING)"
+ "void WebKit::ProvisionalPageProxy::didFailProvisionalLoadForFrame(FrameInfoData &&, ResourceRequest &&, std::optional<WebCore::NavigationIdentifier>, const String &, const WebCore::ResourceError &, WebCore::WillContinueLoading, const UserData &, WebCore::WillInternallyHandleFailure)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7359: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6090: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9390: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7657: Invalid message dispatched %!s(MISSING)"
+ "Decoding task failed"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6560: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5929: Invalid message dispatched %!s(MISSING)"
+ "void WebKit::WebPageProxy::didFailProvisionalLoadForFrameShared(Ref<WebProcessProxy> &&, WebFrameProxy &, FrameInfoData &&, WebCore::ResourceRequest &&, std::optional<WebCore::NavigationIdentifier>, const String &, const ResourceError &, WillContinueLoading, const UserData &, WillInternallyHandleFailure)"
+ "void WebKit::WebPageProxy::decidePolicyForResponse(IPC::Connection &, FrameInfoData &&, std::optional<WebCore::NavigationIdentifier>, const ResourceResponse &, const ResourceRequest &, bool, const String &, bool, WebCore::CrossOriginOpenerPolicyValue, CompletionHandler<void (PolicyDecision &&)> &&)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12591: Invalid message dispatched %!s(MISSING)"
+ "LibWebRTCCodecsProxy_DecodeFrameReply"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12850: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6061: Invalid message dispatched %!s(MISSING)"
+ "void WebKit::WebPageProxy::didChangeProvisionalURLForFrameShared(Ref<WebProcessProxy> &&, FrameIdentifier, std::optional<WebCore::NavigationIdentifier>, URL &&)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9382: Invalid message dispatched %!s(MISSING)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/JSONValues.h"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7611: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12717: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6882: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7627: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12646: Invalid message dispatched %!s(MISSING)"
+ "void WebKit::WebPageProxy::didFinishDocumentLoadForFrame(IPC::Connection &, FrameIdentifier, std::optional<WebCore::NavigationIdentifier>, const UserData &)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7626: Invalid message dispatched %!s(MISSING)"
+ "{ObjectStorage<API::NavigationAction>=\"data\"{type=\"__lx\"[2896C]}}"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7437: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6976: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9510: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9586: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10796: Invalid message dispatched %!s(MISSING)"
+ "%!p(MISSING) - [pageProxyID=%!l(MISSING)lu, webPageID=%!l(MISSING)lu, PID=%!i(MISSING)] WebPageProxy::updateThrottleState: releasing a web process background assertion for muted media capture"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12759: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 3798: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9507: Invalid message dispatched %!s(MISSING)"
+ "removeClientForContext"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7921: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9697: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7408: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6736: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8921: Invalid message dispatched %!s(MISSING)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
+ "%!p(MISSING) - [pageProxyID=%!l(MISSING)lu, webPageID=%!l(MISSING)lu, frameID=%!l(MISSING)lu, resourceID=%!l(MISSING)lu, isMainResource=%!d(MISSING), destination=%!u(MISSING), isSynchronous=%!d(MISSING)] NetworkResourceLoader::sendDidReceiveResponsePotentiallyInNewBrowsingContextGroup: Missing navigationID, loaderIdentifier %!l(MISSING)lu, m_isKeptAlive=%!d(MISSING), needsContinueDidReceiveResponseMessage=%!d(MISSING)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xc2\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0a"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6273: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6192: Invalid message dispatched %!s(MISSING)"
+ "void WebKit::WebNavigationState::didDestroyNavigation(WebCore::ProcessIdentifier, WebCore::NavigationIdentifier)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9828: Invalid message dispatched %!s(MISSING)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7613: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7614: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12571: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7560: Invalid message dispatched %!s(MISSING)"
+ "{ObjectStorage<API::Navigation>=\"data\"{type=\"__lx\"[3504C]}}"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7659: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8669: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12718: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12580: Invalid message dispatched %!s(MISSING)"
+ "API::Navigation *WebKit::WebNavigationState::navigation(WebCore::NavigationIdentifier)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6962: Invalid message dispatched %!s(MISSING)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/GCGLSpan.h"
+ "RefPtr<API::Navigation> WebKit::WebNavigationState::takeNavigation(WebCore::NavigationIdentifier)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/VideoPresentationManagerProxy.mm 913: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7435: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12638: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7629: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/VideoPresentationManagerProxy.mm 1040: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6931: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9481: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7583: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12851: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8098: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12776: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11050: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 2444: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7448: Invalid message dispatched %!s(MISSING)"
+ "auto WebKit::WebPageProxy::decidePolicyForResponseShared(Ref<WebProcessProxy> &&, PageIdentifier, FrameInfoData &&, std::optional<WebCore::NavigationIdentifier>, const ResourceResponse &, const ResourceRequest &, bool, const String &, bool, WebCore::CrossOriginOpenerPolicyValue, CompletionHandler<void (PolicyDecision &&)> &&)::(anonymous class)::operator()(PolicyAction, API::WebsitePolicies *, ProcessSwapRequestedByClient, RefPtr<SafeBrowsingWarning> &&, std::optional<NavigatingToAppBoundDomain>, WasNavigationIntercepted)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5513: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7009: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8706: Invalid message dispatched %!s(MISSING)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13997: Invalid message dispatched %!s(MISSING)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12732: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7875: Invalid message dispatched %!s(MISSING)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7580: Invalid message dispatched %!s(MISSING)"
+ "void WebKit::WebPageProxy::didFailProvisionalLoadForFrame(IPC::Connection &, FrameInfoData &&, ResourceRequest &&, std::optional<WebCore::NavigationIdentifier>, const String &, const ResourceError &, WillContinueLoading, const UserData &, WillInternallyHandleFailure)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5928: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8133: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12582: Invalid message dispatched %!s(MISSING)"
+ "addTextAnimationForAnimationID:withData:"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12750: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10991: Invalid message dispatched %!s(MISSING)"
+ "void WebKit::WebPageProxy::didFailLoadForFrame(IPC::Connection &, FrameIdentifier, FrameInfoData &&, ResourceRequest &&, std::optional<WebCore::NavigationIdentifier>, const ResourceError &, const UserData &)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6091: Invalid message dispatched %!s(MISSING)"
+ "void WebKit::WebPageProxy::didDestroyNavigationShared(Ref<WebProcessProxy> &&, WebCore::NavigationIdentifier)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12733: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14041: Invalid message dispatched %!s(MISSING)"
+ "%!p(MISSING) - [pageProxyID=%!l(MISSING)lu, webPageID=%!l(MISSING)lu, PID=%!i(MISSING)] WebPageProxy::didCleanupFullscreen"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6288: Invalid message dispatched %!s(MISSING)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Ref.h"
+ "_sourceAnimationIDtoDestinationAnimationID"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7361: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7407: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7535: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8125: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9789: Invalid message dispatched %!s(MISSING)"
+ "WebKit Muted Media Capture"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 2450: Invalid message dispatched %!s(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9745: Invalid message dispatched %!s(MISSING)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/ImageBufferPixelFormat.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/pal/spi/cocoa/NSAttributedStringSPI.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8001: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10774: Invalid message dispatched %!s(MISSING)"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9677: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7524: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/WebPageProxyCocoa.mm 1310: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7525: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9792: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8885: Invalid message dispatched %!s(MISSING)"
- "WebPage_ShowSelectionForActiveWritingToolsSession"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 2425: Invalid message dispatched %!s(MISSING)"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10955: Invalid message dispatched %!s(MISSING)"
- "void WebKit::WebPageProxy::decidePolicyForResponse(IPC::Connection &, FrameInfoData &&, uint64_t, const ResourceResponse &, const ResourceRequest &, bool, const String &, bool, WebCore::CrossOriginOpenerPolicyValue, CompletionHandler<void (PolicyDecision &&)> &&)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9550: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7547: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/VideoPresentationManagerProxy.mm 1035: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14005: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5478: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6122: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7885: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/VideoPresentationManagerProxy.mm 1056: Invalid message dispatched %!s(MISSING)"
- "void WebKit::WebPageProxy::didCommitLoadForFrame(IPC::Connection &, FrameIdentifier, FrameInfoData &&, ResourceRequest &&, uint64_t, const String &, bool, FrameLoadType, const CertificateInfo &, bool, bool, bool, HasInsecureContent, MouseEventPolicy, const UserData &)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7326: Invalid message dispatched %!s(MISSING)"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/WebKitAdditions/DyldCallbackAdditions.h"
- "auto WebKit::WebPageProxy::decidePolicyForResponseShared(Ref<WebProcessProxy> &&, PageIdentifier, FrameInfoData &&, uint64_t, const ResourceResponse &, const ResourceRequest &, bool, const String &, bool, WebCore::CrossOriginOpenerPolicyValue, CompletionHandler<void (PolicyDecision &&)> &&)::(anonymous class)::operator()(PolicyAction, API::WebsitePolicies *, ProcessSwapRequestedByClient, RefPtr<SafeBrowsingWarning> &&, std::optional<NavigatingToAppBoundDomain>, WasNavigationIntercepted)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7545: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8634: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10992: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7548: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12739: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7839: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6056: Invalid message dispatched %!s(MISSING)"
- "WebKit::NetworkResourceLoadParameters::NetworkResourceLoadParameters(NetworkLoadParameters &&, WebCore::ResourceLoaderIdentifier, RefPtr<WebCore::FormData> &&, std::optional<Vector<SandboxExtension::Handle>> &&, std::optional<SandboxExtension::Handle> &&, Seconds, WebCore::FetchOptions &&, std::optional<WebCore::ContentSecurityPolicyResponseHeaders> &&, URL &&, URL &&, WebCore::CrossOriginEmbedderPolicy, WebCore::CrossOriginEmbedderPolicy, WebCore::HTTPHeaderMap &&, bool, WebCore::PreflightPolicy, bool, Vector<Ref<WebCore::SecurityOrigin>> &&, bool, std::optional<WebCore::FrameIdentifier>, bool, URL &&, bool, bool, bool, WebCore::SandboxFlags, URL &&, WebCore::CrossOriginOpenerPolicy &&, uint64_t, std::optional<WebCore::NavigationRequester> &&, WebCore::ServiceWorkersMode, std::optional<WebCore::ServiceWorkerRegistrationIdentifier>, OptionSet<WebCore::HTTPHeadersToKeepFromCleaning>, std::optional<WebCore::FetchIdentifier>, URL &&, std::optional<UserContentControllerIdentifier>, bool, bool, bool)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5894: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12681: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12610: Invalid message dispatched %!s(MISSING)"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12696: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12740: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7594: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6223: Invalid message dispatched %!s(MISSING)"
- "void WebKit::ProvisionalPageProxy::didFailProvisionalLoadForFrame(FrameInfoData &&, ResourceRequest &&, uint64_t, const String &, const WebCore::ResourceError &, WebCore::WillContinueLoading, const UserData &, WebCore::WillInternallyHandleFailure)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12828: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9354: Invalid message dispatched %!s(MISSING)"
- "void WebKit::WebPageProxy::didDestroyNavigationShared(Ref<WebProcessProxy> &&, uint64_t)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6190: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6740: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9693: Invalid message dispatched %!s(MISSING)"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/SecurityOriginData.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7862: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7022: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12697: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6253: Invalid message dispatched %!s(MISSING)"
- "_disableTextIndicatorStylingWithUUID:"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7494: Invalid message dispatched %!s(MISSING)"
- "void WebKit::WebPageProxy::didStartProvisionalLoadForFrameShared(Ref<WebProcessProxy> &&, FrameIdentifier, FrameInfoData &&, ResourceRequest &&, uint64_t, URL &&, URL &&, const UserData &)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6739: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7575: Invalid message dispatched %!s(MISSING)"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/StorageNamespaceProvider.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12555: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5916: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9471: Invalid message dispatched %!s(MISSING)"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Ref.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/GCGLSpan.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7402: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8585: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8062: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8097: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7578: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7497: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6974: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12537: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10776: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13961: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6222: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6650: Invalid message dispatched %!s(MISSING)"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12553: Invalid message dispatched %!s(MISSING)"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xc2\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0A"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8090: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6701: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9445: Invalid message dispatched %!s(MISSING)"
- "_enableTextIndicatorStylingForElementWithID:"
- "void WebKit::WebPageProxy::didFinishLoadForFrame(IPC::Connection &, FrameIdentifier, FrameInfoData &&, ResourceRequest &&, uint64_t, const UserData &)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12546: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6359: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8580: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6221: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7624: Invalid message dispatched %!s(MISSING)"
- "void WebKit::WebPageProxy::didFailProvisionalLoadForFrameShared(Ref<WebProcessProxy> &&, WebFrameProxy &, FrameInfoData &&, WebCore::ResourceRequest &&, uint64_t, const String &, const ResourceError &, WillContinueLoading, const UserData &, WillInternallyHandleFailure)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10760: Invalid message dispatched %!s(MISSING)"
- "v32@0:8@16r^{TextAnimationData=CC{UUID=T}}24"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6203: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5893: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7373: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6941: Invalid message dispatched %!s(MISSING)"
- "void WebKit::WebPageProxy::didChangeProvisionalURLForFrameShared(Ref<WebProcessProxy> &&, FrameIdentifier, uint64_t, URL &&)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7411: Invalid message dispatched %!s(MISSING)"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/RealtimeMediaSourceCapabilities.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7579: Invalid message dispatched %!s(MISSING)"
- "{ObjectStorage<API::Navigation>=\"data\"{type=\"__lx\"[3488C]}}"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6055: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12815: Invalid message dispatched %!s(MISSING)"
- "void WebKit::WebPageProxy::didSameDocumentNavigationForFrame(IPC::Connection &, FrameIdentifier, uint64_t, SameDocumentNavigationType, URL &&, const UserData &)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6054: Invalid message dispatched %!s(MISSING)"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/ImageBufferPixelFormat.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12715: Invalid message dispatched %!s(MISSING)"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6254: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9709: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9442: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7412: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7622: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7400: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9737: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9346: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7500: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7337: Invalid message dispatched %!s(MISSING)"
- "void WebKit::WebPageProxy::didFinishDocumentLoadForFrame(IPC::Connection &, FrameIdentifier, uint64_t, const UserData &)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6083: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12829: Invalid message dispatched %!s(MISSING)"
- "{ObjectStorage<API::NavigationAction>=\"data\"{type=\"__lx\"[2880C]}}"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12770: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8091: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8089: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11014: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6026: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/VideoPresentationManagerProxy.mm 1049: Invalid message dispatched %!s(MISSING)"
- "void WebKit::WebPageProxy::didReceiveServerRedirectForProvisionalLoadForFrameShared(Ref<WebProcessProxy> &&, FrameIdentifier, uint64_t, ResourceRequest &&, const UserData &)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12714: Invalid message dispatched %!s(MISSING)"
- "void WebKit::WebPageProxy::didFailLoadForFrame(IPC::Connection &, FrameIdentifier, FrameInfoData &&, ResourceRequest &&, uint64_t, const ResourceError &, const UserData &)"
- "_intelligenceTextPonderingAnimationIsComplete"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9474: Invalid message dispatched %!s(MISSING)"
- "void WebKit::WebPageProxy::decidePolicyForResponseShared(Ref<WebProcessProxy> &&, PageIdentifier, FrameInfoData &&, uint64_t, const ResourceResponse &, const ResourceRequest &, bool, const String &, bool, WebCore::CrossOriginOpenerPolicyValue, CompletionHandler<void (PolicyDecision &&)> &&)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 3763: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8633: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12602: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12814: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9753: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6927: Invalid message dispatched %!s(MISSING)"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6700: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9661: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/VideoPresentationManagerProxy.mm 908: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7546: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6847: Invalid message dispatched %!s(MISSING)"
- "void WebKit::WebPageProxy::didFailProvisionalLoadForFrame(IPC::Connection &, FrameInfoData &&, ResourceRequest &&, uint64_t, const String &, const ResourceError &, WillContinueLoading, const UserData &, WillInternallyHandleFailure)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6587: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7324: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12544: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12535: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6525: Invalid message dispatched %!s(MISSING)"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/JSONValues.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6158: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12741: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12723: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7592: Invalid message dispatched %!s(MISSING)"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 2419: Invalid message dispatched %!s(MISSING)"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12682: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7623: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7591: Invalid message dispatched %!s(MISSING)"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7413: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8107: Invalid message dispatched %!s(MISSING)"
- "_enableTextIndicatorStylingAfterElementWithID:"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5472: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6896: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5484: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10937: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7576: Invalid message dispatched %!s(MISSING)"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8711: Invalid message dispatched %!s(MISSING)"

```
