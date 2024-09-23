## AssistantServices

> `/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices`

```diff

-3401.21.1.0.0
-  __TEXT.__text: 0x1a1b80
+3401.26.2.0.0
+  __TEXT.__text: 0x1a2424
   __TEXT.__auth_stubs: 0x1530
-  __TEXT.__objc_methlist: 0x199cc
+  __TEXT.__objc_methlist: 0x199fc
   __TEXT.__const: 0x458
   __TEXT.__gcc_except_tab: 0x2570
-  __TEXT.__cstring: 0x3b5a1
-  __TEXT.__oslogstring: 0xff09
+  __TEXT.__cstring: 0x3b6bc
+  __TEXT.__oslogstring: 0xffca
   __TEXT.__dlopen_cstrs: 0x42e
-  __TEXT.__unwind_info: 0x79f0
+  __TEXT.__unwind_info: 0x7a28
   __TEXT.__objc_classname: 0x4e2f
-  __TEXT.__objc_methname: 0x3a462
+  __TEXT.__objc_methname: 0x3a4e6
   __TEXT.__objc_methtype: 0xa8ea
-  __TEXT.__objc_stubs: 0x23e20
+  __TEXT.__objc_stubs: 0x23e60
   __DATA_CONST.__got: 0x1610
-  __DATA_CONST.__const: 0x80f8
+  __DATA_CONST.__const: 0x8120
   __DATA_CONST.__objc_classlist: 0xda8
   __DATA_CONST.__objc_catlist: 0x290
   __DATA_CONST.__objc_protolist: 0x550
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbe48
+  __DATA_CONST.__objc_selrefs: 0xbe68
   __DATA_CONST.__objc_protorefs: 0x140
   __DATA_CONST.__objc_superrefs: 0xdb8
-  __DATA_CONST.__objc_arraydata: 0x1f68
+  __DATA_CONST.__objc_arraydata: 0x1fa8
   __AUTH_CONST.__auth_got: 0xaa8
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x3840
-  __AUTH_CONST.__cfstring: 0x267e0
-  __AUTH_CONST.__objc_const: 0x39c98
-  __AUTH_CONST.__objc_intobj: 0x22c8
-  __AUTH_CONST.__objc_dictobj: 0xb68
+  __AUTH_CONST.__const: 0x3880
+  __AUTH_CONST.__cfstring: 0x268a0
+  __AUTH_CONST.__objc_const: 0x39cb8
+  __AUTH_CONST.__objc_intobj: 0x2328
+  __AUTH_CONST.__objc_dictobj: 0xb90
   __AUTH_CONST.__objc_arrayobj: 0x588
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x73f0
   __AUTH.__data: 0x2f0
   __DATA.__objc_ivar: 0x2538
   __DATA.__data: 0x4108
-  __DATA.__bss: 0x1318
+  __DATA.__bss: 0x1300
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x14a0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x168
+  __DATA_DIRTY.__bss: 0x1a0
   __DATA_DIRTY.__common: 0xf8
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 11596
-  Symbols:   13791
-  CStrings:  18876
+  Functions: 11613
+  Symbols:   13808
+  CStrings:  18893
 
Symbols:
+ _AFSiriClientStateManagerTransactionReasonGetIsValidAndSpecified
+ _AFSiriClientStateManagerTransactionReasonGetName
+ _AFAssistantRestrictedWithReason
+ _AFSiriClientStateManagerTransactionReasonGetFromName
+ __AFPreferencesSearchQueriesDataSharingStatusIsForced
+ _AFHasGreenTeaCapability
+ __AFPreferencesValueIsForcedWithContext
+ _AFPreferencesAssistantIsRestrictedWithReason
+ _AFSiriClientStateManagerTransactionReasonGetIsValid
CStrings:
+ "startRecording"
+ "-[AFSiriClientStateManager endTransactionForReason:]_block_invoke"
+ "-[AFSiriClientStateManager beginTransactionForReason:]_block_invoke"
+ "%!s(MISSING) Started transaction for reason: %!@(MISSING)"
+ "endTransactionForReason:"
+ "connectionFailed"
+ "%!s(MISSING) Not begining transaction for reason: %!@(MISSING)"
+ "failRequest"
+ "-[AFSettingsConnection isSearchDataSharingStatusForced:]"
+ "-[AFSettingsConnection isSearchDataSharingStatusForced:]_block_invoke"
+ "%!s(MISSING) Checking if Search Queries Data Sharing status is configured by profile"
+ "GREENTEA_"
+ "_shouldSetTurnIdentifierForRequest"
+ "isSearchDataSharingStatusForced:"
+ "green-tea"
+ "isSearchDataSharingStatusForced"
+ "beginTransactionForReason:"
+ "%!s(MISSING) Ending transaction for reason: %!@(MISSING)"
- "-[AFSiriClientStateManager endTransaction]_block_invoke"
- "hasBobbleCapability"

```
