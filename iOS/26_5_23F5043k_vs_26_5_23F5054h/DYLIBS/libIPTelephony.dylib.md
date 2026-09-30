## libIPTelephony.dylib

> `/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`

```diff

-2655.0.0.0.0
-  __TEXT.__text: 0x50c10c
+2656.2.0.0.0
+  __TEXT.__text: 0x50c5f0
   __TEXT.__auth_stubs: 0x2d80
   __TEXT.__init_offsets: 0x158
   __TEXT.__objc_methlist: 0x748
   __TEXT.__const: 0x2000b
-  __TEXT.__gcc_except_tab: 0x4ea30
-  __TEXT.__cstring: 0x37b39
-  __TEXT.__oslogstring: 0xf866
-  __TEXT.__unwind_info: 0x18e58
+  __TEXT.__gcc_except_tab: 0x4eb2c
+  __TEXT.__cstring: 0x37b31
+  __TEXT.__oslogstring: 0xf984
+  __TEXT.__unwind_info: 0x18e68
   __TEXT.__objc_classname: 0x12f
   __TEXT.__objc_methname: 0x1de8
   __TEXT.__objc_methtype: 0x1118

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 4C4F6AD1-F343-3598-BA53-C8DFB3F1512B
-  Functions: 17036
-  Symbols:   51083
-  CStrings:  9998
+  UUID: 02A479D6-4A62-3F2F-8A78-BB297A415199
+  Functions: 17037
+  Symbols:   51086
+  CStrings:  10001
 
Symbols:
+ __ZZN14IMSCallManager25initializeMOLazuliSessionERK16LazuliSendParamsbbEN14MlsInviteGuardD1Ev
Functions:
~ __ZN14IMSCallManager25initializeMOLazuliSessionERK16LazuliSendParamsbb : 3700 -> 3404
+ __ZZN14IMSCallManager25initializeMOLazuliSessionERK16LazuliSendParamsbbEN14MlsInviteGuardD1Ev
- __ZN7ImsUuidC2ERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZN7ImsUuidC2ERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
~ __ZN14MessageSession28handleConferenceNotificationERK6SipUriRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE : 1016 -> 1200
~ __ZN13LazuliSession12processEventEP14BambiCallEvent : 6000 -> 6180
~ __ZN21SipRegistrationClient11checkTimersEv : 2112 -> 2284
CStrings:
+ "#E %{private, mask.hash}sInvalid SipStack"
+ "#E Didn't send outgoing INVITE with Mls Blob because session already established. Try again later."
+ "#W %{private, mask.hash}sbailing timer check as expiration is not yet set"
+ "%{private, mask.hash}sLeave Group trx %s, conv %s, isSuccess: %{bool}d"
+ "/AppleInternal/Library/BuildRoots/4~CMtyugDll0VQfWWvTs3a5LfhUiVkTNpbtapgyd8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "/AppleInternal/Library/BuildRoots/4~CMtyugDll0VQfWWvTs3a5LfhUiVkTNpbtapgyd8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "Session already established"
- "/AppleInternal/Library/BuildRoots/4~CLiFugAywAN70dlBZGt_kvP6_Kq2XuseBk3x9Os/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "/AppleInternal/Library/BuildRoots/4~CLiFugAywAN70dlBZGt_kvP6_Kq2XuseBk3x9Os/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "Leave Group trx "
- "session found for "

```
