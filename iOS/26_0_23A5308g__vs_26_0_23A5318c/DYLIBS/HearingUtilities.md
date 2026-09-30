## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities`

```diff

-494.0.0.0.0
-  __TEXT.__text: 0xa6af0
+495.0.0.0.0
+  __TEXT.__text: 0xa6b08
   __TEXT.__auth_stubs: 0x1110
-  __TEXT.__objc_methlist: 0x7d2c
+  __TEXT.__objc_methlist: 0x7d3c
   __TEXT.__const: 0x3da
   __TEXT.__gcc_except_tab: 0x31a8
-  __TEXT.__cstring: 0xe59b
+  __TEXT.__cstring: 0xe61b
   __TEXT.__oslogstring: 0x35fd
   __TEXT.__dlopen_cstrs: 0x7a7
   __TEXT.__swift5_typeref: 0x46

   __TEXT.__unwind_info: 0x25d0
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x841
-  __TEXT.__objc_methname: 0x141b9
+  __TEXT.__objc_methname: 0x141ce
   __TEXT.__objc_methtype: 0x2183
-  __TEXT.__objc_stubs: 0xed00
+  __TEXT.__objc_stubs: 0xed20
   __DATA_CONST.__got: 0x648
-  __DATA_CONST.__const: 0x3420
+  __DATA_CONST.__const: 0x3428
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4960
+  __DATA_CONST.__objc_selrefs: 0x4968
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x430
   __AUTH_CONST.__auth_got: 0x898
   __AUTH_CONST.__const: 0xd98
-  __AUTH_CONST.__cfstring: 0x8e40
+  __AUTH_CONST.__cfstring: 0x8e60
   __AUTH_CONST.__objc_const: 0xa5d8
   __AUTH_CONST.__objc_intobj: 0xa80
   __AUTH_CONST.__objc_arrayobj: 0x1f8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DF8EB8C0-67A3-3AD4-AB69-B45A0900584B
-  Functions: 3529
-  Symbols:   11383
-  CStrings:  6838
+  UUID: 21C64833-8C5C-318F-9A01-BF6AA1CAAF6F
+  Functions: 3530
+  Symbols:   11387
+  CStrings:  6841
 
Symbols:
+ -[HUNoiseController shouldSuggestANCMode]
+ GCC_except_table53
+ GCC_except_table56
+ _HUBackgroundSoundsEnabledStatusChangedNotification
+ ___65-[HUComfortSoundsController registerHasBlankedScreenNotification]_block_invoke.170
+ ___65-[HUComfortSoundsController registerHasBlankedScreenNotification]_block_invoke.174
+ ___block_literal_global.209
+ ___block_literal_global.334
+ _objc_msgSend$shouldSuggestANCMode
- GCC_except_table47
- ___65-[HUComfortSoundsController registerHasBlankedScreenNotification]_block_invoke.173
- ___65-[HUComfortSoundsController registerHasBlankedScreenNotification]_block_invoke.177
- ___block_literal_global.212
- ___block_literal_global.337
Functions:
~ -[HUComfortSoundsController updateAnalytics] : 588 -> 592
~ ___33-[HUComfortSoundsController init]_block_invoke.17 : 760 -> 792
~ -[HUNoiseController showNotificationForAlertType:] : 1180 -> 1128
+ -[HUNoiseController shouldSuggestANCMode]
CStrings:
+ "IDS Sending(%@) %@ to %{sensitive}@ with %@, priority: %@"
+ "NoiseAlertDamageWarningConsiderSuggestionANC"
+ "com.apple.accessibility.hearing.backgroundsounds.enabled.status.changed"
+ "shouldSuggestANCMode"
- " %@"
- "IDS Sending(%@) %@ to %@ with %@, priority: %@"

```
