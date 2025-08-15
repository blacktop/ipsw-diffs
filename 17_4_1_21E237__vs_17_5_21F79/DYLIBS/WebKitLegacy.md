## WebKitLegacy

> `/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy`

```diff

-618.1.15.10.15
-  __TEXT.__text: 0x120194
-  __TEXT.__auth_stubs: 0x8ad0
+618.2.12.10.9
+  __TEXT.__text: 0x120640
+  __TEXT.__auth_stubs: 0x8af0
   __TEXT.__objc_methlist: 0xeb28
-  __TEXT.__const: 0x1a0
-  __TEXT.__gcc_except_tab: 0xd964
-  __TEXT.__cstring: 0xf002
+  __TEXT.__const: 0x1b0
+  __TEXT.__gcc_except_tab: 0xd9a0
+  __TEXT.__cstring: 0xf194
   __TEXT.__oslogstring: 0x136
-  __TEXT.__unwind_info: 0x7e9c
+  __TEXT.__unwind_info: 0x7ea0
   __TEXT.__objc_classname: 0x1c2c
   __TEXT.__objc_methname: 0x18af0
   __TEXT.__objc_methtype: 0x81e8

   __DATA_CONST.__objc_classrefs: 0x810
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__const: 0x4b68
+  __AUTH_CONST.__const: 0x4b60
   __AUTH_CONST.__objc_const: 0x4b80
-  __AUTH_CONST.__cfstring: 0xd3e0
+  __AUTH_CONST.__cfstring: 0xd560
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x4580
+  __AUTH_CONST.__auth_got: 0x4590
   __AUTH.__objc_data: 0x2490
   __AUTH.__data: 0xe8
   __DATA.__objc_ivar: 0x498

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 632D34F6-A6AB-342F-A5AE-D7068136AA62
+  UUID: B7D094A1-13B0-3ED5-8D3F-90DDFA2C4B37
   Functions: 7096
-  Symbols:   22677
-  CStrings:  9074
+  Symbols:   22679
+  CStrings:  9098
 
Symbols:
+ __ZN15WebBlobRegistry8blobTypeERKN3WTF3URLE
+ __ZN15WebEditorClient21requestDOMPasteAccessEN7WebCore22DOMPasteAccessCategoryENS0_16ProcessQualifiedIN3WTF23ObjectIdentifierGenericINS0_19FrameIdentifierTypeENS3_38ObjectIdentifierMainThreadAccessTraitsEEEEERKNS3_6StringE
+ __ZN15WebEditorClient23getClientPasteboardDataERKNSt3__18optionalIN7WebCore11SimpleRangeEEERN3WTF6VectorINS0_4pairINS7_6StringENS7_6RefPtrINS2_12SharedBufferENS7_12RawPtrTraitsISC_EENS7_21DefaultRefDerefTraitsISC_EEEEEELm0ENS7_15CrashOnOverflowELm16ENS7_10FastMallocEEE
+ __ZN7WebCore16BlobRegistryImpl8blobTypeERKN3WTF3URLE
+ __ZN7WebCore16HTMLImageElement10currentSrcEv
+ __ZN7WebCore18CustomElementQueue12processQueueEPN3JSC14JSGlobalObjectE
+ __ZN7WebCore26ValidatedFormListedElement17setCustomValidityERKN3WTF6StringE
- __ZN15WebEditorClient21requestDOMPasteAccessEN7WebCore22DOMPasteAccessCategoryERKN3WTF6StringE
- __ZN15WebEditorClient23getClientPasteboardDataERKNSt3__18optionalIN7WebCore11SimpleRangeEEERN3WTF6VectorINS7_6StringELm0ENS7_15CrashOnOverflowELm16ENS7_10FastMallocEEERNS8_INS7_6RefPtrINS2_12SharedBufferENS7_12RawPtrTraitsISF_EENS7_21DefaultRefDerefTraitsISF_EEEELm0ESA_Lm16ESB_EE
- __ZN7WebCore26CustomElementReactionStack12processQueueEPN3JSC14JSGlobalObjectE
- __ZNK15WebChromeClient17storeAppHighlightEON7WebCore12AppHighlightE
- __ZNSt3__110unique_ptrIN7WebCore18CustomElementQueueENS_14default_deleteIS2_EEED1B8sn170006Ev
CStrings:
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/optional"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/wtf/Expected.h"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/wtf/text/StringCommon.h"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "CSS @starting-style rule"
+ "CSS light-dark()"
+ "CSSLightDarkEnabled"
+ "CSSStartingStyleAtRuleEnabled"
+ "Enable CSS @starting-style rule"
+ "Enable private token usage by third party"
+ "Enable support for CSS light-dark() defined in CSS Color 5"
+ "Private Token usage by third party"
+ "PrivateTokenUsageByThirdPartyEnabled"
+ "WebKitCSSLightDarkEnabled"
+ "WebKitCSSStartingStyleAtRuleEnabled"
+ "WebKitPrivateTokenUsageByThirdPartyEnabled"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/optional"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/include/wtf/Expected.h"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/include/wtf/text/StringCommon.h"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"

```
