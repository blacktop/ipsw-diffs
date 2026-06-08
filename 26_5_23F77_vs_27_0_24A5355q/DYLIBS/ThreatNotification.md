## ThreatNotification

> `/System/Library/PrivateFrameworks/ThreatNotification.framework/ThreatNotification`

```diff

-24.100.19.0.0
-  __TEXT.__text: 0x17a4
-  __TEXT.__auth_stubs: 0x490
+46.0.0.0.0
+  __TEXT.__text: 0x1760
   __TEXT.__objc_methlist: 0xc8
   __TEXT.__const: 0xa2
-  __TEXT.__cstring: 0x34
+  __TEXT.__cstring: 0x36
   __TEXT.__oslogstring: 0x4e
   __TEXT.__swift5_typeref: 0x5e
   __TEXT.__unwind_info: 0xd8
   __TEXT.__eh_frame: 0x80
-  __TEXT.__objc_classname: 0x2b
-  __TEXT.__objc_methname: 0x271
-  __TEXT.__objc_methtype: 0x63
-  __TEXT.__objc_stubs: 0xe0
-  __DATA_CONST.__got: 0x60
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x38
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x250
+  __DATA_CONST.__got: 0x60
   __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_const: 0x1a8
+  __AUTH_CONST.__auth_got: 0x288
   __AUTH.__objc_data: 0xc0
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 5D1B6A63-E168-3590-AD00-734F0A6FE7CB
+  UUID: 259EDED1-88D6-3446-BA0E-B9E9F649A1C8
   Functions: 30
-  Symbols:   115
-  CStrings:  44
+  Symbols:   122
+  CStrings:  10
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x21
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x8
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
- _objc_release_x8
- _swift_release
- _swift_retain
Functions:
~ -[TNFollowUpItemConfiguration initWithPrimaryAccountAltDSID:expirationDate:] : 144 -> 152
~ -[TNFollowUpItemConfiguration description] : 388 -> 360
~ sub_296af8298 -> sub_2a9035284 : 392 -> 368
~ sub_296af84a8 -> sub_2a903547c : 1016 -> 972
~ sub_296af88d4 -> sub_2a903587c : 1024 -> 1080
~ sub_296af8cd4 -> sub_2a9035cb4 : 716 -> 680
~ sub_296af9030 -> sub_2a9035fec : 344 -> 376
~ sub_296af93f0 -> sub_2a90363cc : 176 -> 184
~ sub_296af94a0 -> sub_2a9036484 : 304 -> 256
~ sub_296af9634 -> sub_2a90365e8 : 96 -> 104
CStrings:
- ".cxx_destruct"
- "@\"NSDate\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "B16@0:8"
- "B24@0:8^@16"
- "B32@0:8@16^@24"
- "T@\"NSDate\",R,N,V_expirationDate"
- "T@\"NSString\",R,N,V_primaryAccountAltDSID"
- "T@\"TNController\",N,R"
- "TNController"
- "TNFollowUpItemConfiguration"
- "_expirationDate"
- "_primaryAccountAltDSID"
- "arrayWithObjects:count:"
- "clearFollowUpItemWithError:"
- "componentsJoinedByString:"
- "description"
- "expirationDate"
- "followUpController"
- "init"
- "initWithPrimaryAccountAltDSID:"
- "initWithPrimaryAccountAltDSID:expirationDate:"
- "isFollowUpItemPending"
- "isOnBoardingFlowRequired"
- "onBoardingController"
- "postFollowUpItemWithConfiguration:error:"
- "primaryAccountAltDSID"
- "repostFollowUpItemIfNeededWithError:"
- "sharedInstance"
- "stringWithFormat:"
- "v16@0:8"

```
