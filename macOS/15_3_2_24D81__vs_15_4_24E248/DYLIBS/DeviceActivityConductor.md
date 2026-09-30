## DeviceActivityConductor

> `/System/Library/PrivateFrameworks/DeviceActivityConductor.framework/Versions/A/DeviceActivityConductor`

```diff

-36.0.0.0.0
-  __TEXT.__text: 0xc060
+36.40.1.0.0
+  __TEXT.__text: 0xc00c
   __TEXT.__auth_stubs: 0x2c0
-  __TEXT.__objc_methlist: 0x774
+  __TEXT.__objc_methlist: 0x914
   __TEXT.__const: 0xc8
   __TEXT.__cstring: 0x570
-  __TEXT.__gcc_except_tab: 0x55c
+  __TEXT.__gcc_except_tab: 0x558
   __TEXT.__oslogstring: 0x94a
   __TEXT.__unwind_info: 0x428
   __TEXT.__objc_classname: 0x167

   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x418
+  __DATA_CONST.__objc_selrefs: 0x4a0
   __DATA_CONST.__objc_superrefs: 0x60
   __AUTH_CONST.__auth_got: 0x170
   __AUTH_CONST.__const: 0x410
   __AUTH_CONST.__cfstring: 0x480
-  __AUTH_CONST.__objc_const: 0x1708
+  __AUTH_CONST.__objc_const: 0x1430
   __AUTH.__objc_data: 0x3c0
   __DATA.__objc_ivar: 0xe0
   __DATA.__data: 0x240

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 71C242B7-AD4B-366D-AF4F-9CAC11B1A4AD
+  UUID: 8F3B650B-462E-3EE1-8305-3E73302CA1BD
   Functions: 252
   Symbols:   676
   CStrings:  437
Functions:
~ -[DACActivityAssertion _initWithActivity:requester:changeMarker:relinquishHandler:] : 328 -> 316
~ -[DACActivityAssertion setState:] : 392 -> 396
~ -[DACActivityListEntry isEqual:] : 524 -> 528
~ -[DACActivityList initWithCoder:] : 804 -> 792
~ -[DACActivityList isEqual:] : 332 -> 324
~ -[DACActivityList _stateOfActivity:] : 308 -> 304
~ ___43-[DACActivityList changeMarkerForActivity:]_block_invoke : 176 -> 172
~ ___29-[DACActivityList enumerate:]_block_invoke : 540 -> 508
~ -[DACActivityList _entryOfActivity:] : 148 -> 144
~ -[DACActivityList _addActivityEntry:] : 536 -> 532
~ -[DACActivityList listWithMerge:] : 400 -> 396
~ ___53-[DACActivityList changesFromList:includingMetadata:]_block_invoke_2 : 960 -> 980
~ ___53-[DACActivityList changesFromList:includingMetadata:]_block_invoke_3 : 1760 -> 1764
~ ___47-[DACRoleManager requestSpeakerGroupLeaderRole]_block_invoke : 436 -> 424
~ ___46-[DACLifecycleManager initWithDelegate:queue:]_block_invoke : 60 -> 72
~ -[DACLifecycleManager _remoteInterfaceWithErrorHandler:] : 132 -> 124
~ ___42-[DACLifecycleManager unregisterActivity:]_block_invoke : 280 -> 276
~ -[DACLifecycleManager enumerateLifecycleInfo:] : 368 -> 360
~ ___61-[DACLifecycleManager requestActivationOfActivity:requester:]_block_invoke : 1396 -> 1392
~ ___63-[DACLifecycleManager requestDeactivationOfActivity:requester:]_block_invoke : 676 -> 672
~ ___55-[DACLifecycleManager _assertionForActivity:requester:]_block_invoke_2 : 980 -> 976

```
