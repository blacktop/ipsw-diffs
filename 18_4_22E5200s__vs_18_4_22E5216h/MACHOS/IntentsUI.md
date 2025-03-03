## IntentsUI

> `/Applications/InCallService.app/PlugIns/IntentsUI.appex/IntentsUI`

```diff

-2975.500.125.2.4
-  __TEXT.__text: 0x69174
-  __TEXT.__auth_stubs: 0x1a60
-  __TEXT.__objc_stubs: 0x9040
-  __TEXT.__objc_methlist: 0x4bdc
+2975.500.161.2.1
+  __TEXT.__text: 0x6b4e0
+  __TEXT.__auth_stubs: 0x1a70
+  __TEXT.__objc_stubs: 0x9140
+  __TEXT.__objc_methlist: 0x4c2c
   __TEXT.__cstring: 0x30a2
   __TEXT.__objc_classname: 0x57f
-  __TEXT.__objc_methname: 0xeb87
+  __TEXT.__objc_methname: 0xeca3
   __TEXT.__objc_methtype: 0x20f5
-  __TEXT.__oslogstring: 0x2332
+  __TEXT.__oslogstring: 0x23ff
   __TEXT.__const: 0x14e0
-  __TEXT.__gcc_except_tab: 0x2b4
+  __TEXT.__gcc_except_tab: 0x2cc
   __TEXT.__constg_swiftt: 0xabc
-  __TEXT.__swift5_typeref: 0xdbc
+  __TEXT.__swift5_typeref: 0xdba
   __TEXT.__swift5_reflstr: 0x64f
   __TEXT.__swift5_fieldmd: 0x738
   __TEXT.__swift5_builtin: 0x78

   __TEXT.__swift_as_ret: 0xec
   __TEXT.__swift5_mpenum: 0x1c
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x1df8
-  __TEXT.__eh_frame: 0x2e20
-  __DATA_CONST.__auth_got: 0xd40
-  __DATA_CONST.__got: 0x750
+  __TEXT.__unwind_info: 0x1e38
+  __TEXT.__eh_frame: 0x2ec8
+  __DATA_CONST.__auth_got: 0xd48
+  __DATA_CONST.__got: 0x758
   __DATA_CONST.__auth_ptr: 0x4f0
-  __DATA_CONST.__const: 0x26e0
+  __DATA_CONST.__const: 0x2708
   __DATA_CONST.__cfstring: 0xe60
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x58

   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0x77e8
-  __DATA.__objc_selrefs: 0x3280
-  __DATA.__objc_ivar: 0x404
+  __DATA.__objc_const: 0x7848
+  __DATA.__objc_selrefs: 0x32d0
+  __DATA.__objc_ivar: 0x40c
   __DATA.__objc_data: 0x1830
-  __DATA.__data: 0x1d68
+  __DATA.__data: 0x1d70
   __DATA.__bss: 0x1600
   __DATA.__common: 0x110
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/CommonUtilities.framework/CommonUtilities
   - /System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreEmoji.framework/CoreEmoji
   - /System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers
   - /System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore
   - /System/Library/PrivateFrameworks/IDS.framework/IDS

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2497
-  Symbols:   516
-  CStrings:  3092
+  Functions: 2506
+  Symbols:   518
+  CStrings:  3111
 
Symbols:
+ _CEMCreateStringByStrippingEmojiCharacters
+ _OBJC_CLASS_$_NSCharacterSet
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initEnumMetadataMultiPayloadWithLayoutString
- _swift_initStructMetadataWithLayoutString
- _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_multiPayloadEnumGeneric_getEnumTag
CStrings:
+ "TB,N,V_hasPendingUpdates"
+ "TB,N,V_hasUpdated"
+ "VMD(%s) estimatedAccountCount: %ld"
+ "VMD(%s) isMessageWaiting: %{bool}d"
+ "VMD(%s) isSubscribed: %{bool}d"
+ "VMD(%s) online: %{bool}d"
+ "VMD(%s) storageUsage: %lu"
+ "_hasPendingUpdates"
+ "_hasUpdated"
+ "fetchRecentCalls:"
+ "hasPendingUpdates"
+ "hasUpdated"
+ "parsedNamesStrippingEmoji"
+ "setHasPendingUpdates:"
+ "setHasUpdated:"
+ "stringByTrimmingCharactersInSet:"
+ "subarrayWithRange:"
+ "updateRecentCalls:"
+ "updateWithRecentCalls:"
+ "whitespaceCharacterSet"
- "fetchRecentCalls"

```
