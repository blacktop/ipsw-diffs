## WebCore

> `/System/Library/PrivateFrameworks/WebCore.framework/WebCore`

```diff

-621.3.7.10.1
-  __TEXT.__text: 0x2e57b04
+621.3.8.0.0
+  __TEXT.__text: 0x2e59810
   __TEXT.__auth_stubs: 0xd3a0
   __TEXT.__objc_methlist: 0x54d4
   __TEXT.__const: 0x1b1ee0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 689C0505-12FF-3799-953B-D8C1F12C80A5
+  UUID: 0D1E1555-CED4-3683-820E-184E040F015B
   Functions: 123646
-  Symbols:   279230
+  Symbols:   279228
   CStrings:  34388
 
Symbols:
+ __ZN7WebCore16SelectorCompilerL18addPseudoClassTypeERKNS_11CSSSelectorERNS0_16SelectorFragmentENS0_15SelectorContextENS0_14FragmentsLevelENS0_31FragmentPositionInRootFragmentsEbRNS0_11VisitedModeENS0_29PseudoElementMatchingBehaviorE
+ __ZN7WebCore24ElementAnimationRareData28setAnimationsCreatedByMarkupEON3WTF11ListHashSetINS1_3RefINS_12CSSAnimationENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEENS1_11DefaultHashIS9_EEEE
- __ZN3WTF6VectorINS_7CodePtrILNS_6PtrTagE45961ELNS_18FunctionAttributesE0EEELm4ENS_15CrashOnOverflowELm16ENS_10FastMallocEE14appendSlowCaseILNS_13FailureActionE0ES4_EEbOT0_
- __ZN3WTF7CodePtrILNS_6PtrTagE45961ELNS_18FunctionAttributesE0EEC1IbJRKN7WebCore7ElementEEEEPFT_DpT0_E
- __ZN7WebCore16SelectorCompiler12SelectorListC1ERKS1_
Functions (modified):
~ __ZN7WebCore16SelectorCompilerL18constructFragmentsEPKNS_11CSSSelectorENS0_15SelectorContextERNS0_20SelectorFragmentListENS0_14FragmentsLevelENS0_31FragmentPositionInRootFragmentsEbRNS0_11VisitedModeENS0_29PseudoElementMatchingBehaviorE : 5900 -> 1640
~ __ZN7WebCore21RenderLayerCompositor23updateCompositingLayersENS_21CompositingUpdateTypeEPNS_11RenderLayerE : 5716 -> 5720
~ __ZN7WebCore7Element28setAnimationsCreatedByMarkupERKNSt3__18optionalINS_5Style23PseudoElementIdentifierEEEON3WTF11ListHashSetINS8_3RefINS_12CSSAnimationENS8_12RawPtrTraitsISB_EENS8_21DefaultRefDerefTraitsISB_EEEENS8_11DefaultHashISG_EEEE : 1452 -> 1388
~ __ZN7WebCore11DisplayList12RecorderImpl7restoreENS_20GraphicsContextState7PurposeE : 168 -> 180
~ __ZZN7WebCore21RenderLayerCompositor31updateSynchronousScrollingNodesEvENK3$_1clEb : 240 -> 244
~ __ZN7WebCore17RenderTreeBuilder23detachFromRenderElementERNS_13RenderElementERNS_12RenderObjectENS0_15WillBeDestroyedE : 3108 -> 2904
~ __ZN7WebCore17RenderTreeBuilder21removeFloatingObjectsERNS_11RenderBlockE : 436 -> 328
~ __ZN7WebCore17RenderTreeBuilder34destroyAndCleanUpAnonymousWrappersERNS_12RenderObjectEPKNS_13RenderElementE : 2372 -> 2292
~ __ZN7WebCore17RenderTreeUpdater17tearDownRenderersERNS_7ElementENS0_12TeardownTypeERNS_17RenderTreeBuilderE : 7320 -> 7680
~ __ZNK7WebCore9Styleable17elementWasRemovedEv : 4100 -> 4124
~ __ZNK7WebCore9Styleable31cancelStyleOriginatedAnimationsEv : 3656 -> 3680
~ __ZN7WebCore19SVGAnimationElement21startedActiveIntervalEv : 3028 -> 3052

Functions (added):
+ __ZN7WebCore16SelectorCompilerL18addPseudoClassTypeERKNS_11CSSSelectorERNS0_16SelectorFragmentENS0_15SelectorContextENS0_14FragmentsLevelENS0_31FragmentPositionInRootFragmentsEbRNS0_11VisitedModeENS0_29PseudoElementMatchingBehaviorE
+ __ZN7WebCore24ElementAnimationRareData28setAnimationsCreatedByMarkupEON3WTF11ListHashSetINS1_3RefINS_12CSSAnimationENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEENS1_11DefaultHashIS9_EEEE

Functions (removed):
- sub_198009418
- sub_198dde3b4
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ARM64Assembler.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/AbstractSlotVisitorInlines.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArgList.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBuffer.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBufferView.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DataView.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ExecutableAllocator.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/IndexingHeader.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArray.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCPtrTag.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCast.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObject.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObjectInlines.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/MacroAssemblerARM64.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/WebKitAdditions/EventHandlerIOSTouch.cpp"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/CheckedPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/CompactVariantOperations.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/CryptographicUtilities.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/HashTable.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/JSONValues.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Markable.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Ref.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/RefCounted.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/RefPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/TrailingArray.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/WeakRef.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/cocoa/TypeCastsCocoa.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
+ "void JSC::SecureARM64EHashPins::forEachPage(Function) [Function = (lambda at /AppleInternal/Library/BuildRoots/4~B4tZugCQvLLTCIFCBECC3kWQQZBiZ_qIGNc2hGc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h:65:17)]"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ARM64Assembler.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/AbstractSlotVisitorInlines.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArgList.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBuffer.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBufferView.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DataView.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ExecutableAllocator.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/IndexingHeader.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArray.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCPtrTag.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCast.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObject.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObjectInlines.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/MacroAssemblerARM64.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/WebKitAdditions/EventHandlerIOSTouch.cpp"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/CheckedPtr.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/CompactVariantOperations.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/CryptographicUtilities.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/HashTable.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/JSONValues.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Markable.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Ref.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/RefCounted.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/RefPtr.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/TrailingArray.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/WeakRef.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/cocoa/TypeCastsCocoa.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
- "/AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
- "void JSC::SecureARM64EHashPins::forEachPage(Function) [Function = (lambda at /AppleInternal/Library/BuildRoots/4~B31wugBnLxQJ9i0Dra86SUP1Un_9W-6tNukvdko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h:65:17)]"

```
