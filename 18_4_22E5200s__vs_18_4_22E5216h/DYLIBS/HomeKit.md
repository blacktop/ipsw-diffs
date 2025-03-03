## HomeKit

> `/System/Library/Frameworks/HomeKit.framework/HomeKit`

```diff

-1277.0.0.1.2
-  __TEXT.__text: 0x2b4364
+1278.5.8.2.0
+  __TEXT.__text: 0x2b4790
   __TEXT.__auth_stubs: 0x1a10
-  __TEXT.__objc_methlist: 0x24b94
+  __TEXT.__objc_methlist: 0x24aec
   __TEXT.__const: 0x175c
   __TEXT.__dlopen_cstrs: 0x3a1
-  __TEXT.__cstring: 0x28d3e
+  __TEXT.__cstring: 0x28c36
   __TEXT.__swift5_typeref: 0x8fe
   __TEXT.__constg_swiftt: 0x7f8
   __TEXT.__swift5_reflstr: 0x321

   __TEXT.__swift5_types: 0x88
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x18
-  __TEXT.__oslogstring: 0x28de9
+  __TEXT.__oslogstring: 0x292bc
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__gcc_except_tab: 0x6c30
+  __TEXT.__gcc_except_tab: 0x6ca8
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x9a30
+  __TEXT.__unwind_info: 0x9a10
   __TEXT.__eh_frame: 0xbd8
-  __TEXT.__objc_classname: 0x4e42
-  __TEXT.__objc_methname: 0x464fc
-  __TEXT.__objc_methtype: 0x8496
-  __TEXT.__objc_stubs: 0x24e80
-  __DATA_CONST.__got: 0x17e0
-  __DATA_CONST.__const: 0x75b8
-  __DATA_CONST.__objc_classlist: 0x11e0
+  __TEXT.__objc_classname: 0x4e2c
+  __TEXT.__objc_methname: 0x4647a
+  __TEXT.__objc_methtype: 0x8486
+  __TEXT.__objc_stubs: 0x24e60
+  __DATA_CONST.__got: 0x17d8
+  __DATA_CONST.__const: 0x75c0
+  __DATA_CONST.__objc_classlist: 0x11d8
   __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x488
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xccf0
+  __DATA_CONST.__objc_selrefs: 0xcce0
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0xef8
+  __DATA_CONST.__objc_superrefs: 0xef0
   __DATA_CONST.__objc_arraydata: 0x1358
   __AUTH_CONST.__auth_got: 0xd18
   __AUTH_CONST.__auth_ptr: 0x2e0
-  __AUTH_CONST.__const: 0x27a8
-  __AUTH_CONST.__cfstring: 0x261c0
-  __AUTH_CONST.__objc_const: 0x41b30
+  __AUTH_CONST.__const: 0x2788
+  __AUTH_CONST.__cfstring: 0x260a0
+  __AUTH_CONST.__objc_const: 0x419e8
   __AUTH_CONST.__objc_intobj: 0x7b0
   __AUTH_CONST.__objc_dictobj: 0x848
   __AUTH_CONST.__objc_arrayobj: 0x558
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH.__objc_data: 0x82a8
+  __AUTH.__objc_data: 0x8258
   __AUTH.__data: 0x580
-  __DATA.__objc_ivar: 0x245c
+  __DATA.__objc_ivar: 0x2458
   __DATA.__data: 0x3bb8
-  __DATA.__bss: 0x2770
+  __DATA.__bss: 0x2760
   __DATA.__common: 0x59
   __DATA_DIRTY.__objc_data: 0x31b0
   __DATA_DIRTY.__data: 0x10

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 13996
-  Symbols:   17125
-  CStrings:  20117
+  Functions: 13983
+  Symbols:   17111
+  CStrings:  20113
 
Symbols:
+ _HMCameraStreamAudioUplinkTokenMessageKey
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _OBJC_CLASS_$_HMWeeklyScheduleEntry
- _OBJC_METACLASS_$_HMWeeklyScheduleEntry
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
CStrings:
+ "%{public}@Failed to unpack audio uplink token: %@"
+ "%{public}@Home reference was nil in fetchAccessCodeConstraintsFromAccessories for accessories: %@"
+ "%{public}@Home reference was nil in fetchAccessCodesFromAccessories for accessories: %@"
+ "%{public}@Home reference was nil in fetchCachedAccessoryAccessCodesWithCompletion"
+ "%{public}@Home reference was nil in fetchHomeAccessCodesWithCompletion"
+ "%{public}@Home reference was nil in generateAccessCodeForUser for user: %@"
+ "%{public}@Home reference was nil in handleDidAddAccessoryAccessCodesMessage for accessoryAccessCodeValues: %@"
+ "%{public}@Home reference was nil in handleDidAddHomeAccessCodesMessage for homeAccessCodeValues: %@"
+ "%{public}@Home reference was nil in handleDidRemoveAccessoryAccessCodesMessage for accessoryAccessCodeValues: %@"
+ "%{public}@Home reference was nil in handleDidRemoveHomeAccessCodesMessage for homeAccessCodeValues: %@"
+ "%{public}@Home reference was nil in handleDidUpdateAccessoryAccessCodesMessage for accessoryAccessCodeValues: %@"
+ "%{public}@Home reference was nil in handleDidUpdateHomeAccessCodesMessage for homeAccessCodeValues: %@"
+ "%{public}@Home reference was nil in removeSimpleLabelAccessCode"
+ "%{public}@Home reference was nil in resetAccessoryAccessCodesWithValueMatchingHomeAccessCode for access code: %@"
+ "%{public}@Home reference was nil in setAccessCode for access code: %@"
+ "%{public}@Home reference was nil in submitAccessCodeModificationRequests for modification requests: %@"
+ "@72@0:8@16@24d32@40Q48q56q64"
+ "HMCameraStreamAudioUplinkTokenMessageKey"
+ "Tq,R,V_audioUplinkToken"
+ "_audioUplinkToken"
+ "audioUplinkToken"
+ "com.apple.accountsd"
+ "initWithProfileUniqueIdentifier:slotIdentifier:aspectRatio:sessionID:audioStreamSetting:audioDownlinkToken:audioUplinkToken:"
- "%{public}@Could not initialize due to nil object after decoding start:%@, end:%@"
- "%{public}@Not yet implemented"
- "%{public}@Unable to determine the end date components"
- "%{public}@Unable to determine the start date components"
- "-[HMHomeManager fetchCachedWiFiInfosForHomesWithCompletionHandler:]"
- "-[HMHomeManager fetchWiFiInfosForHomesWithTimeout:partialResultHandler:completion:]"
- "@64@0:8@16@24d32@40Q48q56"
- "HMScheduleEntryEndCodingKey"
- "HMScheduleEntryStartCodingKey"
- "HMWeeklyScheduleEntry"
- "T@\"NSDateComponents\",R,N,V_end"
- "T@\"NSDateComponents\",R,N,V_start"
- "_end"
- "accountsd"
- "endHour"
- "endMinute"
- "endWeekday"
- "fetchCachedWiFiInfosForHomesWithCompletionHandler:"
- "fetchWiFiInfosForHomesWithTimeout:partialResultHandler:completion:"
- "initWithProfileUniqueIdentifier:slotIdentifier:aspectRatio:sessionID:audioStreamSetting:audioDownlinkToken:"
- "initWithStart:end:"
- "partialResultHandler"
- "startHour"
- "startMinute"
- "startWeekday"
- "v40@0:8d16@?24@?32"
- "weeklyScheduleEntry"

```
