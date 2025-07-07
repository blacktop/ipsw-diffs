## safetycheckd

> `/usr/libexec/safetycheckd`

```diff

-565.0.1.0.0
-  __TEXT.__text: 0x2550
-  __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_stubs: 0xa40
-  __TEXT.__objc_methlist: 0x4c8
-  __TEXT.__const: 0x28
-  __TEXT.__objc_methname: 0xa2f
-  __TEXT.__oslogstring: 0x129
-  __TEXT.__objc_classname: 0xea
-  __TEXT.__objc_methtype: 0x335
-  __TEXT.__cstring: 0x1db
-  __TEXT.__gcc_except_tab: 0x10
-  __TEXT.__unwind_info: 0x138
-  __DATA_CONST.__auth_got: 0x180
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x120
-  __DATA_CONST.__cfstring: 0x180
+574.0.0.0.0
+  __TEXT.__text: 0x8920
+  __TEXT.__auth_stubs: 0x4d0
+  __TEXT.__objc_stubs: 0xf20
+  __TEXT.__objc_methlist: 0x508
+  __TEXT.__const: 0x50
+  __TEXT.__objc_methname: 0xe90
+  __TEXT.__oslogstring: 0x8f6
+  __TEXT.__objc_classname: 0xeb
+  __TEXT.__objc_methtype: 0x373
+  __TEXT.__cstring: 0x326
+  __TEXT.__gcc_except_tab: 0x644
+  __TEXT.__unwind_info: 0x1c0
+  __DATA_CONST.__auth_got: 0x278
+  __DATA_CONST.__got: 0x168
+  __DATA_CONST.__const: 0x2b0
+  __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA.__objc_const: 0x860
-  __DATA.__objc_selrefs: 0x360
-  __DATA.__objc_ivar: 0x30
+  __DATA.__objc_const: 0x8c0
+  __DATA.__objc_selrefs: 0x498
+  __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x248
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation
   - /System/Library/PrivateFrameworks/SCSharingReminders.framework/SCSharingReminders
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BCD6BF7B-209C-3281-83A9-A68B9E54480C
-  Functions: 76
-  Symbols:   76
-  CStrings:  228
+  UUID: 6250F907-729E-383C-832D-48B2EF8484A7
+  Functions: 106
+  Symbols:   131
+  CStrings:  354
 
Symbols:
+ _AnalyticsSendEventLazy
+ _DSErrorDomain
+ _DSSourceNameActivity
+ _DSSourceNameCalendars
+ _DSSourceNameFindMy
+ _DSSourceNameHealthSharing
+ _DSSourceNameHomeSharing
+ _DSSourceNameItemSharing
+ _DSSourceNameMaps
+ _DSSourceNameNotes
+ _DSSourceNamePassKeys
+ _DSSourceNamePhotos
+ _DSSourceNameZelkova
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_CTDataUsagePolicies
+ _OBJC_CLASS_$_CoreTelephonyClient
+ _OBJC_CLASS_$_DSError
+ _OBJC_CLASS_$_DSRestrictionStore
+ _OBJC_CLASS_$_DSSourceDescriptor
+ _OBJC_CLASS_$_DSUtilities
+ _OBJC_CLASS_$_DSXPCParticipant
+ _OBJC_CLASS_$_DSXPCSharedResource
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSSet
+ _OBJC_EHTYPE_$_NSException
+ ___NSDictionary0__struct
+ __dispatch_main_q
+ __os_log_fault_impl
+ __os_signpost_emit_with_name_impl
+ _clock_gettime_nsec_np
+ _dispatch_apply
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _objc_begin_catch
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_end_catch
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_opt_class
+ _objc_opt_respondsToSelector
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x9
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x27
+ _os_signpost_enabled
+ _os_signpost_id_generate
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- _OBJC_CLASS_$_DSSharingPermissions
- _OBJC_CLASS_$_NSDate
- _objc_retain_x4
CStrings:
+ " enableTelemetry=YES "
+ "\"All sources have required data usage policies\""
+ "\"Failed to get data usage policies for %{public}@ because %{public}@\""
+ "\"Got data usage policy for %{public}@: %{public}@\""
+ "\"Required policy %{public}@ for %{public}@ not met.\""
+ "@\"DSSourceRepository\""
+ "@\"NSDictionary\"8@?0"
+ "@\"NSMutableDictionary\""
+ "Asked to stop sharing %@ but couldn't retrieve a source with that name"
+ "B32@?0@\"<DSParticipation>\"8Q16^B24"
+ "Cannot reset %@ due to restrictions"
+ "Failed to fetch shared resources from %{public}@ because %{public}@"
+ "Failed to fetch shared resources from %{public}@ because exception %{public}@"
+ "Failed to find participant matching %@ in list %@"
+ "Failed to stop sharing on source %{public}@ for %{public}@ because %{public}@"
+ "Failed to stop sharing on source %{public}@ for %{public}@ because exception %{public}@"
+ "Failed to stop sharing on source %{public}@ for participants %{private}@ because %{public}@"
+ "Failed to stop sharing on source %{public}@ for participants %{private}@ because exception %{public}@"
+ "Fetching sharing permissions from %{public}@"
+ "Fetching sharing permissions from sources: %{public}@"
+ "Finished fetching sharing permissions from %{public}@ with %{private}@ resources (%{public}lu)"
+ "Signpost for unsupported source name %{public}@"
+ "StopSharingWithParticipants:completion: stopping sharing of %ld sources"
+ "Stopping sharing of %{private}@ from source %{public}@"
+ "Stopping sharing of participants %{private}@ from source %{public}@"
+ "Stopping sharing with %{public}@ complete"
+ "Stopping sharing with %{public}@ for participants complete"
+ "T@\"DSSourceRepository\",&,N,V_repo"
+ "T@\"NSMutableDictionary\",&,N,V_fetchStartTimesBySource"
+ "T@\"NSMutableDictionary\",&,N,V_participantsBySource"
+ "_dataUsageQueue"
+ "_fetchStartTimesBySource"
+ "_participantsBySource"
+ "_permissionsLock"
+ "_repo"
+ "allApps"
+ "allKeys"
+ "allValues"
+ "arrayWithArray:"
+ "bundleId"
+ "com.apple.DigitalSeparation"
+ "com.apple.DigitalSeparation.FinishedFetch"
+ "com.apple.Health"
+ "com.apple.safetycheckd.SCPermissionsService.dataUsageQueue"
+ "dataUsageBundleIdentifier"
+ "dictionaryWithCapacity:"
+ "dictionaryWithObjects:forKeys:count:"
+ "domain"
+ "ds_DataUsagePolicyWithPolicy:sourceName:"
+ "ds_errorFromIgnorableError:sourceName:"
+ "errorCode"
+ "errorDomain"
+ "errorWithCode:sourceName:"
+ "errorWithCode:sourceName:underlyingErrors:"
+ "fetch"
+ "fetch.Activity"
+ "fetch.Calendars"
+ "fetch.FindMy"
+ "fetch.Health"
+ "fetch.Home"
+ "fetch.ItemSharing"
+ "fetch.Maps"
+ "fetch.Notes"
+ "fetch.Passkeys"
+ "fetch.Photos"
+ "fetch.Zelkova"
+ "fetchCompletedForSource:"
+ "fetchPermissionsFromSources:includingErrors:queue:completion:"
+ "fetchSharedResourcesOnQueue:withCompletion:"
+ "fetchSharedResourcesWithCompletion:"
+ "fetchStartTimesBySource"
+ "fetchStartedForSource:"
+ "fetchedParticipants:forSource:"
+ "getLocalPolicies:completion:"
+ "green-tea"
+ "identity"
+ "indexOfObjectPassingTest:"
+ "initWithQueue:"
+ "initWithResource:"
+ "isEqualToString:"
+ "isSourceRestricted:"
+ "numberWithLong:"
+ "numberWithUnsignedLongLong:"
+ "objectAtIndexedSubscript:"
+ "participants"
+ "participantsBySource"
+ "permission"
+ "removeAllObjects"
+ "repo"
+ "role"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "setFetchStartTimesBySource:"
+ "setParticipantsBySource:"
+ "setRepo:"
+ "setValue:forKey:"
+ "setWithObject:"
+ "setWithObjects:"
+ "shouldAllowBundleIDWithNoPolicy:"
+ "sourceDescriptorForSource:"
+ "sourceName"
+ "stop"
+ "stop.Activity"
+ "stop.Calendars"
+ "stop.FindMy"
+ "stop.Health"
+ "stop.Home"
+ "stop.ItemSharing"
+ "stop.Maps"
+ "stop.Notes"
+ "stop.Passkeys"
+ "stop.Photos"
+ "stop.Zelkova"
+ "stopParticipants.Activity"
+ "stopParticipants.Calendars"
+ "stopParticipants.FindMy"
+ "stopParticipants.Health"
+ "stopParticipants.Home"
+ "stopParticipants.ItemSharing"
+ "stopParticipants.Maps"
+ "stopParticipants.Notes"
+ "stopParticipants.Passkeys"
+ "stopParticipants.Photos"
+ "stopParticipants.Zelkova"
+ "stopSharingWithParticipant:completion:"
+ "stopSharingWithParticipants:completion:"
+ "stopSharingWithSource: %@ originalParticipants: %@"
+ "userInfo"
+ "v16@?0Q8"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
+ "v24@?0@\"NSArray\"8@\"NSArray\"16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v24@?0@\"NSSet\"8@\"NSError\"16"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@16@24"
+ "v48@0:8@16@24@32@?40"
+ "verifyDataUsagePoliciesForSources:queue:completion:"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "\"SCPermissionsService finished permissions fetch in %.2fs and error %@.\""
- "None"
- "allPeople"
- "fetchPermissionsOnQueue:completion:"
- "sourceNames"
- "sourcesWithNames:"
- "stopAllSharingWithPerson:"
- "stopAllSharingWithPerson:completion:"
- "stopSharingSources:queue:completion:"
- "stopSharingSources:withPerson:completion:"
- "timeIntervalSinceReferenceDate"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v32@0:8@\"DSXPCSharingPerson\"16@?<v@?@\"NSError\">24"
- "v40@0:8@\"NSArray\"16@\"DSXPCSharingPerson\"24@?<v@?@\"NSError\">32"
- "xpcRepresentation"

```
