## CoreBluetooth

> `/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`

```diff

-  __TEXT.__text: 0xd7634
-  __TEXT.__objc_methlist: 0xd654
-  __TEXT.__const: 0x2d01
-  __TEXT.__oslogstring: 0x30f7
-  __TEXT.__cstring: 0x1adc5
+  __TEXT.__text: 0xd7a60
+  __TEXT.__objc_methlist: 0xd6a4
+  __TEXT.__const: 0x2d09
+  __TEXT.__oslogstring: 0x3110
+  __TEXT.__cstring: 0x1ae30
   __TEXT.__gcc_except_tab: 0x25ec
   __TEXT.__ustring: 0x82
-  __TEXT.__unwind_info: 0x29d0
+  __TEXT.__unwind_info: 0x29e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x68a0
-  __DATA_CONST.__objc_classlist: 0x350
+  __DATA_CONST.__objc_classlist: 0x358
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5cb0
+  __DATA_CONST.__objc_selrefs: 0x5cc8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x140
   __DATA_CONST.__got: 0x420
-  __AUTH_CONST.__const: 0x5c0
-  __AUTH_CONST.__cfstring: 0x11100
-  __AUTH_CONST.__objc_const: 0x1c470
+  __AUTH_CONST.__const: 0x5e0
+  __AUTH_CONST.__cfstring: 0x11140
+  __AUTH_CONST.__objc_const: 0x1c580
   __AUTH_CONST.__objc_intobj: 0x900
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0xa30
   __AUTH.__objc_data: 0xa00
-  __DATA.__objc_ivar: 0x136c
+  __DATA.__objc_ivar: 0x1374
   __DATA.__data: 0xf98
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x1720
+  __DATA_DIRTY.__objc_data: 0x1770
   __DATA_DIRTY.__data: 0x1d0
-  __DATA_DIRTY.__bss: 0x230
+  __DATA_DIRTY.__bss: 0x240
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5524
-  Symbols:   17677
-  CStrings:  7281
+  Functions: 5532
+  Symbols:   17705
+  CStrings:  7287
 
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
~ __AUTH.__objc_data : content changed
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
+ GCC_except_table532
+ GCC_except_table547
+ GCC_except_table610
+ _OBJC_CLASS_$_CBDeviceCompanionSetupInfo
+ _OBJC_IVAR_$_CBDeviceCompanionSetupInfo._action
+ _OBJC_IVAR_$_CBDeviceCompanionSetupInfo._model
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
- GCC_except_table526
- GCC_except_table541
- GCC_except_table604
CStrings:
+ "%@%c"
+ "%u%c%u"
+ "Channel Sounding procedure was terminated by the peer device."
+ "Device found: %{public}@"
+ "FindNearbyLocalFindableAccessoryExtendedRange"
+ "MobileBluetooth-2700.43"
- "%u.%u.%u"
- "MobileBluetooth-2700.41.1.1"

```
