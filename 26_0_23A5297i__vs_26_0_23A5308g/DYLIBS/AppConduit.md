## AppConduit

> `/System/Library/PrivateFrameworks/AppConduit.framework/AppConduit`

```diff

-388.0.0.0.1
-  __TEXT.__text: 0x1d784
+391.0.0.0.0
+  __TEXT.__text: 0x1de04
   __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0x145c
+  __TEXT.__objc_methlist: 0x1474
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x60cc
+  __TEXT.__cstring: 0x62ce
   __TEXT.__gcc_except_tab: 0x4e4
   __TEXT.__oslogstring: 0x7d
-  __TEXT.__unwind_info: 0x7c8
+  __TEXT.__unwind_info: 0x7d0
   __TEXT.__objc_classname: 0x147
-  __TEXT.__objc_methname: 0x50f4
+  __TEXT.__objc_methname: 0x5197
   __TEXT.__objc_methtype: 0xb0b
-  __TEXT.__objc_stubs: 0x2e40
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x8e0
+  __TEXT.__objc_stubs: 0x2ea0
+  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__const: 0x8e8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfa0
+  __DATA_CONST.__objc_selrefs: 0xfc0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x428
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x2900
-  __AUTH_CONST.__objc_const: 0x1b28
-  __DATA.__objc_ivar: 0xf0
+  __AUTH_CONST.__cfstring: 0x29c0
+  __AUTH_CONST.__objc_const: 0x1b58
+  __DATA.__objc_ivar: 0xf4
   __DATA.__data: 0x280
   __DATA.__bss: 0x38
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 720A03EF-3FFC-3937-B4F1-4AE3215F36D7
-  Functions: 564
-  Symbols:   2105
-  CStrings:  1615
+  UUID: A6DF4B54-A009-3B6D-A8E2-10468D787E6E
+  Functions: 567
+  Symbols:   2119
+  CStrings:  1634
 
Symbols:
+ -[ACXSyncedApplication accessorySetupKitSupports]
+ -[ACXSyncedApplication setAccessorySetupKitSupports:]
+ _ACXAccessorySetupKitSupportsKey
+ _MIPlaceholderArchitecturesKey
+ _MIPlaceholderCPUSubtypeKey
+ _MIPlaceholderCPUTypeKey
+ _OBJC_IVAR_$_ACXSyncedApplication._accessorySetupKitSupports
+ __ValidateSupportedArchitecturesListForPlaceholder
+ _objc_msgSend$accessorySetupKitSupports
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$intersectsSet:
+ _objc_retain_x27
- _objc_retain_x26
CStrings:
+ "%@ entry in Info.plist of %@ contains non-dictionary items"
+ "ACXAccessorySetupKitSupportsKey"
+ "Expected both %@ and %@ to be set in dictionary %@ within the array of dictionaries mapped to %@ in Info.plist of %@"
+ "Expected dictionary %@ in the array of dictionaries mapped to %@ in Info.plist of %@ to contain strings mapped to numbers"
+ "T@\"NSArray\",C,N,V_accessorySetupKitSupports"
+ "Unexpected NULL deviceArchName from macho_arch_name_for_cpu_type with sliceCpuType: 0x%x sliceSubType: 0x%x"
+ "_ValidateSupportedArchitecturesListForPlaceholder"
+ "_accessorySetupKitSupports"
+ "accessorySetupKitSupports"
+ "addObjectsFromArray:"
+ "intersectsSet:"
+ "setAccessorySetupKitSupports:"

```
