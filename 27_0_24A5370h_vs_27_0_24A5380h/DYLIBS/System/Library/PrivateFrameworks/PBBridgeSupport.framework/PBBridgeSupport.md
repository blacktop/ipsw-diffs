## PBBridgeSupport

> `/System/Library/PrivateFrameworks/PBBridgeSupport.framework/PBBridgeSupport`

```diff

-  __TEXT.__text: 0x435d4
-  __TEXT.__objc_methlist: 0x513c
+  __TEXT.__text: 0x435d8
+  __TEXT.__objc_methlist: 0x5144
   __TEXT.__cstring: 0x5e49
   __TEXT.__const: 0x9e0
   __TEXT.__oslogstring: 0x27d6

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2568
+  __DATA_CONST.__objc_selrefs: 0x2570
   __DATA_CONST.__objc_superrefs: 0x248
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__got: 0x5e0
   __AUTH_CONST.__const: 0x3c0
   __AUTH_CONST.__cfstring: 0x5820
-  __AUTH_CONST.__objc_const: 0x7188
+  __AUTH_CONST.__objc_const: 0x71b0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x19a0
   __DATA.__objc_ivar: 0x410
   __DATA.__data: 0x320
-  __DATA.__bss: 0x1c0
+  __DATA.__bss: 0x130
+  __DATA_DIRTY.__objc_data: 0x19a0
+  __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1859
-  Symbols:   5823
+  Functions: 1860
+  Symbols:   5827
   CStrings:  1837
 
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __DATA.__objc_ivar : content changed
~ __DATA.__data : content changed
Symbols:
+ +[PBBridgeWatchAttributeController sharedController]
+ __OBJC_$_CLASS_PROP_LIST_PBBridgeWatchAttributeController
+ ___52+[PBBridgeWatchAttributeController sharedController]_block_invoke
+ _objc_msgSend$sharedController
+ _sharedController.__shared
+ _sharedController.onceToken
- ___58+[PBBridgeWatchAttributeController sharedDeviceController]_block_invoke
- _sharedDeviceController.__material
- _sharedDeviceController.onceToken
Functions:
~ +[PBBridgeWatchAttributeController sharedDeviceController] : 68 -> 4
+ +[PBBridgeWatchAttributeController sharedController]

```
