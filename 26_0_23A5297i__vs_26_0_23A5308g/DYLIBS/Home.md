## Home

> `/System/Library/PrivateFrameworks/Home.framework/Home`

```diff

-1093.1.0.0.0
-  __TEXT.__text: 0x37acb8
-  __TEXT.__auth_stubs: 0x35b0
-  __TEXT.__objc_methlist: 0x2ba34
-  __TEXT.__const: 0x37e0
+1097.1.2.1.2
+  __TEXT.__text: 0x37aee0
+  __TEXT.__auth_stubs: 0x35a0
+  __TEXT.__objc_methlist: 0x2ba9c
+  __TEXT.__const: 0x3800
   __TEXT.__dlopen_cstrs: 0x4b
-  __TEXT.__cstring: 0x35046
+  __TEXT.__cstring: 0x35112
   __TEXT.__swift5_typeref: 0x1fe0
   __TEXT.__swift5_reflstr: 0x8cb
   __TEXT.__swift5_assocty: 0x2a0

   __TEXT.__swift5_proto: 0x198
   __TEXT.__swift5_types: 0xf4
   __TEXT.__swift5_capture: 0xbcc
-  __TEXT.__oslogstring: 0x1c462
+  __TEXT.__oslogstring: 0x1c817
   __TEXT.__swift_as_entry: 0x1bc
   __TEXT.__swift_as_ret: 0x1e0
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__gcc_except_tab: 0x5aac
+  __TEXT.__gcc_except_tab: 0x5ac4
   __TEXT.__ustring: 0x8c
-  __TEXT.__unwind_info: 0xd838
-  __TEXT.__eh_frame: 0x6148
+  __TEXT.__unwind_info: 0xd840
+  __TEXT.__eh_frame: 0x6078
   __TEXT.__objc_classname: 0x6a06
-  __TEXT.__objc_methname: 0x59d7d
-  __TEXT.__objc_methtype: 0x75bc
-  __TEXT.__objc_stubs: 0x3a040
+  __TEXT.__objc_methname: 0x59f14
+  __TEXT.__objc_methtype: 0x75f5
+  __TEXT.__objc_stubs: 0x3a120
   __DATA_CONST.__got: 0x2f50
-  __DATA_CONST.__const: 0x11098
+  __DATA_CONST.__const: 0x110a0
   __DATA_CONST.__objc_classlist: 0x17c0
   __DATA_CONST.__objc_catlist: 0x410
   __DATA_CONST.__objc_protolist: 0x8a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x127b0
+  __DATA_CONST.__objc_selrefs: 0x12808
   __DATA_CONST.__objc_protorefs: 0x398
   __DATA_CONST.__objc_superrefs: 0x1310
   __DATA_CONST.__objc_arraydata: 0x3c0
-  __AUTH_CONST.__auth_got: 0x1ae8
-  __AUTH_CONST.__const: 0xded0
-  __AUTH_CONST.__cfstring: 0x26a20
-  __AUTH_CONST.__objc_const: 0x4a728
+  __AUTH_CONST.__auth_got: 0x1ae0
+  __AUTH_CONST.__const: 0xe018
+  __AUTH_CONST.__cfstring: 0x26a40
+  __AUTH_CONST.__objc_const: 0x4a7c8
   __AUTH_CONST.__objc_intobj: 0x2208
   __AUTH_CONST.__objc_doubleobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_floatobj: 0x50
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x9ef8
-  __AUTH.__data: 0xcc0
-  __DATA.__objc_ivar: 0x1528
-  __DATA.__data: 0x6df0
+  __AUTH.__objc_data: 0x9e80
+  __AUTH.__data: 0xca0
+  __DATA.__objc_ivar: 0x1534
+  __DATA.__data: 0x6dd0
   __DATA.__objc_stublist: 0x10
   __DATA.__bss: 0x2968
   __DATA.__common: 0x138
   __DATA_DIRTY.__objc_ivar: 0xce0
-  __DATA_DIRTY.__objc_data: 0x6178
-  __DATA_DIRTY.__data: 0x4b8
-  __DATA_DIRTY.__bss: 0x1918
+  __DATA_DIRTY.__objc_data: 0x61f0
+  __DATA_DIRTY.__data: 0x4f8
+  __DATA_DIRTY.__bss: 0x1928
   __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 59F01FA1-F17F-3C58-B63E-88359336EE7C
-  Functions: 20002
-  Symbols:   56335
-  CStrings:  28404
+  UUID: 4CB6A6D3-11F2-32C4-B35E-6E6DC79361A9
+  Functions: 20019
+  Symbols:   56381
+  CStrings:  28441
 
Symbols:
+ +[HFDemoModeAccessoryManager demoLiveStreamURLForCamera:]
+ +[HFDemoModeAccessoryManager demoSnapshotURLForCamera:]
+ +[HFDemoModeAccessoryManager demoURLWithCamera:fileName:extension:]
+ +[HMSymptomsHandler(HFAdditions) hf_nextSymptomAfterInternetOutageInSortedList:]
+ -[HFItemManager(HomeKitDelegates) accessory:didUpdateHH1EOLEnabled:]
+ -[HFStateRestorationSettings _reallySetSelectedHomeIdentifier:]
+ -[HFStateRestorationSettings cancelationToken]
+ -[HFStateRestorationSettings selectedHomeLock]
+ -[HFStateRestorationSettings serialQueue]
+ -[HFStateRestorationSettings setCancelationToken:]
+ -[HFStateRestorationSettings setSelectedHomeLock:]
+ -[HFStateRestorationSettings setSerialQueue:]
+ -[HMAccessory(HFMediaAdditions) hf_isHH1EOLEnabled]
+ GCC_except_table105
+ GCC_except_table185
+ _HFResultBannerSymptomKey
+ _OBJC_IVAR_$_HFStateRestorationSettings._cancelationToken
+ _OBJC_IVAR_$_HFStateRestorationSettings._selectedHomeLock
+ _OBJC_IVAR_$_HFStateRestorationSettings._serialQueue
+ ___45-[HFHomeKitDispatcher updateHomeSensingState]_block_invoke.639
+ ___48-[HFHomeKitDispatcher _setupHomeManagerObserver]_block_invoke.268
+ ___48-[HFHomeKitDispatcher _setupHomeManagerObserver]_block_invoke.273
+ ___48-[HFHomeKitDispatcher _setupHomeManagerObserver]_block_invoke_2.271
+ ___51-[HFSymptomStatusItem _subclass_updateWithOptions:]_block_invoke.13
+ ___51-[HFSymptomStatusItem _subclass_updateWithOptions:]_block_invoke_2.15
+ ___51-[HFSymptomStatusItem _subclass_updateWithOptions:]_block_invoke_3.19
+ ___51-[HFSymptomStatusItem _subclass_updateWithOptions:]_block_invoke_4.22
+ ___55-[HFHomeKitDispatcher _setupLocationSensingCoordinator]_block_invoke.610
+ ___63-[HFStateRestorationSettings _reallySetSelectedHomeIdentifier:]_block_invoke
+ ___80+[HMSymptomsHandler(HFAdditions) hf_nextSymptomAfterInternetOutageInSortedList:]_block_invoke
+ ___block_literal_global.210
+ ___block_literal_global.522
+ ___block_literal_global.551
+ ___block_literal_global.572
+ ___block_literal_global.581
+ ___block_literal_global.619
+ ___block_literal_global.632
+ ___swift_memcpy0_1
+ _objc_msgSend$_reallySetSelectedHomeIdentifier:
+ _objc_msgSend$cancelationToken
+ _objc_msgSend$demoLiveStreamURLForCamera:
+ _objc_msgSend$demoSnapshotURLForCamera:
+ _objc_msgSend$demoURLWithCamera:fileName:extension:
+ _objc_msgSend$hf_nextSymptomAfterInternetOutageInSortedList:
+ _objc_msgSend$isCanceled
+ _objc_msgSend$isHH1EOLEnabled
+ _objc_msgSend$serialQueue
+ _objc_msgSend$setCancelationToken:
- +[HFDemoModeAccessoryManager demoLiveStreamURLForCameraName:]
- +[HFDemoModeAccessoryManager demoSnapshotURLForCameraName:]
- +[HFDemoModeAccessoryManager demoURLWithCameraName:fileName:extension:]
- GCC_except_table100
- GCC_except_table104
- GCC_except_table152
- GCC_except_table180
- GCC_except_table183
- GCC_except_table186
- GCC_except_table87
- ___44-[HFHomeKitDispatcher _requestSelectedHome:]_block_invoke
- ___45-[HFHomeKitDispatcher updateHomeSensingState]_block_invoke.641
- ___48-[HFHomeKitDispatcher _setupHomeManagerObserver]_block_invoke.270
- ___48-[HFHomeKitDispatcher _setupHomeManagerObserver]_block_invoke.275
- ___48-[HFHomeKitDispatcher _setupHomeManagerObserver]_block_invoke_2.273
- ___51-[HFSymptomStatusItem _subclass_updateWithOptions:]_block_invoke_5
- ___55-[HFHomeKitDispatcher _setupLocationSensingCoordinator]_block_invoke.612
- ___block_literal_global.524
- ___block_literal_global.553
- ___block_literal_global.574
- ___block_literal_global.583
- ___block_literal_global.621
- ___block_literal_global.634
- _objc_msgSend$demoLiveStreamURLForCameraName:
- _objc_msgSend$demoSnapshotURLForCameraName:
- _objc_msgSend$demoURLWithCameraName:fileName:extension:
CStrings:
+ "%{public}s Home Sensing"
+ "(%@:%s) selected home is current home %{private}@ %{public}@"
+ "(%@:%s) selected home is synced identifier %{public}@"
+ "(%s) accessory %@ (uniqueIdentifier: %{public}@) | hh1EOLEnabled = %{BOOL}d"
+ "-[HFItemManager(HomeKitDelegates) accessory:didUpdateHH1EOLEnabled:]"
+ "@\"CLLocation\""
+ "Current accessory set, Ignoring requested home - %{private}@ %{public}@"
+ "Error: non-Home process is trying set state restoration values %@"
+ "HFStateRestorationSettings Saving home identifier %{public}@"
+ "HFStateRestorationSettings Sending notification for home identifier %{public}@"
+ "HFStateRestorationSettings Synchronizing prefs with selected home %{public}@"
+ "HFStateRestorationSettings selectedHomeDidChange Notifying observers of new home ID %{public}@"
+ "HF_SymptomStatusBannerItem"
+ "HF_SymptomStatusItem"
+ "Handler has symptom other than internet outage: %@"
+ "Home Sensing is %{public}s"
+ "Loaded synced selected home %{private}@ %{public}@"
+ "Notifying local clients of selected home change and saving to preferences %{private}@ %{public}@"
+ "PIP - Checking for locked screen; isDeviceUnlocked: %{BOOL}d"
+ "PIP - manually setting wantsToPlay = YES after play selected during PIP."
+ "Previous save existed - cancelling"
+ "Primary home not specified - using first home %{private}@ %{public}@"
+ "Received HFHomeSyncPreferencesDidChange notification"
+ "Selected home defaulting to currentAccessory Home - %{private}@ %{public}@"
+ "Selected home is now %{private}@ %{public}@"
+ "Selected home not specified - using primary home %{private}@ %{public}@"
+ "T@\"NACancelationToken\",&,N,V_cancelationToken"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_serialQueue"
+ "T{os_unfair_lock_s=I},N,V_selectedHomeLock"
+ "Updating value for Home.app preference %{public}@ to: %{public}@"
+ "User initiated change to home: %{private}@ %{public}@"
+ "_cancelationToken"
+ "_reallySetSelectedHomeIdentifier:"
+ "_requestSelectedHome %{private}@ %{public}@"
+ "_selectedHomeLock"
+ "_serialQueue"
+ "bannerSymptom"
+ "cancelationToken"
+ "demoLiveStreamURLForCamera:"
+ "demoSnapshotURLForCamera:"
+ "demoURLWithCamera:fileName:extension:"
+ "hf_isHH1EOLEnabled"
+ "hf_nextSymptomAfterInternetOutageInSortedList:"
+ "homeManagerDidUpdateHomes: %@, manager's currentHome: %{private}@ %{public}@"
+ "isCanceled"
+ "isHH1EOLEnabled"
+ "selectedHomeLock"
+ "serialQueue"
+ "setCancelationToken:"
+ "setSelectedHomeLock:"
+ "setSerialQueue:"
+ "updateHomeSensingState - Home Sensing: isSensingEnabled? %{bool}d homeManager.currentHome: %{private}@ %{public}@ selectedHome: %{private}@ %{public}@"
+ "updateHomeSensingState Home Sensing: requesting home %{private}@ %{public}@"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "{os_unfair_lock_s=I}16@0:8"
- "%s Home Sensing"
- "(%@:%s) selected home is current home %@"
- "(%@:%s) selected home is synced identifier %@"
- "Checking for locked screen; isDeviceUnlocked: %{BOOL}d"
- "Current accessory set, Ignoring requested home - %@"
- "Home Sensing is %s"
- "Home Sensing: requesting home %@"
- "Loaded synced selected home %@"
- "Notifying local clients of selected home change and saving to preferences"
- "Primary home not specified - using first home %@"
- "Saving home identifier %@"
- "Selected home defaulting to currentAccessory Home - %@"
- "Selected home is now %@"
- "Selected home not specified - using primary home %@"
- "Updating value for Home.app preference %@ to: %@"
- "User initiated change to home: %@"
- "demoLiveStreamURLForCameraName:"
- "demoSnapshotURLForCameraName:"
- "demoURLWithCameraName:fileName:extension:"
- "homeManagerDidUpdateHomes: %@, manager's currentHome: %@"
- "manually setting wantsToPlay = YES after play selected during PIP."
- "updateHomeSensingState - Home Sensing: isSensingEnabled? %{bool}d homeManager.currentHome: %@ selectedHome: %@"

```
