## WebKit

> `/System/Library/Frameworks/WebKit.framework/WebKit`

```diff

-620.1.16.10.11
-  __TEXT.__text: 0xed4868
-  __TEXT.__auth_stubs: 0x17240
+620.2.2.0.0
+  __TEXT.__text: 0xed9858
+  __TEXT.__auth_stubs: 0x172a0
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x14be4
+  __TEXT.__objc_methlist: 0x14bf4
   __TEXT.__const: 0x3960
-  __TEXT.__gcc_except_tab: 0x600a8
-  __TEXT.__cstring: 0x8aeb8
-  __TEXT.__oslogstring: 0x3d8ca
-  __TEXT.__ustring: 0xcd4
-  __TEXT.__unwind_info: 0x28410
+  __TEXT.__gcc_except_tab: 0x6048c
+  __TEXT.__cstring: 0x8b308
+  __TEXT.__oslogstring: 0x3dc7b
+  __TEXT.__ustring: 0xd40
+  __TEXT.__unwind_info: 0x28998
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x32e5
-  __TEXT.__objc_methname: 0x46998
+  __TEXT.__objc_methname: 0x46a05
   __TEXT.__objc_methtype: 0x35da7
-  __TEXT.__objc_stubs: 0x29b00
+  __TEXT.__objc_stubs: 0x29b20
   __DATA_CONST.__got: 0x1ba8
-  __DATA_CONST.__const: 0x19f20
+  __DATA_CONST.__const: 0x19f98
   __DATA_CONST.__objc_classlist: 0xba8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x410
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf0f8
+  __DATA_CONST.__objc_selrefs: 0xf100
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA_CONST.__objc_superrefs: 0x9b0
+  __DATA_CONST.__objc_superrefs: 0x9b8
   __DATA_CONST.__objc_arraydata: 0x688
-  __AUTH_CONST.__auth_got: 0xb938
+  __AUTH_CONST.__auth_got: 0xb968
   __AUTH_CONST.__auth_ptr: 0x70
-  __AUTH_CONST.__const: 0x5e068
-  __AUTH_CONST.__cfstring: 0x13ae0
-  __AUTH_CONST.__objc_const: 0x2e9a8
+  __AUTH_CONST.__const: 0x5e158
+  __AUTH_CONST.__cfstring: 0x13b40
+  __AUTH_CONST.__objc_const: 0x2ea08
   __AUTH_CONST.__objc_intobj: 0x630
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x208

   __AUTH.__objc_data: 0x5190
   __AUTH.__data: 0x2e0
   __DATA.__objc_ivar: 0xf40
-  __DATA.__data: 0x34c8
-  __DATA.__bss: 0x838
-  __DATA.__common: 0x5b0
-  __DATA_DIRTY.__objc_ivar: 0x530
+  __DATA.__data: 0x34f0
+  __DATA.__bss: 0x7c0
+  __DATA.__common: 0x5c0
+  __DATA_DIRTY.__objc_ivar: 0x538
   __DATA_DIRTY.__objc_data: 0x2300
   __DATA_DIRTY.__data: 0x5a10
-  __DATA_DIRTY.__bss: 0x1b00
+  __DATA_DIRTY.__bss: 0x1b80
   __DATA_DIRTY.__common: 0x2a79
   - /System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 64915
-  Symbols:   77977
-  CStrings:  26678
+  Functions: 64943
+  Symbols:   78007
+  CStrings:  26707
 
Symbols:
+ _WKPageShowWebInspectorForTesting
+ __ZN3WTF11parseLocaleERKNS_6StringE
+ __ZN3WTF33indexOfBestMatchingLanguageInListERKNS_6StringERKNS_6VectorIS0_Lm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEEERb
+ __ZN7WebCore15GraphicsLayerCA24setContentsToImageBufferEPNS_11ImageBufferE
+ __ZN7WebCore21NetworkStorageSession9setCookieERKNS_6CookieERKN3WTF3URLES7_
+ __ZN7WebCore23commonInclusiveAncestorERKNS_8PositionES2_
+ __ZN7WebCore32ScrollingStateFrameScrollingNodeC1EbNS_16ProcessQualifiedIN3WTF23ObjectIdentifierGenericINS_19ScrollingNodeIDTypeENS2_38ObjectIdentifierMainThreadAccessTraitsIyEEyLNS2_33SupportsObjectIdentifierNullStateE1EEEEEONS2_6VectorINS2_3RefINS_18ScrollingStateNodeENS2_12RawPtrTraitsISC_EENS2_21DefaultRefDerefTraitsISC_EEEELm0ENS2_15CrashOnOverflowELm16ENS2_10FastMallocEEENS2_9OptionSetINS_26ScrollingStateNodePropertyEEENSt3__18optionalINS1_INS3_INS_27PlatformLayerIdentifierTypeES6_yLS7_0EEEEEEENS_9FloatSizeESV_SV_NS_10FloatPointENS_8IntPointEONS_24ScrollableAreaParametersEONS_19RequestedScrollDataEONS_21ScrollSnapOffsetsInfoIfNS_9FloatRectEEENSQ_IjEES16_bSU_SU_SU_SU_bONS_18MouseLocationStateEONS_19ScrollbarHoverStateEONS_21ScrollbarEnabledStateENS_28UserInterfaceLayoutDirectionENS_14ScrollbarWidthEbONS_27RequestedKeyboardScrollDataEfONS_20EventTrackingRegionsESU_SU_SU_SU_iiONS_30ScrollBehaviorForFixedElementsEfbbbbbS13_SW_SW_NSQ_ISV_EEb
+ __ZN7WebCore33ScrollingStatePluginScrollingNodeC1ENS_16ProcessQualifiedIN3WTF23ObjectIdentifierGenericINS_19ScrollingNodeIDTypeENS2_38ObjectIdentifierMainThreadAccessTraitsIyEEyLNS2_33SupportsObjectIdentifierNullStateE1EEEEEONS2_6VectorINS2_3RefINS_18ScrollingStateNodeENS2_12RawPtrTraitsISC_EENS2_21DefaultRefDerefTraitsISC_EEEELm0ENS2_15CrashOnOverflowELm16ENS2_10FastMallocEEENS2_9OptionSetINS_26ScrollingStateNodePropertyEEENSt3__18optionalINS1_INS3_INS_27PlatformLayerIdentifierTypeES6_yLS7_0EEEEEEENS_9FloatSizeESV_SV_NS_10FloatPointENS_8IntPointEONS_24ScrollableAreaParametersEONS_19RequestedScrollDataEONS_21ScrollSnapOffsetsInfoIfNS_9FloatRectEEENSQ_IjEES16_bSU_SU_SU_SU_bONS_18MouseLocationStateEONS_19ScrollbarHoverStateEONS_21ScrollbarEnabledStateENS_28UserInterfaceLayoutDirectionENS_14ScrollbarWidthEbONS_27RequestedKeyboardScrollDataE
+ __ZN7WebCore35ScrollingStateOverflowScrollingNodeC1ENS_16ProcessQualifiedIN3WTF23ObjectIdentifierGenericINS_19ScrollingNodeIDTypeENS2_38ObjectIdentifierMainThreadAccessTraitsIyEEyLNS2_33SupportsObjectIdentifierNullStateE1EEEEEONS2_6VectorINS2_3RefINS_18ScrollingStateNodeENS2_12RawPtrTraitsISC_EENS2_21DefaultRefDerefTraitsISC_EEEELm0ENS2_15CrashOnOverflowELm16ENS2_10FastMallocEEENS2_9OptionSetINS_26ScrollingStateNodePropertyEEENSt3__18optionalINS1_INS3_INS_27PlatformLayerIdentifierTypeES6_yLS7_0EEEEEEENS_9FloatSizeESV_SV_NS_10FloatPointENS_8IntPointEONS_24ScrollableAreaParametersEONS_19RequestedScrollDataEONS_21ScrollSnapOffsetsInfoIfNS_9FloatRectEEENSQ_IjEES16_bSU_SU_SU_SU_bONS_18MouseLocationStateEONS_19ScrollbarHoverStateEONS_21ScrollbarEnabledStateENS_28UserInterfaceLayoutDirectionENS_14ScrollbarWidthEbONS_27RequestedKeyboardScrollDataE
+ __ZN7WebCore6Quirks50shouldOmitTouchEventDOMAttributesForDesktopWebsiteERKN3WTF3URLE
+ __ZNK7WebCore21NetworkStorageSession12deleteCookieERKN3WTF3URLES4_RKNS1_6StringEONS1_17CompletionHandlerIFvvEEE
+ __ZNK7WebCore6Quirks38shouldIgnoreContentObservationForClickERKNS_4NodeE
+ _toWebExtensionWebRequestResourceType
- _WKBundlePageShowInspectorForTest
- __WKWebExtensionWebRequestResourceTypeFromResourceLoadInfo
- __ZN7WebCore32ScrollingStateFrameScrollingNodeC1EbNS_16ProcessQualifiedIN3WTF23ObjectIdentifierGenericINS_19ScrollingNodeIDTypeENS2_38ObjectIdentifierMainThreadAccessTraitsIyEEyLNS2_33SupportsObjectIdentifierNullStateE1EEEEEONS2_6VectorINS2_3RefINS_18ScrollingStateNodeENS2_12RawPtrTraitsISC_EENS2_21DefaultRefDerefTraitsISC_EEEELm0ENS2_15CrashOnOverflowELm16ENS2_10FastMallocEEENS2_9OptionSetINS_26ScrollingStateNodePropertyEEENSt3__18optionalINS1_INS3_INS_27PlatformLayerIdentifierTypeES6_yLS7_0EEEEEEENS_9FloatSizeESV_SV_NS_10FloatPointENS_8IntPointEONS_24ScrollableAreaParametersEONS_19RequestedScrollDataEONS_21ScrollSnapOffsetsInfoIfNS_9FloatRectEEENSQ_IjEES16_bSU_SU_SU_SU_bONS_18MouseLocationStateEONS_19ScrollbarHoverStateEONS_21ScrollbarEnabledStateENS_28UserInterfaceLayoutDirectionENS_14ScrollbarWidthEONS_27RequestedKeyboardScrollDataEfONS_20EventTrackingRegionsESU_SU_SU_SU_iiONS_30ScrollBehaviorForFixedElementsEfbbbbbS13_SW_SW_NSQ_ISV_EEb
- __ZN7WebCore33ScrollingStatePluginScrollingNodeC1ENS_16ProcessQualifiedIN3WTF23ObjectIdentifierGenericINS_19ScrollingNodeIDTypeENS2_38ObjectIdentifierMainThreadAccessTraitsIyEEyLNS2_33SupportsObjectIdentifierNullStateE1EEEEEONS2_6VectorINS2_3RefINS_18ScrollingStateNodeENS2_12RawPtrTraitsISC_EENS2_21DefaultRefDerefTraitsISC_EEEELm0ENS2_15CrashOnOverflowELm16ENS2_10FastMallocEEENS2_9OptionSetINS_26ScrollingStateNodePropertyEEENSt3__18optionalINS1_INS3_INS_27PlatformLayerIdentifierTypeES6_yLS7_0EEEEEEENS_9FloatSizeESV_SV_NS_10FloatPointENS_8IntPointEONS_24ScrollableAreaParametersEONS_19RequestedScrollDataEONS_21ScrollSnapOffsetsInfoIfNS_9FloatRectEEENSQ_IjEES16_bSU_SU_SU_SU_bONS_18MouseLocationStateEONS_19ScrollbarHoverStateEONS_21ScrollbarEnabledStateENS_28UserInterfaceLayoutDirectionENS_14ScrollbarWidthEONS_27RequestedKeyboardScrollDataE
- __ZN7WebCore35ScrollingStateOverflowScrollingNodeC1ENS_16ProcessQualifiedIN3WTF23ObjectIdentifierGenericINS_19ScrollingNodeIDTypeENS2_38ObjectIdentifierMainThreadAccessTraitsIyEEyLNS2_33SupportsObjectIdentifierNullStateE1EEEEEONS2_6VectorINS2_3RefINS_18ScrollingStateNodeENS2_12RawPtrTraitsISC_EENS2_21DefaultRefDerefTraitsISC_EEEELm0ENS2_15CrashOnOverflowELm16ENS2_10FastMallocEEENS2_9OptionSetINS_26ScrollingStateNodePropertyEEENSt3__18optionalINS1_INS3_INS_27PlatformLayerIdentifierTypeES6_yLS7_0EEEEEEENS_9FloatSizeESV_SV_NS_10FloatPointENS_8IntPointEONS_24ScrollableAreaParametersEONS_19RequestedScrollDataEONS_21ScrollSnapOffsetsInfoIfNS_9FloatRectEEENSQ_IjEES16_bSU_SU_SU_SU_bONS_18MouseLocationStateEONS_19ScrollbarHoverStateEONS_21ScrollbarEnabledStateENS_28UserInterfaceLayoutDirectionENS_14ScrollbarWidthEONS_27RequestedKeyboardScrollDataE
- __ZNK7WebCore19InspectorController11isUnderTestEv
- __ZNK7WebCore21NetworkStorageSession12deleteCookieERKN3WTF3URLERKNS1_6StringEONS1_17CompletionHandlerIFvvEEE
CStrings:
+ "%@-%@-%@-%@-%@"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/GCGLSpan.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/ImageBufferPixelFormat.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/RealtimeMediaSourceCapabilities.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/SecurityOriginData.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/StorageNamespaceProvider.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/WebKitAdditions/DownloadProgressAdditions.mm"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/WebKitAdditions/DyldCallbackAdditions.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/pal/spi/cocoa/NSAttributedStringSPI.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/JSONValues.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/Markable.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/Ref.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1009: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1010: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1065: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1071: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1099: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1104: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1517: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1667: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 904: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 918: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 931: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 955: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 980: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 982: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 997: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 998: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/storage/CacheStorageRecord.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/UserMediaCaptureManagerProxy.cpp 580: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/UserMediaCaptureManagerProxy.cpp 681: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/UserMediaCaptureManagerProxy.cpp 683: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/UserMediaCaptureManagerProxy.cpp 697: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/UserMediaCaptureManagerProxy.cpp 698: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Network/NetworkProcessProxy.cpp 342: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Network/NetworkProcessProxy.cpp 386: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Network/NetworkProcessProxy.cpp 395: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Network/NetworkProcessProxy.cpp 402: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Network/NetworkProcessProxy.cpp 411: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Network/NetworkProcessProxy.cpp 418: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10008: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10036: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10052: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10091: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11071: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11085: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11087: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11258: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11418: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11440: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12970: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12972: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12979: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12981: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12988: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12990: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13037: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13045: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13116: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13117: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13131: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13132: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13149: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13150: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13158: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13174: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13175: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13176: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13205: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13208: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13252: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13253: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13266: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13267: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14406: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14450: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 2497: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 2503: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 3900: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5619: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5625: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5631: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6053: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6209: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6238: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6239: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6271: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6311: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6346: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6347: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6379: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6392: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6411: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6412: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6427: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6442: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6443: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6586: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6743: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6810: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6873: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6923: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6924: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6962: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6963: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7063: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7112: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7155: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7169: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7202: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7250: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7554: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7564: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7599: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7600: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7629: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7639: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7640: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7721: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7724: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7727: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7751: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7752: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7774: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7775: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7802: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7805: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7806: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7818: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7821: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7850: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7851: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8071: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8094: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8117: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8233: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8294: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8321: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8322: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8323: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8329: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8339: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8812: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8817: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8865: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8866: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8902: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8943: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9143: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9645: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9653: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9741: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9744: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9770: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9773: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9849: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9960: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9976: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9992: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/ios/WebPageProxyIOS.mm 587: Invalid message dispatched %{public}s"
+ "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/ios/WebPageProxyIOS.mm 897: Invalid message dispatched %{public}s"
+ "Clear-Site-Data: 'executionContexts' support"
+ "ClearSiteDataExecutionContextsSupportEnabled"
+ "Connection to web push daemon failed"
+ "Could not retrieve the metadata from UDPSocket Context, so use default ECN value"
+ "Empty or invalid `default_locale` manifest entry."
+ "Enable Clear-Site-Data: 'executionContexts' support"
+ "Info.plist"
+ "Loaded default locale %{public}@"
+ "Loaded language-only locale %{public}@"
+ "Loaded regional locale %{public}@"
+ "NetworkProcess_SetShouldRelaxThirdPartyCookieBlockingForPage"
+ "No localization found for default locale %{public}@"
+ "PushClientConnection_SetProtocolVersionForTesting"
+ "PushClientConnection_SetProtocolVersionForTestingReply"
+ "T@\"NSNumber\",&,N,V_version"
+ "T@\"NSString\",&,N,V_type"
+ "T@\"NSUUID\",&,N,V_webClipIdentifier"
+ "WebInspectorUIProxy_RequestOpenLocalInspectorFrontend"
+ "WebInspector_ShowReply"
+ "WebKit::CacheStorageRecordInformation::CacheStorageRecordInformation(NetworkCache::Key &&, double, uint64_t, uint64_t, uint64_t, URL &&, bool, HashMap<String, String> &&)"
+ "WebKit::NetworkResourceLoadParameters::NetworkResourceLoadParameters(NetworkLoadParameters &&, WebCore::ResourceLoaderIdentifier, RefPtr<WebCore::FormData> &&, std::optional<Vector<SandboxExtension::Handle>> &&, std::optional<SandboxExtension::Handle> &&, Seconds, WebCore::FetchOptions &&, std::optional<WebCore::ContentSecurityPolicyResponseHeaders> &&, URL &&, URL &&, WebCore::CrossOriginEmbedderPolicy, WebCore::CrossOriginEmbedderPolicy, WebCore::HTTPHeaderMap &&, bool, WebCore::PreflightPolicy, bool, Vector<Ref<WebCore::SecurityOrigin>> &&, bool, std::optional<WebCore::FrameIdentifier>, bool, URL &&, bool, bool, bool, bool, WebCore::SandboxFlags, URL &&, WebCore::CrossOriginOpenerPolicy &&, std::optional<WebCore::NavigationIdentifier>, std::optional<WebCore::NavigationRequester> &&, WebCore::ServiceWorkersMode, std::optional<WebCore::ServiceWorkerRegistrationIdentifier>, OptionSet<WebCore::HTTPHeadersToKeepFromCleaning>, std::optional<WebCore::FetchIdentifier>, URL &&, std::optional<UserContentControllerIdentifier>, bool, bool, bool)"
+ "WebPage_ClearSelectionAfterTappingSelectionHighlightIfNeeded"
+ "_interactionPointInWindow"
+ "_isMenuPreviouslyRepositioned"
+ "_locales/"
+ "_shouldToggleEditMenuAfterTapAt:"
+ "_webClipIdentifier"
+ "initWithUUIDString:"
+ "match_constness_t<Source, Target> *WTF::downcast(Source *) [Target = WebKit::PlatformCALayerRemote, Source = WebCore::PlatformCALayer]"
+ "repositionContextMenuIfNeeded:"
+ "setWebClipIdentifier:"
+ "shouldBypassPermissionsForWebExtensionContext:"
+ "void WebKit::CacheStorageRecordInformation::setURL(URL &&)"
+ "void WebKit::NetworkConnectionToWebProcess::cookieRequestHeaderFieldValue(const URL &, const SameSiteInfo &, const URL &, std::optional<FrameIdentifier>, std::optional<PageIdentifier>, IncludeSecureCookies, std::optional<WebPageProxyIdentifier>, CompletionHandler<void (String, bool)> &&)"
+ "void WebKit::NetworkConnectionToWebProcess::cookiesEnabled(const URL &, const URL &, std::optional<FrameIdentifier>, std::optional<PageIdentifier>, WebPageProxyIdentifier, CompletionHandler<void (bool)> &&)"
+ "void WebKit::NetworkConnectionToWebProcess::cookiesForDOM(const URL &, const SameSiteInfo &, const URL &, FrameIdentifier, PageIdentifier, IncludeSecureCookies, WebPageProxyIdentifier, CompletionHandler<void (String, bool)> &&)"
+ "void WebKit::NetworkConnectionToWebProcess::cookiesForDOMAsync(const URL &, const SameSiteInfo &, const URL &, std::optional<FrameIdentifier>, std::optional<PageIdentifier>, IncludeSecureCookies, CookieStoreGetOptions &&, std::optional<WebPageProxyIdentifier>, CompletionHandler<void (std::optional<Vector<WebCore::Cookie>> &&)> &&)"
+ "void WebKit::NetworkConnectionToWebProcess::createSocketChannel(const ResourceRequest &, const String &, WebSocketIdentifier, WebPageProxyIdentifier, std::optional<FrameIdentifier>, std::optional<PageIdentifier>, const ClientOrigin &, bool, bool, OptionSet<AdvancedPrivacyProtections>, WebCore::StoredCredentialsPolicy)"
+ "void WebKit::NetworkConnectionToWebProcess::deleteCookie(const URL &, const URL &, const String &, CompletionHandler<void ()> &&)"
+ "void WebKit::NetworkConnectionToWebProcess::getRawCookies(const URL &, const SameSiteInfo &, const URL &, std::optional<FrameIdentifier>, std::optional<PageIdentifier>, std::optional<WebPageProxyIdentifier>, CompletionHandler<void (Vector<WebCore::Cookie> &&)> &&)"
+ "void WebKit::NetworkConnectionToWebProcess::setCookieFromDOMAsync(const URL &, const SameSiteInfo &, const URL &, std::optional<FrameIdentifier>, std::optional<PageIdentifier>, WebCore::Cookie &&, std::optional<WebPageProxyIdentifier>, CompletionHandler<void (bool)> &&)"
+ "void WebKit::NetworkConnectionToWebProcess::setCookiesFromDOM(const URL &, const SameSiteInfo &, const URL &, FrameIdentifier, PageIdentifier, String &&, WebPageProxyIdentifier)"
+ "void WebKit::NetworkConnectionToWebProcess::setRawCookie(const URL &, const URL &, const WebCore::Cookie &)"
+ "void WebKit::NetworkConnectionToWebProcess::subscribeToCookieChangeNotifications(const String &)"
+ "void WebKit::NetworkConnectionToWebProcess::unsubscribeFromCookieChangeNotifications(const String &)"
+ "webClipIdentifier"
+ "{ObjectStorage<WebKit::WebExtension>=\"data\"{type=\"__lx\"[376C]}}"
+ "\xf0a"
- "%@_%@"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/GCGLSpan.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/ImageBufferPixelFormat.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/RealtimeMediaSourceCapabilities.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/SecurityOriginData.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Cryptexes/OS/System/Library/PrivateFrameworks/WebCore.framework/PrivateHeaders/StorageNamespaceProvider.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/WebKitAdditions/DownloadProgressAdditions.mm"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/WebKitAdditions/DyldCallbackAdditions.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/pal/spi/cocoa/NSAttributedStringSPI.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/JSONValues.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/Markable.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/Ref.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
- "/AppleInternal/Library/BuildRoots/7a5643da-a7fb-11ef-987a-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1049: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1055: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1083: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1088: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1500: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 1650: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 921: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 945: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 970: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp 972: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/UserMediaCaptureManagerProxy.cpp 576: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/UserMediaCaptureManagerProxy.cpp 673: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/UserMediaCaptureManagerProxy.cpp 675: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/UserMediaCaptureManagerProxy.cpp 689: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Cocoa/UserMediaCaptureManagerProxy.cpp 690: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Network/NetworkProcessProxy.cpp 336: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Network/NetworkProcessProxy.cpp 380: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Network/NetworkProcessProxy.cpp 389: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Network/NetworkProcessProxy.cpp 396: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Network/NetworkProcessProxy.cpp 405: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/Network/NetworkProcessProxy.cpp 412: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10026: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10042: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 10081: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11061: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11075: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11077: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11238: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11408: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 11430: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12960: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12962: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12969: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12971: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12978: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 12980: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13027: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13035: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13106: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13107: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13121: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13122: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13139: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13140: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13148: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13164: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13165: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13166: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13195: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13198: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13242: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13243: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13256: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 13257: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14396: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 14440: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 2495: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 2501: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 3898: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5617: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5623: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 5629: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6051: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6207: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6235: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6236: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6269: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6309: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6344: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6345: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6377: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6390: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6408: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6409: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6425: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6440: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6441: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6584: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6741: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6808: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6871: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6921: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6922: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6960: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 6961: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7061: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7110: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7153: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7167: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7200: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7248: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7550: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7562: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7597: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7598: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7625: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7636: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7637: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7719: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7722: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7725: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7749: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7750: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7770: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7771: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7800: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7801: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7804: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7816: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7817: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7847: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 7848: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8067: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8090: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8113: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8229: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8290: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8317: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8318: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8319: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8325: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8335: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8808: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8813: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8861: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8862: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8898: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 8939: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9139: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9635: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9643: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9731: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9734: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9760: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9763: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9839: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9950: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9966: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9982: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/WebPageProxy.cpp 9998: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/ios/WebPageProxyIOS.mm 581: Invalid message dispatched %{public}s"
- "/Library/Caches/com.apple.xbs/Sources/WebKit/Source/WebKit/UIProcess/ios/WebPageProxyIOS.mm 885: Invalid message dispatched %{public}s"
- "Could not retreive the metadata from UDPSocket Context, so use default ECN value"
- "Default locale available for %{public}@"
- "Language locale available for %{public}@"
- "Regional locale available for %{public}@"
- "T &WTF::Deque<WTF::Function<void ()>>::first()"
- "T@\"NSNumber\",N,V_version"
- "T@\"NSString\",N,V_pushPartition"
- "T@\"NSString\",N,V_type"
- "WebInspectorUIProxy_OpenLocalInspectorFrontend"
- "WebKit::NetworkResourceLoadParameters::NetworkResourceLoadParameters(NetworkLoadParameters &&, WebCore::ResourceLoaderIdentifier, RefPtr<WebCore::FormData> &&, std::optional<Vector<SandboxExtension::Handle>> &&, std::optional<SandboxExtension::Handle> &&, Seconds, WebCore::FetchOptions &&, std::optional<WebCore::ContentSecurityPolicyResponseHeaders> &&, URL &&, URL &&, WebCore::CrossOriginEmbedderPolicy, WebCore::CrossOriginEmbedderPolicy, WebCore::HTTPHeaderMap &&, bool, WebCore::PreflightPolicy, bool, Vector<Ref<WebCore::SecurityOrigin>> &&, bool, std::optional<WebCore::FrameIdentifier>, bool, URL &&, bool, bool, bool, WebCore::SandboxFlags, URL &&, WebCore::CrossOriginOpenerPolicy &&, std::optional<WebCore::NavigationIdentifier>, std::optional<WebCore::NavigationRequester> &&, WebCore::ServiceWorkersMode, std::optional<WebCore::ServiceWorkerRegistrationIdentifier>, OptionSet<WebCore::HTTPHeadersToKeepFromCleaning>, std::optional<WebCore::FetchIdentifier>, URL &&, std::optional<UserContentControllerIdentifier>, bool, bool, bool)"
- "_pushPartition"
- "_shouldToggleSelectionCommandsAfterTapAt:"
- "autoupdatingCurrentLocale"
- "pushPartition"
- "repositionContextMenuIfNeeded"
- "setPushPartition:"
- "void WebKit::NetworkConnectionToWebProcess::cookieRequestHeaderFieldValue(const URL &, const SameSiteInfo &, const URL &, std::optional<FrameIdentifier>, std::optional<PageIdentifier>, IncludeSecureCookies, ApplyTrackingPrevention, ShouldRelaxThirdPartyCookieBlocking, CompletionHandler<void (String, bool)> &&)"
- "void WebKit::NetworkConnectionToWebProcess::cookiesEnabled(const URL &, const URL &, std::optional<FrameIdentifier>, std::optional<PageIdentifier>, ShouldRelaxThirdPartyCookieBlocking, CompletionHandler<void (bool)> &&)"
- "void WebKit::NetworkConnectionToWebProcess::cookiesForDOM(const URL &, const SameSiteInfo &, const URL &, FrameIdentifier, PageIdentifier, IncludeSecureCookies, ApplyTrackingPrevention, ShouldRelaxThirdPartyCookieBlocking, CompletionHandler<void (String, bool)> &&)"
- "void WebKit::NetworkConnectionToWebProcess::cookiesForDOMAsync(const URL &, const SameSiteInfo &, const URL &, std::optional<WebCore::FrameIdentifier>, std::optional<WebCore::PageIdentifier>, IncludeSecureCookies, ApplyTrackingPrevention, ShouldRelaxThirdPartyCookieBlocking, WebCore::CookieStoreGetOptions &&, CompletionHandler<void (std::optional<Vector<WebCore::Cookie>> &&)> &&)"
- "void WebKit::NetworkConnectionToWebProcess::createSocketChannel(const ResourceRequest &, const String &, WebSocketIdentifier, WebPageProxyIdentifier, std::optional<FrameIdentifier>, std::optional<PageIdentifier>, const ClientOrigin &, bool, bool, OptionSet<AdvancedPrivacyProtections>, ShouldRelaxThirdPartyCookieBlocking, WebCore::StoredCredentialsPolicy)"
- "void WebKit::NetworkConnectionToWebProcess::getRawCookies(const URL &, const SameSiteInfo &, const URL &, std::optional<FrameIdentifier>, std::optional<PageIdentifier>, ApplyTrackingPrevention, ShouldRelaxThirdPartyCookieBlocking, CompletionHandler<void (Vector<WebCore::Cookie> &&)> &&)"
- "void WebKit::NetworkConnectionToWebProcess::setCookieFromDOMAsync(const URL &, const SameSiteInfo &, const URL &, std::optional<WebCore::FrameIdentifier>, std::optional<WebCore::PageIdentifier>, ApplyTrackingPrevention, WebCore::Cookie &&, ShouldRelaxThirdPartyCookieBlocking, CompletionHandler<void (bool)> &&)"
- "void WebKit::NetworkConnectionToWebProcess::setCookiesFromDOM(const URL &, const SameSiteInfo &, const URL &, WebCore::FrameIdentifier, PageIdentifier, ApplyTrackingPrevention, const String &, ShouldRelaxThirdPartyCookieBlocking)"
- "{ObjectStorage<WebKit::WebExtension>=\"data\"{type=\"__lx\"[360C]}}"
- "\xf0A"

```
