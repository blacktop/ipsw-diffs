## AccessibilityAudit

> `/System/Library/PrivateFrameworks/AccessibilityAudit.framework/AccessibilityAudit`

```diff

-165.2.0.0.0
-  __TEXT.__text: 0x1fe90
-  __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0x310c
-  __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x33df
+179.0.0.0.0
+  __TEXT.__text: 0x22594
+  __TEXT.__auth_stubs: 0x8f0
+  __TEXT.__objc_methlist: 0x3484
+  __TEXT.__const: 0x218
+  __TEXT.__cstring: 0x3809
   __TEXT.__gcc_except_tab: 0x120
-  __TEXT.__oslogstring: 0x3c1
-  __TEXT.__unwind_info: 0x998
-  __TEXT.__objc_classname: 0x578
-  __TEXT.__objc_methname: 0x73dc
-  __TEXT.__objc_methtype: 0x1132
-  __TEXT.__objc_stubs: 0x5580
-  __DATA_CONST.__got: 0x328
-  __DATA_CONST.__const: 0xcc0
-  __DATA_CONST.__objc_classlist: 0x198
+  __TEXT.__oslogstring: 0x4d9
+  __TEXT.__unwind_info: 0xa50
+  __TEXT.__objc_classname: 0x628
+  __TEXT.__objc_methname: 0x7a38
+  __TEXT.__objc_methtype: 0x1248
+  __TEXT.__objc_stubs: 0x58c0
+  __DATA_CONST.__got: 0x340
+  __DATA_CONST.__const: 0xde8
+  __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bf8
+  __DATA_CONST.__objc_selrefs: 0x1d68
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xe0
-  __DATA_CONST.__objc_arraydata: 0x378
-  __AUTH_CONST.__auth_got: 0x470
-  __AUTH_CONST.__const: 0x1160
-  __AUTH_CONST.__cfstring: 0x3580
-  __AUTH_CONST.__objc_const: 0x5178
+  __DATA_CONST.__objc_superrefs: 0xf0
+  __DATA_CONST.__objc_arraydata: 0x388
+  __AUTH_CONST.__auth_got: 0x488
+  __AUTH_CONST.__const: 0x1200
+  __AUTH_CONST.__cfstring: 0x3760
+  __AUTH_CONST.__objc_const: 0x56b8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x870
   __AUTH_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_ivar: 0x328
-  __DATA.__data: 0x488
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x35c
+  __DATA.__data: 0x608
   __DATA.__bss: 0x168
   __DATA_DIRTY.__objc_data: 0xff0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/Vision.framework/Vision
   - /System/Library/PrivateFrameworks/AXAssetLoader.framework/AXAssetLoader
+  - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime
+  - /System/Library/PrivateFrameworks/AccessibilityPlatformTranslation.framework/AccessibilityPlatformTranslation
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/DTXConnectionServices.framework/DTXConnectionServices
   - /System/Library/PrivateFrameworks/UIUnderstanding.framework/UIUnderstanding
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4B9CE148-4CFE-32D4-B901-FADE6E04F015
-  Functions: 1106
-  Symbols:   4088
-  CStrings:  2513
+  UUID: 41BAD3F1-AE43-3962-8EC0-005A042DD018
+  Functions: 1194
+  Symbols:   4358
+  CStrings:  2648
 
Symbols:
+ +[AXAuditInspectorSection identifierForType:]
+ +[AXAuditInspectorSection titleForType:]
+ -[AXAuditDevicesAppRemoteServer .cxx_destruct]
+ -[AXAuditDevicesAppRemoteServer accessibilityTranslationTransportAddReceiveDataHandler:]
+ -[AXAuditDevicesAppRemoteServer accessibilityTranslationTransportCancel]
+ -[AXAuditDevicesAppRemoteServer accessibilityTranslationTransportSendData:completionHandler:]
+ -[AXAuditDevicesAppRemoteServer axpTransportDataHandler]
+ -[AXAuditDevicesAppRemoteServer cancel]
+ -[AXAuditDevicesAppRemoteServer clientNeedsAccessibility:]
+ -[AXAuditDevicesAppRemoteServer clientNeedsAccessibility:].cold.1
+ -[AXAuditDevicesAppRemoteServer connectionInterrupted]
+ -[AXAuditDevicesAppRemoteServer connection]
+ -[AXAuditDevicesAppRemoteServer dealloc]
+ -[AXAuditDevicesAppRemoteServer deviceAPIVersion]
+ -[AXAuditDevicesAppRemoteServer hostAPIVersion]
+ -[AXAuditDevicesAppRemoteServer initWithTransport:]
+ -[AXAuditDevicesAppRemoteServer processDataFromHost:]
+ -[AXAuditDevicesAppRemoteServer processDataFromHost:].cold.1
+ -[AXAuditDevicesAppRemoteServer remoteCacheManager]
+ -[AXAuditDevicesAppRemoteServer requestHostAPIVersion]
+ -[AXAuditDevicesAppRemoteServer resume]
+ -[AXAuditDevicesAppRemoteServer setAxpTransportDataHandler:]
+ -[AXAuditDevicesAppRemoteServer setConnection:]
+ -[AXAuditDevicesAppRemoteServer setHostAPIVersion:]
+ -[AXAuditDevicesAppRemoteServer setMaxConnectionEnqueue:]
+ -[AXAuditDevicesAppRemoteServer setRemoteCacheManager:]
+ -[AXAuditInspectorSection allowsFilter]
+ -[AXAuditInspectorSection displaysHierarchy]
+ -[AXAuditInspectorSection hasActions]
+ -[AXAuditInspectorSection initWithType:]
+ -[AXAuditInspectorSection setAllowsFilter:]
+ -[AXAuditRemoteDevice .cxx_destruct]
+ -[AXAuditRemoteDevice _degree1:isAlmostEqualTo:]
+ -[AXAuditRemoteDevice _setupConnectionForFileDescriptor:]
+ -[AXAuditRemoteDevice accessibilityHostCacheManagerDeviceOrientationForDeviceIdentifier:]
+ -[AXAuditRemoteDevice accessibilityTranslationTransportAddReceiveDataHandler:]
+ -[AXAuditRemoteDevice accessibilityTranslationTransportCancel]
+ -[AXAuditRemoteDevice accessibilityTranslationTransportSendData:completionHandler:]
+ -[AXAuditRemoteDevice axpTransportDataHandler]
+ -[AXAuditRemoteDevice byteFormatter]
+ -[AXAuditRemoteDevice completeConnection]
+ -[AXAuditRemoteDevice connection]
+ -[AXAuditRemoteDevice delegate]
+ -[AXAuditRemoteDevice deviceAPIVersion]
+ -[AXAuditRemoteDevice deviceID]
+ -[AXAuditRemoteDevice deviceOrientation]
+ -[AXAuditRemoteDevice deviceSize]
+ -[AXAuditRemoteDevice didDisconnect]
+ -[AXAuditRemoteDevice hostAPIVersion]
+ -[AXAuditRemoteDevice initWithFileDescriptor:identifier:deviceSize:]
+ -[AXAuditRemoteDevice initWithFileDescriptor:identifier:deviceSize:].cold.1
+ -[AXAuditRemoteDevice notifyDelegateOfConnectionCompletionIfNecessary]
+ -[AXAuditRemoteDevice orientationChangedToDegrees:]
+ -[AXAuditRemoteDevice processDataFromRemoteDevice:]
+ -[AXAuditRemoteDevice processDataFromRemoteDevice:].cold.1
+ -[AXAuditRemoteDevice requestDeviceAPIVersion]
+ -[AXAuditRemoteDevice setAxpTransportDataHandler:]
+ -[AXAuditRemoteDevice setByteFormatter:]
+ -[AXAuditRemoteDevice setConnection:]
+ -[AXAuditRemoteDevice setDelegate:]
+ -[AXAuditRemoteDevice setDeviceAPIVersion:]
+ -[AXAuditRemoteDevice setDeviceID:]
+ -[AXAuditRemoteDevice setDeviceOrientation:]
+ -[AXAuditRemoteDevice setDeviceSize:]
+ -[AXAuditRemoteDevice startAccessibility]
+ -[AXAuditRemoteDevice stopAccessibility]
+ _OBJC_CLASS_$_AXAuditDevicesAppRemoteServer
+ _OBJC_CLASS_$_AXAuditRemoteDevice
+ _OBJC_CLASS_$_AXPRemoteCacheManager
+ _OBJC_CLASS_$_DTXSocketTransport
+ _OBJC_CLASS_$_NSByteCountFormatter
+ _OBJC_IVAR_$_AXAuditDevicesAppRemoteServer._axpTransportDataHandler
+ _OBJC_IVAR_$_AXAuditDevicesAppRemoteServer._connection
+ _OBJC_IVAR_$_AXAuditDevicesAppRemoteServer._hostAPIVersion
+ _OBJC_IVAR_$_AXAuditDevicesAppRemoteServer._remoteCacheManager
+ _OBJC_IVAR_$_AXAuditInspectorSection._allowsFilter
+ _OBJC_IVAR_$_AXAuditRemoteDevice._axpTransportDataHandler
+ _OBJC_IVAR_$_AXAuditRemoteDevice._byteFormatter
+ _OBJC_IVAR_$_AXAuditRemoteDevice._connection
+ _OBJC_IVAR_$_AXAuditRemoteDevice._delegate
+ _OBJC_IVAR_$_AXAuditRemoteDevice._deviceAPIVersion
+ _OBJC_IVAR_$_AXAuditRemoteDevice._deviceID
+ _OBJC_IVAR_$_AXAuditRemoteDevice._deviceOrientation
+ _OBJC_IVAR_$_AXAuditRemoteDevice._deviceSize
+ _OBJC_METACLASS_$_AXAuditDevicesAppRemoteServer
+ _OBJC_METACLASS_$_AXAuditRemoteDevice
+ __OBJC_$_INSTANCE_METHODS_AXAuditDevicesAppRemoteServer
+ __OBJC_$_INSTANCE_METHODS_AXAuditRemoteDevice
+ __OBJC_$_INSTANCE_VARIABLES_AXAuditDevicesAppRemoteServer
+ __OBJC_$_INSTANCE_VARIABLES_AXAuditRemoteDevice
+ __OBJC_$_PROP_LIST_AXAuditDevicesAppRemoteServer
+ __OBJC_$_PROP_LIST_AXAuditRemoteDevice
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AXAuditRemoteDeviceAPIDevice
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AXAuditRemoteDeviceAPIHost
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AXPTranslationTransportCancellable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AXPTranslationTransportDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AXAuditRemoteDeviceAPIDevice
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AXAuditRemoteDeviceAPIHost
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AXPTranslationTransportCancellable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AXPTranslationTransportDelegate
+ __OBJC_$_PROTOCOL_REFS_AXAuditRemoteDeviceAPIDevice
+ __OBJC_$_PROTOCOL_REFS_AXAuditRemoteDeviceAPIHost
+ __OBJC_$_PROTOCOL_REFS_AXPTranslationTransportCancellable
+ __OBJC_$_PROTOCOL_REFS_AXPTranslationTransportDelegate
+ __OBJC_CLASS_PROTOCOLS_$_AXAuditDevicesAppRemoteServer
+ __OBJC_CLASS_PROTOCOLS_$_AXAuditRemoteDevice
+ __OBJC_CLASS_RO_$_AXAuditDevicesAppRemoteServer
+ __OBJC_CLASS_RO_$_AXAuditRemoteDevice
+ __OBJC_LABEL_PROTOCOL_$_AXAuditRemoteDeviceAPIDevice
+ __OBJC_LABEL_PROTOCOL_$_AXAuditRemoteDeviceAPIHost
+ __OBJC_LABEL_PROTOCOL_$_AXPTranslationTransportCancellable
+ __OBJC_LABEL_PROTOCOL_$_AXPTranslationTransportDelegate
+ __OBJC_METACLASS_RO_$_AXAuditDevicesAppRemoteServer
+ __OBJC_METACLASS_RO_$_AXAuditRemoteDevice
+ __OBJC_PROTOCOL_$_AXAuditRemoteDeviceAPIDevice
+ __OBJC_PROTOCOL_$_AXAuditRemoteDeviceAPIHost
+ __OBJC_PROTOCOL_$_AXPTranslationTransportCancellable
+ __OBJC_PROTOCOL_$_AXPTranslationTransportDelegate
+ ___40-[AXAuditRemoteDevice stopAccessibility]_block_invoke
+ ___40-[AXAuditRemoteDevice stopAccessibility]_block_invoke.cold.1
+ ___41-[AXAuditRemoteDevice startAccessibility]_block_invoke
+ ___41-[AXAuditRemoteDevice startAccessibility]_block_invoke_2
+ ___41-[AXAuditRemoteDevice startAccessibility]_block_invoke_2.cold.1
+ ___46-[AXAuditRemoteDevice requestDeviceAPIVersion]_block_invoke
+ ___46-[AXAuditRemoteDevice requestDeviceAPIVersion]_block_invoke_2
+ ___46-[AXAuditRemoteDevice requestDeviceAPIVersion]_block_invoke_2.cold.1
+ ___51-[AXAuditDevicesAppRemoteServer initWithTransport:]_block_invoke
+ ___51-[AXAuditDevicesAppRemoteServer initWithTransport:]_block_invoke.2
+ ___51-[AXAuditDevicesAppRemoteServer initWithTransport:]_block_invoke.2.cold.1
+ ___51-[AXAuditRemoteDevice processDataFromRemoteDevice:]_block_invoke
+ ___53-[AXAuditDevicesAppRemoteServer processDataFromHost:]_block_invoke
+ ___54-[AXAuditDevicesAppRemoteServer requestHostAPIVersion]_block_invoke
+ ___54-[AXAuditDevicesAppRemoteServer requestHostAPIVersion]_block_invoke_2
+ ___57-[AXAuditRemoteDevice _setupConnectionForFileDescriptor:]_block_invoke
+ ___66+[AXAuditInspectorSection registerTransportableObjectWithManager:]_block_invoke_7
+ ___66+[AXAuditInspectorSection registerTransportableObjectWithManager:]_block_invoke_8
+ ___83-[AXAuditRemoteDevice accessibilityTranslationTransportSendData:completionHandler:]_block_invoke
+ ___83-[AXAuditRemoteDevice accessibilityTranslationTransportSendData:completionHandler:]_block_invoke_2
+ ___93-[AXAuditDevicesAppRemoteServer accessibilityTranslationTransportSendData:completionHandler:]_block_invoke
+ ___93-[AXAuditDevicesAppRemoteServer accessibilityTranslationTransportSendData:completionHandler:]_block_invoke_2
+ ___block_descriptor_32_e20_v16?0"DTXMessage"8l
+ ___block_descriptor_32_e36_v32?0"DTXChannel"8"NSString"16#24l
+ ___block_descriptor_32_e43_"NSNumber"16?0"AXAuditInspectorSection"8l
+ ___block_descriptor_36_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e20_v16?0"DTXMessage"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_literal_global.63
+ ___block_literal_global.65
+ ___block_literal_global.74
+ _close
+ _dup
+ _objc_msgSend$_degree1:isAlmostEqualTo:
+ _objc_msgSend$_setupConnectionForFileDescriptor:
+ _objc_msgSend$allowsFilter
+ _objc_msgSend$axpTransportDataHandler
+ _objc_msgSend$colorWithAlphaComponent:
+ _objc_msgSend$completeConnection
+ _objc_msgSend$deviceAPIVersion
+ _objc_msgSend$deviceID
+ _objc_msgSend$deviceOrientation
+ _objc_msgSend$error
+ _objc_msgSend$identifierForType:
+ _objc_msgSend$initWithCachedTreeClientType:
+ _objc_msgSend$initWithConnectedSocket:disconnectAction:
+ _objc_msgSend$notifyDelegateOfConnectionCompletionIfNecessary
+ _objc_msgSend$remoteCacheManager
+ _objc_msgSend$remoteDeviceDidCompleteConnection
+ _objc_msgSend$requestDeviceAPIVersion
+ _objc_msgSend$setAllowsFilter:
+ _objc_msgSend$setAxpTransportDataHandler:
+ _objc_msgSend$setConnection:
+ _objc_msgSend$setDeviceAPIVersion:
+ _objc_msgSend$setDeviceOrientation:
+ _objc_msgSend$setRemoteCacheManager:
+ _objc_msgSend$setTransportDelegate:
+ _objc_msgSend$systemGreenColor
+ _objc_msgSend$titleForType:
+ _objc_release_x2
- -[AXAuditInspectorSection init]
CStrings:
+ "%s, needsAX: %@"
+ "%s: DTXMessageErrorStatus_ConnectionInterrupted"
+ "%s: axpTransportDataHandler is nil!"
+ "%s: error: %u, %@"
+ "%s: failed to set up connection with file descriptor"
+ "-[AXAuditDevicesAppRemoteServer cancel]"
+ "-[AXAuditDevicesAppRemoteServer clientNeedsAccessibility:]"
+ "-[AXAuditDevicesAppRemoteServer connectionInterrupted]"
+ "-[AXAuditDevicesAppRemoteServer dealloc]"
+ "-[AXAuditDevicesAppRemoteServer initWithTransport:]_block_invoke"
+ "-[AXAuditDevicesAppRemoteServer processDataFromHost:]"
+ "-[AXAuditDevicesAppRemoteServer resume]"
+ "-[AXAuditRemoteDevice _setupConnectionForFileDescriptor:]"
+ "-[AXAuditRemoteDevice didDisconnect]"
+ "-[AXAuditRemoteDevice initWithFileDescriptor:identifier:deviceSize:]"
+ "-[AXAuditRemoteDevice processDataFromRemoteDevice:]"
+ "-[AXAuditRemoteDevice requestDeviceAPIVersion]_block_invoke_2"
+ "-[AXAuditRemoteDevice startAccessibility]_block_invoke_2"
+ "-[AXAuditRemoteDevice stopAccessibility]_block_invoke"
+ "/documentation/appkit/nsaccessibilitylayoutarea/accessibilityfocuseduielement"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilityactivationpoint()"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilitychildren()"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilitychildreninnavigationorder()"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilityextrasmenubar()"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilityfocusedwindow()"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilityframe()"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilityhelp()"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilitylabel()"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilitymainwindow()"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilitymenubar()"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilityparent()"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilityperformpress()"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilityperformshowmenu()"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilityrole()"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilityroledescription()"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilitysubrole()"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilitytitle()"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilitytopleveluielement()"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilityurl()"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilityvalue()"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilitywindow()"
+ "/documentation/appkit/nsaccessibilityprotocol/accessibilitywindows()"
+ "/documentation/appkit/nsaccessibilityprotocol/isaccessibilityenabled()"
+ "/documentation/appkit/nsaccessibilityprotocol/isaccessibilityfocused()"
+ "/documentation/appkit/nsaccessibilityprotocol/isaccessibilityfrontmost()"
+ "/documentation/appkit/nsaccessibilityprotocol/isaccessibilityhidden()"
+ "@\"<AXAuditRemoteDeviceDelegate>\""
+ "@\"<AXPTranslationTransportCancellable>\"24@0:8@?<v@?@\"NSData\"@\"NSString\">16"
+ "@\"AXPRemoteCacheManager\""
+ "@\"NSByteCountFormatter\""
+ "@\"NSNumber\"16@?0@\"AXAuditInspectorSection\"8"
+ "@24@0:8@?16"
+ "@44@0:8i16@20{CGSize=dd}28"
+ "AXAuditDevicesAppRemoteServer"
+ "AXAuditRemoteDevice"
+ "AXAuditRemoteDeviceAPIDevice"
+ "AXAuditRemoteDeviceAPIHost"
+ "AXIdentifier"
+ "AXPTranslationTransportCancellable"
+ "AXPTranslationTransportDelegate"
+ "Actions"
+ "Actions_v1"
+ "Advanced"
+ "Advanced_iOS_v1"
+ "Advanced_v1"
+ "AllowsFilter_v1"
+ "B20@0:8i16"
+ "B32@0:8d16d24"
+ "Basic"
+ "Basic_v1"
+ "Catalyst"
+ "Could not create service named %@"
+ "Element"
+ "Element_v1"
+ "Hierarchy"
+ "Hierarchy_v1"
+ "T@\"<AXAuditRemoteDeviceDelegate>\",W,N,V_delegate"
+ "T@\"AXPRemoteCacheManager\",&,N,V_remoteCacheManager"
+ "T@\"DTXConnection\",&,N,V_connection"
+ "T@\"NSByteCountFormatter\",&,N,V_byteFormatter"
+ "T@\"NSString\",&,N,V_deviceID"
+ "T@?,C,N,V_axpTransportDataHandler"
+ "TB,N,V_allowsFilter"
+ "TB,R,N"
+ "Tq,N,V_deviceAPIVersion"
+ "Tq,N,V_deviceOrientation"
+ "Tq,N,V_hostAPIVersion"
+ "T{CGSize=dd},N,V_deviceSize"
+ "_allowsFilter"
+ "_axpTransportDataHandler"
+ "_byteFormatter"
+ "_degree1:isAlmostEqualTo:"
+ "_deviceAPIVersion"
+ "_deviceID"
+ "_deviceOrientation"
+ "_deviceSize"
+ "_remoteCacheManager"
+ "_setupConnectionForFileDescriptor:"
+ "accessibilityHostCacheManagerDeviceOrientationForDeviceIdentifier:"
+ "accessibilityTranslationTransportAddReceiveDataHandler:"
+ "accessibilityTranslationTransportCancel"
+ "accessibilityTranslationTransportSendData:completionHandler:"
+ "allowsFilter"
+ "axpTransportDataHandler"
+ "byteFormatter"
+ "clientNeedsAccessibility:"
+ "colorWithAlphaComponent:"
+ "com.apple.AXAuditDevicesAppRemoteServer"
+ "completeConnection"
+ "could not call initWithCachedTreeClientType, mac build is probably too old"
+ "deviceAPIVersion"
+ "deviceID"
+ "deviceOrientation"
+ "deviceSize"
+ "didDisconnect"
+ "displaysHierarchy"
+ "error"
+ "hasActions"
+ "identifierForType:"
+ "initWithCachedTreeClientType:"
+ "initWithConnectedSocket:disconnectAction:"
+ "initWithFileDescriptor:identifier:deviceSize:"
+ "initWithType:"
+ "notifyDelegateOfConnectionCompletionIfNecessary"
+ "orientationChangedToDegrees:"
+ "processDataFromHost:"
+ "processDataFromRemoteDevice:"
+ "remoteCacheManager"
+ "remoteDeviceDidCompleteConnection"
+ "requestDeviceAPIVersion"
+ "setAllowsFilter:"
+ "setAxpTransportDataHandler:"
+ "setByteFormatter:"
+ "setConnection:"
+ "setDeviceAPIVersion:"
+ "setDeviceID:"
+ "setDeviceOrientation:"
+ "setDeviceSize:"
+ "setRemoteCacheManager:"
+ "setTransportDelegate:"
+ "startAccessibility"
+ "stopAccessibility"
+ "systemGreenColor"
+ "titleForType:"
+ "v24@0:8@\"NSData\"16"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
- "/documentation/appkit/nsaccessibility/1526358-accessibilityperformpress"
- "/documentation/appkit/nsaccessibility/1532774-accessibilityperformshowmenu"
- "/documentation/appkit/nsaccessibility/1534939-accessibilityframe"
- "/documentation/appkit/nsaccessibility/1534961-accessibilityhidden"
- "/documentation/appkit/nsaccessibility/1534974-accessibilityhelp"
- "/documentation/appkit/nsaccessibility/1534976-accessibilitylabel"
- "/documentation/appkit/nsaccessibility/1534986-accessibilityfocusedwindow"
- "/documentation/appkit/nsaccessibility/1534994-accessibilityfocused"
- "/documentation/appkit/nsaccessibility/1534996-accessibilityextrasmenubar"
- "/documentation/appkit/nsaccessibility/1535005-accessibilityrole"
- "/documentation/appkit/nsaccessibility/1535018-accessibilitychildren"
- "/documentation/appkit/nsaccessibility/1535024-accessibilityenabled"
- "/documentation/appkit/nsaccessibility/1535030-accessibilitywindow"
- "/documentation/appkit/nsaccessibility/1535033-accessibilitytitle"
- "/documentation/appkit/nsaccessibility/1535040-accessibilityparent"
- "/documentation/appkit/nsaccessibility/1535055-accessibilitymenubar"
- "/documentation/appkit/nsaccessibility/1535070-accessibilitysubrole"
- "/documentation/appkit/nsaccessibility/1535073-accessibilityfrontmost"
- "/documentation/appkit/nsaccessibility/1535092-accessibilitytopleveluielement"
- "/documentation/appkit/nsaccessibility/1535103-accessibilityvalue"
- "/documentation/appkit/nsaccessibility/1535117-accessibilitywindows"
- "/documentation/appkit/nsaccessibility/1535138-accessibilitymainwindow"
- "/documentation/appkit/nsaccessibility/1535144-accessibilityroledescription"
- "/documentation/appkit/nsaccessibility/1535149-accessibilityactivationpoint"
- "/documentation/appkit/nsaccessibility/1535157-accessibilityurl"
- "/documentation/appkit/nsaccessibility/2869552-accessibilitychildreninnavigatio"
- "/documentation/appkit/nsaccessibilitylayoutarea/1533902-accessibilityfocuseduielement"

```
