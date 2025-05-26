## Portrait

> `/System/Library/PrivateFrameworks/Portrait.framework/Portrait`

```diff

-330.9.0.0.0
-  __TEXT.__text: 0x8fd54
-  __TEXT.__auth_stubs: 0x1140
-  __TEXT.__objc_methlist: 0x80ec
+334.7.0.0.0
+  __TEXT.__text: 0x90054
+  __TEXT.__auth_stubs: 0x1120
+  __TEXT.__objc_methlist: 0x810c
   __TEXT.__const: 0x21010
   __TEXT.__cstring: 0x739a
-  __TEXT.__oslogstring: 0x39dd
+  __TEXT.__oslogstring: 0x3a84
   __TEXT.__gcc_except_tab: 0x1ac
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x2048
-  __TEXT.__objc_classname: 0x110e
-  __TEXT.__objc_methname: 0x175ad
-  __TEXT.__objc_methtype: 0x4b70
-  __TEXT.__objc_stubs: 0xe0c0
+  __TEXT.__unwind_info: 0x2054
+  __TEXT.__objc_classname: 0x1110
+  __TEXT.__objc_methname: 0x17665
+  __TEXT.__objc_methtype: 0x4b9b
+  __TEXT.__objc_stubs: 0xe140
   __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__const: 0x670
   __DATA_CONST.__objc_classlist: 0x4c8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x15b78
-  __DATA_CONST.__objc_selrefs: 0x46b0
+  __DATA_CONST.__objc_const: 0x15c10
+  __DATA_CONST.__objc_selrefs: 0x46d0
   __DATA_CONST.__objc_arraydata: 0x5c0
   __AUTH_CONST.__cfstring: 0x4960
-  __AUTH_CONST.__objc_const: 0x3900
+  __AUTH_CONST.__objc_const: 0x38b8
   __AUTH_CONST.__objc_arrayobj: 0x198
-  __AUTH_CONST.__objc_intobj: 0x7f8
+  __AUTH_CONST.__objc_intobj: 0x828
   __AUTH_CONST.__const: 0x2e0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x8b0
+  __AUTH_CONST.__auth_got: 0x8a0
   __AUTH.__objc_data: 0x2e90
   __AUTH.__data: 0xb80
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x650
   __DATA.__objc_superrefs: 0x438
-  __DATA.__objc_ivar: 0x141c
-  __DATA.__data: 0x6b0
-  __DATA.__bss: 0x1f4
+  __DATA.__objc_ivar: 0x1424
+  __DATA.__data: 0x6a8
+  __DATA.__bss: 0x1e4
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4010
-  Symbols:   13034
-  CStrings:  6150
+  Functions: 4022
+  Symbols:   13058
+  CStrings:  6162
 
Symbols:
+ -[PTEffect render:].cold.6
+ -[PTEffectRenderer render:humanDetections:waitUntilCompleted:gpuCompleted:].cold.11
+ -[PTMTLDropHintsInFlight _addResourceGroup:toCommandBuffer:].cold.1
+ -[PTMTLDropHintsInFlight _dropResourceGroup:fromCommandBuffer:].cold.1
+ -[PTMTLDropHintsInFlight _setActiveResourceGroups:]
+ -[PTMTLDropHintsInFlight _setActiveResourceGroups:].cold.1
+ -[PTMTLDropHintsInFlight checkForUnreleasedDrophints].cold.1
+ -[PTMTLDropHintsInFlight initWithDevice:]
+ -[PTMetalContext dropHintsInFlight]
+ -[PTMetalContext initWithCommandQueue:bundleClass:dropHints:]
+ -[PTMetalContext initWithCommandQueue:bundleClass:dropHints:].cold.1
+ -[PTMetalContext initWithCommandQueue:bundleClass:dropHints:].cold.2
+ -[PTMetalContext initWithCommandQueue:bundleClass:dropHints:].cold.3
+ -[PTMetalContext initWithCommandQueue:bundleClass:dropHints:].cold.4
+ -[PTMetalContext initWithCommandQueue:bundleClass:dropHints:].cold.5
+ -[PTMetalContext initWithCommandQueue:bundleClass:dropHints:].cold.6
+ -[PTMetalContext setDropHintsInFlight:]
+ _OBJC_IVAR_$_PTMTLDropHints._metalContext
+ _OBJC_IVAR_$_PTMetalContext._dropHintsInFlight
+ _objc_msgSend$_setActiveResourceGroups:
+ _objc_msgSend$dropHintsInFlight
+ _objc_msgSend$initWithCommandQueue:bundleClass:dropHints:
+ _objc_msgSend$initWithDevice:
+ _objc_msgSend$setDropHintsInFlight:
- +[PTMTLDropHintsInFlight instance:]
- -[PTMTLDropHintsInFlight init]
- -[PTMetalContext initWithCommandQueue:bundleClass:].cold.1
- -[PTMetalContext initWithCommandQueue:bundleClass:].cold.2
- -[PTMetalContext initWithCommandQueue:bundleClass:].cold.3
- -[PTMetalContext initWithCommandQueue:bundleClass:].cold.4
- -[PTMetalContext initWithCommandQueue:bundleClass:].cold.5
- -[PTMetalContext initWithCommandQueue:bundleClass:].cold.6
- __OBJC_$_CLASS_METHODS_PTMTLDropHintsInFlight
- ___35+[PTMTLDropHintsInFlight instance:]_block_invoke
- _dropHintsInFlightKey
- _instance:.once
- _isSupported
- _objc_getAssociatedObject
- _objc_msgSend$instance:
- _objc_setAssociatedObject
CStrings:
+ "\x16"
+ "@\"PTMTLDropHintsInFlight\""
+ "@36@0:8@16#24B32"
+ "T@\"PTMTLDropHintsInFlight\",&,N,V_dropHintsInFlight"
+ "Unreleased drop hints"
+ "_dropHintsInFlight"
+ "_setActiveResourceGroups:"
+ "addResourceGroup: active groups already contains resourceGroup"
+ "dropHintsInFlight"
+ "dropResourceGroup: active groups does not contain resourceGroup"
+ "initWithCommandQueue:bundleClass:dropHints:"
+ "initWithDevice:"
+ "setActiveResourceGroups: Out of bounds"
+ "setDropHintsInFlight:"
- "Disabling drop hints"
- "instance:"

```
