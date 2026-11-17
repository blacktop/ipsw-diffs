## AppStoreDaemon

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon`

```diff

-13.2.8.0.0
-  __TEXT.__text: 0x88118
-  __TEXT.__objc_methlist: 0xb4b4
+13.2.11.0.0
+  __TEXT.__text: 0x8833c
+  __TEXT.__objc_methlist: 0xb4ec
   __TEXT.__const: 0x12a8
   __TEXT.__dlopen_cstrs: 0x5b
   __TEXT.__constg_swiftt: 0x1d4

   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_reflstr: 0x10b
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__cstring: 0x58e8
+  __TEXT.__cstring: 0x590c
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_fieldmd: 0x278
   __TEXT.__swift5_proto: 0xfc

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4648
+  __DATA_CONST.__objc_selrefs: 0x4650
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0xc8
   __DATA_CONST.__got: 0x698
   __AUTH_CONST.__const: 0xf68
-  __AUTH_CONST.__cfstring: 0x6d00
-  __AUTH_CONST.__objc_const: 0x16590
+  __AUTH_CONST.__cfstring: 0x6d40
+  __AUTH_CONST.__objc_const: 0x16620
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x7e8
-  __DATA.__objc_ivar: 0xe04
+  __DATA.__objc_ivar: 0xe10
   __DATA.__data: 0x198
   __DATA_DIRTY.__objc_ivar: 0x18c
   __DATA_DIRTY.__objc_data: 0x3c70

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4706
-  Symbols:   7928
-  CStrings:  1425
+  Functions: 4711
+  Symbols:   7936
+  CStrings:  1427
 
Symbols:
+ -[ASDAppLedgerItem initWithBundleID:bundleVersion:itemID:versionID:installDate:lastLaunchDate:wasFactoryInstall:]
+ -[ASDAppLedgerItem wasFactoryInstall]
+ -[ASDAppLedgerQuery bundleID]
+ -[ASDAppLedgerQuery itemID]
+ -[ASDAppLedgerQuery setBundleID:]
+ -[ASDAppLedgerQuery setItemID:]
+ _OBJC_IVAR_$_ASDAppLedgerItem._wasFactoryInstall
+ _OBJC_IVAR_$_ASDAppLedgerQuery._bundleID
+ _OBJC_IVAR_$_ASDAppLedgerQuery._itemID
- -[ASDAppLedgerItem initWithBundleID:bundleVersion:itemID:versionID:installDate:lastLaunchDate:]
CStrings:
+ "<%@: %p> bundleID=%@ bundleVersion=%@ itemID=%@ versionID=%@ installDate=%@ lastLaunchDate=%@ wasFactoryInstall=%@"
+ "FI"
+ "itemID = %@"
- "<%@: %p> bundleID=%@ bundleVersion=%@ itemID=%@ versionID=%@ installDate=%@ lastLaunchDate=%@"
```
