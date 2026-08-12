## HearingCore

> `/System/Library/PrivateFrameworks/HearingCore.framework/HearingCore`

```diff

-536.0.0.0.0
-  __TEXT.__text: 0x8384
-  __TEXT.__objc_methlist: 0x9a0
+539.1.0.0.0
+  __TEXT.__text: 0x843c
+  __TEXT.__objc_methlist: 0x9a8
   __TEXT.__const: 0xd4
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__gcc_except_tab: 0x120
-  __TEXT.__cstring: 0xb79
+  __TEXT.__cstring: 0xbe6
   __TEXT.__oslogstring: 0x78e
-  __TEXT.__unwind_info: 0x320
+  __TEXT.__unwind_info: 0x328
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x848
+  __DATA_CONST.__objc_selrefs: 0x860
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x1b0
+  __DATA_CONST.__got: 0x1b8
   __AUTH_CONST.__const: 0x480
-  __AUTH_CONST.__cfstring: 0xda0
+  __AUTH_CONST.__cfstring: 0xdc0
   __AUTH_CONST.__objc_const: 0xb60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 251
-  Symbols:   835
-  CStrings:  173
+  Functions: 252
+  Symbols:   842
+  CStrings:  175
 
Symbols:
+ +[HCUtilities processCanUseBluetooth]
+ GCC_except_table141
+ GCC_except_table147
+ GCC_except_table165
+ GCC_except_table187
+ GCC_except_table212
+ GCC_except_table224
+ GCC_except_table229
+ GCC_except_table236
+ GCC_except_table250
+ _OBJC_CLASS_$_CBManager
+ _notify_cancel
+ _objc_msgSend$authorization
+ _objc_msgSend$objectForInfoDictionaryKey:
+ _xpc_bool_get_value
+ _xpc_copy_entitlement_for_self
- GCC_except_table140
- GCC_except_table146
- GCC_except_table164
- GCC_except_table186
- GCC_except_table211
- GCC_except_table223
- GCC_except_table228
- GCC_except_table235
- GCC_except_table249
Functions:
~ -[HCDatabaseManager init] : 292 -> 300
+ +[HCUtilities processCanUseBluetooth]
~ ___25-[HCDatabaseManager init]_block_invoke : 124 -> 120
~ -[HCDatabaseManager dealloc] : 112 -> 136
CStrings:
+ "NSBluetoothAlwaysUsageDescription"
+ "Protected data available; performing deferred database setup"
+ "com.apple.bluetooth.system"
- "Auth changed"
```
