## CarPlay

> `/System/Library/Frameworks/CarPlay.framework/CarPlay`

```diff

-474.4.2.0.0
-  __TEXT.__text: 0x46c04
-  __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_methlist: 0x7170
+479.3.0.0.0
+  __TEXT.__text: 0x483e8
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_methlist: 0x7278
   __TEXT.__const: 0x238
-  __TEXT.__cstring: 0x3b29
-  __TEXT.__oslogstring: 0x1e29
-  __TEXT.__gcc_except_tab: 0x808
-  __TEXT.__unwind_info: 0x1718
-  __TEXT.__objc_classname: 0xfca
-  __TEXT.__objc_methname: 0xe488
-  __TEXT.__objc_methtype: 0x221c
-  __TEXT.__objc_stubs: 0x8ce0
-  __DATA_CONST.__got: 0x5f0
-  __DATA_CONST.__const: 0x1ae8
-  __DATA_CONST.__objc_classlist: 0x320
+  __TEXT.__cstring: 0x3d04
+  __TEXT.__oslogstring: 0x1f64
+  __TEXT.__gcc_except_tab: 0x884
+  __TEXT.__unwind_info: 0x1768
+  __TEXT.__objc_classname: 0xfdf
+  __TEXT.__objc_methname: 0xe5e0
+  __TEXT.__objc_methtype: 0x225e
+  __TEXT.__objc_stubs: 0x8da0
+  __DATA_CONST.__got: 0x5f8
+  __DATA_CONST.__const: 0x1b38
+  __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x30c8
+  __DATA_CONST.__objc_selrefs: 0x3110
   __DATA_CONST.__objc_protorefs: 0x108
-  __DATA_CONST.__objc_superrefs: 0x288
-  __AUTH_CONST.__auth_got: 0x350
-  __AUTH_CONST.__const: 0x8a0
-  __AUTH_CONST.__cfstring: 0x3dc0
-  __AUTH_CONST.__objc_const: 0x1a188
+  __DATA_CONST.__objc_superrefs: 0x290
+  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__const: 0x8c0
+  __AUTH_CONST.__cfstring: 0x3e80
+  __AUTH_CONST.__objc_const: 0x1a3d8
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0x768
+  __AUTH.__objc_data: 0x500
+  __DATA.__objc_ivar: 0x78c
   __DATA.__data: 0x1980
-  __DATA.__bss: 0x228
+  __DATA.__bss: 0x238
   __DATA_DIRTY.__objc_data: 0x1a90
   __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
   - /System/Library/PrivateFrameworks/CarKitNavigation.framework/CarKitNavigation
   - /System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices
+  - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6EB88C52-D986-3BEC-B2B7-012EA1EFA638
-  Functions: 2410
-  Symbols:   8943
-  CStrings:  4036
+  UUID: 96366AEC-E449-3A56-9770-E26D1AC7928F
+  Functions: 2441
+  Symbols:   9040
+  CStrings:  4088
 
Symbols:
+ +[CPListImageRowItemCardElement convertImage:showsImageFullHeight:]
+ -[CPListImageRowItem elementType]
+ -[CPListImageRowItemCardElement initWithImage:showsImageFullHeight:title:subtitle:tintColor:]
+ -[CPListImageRowItemCardElement showsImageFullHeight]
+ -[CPListImageRowItemImageGridElement .cxx_destruct]
+ -[CPListImageRowItemImageGridElement accessorySymbolName]
+ -[CPListImageRowItemImageGridElement initWithImage:imageShape:title:accessorySymbolName:]
+ -[CPListImageRowItemImageGridElement setAccessorySymbolName:]
+ -[CPListImageRowItemImageGridElement setTitle:]
+ -[CPListImageRowItemImageGridElement title]
+ -[CPNavigationManager stateCaptures]
+ -[CPTextButton associatedTemplate]
+ -[CPTextButton setAssociatedTemplate:]
+ -[CYStateCapture .cxx_destruct]
+ -[CYStateCapture capture]
+ -[CYStateCapture dealloc]
+ -[CYStateCapture description]
+ -[CYStateCapture handler]
+ -[CYStateCapture identifier]
+ -[CYStateCapture initWithIdentifier:capture:]
+ -[CYStateCapture queue]
+ -[CYStateCapture setCapture:]
+ -[CYStateCapture setHandler:]
+ -[CYStateCapture setQueue:]
+ -[CYStateCapture stateCapture]
+ -[CYStateCapture stateCapture].cold.1
+ -[CYStateCapture stateCapture].cold.2
+ -[CYStateCapture stateCapture].cold.3
+ GCC_except_table60
+ _CarPlayFrameworkStateCaptureLogging
+ _CarPlayFrameworkStateCaptureLogging.cold.1
+ _CarPlayFrameworkStateCaptureLogging.facility
+ _CarPlayFrameworkStateCaptureLogging.onceToken
+ _OBJC_CLASS_$_CYStateCapture
+ _OBJC_IVAR_$_CPListImageRowItem._elementType
+ _OBJC_IVAR_$_CPListImageRowItemCardElement._showsImageFullHeight
+ _OBJC_IVAR_$_CPListImageRowItemImageGridElement._accessorySymbolName
+ _OBJC_IVAR_$_CPListImageRowItemImageGridElement._title
+ _OBJC_IVAR_$_CPNavigationManager._stateCaptures
+ _OBJC_IVAR_$_CPTextButton._associatedTemplate
+ _OBJC_IVAR_$_CYStateCapture._capture
+ _OBJC_IVAR_$_CYStateCapture._handler
+ _OBJC_IVAR_$_CYStateCapture._identifier
+ _OBJC_IVAR_$_CYStateCapture._queue
+ _OBJC_METACLASS_$_CYStateCapture
+ _OPACKEncoderCreateData
+ __OBJC_$_INSTANCE_METHODS_CYStateCapture
+ __OBJC_$_INSTANCE_VARIABLES_CYStateCapture
+ __OBJC_$_PROP_LIST_CYStateCapture
+ __OBJC_CLASS_RO_$_CYStateCapture
+ __OBJC_METACLASS_RO_$_CYStateCapture
+ ___39-[CPNavigationManager _setupConnection]_block_invoke.121
+ ___39-[CPNavigationManager _setupConnection]_block_invoke.122
+ ___39-[CPNavigationManager _setupConnection]_block_invoke.124
+ ___45-[CYStateCapture initWithIdentifier:capture:]_block_invoke
+ ___49-[CPNavigationManager didUpdateActiveComponents:]_block_invoke.133
+ ___51-[CPNavigationManager initWithIdentifier:delegate:]_block_invoke.74
+ ___51-[CPNavigationManager initWithIdentifier:delegate:]_block_invoke.74.cold.1
+ ___51-[CPNavigationManager initWithIdentifier:delegate:]_block_invoke.81
+ ___51-[CPNavigationManager initWithIdentifier:delegate:]_block_invoke.81.cold.1
+ ___67+[CPListImageRowItemCardElement convertImage:showsImageFullHeight:]_block_invoke
+ ___CarPlayFrameworkStateCaptureLogging_block_invoke
+ ___block_descriptor_40_e8_32w_e103_^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16?0^{os_state_hints_s=I*II}8lw32l8
+ ___block_descriptor_40_e8_32w_e5_8?0lw32l8
+ ___block_literal_global.101
+ ___block_literal_global.107
+ ___block_literal_global.109
+ ___block_literal_global.112
+ ___block_literal_global.116
+ ___block_literal_global.127
+ ___block_literal_global.181
+ ___block_literal_global.6
+ ___block_literal_global.94
+ ___block_literal_global.99
+ ___strlcpy_chk
+ _class_getName
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _malloc_type_calloc
+ _memcpy
+ _objc_msgSend$bytes
+ _objc_msgSend$capture
+ _objc_msgSend$convertImage:showsImageFullHeight:
+ _objc_msgSend$dictionaryStringFormat:
+ _objc_msgSend$initWithIdentifier:capture:
+ _objc_msgSend$setEnabled:
+ _objc_msgSend$showsImageFullHeight
+ _objc_msgSend$stateCapture
+ _os_state_add_handler
+ _os_state_remove_handler
- +[CPListImageRowItemCardElement convertImage:showImageFullHeight:]
- -[CPListImageRowItemCardElement initWithImage:showImageFullHeight:title:subtitle:tintColor:]
- -[CPListImageRowItemCardElement showImageFullHeight]
- -[CPListImageRowItemImageGridElement initWithImage:imageShape:]
- GCC_except_table58
- _OBJC_IVAR_$_CPListImageRowItemCardElement._showImageFullHeight
- ___39-[CPNavigationManager _setupConnection]_block_invoke.109
- ___39-[CPNavigationManager _setupConnection]_block_invoke.110
- ___39-[CPNavigationManager _setupConnection]_block_invoke.112
- ___49-[CPNavigationManager didUpdateActiveComponents:]_block_invoke.121
- ___65-[CPListImageRowItem _populateElementsFromImages:andImageTitles:]_block_invoke
- ___66+[CPListImageRowItemCardElement convertImage:showImageFullHeight:]_block_invoke
- ___block_literal_global.100
- ___block_literal_global.102
- ___block_literal_global.115
- ___block_literal_global.169
- ___block_literal_global.81
- ___block_literal_global.84
- ___block_literal_global.86
- ___block_literal_global.89
- ___block_literal_global.92
- ___block_literal_global.95
- _objc_msgSend$convertImage:showImageFullHeight:
- _objc_msgSend$showImageFullHeight
CStrings:
+ "%@ %s"
+ "%@ Error serializing dictionary for State Capture: %d"
+ "%@ captured state data.length=%lu"
+ "%@ failed to create state"
+ "%@ got called os_state_add_handler"
+ "%@ over data limit, length=%lu"
+ "-[CPNavigationManager dealloc]"
+ "-[CPNavigationManager invalidate]"
+ "-[CYStateCapture dealloc]"
+ "-[CYStateCapture initWithIdentifier:capture:]"
+ "<%@: %p identifier=%@>"
+ "@56@0:8@16q24@32@40@48"
+ "@8@?0"
+ "CYStateCapture"
+ "LaneGuidances"
+ "Maneuvers"
+ "R"
+ "StateCapture"
+ "T#,R,N,V_elementType"
+ "T@\"NSArray\",R,N,V_stateCaptures"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T@\"NSString\",R,N,V_identifier"
+ "T@?,C,N,V_capture"
+ "TB,R,N,V_showsImageFullHeight"
+ "TQ,N,V_handler"
+ "Tq,R,N,V_imageShape"
+ "[StateCapture] capturing %ld laneGuidances"
+ "[StateCapture] capturing %ld maneuvers"
+ "[StateCapture] disabled"
+ "[StateCapture] enabled"
+ "^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@0:8"
+ "^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8"
+ "_capture"
+ "_elementType"
+ "_queue"
+ "_showsImageFullHeight"
+ "_stateCaptures"
+ "bytes"
+ "capture"
+ "caraccessoryd"
+ "com.apple.caraccessoryframework.StateCapture-%@-%p"
+ "convertImage:showsImageFullHeight:"
+ "elementType"
+ "initWithIdentifier:capture:"
+ "initWithImage:imageShape:title:accessorySymbolName:"
+ "initWithImage:showsImageFullHeight:title:subtitle:tintColor:"
+ "kCPListImageRowItemCardElementShowsImageFullHeightKey"
+ "kCPListImageRowItemImageGridElementAccessorySymbolNameKey"
+ "kCPListImageRowItemImageGridElementTitleKey"
+ "queue"
+ "setCapture:"
+ "setQueue:"
+ "showsImageFullHeight"
+ "stateCapture"
+ "stateCaptures"
+ "\x81"
- "@32@0:8@16Q24"
- "@56@0:8@16Q24@32@40@48"
- "TB,R,N,V_showImageFullHeight"
- "TQ,R,N,V_imageShape"
- "_showImageFullHeight"
- "convertImage:showImageFullHeight:"
- "initWithImage:imageShape:"
- "initWithImage:showImageFullHeight:title:subtitle:tintColor:"
- "kCPListImageRowItemCardElementShowImageFullHeightKey"
- "showImageFullHeight"

```
