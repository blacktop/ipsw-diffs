## CoreBluetooth

> `/System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth`

```diff

-  __TEXT.__text: 0xe02c4
-  __TEXT.__objc_methlist: 0xd5fc
-  __TEXT.__const: 0x2cf1
-  __TEXT.__oslogstring: 0x30b7
-  __TEXT.__cstring: 0x1b087
+  __TEXT.__text: 0xe070c
+  __TEXT.__objc_methlist: 0xd64c
+  __TEXT.__const: 0x2cf9
+  __TEXT.__oslogstring: 0x30d0
+  __TEXT.__cstring: 0x1b0b8
   __TEXT.__gcc_except_tab: 0x264c
   __TEXT.__ustring: 0x82
-  __TEXT.__unwind_info: 0x28b0
+  __TEXT.__unwind_info: 0x28c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x5a30
-  __DATA_CONST.__objc_classlist: 0x348
+  __DATA_CONST.__objc_classlist: 0x350
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5c78
+  __DATA_CONST.__objc_selrefs: 0x5c90
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0x140
   __DATA_CONST.__got: 0x400
-  __AUTH_CONST.__const: 0x1610
-  __AUTH_CONST.__cfstring: 0x10f00
-  __AUTH_CONST.__objc_const: 0x1c3d0
+  __AUTH_CONST.__const: 0x1630
+  __AUTH_CONST.__cfstring: 0x10f20
+  __AUTH_CONST.__objc_const: 0x1c4e0
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x978
-  __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_ivar: 0x136c
+  __AUTH.__objc_data: 0x820
+  __DATA.__objc_ivar: 0x1374
   __DATA.__data: 0xf28
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x19f0
+  __DATA_DIRTY.__objc_data: 0x1900
   __DATA_DIRTY.__data: 0x200
   __DATA_DIRTY.__common: 0x10
-  __DATA_DIRTY.__bss: 0x218
+  __DATA_DIRTY.__bss: 0x228
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5572
-  Symbols:   11814
-  CStrings:  7275
+  Functions: 5580
+  Symbols:   11834
+  CStrings:  7279
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[CBDevice companionSetupInfo]
+ -[CBDeviceCompanionSetupInfo .cxx_destruct]
+ -[CBDeviceCompanionSetupInfo action]
+ -[CBDeviceCompanionSetupInfo model]
+ -[CBDeviceCompanionSetupInfo setAction:]
+ -[CBDeviceCompanionSetupInfo setModel:]
+ GCC_except_table527
+ GCC_except_table534
+ GCC_except_table549
+ GCC_except_table614
+ OBJC_IVAR_$_CBDeviceCompanionSetupInfo._action
+ OBJC_IVAR_$_CBDeviceCompanionSetupInfo._model
+ _OBJC_CLASS_$_CBDeviceCompanionSetupInfo
+ _OBJC_METACLASS_$_CBDeviceCompanionSetupInfo
+ __OBJC_$_INSTANCE_METHODS_CBDeviceCompanionSetupInfo
+ __OBJC_$_INSTANCE_VARIABLES_CBDeviceCompanionSetupInfo
+ __OBJC_$_PROP_LIST_CBDeviceCompanionSetupInfo
+ __OBJC_CLASS_RO_$_CBDeviceCompanionSetupInfo
+ __OBJC_METACLASS_RO_$_CBDeviceCompanionSetupInfo
+ ___CBDiscoveryLogger_block_invoke
+ _objc_msgSend$setAction:
+ _objc_msgSend$setModel:
- GCC_except_table521
- GCC_except_table528
- GCC_except_table543
- GCC_except_table608
CStrings:
+ "%@%c"
+ "%u%c%u"
+ "Device found: %{public}@"
+ "FindNearbyLocalFindableAccessoryExtendedRange"
+ "MobileBluetooth-2700.43"
- "%u.%u.%u"
- "MobileBluetooth-2700.41"

```
