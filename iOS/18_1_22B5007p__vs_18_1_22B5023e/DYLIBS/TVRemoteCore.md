## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore`

```diff

-443.0.31.0.0
-  __TEXT.__text: 0xb9864
+443.10.8.0.0
+  __TEXT.__text: 0xb5c4c
   __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_methlist: 0x85fc
-  __TEXT.__const: 0x23f50
-  __TEXT.__gcc_except_tab: 0xf00
-  __TEXT.__cstring: 0x52b0
-  __TEXT.__oslogstring: 0x81d9
-  __TEXT.__unwind_info: 0x1c48
-  __TEXT.__eh_frame: 0x880
+  __TEXT.__objc_methlist: 0x8614
+  __TEXT.__const: 0x23c40
+  __TEXT.__gcc_except_tab: 0xf48
+  __TEXT.__cstring: 0x5305
+  __TEXT.__oslogstring: 0x8366
+  __TEXT.__unwind_info: 0x1c88
+  __TEXT.__eh_frame: 0x7f8
   __TEXT.__objc_classname: 0x10cc
-  __TEXT.__objc_methname: 0x12253
+  __TEXT.__objc_methname: 0x122e4
   __TEXT.__objc_methtype: 0x3ca2
-  __TEXT.__objc_stubs: 0xb8e0
-  __DATA_CONST.__got: 0x770
-  __DATA_CONST.__const: 0x19d0
+  __TEXT.__objc_stubs: 0xb9c0
+  __DATA_CONST.__got: 0x778
+  __DATA_CONST.__const: 0x1a08
   __DATA_CONST.__objc_classlist: 0x418
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3cd0
+  __DATA_CONST.__objc_selrefs: 0x3d08
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x348
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__auth_got: 0x670
-  __AUTH_CONST.__const: 0x3f50
-  __AUTH_CONST.__cfstring: 0x7400
+  __AUTH_CONST.__const: 0x3b38
+  __AUTH_CONST.__cfstring: 0x74c0
   __AUTH_CONST.__objc_const: 0x11918
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0xa0

   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x27b0
   __DATA.__objc_ivar: 0xa24
-  __DATA.__data: 0x12c0
+  __DATA.__data: 0x1280
   __DATA.__bss: 0x130
-  __DATA.__common: 0x9ec
+  __DATA.__common: 0x9f8
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
+  - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3207
-  Symbols:   3942
-  CStrings:  5443
+  Functions: 3240
+  Symbols:   3956
+  CStrings:  5463
 
Symbols:
+ _OBJC_CLASS_$_ACAccountStore
+ _TVRCFetchSupportedActionsEvent
+ _TVRCSessionStart
+ _TVRCSessionStop
CStrings:
+ "Could not send SessionStart for companionLinkClient %!{(MISSING)public}@. Error - %!{(MISSING)public}@"
+ "Could not send SessionStop for companionLinkClient %!{(MISSING)public}@. Error - %!{(MISSING)public}@"
+ "FetchSupportedActionsEvent"
+ "START: Active queries: %!@(MISSING) - before adding: %!@(MISSING)"
+ "STOP: Active queries: %!@(MISSING) - before removing: %!@(MISSING)"
+ "Session started for companionLinkClient %!{(MISSING)public}@."
+ "Session stopped for companionLinkClient %!{(MISSING)public}@."
+ "SportingEvent"
+ "Successfully registered %!{(MISSING)public}@"
+ "TVRCSessionStart"
+ "TVRCSessionStop"
+ "US"
+ "_sendSessionStart"
+ "_sendSessionStop"
+ "ams_activeiTunesAccount"
+ "ams_sharedAccountStore"
+ "ams_storefront"
+ "country"
+ "countryCode"
+ "preferredLanguages"
+ "setEventIDRegistrationCompletion:"
- "localeIdentifier"

```
