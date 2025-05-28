## ReplayKit

> `/System/Library/Frameworks/ReplayKit.framework/ReplayKit`

```diff

-526.7.0.0.0
-  __TEXT.__text: 0x23790
+530.14.1.3.0
+  __TEXT.__text: 0x250b4
   __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_methlist: 0x1c4c
+  __TEXT.__objc_methlist: 0x1d3c
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x3f95
-  __TEXT.__oslogstring: 0x3420
+  __TEXT.__cstring: 0x4356
+  __TEXT.__oslogstring: 0x3521
   __TEXT.__gcc_except_tab: 0x130
-  __TEXT.__unwind_info: 0x790
-  __TEXT.__objc_classname: 0x634
-  __TEXT.__objc_methname: 0x69a6
-  __TEXT.__objc_methtype: 0x1993
-  __TEXT.__objc_stubs: 0x44c0
+  __TEXT.__unwind_info: 0x7cc
+  __TEXT.__objc_classname: 0x67a
+  __TEXT.__objc_methname: 0x6e16
+  __TEXT.__objc_methtype: 0x1abe
+  __TEXT.__objc_stubs: 0x48c0
   __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x7a8
-  __DATA_CONST.__objc_classlist: 0xf8
+  __DATA_CONST.__const: 0x818
+  __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0xd0
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4eb0
-  __DATA_CONST.__objc_selrefs: 0x1650
-  __AUTH_CONST.__cfstring: 0x12c0
-  __AUTH_CONST.__const: 0x818
-  __AUTH_CONST.__objc_const: 0xf28
+  __DATA_CONST.__objc_const: 0x5498
+  __DATA_CONST.__objc_selrefs: 0x1758
+  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_classrefs: 0x2b0
+  __DATA_CONST.__objc_superrefs: 0xa0
+  __AUTH_CONST.__const: 0x898
+  __AUTH_CONST.__cfstring: 0x1360
+  __AUTH_CONST.__objc_const: 0xfb8
   __AUTH_CONST.__auth_got: 0x4c8
-  __AUTH.__objc_data: 0x960
-  __DATA.__objc_protorefs: 0x60
-  __DATA.__objc_classrefs: 0x270
-  __DATA.__objc_superrefs: 0x98
-  __DATA.__objc_ivar: 0x1bc
-  __DATA.__data: 0x9c8
-  __DATA.__bss: 0xa0
+  __AUTH.__objc_data: 0x9b0
+  __DATA.__objc_ivar: 0x1c8
+  __DATA.__data: 0xa88
+  __DATA.__bss: 0xd0
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AVConference.framework/AVConference
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
+  - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
+  - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /System/Library/PrivateFrameworks/Celestial.framework/Celestial
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/Pegasus.framework/Pegasus
   - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 917
-  Symbols:   3356
-  CStrings:  1886
+  Functions: 943
+  Symbols:   3487
+  CStrings:  1969
 
Symbols:
+ +[RPControlCenterAngelProxy sharedInstance]
+ -[RPControlCenterAngelProxy .cxx_destruct]
+ -[RPControlCenterAngelProxy cancelRecordingCountdown]
+ -[RPControlCenterAngelProxy connectionManagerQueue]
+ -[RPControlCenterAngelProxy countdownInterruptWithStatus:]
+ -[RPControlCenterAngelProxy delegate]
+ -[RPControlCenterAngelProxy getBSServiceInterface]
+ -[RPControlCenterAngelProxy hideAndStopRecordingBanner]
+ -[RPControlCenterAngelProxy init]
+ -[RPControlCenterAngelProxy setCountdownState:]
+ -[RPControlCenterAngelProxy setDelegate:]
+ -[RPControlCenterAngelProxy setupConnection]
+ -[RPControlCenterAngelProxy showReactionsTipForApplication:bundleID:]
+ -[RPControlCenterAngelProxy showRecordingBanner]
+ -[RPControlCenterAngelProxy startRecordingCountdown]
+ -[RPControlCenterAngelProxy stopCurrentSession]
+ -[RPControlCenterAngelProxy stopRecordingCalled]
+ -[RPFeatureFlagUtility coreGraphicsProxyingEnabled]
+ _OBJC_CLASS_$_BSMutableServiceInterface
+ _OBJC_CLASS_$_BSObjCProtocol
+ _OBJC_CLASS_$_BSServiceConnection
+ _OBJC_CLASS_$_BSServiceConnectionEndpoint
+ _OBJC_CLASS_$_BSServiceQuality
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_RBSDomainAttribute
+ _OBJC_CLASS_$_RPControlCenterAngelProxy
+ _OBJC_IVAR_$_RPControlCenterAngelProxy._connection
+ _OBJC_IVAR_$_RPControlCenterAngelProxy._delegate
+ _OBJC_IVAR_$_RPFeatureFlagUtility._coreGraphicsProxyingEnabled
+ _OBJC_METACLASS_$_RPControlCenterAngelProxy
+ __OBJC_$_CLASS_METHODS_RPControlCenterAngelProxy
+ __OBJC_$_INSTANCE_METHODS_RPControlCenterAngelProxy
+ __OBJC_$_INSTANCE_VARIABLES_RPControlCenterAngelProxy
+ __OBJC_$_PROP_LIST_RPControlCenterAngelProxy
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_RPAngelClientProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_RPAngelServerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RPAngelClientProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RPAngelServerProtocol
+ __OBJC_$_PROTOCOL_REFS_RPAngelClientProtocol
+ __OBJC_$_PROTOCOL_REFS_RPAngelServerProtocol
+ __OBJC_CLASS_PROTOCOLS_$_RPControlCenterAngelProxy
+ __OBJC_CLASS_RO_$_RPControlCenterAngelProxy
+ __OBJC_LABEL_PROTOCOL_$_RPAngelClientProtocol
+ __OBJC_LABEL_PROTOCOL_$_RPAngelServerProtocol
+ __OBJC_METACLASS_RO_$_RPControlCenterAngelProxy
+ __OBJC_PROTOCOL_$_RPAngelClientProtocol
+ __OBJC_PROTOCOL_$_RPAngelServerProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_RPAngelClientProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_RPAngelServerProtocol
+ ___21-[RPDaemonProxy init]_block_invoke.142
+ ___43+[RPControlCenterAngelProxy sharedInstance]_block_invoke
+ ___44-[RPControlCenterAngelProxy setupConnection]_block_invoke
+ ___44-[RPControlCenterAngelProxy setupConnection]_block_invoke.85
+ ___44-[RPControlCenterAngelProxy setupConnection]_block_invoke.92
+ ___44-[RPControlCenterAngelProxy setupConnection]_block_invoke_2
+ ___48-[RPBroadcastExtensionProxy setupNewConnection:]_block_invoke.62
+ ___48-[RPBroadcastExtensionProxy setupNewConnection:]_block_invoke.62.cold.1
+ ___50-[RPControlCenterAngelProxy getBSServiceInterface]_block_invoke
+ ___51-[RPControlCenterAngelProxy connectionManagerQueue]_block_invoke
+ ___55-[RPBroadcastSampleHandler _setupListenerWithEndpoint:]_block_invoke.94
+ ___55-[RPBroadcastSampleHandler _setupListenerWithEndpoint:]_block_invoke.97
+ ___55-[RPBroadcastSampleHandler _setupListenerWithEndpoint:]_block_invoke.97.cold.1
+ ___block_descriptor_32_e57_v16?0"BSServiceConnection<BSServiceConnectionContext>"8l
+ ___block_descriptor_40_e8_32s_e42_v16?0"<BSServiceConnectionConfiguring>"8ls32l8
+ ___block_descriptor_40_e8_32s_e57_v16?0"BSServiceConnection<BSServiceConnectionContext>"8ls32l8
+ ___block_literal_global.100
+ ___block_literal_global.146
+ ___block_literal_global.148
+ ___block_literal_global.150
+ ___block_literal_global.152
+ ___block_literal_global.154
+ ___block_literal_global.156
+ ___block_literal_global.158
+ ___block_literal_global.160
+ ___block_literal_global.162
+ ___block_literal_global.164
+ ___block_literal_global.166
+ ___block_literal_global.168
+ ___block_literal_global.170
+ ___block_literal_global.172
+ ___block_literal_global.174
+ ___block_literal_global.176
+ ___block_literal_global.178
+ ___block_literal_global.180
+ ___block_literal_global.182
+ ___block_literal_global.184
+ ___block_literal_global.186
+ ___block_literal_global.188
+ ___block_literal_global.190
+ ___block_literal_global.192
+ ___block_literal_global.194
+ ___block_literal_global.196
+ ___block_literal_global.198
+ ___block_literal_global.200
+ ___block_literal_global.202
+ ___block_literal_global.204
+ ___block_literal_global.206
+ ___block_literal_global.208
+ ___block_literal_global.210
+ ___block_literal_global.212
+ ___block_literal_global.214
+ ___block_literal_global.216
+ ___block_literal_global.218
+ ___block_literal_global.220
+ ___block_literal_global.226
+ ___block_literal_global.228
+ ___block_literal_global.230
+ ___block_literal_global.232
+ ___block_literal_global.234
+ ___block_literal_global.84
+ ___block_literal_global.93
+ ___block_literal_global.96
+ _connectionManagerQueue.connectionQueue
+ _connectionManagerQueue.onceToken
+ _getBSServiceInterface.__interface
+ _getBSServiceInterface.onceToken
+ _objc_msgSend$activate
+ _objc_msgSend$attributeWithDomain:name:
+ _objc_msgSend$cancelRecordingCountdown
+ _objc_msgSend$configureConnection:
+ _objc_msgSend$connectionManagerQueue
+ _objc_msgSend$connectionWithEndpoint:
+ _objc_msgSend$countdownInterruptWithStatus:
+ _objc_msgSend$endpointForMachName:service:instance:
+ _objc_msgSend$getBSServiceInterface
+ _objc_msgSend$hideAndStopRecordingBanner
+ _objc_msgSend$initWithBundleIdentifier:allowPlaceholder:error:
+ _objc_msgSend$interfaceWithIdentifier:
+ _objc_msgSend$localizedName
+ _objc_msgSend$protocolForProtocol:
+ _objc_msgSend$remoteTargetWithLaunchingAssertionAttributes:
+ _objc_msgSend$replayKitAngelDisconnected
+ _objc_msgSend$setActivationHandler:
+ _objc_msgSend$setClient:
+ _objc_msgSend$setClientMessagingExpectation:
+ _objc_msgSend$setCountdownState:
+ _objc_msgSend$setInterface:
+ _objc_msgSend$setInterfaceTarget:
+ _objc_msgSend$setServer:
+ _objc_msgSend$setServiceQuality:
+ _objc_msgSend$setTargetQueue:
+ _objc_msgSend$setupConnection
+ _objc_msgSend$showReactionsTipForApplication:bundleID:
+ _objc_msgSend$showRecordingBanner
+ _objc_msgSend$startRecordingCountdown
+ _objc_msgSend$stopCurrentSession
+ _objc_msgSend$stopRecordingCalled
+ _objc_msgSend$userInitiated
+ _sharedInstance.angelProxy
+ _showReactionsTip
- ___21-[RPDaemonProxy init]_block_invoke.141
- ___48-[RPBroadcastExtensionProxy setupNewConnection:]_block_invoke.61
- ___48-[RPBroadcastExtensionProxy setupNewConnection:]_block_invoke.61.cold.1
- ___55-[RPBroadcastSampleHandler _setupListenerWithEndpoint:]_block_invoke.93
- ___55-[RPBroadcastSampleHandler _setupListenerWithEndpoint:]_block_invoke.96
- ___55-[RPBroadcastSampleHandler _setupListenerWithEndpoint:]_block_invoke.96.cold.1
- ___block_literal_global.145
- ___block_literal_global.147
- ___block_literal_global.149
- ___block_literal_global.151
- ___block_literal_global.153
- ___block_literal_global.155
- ___block_literal_global.157
- ___block_literal_global.159
- ___block_literal_global.161
- ___block_literal_global.163
- ___block_literal_global.165
- ___block_literal_global.167
- ___block_literal_global.169
- ___block_literal_global.171
- ___block_literal_global.173
- ___block_literal_global.175
- ___block_literal_global.177
- ___block_literal_global.179
- ___block_literal_global.181
- ___block_literal_global.183
- ___block_literal_global.185
- ___block_literal_global.187
- ___block_literal_global.189
- ___block_literal_global.191
- ___block_literal_global.193
- ___block_literal_global.195
- ___block_literal_global.197
- ___block_literal_global.199
- ___block_literal_global.201
- ___block_literal_global.203
- ___block_literal_global.205
- ___block_literal_global.207
- ___block_literal_global.209
- ___block_literal_global.211
- ___block_literal_global.213
- ___block_literal_global.215
- ___block_literal_global.217
- ___block_literal_global.219
- ___block_literal_global.225
- ___block_literal_global.227
- ___block_literal_global.229
- ___block_literal_global.231
- ___block_literal_global.233
- ___block_literal_global.92
- ___block_literal_global.95
- ___block_literal_global.99
CStrings:
+ " [INFO] %{public}s:%d Activation handler"
+ " [INFO] %{public}s:%d Interruption handler"
+ " [INFO] %{public}s:%d Invalidation handler"
+ " [INFO] %{public}s:%d RPAngel endpoint nil"
+ " [INFO] %{public}s:%d RPAngelServerProtocol nil"
+ " [INFO] %{public}s:%d hideStatusBar=%d"
+ "-[RPControlCenterAngelProxy cancelRecordingCountdown]"
+ "-[RPControlCenterAngelProxy countdownInterruptWithStatus:]"
+ "-[RPControlCenterAngelProxy hideAndStopRecordingBanner]"
+ "-[RPControlCenterAngelProxy setCountdownState:]"
+ "-[RPControlCenterAngelProxy setupConnection]"
+ "-[RPControlCenterAngelProxy setupConnection]_block_invoke"
+ "-[RPControlCenterAngelProxy setupConnection]_block_invoke_2"
+ "-[RPControlCenterAngelProxy showReactionsTipForApplication:bundleID:]"
+ "-[RPControlCenterAngelProxy showRecordingBanner]"
+ "-[RPControlCenterAngelProxy startRecordingCountdown]"
+ "-[RPControlCenterAngelProxy stopCurrentSession]"
+ "-[RPControlCenterAngelProxy stopRecordingCalled]"
+ "@\"<RPControlCenterAngelProxyDelegate>\""
+ "@\"BSServiceConnection<BSServiceConnectionClient>\""
+ "BasicAngelIPC"
+ "CoreGraphicsProxying"
+ "EasyScreenSharing"
+ "RPAngelClientProtocol"
+ "RPAngelServerProtocol"
+ "RPControlCenterAngelProxy"
+ "RPHideStatusBar"
+ "T@\"<RPControlCenterAngelProxyDelegate>\",&,N,V_delegate"
+ "T@\"NSString\",?,R,C"
+ "TB,R,N,V_coreGraphicsProxyingEnabled"
+ "VB32@0:8@\"NSString\"16@\"NSString\"24"
+ "VB32@0:8@16@24"
+ "Vv24@0:8@?<v@?@\"NSString\"@\"NSError\">16"
+ "Vv32@0:8@\"NSString\"16@\"NSString\"24"
+ "Vv48@0:8@\"NSURL\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "Vv48@0:8@16@24@32@?40"
+ "_coreGraphicsProxyingEnabled"
+ "activate"
+ "attributeWithDomain:name:"
+ "cancelRecordingCountdown"
+ "com.apple.ReplayKitAngel.mach"
+ "com.apple.ReplayKitAngel.session"
+ "com.apple.common"
+ "com.replaykitangel.angelProxyConnectionQueue"
+ "configureConnection:"
+ "connectToAngelWithCompletionHandler:"
+ "connectionManagerQueue"
+ "connectionWithEndpoint:"
+ "coreGraphicsProxyingEnabled"
+ "countdownInterruptWithStatus:"
+ "dismissReactionsTipForApplication:bundleID:"
+ "endpointForMachName:service:instance:"
+ "getBSServiceInterface"
+ "hideAndStopRecordingBanner"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "interfaceWithIdentifier:"
+ "localizedName"
+ "pauseCurrentSystemSession"
+ "protocolForProtocol:"
+ "remoteTargetWithLaunchingAssertionAttributes:"
+ "replayKitAngelDisconnected"
+ "resumeCurrentSystemSession"
+ "setActivationHandler:"
+ "setClient:"
+ "setClientMessagingExpectation:"
+ "setCountdownState:"
+ "setInterface:"
+ "setInterfaceTarget:"
+ "setServer:"
+ "setServiceQuality:"
+ "setTargetQueue:"
+ "setupConnection"
+ "showReactionsTip"
+ "showReactionsTipForApplication:bundleID:"
+ "showRecordingBanner"
+ "showSavedToPhotosBannerWithPhotosURL:identifier:sessionID:completionHandler:"
+ "startRecordingCountdown"
+ "stopCurrentSession"
+ "stopRecordingCalled"
+ "updateTimer:"
+ "userInitiated"
+ "v16@?0@\"<BSServiceConnectionConfiguring>\"8"
+ "v16@?0@\"BSServiceConnection<BSServiceConnectionContext>\"8"

```
