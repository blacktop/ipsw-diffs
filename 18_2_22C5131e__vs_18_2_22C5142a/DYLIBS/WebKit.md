## WebKit

> `/System/Library/Frameworks/WebKit.framework/WebKit`

```diff

-620.1.15.10.3
-  __TEXT.__text: 0xeb70f0
-  __TEXT.__auth_stubs: 0x171d0
+620.1.16.10.8
+  __TEXT.__text: 0xed44bc
+  __TEXT.__auth_stubs: 0x17230
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x14b74
-  __TEXT.__const: 0x3920
-  __TEXT.__gcc_except_tab: 0x5f4a0
-  __TEXT.__cstring: 0x86c68
-  __TEXT.__oslogstring: 0x3d603
+  __TEXT.__objc_methlist: 0x14be4
+  __TEXT.__const: 0x3960
+  __TEXT.__gcc_except_tab: 0x600a8
+  __TEXT.__cstring: 0x8aeb8
+  __TEXT.__oslogstring: 0x3d597
   __TEXT.__ustring: 0xcd4
-  __TEXT.__unwind_info: 0x282c8
+  __TEXT.__unwind_info: 0x28410
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x32e5
-  __TEXT.__objc_methname: 0x46684
-  __TEXT.__objc_methtype: 0x35d2a
-  __TEXT.__objc_stubs: 0x29a60
+  __TEXT.__objc_methname: 0x46998
+  __TEXT.__objc_methtype: 0x35da7
+  __TEXT.__objc_stubs: 0x29b00
   __DATA_CONST.__got: 0x1ba8
-  __DATA_CONST.__const: 0x19e18
+  __DATA_CONST.__const: 0x19f20
   __DATA_CONST.__objc_classlist: 0xba8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x410
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf088
+  __DATA_CONST.__objc_selrefs: 0xf0f8
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x9b0
   __DATA_CONST.__objc_arraydata: 0x688
-  __AUTH_CONST.__auth_got: 0xb900
+  __AUTH_CONST.__auth_got: 0xb930
   __AUTH_CONST.__auth_ptr: 0x70
-  __AUTH_CONST.__const: 0x5dd80
+  __AUTH_CONST.__const: 0x5e068
   __AUTH_CONST.__cfstring: 0x13ae0
-  __AUTH_CONST.__objc_const: 0x2e948
+  __AUTH_CONST.__objc_const: 0x2e9a8
   __AUTH_CONST.__objc_intobj: 0x630
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x208
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x5190
-  __AUTH.__data: 0x2c8
+  __AUTH.__data: 0x2e0
   __DATA.__objc_ivar: 0xf40
-  __DATA.__data: 0x34a8
-  __DATA.__bss: 0xb90
-  __DATA.__common: 0x528
-  __DATA_DIRTY.__objc_ivar: 0x528
+  __DATA.__data: 0x34c8
+  __DATA.__bss: 0x838
+  __DATA.__common: 0x5b0
+  __DATA_DIRTY.__objc_ivar: 0x530
   __DATA_DIRTY.__objc_data: 0x2300
-  __DATA_DIRTY.__data: 0x5a20
-  __DATA_DIRTY.__bss: 0x1818
-  __DATA_DIRTY.__common: 0x2a71
+  __DATA_DIRTY.__data: 0x5a10
+  __DATA_DIRTY.__bss: 0x1b00
+  __DATA_DIRTY.__common: 0x2a79
   - /System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 65257
-  Symbols:   78379
-  CStrings:  26637
+  Functions: 64914
+  Symbols:   77975
+  CStrings:  26672
 
Symbols:
+ __ZN4fido31encodeGetAssertionRequestAsCBORERKN3WTF6VectorIhLm0ENS0_15CrashOnOverflowELm16ENS0_10FastMallocEEERKN7WebCore33PublicKeyCredentialRequestOptionsENS_29AuthenticatorSupportedOptions28UserVerificationAvailabilityERKNS1_INS0_6StringELm0ES2_Lm16ES3_EENSt3__18optionalINS_13PinParametersEEE
+ __ZN4fido33encodeMakeCredentialRequestAsCBORERKN3WTF6VectorIhLm0ENS0_15CrashOnOverflowELm16ENS0_10FastMallocEEERKN7WebCore34PublicKeyCredentialCreationOptionsENS_29AuthenticatorSupportedOptions28UserVerificationAvailabilityENSB_23ResidentKeyAvailabilityERKNS1_INS0_6StringELm0ES2_Lm16ES3_EENSt3__18optionalINS_13PinParametersEEE
+ __ZN7WebCore13ContainerNode14removeChildrenEv
+ __ZN7WebCore4Page26willEndWritingToolsSessionERKNS_12WritingTools7SessionEb
+ __ZN7WebCore4Page40proofreadingSessionDidReceiveSuggestionsERKNS_12WritingTools7SessionERKN3WTF6VectorINS1_14TextSuggestionELm0ENS5_15CrashOnOverflowELm16ENS5_10FastMallocEEERKNS_14CharacterRangeERKNS1_7ContextEb
+ __ZN7WebCore4Page40setSelectionForActiveWritingToolsSessionERKNS_14CharacterRangeE
+ __ZN7WebCore4Page43textPreviewDataForActiveWritingToolsSessionERKNS_14CharacterRangeE
+ __ZN7WebCore4Page48updateTextVisibilityForActiveWritingToolsSessionERKNS_14CharacterRangeEbRKN3WTF4UUIDE
+ __ZN7WebCore4Page52decorateTextReplacementsForActiveWritingToolsSessionERKNS_14CharacterRangeE
+ __ZN7WebCore7Element25ensureUserAgentShadowRootEv
+ __ZNK7WebCore4Page24isAlwaysOnLoggingAllowedEv
+ __ZNK7WebCore4Page59proofreadingSessionSuggestionTextRectsInRootViewCoordinatesERKNS_14CharacterRangeE
+ __ZNK7WebCore7Element19userAgentShadowRootEv
- __ZN4fido24encodeSilentGetAssertionERKN3WTF6StringERKNS0_6VectorIhLm0ENS0_15CrashOnOverflowELm16ENS0_10FastMallocEEERKNS4_IN7WebCore29PublicKeyCredentialDescriptorELm0ES5_Lm16ES6_EENSt3__18optionalINS_13PinParametersEEE
- __ZN4fido28AuthenticatorGetInfoResponse24setMaxCredentialIDLengthEj
- __ZN4fido28AuthenticatorGetInfoResponse27setMaxCredentialCountInListEj
- __ZN4fido31encodeGetAssertionRequestAsCBORERKN3WTF6VectorIhLm0ENS0_15CrashOnOverflowELm16ENS0_10FastMallocEEERKN7WebCore33PublicKeyCredentialRequestOptionsENS_29AuthenticatorSupportedOptions28UserVerificationAvailabilityERKNS1_INS0_6StringELm0ES2_Lm16ES3_EENSt3__18optionalINS_13PinParametersEEEONSI_INS1_INS7_29PublicKeyCredentialDescriptorELm0ES2_Lm16ES3_EEEE
- __ZN4fido33encodeMakeCredentialRequestAsCBORERKN3WTF6VectorIhLm0ENS0_15CrashOnOverflowELm16ENS0_10FastMallocEEERKN7WebCore34PublicKeyCredentialCreationOptionsENS_29AuthenticatorSupportedOptions28UserVerificationAvailabilityENSB_23ResidentKeyAvailabilityERKNS1_INS0_6StringELm0ES2_Lm16ES3_EENSt3__18optionalINS_13PinParametersEEEONSJ_INS1_INS7_29PublicKeyCredentialDescriptorELm0ES2_Lm16ES3_EEEE
- __ZN7WebCore4Page40proofreadingSessionDidReceiveSuggestionsERKNS_12WritingTools7SessionERKN3WTF6VectorINS1_14TextSuggestionELm0ENS5_15CrashOnOverflowELm16ENS5_10FastMallocEEERKNS1_7ContextEb
- __ZN7WebCore4Page48proofreadingSessionDidCompletePartialReplacementERKNS_12WritingTools7SessionERKN3WTF6VectorINS1_14TextSuggestionELm0ENS5_15CrashOnOverflowELm16ENS5_10FastMallocEEERKNS1_7ContextEb
CStrings:
+ "#annotationContainer {    overflow: hidden;    position: relative;    pointer-events: none;    display: flex;    place-content: center;    place-items: center;}.annotation {    position: absolute;    pointer-events: auto;}.lock-icon {    width: 64px;    height: 64px;    margin-bottom: 12px;}.password-form {    position: static;    display: block;    text-align: center;    font-family: system-ui;    font-size: 15px;}.password-form p {    margin: 4pt;}.password-form .subtitle {    font-size: 12px;}"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/GCGLSpan.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/ImageBufferPixelFormat.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/RealtimeMediaSourceCapabilities.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/SecurityOriginData.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/StorageNamespaceProvider.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/WebKitAdditions/DownloadProgressAdditions.mm"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/WebKitAdditions/DyldCallbackAdditions.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/pal/spi/cocoa/NSAttributedStringSPI.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/JSONValues.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/Markable.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/Ref.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "/AppleInternal/Library/BuildRoots/77ed9d33-a365-11ef-a828-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1017: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1023: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1051: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1056: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1468: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1618: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 790: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 810: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 834: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 851: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 865: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 897: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 938: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 940: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/WebPageProxyCocoa.mm 1293: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/WebPageProxyCocoa.mm 1295: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/WebPageProxyCocoa.mm 1394: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10026: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10042: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10081: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11061: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11075: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11077: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11238: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11248: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11408: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11430: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12960: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12962: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12969: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12971: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12978: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12980: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13027: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13035: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13106: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13107: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13121: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13122: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13139: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13140: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13148: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13164: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13165: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13166: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13195: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13198: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13242: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13243: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13256: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13257: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14396: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14440: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5617: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5623: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5629: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6051: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6207: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6237: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6269: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6309: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6345: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6377: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6390: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6410: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6425: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6441: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6584: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6741: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6808: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6871: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6922: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6961: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7061: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7110: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7153: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7167: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7200: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7248: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7550: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7552: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7562: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7597: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7598: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7625: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7627: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7636: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7637: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7638: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7719: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7722: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7725: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7749: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7750: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7770: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7771: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7772: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7773: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7801: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7803: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7804: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7816: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7817: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7819: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7847: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7848: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7849: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8067: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8090: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8113: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8229: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8290: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8317: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8318: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8319: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8325: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8335: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8808: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8813: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8861: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8862: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8898: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8939: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9139: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9635: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9643: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9731: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9734: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9760: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9763: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9839: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9950: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9966: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9982: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9998: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebProcessProxy.cpp 2148: Invalid message dispatched %!{(MISSING)public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebProcessProxy.cpp 2333: Invalid message dispatched %!{(MISSING)public}s"
+ "CSS line-fit-edge"
+ "CSSLineFitEdgeEnabled"
+ "Enable CSS line-fit-edge"
+ "RemoteLegacyCDMFactoryProxy_RemoveSessionReply"
+ "TB,N,S_setSpatialVideoEnabled:"
+ "WKIntelligenceTextEffectCoordinator"
+ "Web Extension background content"
+ "WebPage_DecorateTextReplacementsForActiveWritingToolsSession"
+ "WebPage_DecorateTextReplacementsForActiveWritingToolsSessionReply"
+ "WebPage_ProofreadingSessionSuggestionTextRectsInRootViewCoordinates"
+ "WebPage_ProofreadingSessionSuggestionTextRectsInRootViewCoordinatesReply"
+ "WebPage_SetSelectionForActiveWritingToolsSession"
+ "WebPage_SetSelectionForActiveWritingToolsSessionReply"
+ "WebPage_TextPreviewDataForActiveWritingToolsSession"
+ "WebPage_TextPreviewDataForActiveWritingToolsSessionReply"
+ "WebPage_UpdateTextVisibilityForActiveWritingToolsSession"
+ "WebPage_UpdateTextVisibilityForActiveWritingToolsSessionReply"
+ "WebPage_WillEndWritingToolsSession"
+ "WebPage_WillEndWritingToolsSessionReply"
+ "_intelligenceTextEffectCoordinator"
+ "_isLoggerEnabledForTesting"
+ "_setSpatialVideoEnabled:"
+ "_spatialVideoEnabled"
+ "characterDeltaForReceivedSuggestions:"
+ "flushReplacementsWithCompletion:"
+ "intelligenceTextEffectCoordinator:decorateReplacementsForRange:completion:"
+ "intelligenceTextEffectCoordinator:rectsForProofreadingSuggestionsInRange:completion:"
+ "intelligenceTextEffectCoordinator:setSelectionForRange:completion:"
+ "intelligenceTextEffectCoordinator:textPreviewsForRange:completion:"
+ "intelligenceTextEffectCoordinator:updateTextVisibilityForRange:visible:identifier:completion:"
+ "m_fileCreatedHandlerCalled"
+ "requestReplacementWithProcessedRange:finished:characterDelta:operation:completion:"
+ "restoreSelectionAcceptedReplacements:completion:"
+ "startAnimationForRange:completion:"
+ "v48@0:8@16{_NSRange=QQ}24@?40"
+ "v60@0:8@16{_NSRange=QQ}24B40@44@?52"
+ "valueWithRect:"
+ "viewForIntelligenceTextEffectCoordinator:"
+ "x-"
+ "{ObjectStorage<API::NavigationAction>=\"data\"{type=\"__lx\"[2912C]}}"
+ "{ObjectStorage<WebKit::WebExtensionContext>=\"data\"{type=\"__lx\"[752C]}}"
+ "{RetainPtr<WKIntelligenceTextEffectCoordinator>=\"m_ptr\"^v}"
- "%!p(MISSING) [aaguid=%!s(MISSING), transport=%!s(MISSING)] - CtapAuthenticator::getAssertion"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/GCGLSpan.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/ImageBufferPixelFormat.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/RealtimeMediaSourceCapabilities.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/SecurityOriginData.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/StorageNamespaceProvider.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/WebKitAdditions/DownloadProgressAdditions.mm"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/WebKitAdditions/DyldCallbackAdditions.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/pal/spi/cocoa/NSAttributedStringSPI.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/JSONValues.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/Markable.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/Ref.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
- "/AppleInternal/Library/BuildRoots/822a4175-9c36-11ef-a772-ce2c30f2a3e7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1027: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1032: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1443: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1593: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 789: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 806: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 827: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 841: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 852: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 881: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 898: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 918: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 993: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 999: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/WebPageProxyCocoa.mm 1268: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/WebPageProxyCocoa.mm 1270: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/WebPageProxyCocoa.mm 1369: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10022: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10038: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10077: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11057: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11071: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11073: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11234: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11244: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11404: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11426: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12956: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12958: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12965: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12967: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12974: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12976: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13023: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13031: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13102: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13103: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13117: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13118: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13135: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13136: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13144: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13160: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13161: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13162: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13191: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13194: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13238: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13239: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13252: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13253: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14392: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14436: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5616: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5622: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5628: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6050: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6206: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6234: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6268: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6308: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6343: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6376: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6389: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6407: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6424: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6439: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6583: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6740: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6807: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6870: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6920: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6959: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7060: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7109: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7152: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7166: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7199: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7247: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7546: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7548: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7558: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7593: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7594: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7621: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7623: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7632: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7633: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7634: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7715: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7718: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7721: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7745: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7746: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7766: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7767: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7768: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7769: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7796: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7797: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7799: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7812: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7813: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7815: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7843: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7844: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7845: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8063: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8086: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8109: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8225: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8286: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8313: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8314: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8315: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8321: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8331: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8804: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8809: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8857: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8858: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8894: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8935: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9135: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9631: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9639: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9727: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9730: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9756: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9759: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9835: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9946: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9962: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9978: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9994: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebProcessProxy.cpp 2144: Invalid message dispatched %!{(MISSING)public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebProcessProxy.cpp 2329: Invalid message dispatched %!{(MISSING)public}s"
- "Download::publishProgress: Invalid request URL"
- "WebPage_ProofreadingSessionDidCompletePartialReplacement"
- "WebPage_ProofreadingSessionDidCompletePartialReplacementReply"
- "alternateLargeBlobIfNecessaryForRelyingParty:clientDataHash:"
- "void WTF::Deque<IPC::Connection::SyncMessageState::ConnectionAndIncomingMessage>::removeFirst()"
- "{ObjectStorage<API::NavigationAction>=\"data\"{type=\"__lx\"[2896C]}}"
- "{ObjectStorage<WebKit::WebExtensionContext>=\"data\"{type=\"__lx\"[744C]}}"

```
