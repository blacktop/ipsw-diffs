## ImageKit

> `/System/Library/Frameworks/Quartz.framework/Versions/A/Frameworks/ImageKit.framework/Versions/A/ImageKit`

```diff

-1243.0.0.0.0
-  __TEXT.__text: 0x16fbac
-  __TEXT.__objc_methlist: 0x1fbd4
-  __TEXT.__cstring: 0x174ba
+1245.0.0.0.0
+  __TEXT.__text: 0x16feec
+  __TEXT.__objc_methlist: 0x1fbec
+  __TEXT.__cstring: 0x174d9
   __TEXT.__gcc_except_tab: 0xdec
   __TEXT.__const: 0x1b68
   __TEXT.__ustring: 0x9c
   __TEXT.__oslogstring: 0x7c
-  __TEXT.__unwind_info: 0x6888
+  __TEXT.__unwind_info: 0x6898
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x108e0
+  __DATA_CONST.__objc_selrefs: 0x108f0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x958
   __DATA_CONST.__objc_arraydata: 0x5f8
   __DATA_CONST.__got: 0x1bc0
-  __AUTH_CONST.__const: 0x2460
+  __AUTH_CONST.__const: 0x2490
   __AUTH_CONST.__cfstring: 0x16560
-  __AUTH_CONST.__objc_const: 0x304c0
+  __AUTH_CONST.__objc_const: 0x30500
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x630
   __AUTH_CONST.__objc_doubleobj: 0x60

   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0x1528
   __AUTH.__objc_data: 0x7120
-  __DATA.__objc_ivar: 0x263c
+  __DATA.__objc_ivar: 0x2644
   __DATA.__data: 0x10d0
   __DATA.__bss: 0x807b8
   __DATA.__common: 0x8c

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 10826
-  Symbols:   24728
-  CStrings:  3163
+  Functions: 10832
+  Symbols:   24739
+  CStrings:  3164
 
Symbols:
+ -[IKScan finishScanOnMain]
+ -[IKScan saveImageToFinalDestination:pageIndex:]
+ -[IKScan setDelegateStatusText:]
+ OBJC_IVAR_$_IKScan._pendingPostProcessError
+ OBJC_IVAR_$_IKScan._saveQueue
+ __46-[IKScan scannerDevice:didScanToURL:newStyle:]_block_invoke
+ ___20-[IKScan postError:]_block_invoke
+ ___32-[IKScan setDelegateStatusText:]_block_invoke
+ ___46-[IKScan scannerDevice:didScanToURL:newStyle:]_block_invoke_3
+ ___block_descriptor_44_e8_32o_e28_v24?0^{CGImage=}8"NSURL"16l
+ ___block_descriptor_52_e8_32o_e5_v8?0l
+ _objc_msgSend$finishScanOnMain
+ _objc_msgSend$saveImageToFinalDestination:pageIndex:
+ _objc_msgSend$setDelegateStatusText:
- -[IKScan saveToFinalDestination:url:]
- ___block_descriptor_40_e8_32o_e28_v24?0^{CGImage=}8"NSURL"16l
- _objc_msgSend$saveToFinalDestination:url:
CStrings:
+ "com.apple.imagekit.IKScan.save"
```
