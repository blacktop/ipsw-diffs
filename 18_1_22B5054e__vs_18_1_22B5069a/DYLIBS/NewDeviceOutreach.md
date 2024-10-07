## NewDeviceOutreach

> `/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach`

```diff

-425.2.0.0.0
-  __TEXT.__text: 0x169bc
+425.3.0.0.0
+  __TEXT.__text: 0x176cc
   __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0x1398
+  __TEXT.__objc_methlist: 0x1420
   __TEXT.__const: 0x108
-  __TEXT.__cstring: 0x1f38
-  __TEXT.__oslogstring: 0x1670
+  __TEXT.__cstring: 0x2115
+  __TEXT.__oslogstring: 0x176c
   __TEXT.__gcc_except_tab: 0x6ac
   __TEXT.__ustring: 0x30
   __TEXT.__dlopen_cstrs: 0x41
-  __TEXT.__unwind_info: 0x4d8
+  __TEXT.__unwind_info: 0x500
   __TEXT.__objc_classname: 0x1b9
-  __TEXT.__objc_methname: 0x5146
-  __TEXT.__objc_methtype: 0x7bf
-  __TEXT.__objc_stubs: 0x36a0
-  __DATA_CONST.__got: 0x2c8
-  __DATA_CONST.__const: 0x7e8
+  __TEXT.__objc_methname: 0x53a1
+  __TEXT.__objc_methtype: 0x7d9
+  __TEXT.__objc_stubs: 0x38a0
+  __DATA_CONST.__got: 0x2d0
+  __DATA_CONST.__const: 0x7c0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1168
+  __DATA_CONST.__objc_selrefs: 0x11f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
-  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x2e0
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x20c0
-  __AUTH_CONST.__objc_const: 0x3730
-  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__cfstring: 0x21a0
+  __AUTH_CONST.__objc_const: 0x3780
   __AUTH_CONST.__objc_intobj: 0xd8
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x1d4
+  __DATA.__objc_ivar: 0x1d8
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x2d0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 559
-  Symbols:   801
-  CStrings:  1418
+  Functions: 576
+  Symbols:   818
+  CStrings:  1456
 
Symbols:
+ _OBJC_CLASS_$_NSPredicate
CStrings:
+ "%!@(MISSING) :: (%!@(MISSING)) :: (%!@(MISSING)) :: %!@(MISSING) - %!@(MISSING) :: (%!@(MISSING)) :: (isActiveWatch:%!d(MISSING)) :: %!d(MISSING)"
+ "%!@(MISSING)%!@(MISSING)"
+ "%!{(MISSING)public}s Cannot create follow up item for SN:%!@(MISSING) WI:%!@(MISSING)"
+ "%!{(MISSING)public}s DeviceType:%!@(MISSING) bundleIDs%!@(MISSING)"
+ "%!{(MISSING)public}s Error. Invalid serial: @{private}%!@(MISSING)"
+ "%!{(MISSING)public}s Failed to get pending follow ups. Err:%!@(MISSING)"
+ "%!{(MISSING)public}s Unsupported device type"
+ "%!{(MISSING)public}s bundleIDs:%!@(MISSING) for deviceInfo:%!@(MISSING)"
+ "%!{(MISSING)public}s: Cannot generate follow up with prefix:%!@(MISSING), SN:%!@(MISSING), target bundle id:%!@(MISSING)"
+ "%!{(MISSING)public}s: Device NOT eligible. Warranty:%!@(MISSING) acOfferDisplay:%!@(MISSING) eligibleUntil:%!@(MISSING)"
+ "%!{(MISSING)public}s: showRowBadge:%!d(MISSING) showNotification:%!d(MISSING)"
+ "+[NDOFollowUp followUpTargetBundleIDsForDevice:]"
+ "+[NDOFollowUp uniqueIdentfierForSerialNumber:bundleId:]"
+ "-[NDOFollowUp _clearFollowUpForSerialNumber:]"
+ "-[NDOFollowUp _clearFollowUpsForDeviceSerialNumbers:]"
+ "-[NDOFollowUp _pendingFollowUpItemsForSerialNumber:]"
+ "-[NDOFollowUp followUpItemsForDeviceInfo:]"
+ "-[NDOFollowUp refreshFollowupWithDeviceInfos:clearUntrackedDeviceFollowups:andForcePostFollowup:]"
+ ".%!@(MISSING).%!@(MISSING)"
+ "@60@0:8@16@24@32B40@44@52"
+ "@{public}s: no device serial. Cannot generate follow up IDs"
+ "@{public}s: no serial. Cannot generate follow up IDs"
+ "B24@?0@\"FLFollowUpItem\"8@\"NSDictionary\"16"
+ "Clear follow-ups for serials:[%!@(MISSING)] status:%!@(MISSING)"
+ "Clearing follow up for serial numbers: %!{(MISSING)private}@"
+ "Device needs follow up update. Dismiss and repost for %!@(MISSING)"
+ "FollowupEligibilityEventId"
+ "No longer tracking serials: %!{(MISSING)private}@"
+ "Posted follow-up: %!@(MISSING)"
+ "TB,V_isActiveWatch"
+ "WATCH_SETTINGS_FOLLOWUP"
+ "_FOLLOWUP"
+ "_clearFollowUpsForDeviceSerialNumbers:"
+ "_isActiveWatch"
+ "_pendingFollowUpItemsForSerialNumber:"
+ "allPossibleFollowUpTargetBundleIdentifiers"
+ "com.applecare.followup.saleflowsource"
+ "filteredArrayUsingPredicate:"
+ "followUpItemsForDeviceInfo:"
+ "followUpSaleFlowSourceForBundleId:device:"
+ "followUpTargetBundleIDsForDevice:"
+ "isActiveWatch"
+ "numberWithUnsignedInteger:"
+ "possibleUniqueIdentifiersForSerialNumber:"
+ "predicateWithBlock:"
+ "setIsActiveWatch:"
+ "setWithObject:"
+ "targetBundleIdentifier"
+ "uniqueFollowUpIdentifiersForDevice:"
+ "uniqueIdentfierForSerialNumber:bundleId:"
+ "watchDeviceWithName:serialNumber:activationDate:isActive:productID:productName:"
- "%!@(MISSING) :: (%!@(MISSING)) :: (%!@(MISSING)) :: %!@(MISSING) - %!@(MISSING) :: (%!@(MISSING)) :: %!d(MISSING)"
- "%!{(MISSING)public}s: Device NOT eligible. Remove the followup for %!{(MISSING)private}@"
- "%!{(MISSING)public}s: Device no longer eligible. Remove the followup for %!{(MISSING)private}@"
- "%!{(MISSING)public}s: No warranty downloaded for device. Remove the followup for %!{(MISSING)private}@"
- "%!{(MISSING)public}s: shouldShowNotification: %!d(MISSING)"
- "%!{(MISSING)public}s: shouldShowRowBadge: %!d(MISSING)"
- "-[NDOFollowUp refreshFollowupWithDeviceInfos:clearUntrackedDeviceFollowups:andForcePostFollowup:]_block_invoke"
- "Clearing legacy followup, no legacy warranty was found.."
- "Error clearing legacy follow-up: %!@(MISSING)"
- "Error posting migrated follow-up: %!@(MISSING)"
- "Migrating legacy followup.."
- "No longer tracking device %!{(MISSING)private}@, clearing"
- "Reposted follow-up: %!@(MISSING)"
- "Updated follow-up: %!@(MISSING)"

```
