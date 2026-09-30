## AppTrackingTransparency

> `/System/Library/Frameworks/AppTrackingTransparency.framework/AppTrackingTransparency`

```diff

 106.1.1.0.0
-  __TEXT.__text: 0x21fc
-  __TEXT.__auth_stubs: 0x320
+  __TEXT.__text: 0x22dc
+  __TEXT.__auth_stubs: 0x2f0
   __TEXT.__objc_methlist: 0x144
   __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0x1b0
   __TEXT.__cstring: 0x1aa
   __TEXT.__oslogstring: 0x6f6
-  __TEXT.__unwind_info: 0x100
+  __TEXT.__unwind_info: 0x108
   __TEXT.__objc_classname: 0x4c
   __TEXT.__objc_methname: 0x496
   __TEXT.__objc_methtype: 0x86

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x188
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1a0
+  __AUTH_CONST.__auth_got: 0x188
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x188

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FD31B987-6D31-3618-87F7-0B2D6DCD8A43
+  UUID: 79E1D66B-E591-37B3-A166-1B09631DDD26
   Functions: 40
-  Symbols:   243
+  Symbols:   240
   CStrings:  120
 
Symbols:
+ _objc_autoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
- _objc_storeStrong
Functions:
~ +[ATTrackingEnforcementManager setLastBagLookup:] : 16 -> 64
~ +[ATTrackingEnforcementManager lastBagLookup] : 12 -> 60
~ +[ATTrackingEnforcementManager _refreshEnforcementStatusInBackground] : 632 -> 624
~ ___69+[ATTrackingEnforcementManager _refreshEnforcementStatusInBackground]_block_invoke.7 : 360 -> 364
~ +[ATTrackingEnforcementManager shouldEnforceTrackingWithReasonCode:] : 416 -> 436
~ +[ATTrackingManager _restrictionProfileInstalled] : 76 -> 80
~ +[ATTrackingManager _userAllowedToChangeSettings] : 124 -> 132
~ +[ATTrackingManager _isCrossAppTrackingAllowed] : 80 -> 84
~ +[ATTrackingManager _sendRequestTrackingAnalytic:prompted:deniedReason:] : 248 -> 264
~ +[ATTrackingManager _sendTrackingStatusAnalytic:prompted:deniedReason:] : 248 -> 264
~ +[ATTrackingManager _TCCServer] : 68 -> 84
~ +[ATTrackingManager _performTCCPreflightRequest] : 492 -> 504
~ +[ATTrackingManager _performTCCAccessRequest:] : 436 -> 444
~ +[ATTrackingManager _trackingAuthorizationStatus] : 208 -> 212
~ ___43+[ATTrackingManager applicationStateActive]_block_invoke : 200 -> 216
~ +[ATTrackingManager isApplicationExtension] : 96 -> 104

```
