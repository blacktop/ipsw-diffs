## WebCore

> `/System/Library/PrivateFrameworks/WebCore.framework/WebCore`

```diff

-619.2.1.10.2
-  __TEXT.__text: 0x2a47138
+619.2.3.1.0
+  __TEXT.__text: 0x2a48418
   __TEXT.__auth_stubs: 0xc710
   __TEXT.__objc_methlist: 0x49a4
   __TEXT.__const: 0x1a4290
-  __TEXT.__cstring: 0x12f6d7
-  __TEXT.__gcc_except_tab: 0x208d4
-  __TEXT.__oslogstring: 0xf071
+  __TEXT.__cstring: 0x12f297
+  __TEXT.__gcc_except_tab: 0x208c4
+  __TEXT.__oslogstring: 0xf052
   __TEXT.__ustring: 0x262
-  __TEXT.__unwind_info: 0x1d700
+  __TEXT.__unwind_info: 0x1d698
   __TEXT.__eh_frame: 0x560
   __TEXT.__objc_classname: 0xebe
   __TEXT.__objc_methname: 0x119af

   __DATA_CONST.__jsc_ops: 0x4c0
   __AUTH_CONST.__auth_got: 0x63a0
   __AUTH_CONST.__auth_ptr: 0x1a0
-  __AUTH_CONST.__const: 0x25b260
+  __AUTH_CONST.__const: 0x25b138
   __AUTH_CONST.__cfstring: 0x6f60
   __AUTH_CONST.__objc_const: 0x9338
   __AUTH_CONST.__objc_arrayobj: 0x90

   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x1540
-  __AUTH.__data: 0xe60
+  __AUTH.__data: 0xe20
   __DATA.__objc_ivar: 0x464
   __DATA.__data: 0x11c60
   __DATA.__common: 0x12c08

   __DATA_DIRTY.__objc_ivar: 0x6c
   __DATA_DIRTY.__objc_data: 0x870
   __DATA_DIRTY.__data: 0x6d40
-  __DATA_DIRTY.__bss: 0x9fc9
+  __DATA_DIRTY.__bss: 0x9f49
   __DATA_DIRTY.__common: 0xa4a9
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libxslt.1.dylib
   - /usr/lib/libz.1.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  Functions: 117907
-  Symbols:   123840
-  CStrings:  32133
+  Functions: 117889
+  Symbols:   123818
+  CStrings:  32111
 
Symbols:
+ __ZN4fido33encodeMakeCredentialRequestAsCBORERKN3WTF6VectorIhLm0ENS0_15CrashOnOverflowELm16ENS0_10FastMallocEEERKN7WebCore34PublicKeyCredentialCreationOptionsENS_29AuthenticatorSupportedOptions28UserVerificationAvailabilityENSB_23ResidentKeyAvailabilityERKNS1_INS0_6StringELm0ES2_Lm16ES3_EENSt3__18optionalINS_13PinParametersEEEONSJ_INS1_INS7_29PublicKeyCredentialDescriptorELm0ES2_Lm16ES3_EEEE
+ __ZN7WebCore14FrameSelection38removeCaretVisibilitySuppressionReasonENS_32CaretVisibilitySuppressionReasonENS0_22ShouldUpdateAppearanceE
+ __ZN4fido28AuthenticatorGetInfoResponse27setMaxCredentialCountInListEj
+ __ZN7WebCore14FrameSelection35addCaretVisibilitySuppressionReasonENS_32CaretVisibilitySuppressionReasonENS0_22ShouldUpdateAppearanceE
+ __ZN4fido31encodeGetAssertionRequestAsCBORERKN3WTF6VectorIhLm0ENS0_15CrashOnOverflowELm16ENS0_10FastMallocEEERKN7WebCore33PublicKeyCredentialRequestOptionsENS_29AuthenticatorSupportedOptions28UserVerificationAvailabilityERKNS1_INS0_6StringELm0ES2_Lm16ES3_EENSt3__18optionalINS_13PinParametersEEEONSI_INS1_INS7_29PublicKeyCredentialDescriptorELm0ES2_Lm16ES3_EEEE
+ __ZNK7WebCore4Page40contextRangeForActiveWritingToolsSessionEv
+ __ZNK7WebCore4Page41showSelectionForActiveWritingToolsSessionEv
+ __ZN4fido28AuthenticatorGetInfoResponse24setMaxCredentialIDLengthEj
+ __ZN4fido24encodeSilentGetAssertionERKN3WTF6StringERKNS0_6VectorIhLm0ENS0_15CrashOnOverflowELm16ENS0_10FastMallocEEERKNS4_IN7WebCore29PublicKeyCredentialDescriptorELm0ES5_Lm16ES6_EENSt3__18optionalINS_13PinParametersEEE
- __ZN4fido33encodeMakeCredentialRequestAsCBORERKN3WTF6VectorIhLm0ENS0_15CrashOnOverflowELm16ENS0_10FastMallocEEERKN7WebCore34PublicKeyCredentialCreationOptionsENS_29AuthenticatorSupportedOptions28UserVerificationAvailabilityENSB_23ResidentKeyAvailabilityERKNS1_INS0_6StringELm0ES2_Lm16ES3_EENSt3__18optionalINS_13PinParametersEEE
- __ZN7WebCore14FrameSelection18setCaretVisibilityENS_9CaretBase15CaretVisibilityENS0_22ShouldUpdateAppearanceE
- __ZN3PAL36getWTWritingToolsViewControllerClassE
- __ZN4fido31encodeGetAssertionRequestAsCBORERKN3WTF6VectorIhLm0ENS0_15CrashOnOverflowELm16ENS0_10FastMallocEEERKN7WebCore33PublicKeyCredentialRequestOptionsENS_29AuthenticatorSupportedOptions28UserVerificationAvailabilityERKNS1_INS0_6StringELm0ES2_Lm16ES3_EENSt3__18optionalINS_13PinParametersEEE
- __ZN3PAL21WritingToolsUILibraryEb
- __ZN3PAL26get_WTSweepTextEffectClassE
- __ZNK7WebCore4Page28contextRangeForSessionWithIDERKN3WTF4UUIDE
- __ZN3PAL25get_WTTextEffectViewClassE
- __ZN3PAL20get_WTTextChunkClassE
- __ZN3PAL39get_WTReplaceDestinationTextEffectClassE
- __ZN3PAL22getWTWritingToolsClassE
- __ZN3PAL34get_WTReplaceSourceTextEffectClassE
- __ZN3PAL28get_WTReplaceTextEffectClassE
- __ZN3PAL22get_WTTextPreviewClassE
CStrings:
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Ref.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ARM64Assembler.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/RefPtr.h"
+ "void JSC::SecureARM64EHashPins::forEachPage(Function) [Function = (lambda at /AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h:65:17)]"
+ "WritingToolsController::writingToolsSessionDidReceiveAction [action: %!h(MISSING)hu]"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ExecutableAllocator.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObject.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArray.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/MacroAssemblerARM64.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBuffer.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/IndexingHeader.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObjectInlines.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCast.h"
+ "WritingToolsController::writingToolsSessionDidReceiveAction<Composition> [action: %!h(MISSING)hu]"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DataView.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBufferView.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/AbstractSlotVisitorInlines.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "WritingToolsController::didEndWritingToolsSession [accepted: %!d(MISSING)]"
+ "WritingToolsController::didBeginWritingToolsSession [received contexts: %!z(MISSING)u]"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCPtrTag.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/WebKitAdditions/EventHandlerIOSTouch.cpp"
+ "void WebCore::WritingToolsController::showOriginalCompositionForSession()"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/TrailingArray.h"
+ "void WebCore::WritingToolsController::showRewrittenCompositionForSession()"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/JSONValues.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
+ "WritingToolsController::proofreadingSessionDidReceiveSuggestion [received suggestions: %!z(MISSING)u, finished: %!d(MISSING)]"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArgList.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ExceptionScope.h"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
+ "WritingToolsController::compositionSessionDidReceiveTextWithReplacementRange [range: %!l(MISSING)lu, %!l(MISSING)lu; finished: %!d(MISSING)]"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ARM64Assembler.h"
- "auto WebCore::WritingToolsController::contextRangeForSessionWithID(const WritingTools::Session::ID &)::(anonymous class)::operator()(std::monostate) const"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBufferView.h"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "Class PAL::init_WTReplaceSourceTextEffect()_block_invoke"
- "Class PAL::init_WTReplaceDestinationTextEffect()_block_invoke"
- "Class PAL::init_WTTextEffectView()_block_invoke"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/MacroAssemblerARM64.h"
- "/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ExecutableAllocator.h"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Ref.h"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObjectInlines.h"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
- "void WebCore::WritingToolsController::showOriginalCompositionForSession(const WritingTools::Session &)"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/JSONValues.h"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/IndexingHeader.h"
- "Class PAL::init_WTTextChunk()_block_invoke"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
- "_WTReplaceDestinationTextEffect"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArgList.h"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/AbstractSlotVisitorInlines.h"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ExceptionScope.h"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/WebKitAdditions/EventHandlerIOSTouch.cpp"
- "WritingToolsController::writingToolsSessionDidReceiveAction (%!s(MISSING)) [action: %!h(MISSING)hu]"
- "Class PAL::initWTWritingToolsViewController()_block_invoke"
- "WritingToolsController::didEndWritingToolsSession (%!s(MISSING)) [accepted: %!d(MISSING)]"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArray.h"
- "_WTReplaceTextEffect"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObject.h"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
- "void JSC::SecureARM64EHashPins::forEachPage(Function) [Function = (lambda at /AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h:65:17)]"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h"
- "_WTSweepTextEffect"
- "Class PAL::init_WTSweepTextEffect()_block_invoke"
- "WritingToolsController::compositionSessionDidReceiveTextWithReplacementRange (%!s(MISSING)) [range: %!l(MISSING)lu, %!l(MISSING)lu; finished: %!d(MISSING)]"
- "void *PAL::WritingToolsUILibrary(bool)_block_invoke"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
- "Class PAL::init_WTReplaceTextEffect()_block_invoke"
- "_WTTextChunk"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/TrailingArray.h"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
- "WritingToolsController::didBeginWritingToolsSession (%!s(MISSING)) [received contexts: %!z(MISSING)u]"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCPtrTag.h"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DataView.h"
- "_WTTextPreview"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
- "void WebCore::WritingToolsController::showRewrittenCompositionForSession(const WritingTools::Session &)"
- "WTWritingToolsViewController"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
- "/Library/Caches/com.apple.xbs/Sources/WebCore/Source/WebCore/PAL/pal/cocoa/WritingToolsUISoftLink.mm"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
- "Class PAL::init_WTTextPreview()_block_invoke"
- "_WTTextEffectView"
- "Class PAL::initWTWritingTools()_block_invoke"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBuffer.h"
- "_WTReplaceSourceTextEffect"
- "WritingToolsController::proofreadingSessionDidReceiveSuggestions (%!s(MISSING)) [received suggestions: %!z(MISSING)u, finished: %!d(MISSING)]"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
- "WTWritingTools"
- "WritingToolsController::writingToolsSessionDidReceiveAction<Composition> (%!s(MISSING)) [action: %!h(MISSING)hu]"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/RefPtr.h"
- "/AppleInternal/Library/BuildRoots/174e9dbe-6096-11ef-8f57-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCast.h"

```
