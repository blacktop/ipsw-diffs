## SiriFindMyUI

> `/System/Library/Assistant/UIPlugins/SiriFindMyUIPlugin.siriUIBundle/Frameworks/SiriFindMyUI.framework/SiriFindMyUI`

```diff

-3402.13.1.0.0
-  __TEXT.__text: 0x60f84
-  __TEXT.__auth_stubs: 0x27f0
+3402.15.1.0.0
+  __TEXT.__text: 0x65d4c
+  __TEXT.__auth_stubs: 0x27c0
   __TEXT.__objc_methlist: 0x10c
-  __TEXT.__const: 0x32f4
-  __TEXT.__cstring: 0xe2c
-  __TEXT.__constg_swiftt: 0x17cc
-  __TEXT.__swift5_typeref: 0x4220
-  __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_reflstr: 0xabb
-  __TEXT.__swift5_fieldmd: 0xfcc
-  __TEXT.__swift5_assocty: 0x508
-  __TEXT.__swift5_proto: 0x144
-  __TEXT.__swift5_types: 0x160
-  __TEXT.__swift5_capture: 0x5d0
-  __TEXT.__oslogstring: 0x383
+  __TEXT.__const: 0x3574
+  __TEXT.__cstring: 0xd6c
+  __TEXT.__constg_swiftt: 0x1730
+  __TEXT.__swift5_typeref: 0x3f08
+  __TEXT.__swift5_builtin: 0xdc
+  __TEXT.__swift5_reflstr: 0xa4b
+  __TEXT.__swift5_fieldmd: 0xfd8
+  __TEXT.__swift5_assocty: 0x568
+  __TEXT.__swift5_proto: 0x160
+  __TEXT.__swift5_types: 0x16c
+  __TEXT.__swift5_capture: 0x530
+  __TEXT.__oslogstring: 0x463
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x1828
-  __TEXT.__eh_frame: 0xb90
+  __TEXT.__unwind_info: 0x17c8
+  __TEXT.__eh_frame: 0x9e0
   __TEXT.__objc_classname: 0x74
-  __TEXT.__objc_methname: 0xf08
+  __TEXT.__objc_methname: 0xfea
   __TEXT.__objc_methtype: 0x73a
-  __DATA_CONST.__got: 0x958
-  __DATA_CONST.__const: 0x150
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__got: 0x9f8
+  __DATA_CONST.__const: 0x138
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x280
+  __DATA_CONST.__objc_selrefs: 0x2a8
   __DATA_CONST.__objc_protorefs: 0x40
-  __AUTH_CONST.__auth_got: 0x13f8
-  __AUTH_CONST.__auth_ptr: 0xdb0
-  __AUTH_CONST.__const: 0x2410
-  __AUTH_CONST.__objc_const: 0x11f0
-  __AUTH.__objc_data: 0x258
-  __AUTH.__data: 0x1268
-  __DATA.__data: 0x2058
-  __DATA.__bss: 0x2990
+  __AUTH_CONST.__auth_got: 0x13e0
+  __AUTH_CONST.__auth_ptr: 0xdb8
+  __AUTH_CONST.__const: 0x22a8
+  __AUTH_CONST.__objc_const: 0x1080
+  __AUTH.__objc_data: 0x208
+  __AUTH.__data: 0x11b8
+  __DATA.__data: 0x2050
+  __DATA.__bss: 0x2cf0
   __DATA.__common: 0x478
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/MapKit.framework/MapKit
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2173
-  Symbols:   502
-  CStrings:  348
+  Functions: 2148
+  Symbols:   520
+  CStrings:  350
 
Symbols:
+ _CNContactIdentifierKey
+ _CNLabelHome
+ _CNLabelOther
+ _CNLabelPhoneNumberHomeFax
+ _CNLabelPhoneNumberMain
+ _CNLabelPhoneNumberMobile
+ _CNLabelPhoneNumberOtherFax
+ _CNLabelPhoneNumberPager
+ _CNLabelPhoneNumberWorkFax
+ _CNLabelPhoneNumberiPhone
+ _CNLabelSchool
+ _CNLabelWork
+ _INPersonHandleLabelHome
+ _INPersonHandleLabelHomeFax
+ _INPersonHandleLabelMain
+ _INPersonHandleLabelMobile
+ _INPersonHandleLabelOther
+ _INPersonHandleLabelPager
+ _INPersonHandleLabelSchool
+ _INPersonHandleLabelWork
+ _INPersonHandleLabelWorkFax
+ _INPersonHandleLabeliPhone
+ _OBJC_CLASS_$_INPerson
+ _OBJC_CLASS_$_INPersonHandle
+ _OBJC_CLASS_$_INScoredPerson
+ _OBJC_CLASS_$_INStartCallIntent
+ _OBJC_CLASS_$_SKIDirectInvocationPayload
+ _objc_release_x9
- _OBJC_CLASS_$_MKDirections
- _OBJC_CLASS_$_MKDirectionsRequest
- _OBJC_CLASS_$_MKMapItem
- _OBJC_CLASS_$_MKPlacemark
- _OBJC_CLASS_$_MKRoute
CStrings:
+ "Open maps to %!s(MISSING)"
+ "[StartAudioCallDirectInvocation] Contact id not found returning nil"
+ "[StartAudioCallDirectInvocation] Could not fetch contact: %!@(MISSING)"
+ "[StartAudioCallDirectInvocation] Fetching contact %!s(MISSING)"
+ "[StartAudioCallDirectInvocation] Making payload"
+ "[StartAudioCallDirectInvocation] Unable to serialize INStartCallIntent"
+ "[StartAudioCallDirectInvocation]Start call: %!s(MISSING)"
+ "backingStore"
+ "com.apple.mobilephone"
+ "com.apple.siri.DirectInvocation.Phone.StartAudioCall"
+ "data"
+ "digits"
+ "identifier"
+ "initWithCallRecordFilter:callRecordToCallBack:audioRoute:destinationType:preferredCallProvider:contacts:ttyType:callCapability:"
+ "initWithIdentifier:"
+ "initWithPerson:recommendation:"
+ "initWithPersonHandle:nameComponents:displayName:image:contactIdentifier:customIdentifier:"
+ "initWithValue:type:"
+ "initWithValue:type:label:"
+ "label"
+ "setScoredAlternatives:"
+ "setUserData:"
+ "typeName"
+ "userData"
- "Expected friend to have contactUUID when fetching phone numbers"
- "Failed to fetch contact, error: %!@(MISSING)"
- "Failed to fetch contact, expected friend's contact to exist"
- "FriendLocationViewModel timer queue"
- "_TtC12SiriFindMyUI30CarPlayFriendLocationViewModel"
- "_phoneNumbers"
- "_travelTimeToFriend"
- "_userLocation"
- "calculateDirectionsWithCompletionHandler:"
- "distance"
- "expectedTravelTime"
- "initWithCoordinate:"
- "initWithPlacemark:"
- "initWithRequest:"
- "navigationButtonDisplayThresholdInMeters"
- "routes"
- "session"
- "setBundleId:"
- "setDestination:"
- "setSource:"
- "stringValue"
- "v24@?0@\"MKDirectionsResponse\"8@\"NSError\"16"

```
