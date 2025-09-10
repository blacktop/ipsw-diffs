## AccessibilityUIShared

> `/System/Library/PrivateFrameworks/AccessibilityUIShared.framework/AccessibilityUIShared`

```diff

-3093.32.1.2.0
-  __TEXT.__text: 0x2040
-  __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x210
+3093.32.11.0.0
+  __TEXT.__text: 0x221c
+  __TEXT.__auth_stubs: 0x490
+  __TEXT.__objc_methlist: 0x228
   __TEXT.__cstring: 0x46d
   __TEXT.__oslogstring: 0x119
   __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0x78
-  __TEXT.__unwind_info: 0x104
+  __TEXT.__gcc_except_tab: 0x88
+  __TEXT.__unwind_info: 0x118
   __TEXT.__objc_classname: 0x96
-  __TEXT.__objc_methname: 0xb83
-  __TEXT.__objc_methtype: 0x292
-  __TEXT.__objc_stubs: 0x760
+  __TEXT.__objc_methname: 0xbed
+  __TEXT.__objc_methtype: 0x2f8
+  __TEXT.__objc_stubs: 0x780
   __DATA_CONST.__got: 0x18
-  __DATA_CONST.__const: 0x218
+  __DATA_CONST.__const: 0x268
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6d8
-  __DATA_CONST.__objc_selrefs: 0x228
+  __DATA_CONST.__objc_const: 0x708
+  __DATA_CONST.__objc_selrefs: 0x238
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__cfstring: 0x260
-  __AUTH_CONST.__auth_got: 0x240
-  __DATA.__objc_ivar: 0x34
+  __AUTH_CONST.__auth_got: 0x258
+  __DATA.__objc_ivar: 0x38
   __DATA.__data: 0x110
   __DATA_DIRTY.__const: 0x40
   __DATA_DIRTY.__objc_const: 0x120

   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5842FE57-114A-338E-8DA2-F7A29FFB9566
-  Functions: 64
-  Symbols:   362
-  CStrings:  228
+  UUID: E783FAFB-CA6E-37BF-897E-46AB570E6FA6
+  Functions: 68
+  Symbols:   378
+  CStrings:  235
 
Symbols:
+ -[AXUIMessageSender delegateAccessLock]
+ -[AXUIMessageSender setDelegateAccessLock:]
+ GCC_except_table1
+ GCC_except_table13
+ GCC_except_table22
+ _AX_PERFORM_WITH_LOCK
+ _OBJC_IVAR_$_AXUIMessageSender._delegateAccessLock
+ ___29-[AXUIMessageSender delegate]_block_invoke
+ ___33-[AXUIMessageSender setDelegate:]_block_invoke
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ _objc_msgSend$setDelegateAccessLock:
+ _objc_release_x1
+ _objc_retain
- GCC_except_table14
- GCC_except_table7
CStrings:
+ "T{os_unfair_lock_s=I},N,V_delegateAccessLock"
+ "_delegateAccessLock"
+ "delegateAccessLock"
+ "setDelegateAccessLock:"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "{os_unfair_lock_s=I}16@0:8"

```
