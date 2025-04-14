## WebCore

> `/System/Library/PrivateFrameworks/WebCore.framework/WebCore`

```diff

-621.2.1.10.3
-  __TEXT.__text: 0x2e78100
-  __TEXT.__auth_stubs: 0xd350
+621.2.3.10.3
+  __TEXT.__text: 0x2e8bb08
+  __TEXT.__auth_stubs: 0xd3a0
   __TEXT.__objc_methlist: 0x54d4
-  __TEXT.__const: 0x1b19b0
-  __TEXT.__gcc_except_tab: 0x26adc
+  __TEXT.__const: 0x1b19a0
+  __TEXT.__gcc_except_tab: 0x26b8c
   __TEXT.__swift5_typeref: 0xea
-  __TEXT.__cstring: 0x2a4dad
+  __TEXT.__cstring: 0x2a4b63
   __TEXT.__constg_swiftt: 0x3e8
   __TEXT.__swift5_fieldmd: 0x2a0
   __TEXT.__swift5_reflstr: 0xa4
   __TEXT.__swift5_proto: 0x34
   __TEXT.__swift5_types: 0x54
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__oslogstring: 0xfb97
+  __TEXT.__oslogstring: 0xfc86
   __TEXT.__ustring: 0x262
-  __TEXT.__unwind_info: 0x1c030
+  __TEXT.__unwind_info: 0x1c060
   __TEXT.__eh_frame: 0xe48
   __TEXT.__objc_classname: 0xef7
-  __TEXT.__objc_methname: 0x11f5c
+  __TEXT.__objc_methname: 0x11fad
   __TEXT.__objc_methtype: 0x7e95
-  __TEXT.__objc_stubs: 0x102a0
+  __TEXT.__objc_stubs: 0x10300
   __DATA_CONST.__got: 0x1348
-  __DATA_CONST.__const: 0x47858
+  __DATA_CONST.__const: 0x478a8
   __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x55e8
+  __DATA_CONST.__objc_selrefs: 0x5600
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x260
   __DATA_CONST.__jsc_ops: 0x4c0
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x69c8
+  __AUTH_CONST.__auth_got: 0x69f0
   __AUTH_CONST.__auth_ptr: 0x290
-  __AUTH_CONST.__const: 0x264088
-  __AUTH_CONST.__cfstring: 0x70c0
+  __AUTH_CONST.__const: 0x264220
+  __AUTH_CONST.__cfstring: 0x7120
   __AUTH_CONST.__objc_const: 0x8588
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x270

   __AUTH.__data: 0x15e0
   __DATA.__objc_ivar: 0x478
   __DATA.__data: 0xd4b0
-  __DATA.__common: 0x15b90
-  __DATA.__bss: 0x40258
+  __DATA.__common: 0x15bb0
+  __DATA.__bss: 0x40288
   __DATA_DIRTY.__objc_ivar: 0x5c
   __DATA_DIRTY.__objc_data: 0x870
   __DATA_DIRTY.__data: 0x7680
-  __DATA_DIRTY.__bss: 0x9b89
+  __DATA_DIRTY.__bss: 0x9b59
   __DATA_DIRTY.__common: 0xa799
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 120009
-  Symbols:   128635
-  CStrings:  33444
+  Functions: 119991
+  Symbols:   128602
+  CStrings:  33458
 
Symbols:
+ __ZN3JSC14MicrotaskQueue7enqueueEONS_10QueuedTaskE
+ __ZN3JSC14MicrotaskQueueC1ERNS_2VME
+ __ZN3JSC14MicrotaskQueueD1Ev
+ __ZN6webrtc24registerWebKitVP9DecoderEv
+ __ZN7WebCore10IDBKeyData12isValidValueERKNSt3__17variantIJDnNS0_7InvalidEN3WTF6VectorIS0_Lm0ENS4_15CrashOnOverflowELm16ENS4_10FastMallocEEENS4_6StringEdNS0_4DateENS_20ThreadSafeDataBufferENS0_3MinENS0_3MaxEEEE
+ __ZN7WebCore11FrameLoader19prefetchDNSIfNeededERKN3WTF3URLE
+ __ZN7WebCore14MicrotaskQueue6appendEON3JSC10QueuedTaskE
+ __ZN7WebCore15JSDOMWindowBase25queueMicrotaskToEventLoopERN3JSC14JSGlobalObjectEONS1_10QueuedTaskE
+ __ZN7WebCore16FontCascadeFonts14determinePitchERKNS_22FontCascadeDescriptionEPNS_12FontSelectorE
+ __ZN7WebCore16FontCascadeFonts23realizeFallbackRangesAtERKNS_22FontCascadeDescriptionEPNS_12FontSelectorEj
+ __ZN7WebCore16FontCascadeFonts46determineCanTakeFixedPitchFastContentMeasuringERKNS_22FontCascadeDescriptionEPNS_12FontSelectorE
+ __ZN7WebCore17LibWebRTCProvider24registerWebKitVP9DecoderEv
+ __ZN7WebCore18EventLoopTaskGroup14queueMicrotaskEON3JSC10QueuedTaskE
+ __ZN7WebCore22SWRegistrationDatabase14deleteAllFilesEv
+ __ZN7WebCore24registerWebKitVP9DecoderEv
+ __ZN7WebCore24shouldEnableSWVP9DecoderEv
+ __ZN7WebCore26MediaRecorderPrivateWriter6createENS_26MediaRecorderContainerTypeERNS_34MediaRecorderPrivateWriterListenerE
+ __ZN7WebCore29VideoPresentationInterfaceIOS27audioSessionCategoryChangedENS_20AudioSessionCategoryENS_16AudioSessionModeENS_18RouteSharingPolicyE
+ __ZN9Inspector22ContentSearchUtilities19searcherMatchesTextERKNSt3__17variantIJN3WTF6StringEN3JSC4Yarr17RegularExpressionEEEERKS4_
+ __ZN9Inspector22ContentSearchUtilities23createSearcherForStringERKN3WTF6StringENS0_10SearchTypeENS0_19SearchCaseSensitiveE
+ __ZN9Inspector22ContentSearchUtilities32createRegularExpressionForStringERKN3WTF6StringENS0_10SearchTypeENS0_19SearchCaseSensitiveE
+ __ZNK3JSC20MarkedMicrotaskDeque35hasMicrotasksForFullyActiveDocumentEv
+ __ZNK7WebCore13MediaStrategy32createMediaRecorderPrivateWriterENS_26MediaRecorderContainerTypeERNS_34MediaRecorderPrivateWriterListenerE
+ __ZThn16_N7WebCore34VideoPresentationModelVideoElementD0Ev
+ __ZThn16_N7WebCore34VideoPresentationModelVideoElementD1Ev
- __ZN3JSC14JSGlobalObject14queueMicrotaskEON3WTF3RefINS_9MicrotaskENS1_12RawPtrTraitsIS3_EENS1_21DefaultRefDerefTraitsIS3_EEEE
- __ZN3JSC2VM14clearExceptionEv
- __ZN7WebCore14MicrotaskQueue6appendEONSt3__110unique_ptrINS_13EventLoopTaskENS1_14default_deleteIS3_EEEE
- __ZN7WebCore15JSDOMWindowBase25queueMicrotaskToEventLoopERN3JSC14JSGlobalObjectEON3WTF3RefINS1_9MicrotaskENS4_12RawPtrTraitsIS6_EENS4_21DefaultRefDerefTraitsIS6_EEEE
- __ZN7WebCore16FontCascadeFonts14determinePitchERKNS_22FontCascadeDescriptionE
- __ZN7WebCore16FontCascadeFonts23realizeFallbackRangesAtERKNS_22FontCascadeDescriptionEj
- __ZN7WebCore16FontCascadeFonts46determineCanTakeFixedPitchFastContentMeasuringERKNS_22FontCascadeDescriptionE
- __ZN7WebCore22SWRegistrationDatabase21clearAllRegistrationsEv
- __ZN9Inspector22ContentSearchUtilities38createRegularExpressionForSearchStringERKN3WTF6StringEbNS0_16SearchStringTypeE
- __ZNK7WebCore13MediaStrategy32createMediaRecorderPrivateWriterERKN3WTF6StringERNS_34MediaRecorderPrivateWriterListenerE
CStrings:
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ARM64Assembler.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/AbstractSlotVisitorInlines.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArgList.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBuffer.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBufferView.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DataView.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ExecutableAllocator.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/IndexingHeader.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArray.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCPtrTag.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCast.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObject.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObjectInlines.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/MacroAssemblerARM64.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/WebKitAdditions/EventHandlerIOSTouch.cpp"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/CheckedPtr.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/CryptographicUtilities.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/HashTable.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/JSONValues.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/Markable.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/Ref.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/RefCounted.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/RefPtr.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/TrailingArray.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/WeakRef.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/cocoa/TypeCastsCocoa.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "/AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
+ "AVVideoCaptureSource device has invalid width, height or frameRate capabilities"
+ "Display capture"
+ "Element to fullscreen is disconnected; bailing."
+ "HH"
+ "RealtimeVideoCaptureSource::updateCapabilities max width, max height or max frame rate is 0"
+ "SELECT COUNT(*) FROM Records;"
+ "SWRegistrationDatabase::recordsCount failed on creating statement (%d) - %s"
+ "SWRegistrationDatabase::recordsCount failed to count records (%d) - %s"
+ "T &WTF::WeakPtr<WebCore::HTMLCanvasElement, WebCore::WeakPtrImplWithEventTargetData>::operator*() const [T = WebCore::HTMLCanvasElement, WeakPtrImpl = WebCore::WeakPtrImplWithEventTargetData, PtrTraits = WTF::RawPtrTraits<WebCore::WeakPtrImplWithEventTargetData>]"
+ "Unknown capture"
+ "containsString:"
+ "initWithUnsignedLongLong:"
+ "j"
+ "localizedStringFromNumber:numberStyle:"
+ "match_constness_t<Source, Target> *WTF::downcast(Source *) [Target = WebCore::WebCoreMicrotaskDispatcher, Source = JSC::MicrotaskDispatcher]"
+ "void JSC::SecureARM64EHashPins::forEachPage(Function) [Function = (lambda at /AppleInternal/Library/BuildRoots/620bb219-15ec-11f0-9879-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h:65:17)]"
+ "void WTF::HashTable<WTF::Ref<WTF::SingleThreadWeakPtrImpl>, WTF::KeyValuePair<WTF::Ref<WTF::SingleThreadWeakPtrImpl>, std::unique_ptr<WebCore::ClipperData>>, WTF::KeyValuePairKeyExtractor<WTF::KeyValuePair<WTF::Ref<WTF::SingleThreadWeakPtrImpl>, std::unique_ptr<WebCore::ClipperData>>>, WTF::DefaultHash<WTF::Ref<WTF::SingleThreadWeakPtrImpl>>, WTF::HashMap<WTF::Ref<WTF::SingleThreadWeakPtrImpl>, std::unique_ptr<WebCore::ClipperData>>::KeyValuePairTraits, WTF::HashTraits<WTF::Ref<WTF::SingleThreadWeakPtrImpl>>, WTF::ShouldValidateKey::Yes>::checkKey(const T &) [Key = WTF::Ref<WTF::SingleThreadWeakPtrImpl>, Value = WTF::KeyValuePair<WTF::Ref<WTF::SingleThreadWeakPtrImpl>, std::unique_ptr<WebCore::ClipperData>>, Extractor = WTF::KeyValuePairKeyExtractor<WTF::KeyValuePair<WTF::Ref<WTF::SingleThreadWeakPtrImpl>, std::unique_ptr<WebCore::ClipperData>>>, HashFunctions = WTF::DefaultHash<WTF::Ref<WTF::SingleThreadWeakPtrImpl>>, Traits = WTF::HashMap<WTF::Ref<WTF::SingleThreadWeakPtrImpl>, std::unique_ptr<WebCore::ClipperData>>::KeyValuePairTraits, KeyTraits = WTF::HashTraits<WTF::Ref<WTF::SingleThreadWeakPtrImpl>>, shouldValidateKey = WTF::ShouldValidateKey::Yes, HashTranslator = WTF::HashMapEnsureTranslator<WTF::HashMap<WTF::Ref<WTF::SingleThreadWeakPtrImpl>, std::unique_ptr<WebCore::ClipperData>>::KeyValuePairTraits, WTF::DefaultHash<WTF::Ref<WTF::SingleThreadWeakPtrImpl>>>, T = WTF::Ref<WTF::SingleThreadWeakPtrImpl>]"
+ "void WTF::HashTable<WebCore::IDBResourceIdentifier, WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WTF::RefPtr<WebCore::IDBServer::MemoryIndexCursor>>, WTF::KeyValuePairKeyExtractor<WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WTF::RefPtr<WebCore::IDBServer::MemoryIndexCursor>>>, WTF::DefaultHash<WebCore::IDBResourceIdentifier>, WTF::HashMap<WebCore::IDBResourceIdentifier, WTF::RefPtr<WebCore::IDBServer::MemoryIndexCursor>>::KeyValuePairTraits, WTF::HashTraits<WebCore::IDBResourceIdentifier>, WTF::ShouldValidateKey::Yes>::checkKey(const T &) [Key = WebCore::IDBResourceIdentifier, Value = WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WTF::RefPtr<WebCore::IDBServer::MemoryIndexCursor>>, Extractor = WTF::KeyValuePairKeyExtractor<WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WTF::RefPtr<WebCore::IDBServer::MemoryIndexCursor>>>, HashFunctions = WTF::DefaultHash<WebCore::IDBResourceIdentifier>, Traits = WTF::HashMap<WebCore::IDBResourceIdentifier, WTF::RefPtr<WebCore::IDBServer::MemoryIndexCursor>>::KeyValuePairTraits, KeyTraits = WTF::HashTraits<WebCore::IDBResourceIdentifier>, shouldValidateKey = WTF::ShouldValidateKey::Yes, HashTranslator = WTF::HashMapTranslator<WTF::HashMap<WebCore::IDBResourceIdentifier, WTF::RefPtr<WebCore::IDBServer::MemoryIndexCursor>>::KeyValuePairTraits, WTF::DefaultHash<WebCore::IDBResourceIdentifier>>, T = WebCore::IDBResourceIdentifier]"
+ "void WTF::HashTable<WebCore::IDBResourceIdentifier, WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WTF::RefPtr<WebCore::IDBServer::MemoryObjectStoreCursor>>, WTF::KeyValuePairKeyExtractor<WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WTF::RefPtr<WebCore::IDBServer::MemoryObjectStoreCursor>>>, WTF::DefaultHash<WebCore::IDBResourceIdentifier>, WTF::HashMap<WebCore::IDBResourceIdentifier, WTF::RefPtr<WebCore::IDBServer::MemoryObjectStoreCursor>>::KeyValuePairTraits, WTF::HashTraits<WebCore::IDBResourceIdentifier>, WTF::ShouldValidateKey::Yes>::checkKey(const T &) [Key = WebCore::IDBResourceIdentifier, Value = WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WTF::RefPtr<WebCore::IDBServer::MemoryObjectStoreCursor>>, Extractor = WTF::KeyValuePairKeyExtractor<WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WTF::RefPtr<WebCore::IDBServer::MemoryObjectStoreCursor>>>, HashFunctions = WTF::DefaultHash<WebCore::IDBResourceIdentifier>, Traits = WTF::HashMap<WebCore::IDBResourceIdentifier, WTF::RefPtr<WebCore::IDBServer::MemoryObjectStoreCursor>>::KeyValuePairTraits, KeyTraits = WTF::HashTraits<WebCore::IDBResourceIdentifier>, shouldValidateKey = WTF::ShouldValidateKey::Yes, HashTranslator = WTF::HashMapTranslator<WTF::HashMap<WebCore::IDBResourceIdentifier, WTF::RefPtr<WebCore::IDBServer::MemoryObjectStoreCursor>>::KeyValuePairTraits, WTF::DefaultHash<WebCore::IDBResourceIdentifier>>, T = WebCore::IDBResourceIdentifier]"
+ "void WTF::HashTable<WebCore::IDBResourceIdentifier, WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WTF::WeakPtr<WebCore::IDBServer::MemoryCursor>>, WTF::KeyValuePairKeyExtractor<WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WTF::WeakPtr<WebCore::IDBServer::MemoryCursor>>>, WTF::DefaultHash<WebCore::IDBResourceIdentifier>, WTF::HashMap<WebCore::IDBResourceIdentifier, WTF::WeakPtr<WebCore::IDBServer::MemoryCursor>>::KeyValuePairTraits, WTF::HashTraits<WebCore::IDBResourceIdentifier>, WTF::ShouldValidateKey::Yes>::checkKey(const T &) [Key = WebCore::IDBResourceIdentifier, Value = WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WTF::WeakPtr<WebCore::IDBServer::MemoryCursor>>, Extractor = WTF::KeyValuePairKeyExtractor<WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WTF::WeakPtr<WebCore::IDBServer::MemoryCursor>>>, HashFunctions = WTF::DefaultHash<WebCore::IDBResourceIdentifier>, Traits = WTF::HashMap<WebCore::IDBResourceIdentifier, WTF::WeakPtr<WebCore::IDBServer::MemoryCursor>>::KeyValuePairTraits, KeyTraits = WTF::HashTraits<WebCore::IDBResourceIdentifier>, shouldValidateKey = WTF::ShouldValidateKey::Yes, HashTranslator = WTF::HashMapTranslator<WTF::HashMap<WebCore::IDBResourceIdentifier, WTF::WeakPtr<WebCore::IDBServer::MemoryCursor>>::KeyValuePairTraits, WTF::DefaultHash<WebCore::IDBResourceIdentifier>>, T = WebCore::IDBResourceIdentifier]"
+ "void WTF::HashTable<WebCore::IDBResourceIdentifier, WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WTF::WeakPtr<WebCore::IDBServer::MemoryCursor>>, WTF::KeyValuePairKeyExtractor<WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WTF::WeakPtr<WebCore::IDBServer::MemoryCursor>>>, WTF::DefaultHash<WebCore::IDBResourceIdentifier>, WTF::HashMap<WebCore::IDBResourceIdentifier, WTF::WeakPtr<WebCore::IDBServer::MemoryCursor>>::KeyValuePairTraits, WTF::HashTraits<WebCore::IDBResourceIdentifier>, WTF::ShouldValidateKey::Yes>::checkKey(const T &) [Key = WebCore::IDBResourceIdentifier, Value = WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WTF::WeakPtr<WebCore::IDBServer::MemoryCursor>>, Extractor = WTF::KeyValuePairKeyExtractor<WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WTF::WeakPtr<WebCore::IDBServer::MemoryCursor>>>, HashFunctions = WTF::DefaultHash<WebCore::IDBResourceIdentifier>, Traits = WTF::HashMap<WebCore::IDBResourceIdentifier, WTF::WeakPtr<WebCore::IDBServer::MemoryCursor>>::KeyValuePairTraits, KeyTraits = WTF::HashTraits<WebCore::IDBResourceIdentifier>, shouldValidateKey = WTF::ShouldValidateKey::Yes, HashTranslator = WTF::HashMapTranslatorAdapter<WTF::HashMap<WebCore::IDBResourceIdentifier, WTF::WeakPtr<WebCore::IDBServer::MemoryCursor>>::KeyValuePairTraits, WTF::IdentityHashTranslator<WTF::HashMap<WebCore::IDBResourceIdentifier, WTF::WeakPtr<WebCore::IDBServer::MemoryCursor>>::KeyValuePairTraits, WTF::DefaultHash<WebCore::IDBResourceIdentifier>>>, T = WebCore::IDBResourceIdentifier]"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ARM64Assembler.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/AbstractSlotVisitorInlines.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArgList.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBuffer.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBufferView.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DataView.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ExecutableAllocator.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/IndexingHeader.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArray.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCPtrTag.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCast.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObject.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObjectInlines.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/MacroAssemblerARM64.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/WebKitAdditions/EventHandlerIOSTouch.cpp"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/CheckedPtr.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/CryptographicUtilities.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/HashTable.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/JSONValues.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/Markable.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/Ref.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/RefCounted.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/RefPtr.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/TrailingArray.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/WeakRef.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/cocoa/TypeCastsCocoa.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
- "/AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
- "void JSC::SecureARM64EHashPins::forEachPage(Function) [Function = (lambda at /AppleInternal/Library/BuildRoots/cd4f8b63-0af1-11f0-9708-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h:65:17)]"
- "void WTF::HashTable<WebCore::IDBResourceIdentifier, WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>, WTF::KeyValuePairKeyExtractor<WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>>, WTF::DefaultHash<WebCore::IDBResourceIdentifier>, WTF::HashMap<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>::KeyValuePairTraits, WTF::HashTraits<WebCore::IDBResourceIdentifier>, WTF::ShouldValidateKey::Yes>::checkKey(const T &) [Key = WebCore::IDBResourceIdentifier, Value = WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>, Extractor = WTF::KeyValuePairKeyExtractor<WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>>, HashFunctions = WTF::DefaultHash<WebCore::IDBResourceIdentifier>, Traits = WTF::HashMap<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>::KeyValuePairTraits, KeyTraits = WTF::HashTraits<WebCore::IDBResourceIdentifier>, shouldValidateKey = WTF::ShouldValidateKey::Yes, HashTranslator = WTF::HashMapTranslator<WTF::HashMap<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>::KeyValuePairTraits, WTF::DefaultHash<WebCore::IDBResourceIdentifier>>, T = WebCore::IDBResourceIdentifier]"
- "void WTF::HashTable<WebCore::IDBResourceIdentifier, WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>, WTF::KeyValuePairKeyExtractor<WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>>, WTF::DefaultHash<WebCore::IDBResourceIdentifier>, WTF::HashMap<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>::KeyValuePairTraits, WTF::HashTraits<WebCore::IDBResourceIdentifier>, WTF::ShouldValidateKey::Yes>::checkKey(const T &) [Key = WebCore::IDBResourceIdentifier, Value = WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>, Extractor = WTF::KeyValuePairKeyExtractor<WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>>, HashFunctions = WTF::DefaultHash<WebCore::IDBResourceIdentifier>, Traits = WTF::HashMap<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>::KeyValuePairTraits, KeyTraits = WTF::HashTraits<WebCore::IDBResourceIdentifier>, shouldValidateKey = WTF::ShouldValidateKey::Yes, HashTranslator = WTF::HashMapTranslatorAdapter<WTF::HashMap<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>::KeyValuePairTraits, WTF::IdentityHashTranslator<WTF::HashMap<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>::KeyValuePairTraits, WTF::DefaultHash<WebCore::IDBResourceIdentifier>>>, T = WebCore::IDBResourceIdentifier]"
- "void WTF::HashTable<WebCore::IDBResourceIdentifier, WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>, WTF::KeyValuePairKeyExtractor<WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>>, WTF::DefaultHash<WebCore::IDBResourceIdentifier>, WTF::HashMap<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>::KeyValuePairTraits, WTF::HashTraits<WebCore::IDBResourceIdentifier>, WTF::ShouldValidateKey::Yes>::checkKey(const T &) [Key = WebCore::IDBResourceIdentifier, Value = WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>, Extractor = WTF::KeyValuePairKeyExtractor<WTF::KeyValuePair<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>>, HashFunctions = WTF::DefaultHash<WebCore::IDBResourceIdentifier>, Traits = WTF::HashMap<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>::KeyValuePairTraits, KeyTraits = WTF::HashTraits<WebCore::IDBResourceIdentifier>, shouldValidateKey = WTF::ShouldValidateKey::Yes, HashTranslator = WTF::IdentityHashTranslator<WTF::HashMap<WebCore::IDBResourceIdentifier, WebCore::IDBServer::MemoryCursor *>::KeyValuePairTraits, WTF::DefaultHash<WebCore::IDBResourceIdentifier>>, T = WebCore::IDBResourceIdentifier]"
- "void WTF::HashTable<WebCore::IDBResourceIdentifier, WTF::KeyValuePair<WebCore::IDBResourceIdentifier, std::unique_ptr<WebCore::IDBServer::MemoryIndexCursor>>, WTF::KeyValuePairKeyExtractor<WTF::KeyValuePair<WebCore::IDBResourceIdentifier, std::unique_ptr<WebCore::IDBServer::MemoryIndexCursor>>>, WTF::DefaultHash<WebCore::IDBResourceIdentifier>, WTF::HashMap<WebCore::IDBResourceIdentifier, std::unique_ptr<WebCore::IDBServer::MemoryIndexCursor>>::KeyValuePairTraits, WTF::HashTraits<WebCore::IDBResourceIdentifier>, WTF::ShouldValidateKey::Yes>::checkKey(const T &) [Key = WebCore::IDBResourceIdentifier, Value = WTF::KeyValuePair<WebCore::IDBResourceIdentifier, std::unique_ptr<WebCore::IDBServer::MemoryIndexCursor>>, Extractor = WTF::KeyValuePairKeyExtractor<WTF::KeyValuePair<WebCore::IDBResourceIdentifier, std::unique_ptr<WebCore::IDBServer::MemoryIndexCursor>>>, HashFunctions = WTF::DefaultHash<WebCore::IDBResourceIdentifier>, Traits = WTF::HashMap<WebCore::IDBResourceIdentifier, std::unique_ptr<WebCore::IDBServer::MemoryIndexCursor>>::KeyValuePairTraits, KeyTraits = WTF::HashTraits<WebCore::IDBResourceIdentifier>, shouldValidateKey = WTF::ShouldValidateKey::Yes, HashTranslator = WTF::HashMapTranslator<WTF::HashMap<WebCore::IDBResourceIdentifier, std::unique_ptr<WebCore::IDBServer::MemoryIndexCursor>>::KeyValuePairTraits, WTF::DefaultHash<WebCore::IDBResourceIdentifier>>, T = WebCore::IDBResourceIdentifier]"
- "void WTF::HashTable<WebCore::IDBResourceIdentifier, WTF::KeyValuePair<WebCore::IDBResourceIdentifier, std::unique_ptr<WebCore::IDBServer::MemoryObjectStoreCursor>>, WTF::KeyValuePairKeyExtractor<WTF::KeyValuePair<WebCore::IDBResourceIdentifier, std::unique_ptr<WebCore::IDBServer::MemoryObjectStoreCursor>>>, WTF::DefaultHash<WebCore::IDBResourceIdentifier>, WTF::HashMap<WebCore::IDBResourceIdentifier, std::unique_ptr<WebCore::IDBServer::MemoryObjectStoreCursor>>::KeyValuePairTraits, WTF::HashTraits<WebCore::IDBResourceIdentifier>, WTF::ShouldValidateKey::Yes>::checkKey(const T &) [Key = WebCore::IDBResourceIdentifier, Value = WTF::KeyValuePair<WebCore::IDBResourceIdentifier, std::unique_ptr<WebCore::IDBServer::MemoryObjectStoreCursor>>, Extractor = WTF::KeyValuePairKeyExtractor<WTF::KeyValuePair<WebCore::IDBResourceIdentifier, std::unique_ptr<WebCore::IDBServer::MemoryObjectStoreCursor>>>, HashFunctions = WTF::DefaultHash<WebCore::IDBResourceIdentifier>, Traits = WTF::HashMap<WebCore::IDBResourceIdentifier, std::unique_ptr<WebCore::IDBServer::MemoryObjectStoreCursor>>::KeyValuePairTraits, KeyTraits = WTF::HashTraits<WebCore::IDBResourceIdentifier>, shouldValidateKey = WTF::ShouldValidateKey::Yes, HashTranslator = WTF::HashMapTranslator<WTF::HashMap<WebCore::IDBResourceIdentifier, std::unique_ptr<WebCore::IDBServer::MemoryObjectStoreCursor>>::KeyValuePairTraits, WTF::DefaultHash<WebCore::IDBResourceIdentifier>>, T = WebCore::IDBResourceIdentifier]"
- "void WTF::HashTable<WebCore::IDBServer::MemoryIndexCursor *, WebCore::IDBServer::MemoryIndexCursor *, WTF::IdentityExtractor, WTF::DefaultHash<WebCore::IDBServer::MemoryIndexCursor *>, WTF::HashTraits<WebCore::IDBServer::MemoryIndexCursor *>, WTF::HashTraits<WebCore::IDBServer::MemoryIndexCursor *>, WTF::ShouldValidateKey::Yes>::checkKey(const T &) [Key = WebCore::IDBServer::MemoryIndexCursor *, Value = WebCore::IDBServer::MemoryIndexCursor *, Extractor = WTF::IdentityExtractor, HashFunctions = WTF::DefaultHash<WebCore::IDBServer::MemoryIndexCursor *>, Traits = WTF::HashTraits<WebCore::IDBServer::MemoryIndexCursor *>, KeyTraits = WTF::HashTraits<WebCore::IDBServer::MemoryIndexCursor *>, shouldValidateKey = WTF::ShouldValidateKey::Yes, HashTranslator = WTF::IdentityHashTranslator<WTF::HashTraits<WebCore::IDBServer::MemoryIndexCursor *>, WTF::DefaultHash<WebCore::IDBServer::MemoryIndexCursor *>>, T = WebCore::IDBServer::MemoryIndexCursor *]"

```
