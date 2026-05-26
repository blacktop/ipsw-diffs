## ndoagent

> `/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent`

```diff

-517.120.3.0.0
-  __TEXT.__text: 0x71f04
-  __TEXT.__auth_stubs: 0x2760
-  __TEXT.__objc_stubs: 0x38a0
-  __TEXT.__objc_methlist: 0x14cc
+517.160.4.0.0
+  __TEXT.__text: 0x72b04
+  __TEXT.__auth_stubs: 0x2780
+  __TEXT.__objc_stubs: 0x3920
+  __TEXT.__objc_methlist: 0x14e4
   __TEXT.__const: 0x72c8
   __TEXT.__gcc_except_tab: 0x4fc
-  __TEXT.__objc_methname: 0x4165
-  __TEXT.__oslogstring: 0x39c6
-  __TEXT.__cstring: 0x2571
+  __TEXT.__objc_methname: 0x41b5
+  __TEXT.__oslogstring: 0x3b46
+  __TEXT.__cstring: 0x25e1
   __TEXT.__objc_classname: 0x552
   __TEXT.__objc_methtype: 0xdd2
   __TEXT.__swift5_typeref: 0x1432

   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x24
   __TEXT.__swift5_assocty: 0x60
-  __TEXT.__unwind_info: 0x1c70
+  __TEXT.__unwind_info: 0x1c88
   __TEXT.__eh_frame: 0x1b68
-  __DATA_CONST.__auth_got: 0x13c0
-  __DATA_CONST.__got: 0x970
-  __DATA_CONST.__auth_ptr: 0x7b0
-  __DATA_CONST.__const: 0x3c68
-  __DATA_CONST.__cfstring: 0x1320
+  __DATA_CONST.__auth_got: 0x13d0
+  __DATA_CONST.__got: 0x980
+  __DATA_CONST.__auth_ptr: 0x7b8
+  __DATA_CONST.__const: 0x3c90
+  __DATA_CONST.__cfstring: 0x1340
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x4c58
-  __DATA.__objc_selrefs: 0x10c8
+  __DATA.__objc_selrefs: 0x10e8
   __DATA.__objc_ivar: 0x84
   __DATA.__objc_data: 0xf38
   __DATA.__data: 0x15f8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CA63B8D6-2CE8-3FF1-944A-3FBC4D949DAE
-  Functions: 2461
-  Symbols:   1064
-  CStrings:  1518
+  UUID: 84474D62-19E1-3A4F-A050-1B3E6A14E3E1
+  Functions: 2469
+  Symbols:   1068
+  CStrings:  1532
 
Symbols:
+ _$s6NDOAPI19NDOKeyValueStoreKeyO03rawC0SSvg
+ _$s6NDOAPI19NDOKeyValueStoreKeyO11developmentyA2CmFWC
+ _$s6NDOAPI19NDOKeyValueStoreKeyO17wasProfileManagedyA2CmFWC
+ _$sSo13os_log_type_ta0A0E4infoABvgZ
CStrings:
+ "%s Environment is profile-managed. Recording sentinel."
+ "%s NDO environment profile removed. Resetting to production environment."
+ "%s Profile expired. Resetting to production environment."
+ "%s Profile list changed but NDO environment is still profile-managed. Recording sentinel."
+ "%s Profile no longer active but development flag is set. No action needed."
+ "checkForExpiredProfile(_:)"
+ "checkForExpiredProfile:"
+ "com.apple.ManagedConfiguration.profileListChanged"
+ "handleProfileListChanged(_:)"
+ "handleProfileListChanged:"
+ "ndoagent1"
+ "objectIsForcedForKey:"
+ "setPriority:"

```
