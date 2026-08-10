## com.apple.accessoryd.matching

> `/System/Library/UserEventPlugins/com.apple.accessoryd.matching.plugin/com.apple.accessoryd.matching`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA.__objc_classlist`
- `__DATA.__objc_catlist`
- `__DATA.__objc_protolist`
- `__DATA.__objc_const`
- `__DATA.__objc_protorefs`
- `__DATA.__objc_superrefs`
- `__DATA.__objc_data`
- `__DATA.__objc_arraydata`
- `__DATA.__objc_arrayobj`
- `__DATA.__objc_intobj`
- `__DATA.__data`
- `__DATA.__objc_dictobj`
- `__DATA.__auth_ptr`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-1210.0.0.502.1
-  __TEXT.__text: 0x37ca4
+1216.0.0.0.0
+  __TEXT.__text: 0x37d60
   __TEXT.__auth_stubs: 0x1000
-  __TEXT.__objc_stubs: 0x5080
+  __TEXT.__objc_stubs: 0x50c0
   __TEXT.__objc_methlist: 0x23ac
-  __TEXT.__cstring: 0x4f8e
-  __TEXT.__objc_methname: 0x6ebf
+  __TEXT.__cstring: 0x4faa
+  __TEXT.__objc_methname: 0x6ed9
   __TEXT.__objc_classname: 0x27f
   __TEXT.__objc_methtype: 0xaeb
   __TEXT.__const: 0x228
-  __TEXT.__oslogstring: 0x3f4f
+  __TEXT.__oslogstring: 0x3f71
   __TEXT.__gcc_except_tab: 0x404
   __TEXT.__ustring: 0x18
   __TEXT.__unwind_info: 0xa58
-  __DATA.__const: 0x10e0
-  __DATA.__cfstring: 0x39a0
+  __DATA.__const: 0x10f0
+  __DATA.__cfstring: 0x39c0
   __DATA.__objc_classlist: 0xb0
   __DATA.__objc_catlist: 0x10
   __DATA.__objc_protolist: 0x48
   __DATA.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x3cb0
-  __DATA.__objc_selrefs: 0x1a20
+  __DATA.__objc_selrefs: 0x1a30
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_superrefs: 0xa8
   __DATA.__objc_ivar: 0x38c

   __DATA.__data: 0x39e
   __DATA.__objc_dictobj: 0x28
   __DATA.__auth_got: 0x810
-  __DATA.__got: 0x380
+  __DATA.__got: 0x388
   __DATA.__auth_ptr: 0x18
   __DATA.__bss: 0x1e8
   __DATA.__common: 0x18

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 1496
-  Symbols:   3144
-  CStrings:  2503
+  Symbols:   3149
+  CStrings:  2507
 
Symbols:
+ _ACCUserDefaultsKey_BLEPairingAuthTimeoutValueS
+ _OBJC_CLASS_$_ACCTransportClient
+ _kCFACCUserDefaultsKey_BLEPairingAuthTimeoutValueS
+ _objc_msgSend$launchServer
+ _objc_msgSend$sharedClient
Functions:
~ _OUTLINED_FUNCTION_16 : 20 -> 16
~ _OUTLINED_FUNCTION_17 : 16 -> 20
~ _OUTLINED_FUNCTION_19 : 24 -> 12
~ _OUTLINED_FUNCTION_20 : 12 -> 24
~ _OUTLINED_FUNCTION_25 : 20 -> 12
~ _OUTLINED_FUNCTION_26 : 12 -> 20
~ _OUTLINED_FUNCTION_8 : 8 -> 12
~ _OUTLINED_FUNCTION_9 : 12 -> 28
~ _OUTLINED_FUNCTION_10 : 16 -> 8
~ _OUTLINED_FUNCTION_11 : 28 -> 16
~ _OUTLINED_FUNCTION_20 : 12 -> 20
~ _OUTLINED_FUNCTION_21 : 20 -> 12
~ -[accessorydMatchingPlugin initWithModule:] : 2248 -> 2372
~ _LibSer_SEPControl_Deserialize : 160 -> 200
~ _LibSer_SEPControlResponse_Deserialize : 64 -> 88
CStrings:
+ "BLEPairingAuthTimeoutValueS"
+ "initWithModule: call launchServer"
+ "launchServer"
+ "sharedClient"
```
