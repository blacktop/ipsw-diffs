## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/Versions/A/HearingUtilities`

```diff

-456.6.3.0.0
-  __TEXT.__text: 0x705d4
-  __TEXT.__auth_stubs: 0x930
-  __TEXT.__objc_methlist: 0x46c0
+456.8.7.0.0
+  __TEXT.__text: 0x71900
+  __TEXT.__auth_stubs: 0x940
+  __TEXT.__objc_methlist: 0x51fc
   __TEXT.__const: 0x1f8
-  __TEXT.__gcc_except_tab: 0x1d34
-  __TEXT.__cstring: 0x8967
-  __TEXT.__oslogstring: 0x1826
-  __TEXT.__dlopen_cstrs: 0x1b2
-  __TEXT.__unwind_info: 0x1730
-  __TEXT.__objc_classname: 0x519
-  __TEXT.__objc_methname: 0xc485
-  __TEXT.__objc_methtype: 0x189c
-  __TEXT.__objc_stubs: 0x9100
-  __DATA_CONST.__got: 0x3e8
-  __DATA_CONST.__const: 0x7e8
+  __TEXT.__gcc_except_tab: 0x1d2c
+  __TEXT.__cstring: 0x8a73
+  __TEXT.__oslogstring: 0x1a4c
+  __TEXT.__dlopen_cstrs: 0x224
+  __TEXT.__unwind_info: 0x1770
+  __TEXT.__objc_classname: 0x544
+  __TEXT.__objc_methname: 0xc8c4
+  __TEXT.__objc_methtype: 0x18c4
+  __TEXT.__objc_stubs: 0x93e0
+  __DATA_CONST.__got: 0x3f0
+  __DATA_CONST.__const: 0x800
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x88
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2bd8
+  __DATA_CONST.__objc_selrefs: 0x2e80
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x218
-  __AUTH_CONST.__auth_got: 0x4a8
-  __AUTH_CONST.__const: 0x2980
-  __AUTH_CONST.__cfstring: 0x5ea0
-  __AUTH_CONST.__objc_const: 0x8108
+  __AUTH_CONST.__auth_got: 0x4b0
+  __AUTH_CONST.__const: 0x2a00
+  __AUTH_CONST.__cfstring: 0x5f60
+  __AUTH_CONST.__objc_const: 0x6f30
   __AUTH_CONST.__objc_intobj: 0x4b0
   __AUTH_CONST.__objc_dictobj: 0x208
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xb40
-  __DATA.__objc_ivar: 0x5fc
-  __DATA.__data: 0x778
-  __DATA.__bss: 0x238
+  __DATA.__objc_ivar: 0x614
+  __DATA.__data: 0x7d8
+  __DATA.__bss: 0x258
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D4453C9A-5F0F-3412-9D97-1EF254557850
-  Functions: 2165
-  Symbols:   4915
-  CStrings:  4320
+  UUID: 0F3CAEC9-30FD-3CB1-B21E-0B09C7500556
+  Functions: 2228
+  Symbols:   5026
+  CStrings:  4392
 
Symbols:
+ +[AXHAController descriptionForHandoffReason:].cold.1
+ +[AXHAController sharedController].cold.1
+ +[AXHAServer sharedInstance].cold.1
+ +[AXHeardController sharedServer].cold.1
+ +[AXHearingAidDeviceController sharedController].cold.1
+ +[HANanoSettings sharedInstance].cold.1
+ +[HUAccessoryHearingSettings sharedInstance].cold.1
+ +[HUAccessoryHearingSyncManager sharedInstance].cold.1
+ +[HUAccessoryManager sharedInstance].cold.1
+ +[HUComfortSoundsController sharedController].cold.1
+ +[HUComfortSoundsSettings sharedInstance].cold.1
+ +[HUHearingAidSettings sharedInstance].cold.1
+ +[HUHearingSettings sharedInstance].cold.1
+ +[HUNearbyController sharedInstance].cold.1
+ +[HUNearbyHearingAidController sharedInstance].cold.1
+ +[HUNearbySettings sharedInstance].cold.1
+ +[HUUtilities sharedUtilities].cold.1
+ -[HUComfortSoundsSettings keysMonitoredForUpdates]
+ -[HUComfortSoundsSettings keysMonitoredForUpdates].cold.1
+ -[HUComfortSoundsSettings preferenceKeyForSelector:].cold.1
+ -[HUComfortSoundsSettings setValue:forPreferenceKey:].cold.2
+ -[HUHearingAidSettings preferenceKeyForSelector:].cold.1
+ -[HUNearbyController didReceiveHearingAidsMessage:fromDevice:]
+ -[HUNearbyController didUpdateDevices:]
+ -[HUNearbyController discoverSCIDSServiceWithDevicesUpdates:messageBlock:]
+ -[HUNearbyController interDeviceCommunicator]
+ -[HUNearbyController logSCIDSDeviceFromDevices:]
+ -[HUNearbyController scIDSDevices]
+ -[HUNearbyController scIDSHasPeers]
+ -[HUNearbyController scIDSServiceDevicesUpdatesBlock]
+ -[HUNearbyController scIDSServiceHasPeers]
+ -[HUNearbyController scIDSServiceMessageBlock]
+ -[HUNearbyController sendSCIDSMessage:toDevice:]
+ -[HUNearbyController setInterDeviceCommunicator:]
+ -[HUNearbyController setScIDSDevices:]
+ -[HUNearbyController setScIDSServiceDevicesUpdatesBlock:]
+ -[HUNearbyController setScIDSServiceHasPeers:]
+ -[HUNearbyController setScIDSServiceMessageBlock:]
+ -[HUNearbyController stopDiscoveringSCIDSService]
+ -[HUNearbyDevice isSCIDSService]
+ -[HUNearbyDevice setIsSCIDSService:]
+ -[HUNearbyHearingAidController scIDSServiceDevice:didReceiveMessage:]
+ -[HUNearbyHearingAidController scIDSServiceDidRemoveDevices:]
+ -[HUUtilities headphoneStreamSelectedForAddresses:]
+ -[HUUtilities headphoneStreamSelectedForAddresses:].cold.1
+ -[HUUtilities headphoneStreamSelected].cold.1
+ AXLogHearingHalPlugin.cold.1
+ AccessibilitySharedSupportLibraryCore.frameworkLibrary
+ GCC_except_table129
+ GCC_except_table50
+ GCC_except_table66
+ OBJC_IVAR_$_HUNearbyController._interDeviceCommunicator
+ OBJC_IVAR_$_HUNearbyController._scIDSDevices
+ OBJC_IVAR_$_HUNearbyController._scIDSServiceDevicesUpdatesBlock
+ OBJC_IVAR_$_HUNearbyController._scIDSServiceHasPeers
+ OBJC_IVAR_$_HUNearbyController._scIDSServiceMessageBlock
+ OBJC_IVAR_$_HUNearbyDevice._isSCIDSService
+ _OUTLINED_FUNCTION_3
+ __35+[HUUtilities XDCObjectFromObject:]_block_invoke.74
+ __35+[HUUtilities objectFromXDCObject:]_block_invoke.82
+ __37-[HUNearbyHearingAidController start]_block_invoke.112
+ __37-[HUNearbyHearingAidController start]_block_invoke.116
+ __37-[HUNearbyHearingAidController start]_block_invoke.121
+ __37-[HUNearbyHearingAidController start]_block_invoke.127
+ __37-[HUNearbyHearingAidController start]_block_invoke.131
+ __37-[HUNearbyHearingAidController start]_block_invoke.98
+ __37-[HUNearbyHearingAidController start]_block_invoke_2.113
+ __37-[HUNearbyHearingAidController start]_block_invoke_2.117
+ __37-[HUNearbyHearingAidController start]_block_invoke_2.122
+ __37-[HUNearbyHearingAidController start]_block_invoke_2.128
+ __49-[HUNearbyController stopDiscoveringSCIDSService]_block_invoke.185
+ __55-[HUUtilities pauseNowPlaying:withQueue:andCompletion:]_block_invoke.51
+ __55-[HUUtilities pauseNowPlaying:withQueue:andCompletion:]_block_invoke_2.52
+ __56-[HUNearbyHearingAidController checkHandoffAfterTimeout]_block_invoke.88
+ __59-[HUNearbyHearingAidController sendMessagesPriorityDefault]_block_invoke.181
+ __69-[HUNearbyHearingAidController scIDSServiceDevice:didReceiveMessage:]_block_invoke.234
+ __74-[HUNearbyController discoverSCIDSServiceWithDevicesUpdates:messageBlock:]_block_invoke.184
+ __76-[HUNearbyHearingAidController checkConnectionRequestedForMediaAfterTimeout]_block_invoke.50
+ __77-[NSArray(_AX_HA_PROGRAMS_ARRAY_) setProgram:withOtherSidePrograms:selected:]_block_invoke.152
+ __AXSIsNonUIBuild
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AXSSInterDeviceHearingAidsMessagesObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AXSSInterDeviceHearingAidsMessagesObserver
+ __OBJC_$_PROTOCOL_REFS_AXSSInterDeviceHearingAidsMessagesObserver
+ __OBJC_LABEL_PROTOCOL_$_AXSSInterDeviceHearingAidsMessagesObserver
+ __OBJC_PROTOCOL_$_AXSSInterDeviceHearingAidsMessagesObserver
+ ___39-[HUNearbyController didUpdateDevices:]_block_invoke
+ ___48-[HUNearbyController sendSCIDSMessage:toDevice:]_block_invoke
+ ___49-[HUNearbyController stopDiscoveringSCIDSService]_block_invoke
+ ___50-[HUComfortSoundsSettings keysMonitoredForUpdates]_block_invoke
+ ___62-[HUNearbyController didReceiveHearingAidsMessage:fromDevice:]_block_invoke
+ ___69-[HUNearbyHearingAidController scIDSServiceDevice:didReceiveMessage:]_block_invoke
+ ___74-[HUNearbyController discoverSCIDSServiceWithDevicesUpdates:messageBlock:]_block_invoke
+ ___AccessibilitySharedSupportLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32s_e41_v24?0"HUNearbyDevice"8"NSDictionary"16l
+ ___block_descriptor_64_e8_32s40bs48bs56r_e5_v8?0l
+ ___copy_helper_block_e8_32s40b48b56r
+ ___getAXSSInterDeviceCommunicatorClass_block_invoke
+ __block_literal_global.159
+ __block_literal_global.186
+ __getAXSSInterDeviceCommunicatorClass_block_invoke.cold.1
+ _audit_stringAccessibilitySharedSupport
+ _headphoneStreamSelectedForAddresses
+ _objc_msgSend$additionalInfoForPrefenceUpdate
+ _objc_msgSend$discoverSCIDSServiceWithDevicesUpdates:messageBlock:
+ _objc_msgSend$hasPeers
+ _objc_msgSend$headphoneStreamSelectedForAddresses:
+ _objc_msgSend$interDeviceCommunicator
+ _objc_msgSend$isSCIDSService
+ _objc_msgSend$logSCIDSDeviceFromDevices:
+ _objc_msgSend$scIDSDevices
+ _objc_msgSend$scIDSHasPeers
+ _objc_msgSend$scIDSServiceDevice:didReceiveMessage:
+ _objc_msgSend$scIDSServiceDevicesUpdatesBlock
+ _objc_msgSend$scIDSServiceDidRemoveDevices:
+ _objc_msgSend$scIDSServiceHasPeers
+ _objc_msgSend$scIDSServiceMessageBlock
+ _objc_msgSend$sendHearingAidsMessage:toDevice:
+ _objc_msgSend$sendSCIDSMessage:toDevice:
+ _objc_msgSend$setHearingAidsMessagesObserver:
+ _objc_msgSend$setInterDeviceCommunicator:
+ _objc_msgSend$setScIDSServiceDevicesUpdatesBlock:
+ _objc_msgSend$setScIDSServiceHasPeers:
+ _objc_msgSend$setScIDSServiceMessageBlock:
+ _objc_msgSend$stopDiscoveringSCIDSService
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ getAXSSInterDeviceCommunicatorClass.softClass
+ keysMonitoredForUpdates.KeysMonitoredForUpdates
+ keysMonitoredForUpdates.onceToken
- GCC_except_table123
- GCC_except_table31
- GCC_except_table33
- GCC_except_table37
- GCC_except_table40
- GCC_except_table46
- __35+[HUUtilities XDCObjectFromObject:]_block_invoke.62
- __35+[HUUtilities objectFromXDCObject:]_block_invoke.70
- __37-[HUNearbyHearingAidController start]_block_invoke.109
- __37-[HUNearbyHearingAidController start]_block_invoke.113
- __37-[HUNearbyHearingAidController start]_block_invoke.118
- __37-[HUNearbyHearingAidController start]_block_invoke.95
- __37-[HUNearbyHearingAidController start]_block_invoke_2.110
- __37-[HUNearbyHearingAidController start]_block_invoke_2.114
- __55-[HUUtilities pauseNowPlaying:withQueue:andCompletion:]_block_invoke.39
- __55-[HUUtilities pauseNowPlaying:withQueue:andCompletion:]_block_invoke_2.40
- __56-[HUNearbyHearingAidController checkHandoffAfterTimeout]_block_invoke.84
- __59-[HUNearbyHearingAidController sendMessagesPriorityDefault]_block_invoke.168
- __76-[HUNearbyHearingAidController checkConnectionRequestedForMediaAfterTimeout]_block_invoke.46
- __77-[NSArray(_AX_HA_PROGRAMS_ARRAY_) setProgram:withOtherSidePrograms:selected:]_block_invoke.139
- __block_literal_global.146
- __block_literal_global.184
- __block_literal_global.91
CStrings:
+ "-"
+ "/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Contents/MacOS/AccessibilitySharedSupport"
+ ":"
+ ":output"
+ "AXSSInterDeviceCommunicator"
+ "AXSSInterDeviceHearingAidsMessagesObserver"
+ "HCMessageIdentifierControllerConnected"
+ "HCMessageIdentifierRemoteControllerConnectWithReason"
+ "IDS Sending(%@) %@ to %{sensitive}@ with %@, priority: %@"
+ "Received HearingAids Message %@ from device: %@"
+ "Request connection from SC IDS Service Device %@"
+ "SC IDS Service Removed devices: %@"
+ "SC IDS Service cleaned"
+ "SC IDS Service didReceiveHearingAidsMessage %@ from device: %@"
+ "SC IDS Service didUpdateDevices: %@"
+ "SC IDS Service has peers %d"
+ "SC IDS Service removed devices: %@, updated devices: %@"
+ "SC IDS Service sending message %@"
+ "SC IDS Service start"
+ "SC IDS Service stop"
+ "T@\"NSArray\",&,V_manufacturer"
+ "T@\"NSArray\",&,V_model"
+ "T@\"NSArray\",R,&"
+ "T@\"NSMutableArray\",C,N,V_scIDSDevices"
+ "T@,&,N,V_interDeviceCommunicator"
+ "T@?,C,N,V_scIDSServiceDevicesUpdatesBlock"
+ "T@?,C,N,V_scIDSServiceMessageBlock"
+ "TB,N,V_isSCIDSService"
+ "TB,V_scIDSServiceHasPeers"
+ "Update controllerState %@ for device: %@"
+ "_UpdateInfo"
+ "_interDeviceCommunicator"
+ "_isSCIDSService"
+ "_scIDSDevices"
+ "_scIDSServiceDevicesUpdatesBlock"
+ "_scIDSServiceHasPeers"
+ "_scIDSServiceMessageBlock"
+ "additionalInfoForPrefenceUpdate"
+ "didReceiveHearingAidsMessage:fromDevice:"
+ "didUpdateDevices:"
+ "discoverSCIDSServiceWithDevicesUpdates:messageBlock:"
+ "hasPeers"
+ "headphoneStreamSelected selectedRoute: %@"
+ "headphoneStreamSelected uniqueID %@ selectedRoute: %@"
+ "headphoneStreamSelectedForAddresses:"
+ "interDeviceCommunicator"
+ "isSCIDSService"
+ "keysMonitoredForUpdates"
+ "logSCIDSDeviceFromDevices:"
+ "scIDSDevices"
+ "scIDSHasPeers"
+ "scIDSServiceDevice:didReceiveMessage:"
+ "scIDSServiceDevicesUpdatesBlock"
+ "scIDSServiceDidRemoveDevices:"
+ "scIDSServiceHasPeers"
+ "scIDSServiceMessageBlock"
+ "sendHearingAidsMessage:toDevice:"
+ "sendSCIDSMessage:toDevice:"
+ "setHearingAidsMessagesObserver:"
+ "setInterDeviceCommunicator:"
+ "setIsSCIDSService:"
+ "setScIDSDevices:"
+ "setScIDSServiceDevicesUpdatesBlock:"
+ "setScIDSServiceHasPeers:"
+ "setScIDSServiceMessageBlock:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/AccessibilitySharedSupport"
+ "stopDiscoveringSCIDSService"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "v24@0:8@\"NSArray\"16"
+ "v32@0:8@\"NSDictionary\"16@24"
+ "v32@0:8@?16@?24"
- "@\"NSMutableArray\"16@0:8"
- "IDS Sending(%@) %@ to %@ with %@, priority: %@"
- "T@\"NSMutableArray\",&,V_manufacturer"
- "T@\"NSMutableArray\",&,V_model"
- "T@\"NSMutableArray\",R,&"

```
