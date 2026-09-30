## ScreenTime

> `/System/Library/Frameworks/ScreenTime.framework/ScreenTime`

```diff

-537.5.7.0.0
-  __TEXT.__text: 0x4c08
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_methlist: 0x6c4
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x26f
-  __TEXT.__gcc_except_tab: 0x180
-  __TEXT.__oslogstring: 0x4ce
-  __TEXT.__unwind_info: 0x218
+571.0.0.0.0
+  __TEXT.__text: 0x4e20
+  __TEXT.__auth_stubs: 0x360
+  __TEXT.__objc_methlist: 0x72c
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x242
+  __TEXT.__gcc_except_tab: 0x194
+  __TEXT.__oslogstring: 0x502
+  __TEXT.__unwind_info: 0x230
   __TEXT.__objc_classname: 0x134
-  __TEXT.__objc_methname: 0x1364
-  __TEXT.__objc_methtype: 0x4ee
-  __TEXT.__objc_stubs: 0xde0
-  __DATA_CONST.__got: 0x140
+  __TEXT.__objc_methname: 0x141f
+  __TEXT.__objc_methtype: 0x50c
+  __TEXT.__objc_stubs: 0xe00
+  __DATA_CONST.__got: 0x138
   __DATA_CONST.__const: 0x2b0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x528
+  __DATA_CONST.__objc_selrefs: 0x548
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__objc_superrefs: 0x28
+  __AUTH_CONST.__auth_got: 0x1c0
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x1a0
-  __AUTH_CONST.__objc_const: 0xea8
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x48
+  __AUTH_CONST.__cfstring: 0x160
+  __AUTH_CONST.__objc_const: 0xf08
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x50
   __DATA.__data: 0x2a0
-  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__objc_data: 0x1e0
   - /System/Library/Frameworks/AVKit.framework/AVKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 98392FD6-1820-3B67-9F5D-D91BD504C8CC
-  Functions: 157
-  Symbols:   716
-  CStrings:  335
+  UUID: 506E823B-9CB2-32CB-B90E-35A414673F84
+  Functions: 165
+  Symbols:   736
+  CStrings:  342
 
Symbols:
+ -[STWebRemoteViewController .cxx_destruct]
+ -[STWebRemoteViewController _canShowWhileLocked]
+ -[STWebRemoteViewController dealloc]
+ -[STWebRemoteViewController extensionRequestIdentifier]
+ -[STWebRemoteViewController extension]
+ -[STWebRemoteViewController setExtension:]
+ -[STWebRemoteViewController setExtensionRequestIdentifier:]
+ -[STWebpageController _canShowWhileLocked]
+ GCC_except_table3
+ _OBJC_IVAR_$_STWebRemoteViewController._extension
+ _OBJC_IVAR_$_STWebRemoteViewController._extensionRequestIdentifier
+ ___block_descriptor_40_e8_32w_e47_v24?0"STWebRemoteViewController"8"NSError"16lw32l8
+ ___block_descriptor_48_e8_32s40bs_e54_v32?0"<NSCopying>"8"UIViewController"16"NSError"24ls32l8s40l8
+ ___block_literal_global.46
+ ___block_literal_global.48
+ ___block_literal_global.54
+ ___block_literal_global.56
+ _objc_msgSend$cancelExtensionRequestWithIdentifier:
+ _objc_msgSend$setExtension:
+ _objc_msgSend$setExtensionRequestIdentifier:
+ _objc_release_x27
+ _objc_setProperty_nonatomic_copy
- _OBJC_CLASS_$_NSAssertionHandler
- ___block_descriptor_40_e8_32bs_e54_v32?0"<NSCopying>"8"UIViewController"16"NSError"24ls32l8
- ___block_descriptor_56_e8_32s40s_e47_v24?0"STWebRemoteViewController"8"NSError"16ls32l8s40l8
- ___block_literal_global.53
- ___block_literal_global.55
- ___block_literal_global.61
- ___block_literal_global.63
- _objc_msgSend$currentHandler
- _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
- _objc_retain
CStrings:
+ "@\"<NSCopying>\""
+ "@\"NSExtension\""
+ "Failed to create remote view controller: %{public}@"
+ "T@\"<NSCopying>\",C,N,V_extensionRequestIdentifier"
+ "T@\"NSExtension\",&,N,V_extension"
+ "_canShowWhileLocked"
+ "_extension"
+ "_extensionRequestIdentifier"
+ "cancelExtensionRequestWithIdentifier:"
+ "extension"
+ "extensionRequestIdentifier"
+ "setExtension:"
+ "setExtensionRequestIdentifier:"
- "Fatal error occured %@"
- "STWebpageController.m"
- "currentHandler"
- "handleFailureInMethod:object:file:lineNumber:description:"

```
