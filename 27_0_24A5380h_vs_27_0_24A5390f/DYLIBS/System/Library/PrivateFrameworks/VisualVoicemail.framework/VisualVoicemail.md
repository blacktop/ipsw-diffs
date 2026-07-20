## VisualVoicemail

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/VisualVoicemail`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-954.0.0.0.0
-  __TEXT.__text: 0x1abfc
-  __TEXT.__objc_methlist: 0x1fc0
-  __TEXT.__cstring: 0xf9f
-  __TEXT.__gcc_except_tab: 0x514
+956.0.0.0.0
+  __TEXT.__text: 0x1b554
+  __TEXT.__objc_methlist: 0x2010
+  __TEXT.__cstring: 0x101b
+  __TEXT.__gcc_except_tab: 0x554
   __TEXT.__const: 0x78
-  __TEXT.__oslogstring: 0x21e0
-  __TEXT.__unwind_info: 0x918
+  __TEXT.__oslogstring: 0x2297
+  __TEXT.__unwind_info: 0x948
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa70
+  __DATA_CONST.__const: 0xb10
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1348
+  __DATA_CONST.__objc_selrefs: 0x1378
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x400
   __DATA_CONST.__got: 0x230
-  __AUTH_CONST.__const: 0x220
+  __AUTH_CONST.__const: 0x240
   __AUTH_CONST.__cfstring: 0x1440
-  __AUTH_CONST.__objc_const: 0x3b78
+  __AUTH_CONST.__objc_const: 0x3b90
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x180

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 778
-  Symbols:   1754
-  CStrings:  352
+  Functions: 790
+  Symbols:   1770
+  CStrings:  359
 
Symbols:
+ -[VMVoicemailManager getQuickSwitchDataCache:]
+ -[VMVoicemailManager getQuickSwitchModeParameterForAccountUUID:error:]
+ -[VMVoicemailManager getQuickSwitchParametersForAccountUUID:error:]
+ GCC_except_table185
+ GCC_except_table188
+ GCC_except_table191
+ GCC_except_table196
+ GCC_except_table210
+ GCC_except_table216
+ GCC_except_table222
+ GCC_except_table226
+ GCC_except_table229
+ GCC_except_table240
+ GCC_except_table252
+ GCC_except_table255
+ ___46-[VMVoicemailManager getQuickSwitchDataCache:]_block_invoke
+ ___67-[VMVoicemailManager getQuickSwitchParametersForAccountUUID:error:]_block_invoke
+ ___70-[VMVoicemailManager getQuickSwitchModeParameterForAccountUUID:error:]_block_invoke
+ ___block_descriptor_48_e8_32r40r_e20_v20?0"NSArray"8B16lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e23_v28?0B8Q12"NSError"20lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e32_v28?0B8"NSArray"12"NSError"20lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e45_v24?0"VMQuickSwitchParameters"8"NSError"16lr32l8r40l8
+ _objc_msgSend$getQuickSwitchDataCacheWithReply:
+ _objc_msgSend$getQuickSwitchModeParameterForAccountUUID:reply:
+ _objc_msgSend$getQuickSwitchParametersForAccountUUID:reply:
- GCC_except_table187
- GCC_except_table192
- GCC_except_table195
- GCC_except_table198
- GCC_except_table217
- GCC_except_table220
- GCC_except_table231
- GCC_except_table237
- GCC_except_table243
CStrings:
+ "Could not get QuickSwitch data cache due to error %@"
+ "Could not get QuickSwitch mode for account %@ due to error %@"
+ "Could not get QuickSwitch parameters for account %@ due to error %@"
+ "v20@?0@\"NSArray\"8B16"
+ "v24@?0@\"VMQuickSwitchParameters\"8@\"NSError\"16"
+ "v28@?0B8@\"NSArray\"12@\"NSError\"20"
+ "v28@?0B8Q12@\"NSError\"20"
```
