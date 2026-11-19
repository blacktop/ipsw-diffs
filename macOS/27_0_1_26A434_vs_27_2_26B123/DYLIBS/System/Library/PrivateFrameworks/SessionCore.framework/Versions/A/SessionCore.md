## SessionCore

> `/System/Library/PrivateFrameworks/SessionCore.framework/Versions/A/SessionCore`

```diff

-312.0.0.0.0
-  __TEXT.__text: 0x14f604
-  __TEXT.__objc_methlist: 0xd44
-  __TEXT.__const: 0x5412
-  __TEXT.__swift5_typeref: 0x2d1b
-  __TEXT.__swift5_fieldmd: 0x2c64
-  __TEXT.__constg_swiftt: 0x4574
-  __TEXT.__swift5_reflstr: 0x2c77
+313.2.9.100.0
+  __TEXT.__text: 0x150cb8
+  __TEXT.__objc_methlist: 0xd74
+  __TEXT.__const: 0x54b2
+  __TEXT.__swift5_typeref: 0x2d8b
+  __TEXT.__swift5_fieldmd: 0x2c30
+  __TEXT.__constg_swiftt: 0x4554
+  __TEXT.__swift5_reflstr: 0x2ca7
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__cstring: 0x35b2
-  __TEXT.__oslogstring: 0x7834
-  __TEXT.__swift5_capture: 0x1490
+  __TEXT.__cstring: 0x3662
+  __TEXT.__oslogstring: 0x7a64
+  __TEXT.__swift5_capture: 0x14a0
   __TEXT.__swift5_protos: 0xc8
-  __TEXT.__swift5_proto: 0x35c
-  __TEXT.__swift5_types: 0x290
+  __TEXT.__swift5_proto: 0x360
+  __TEXT.__swift5_types: 0x28c
   __TEXT.__swift5_assocty: 0xa8
   __TEXT.__swift5_mpenum: 0x20
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__unwind_info: 0x2438
-  __TEXT.__eh_frame: 0x3658
+  __TEXT.__unwind_info: 0x24c0
+  __TEXT.__eh_frame: 0x38a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7a8
+  __DATA_CONST.__objc_selrefs: 0x7c0
   __DATA_CONST.__objc_protorefs: 0x120
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x5fd8
-  __AUTH_CONST.__objc_const: 0xc390
-  __AUTH_CONST.__auth_got: 0x1bd8
-  __AUTH_CONST.__auth_ptr: 0xcf0
+  __AUTH_CONST.__const: 0x6038
+  __AUTH_CONST.__objc_const: 0xc3a0
+  __AUTH_CONST.__auth_got: 0x1c48
+  __AUTH_CONST.__auth_ptr: 0xd00
   __AUTH.__objc_data: 0x740
   __AUTH.__data: 0x2e8
-  __DATA.__data: 0x1790
+  __DATA.__data: 0x1800
+  __DATA.__bss: 0x2100
   __DATA.__common: 0x68
-  __DATA.__bss: 0x2080
   __DATA_DIRTY.__objc_data: 0x1988
-  __DATA_DIRTY.__data: 0x7070
+  __DATA_DIRTY.__data: 0x6fa8
   __DATA_DIRTY.__bss: 0xe80
   __DATA_DIRTY.__common: 0x269
   - /System/Library/Frameworks/ActivityKit.framework/Versions/A/ActivityKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3491
-  Symbols:   1804
-  CStrings:  835
+  Functions: 3521
+  Symbols:   1810
+  CStrings:  847
 
Symbols:
+ __swift_closure_destructor.38Tm
+ _associated conformance 11SessionCore20AuthorizationManagerC0cD5ErrorOSHAASQ
+ _objc_msgSend$localizedInfoDictionary
+ _symbolic SDy___________pG 18ReplicatorServices0A6DeviceV0C4TypeO 11SessionCore20ReplicationFilteringP
+ _symbolic Say_____G 11ActivityKit04LiveA17ApplicationRecordV
+ _symbolic _____ 11SessionCore20AuthorizationManagerC0cD5ErrorO
+ _symbolic _____3key_______p5valuet 18ReplicatorServices0A6DeviceV0C4TypeO 11SessionCore20ReplicationFilteringP
+ _symbolic _____SgXw 11SessionCore21ReplicatorParticipantC
+ _symbolic ____________pt 18ReplicatorServices0A6DeviceV0C4TypeO 11SessionCore20ReplicationFilteringP
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 11ActivityKit04LiveD17ApplicationRecordV
+ _symbolic _____y____________ptG s23_ContiguousArrayStorageC 18ReplicatorServices0D6DeviceV0F4TypeO 11SessionCore20ReplicationFilteringP
+ _symbolic _____y___________pG s18_DictionaryStorageC 18ReplicatorServices0C6DeviceV0E4TypeO 11SessionCore20ReplicationFilteringP
- __swift_closure_destructor.39Tm
- _associated conformance 11SessionCore13ActivityStateV0D0OSHAASQ
- _symbolic _____ 11SessionCore13ActivityStateV
- _symbolic _____ 11SessionCore13ActivityStateV0D0O
- _symbolic _____Sg 10Foundation4DataV
- _symbolic ______pSg 11SessionCore20ReplicationFilteringP
CStrings:
+ "Activity request blocked by alert scene target without user consent: %{public}s"
+ "Activity request blocked by content source without user consent: %{public}s"
+ "Activity request blocked by scene target without user consent: %{public}s"
+ "Alert scene target is restricted: %{public}s"
+ "Cannot replicate activity to a device that does not exist: %{public}s: relationshipSchedule %{public}s"
+ "Error finding the app record for bundle identifier: %{private}s"
+ "Failed to encode live activity application records: %@"
+ "Live Activities are not supported for this type of request: %{public}s"
+ "NSLiveActivityDisplayName"
+ "New bundle ID %{public}s does not support Live Activities"
+ "Push cannot assert user preconsent: %{public}s"
+ "Replacing %{public}s with %{public}s"
+ "Replication of activity %{public}s is unfiltered for relationshipSchedule %{public}s"
+ "Requester is entitled to create activities: %{public}s"
+ "Requester is foreground: %{public}s"
+ "Requester is not entitled to assert user preconsent: %{public}d"
+ "Requester is not foreground: %{public}s"
+ "Requester is not targeted by an activity request assertion: %{public}s"
+ "Requester is targeted by an activity request assertion: %{public}s"
+ "Scene target is restricted: %{public}s"
+ "The requesting process is not entitled to make this request"
+ "The requesting process is not entitled to replace bundle IDs"
+ "The requesting process is not entitled to request live activity records"
+ "com.apple.private.activitykit.bundleIDReplacer"
+ "com.apple.private.activitykit.userPreconsentAsserter"
+ "localizedAppNameBundleID"
- "Activity request blocked by alert scene target without user consent: %{private}s"
- "Activity request blocked by content source without user consent: %{private}s"
- "Activity request blocked by scene target without user consent: %{private}s"
- "Alert scene target is restricted: %{private}s"
- "Error finding the app record for bundle identifier: %{private}s: %s"
- "Live Activities are not supported for this type of request: %{private}s"
- "No asset provider bundle ID provided"
- "Requester is entitled to create activities: %{private}s"
- "Requester is foreground: %{private}s"
- "Requester is not foreground: %{private}s"
- "Requester is not targeted by an activity request assertion: %{private}s"
- "Requester is targeted by an activity request assertion: %{private}s"
- "Scene target is restricted: %{private}s"
- "The requesting process is not entitled to set activities authorization"
```
