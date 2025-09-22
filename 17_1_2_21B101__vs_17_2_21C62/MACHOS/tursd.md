## tursd

> `/usr/libexec/tursd`

```diff

-1042.1.8.0.0
-  __TEXT.__text: 0x7860
-  __TEXT.__auth_stubs: 0x4b0
+1042.2.11.0.0
+  __TEXT.__text: 0x7710
+  __TEXT.__auth_stubs: 0x4a0
   __TEXT.__objc_stubs: 0x1a40
   __TEXT.__objc_methlist: 0xa6c
-  __TEXT.__cstring: 0x85a
-  __TEXT.__oslogstring: 0x32b
+  __TEXT.__cstring: 0x8af
+  __TEXT.__oslogstring: 0x2bd
   __TEXT.__const: 0x40
-  __TEXT.__objc_methname: 0x3570
+  __TEXT.__objc_methname: 0x356e
   __TEXT.__objc_classname: 0x150
-  __TEXT.__objc_methtype: 0x872
-  __TEXT.__gcc_except_tab: 0x1c
-  __TEXT.__unwind_info: 0x2f0
-  __DATA_CONST.__auth_got: 0x268
-  __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x5f8
-  __DATA_CONST.__cfstring: 0x8e0
+  __TEXT.__objc_methtype: 0x884
+  __TEXT.__unwind_info: 0x2e0
+  __DATA_CONST.__auth_got: 0x258
+  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__const: 0x5d8
+  __DATA_CONST.__cfstring: 0x8c0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x1ff0
-  __DATA.__objc_selrefs: 0x8d8
+  __DATA.__objc_const: 0x2000
+  __DATA.__objc_selrefs: 0x8d0
   __DATA.__objc_classrefs: 0x138
   __DATA.__objc_superrefs: 0x40
-  __DATA.__objc_ivar: 0x8c
+  __DATA.__objc_ivar: 0x90
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x58
+  __DATA.__bss: 0x48
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 77883E9B-821E-374F-8E00-B0EA9D9388B3
-  Functions: 265
-  Symbols:   146
-  CStrings:  775
+  UUID: B3196921-EA15-353F-9F9C-D45A58FCD41E
+  Functions: 262
+  Symbols:   143
+  CStrings:  776
 
Symbols:
+ __os_feature_enabled_impl
- _NANOPHONE_APPLICATION_BUNDLE_ID
- __Unwind_Resume
- ___objc_personality_v0
- _objc_initWeak
CStrings:
+ "%\x11"
+ "%@: [TUCallCenter.sharedInstance unholdCall:] to %@"
+ "%s: disabling call notifications while suspended"
+ "%s: refreshing on foregrounding"
+ "+[NPHStateManager updateSharedCallCenter]"
+ "+[NPHStateManager updateSharedCallCenter]_block_invoke"
+ "@\"TUCallProvider\""
+ "FAKE-CONTACT-IDENTIFIER"
+ "NanoContacts"
+ "T@\"TUCallProvider\",&,N,V_mockProvider"
+ "_mockProvider"
+ "callServicesClientCapabilities"
+ "fetchCurrentCalls"
+ "isRTT"
+ "mergedRemoteMembers"
+ "mockProvider"
+ "save"
+ "sensitiveContentWarning"
+ "sensitiveContentWarningFeatureFlagEnabled"
+ "setMockProvider:"
+ "setWantsCallNotificationsDisabledWhileSuspended:"
+ "tomabuct_dev@icloud.com"
+ "updateSharedCallCenter"
- "$\x11"
- "%@: [[NPHStateManager sharedCallCenter] unholdCall:] to %@"
- "NPHStateManagerSharedCallCenterCleared"
- "NPHStateManagerSharedCallCenterRegistered"
- "T@\"NPHDialRequestDisplayDetails\",R,N"
- "T@\"NSArray\",C,N"
- "_isInNanoPhoneApp"
- "bundleIdentifier"
- "clearSharedCallCenter"
- "clearing __sharedCallCenter %@"
- "initWithQueue:"
- "initializeSharedCallCenter"
- "initialized __sharedCallCenter %@"
- "mainBundle"
- "nph_disambiguationDestinations"
- "nph_displayDetails"
- "remoteMembers"
- "setNph_disambiguationDestinations:"
- "sharedCallCenter"
- "tomabuct@me.com"
- "weakSharedCallCenter is non-nil (<rdar://problem/34314071> N111:Fortune15R609:Stale Call notification on phone App UI)"

```
