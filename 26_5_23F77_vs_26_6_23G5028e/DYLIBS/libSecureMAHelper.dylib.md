## libSecureMAHelper.dylib

> `/usr/lib/libSecureMAHelper.dylib`

```diff

-1837.122.1.0.0
-  __TEXT.__text: 0x1f120
+1837.160.11.0.0
+  __TEXT.__text: 0x1f5a8
   __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_methlist: 0x55c
+  __TEXT.__objc_methlist: 0x56c
   __TEXT.__const: 0x500
-  __TEXT.__cstring: 0x6c54
-  __TEXT.__oslogstring: 0x2cf6
+  __TEXT.__cstring: 0x6c72
+  __TEXT.__oslogstring: 0x2d8e
   __TEXT.__gcc_except_tab: 0x964
-  __TEXT.__unwind_info: 0x4f0
+  __TEXT.__unwind_info: 0x4f8
   __TEXT.__objc_classname: 0x80
-  __TEXT.__objc_methname: 0x1908
-  __TEXT.__objc_methtype: 0x250
-  __TEXT.__objc_stubs: 0x1e00
+  __TEXT.__objc_methname: 0x196e
+  __TEXT.__objc_methtype: 0x272
+  __TEXT.__objc_stubs: 0x1e20
   __DATA_CONST.__got: 0x2c0
   __DATA_CONST.__const: 0xc50
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x828
+  __DATA_CONST.__objc_selrefs: 0x838
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x2e0
   __AUTH_CONST.__auth_got: 0x670
   __AUTH_CONST.__const: 0x450
-  __AUTH_CONST.__cfstring: 0x7720
+  __AUTH_CONST.__cfstring: 0x7780
   __AUTH_CONST.__objc_const: 0x6e8
   __AUTH_CONST.__objc_intobj: 0x948
   __AUTH_CONST.__objc_arrayobj: 0xd8

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 03012D41-A4A8-3F09-8B23-23278B1A9D9E
-  Functions: 426
-  Symbols:   1388
-  CStrings:  2485
+  UUID: 72D466DC-8908-369F-ACE4-1D3462F59EC5
+  Functions: 427
+  Symbols:   1391
+  CStrings:  2499
 
Symbols:
+ -[SecureMobileAssetBundle _graftedContentsContainAppBundle]
+ -[SecureMobileAssetBundle ungraftOrUnmount:force:ungraftingError:]
+ -[SecureMobileAssetBundle ungraftWithForce:error:]
+ -[SecureMobileAssetBundle unmountWithForce:error:]
+ GCC_except_table110
+ GCC_except_table48
+ GCC_except_table53
+ GCC_except_table56
+ GCC_except_table58
+ GCC_except_table73
+ GCC_except_table90
+ ___block_literal_global.1728
+ ___block_literal_global.2280
+ _objc_msgSend$contentsOfDirectoryAtPath:error:
+ _objc_msgSend$ungraftOrUnmount:force:ungraftingError:
+ _objc_msgSend$ungraftWithForce:error:
+ _objc_msgSend$unmountWithForce:error:
- -[SecureMobileAssetBundle ungraft:]
- -[SecureMobileAssetBundle ungraftOrUnmount:ungraftingError:]
- -[SecureMobileAssetBundle unmount:]
- GCC_except_table109
- GCC_except_table47
- GCC_except_table50
- GCC_except_table55
- GCC_except_table57
- GCC_except_table72
- GCC_except_table87
- ___block_literal_global.1713
- ___block_literal_global.2268
- _objc_msgSend$ungraft:
- _objc_msgSend$ungraftOrUnmount:ungraftingError:
- _objc_msgSend$unmount:
CStrings:
+ "Applications"
+ "B28@0:8B16^@20"
+ "B36@0:8^q16B24^@28"
+ "[SMA] Checked %@ for .app bundles: found=%@"
+ "[SMA] Failed to list contents of %@: %@"
+ "[SMA] Ungrafting %@ with force=%@"
+ "[SMA] Unmounting %@ with force=%@"
+ "_graftedContentsContainAppBundle"
+ "app"
+ "contentsOfDirectoryAtPath:error:"
+ "ungraftOrUnmount:force:ungraftingError:"
+ "ungraftWithForce:error:"
+ "unmountFlags"
+ "unmountWithForce:error:"
- "ungraft:"
- "ungraftOrUnmount:ungraftingError:"
- "unmount:"

```
