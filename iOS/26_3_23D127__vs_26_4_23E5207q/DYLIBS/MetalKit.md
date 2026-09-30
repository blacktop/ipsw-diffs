## MetalKit

> `/System/Library/Frameworks/MetalKit.framework/MetalKit`

```diff

-172.6.0.0.0
-  __TEXT.__text: 0x10870
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0x10e4
+173.7.0.0.0
+  __TEXT.__text: 0x1121c
+  __TEXT.__auth_stubs: 0x7f0
+  __TEXT.__objc_methlist: 0x1114
   __TEXT.__const: 0xbd0
-  __TEXT.__cstring: 0x1bbb
+  __TEXT.__cstring: 0x1c19
   __TEXT.__gcc_except_tab: 0xec
-  __TEXT.__unwind_info: 0x4c0
-  __TEXT.__objc_classname: 0x267
-  __TEXT.__objc_methname: 0x33c2
-  __TEXT.__objc_methtype: 0xd16
-  __TEXT.__objc_stubs: 0x2a40
-  __DATA_CONST.__got: 0x1a0
+  __TEXT.__unwind_info: 0x4e0
+  __TEXT.__objc_classname: 0x269
+  __TEXT.__objc_methname: 0x34d9
+  __TEXT.__objc_methtype: 0xd40
+  __TEXT.__objc_stubs: 0x2b40
+  __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__const: 0x410
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd68
+  __DATA_CONST.__objc_selrefs: 0xdb0
   __DATA_CONST.__objc_superrefs: 0x98
-  __AUTH_CONST.__auth_got: 0x428
+  __AUTH_CONST.__auth_got: 0x408
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0xf60
-  __AUTH_CONST.__objc_const: 0x3600
-  __DATA.__objc_ivar: 0x1f8
+  __AUTH_CONST.__cfstring: 0xf80
+  __AUTH_CONST.__objc_const: 0x3650
+  __DATA.__objc_ivar: 0x200
   __DATA.__data: 0xb08
   __DATA.__common: 0x8
   __DATA.__bss: 0x40

   - /System/Library/PrivateFrameworks/TextureIO.framework/TextureIO
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1EA8606A-38CA-3B44-8ED7-65CC92E6AE4C
-  Functions: 378
-  Symbols:   1716
-  CStrings:  1112
+  UUID: 6BB299C6-10D2-3604-B234-BCE7D9939919
+  Functions: 386
+  Symbols:   1735
+  CStrings:  1130
 
Symbols:
+ -[MTKView _evictResources]
+ -[MTKView _initializeResidencyManagement]
+ -[MTKView _initializeResidencyManagement].cold.1
+ -[MTKView _replaceResidencySetEntryForOriginalTexture:newTexture:]
+ -[MTKView residencySet]
+ _OBJC_CLASS_$_MTLResidencySetDescriptor
+ _OBJC_IVAR_$_MTKView._allocationsToEvict
+ _OBJC_IVAR_$_MTKView._residencySet
+ _OUTLINED_FUNCTION_0
+ _objc_msgSend$_evictResources
+ _objc_msgSend$_initializeResidencyManagement
+ _objc_msgSend$_replaceResidencySetEntryForOriginalTexture:newTexture:
+ _objc_msgSend$addAllocation:
+ _objc_msgSend$newResidencySetWithDescriptor:error:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeAllocation:
+ _objc_msgSend$supportsFamily:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x27
- _objc_claimAutoreleasedReturnValue
- _objc_release_x1
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x24
- _objc_retain_x3
- _objc_retain_x4
CStrings:
+ "-[MTKView _initializeResidencyManagement]"
+ "@\"<MTLResidencySet>\""
+ "T@\"<MTLResidencySet>\",R,N"
+ "[3@\"NSMutableArray\"]"
+ "_allocationsToEvict"
+ "_evictResources"
+ "_initializeResidencyManagement"
+ "_replaceResidencySetEntryForOriginalTexture:newTexture:"
+ "_residencySet"
+ "_residencySet != nil"
+ "addAllocation:"
+ "com.apple.MTKView.residencySet"
+ "newResidencySetWithDescriptor:error:"
+ "removeAllObjects"
+ "removeAllocation:"
+ "residencySet"
+ "supportsFamily:"

```
