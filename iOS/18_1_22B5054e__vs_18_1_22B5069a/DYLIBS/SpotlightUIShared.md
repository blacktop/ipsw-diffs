## SpotlightUIShared

> `/System/Library/PrivateFrameworks/SpotlightUIShared.framework/SpotlightUIShared`

```diff

-115.0.0.0.0
-  __TEXT.__text: 0xdc94
+117.0.0.0.0
+  __TEXT.__text: 0xd890
   __TEXT.__auth_stubs: 0xd90
   __TEXT.__objc_methlist: 0x298
-  __TEXT.__const: 0xd68
-  __TEXT.__cstring: 0x5a8
+  __TEXT.__const: 0xd58
+  __TEXT.__cstring: 0xae8
   __TEXT.__ustring: 0x7d2
   __TEXT.__oslogstring: 0xa2
   __TEXT.__swift5_typeref: 0x6b0

   __TEXT.__swift5_proto: 0xb4
   __TEXT.__swift5_types: 0x2c
   __TEXT.__swift5_capture: 0xb0
-  __TEXT.__unwind_info: 0x608
+  __TEXT.__unwind_info: 0x600
   __TEXT.__eh_frame: 0x7d4
   __TEXT.__objc_classname: 0xa9
   __TEXT.__objc_methname: 0xfe9
   __TEXT.__objc_methtype: 0x23f
   __TEXT.__objc_stubs: 0xf60
-  __DATA_CONST.__got: 0x238
-  __DATA_CONST.__const: 0x1d0
+  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__const: 0x1d8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH.__objc_data: 0x180
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x4d0
-  __DATA.__bss: 0x12c8
-  __DATA.__common: 0xb0
+  __DATA.__bss: 0x12b8
+  __DATA.__common: 0x98
   __DATA_DIRTY.__objc_data: 0x158
   __DATA_DIRTY.__data: 0xd0
   __DATA_DIRTY.__bss: 0x490

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 406
-  Symbols:   266
-  CStrings:  303
+  Functions: 402
+  Symbols:   267
+  CStrings:  320
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
CStrings:
+ "Action that toggles Spotlight visibility"
+ "Description for ClearSpotlightIntent"
+ "Description for SearchSpotlightIntent; intent that opens Spotlight and starts a search"
+ "Description for ToggleSpotlightIntent; intent which shows or hides Spotlight, or toggles between these states."
+ "Display name for entity that retrieves the current search string in the Searchfield in Spotlight"
+ "Name of action that closes Spotlight"
+ "Name of action that dismisses Spotlight"
+ "Name of action that hides Spotlight"
+ "Name of action that launches Spotlight"
+ "Name of action that opens Spotlight"
+ "Name of action that shows Spotlight"
+ "Parameter title for action of ToggleSpotlightIntent; Action can have values Toggle, Show, Hide"
+ "Title for ClearSpotlightIntent; intent which clears the current search and returns to the recents and suggestions page."
+ "Title for SearchSpotlightIntent; intent that opens Spotlight and starts a search"
+ "Title for ToggleSpotlightIntent; intent which shows or hides Spotlight, or toggles between these states."
+ "Title for parameter of SearchSpotlightIntent that represents the search query text the user wants to search for"
+ "Type name for enum type that defines presentation actions for Spotlight (Toggle, Open, Close)"

```
