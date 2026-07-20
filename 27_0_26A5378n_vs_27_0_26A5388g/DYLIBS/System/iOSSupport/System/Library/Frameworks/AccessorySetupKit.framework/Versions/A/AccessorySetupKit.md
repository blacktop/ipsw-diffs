## AccessorySetupKit

> `/System/iOSSupport/System/Library/Frameworks/AccessorySetupKit.framework/Versions/A/AccessorySetupKit`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`

```diff

-2700.27.0.0.0
-  __TEXT.__text: 0x1958c
-  __TEXT.__objc_methlist: 0x1c30
-  __TEXT.__const: 0x4b2
+2700.30.0.0.0
+  __TEXT.__text: 0x196cc
+  __TEXT.__objc_methlist: 0x1c38
+  __TEXT.__const: 0x4c2
   __TEXT.__gcc_except_tab: 0x3b0
-  __TEXT.__cstring: 0x29c1
+  __TEXT.__cstring: 0x29d1
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__constg_swiftt: 0x294
   __TEXT.__swift5_typeref: 0x2b6

   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1580
+  __DATA_CONST.__objc_selrefs: 0x1590
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__got: 0x340
   __AUTH_CONST.__const: 0x370
-  __AUTH_CONST.__cfstring: 0xbe0
-  __AUTH_CONST.__objc_const: 0x2710
+  __AUTH_CONST.__cfstring: 0xc00
+  __AUTH_CONST.__objc_const: 0x2740
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x740
-  __AUTH.__objc_data: 0x890
-  __AUTH.__data: 0x60
-  __DATA.__objc_ivar: 0x180
+  __AUTH.__objc_data: 0x90
+  __DATA.__objc_ivar: 0x184
   __DATA.__data: 0x910
   __DATA.__bss: 0x4a0
   __DATA.__common: 0x18
+  __DATA_DIRTY.__objc_data: 0x800
+  __DATA_DIRTY.__data: 0x60
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 660
-  Symbols:   1590
-  CStrings:  295
+  Functions: 661
+  Symbols:   1596
+  CStrings:  296
 
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
+ "com.apple.AppStore"
```
