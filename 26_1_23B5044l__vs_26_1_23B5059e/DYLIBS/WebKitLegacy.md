## WebKitLegacy

> `/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy`

```diff

-622.2.5.10.3
-  __TEXT.__text: 0x159aa0
+622.2.9.10.3
+  __TEXT.__text: 0x159fd8
   __TEXT.__auth_stubs: 0x8ab0
   __TEXT.__objc_methlist: 0xf608
   __TEXT.__const: 0x250
   __TEXT.__getClass_cstr: 0x12
   __TEXT.__dlsym_cstr: 0x39
-  __TEXT.__gcc_except_tab: 0x1235c
-  __TEXT.__cstring: 0x1ddbe
+  __TEXT.__gcc_except_tab: 0x1236c
+  __TEXT.__cstring: 0x1de4c
   __TEXT.__oslogstring: 0x141
   __TEXT.__unwind_info: 0x83f8
   __TEXT.__objc_classname: 0x1be0

   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x4570
   __AUTH_CONST.__const: 0x4d80
-  __AUTH_CONST.__cfstring: 0xdd80
+  __AUTH_CONST.__cfstring: 0xdde0
   __AUTH_CONST.__objc_const: 0xfe20
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 0DB7DE36-4502-31C8-B076-CFA0FCCD0B42
+  UUID: C78B8FF4-5764-362F-AC43-BDDD3E330FFF
   Functions: 7182
-  Symbols:   23305
-  CStrings:  9320
+  Symbols:   23304
+  CStrings:  9326
 
Symbols:
- ___PRETTY_FUNCTION__._ZN3WTFL17checkHashTableKeyIN3PAL9SessionIDENS_12KeyValuePairIS2_NSt3__110unique_ptrIN7WebCore21NetworkStorageSessionENS4_14default_deleteIS7_EEEEEENS_24KeyValuePairKeyExtractorISB_EENS_11DefaultHashIS2_EENS_7HashMapIS2_SA_SF_NS_10HashTraitsIS2_EENSH_ISA_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE1ENS_10FastMallocEE18KeyValuePairTraitsESI_NS_22IdentityHashTranslatorISO_SF_EELSL_1ES2_EEvRKT7_
Functions:
~ __ZN18InProcessIDBServerD2Ev : 600 -> 612
~ __ZN18InProcessIDBServerD0Ev : 60 -> 76
~ __ZThn16_N18InProcessIDBServerD0Ev : 80 -> 96
~ __ZN18InProcessIDBServerC2EN3PAL9SessionIDERKN3WTF6StringE : 616 -> 640
~ __ZN7WebCore18StorageSyncManagerD1Ev : 220 -> 244
~ __ZN7WebCore18StorageSyncManager5closeEv : 172 -> 188
~ __ZN24NetworkStorageSessionMap21defaultStorageSessionEv : 216 -> 284
~ __ZN24NetworkStorageSessionMap25switchToNewTestingSessionEv : 380 -> 420
~ __ZN24NetworkStorageSessionMap13ensureSessionEN3PAL9SessionIDERKN3WTF6StringE : 3692 -> 3796
~ __ZN24NetworkStorageSessionMap14destroySessionEN3PAL9SessionIDE : 428 -> 476
~ __ZN24WebResourceLoadScheduler10hostForURLERKN3WTF3URLENS_16CreateHostPolicyE : 1012 -> 1088
~ __ZN24WebResourceLoadSchedulerD2Ev : 304 -> 396
~ __ZN24WebResourceLoadSchedulerD0Ev : 56 -> 72
~ __ZN24WebResourceLoadScheduler20servePendingRequestsEN7WebCore20ResourceLoadPriorityE : 1148 -> 1180
~ __ZN3WTF9HashTableIN3PAL9SessionIDENS_12KeyValuePairIS2_NSt3__110unique_ptrIN7WebCore21NetworkStorageSessionENS4_14default_deleteIS7_EEEEEENS_24KeyValuePairKeyExtractorISB_EENS_11DefaultHashIS2_EENS_7HashMapIS2_SA_SF_NS_10HashTraitsIS2_EENSH_ISA_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE1ENS_10FastMallocEE18KeyValuePairTraitsESI_SM_E6rehashEjPSB_ : 480 -> 668
~ __ZN3WTF9HashTableINS_6StringENS_12KeyValuePairIS1_NSt3__110unique_ptrIN24WebResourceLoadScheduler15HostInformationENS3_14default_deleteIS6_EEEEEENS_24KeyValuePairKeyExtractorISA_EENS_10StringHashENS_7HashMapIS1_S9_SD_NS_10HashTraitsIS1_EENSF_IS9_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE1ENS_10FastMallocEE18KeyValuePairTraitsESG_SK_E6rehashEjPSA_ : 520 -> 664
~ __ZN3WTF9HashTableINS_6StringENS_12KeyValuePairIS1_NSt3__110unique_ptrIN24WebResourceLoadScheduler15HostInformationENS3_14default_deleteIS6_EEEEEENS_24KeyValuePairKeyExtractorISA_EENS_10StringHashENS_7HashMapIS1_S9_SD_NS_10HashTraitsIS1_EENSF_IS9_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE1ENS_10FastMallocEE18KeyValuePairTraitsESG_SK_E6removeEPSA_ : 192 -> 228
~ -[WebView(WebPrivate) setSelectTrailingWhitespaceEnabled:] : 72 -> 76
~ -[WebView(WebPrivate) _setWebGLEnabled:] : 56 -> 52
~ __ZNSt3__110unique_ptrI31WebViewRenderingUpdateSchedulerNS_14default_deleteIS1_EEE5resetB8sn200100EPS1_ : 168 -> 180
~ __ZN24WebAlternativeTextClientD0Ev : 16 -> 24
~ +[WebPreferences initialize] : 16112 -> 16312
~ +[WebPreferences(WebPrivateInternalFeatures) _internalFeatures] : 10892 -> 11016
~ -[WebViewPrivate .cxx_destruct] : 908 -> 928
~ -[WebView(WebViewInternalPreferencesChangedGenerated) _preferencesChangedGenerated:] : 21896 -> 21916
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B_F2ugAvEQYMe59sWDKL1z8YLsyVmWjz4BOkvvs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/CheckedPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~B_F2ugAvEQYMe59sWDKL1z8YLsyVmWjz4BOkvvs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
+ "/AppleInternal/Library/BuildRoots/4~B_F2ugAvEQYMe59sWDKL1z8YLsyVmWjz4BOkvvs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/4~B_F2ugAvEQYMe59sWDKL1z8YLsyVmWjz4BOkvvs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/HashTable.h"
+ "/AppleInternal/Library/BuildRoots/4~B_F2ugAvEQYMe59sWDKL1z8YLsyVmWjz4BOkvvs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/RefCounted.h"
+ "/AppleInternal/Library/BuildRoots/4~B_F2ugAvEQYMe59sWDKL1z8YLsyVmWjz4BOkvvs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/4~B_F2ugAvEQYMe59sWDKL1z8YLsyVmWjz4BOkvvs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
+ "/AppleInternal/Library/BuildRoots/4~B_F2ugAvEQYMe59sWDKL1z8YLsyVmWjz4BOkvvs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~B_F2ugAvEQYMe59sWDKL1z8YLsyVmWjz4BOkvvs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/WeakRef.h"
+ "/AppleInternal/Library/BuildRoots/4~B_F2ugAvEQYMe59sWDKL1z8YLsyVmWjz4BOkvvs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
+ "Enable the navigator.userAgentData JavaScript API"
+ "NavigatorUserAgentDataJavaScriptAPIEnabled"
+ "WebKitNavigatorUserAgentDataJavaScriptAPIEnabled"
- "/AppleInternal/Library/BuildRoots/4~B9scugDvMvX9aPmYI8GJfwmzwSmhzvFdDa5uWuU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/CheckedPtr.h"
- "/AppleInternal/Library/BuildRoots/4~B9scugDvMvX9aPmYI8GJfwmzwSmhzvFdDa5uWuU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
- "/AppleInternal/Library/BuildRoots/4~B9scugDvMvX9aPmYI8GJfwmzwSmhzvFdDa5uWuU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/4~B9scugDvMvX9aPmYI8GJfwmzwSmhzvFdDa5uWuU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/HashTable.h"
- "/AppleInternal/Library/BuildRoots/4~B9scugDvMvX9aPmYI8GJfwmzwSmhzvFdDa5uWuU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/RefCounted.h"
- "/AppleInternal/Library/BuildRoots/4~B9scugDvMvX9aPmYI8GJfwmzwSmhzvFdDa5uWuU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/4~B9scugDvMvX9aPmYI8GJfwmzwSmhzvFdDa5uWuU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
- "/AppleInternal/Library/BuildRoots/4~B9scugDvMvX9aPmYI8GJfwmzwSmhzvFdDa5uWuU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
- "/AppleInternal/Library/BuildRoots/4~B9scugDvMvX9aPmYI8GJfwmzwSmhzvFdDa5uWuU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/WeakRef.h"
- "/AppleInternal/Library/BuildRoots/4~B9scugDvMvX9aPmYI8GJfwmzwSmhzvFdDa5uWuU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"

```
