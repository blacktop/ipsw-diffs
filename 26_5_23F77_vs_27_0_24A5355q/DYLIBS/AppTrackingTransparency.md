## AppTrackingTransparency

> `/System/Library/Frameworks/AppTrackingTransparency.framework/AppTrackingTransparency`

```diff

 106.2.2.0.0
-  __TEXT.__text: 0x22dc
-  __TEXT.__auth_stubs: 0x2f0
+  __TEXT.__text: 0x1f4c
   __TEXT.__objc_methlist: 0x144
   __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x1b0
+  __TEXT.__gcc_except_tab: 0xbc
   __TEXT.__cstring: 0x1aa
   __TEXT.__oslogstring: 0x6f6
-  __TEXT.__unwind_info: 0x108
-  __TEXT.__objc_classname: 0x4c
-  __TEXT.__objc_methname: 0x496
-  __TEXT.__objc_methtype: 0x86
-  __TEXT.__objc_stubs: 0x4a0
-  __DATA_CONST.__got: 0x70
+  __TEXT.__unwind_info: 0x100
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x160
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x188
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x188
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x188
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0x60
   __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1A24C2F7-F543-378D-A03A-0792EE539902
+  UUID: B98BAC02-65D0-3A29-B244-7ABF2177EE81
   Functions: 40
-  Symbols:   240
-  CStrings:  120
+  Symbols:   241
+  CStrings:  52
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
+ _objc_storeStrong
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_autoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
Functions:
~ +[ATTrackingEnforcementManager setLastBagLookup:] : 64 -> 16
~ +[ATTrackingEnforcementManager lastBagLookup] : 60 -> 12
~ +[ATTrackingEnforcementManager _refreshEnforcementStatusInBackground] : 624 -> 632
~ ___69+[ATTrackingEnforcementManager _refreshEnforcementStatusInBackground]_block_invoke_2 : 196 -> 152
~ ___69+[ATTrackingEnforcementManager _refreshEnforcementStatusInBackground]_block_invoke.4 : 196 -> 152
~ ___69+[ATTrackingEnforcementManager _refreshEnforcementStatusInBackground]_block_invoke.7 : 364 -> 308
~ +[ATTrackingEnforcementManager shouldEnforceTrackingWithReasonCode:] : 436 -> 376
~ +[ATTrackingManager _restrictionProfileInstalled] : 80 -> 76
~ +[ATTrackingManager _userAllowedToChangeSettings] : 132 -> 124
~ +[ATTrackingManager _isCrossAppTrackingAllowed] : 84 -> 80
~ +[ATTrackingManager _sendRequestTrackingAnalytic:prompted:deniedReason:] : 264 -> 248
~ +[ATTrackingManager _sendTrackingStatusAnalytic:prompted:deniedReason:] : 264 -> 248
~ +[ATTrackingManager _TCCServer] : 84 -> 68
~ +[ATTrackingManager _performTCCPreflightRequest] : 504 -> 440
~ ___48+[ATTrackingManager _performTCCPreflightRequest]_block_invoke : 236 -> 192
~ +[ATTrackingManager _performTCCAccessRequest:] : 444 -> 392
~ ___46+[ATTrackingManager _performTCCAccessRequest:]_block_invoke : 260 -> 216
~ +[ATTrackingManager _trackingAuthorizationStatus] : 212 -> 208
~ +[ATTrackingManager trackingAuthorizationStatus] : 780 -> 732
~ ___43+[ATTrackingManager applicationStateActive]_block_invoke : 216 -> 200
~ +[ATTrackingManager isApplicationExtension] : 104 -> 96
~ +[ATTrackingManager requestTrackingAuthorizationWithCompletionHandler:] : 1904 -> 1716
~ ___71+[ATTrackingManager requestTrackingAuthorizationWithCompletionHandler:]_block_invoke : 548 -> 504
~ ___69+[ATTrackingEnforcementManager _refreshEnforcementStatusInBackground]_block_invoke.5.cold.1 : 216 -> 172
CStrings:
- "@16@0:8"
- "ATEnforcementServiceProtocol"
- "ATTrackingEnforcementManager"
- "ATTrackingManager"
- "B16@0:8"
- "B24@0:8^q16"
- "Q16@0:8"
- "T@\"NSDate\",&,N"
- "TB,N"
- "TQ,R,N"
- "Tq,N"
- "_TCCServer"
- "_applicationHasDisqualifyingEntitlement"
- "_isCrossAppTrackingAllowed"
- "_performTCCAccessRequest:"
- "_performTCCPreflightRequest"
- "_refreshEnforcementStatusInBackground"
- "_restrictionProfileInstalled"
- "_sendRequestTrackingAnalytic:prompted:deniedReason:"
- "_sendTrackingStatusAnalytic:prompted:deniedReason:"
- "_trackingAuthorizationStatus"
- "_userAllowedToChangeSettings"
- "appTrackingEnforcement:"
- "applicationStateActive"
- "bundlePath"
- "date"
- "dictionary"
- "effectiveBoolValueForSetting:"
- "hasSuffix:"
- "initWithServiceName:"
- "interfaceWithProtocol:"
- "invalidate"
- "isApplicationExtension"
- "isBoolSettingLockedDownByRestrictions:"
- "isDefaultReturned"
- "isSharedIPad"
- "lastBagLookup"
- "lastEnforcement"
- "lastReasonCode"
- "localizedDescription"
- "mainBundle"
- "numberWithBool:"
- "numberWithUnsignedInteger:"
- "performSelector:"
- "q16@0:8"
- "remoteObjectProxyWithErrorHandler:"
- "requestTrackingAuthorizationWithCompletionHandler:"
- "resume"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsDefaultReturned:"
- "setLastBagLookup:"
- "setLastEnforcement:"
- "setLastReasonCode:"
- "setRemoteObjectInterface:"
- "setValue:forKey:"
- "sharedConnection"
- "sharedManager"
- "shouldEnforceTrackingWithReasonCode:"
- "timeIntervalSinceDate:"
- "trackingAuthorizationStatus"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?BqB>16"
- "v24@0:8q16"
- "v36@0:8Q16B24Q28"

```
