## AccessorySetupKit

> `/System/iOSSupport/System/Library/Frameworks/AccessorySetupKit.framework/Versions/A/AccessorySetupKit`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__TEXT.__objc_classname`
- `__TEXT.__objc_methtype`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-326.7.0.0.0
-  __TEXT.__text: 0x19c28
+326.9.0.0.0
+  __TEXT.__text: 0x19d70
   __TEXT.__auth_stubs: 0xd40
-  __TEXT.__objc_methlist: 0x1c28
-  __TEXT.__const: 0x4b2
-  __TEXT.__gcc_except_tab: 0x380
-  __TEXT.__cstring: 0x29a1
+  __TEXT.__objc_methlist: 0x1c30
+  __TEXT.__const: 0x4c2
+  __TEXT.__gcc_except_tab: 0x38c
+  __TEXT.__cstring: 0x29b1
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__constg_swiftt: 0x294
   __TEXT.__swift5_typeref: 0x2b6

   __TEXT.__swift5_types: 0x10
   __TEXT.__oslogstring: 0x28b
   __TEXT.__swift5_capture: 0xc0
-  __TEXT.__unwind_info: 0x660
+  __TEXT.__unwind_info: 0x668
   __TEXT.__eh_frame: 0x78
   __TEXT.__objc_classname: 0x352
-  __TEXT.__objc_methname: 0x5601
+  __TEXT.__objc_methname: 0x5661
   __TEXT.__objc_methtype: 0x1203
-  __TEXT.__objc_stubs: 0x33e0
+  __TEXT.__objc_stubs: 0x3440
   __DATA_CONST.__got: 0x338
   __DATA_CONST.__const: 0x528
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1578
+  __DATA_CONST.__objc_selrefs: 0x1588
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x6b0
   __AUTH_CONST.__const: 0x370
-  __AUTH_CONST.__cfstring: 0xbe0
-  __AUTH_CONST.__objc_const: 0x2708
+  __AUTH_CONST.__cfstring: 0xc00
+  __AUTH_CONST.__objc_const: 0x2738
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x890
   __AUTH.__data: 0x60
-  __DATA.__objc_ivar: 0x180
+  __DATA.__objc_ivar: 0x184
   __DATA.__data: 0x910
   __DATA.__bss: 0x4a0
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 659
-  Symbols:   1567
-  CStrings:  1367
+  Functions: 660
+  Symbols:   1573
+  CStrings:  1372
 
Symbols:
+ -[ASAccessoryCompanionAppInfo distributorBundleID]
+ -[ASAccessoryCompanionAppInfo distributorName]
+ -[ASAccessoryCompanionAppInfo initWithBundleID:name:publisherName:adamID:icon:appIsInstalled:distributorBundleID:distributorName:]
+ -[ASAccessoryCompanionAppView initWithBundleID:appInfo:]
+ GCC_except_table1
+ GCC_except_table10
+ GCC_except_table12
+ OBJC_IVAR_$_ASAccessoryCompanionAppInfo._distributorBundleID
+ OBJC_IVAR_$_ASAccessoryCompanionAppInfo._distributorName
+ ___56-[ASAccessoryCompanionAppView initWithBundleID:appInfo:]_block_invoke
+ ___56-[ASAccessoryCompanionAppView initWithBundleID:appInfo:]_block_invoke_2
+ _objc_msgSend$distributorBundleID
+ _objc_msgSend$distributorName
+ _objc_msgSend$initWithBundleID:appInfo:
+ _objc_msgSend$initWithBundleID:name:publisherName:adamID:icon:appIsInstalled:distributorBundleID:distributorName:
+ _objc_msgSend$setPriority:
- -[ASAccessoryCompanionAppInfo initWithBundleID:name:publisherName:adamID:icon:appIsInstalled:]
- -[ASAccessoryCompanionAppView loadingCompletionHandler]
- -[ASAccessoryCompanionAppView setLoadingCompletionHandler:]
- GCC_except_table0
- GCC_except_table9
- OBJC_IVAR_$_ASAccessoryCompanionAppView._loadingCompletionHandler
- ___48-[ASAccessoryCompanionAppView initWithBundleID:]_block_invoke
- ___48-[ASAccessoryCompanionAppView initWithBundleID:]_block_invoke_2
- _objc_msgSend$initWithBundleID:name:publisherName:adamID:icon:appIsInstalled:
- _objc_msgSend$loadingCompletionHandler
CStrings:
+ "@76@0:8@16@24@32@40@48B56@60@68"
+ "T@\"NSString\",R,N,V_distributorBundleID"
+ "T@\"NSString\",R,N,V_distributorName"
+ "_distributorBundleID"
+ "_distributorName"
+ "com.apple.AppStore"
+ "distributorBundleID"
+ "distributorName"
+ "initWithBundleID:appInfo:"
+ "initWithBundleID:name:publisherName:adamID:icon:appIsInstalled:distributorBundleID:distributorName:"
+ "setPriority:"
- "@60@0:8@16@24@32@40@48B56"
- "T@?,C,N,V_loadingCompletionHandler"
- "_loadingCompletionHandler"
- "initWithBundleID:name:publisherName:adamID:icon:appIsInstalled:"
- "loadingCompletionHandler"
- "setLoadingCompletionHandler:"
```
