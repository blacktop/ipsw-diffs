## KeyboardServices

> `/System/Library/PrivateFrameworks/KeyboardServices.framework/KeyboardServices`

```diff

 161.0.0.0.0
-  __TEXT.__text: 0x30d68
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0x1e4c
+  __TEXT.__text: 0x30da8
+  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__objc_methlist: 0x21ec
   __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0xf2c
-  __TEXT.__cstring: 0x47a9
+  __TEXT.__gcc_except_tab: 0xfac
+  __TEXT.__cstring: 0x47a4
   __TEXT.__oslogstring: 0x19ce
   __TEXT.__ustring: 0xd4
-  __TEXT.__unwind_info: 0xc80
+  __TEXT.__unwind_info: 0xcb0
   __TEXT.__objc_classname: 0x492
   __TEXT.__objc_methname: 0x5d0e
   __TEXT.__objc_methtype: 0xc5d

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1818
+  __DATA_CONST.__objc_selrefs: 0x18f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x3f0
+  __AUTH_CONST.__auth_got: 0x3e8
   __AUTH_CONST.__const: 0x1910
   __AUTH_CONST.__cfstring: 0x2840
-  __AUTH_CONST.__objc_const: 0x55a0
+  __AUTH_CONST.__objc_const: 0x4f48
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D3989F46-8020-3EF2-9693-88AA9D835133
-  Functions: 1017
-  Symbols:   2797
-  CStrings:  2188
+  UUID: 0DCEF158-25AC-3E57-BE7F-71BD8CF2FE00
+  Functions: 1031
+  Symbols:   2808
+  CStrings:  2186
 
Symbols:
+ +[_KSDeviceStateMonitor deviceStateMonitor].cold.1
+ +[_KSDeviceStateMonitor isRunningOnInternalBuild].cold.1
+ +[_KSTextReplacementHelper logPhraseWordCount:].cold.1
+ +[_KSTextReplacementLegacyStore basePersistentStoreURL].cold.1
+ +[_KSTextReplacementServer textReplacementServer].cold.1
+ +[_KSUtilities keyboardDirectory].cold.1
+ +[_KSUtilities keyboardServicesDirectory].cold.1
+ +[_KSiCloudDeviceListMonitor iCloudDeviceListMonitor].cold.1
+ -[_KSiCloudDeviceListMonitor queryMigrationState].cold.1
+ GCC_except_table1
+ GCC_except_table2
+ KSCategory.cold.1
+ _homeDirectory.cold.1
- _strcmp
CStrings:
- "."
- ".."

```
