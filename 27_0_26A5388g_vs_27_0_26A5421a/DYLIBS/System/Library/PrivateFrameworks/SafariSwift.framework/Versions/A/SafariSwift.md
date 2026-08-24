## SafariSwift

> `/System/Library/PrivateFrameworks/SafariSwift.framework/Versions/A/SafariSwift`

```diff

-7625.1.24.11.2
-  __TEXT.__text: 0x5644c
-  __TEXT.__objc_methlist: 0x654
-  __TEXT.__cstring: 0x1b40
-  __TEXT.__const: 0x8198
+7625.1.29.11.25
+  __TEXT.__text: 0x5a910
+  __TEXT.__objc_methlist: 0x69c
+  __TEXT.__cstring: 0x1db0
+  __TEXT.__const: 0x81e8
   __TEXT.__constg_swiftt: 0x1010
-  __TEXT.__swift5_typeref: 0x27a2
+  __TEXT.__swift5_typeref: 0x27f8
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0xbad
-  __TEXT.__swift5_fieldmd: 0xa28
+  __TEXT.__swift5_reflstr: 0xbed
+  __TEXT.__swift5_fieldmd: 0xa40
   __TEXT.__swift5_assocty: 0xe30
   __TEXT.__swift5_proto: 0x62c
   __TEXT.__swift5_types: 0x118
-  __TEXT.__oslogstring: 0xb1a
-  __TEXT.__swift_as_entry: 0x2d0
-  __TEXT.__swift_as_ret: 0x25c
-  __TEXT.__swift_as_cont: 0x254
-  __TEXT.__swift5_capture: 0x150
-  __TEXT.__unwind_info: 0x1cb0
-  __TEXT.__eh_frame: 0x31b0
+  __TEXT.__oslogstring: 0xb6a
+  __TEXT.__swift_as_entry: 0x2d8
+  __TEXT.__swift_as_ret: 0x27c
+  __TEXT.__swift_as_cont: 0x2b4
+  __TEXT.__swift5_capture: 0x198
+  __TEXT.__unwind_info: 0x1de0
+  __TEXT.__eh_frame: 0x3760
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x158
+  __DATA_CONST.__const: 0x140
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x510
+  __DATA_CONST.__objc_selrefs: 0x550
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__got: 0x480
-  __AUTH_CONST.__const: 0x1ec8
-  __AUTH_CONST.__objc_const: 0xad8
-  __AUTH_CONST.__auth_got: 0xdc8
+  __DATA_CONST.__got: 0x5e0
+  __AUTH_CONST.__const: 0x1f68
+  __AUTH_CONST.__objc_const: 0xb18
+  __AUTH_CONST.__auth_got: 0xea0
   __AUTH.__objc_data: 0x200
   __AUTH.__data: 0x348
   __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x1928
+  __DATA.__data: 0x1988
   __DATA.__bss: 0xa1e0
   __DATA.__common: 0x3f0
-  __DATA_DIRTY.__objc_data: 0xc8
+  __DATA_DIRTY.__objc_data: 0xd8
   __DATA_DIRTY.__data: 0x610
   __DATA_DIRTY.__bss: 0x2490
   __DATA_DIRTY.__common: 0x18

   - /System/Library/Frameworks/CoreSpotlight.framework/Versions/A/CoreSpotlight
   - /System/Library/Frameworks/CoreTransferable.framework/Versions/A/CoreTransferable
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/Network.framework/Versions/A/Network
   - /System/Library/Frameworks/TipKit.framework/Versions/A/TipKit
   - /System/Library/Frameworks/UserNotifications.framework/Versions/A/UserNotifications
   - /System/Library/Frameworks/_AppIntents_AppKit.framework/Versions/A/_AppIntents_AppKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2191
-  Symbols:   1478
-  CStrings:  201
+  Functions: 2240
+  Symbols:   1498
+  CStrings:  207
 
Symbols:
+ -[TipsCoordinator dismissClusterOnboardingTipIfNeeded]
+ -[TipsCoordinator presentClusterOnboardingTipFrom:]
+ -[TipsCoordinator userDidOpenRelatedTabsView]
+ _OBJC_CLASS_$_WBSSharedFeatureAvailability
+ __swift__destructor
+ _objc_msgSend$bounds
+ _objc_msgSend$dismissClusterOnboardingTipIfNeeded
+ _objc_msgSend$isHidden
+ _objc_msgSend$isPageClusteringEnabled
+ _objc_msgSend$presentClusterOnboardingTipFrom:
+ _objc_msgSend$showRelativeToRect:ofView:preferredEdge:
+ _objc_msgSend$userDidOpenRelatedTabsView
+ _objc_msgSend$window
+ _symbolic So6NSViewCSgXw
+ _symbolic So6NSViewCSgXwz_Xx
+ _symbolic _____ 14SafariSharedUI30WBSClusterOnboardingTipManagerC
+ _symbolic _____Sg 7Network6NWPathV
+ _symbolic _____Sg 7Network6NWPathV6StatusO
+ _symbolic _____Sg_ABt 7Network6NWPathV6StatusO
+ _symbolic _____y______pG s23_ContiguousArrayStorageC s7CVarArgP
CStrings:
+ "Safari was unable to check for changes because the network connection was unavailable, but will try again %@."
+ "Safari was unable to check for changes because the page was blocked by Screen Time, but will try again %@."
+ "Safari was unable to check for changes because the page was not found, but will try again %@."
+ "Safari was unable to check for changes because the server returned an error, but will try again %@."
+ "Safari was unable to check for changes because this %1$@ needed to cool down, but will try again %2$@."
+ "Safari was unable to check for changes because this %1$@ was in Low Power Mode, but will try again %2$@."
+ "shortcutsAutomationUUID was nil when notifying for Notify Me failure."
- " was visited on "
```
