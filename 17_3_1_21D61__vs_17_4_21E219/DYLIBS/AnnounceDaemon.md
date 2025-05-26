## AnnounceDaemon

> `/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon`

```diff

-217.30.3.0.0
-  __TEXT.__text: 0x4e024
-  __TEXT.__auth_stubs: 0xfb0
-  __TEXT.__objc_methlist: 0x2e0c
+217.40.9.0.0
+  __TEXT.__text: 0x4f388
+  __TEXT.__auth_stubs: 0x1010
+  __TEXT.__objc_methlist: 0x2e34
   __TEXT.__const: 0x26c
-  __TEXT.__cstring: 0x2558
-  __TEXT.__oslogstring: 0x5824
-  __TEXT.__gcc_except_tab: 0xacc
+  __TEXT.__cstring: 0x2aa8
+  __TEXT.__oslogstring: 0x5684
+  __TEXT.__gcc_except_tab: 0xae4
   __TEXT.__swift5_typeref: 0x1eb
   __TEXT.__swift5_capture: 0x54
   __TEXT.__constg_swiftt: 0x1a0

   __TEXT.__swift5_fieldmd: 0xe4
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__unwind_info: 0x120c
+  __TEXT.__unwind_info: 0x127c
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x9d2
-  __TEXT.__objc_methname: 0xb45c
+  __TEXT.__objc_methname: 0xb4f6
   __TEXT.__objc_methtype: 0x2911
-  __TEXT.__objc_stubs: 0x8a00
-  __DATA_CONST.__got: 0x4d0
-  __DATA_CONST.__const: 0x16b0
+  __TEXT.__objc_stubs: 0x89a0
+  __DATA_CONST.__got: 0x4c8
+  __DATA_CONST.__const: 0x1690
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6550
-  __DATA_CONST.__objc_selrefs: 0x25d8
-  __AUTH_CONST.__const: 0x9a0
+  __DATA_CONST.__objc_const: 0x6590
+  __DATA_CONST.__objc_selrefs: 0x25f0
+  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_classrefs: 0x3c8
+  __DATA_CONST.__objc_superrefs: 0x108
+  __AUTH_CONST.__const: 0x900
   __AUTH_CONST.__objc_const: 0x12e8
   __AUTH_CONST.__cfstring: 0x13a0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__auth_ptr: 0x28
-  __AUTH_CONST.__auth_got: 0x7e8
+  __AUTH_CONST.__auth_got: 0x818
   __AUTH.__objc_data: 0x598
   __AUTH.__data: 0x68
-  __DATA.__objc_protorefs: 0x48
-  __DATA.__objc_classrefs: 0x3c0
-  __DATA.__objc_superrefs: 0x108
-  __DATA.__objc_ivar: 0x28c
+  __DATA.__objc_ivar: 0x290
   __DATA.__objc_data: 0x68
-  __DATA.__data: 0x1248
+  __DATA.__data: 0x1260
   __DATA.__bss: 0x280
-  __DATA.__common: 0x8
+  __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x948
   __DATA_DIRTY.__data: 0x68
   __DATA_DIRTY.__bss: 0x100

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1461
-  Symbols:   5418
-  CStrings:  2958
+  Functions: 1484
+  Symbols:   5399
+  CStrings:  2987
 
Symbols:
+ -[ANRapportConnection clientQueue]
+ -[ANRapportConnection setClientQueue:]
+ -[HMAccessory(Announce) an_announceSettingFromAccessorySettings]
+ GCC_except_table42
+ GCC_except_table51
+ GCC_except_table59
+ GCC_except_table61
+ GCC_except_table63
+ _OBJC_CLASS_$_HMImmutableSetting
+ _OBJC_IVAR_$_ANRapportConnection._clientQueue
+ __OBJC_$_CLASS_METHODS_HMAccessory(Announce|AnnounceDaemon|AnnounceDaemon1)
+ __OBJC_$_INSTANCE_METHODS_HMAccessory(Announce|AnnounceDaemon|AnnounceDaemon1)
+ ___34-[ANRapportConnection _setupLink:]_block_invoke.36
+ ___34-[ANRapportConnection _setupLink:]_block_invoke.39
+ ___34-[ANRapportConnection _setupLink:]_block_invoke.42
+ ___46-[ANRapportConnection _linkForDevice:handler:]_block_invoke.45
+ ___46-[ANRapportConnection _linkForDevice:handler:]_block_invoke.46
+ ___53-[ANRapportConnection _registerMessageRequestHandler]_block_invoke.48
+ ___58-[ANRapportConnection activateLinkWithOptions:completion:]_block_invoke.25
+ ___64-[ANAnnounceServiceListener listener:shouldAcceptNewConnection:]_block_invoke.98
+ ___64-[ANRapportConnection _registerHomeLocationStatusRequestHandler]_block_invoke.52
+ ___64-[HMAccessory(Announce) an_announceSettingFromAccessorySettings]_block_invoke
+ ___64-[HMAccessory(Announce) an_announceSettingFromAccessorySettings]_block_invoke.8
+ ___66-[ANTonePlayerServiceListener listener:shouldAcceptNewConnection:]_block_invoke.49
+ ___68-[ANRapportConnection _decrementMessageCountForCompanionLinkClient:]_block_invoke
+ ___68-[ANRapportConnection _incrementMessageCountForCompanionLinkClient:]_block_invoke
+ ___71-[ANPlaybackSessionServiceListener listener:shouldAcceptNewConnection:]_block_invoke.89
+ ___71-[ANPlaybackSessionServiceListener listener:shouldAcceptNewConnection:]_block_invoke.92
+ ___76-[ANAnnounceReachabilityServiceListener listener:shouldAcceptNewConnection:]_block_invoke.71
+ ___96-[ANPlaybackSessionServiceListener coordinator:didReceiveAnnouncement:forGroupID:forEndpointID:]_block_invoke.100
+ ___block_descriptor_56_e8_32bs40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs56r64w_e17_v16?0"NSError"8ls32l8s40l8w64l8s48l8r56l8
+ ___block_literal_global.11
+ ___block_literal_global.143
+ ___block_literal_global.15
+ ___block_literal_global.169
+ ___block_literal_global.203
+ ___block_literal_global.224
+ ___swift_allocate_value_buffer
+ ___swift_project_value_buffer
+ _objc_msgSend$clientQueue
+ _swift_dynamicCastObjCClass
- +[HMAccessory(Announce) accessoriesWithAnnounceEnabledFromAccessories:]
- +[HMAccessory(Announce) announceAccessoriesFromAccessories:]
- +[HMAccessory(Announce) announceAccessoriesWithAnnounceEnabledFromAccessories:]
- +[HMAccessory(Announce) appleAnnounceAccessoriesFromAccessories:]
- +[HMAccessory(Announce) appleAnnounceHostAccessoriesFromAccessories:]
- -[HMAccessory(Announce) an_isAnnounceAccessory]
- -[HMAccessory(Announce) an_isAnnounceEnabled]
- -[HMAccessory(Announce) an_isAppleAnnounceAccessory]
- -[HMAccessory(Announce) an_isAppleAnnounceHostAccessory]
- GCC_except_table46
- GCC_except_table58
- GCC_except_table60
- GCC_except_table70
- _ANLogHandleAccessory_Announce
- __OBJC_$_CLASS_METHODS_HMAccessory(Announce)
- __OBJC_$_INSTANCE_METHODS_HMAccessory(Announce)
- ___34-[ANRapportConnection _setupLink:]_block_invoke.34
- ___34-[ANRapportConnection _setupLink:]_block_invoke.37
- ___34-[ANRapportConnection _setupLink:]_block_invoke.40
- ___45-[HMAccessory(Announce) an_isAnnounceEnabled]_block_invoke
- ___45-[HMAccessory(Announce) an_isAnnounceEnabled]_block_invoke.9
- ___46-[ANRapportConnection _linkForDevice:handler:]_block_invoke.44
- ___53-[ANRapportConnection _registerMessageRequestHandler]_block_invoke.46
- ___58-[ANRapportConnection activateLinkWithOptions:completion:]_block_invoke.22
- ___60+[HMAccessory(Announce) announceAccessoriesFromAccessories:]_block_invoke
- ___64-[ANAnnounceServiceListener listener:shouldAcceptNewConnection:]_block_invoke.97
- ___64-[ANRapportConnection _registerHomeLocationStatusRequestHandler]_block_invoke.50
- ___65+[HMAccessory(Announce) appleAnnounceAccessoriesFromAccessories:]_block_invoke
- ___66-[ANTonePlayerServiceListener listener:shouldAcceptNewConnection:]_block_invoke.48
- ___69+[HMAccessory(Announce) appleAnnounceHostAccessoriesFromAccessories:]_block_invoke
- ___71+[HMAccessory(Announce) accessoriesWithAnnounceEnabledFromAccessories:]_block_invoke
- ___71-[ANPlaybackSessionServiceListener listener:shouldAcceptNewConnection:]_block_invoke.88
- ___71-[ANPlaybackSessionServiceListener listener:shouldAcceptNewConnection:]_block_invoke.91
- ___76-[ANAnnounceReachabilityServiceListener listener:shouldAcceptNewConnection:]_block_invoke.70
- ___79+[HMAccessory(Announce) announceAccessoriesWithAnnounceEnabledFromAccessories:]_block_invoke
- ___96-[ANPlaybackSessionServiceListener coordinator:didReceiveAnnouncement:forGroupID:forEndpointID:]_block_invoke.99
- ___block_descriptor_32_e21_B16?0"HMAccessory"8l
- ___block_descriptor_64_e8_32s40bs48bs_e17_v16?0"NSError"8ls40l8s48l8s32l8
- ___block_descriptor_64_e8_32s40bs48r56w_e17_v16?0"NSError"8ls32l8w56l8s40l8r48l8
- ___block_literal_global.142
- ___block_literal_global.168
- ___block_literal_global.18
- ___block_literal_global.202
- ___block_literal_global.216
- ___block_literal_global.22
- ___block_literal_global.24
- ___block_literal_global.41
- _objc_msgSend$accessorySettingsCache
- _objc_msgSend$an_isAppleAnnounceAccessory
- _objc_msgSend$an_isAppleAnnounceHostAccessory
- _objc_msgSend$settingsForAccessory:
CStrings:
+ "("
+ "Announce Enabled Setting For Accessory %@: %{bool}d"
+ "Announce is DISABLED For Accessory %@"
+ "Announce setting not found in accessory settings"
+ "Announce setting not found in settings from data source"
+ "AnnounceDaemon1"
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "Settings not found in settings from data source"
+ "Supports Announce for Accessory %@: %{bool}d"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSNumber\",R,N"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_clientQueue"
+ "T@\"NSString\",?,R,C"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "[Override] Force Allow Announce For Accessory %@ Enabled"
+ "[Override] Force Announce Supported For Accessory %@ Enabled"
+ "_clientQueue"
+ "an_announceSettingFromAccessorySettings"
+ "clientQueue"
+ "com.apple.announce.RapportClientQueue"
+ "home:didUpdateSupportsResidentActionSetStateEvaluation:"
+ "invalid Collection: less than 'count' elements in collection"
+ "setClientQueue:"
- "%@Announce Enabled Setting For Accessory (Name = %@, ID = %@): %@"
- "%@Announce Enabled Setting For Endpoint Accessory (Name = %@, ID = %@): %d"
- "%@Announce is DISABLED For Accessory (Name = %@, ID = %@)"
- "%@Supports Announce for Accessory (Name = %@, ID = %@): %d"
- "%@[Override] Force Allow Announce For Accessory (Name = %@, ID = %@) Enabled"
- "%@[Override] Force Announce Supported For Accessory (Name = %@, ID = %@) Enabled"
- "'"
- "accessory:didUpdateBulletinBoardNotificationServiceGroupForService:"

```
