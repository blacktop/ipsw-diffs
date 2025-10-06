## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

```diff

-1576.200.36.2.2
-  __TEXT.__text: 0x16e1c0
-  __TEXT.__auth_stubs: 0x2370
-  __TEXT.__objc_methlist: 0x1a2c8
-  __TEXT.__cstring: 0x13598
+1576.200.62.0.0
+  __TEXT.__text: 0x16e488
+  __TEXT.__auth_stubs: 0x2390
+  __TEXT.__objc_methlist: 0x1a2e0
+  __TEXT.__cstring: 0x13578
   __TEXT.__const: 0x1044
-  __TEXT.__oslogstring: 0x124f2
-  __TEXT.__gcc_except_tab: 0x1960
+  __TEXT.__oslogstring: 0x12582
+  __TEXT.__gcc_except_tab: 0x1974
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x8df
   __TEXT.__constg_swiftt: 0x578

   __TEXT.__swift_as_ret: 0x84
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5de0
+  __TEXT.__unwind_info: 0x5df8
   __TEXT.__eh_frame: 0x1378
   __TEXT.__objc_classname: 0x274f
-  __TEXT.__objc_methname: 0x3c4ed
+  __TEXT.__objc_methname: 0x3c5ab
   __TEXT.__objc_methtype: 0x7f80
-  __TEXT.__objc_stubs: 0x20ec0
+  __TEXT.__objc_stubs: 0x20f00
   __DATA_CONST.__got: 0xe60
   __DATA_CONST.__const: 0x3678
   __DATA_CONST.__objc_classlist: 0x830
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x410
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xafb0
+  __DATA_CONST.__objc_selrefs: 0xafc0
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x6b0
   __DATA_CONST.__objc_arraydata: 0x6f8
-  __AUTH_CONST.__auth_got: 0x11c8
-  __AUTH_CONST.__const: 0x3188
-  __AUTH_CONST.__cfstring: 0x11ca0
-  __AUTH_CONST.__objc_const: 0x283a8
+  __AUTH_CONST.__auth_got: 0x11d8
+  __AUTH_CONST.__const: 0x31a8
+  __AUTH_CONST.__cfstring: 0x11c80
+  __AUTH_CONST.__objc_const: 0x28390
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH.__objc_data: 0x26c0
+  __AUTH.__objc_data: 0x2648
   __AUTH.__data: 0x5e8
   __DATA.__objc_ivar: 0x17fc
-  __DATA.__data: 0x3380
+  __DATA.__data: 0x3370
   __DATA.__bss: 0x18b0
   __DATA.__common: 0x28
-  __DATA_DIRTY.__objc_data: 0x2be8
+  __DATA_DIRTY.__objc_data: 0x2c60
   __DATA_DIRTY.__data: 0x30
-  __DATA_DIRTY.__bss: 0x230
+  __DATA_DIRTY.__bss: 0x238
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 463AF421-9FAE-3433-960D-B7A154D296E4
-  Functions: 10058
-  Symbols:   30058
-  CStrings:  16497
+  UUID: EFFCC9F3-6BD3-3850-9BE8-0D12A81F5495
+  Functions: 10062
+  Symbols:   30072
+  CStrings:  16499
 
Symbols:
+ -[TUCallFilterController isRestrictedExclusivelyByScreenTimeForDialRequest:]
+ -[TUCallNotificationManager callTranslationAvailabilityChangedForCall:newValue:]
+ -[TUCallServicesInterface isRestrictedExclusivelyByScreenTime:forBundleIdentifier:performSynchronously:]
+ GCC_except_table173
+ __OBJC_$_CLASS_PROP_LIST_TUFeatureFlags.663
+ __OBJC_$_PROP_LIST_TUFeatureFlags.667
+ ___104-[TUCallServicesInterface isRestrictedExclusivelyByScreenTime:forBundleIdentifier:performSynchronously:]_block_invoke
+ ___104-[TUCallServicesInterface isRestrictedExclusivelyByScreenTime:forBundleIdentifier:performSynchronously:]_block_invoke.119
+ ___104-[TUCallServicesInterface isRestrictedExclusivelyByScreenTime:forBundleIdentifier:performSynchronously:]_block_invoke.cold.1
+ ___53-[TUCallServicesInterface resetCallProvisionalStates]_block_invoke.122
+ ___72-[TUCallServicesInterface _handleCurrentCallsChanged:callsDisconnected:]_block_invoke.121
+ ___block_literal_global.118
+ ___block_literal_global.2013
+ ___block_literal_global.2019
+ ___block_literal_global.234
+ __os_signpost_emit_with_name_impl
+ _objc_msgSend$callTranslationAvailabilityChangedForCall:newValue:
+ _objc_msgSend$isRestrictedExclusivelyByScreenTime:forBundleIdentifier:performSynchronously:
+ _objc_msgSend$isRestrictedExclusivelyByScreenTime:forBundleIdentifier:performSynchronously:reply:
+ _os_signpost_enabled
- -[TUCallNotificationManager callTranslationAvailabilityChangedForCall:]
- -[TUFeatureFlags callEndSpamUIEnhancementEnabled]
- __OBJC_$_CLASS_PROP_LIST_TUFeatureFlags.666
- __OBJC_$_PROP_LIST_TUFeatureFlags.670
- ___53-[TUCallServicesInterface resetCallProvisionalStates]_block_invoke.119
- ___72-[TUCallServicesInterface _handleCurrentCallsChanged:callsDisconnected:]_block_invoke.118
- ___block_literal_global.2016
- ___block_literal_global.2022
- ___block_literal_global.233
- _objc_msgSend$callTranslationAvailabilityChangedForCall:
CStrings:
+ "Error using remote object proxy when requesting synchronous exclusive Screen Time check: %@"
+ "callTranslationAvailabilityChangedForCall:newValue:"
+ "isRestrictedExclusivelyByScreenTime:forBundleIdentifier:performSynchronously:"
+ "isRestrictedExclusivelyByScreenTime:forBundleIdentifier:performSynchronously:reply:"
+ "isRestrictedExclusivelyByScreenTimeForDialRequest:"
+ "nearbyModeChangedForCall"
- " transAvail=%d"
- "CallEndSpamUIEnhancement"
- "callEndSpamUIEnhancementEnabled"
- "callTranslationAvailabilityChangedForCall:"

```
