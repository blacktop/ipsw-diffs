## BrowserEngineKit

> `/System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit`

```diff

-7622.1.15.0.0
-  __TEXT.__text: 0x1ce98
+7622.1.18.3.0
+  __TEXT.__text: 0x1d440
   __TEXT.__auth_stubs: 0x10e0
-  __TEXT.__objc_methlist: 0x1770
-  __TEXT.__const: 0xf16
+  __TEXT.__objc_methlist: 0x1838
+  __TEXT.__const: 0xf26
   __TEXT.__cstring: 0xfbb
   __TEXT.__oslogstring: 0x6cb
   __TEXT.__swift5_typeref: 0x6dc
-  __TEXT.__swift5_capture: 0x44c
+  __TEXT.__swift5_capture: 0x46c
   __TEXT.__swift5_fieldmd: 0x57c
   __TEXT.__constg_swiftt: 0xa38
   __TEXT.__swift5_reflstr: 0x3d2

   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift_as_entry: 0x54
   __TEXT.__swift_as_ret: 0x50
-  __TEXT.__unwind_info: 0x9f8
+  __TEXT.__unwind_info: 0x9f0
   __TEXT.__eh_frame: 0xe50
-  __TEXT.__objc_classname: 0x2d0
-  __TEXT.__objc_methname: 0x3a29
-  __TEXT.__objc_methtype: 0xed5
-  __TEXT.__objc_stubs: 0x11e0
-  __DATA_CONST.__got: 0x350
+  __TEXT.__objc_classname: 0x32e
+  __TEXT.__objc_methname: 0x3bc4
+  __TEXT.__objc_methtype: 0xf1d
+  __TEXT.__objc_stubs: 0x12a0
+  __DATA_CONST.__got: 0x360
   __DATA_CONST.__const: 0x1c8
-  __DATA_CONST.__objc_classlist: 0xf0
+  __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x98
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1038
+  __DATA_CONST.__objc_selrefs: 0x10a0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x88
+  __DATA_CONST.__objc_superrefs: 0x98
   __AUTH_CONST.__auth_got: 0x878
-  __AUTH_CONST.__const: 0xfd0
+  __AUTH_CONST.__const: 0x1020
   __AUTH_CONST.__cfstring: 0x340
-  __AUTH_CONST.__objc_const: 0x35a0
-  __AUTH.__objc_data: 0x860
+  __AUTH_CONST.__objc_const: 0x3aa0
+  __AUTH.__objc_data: 0x900
   __AUTH.__data: 0x1d0
-  __DATA.__objc_ivar: 0xa0
-  __DATA.__data: 0x748
+  __DATA.__objc_ivar: 0xac
+  __DATA.__data: 0x7a8
   __DATA.__bss: 0x9b0
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x6e0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3FE0FDA8-7973-3E41-812D-E3968061E85B
-  Functions: 909
-  Symbols:   1516
-  CStrings:  996
+  UUID: F53E53C7-CE4F-3592-B92A-FF1ACD94374B
+  Functions: 925
+  Symbols:   1577
+  CStrings:  1019
 
Symbols:
+ -[BEAccessibilityRemoteElement .cxx_destruct]
+ -[BEAccessibilityRemoteElement accessibilityRemoteSubstituteChildren:]
+ -[BEAccessibilityRemoteElement accessibilityViewIsModal]
+ -[BEAccessibilityRemoteElement backingElement]
+ -[BEAccessibilityRemoteElement initWithIdentifier:hostPid:]
+ -[BEAccessibilityRemoteHostElement .cxx_destruct]
+ -[BEAccessibilityRemoteHostElement accessibilityContainer]
+ -[BEAccessibilityRemoteHostElement accessibilityElements]
+ -[BEAccessibilityRemoteHostElement accessibilityViewIsModal]
+ -[BEAccessibilityRemoteHostElement backingElement]
+ -[BEAccessibilityRemoteHostElement initWithIdentifier:remotePid:]
+ -[BEAccessibilityRemoteHostElement isAccessibilityElement]
+ -[BEAccessibilityRemoteHostElement setAccessibilityContainer:]
+ _OBJC_CLASS_$_AXRemoteElement
+ _OBJC_CLASS_$_BEAccessibilityRemoteElement
+ _OBJC_CLASS_$_BEAccessibilityRemoteHostElement
+ _OBJC_CLASS_$_NSArray
+ _OBJC_IVAR_$_BEAccessibilityRemoteElement._remoteElementBacking
+ _OBJC_IVAR_$_BEAccessibilityRemoteHostElement._accessibilityContainer
+ _OBJC_IVAR_$_BEAccessibilityRemoteHostElement._remoteElementBacking
+ _OBJC_METACLASS_$_BEAccessibilityRemoteElement
+ _OBJC_METACLASS_$_BEAccessibilityRemoteHostElement
+ __OBJC_$_INSTANCE_METHODS_BEAccessibilityRemoteElement
+ __OBJC_$_INSTANCE_METHODS_BEAccessibilityRemoteHostElement
+ __OBJC_$_INSTANCE_VARIABLES_BEAccessibilityRemoteElement
+ __OBJC_$_INSTANCE_VARIABLES_BEAccessibilityRemoteHostElement
+ __OBJC_$_PROP_LIST_BEAccessibilityRemoteElement
+ __OBJC_$_PROP_LIST_BEAccessibilityRemoteHostElement
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AXRemoteElementChildrenDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AXRemoteElementChildrenDelegate
+ __OBJC_$_PROTOCOL_REFS_AXRemoteElementChildrenDelegate
+ __OBJC_CLASS_PROTOCOLS_$_BEAccessibilityRemoteElement
+ __OBJC_CLASS_RO_$_BEAccessibilityRemoteElement
+ __OBJC_CLASS_RO_$_BEAccessibilityRemoteHostElement
+ __OBJC_LABEL_PROTOCOL_$_AXRemoteElementChildrenDelegate
+ __OBJC_METACLASS_RO_$_BEAccessibilityRemoteElement
+ __OBJC_METACLASS_RO_$_BEAccessibilityRemoteHostElement
+ __OBJC_PROTOCOL_$_AXRemoteElementChildrenDelegate
+ _block_copy_helper.122
+ _block_copy_helper.143
+ _block_copy_helper.154
+ _block_descriptor.124
+ _block_descriptor.145
+ _block_descriptor.156
+ _block_destroy_helper.123
+ _block_destroy_helper.144
+ _block_destroy_helper.155
+ _objc_msgSend$accessibilityElements
+ _objc_msgSend$arrayWithObject:
+ _objc_msgSend$initWithUUID:andRemotePid:andContextId:
+ _objc_msgSend$setAccessibilityContainer:
+ _objc_msgSend$setOnClientSide:
+ _objc_msgSend$setRemoteChildrenDelegate:
+ _objectdestroy.127Tm
- _block_copy_helper.117
- _block_copy_helper.133
- _block_copy_helper.149
- _block_descriptor.119
- _block_descriptor.135
- _block_descriptor.151
- _block_destroy_helper.118
- _block_destroy_helper.134
- _block_destroy_helper.150
- _objectdestroy.122Tm
CStrings:
+ "@"
+ "@\"AXRemoteElement\""
+ "@\"NSArray\"24@0:8@\"AXRemoteElement\"16"
+ "@28@0:8@16i24"
+ "AXRemoteElementChildrenDelegate"
+ "BEAccessibilityRemoteElement"
+ "BEAccessibilityRemoteHostElement"
+ "T@,W,N,V_accessibilityContainer"
+ "_accessibilityContainer"
+ "_remoteElementBacking"
+ "accessibilityContainer"
+ "accessibilityElements"
+ "accessibilityRemoteSubstituteChildren:"
+ "accessibilityViewIsModal"
+ "arrayWithObject:"
+ "backingElement"
+ "initWithIdentifier:hostPid:"
+ "initWithIdentifier:remotePid:"
+ "initWithUUID:andRemotePid:andContextId:"
+ "isAccessibilityElement"
+ "setAccessibilityContainer:"
+ "setOnClientSide:"
+ "setRemoteChildrenDelegate:"

```
