## AXContainerServices

> `/System/Library/PrivateFrameworks/AXContainerServices.framework/AXContainerServices`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x8c0
-  __TEXT.__auth_stubs: 0x160
+3229.1.6.0.0
+  __TEXT.__text: 0x848
   __TEXT.__objc_methlist: 0x68
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x6b
+  __TEXT.__cstring: 0x6d
   __TEXT.__unwind_info: 0x88
-  __TEXT.__objc_classname: 0x15
-  __TEXT.__objc_methname: 0x21c
-  __TEXT.__objc_methtype: 0x4a
-  __TEXT.__objc_stubs: 0x100
-  __DATA_CONST.__got: 0x60
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x70
-  __AUTH_CONST.__auth_got: 0xb8
+  __DATA_CONST.__got: 0x60
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0xd0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x4
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2998A62B-3588-3D2C-AA18-BDB809C83823
-  Functions: 13
-  Symbols:   87
-  CStrings:  31
+  UUID: F07A872F-4A45-32E1-B160-25F4D2E8E998
+  Functions: 12
+  Symbols:   90
+  CStrings:  8
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x22
+ _objc_retain_x3
+ _objc_retain_x4
- +[AXContainerManager sharedManager].cold.1
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[AXContainerManager containerServerClient] : 172 -> 160
~ -[AXContainerManager readDataForFileAtAccessibilityContainerPath:completion:] : 344 -> 340
~ ___77-[AXContainerManager readDataForFileAtAccessibilityContainerPath:completion:]_block_invoke : 204 -> 192
~ _getErrorCascading : 364 -> 356
~ ___78-[AXContainerManager writeData:toFileAtAccessibilityContainerPath:completion:]_block_invoke : 100 -> 96
~ -[AXContainerManager deleteFileAtAccessibilityContainerPath:completion:] : 344 -> 340
~ ___72-[AXContainerManager deleteFileAtAccessibilityContainerPath:completion:]_block_invoke : 100 -> 96
~ -[AXContainerManager setContainerServerClient:] : 64 -> 12
CStrings:
- ".cxx_destruct"
- "@\"AXUIClient\""
- "@16@0:8"
- "T@\"AXUIClient\",&,N,V_containerServerClient"
- "_containerServerClient"
- "containerServerClient"
- "deleteFileAtAccessibilityContainerPath:completion:"
- "dictionaryWithObjects:forKeys:count:"
- "errorWithDomain:code:userInfo:"
- "initWithIdentifier:serviceBundleName:"
- "mainAccessQueue"
- "objectForKeyedSubscript:"
- "readDataForFileAtAccessibilityContainerPath:completion:"
- "sendAsynchronousMessage:withIdentifier:targetAccessQueue:completion:"
- "setContainerServerClient:"
- "sharedManager"
- "stringWithFormat:"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@16@?24"
- "v40@0:8@16@24@?32"
- "writeData:toFileAtAccessibilityContainerPath:completion:"

```
